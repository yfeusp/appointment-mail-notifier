from threading import Thread

from appointment_mail_notifier import config
from appointment_mail_notifier.api import main_api
from appointment_mail_notifier.notifier.daily_notifier import DailyNotifier
from appointment_mail_notifier.loggin import get_logger
from appointment_mail_notifier.notifier.mail_notifier import MailNotifier

logger = get_logger()
mail_notifier = MailNotifier(config.site_url, config.email)
daily_notifier = DailyNotifier(config.email)


def run_notifiers():
    Thread(target=mail_notifier.start).start()
    Thread(target=daily_notifier.start).start()


def run_api():
    main_api.run()


def main():
    run_notifiers()
    run_api()


if __name__ == "__main__":
    main()
