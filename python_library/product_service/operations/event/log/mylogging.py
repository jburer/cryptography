import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s : %(created)f : %(filename)s : %(funcName)s : %(pathname)s : %(process)d : %(name)s : %(lineno)d', level=logging.DEBUG)
logging.debug('This message should appear on the console')
logging.info('So should this')
logging.warning('And this, too')