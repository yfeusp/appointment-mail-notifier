from unittest.mock import patch

from notifier.__main__ import main
from notifier.__main__ import MailNotifier, DailyNotifier


@patch.object(MailNotifier, "handle")
@patch.object(DailyNotifier, "handle")
def test_should_run_main_function_successfully(daily_mock, mail_mock):
    main(1)
    daily_mock.assert_called()
    mail_mock.assert_called()


@patch.object(MailNotifier, "handle")
@patch.object(DailyNotifier, "handle")
def test_should_handle_exception_successfully(
    daily_mock, mail_mock, logger, caplog
):
    mail_mock.side_effect = Exception
    main(1)
    daily_mock.assert_not_called()
    assert "An exception has occurred with" in caplog.text
