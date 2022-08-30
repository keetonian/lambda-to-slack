"""Constants used for unit tests.

This can be used to define values for environment variables so unit tests can use these to assert on expected values.
"""

SLACK_URL = "url"
CLOUD_WATCH_MESSAGE = {
    "id": "37058205370587177265792648364803499693132537380611555368",
    "timestamp": 1661747400846,
    "message": '{"log":"2022-08-29 04:30:00,846 - model_gw.app.model_executors.base.base_model_executor - ERROR - error_code: 400, msg: No market_name Lol-Pre-BetterKda-TeamPos ., desc: None\\n","stream":"stderr","kubernetes":{"pod_name":"model-orch-6c58dc9896-bmzxh","namespace_name":"odds-maker","pod_id":"a494f95c-b380-4356-a62f-fb6ca65e8eb4","host":"ip-10-19-131-210.ec2.internal","container_name":"model-orch","docker_id":"35c4faa09de60e60163933b5eebf687d534fcb2a5d4abc527de6a1c49631f1e9","container_hash":"551660765733.dkr.ecr.us-east-1.amazonaws.com/dsodds-model-orchestration-serv@sha256:7a7f622a9afcaa8c448752393ce92f6c7009073905c402779184fa78a47d839b","container_image":"551660765733.dkr.ecr.us-east-1.amazonaws.com/dsodds-model-orchestration-serv:e94aaf12a85a3e8463f5d0222100024a69e80721"}}',
}

EVENT = ["message1", "message2", "message3"]

INVALID_EVENT = {"message": "body"}
