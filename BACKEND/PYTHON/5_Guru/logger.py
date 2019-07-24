'''
import logging
# print(dir(logging))

logger = logging.getLogger()
handler = logging.StreamHandler()
formatter = logging.Formatter(
        '%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

logger.debug('often makes a very good meal of %s', 'visiting tourists')
'''


'''
import logging
logging.basicConfig(level=logging.DEBUG)
logger=logging.getLogger(__name__)

logger.info("start reading database")
#read database here
records={'john':33,'tom':55}
logger.debug('Records:%s',records)
logger.info('Updating Records...')
#update logs here
logger.info("Finish updating records")
'''


#   You can also decide how these messages are processed.
#   For example, you can use a FileHandler to write records to a file.

'''
import logging

logger=logging.getLogger(__name__)
logger.setLevel(logging.INFO)

#create a File Handler
handler=logging.FileHandler('hello.log')
handler.setLevel(logging.INFO)

# create a logging Format
formatter=logging.Formatter("%(asctime)s-%(name)s-%(levelname)s-%(message)s")
handler.setFormatter(formatter)

#add the handlers to the logger
logger.addHandler(handler)

logger.info("Hello baby")
'''


'''
import logging
import smtplib
import os
import sys

def complex_algorithm(items):
    for i,item in enumerate(items):
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)
        logger.debug("%s iteration, item=%s",i,item)

        def handler_request(request):
            logger.info("Handling request %s",request)

            result='result'
            logger.info("Return Result:%s",result)

        def start_service():
            logger.info("starting service at port %s...",port)
            service.start()
            logger.info("Service is Started")
'''


'''
import logging
import logging.config

logger = logging.getLogger(__name__)

# load config from file
# logging.config.fileConfig('logging.ini', disable_existing_loggers=False)
# or, for dictConfig
logging.config.dictConfig({
    'version': 1,
    'disable_existing_loggers': False,  # this fixes the problem
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
    },
    'handlers': {
        'default': {
            'level':'INFO',
            'class':'logging.StreamHandler',
        },
    },
    'loggers': {
        '': {
            'handlers': ['default'],
            'level': 'INFO',
            'propagate': True
        }
    }
})

logger.info('It works!')

'''



'''
import logging

def foo():
    logger = logging.getLogger(__name__)
    logger.info('Hi, foo')

class Bar(object):
    def __init__(self, logger=None):
        self.logger = logger or logging.getLogger(__name__)


    def bar(self):
        self.logger.info('Hi, bar')
'''


'''
import os
import json
import logging.config

def setup_logging(
    default_path='logging.json',
    default_level=logging.INFO,
    env_key='LOG_CFG'
):
    """Setup logging configuration

    """
    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = json.load(f)
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)
'''



'''
import os
import logging.config

# import yaml

def setup_logging(
    default_path='logging.yaml',
    default_level=logging.INFO,
    env_key='LOG_CFG'
):
    """Setup logging configuration

    """
    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)
        
'''


"""
import os
import logging.config

import yaml

def setup_logging(
    default_path='logging.yaml',
    default_level=logging.INFO,
    env_key='LOG_CFG'
):
    
    # Setup logging configuration
    
    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)
"""
import logging

a = 5
b = 0

try:
  c = a / b
except Exception as e:
  logging.error("Exception occurred", exc_info=True)

import logging

logger=logging.getlogger('example_logger')
logger.warning("This is warning")