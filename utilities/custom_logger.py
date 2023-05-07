import logging


class Loggen:
    @staticmethod
    def get_logger():
        logging.basicConfig(filename=r'..\Logs\automation_log.txt', filemode='w', format='%(asctime)s: %(levelname)s: %(message)s: (%(filename)s:%(lineno)s)', datefmt= '%Y-%m-%d %H:%M:%S', level=logging.INFO)
        return logging.getLogger()