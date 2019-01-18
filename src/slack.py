"""Functions for interacting with slack."""
import json
import requests

import lambdalogging

LOG = lambdalogging.getLogger(__name__)
JSON_HEADER = {'Content-Type': 'application/json'}


def post_message(url, message):
    """Post a message to slack using a webhook url."""
    data = {'text': message}
    response = requests.post(url, data=json.dumps(data), headers=JSON_HEADER)
    LOG.info('Sent message: %s\nUrl: %s\nResponse: %s', message, url, response)
    return response.status_code
