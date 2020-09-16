import logging

# Debug (10)
# Info (20)
# Warning (30)
# Error (40)
# Critical (50)

logging.basicConfig(
    level=logging.DEBUG,  # 10
    format='%(filename)s %(asctime)s %(message)s %(funcName)s %(levelname)s %(lineno)s %(module)s %(name)s %(pathname)s %(thread)s %(threadName)s %(process)s %(processName)s',
    datefmt='%H:%M:%S',
    # filename='logging/messages.txt'
)


def messages():
    logging.debug('This is a debug message')
    logging.info('This is a info message')
    logging.warning('This is a warning message')
    logging.error('This is a error message')
    logging.critical('This is a critical message')


if __name__ == '__main__':
    messages()
