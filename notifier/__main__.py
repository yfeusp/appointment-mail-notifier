import time

from notifier import config
from notifier.config import waiting_time
from notifier.mail_notifier import MailNotifier


def main():
    while True:
        mail_notifier = MailNotifier(config.site_url, config.email)
        mail_notifier.handle()
        time.sleep(waiting_time)


if __name__ == "__main__":
    main()
