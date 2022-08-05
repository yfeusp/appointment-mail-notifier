import smtplib
from socket import gaierror
from unittest.mock import patch

import pytest

from notifier.exceptions import (
    InvalidMailCredentialsError,
    InvalidRecipientError,
    HostOrPortFailedConnectionError,
)
from notifier.mail_sender import MailSender

kwargs = {
    "subject": "Subject Test",
}


def test_should_the_send_mail_method_be_called_successfully():
    config = {
        "smtp_username": "valid_username",
        "smtp_password": "valid_password",
        "email_recipient": "valid_recipient",
        "smtp_host": "valid_host",
        "smtp_port": "valid_port",
    }
    mail_sender = MailSender(config)
    with patch("smtplib.SMTP_SSL", autospec=True) as mock_smtp:
        mail_sender.send(**kwargs)

        mock_smtp.assert_called()
        context = mock_smtp.return_value
        assert context.return_value._login_smtp.return_value
        assert context.login.called.__eq__(True)
        assert context.send_message.called.__eq__(True)


def test_should_throw_invalid_mail_credentials_error():
    config = {
        "smtp_username": "invalid_username",
        "smtp_password": "invalid_password",
        "email_recipient": "valid_recipient",
        "smtp_host": "valid_host",
        "smtp_port": "valid_port",
    }
    mail_sender = MailSender(config)
    with patch("smtplib.SMTP_SSL", autospec=True) as mock_smtp:
        context = mock_smtp.return_value
        context.login.side_effect = smtplib.SMTPAuthenticationError({}, msg="")
        with pytest.raises(
            InvalidMailCredentialsError,
            match="Invalid mail credentials",
        ):
            mail_sender.send(**kwargs)


def test_should_throw_invalid_recipient_error():
    config = {
        "smtp_username": "valid_username",
        "smtp_password": "valid_password",
        "email_recipient": "invalid_recipient",
        "smtp_host": "valid_host",
        "smtp_port": "valid_port",
    }
    mail_sender = MailSender(config)
    with patch("smtplib.SMTP_SSL", autospec=True) as mock_smtp:
        context = mock_smtp.return_value
        context.send_message.side_effect = smtplib.SMTPRecipientsRefused({})
        with pytest.raises(
            InvalidRecipientError,
            match="Invalid recipient.",
        ):
            mail_sender.send(**kwargs)


def test_should_throw_host_or_port_failed_connection_error():
    config = {
        "smtp_username": "valid_username",
        "smtp_password": "valid_password",
        "email_recipient": "valid_recipient",
        "smtp_host": "invalid_host",
        "smtp_port": "invalid_port",
    }
    mail_sender = MailSender(config)
    with patch("smtplib.SMTP_SSL", autospec=True) as mock_smtp:
        mock_smtp.side_effect = gaierror()
        with pytest.raises(
            HostOrPortFailedConnectionError,
            match="SMTP host or port could not connect with the server.",
        ):
            mail_sender.send(**kwargs)
