from unittest.mock import patch

from appointment_mail_notifier.__main__ import run_notifiers
from appointment_mail_notifier.__main__ import MailNotifier, DailyNotifier


@patch.object(MailNotifier, "start")
@patch.object(DailyNotifier, "handle")
def test_should_run_notifiers_successfully(daily_mock, mail_mock):
    run_notifiers()
    # daily_mock.assert_called()
    mail_mock.assert_called()


# @patch.object(MailNotifier, "handle")
# @patch.object(DailyNotifier, "handle")
# def test_should_handle_notifiers_exceptions_successfully(
#     daily_mock, mail_mock, logger, caplog
# ):
#     mail_mock.side_effect = Exception
#     run_notifiers(1)
#     daily_mock.assert_not_called()
#     assert "An exception has occurred with" in caplog.text
