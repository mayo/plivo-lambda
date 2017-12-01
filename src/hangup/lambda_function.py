from __future__ import print_function

import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

import urlparse
import plivoxml

print('Loading function')

def lambda_handler(event, context):
    logger.info('got event{}'.format(event))

    if not event['body']:
        raise Exception('No parameters provided')

    params = urlparse.parse_qsl(event['body'], keep_blank_values=True)

    return ''
    #raise Exception('Something went wrong')

