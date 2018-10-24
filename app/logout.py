#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import logging.config
import time


if __name__ == '__main__':
    logging.config.fileConfig('config.ini')
    logger = logging.getLogger(__name__)

    while True:
        logger.debug('this is test message')
        time.sleep(1)
