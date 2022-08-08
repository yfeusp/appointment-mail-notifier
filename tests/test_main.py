from unittest.mock import patch

from appointment_mail_notifier.__main__ import run_notifiers
from appointment_mail_notifier.__main__ import MailNotifier, DailyNotifier


@patch.object(MailNotifier, "start")
@patch.object(DailyNotifier, "start")
def test_should_run_notifiers_successfully(daily_mock, mail_mock):
    run_notifiers()
    daily_mock.assert_called()
    mail_mock.assert_called()
