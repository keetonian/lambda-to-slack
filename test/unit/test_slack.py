import json
from collections import namedtuple

import pytest
import requests
import slack

import test_constants


def test_publish_message(mocker):
    mocker.patch.object(requests, "post")
    response = namedtuple("response", "status_code")
    response.status_code = 200
    requests.post.return_value = response
    slack.post_message(test_constants.SLACK_URL, json.dumps(test_constants.CLOUD_WATCH_MESSAGE))
