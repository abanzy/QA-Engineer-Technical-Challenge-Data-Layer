import requests
import json
import openai
import pytest
from sentence_transformers import SentenceTransformer, util


# Example LLM judge function using OpenAI API (replace with your provider as needed)
def llm_judge(prompt, response):
    """
    Uses OpenAI API (cheapest model: gpt-3.5-turbo) to score the chatbot response for relevance/accuracy.
    Returns True if the score is high (>=4), False otherwise.
    """
    # Use the environment variable for API key (recommended)
    openai.api_key = "" # Just put your OpenAI key, ideally i would be using os.getenv("OPENAI_API_KEY") but this is just a demonstration, fully functional but just for testing purposes
    system_prompt = (
        "You are an expert assistant for evaluating chatbot responses. "
        # Possible markers for validating a chatbot response would be:
        # Relevance, Coherence, Consistency, Accuracy, Factual Correctness,
        # Conciseness vs. Detail Balance, Tone and Formality, Grammar and Language Use,
        # Creativity and Depth, Safety and Ethical Considerations, User Intent Understanding,
        # Engagement and Interactivity or straight Halucination Detection
        # But for this example, we will just use a simple relevance and helpfulness score
        "Given a user prompt and a chatbot's reply, rate the reply's relevance and helpfulness on a scale from 1 (poor) to 5 (excellent). "
        "Only return the number."
    )
    user_prompt = (
        f"User prompt: {prompt}\n"
        f"Chatbot reply: {response['message'] if isinstance(response, dict) and 'message' in response else str(response)}\n"
        "Score (1-5):"
    )

    try:
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            max_tokens=1,
            temperature=0.0, ## I set temperature to 0 for deterministic responses
        )
        score_str = completion.choices[0].message['content'].strip()
        score = int(score_str[0])  # So it only take the first digit
    except Exception as e:
        print(f"LLM judge API error: {e}")
        score = 1  # Default to fail if API call fails

    print(f"LLM judge score: {score}")
    return score >= 4 # # Return True if score is 4 or higher, indicating a good response, this can be tinked based on your needs or moves to the actualt test cases


# Sample function to run a chatbot test with expected keys and semantics/ not being use just for illustration
def run_chatbot_test(prompt, expected_keys, expected_semantics):
    resp = requests.post('http://localhost:5001/chatbot', json={'prompt': prompt})
    try:
        data = resp.json()
    except Exception:
        print('FAIL: Not valid JSON')
        return False
    # Structure check
    for key in expected_keys:
        if key not in data:
            print(f'FAIL: Missing key {key}')
            return False
    # SBERT semantic check
    model = SentenceTransformer('all-MiniLM-L6-v2')

    # Prefer human message for SBERT and logs if present
    if isinstance(data, dict) and 'message' in data:
        actual_text = data['message']
    elif isinstance(data, dict):
        actual_text = json.dumps(data, separators=(',', ': '), sort_keys=True)
    else:
        actual_text = str(data)

    # SBERT similarity and minimal, concise logging jusr for illustration
    emb1 = model.encode(expected_semantics, convert_to_tensor=True)
    emb2 = model.encode(actual_text, convert_to_tensor=True)
    sim = util.pytorch_cos_sim(emb1, emb2).item()
    print(f"Prompt: {prompt}")
    print(f"Response: {actual_text}")
    print(f"SBERT similarity: {sim:.3f}")
    if sim < 0.4:
        print("FAIL: Semantic similarity too low")
        return sim
    # LLM-as-a-judge
    if not llm_judge(prompt, data):
        print('FAIL: LLM judge failed')
        return sim
    print('PASS')
    return sim


# Individual pytest test cases for LLM validation
def test_llm_last_5_transactions():
    prompt = 'Show me my last 5 transactions.'
    resp = requests.post('http://localhost:5001/chatbot', json={'prompt': prompt})
    data = resp.json()
    assert llm_judge(prompt, data), "LLM judge did not approve the response."

def test_llm_recent_txns():
    prompt = 'Can you list my recent transactions?'
    resp = requests.post('http://localhost:5001/chatbot', json={'prompt': prompt})
    data = resp.json()
    assert llm_judge(prompt, data), "LLM judge did not approve the response."

def test_llm_invalid_location():
    prompt = 'Do I have any transactions from Mars?'
    resp = requests.post('http://localhost:5001/chatbot', json={'prompt': prompt})
    data = resp.json()
    assert llm_judge(prompt, data), "LLM judge did not approve the response."

def test_llm_last_transaction():
    prompt = 'Tell me about my most recent transaction.'
    resp = requests.post('http://localhost:5001/chatbot', json={'prompt': prompt})
    data = resp.json()
    assert llm_judge(prompt, data), "LLM judge did not approve the response."

def test_llm_total_amount():
    prompt = 'What is the total amount from all my transactions?'
    resp = requests.post('http://localhost:5001/chatbot', json={'prompt': prompt})
    data = resp.json()
    assert llm_judge(prompt, data), "LLM judge did not approve the response."
