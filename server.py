import logging

from bottle import request, default_app
from bottle import route
from paste import httpserver


def create_logger(name):
    logger = logging.getLogger(name)
    hdlr = logging.FileHandler('./logs/' + name)
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    hdlr.setFormatter(formatter)
    logger.addHandler(hdlr)
    logger.setLevel(logging.INFO)
    return logger


logger = create_logger("test.txt")


@route('/img/', method='POST')
def main_tracker_request():
    request_json = request.json

    logger.info("receive for " + request_json["img"])

    return {"A": 0.3, "B": 0.2}


cur_app = default_app()
httpserver.serve(cur_app, host='0.0.0.1', port=8080, use_threadpool=True, threadpool_workers=20,
                 request_queue_size=100)
