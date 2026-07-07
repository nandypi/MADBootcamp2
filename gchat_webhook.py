from json import dumps
from httplib2 import Http

from dotenv import load_dotenv
load_dotenv()

import os

# Copy the webhook URL from the Chat space where the webhook is registered.
# The values for SPACE_ID, KEY, and TOKEN are set by Chat, and are included
# when you copy the webhook URL.

def main(msg="Hello from a Python script!"):
    """Google Chat incoming webhook quickstart."""
    url = os.getenv("GSPACE_WEBHOOK")
    app_message = {
        "text": msg
    }
    message_headers = {"Content-Type": "application/json; charset=UTF-8"}
    http_obj = Http()
    response = http_obj.request(
        uri=url,
        method="POST",
        headers=message_headers,
        body=dumps(app_message),
    )
    print(response)


if __name__ == "__main__":
    main(msg="Hey, MAD2 Bootcamp students! Welcome to Google Chat Webhook integration with Python.")