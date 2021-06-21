import json
import datetime


def presence():
    """пишем в json файл"""
    presence_msg = {
        "action": "presence",
        "time": 123
        # TODO заменить число датой
    }

    return json.dumps(presence_msg)


def response_decode(msg):
    return json.loads(msg)
