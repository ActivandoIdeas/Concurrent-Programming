import logging
import time
import threading

logging.basicConfig(
    level=logging.DEBUG,
    format='%(thread)s %(threadName)s : %(message)s'
)


def task():
    logging.info('Execute new task')
    time.sleep(2)
    logging.info('End task')


if __name__ == '__main__':
    logging.debug('Hi, In main thread')
    thread = threading.Thread(target=task)
    thread.start()
