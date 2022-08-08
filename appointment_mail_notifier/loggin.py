import logging

from appointment_mail_notifier.config import log_config


def get_logger():
    logger = logging.getLogger(log_config["log_name"])
    log_level = log_config["log_level"]
    if not logger.handlers:
        logger.setLevel(log_level)
        ch = logging.StreamHandler()
        ch.setLevel(log_level)
        ch.setFormatter(logging.Formatter(log_config["log_format"]))
        logger.addHandler(ch)
    return logger
