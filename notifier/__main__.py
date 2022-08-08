import time

from notifier import config
from notifier.config import waiting_time
from notifier.daily_notifier import DailyNotifier
from notifier.mail_notifier import MailNotifier

mail_notifier = MailNotifier(config.site_url, config.email)
daily_notifier = DailyNotifier(config.email)


def main():
    while True:
        # Appointment notifier
        mail_notifier.handle()
        # Daily notifier
        daily_notifier.handle()
        # Wait
        time.sleep(waiting_time)


if __name__ == "__main__":
    main()
