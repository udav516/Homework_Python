import logging

def log_add(string):
    logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', filename="log.txt")
    logging.warning(string)

