from __future__ import print_function

import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

import urlparse
import plivoxml

class HangupException(Exception): pass

def lambda_handler(event, context):
    logger.info('got event {}'.format(event))

    if 'body' not in event:
        raise HangupException('No call parameters provided')

    if 'Number' not in event['params']:
        raise HangupException('No destination number provided')

    params = dict(urlparse.parse_qsl(event['body'], keep_blank_values=True))

    logger.info('got parameters: {}'.format(params))

    response = plivoxml.Response()
    dial = response.addDial(callerId=params.get('From'))
    dial.addNumber(event['params'].get('Number'))


    return response.to_xml()

