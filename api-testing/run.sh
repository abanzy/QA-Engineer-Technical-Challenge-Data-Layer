#!/bin/bash
COLLECTION="api-tests.postman_collection.json"
ENVIRONMENT="mock-environment.json"
REPORT_DIR="../reports"
mkdir -p $REPORT_DIR
newman run $COLLECTION -e $ENVIRONMENT --reporters cli,html,json --reporter-html-export $REPORT_DIR/newman-report.html --reporter-json-export $REPORT_DIR/newman-report.json
