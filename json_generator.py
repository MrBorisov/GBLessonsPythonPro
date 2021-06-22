import json
import datetime, time


def presence():
    """конвертим в json """
    dt = datetime.datetime.now()
    value = datetime.datetime.fromtimestamp(time.mktime(dt.timetuple()))
    presence_msg = {
        "action": "presence",
        "time": value.strftime('%Y-%m-%d %H:%M:%S')

    }

    return json.dumps(presence_msg)


def response_decode(msg):
    return json.loads(msg)
