#!/bin/bash

API_URL="http://localhost:5000/api/timeline_post"

echo "Testing Timeline post api endpoint"

TEST_NAME="John Bao"
TEST_EMAIL="123@gmail.com"
# using date to get the current date
TEST_CONTENT="This is a testing post created at $(date) calling: You have tested it"

echo -e "Step 1: Testing GET endpoint"
echo "Sending GET request to: $API_URL"
INITIAL_RESPONSE=$(curl -s -X GET "$API_URL")
echo "Response: $INITIAL_RESPONSE"

echo "Step 2: Testing POST endpoint"
echo "Sending POST request to: $API_URL"
POST_RESPONSE=$(curl -s -X POST "$API_URL" \
	-H "Content-Type: application/x-www-form-urlencoded" \
	-d "name=$TEST_NAME&email=$TEST_EMAIL&content=$TEST_CONTENT")
echo "POST RESPONSE = $POST_RESPONSE"


# testing if the end point was successful
if [[ $POST_RESPONSE  == *"$TEST_NAME"* ]]; then
	echo -e "POST Request was successful"
	POST_SUCCESS=true
else
	echo -e "POST Request failed"
	POST_SUCCESS=false
fi

