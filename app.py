from flask import Flask, request, jsonify
import requests
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import os
import logging

app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

Slack_TOKEN = os.environ.get('SLACK_TOKEN')
CHATGPT_API_KEY = os.environ.get('CHATGPT_API_KEY')

@app.route('/slack/command', methods=['POST'])
def chatgpt():
    # Get the user input from the request (this is the conversation from the slash command)
    user_input = request.form.get('text')
    channel_id = request.form.get('channel_id')
    logging.debug("channel_id: %s", channel_id)

    # Initialize the Slack API client
    client = WebClient(token=Slack_TOKEN)
    
    # Retrieve the conversation history from the Slack channel
    response = client.conversations_history(channel=channel_id)
    logging.debug("response: %s", response)
    if response["ok"]:
        messages = response["messages"]
        conversation = '\n'.join([message["text"] for message in messages if "text" in message])
        user_input = f"{user_input}\n\n{conversation}"
    else:
        print("Error occurred while retrieving chat history:", response["error"])
        return jsonify({"response_type": "ephemeral", "text": "Failed to retrieve chat history."})

    # Prepare the API request
    headers = {
        'Authorization': f'Bearer {CHATGPT_API_KEY}',
        'Content-Type': 'application/json'
    }

    data = {
        'model': 'gpt-3.5-turbo',
        'messages': [{'role': 'system', 'content': 'You are a helpful assistant.'}, {'role': 'user', 'content': user_input}]
    }

    # Send the API request
    response = requests.post('https://api.openai.com/v1/chat/completions', headers=headers, json=data, timeout=120)

    # Get the generated response from ChatGPT
    api_response = response.json()
    if 'choices' in api_response:
        generated_response = api_response['choices'][0]['message']['content']
    else:
        # Handle the case where 'choices' key is missing
        print("Error: 'choices' key not found in API response.")
        return jsonify({"response_type": "ephemeral", "text": "Failed to get a valid response from the API."})


    # Send the message to Slack
    try:
        response = client.chat_postMessage(channel=channel_id, text=generated_response)
        print("Message sent successfully!")
    except SlackApiError as e:
        print(f"Error sending message to Slack: {e.response['error']}")
        return jsonify({"response_type": "ephemeral", "text": "Failed to send response to Slack."})

    return jsonify({"response_type": "in_channel", "text": "Your request is being processed."})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))