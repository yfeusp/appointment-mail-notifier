import pytest
import logging

from appointment_mail_notifier.config import log_config


@pytest.fixture()
def logger():

    logger = logging.getLogger(log_config["log_name"])
    logger.setLevel(logging.INFO)

    return logger
