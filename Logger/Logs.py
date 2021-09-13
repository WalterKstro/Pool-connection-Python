import logging as log

log.basicConfig(level=log.INFO, format='%(asctime)s: %(levelname)s: [%(filename)s:%(lineno)s]: %(message)s',
                datefmt='%d/%m/%Y %I:%M:%S %p',
                handlers=[ log.FileHandler('logs.txt'), log.StreamHandler()])
