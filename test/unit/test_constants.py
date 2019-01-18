"""Constants used for unit tests.

This can be used to define values for environment variables so unit tests can use these to assert on expected values.
"""

SLACK_URL = 'url'

EVENT = [
    "message1",
    "message2",
    "message3"
]

INVALID_EVENT = {
    "message": "body"
}
