import logging
import os
import datetime

logger = logging.getLogger('ksp')
logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

if not os.path.exists('log'):
    os.mkdir('log')
log_file_name = datetime.datetime.now().strftime('%Y-%m-%d') + '.log'
log_file_path = os.path.join('log', log_file_name)
file_handler = logging.FileHandler(log_file_path, mode='a')
file_handler.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s | %(levelname)-8s | %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(console_handler)
logger.addHandler(file_handler)

# logger.debug('debug message')
# logger.info('info message')
# logger.warning('warning message')
# logger.error('error message')
# logger.critical('critical message')