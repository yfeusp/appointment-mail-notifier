from datetime import datetime
from unittest.mock import MagicMock

from appointment_mail_notifier.notifier.daily_notifier import DailyNotifier

mail_config = {
    "smtp_username": "valid_username",
    "smtp_password": "valid_password",
    "email_recipient": "valid_recipient",
    "smtp_host": "valid_host",
    "smtp_port": "valid_port",
}


def test_should_daily_notify_successfully(logger, caplog):
    daily_notifier = DailyNotifier(mail_config)
    daily_notifier.email_sender.send = MagicMock(name="send")
    daily_notifier.start(number_of_iterations=1)
    daily_notifier.email_sender.send.called.__eq__(True)
    assert "Daily Notification" in caplog.text


def test_should_not_daily_notify_twice(logger, caplog):
    daily_notifier = DailyNotifier(mail_config)
    daily_notifier.days = [datetime.now().strftime("%d-%m-%Y")]
    daily_notifier.email_sender.send = MagicMock(name="send")
    daily_notifier.start(number_of_iterations=1)
    daily_notifier.email_sender.send.called.__eq__(False)
    assert "Daily Notification" not in caplog.text


def test_should_raise_an_exception_when_email_is_not_sent(logger, caplog):
    daily_notifier = DailyNotifier(mail_config)
    daily_notifier.email_sender.send = MagicMock(side_effect=Exception)
    daily_notifier.start(number_of_iterations=1)
    daily_notifier.email_sender.send.called.__eq__(False)
    assert "An exception has occurred with" in caplog.text
