import requests_mock
from unittest.mock import MagicMock

from notifier.mail_notifier import MailNotifier

mail_config = {
    "smtp_username": "valid_username",
    "smtp_password": "valid_password",
    "email_recipient": "valid_recipient",
    "smtp_host": "valid_host",
    "smtp_port": "valid_port",
}
site_url = "http://url.com"


def test_should_notify_when_appointment_is_available(logger, caplog):
    with requests_mock.Mocker() as mock:
        mail_notifier = MailNotifier(site_url, mail_config)
        mail_notifier.email_sender.send = MagicMock(name="send")
        mock.get(site_url, text='[{"id":123}]')
        mail_notifier.handle()
        mail_notifier.email_sender.send.called.__eq__(True)
        assert "Appointment available" in caplog.text


def test_should_not_notify_when_appointment_is_not_available(logger, caplog):
    with requests_mock.Mocker() as mock:
        mail_notifier = MailNotifier(site_url, mail_config)
        mail_notifier.email_sender.send = MagicMock(name="send")
        mock.get(site_url, text="[]")
        mail_notifier.handle()
        mail_notifier.email_sender.send.called.__eq__(False)
        assert "Appointment not available" in caplog.text
