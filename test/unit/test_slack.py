from collections import namedtuple
import slack
import requests
import pytest
import test_constants


def test_publish_message(mocker):
    mocker.patch.object(requests, 'post')
    response = namedtuple('response', 'status_code')
    response.status_code = 200
    requests.post.return_value = response
    slack.post_message(test_constants.SLACK_URL, 'message')