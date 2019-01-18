import pytest
import handlers
import requests
import slack
from exceptions import InputError

import test_constants


def test_post_to_slack(mocker):
    mocker.patch.object(slack, 'post_message')
    handlers.post_to_slack(test_constants.EVENT, None)
    slack.post_message.assert_any_call(test_constants.SLACK_URL, test_constants.EVENT[0])
    slack.post_message.assert_any_call(test_constants.SLACK_URL, test_constants.EVENT[1])
    slack.post_message.assert_any_call(test_constants.SLACK_URL, test_constants.EVENT[2])

def test_post_to_slack_input_error(mocker):
    mocker.patch.object(slack, 'post_message')
    with pytest.raises(InputError):
        handlers.post_to_slack(test_constants.INVALID_EVENT, None)
