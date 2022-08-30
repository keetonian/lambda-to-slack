"""Functions for interacting with slack."""
import json

import requests

import lambdalogging

LOG = lambdalogging.getLogger(__name__)
JSON_HEADER = {"Content-Type": "application/json"}


def post_message(url, message):
    """Post a message to slack using a webhook url."""
    log_data = json.loads(message)
    log_message = json.loads(log_data["message"])

    slack_payload = {
        "text": f'```{log_message["log"]}```',
        "blocks": [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f'Container Name: `{log_message["kubernetes"]["container_name"]}`\n'
                    f'Container Image: `{log_message["kubernetes"]["container_image"]}`\n',
                },
            }
        ],
    }

    response = requests.post(url, data=json.dumps(slack_payload), headers=JSON_HEADER)
    LOG.info("Sent message: %s\nUrl: %s\nResponse: %s", message, url, response)
    return response.status_code
