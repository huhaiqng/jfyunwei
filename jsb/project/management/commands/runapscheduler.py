import logging
import time
from django.conf import settings
from django.core.cache import cache
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from django.core.management.base import BaseCommand
from django_apscheduler.jobstores import DjangoJobStore
from django_apscheduler.models import DjangoJobExecution
import mysql.connector
from dingtalkchatbot.chatbot import DingtalkChatbot
logger = logging.getLogger('django')


def dingding(u, bugs):
    realname = u[0]
    mobile = u[2]
    count = u[3]

    bug_text = '# %s还有 %s 个 bug 未关闭 \n------\n' % (realname, count)

    for b in bugs:
        bug_text = bug_text + '- %s \n' % b[0]

    webhook = 'https://oapi.dingtalk.com/robot/send?' \
              'access_token=da5e3827feba9cb2eed57dfb2a4d6272d92c6a331f377931f6e801a97b3f55ae'
    xiaoding = DingtalkChatbot(webhook)
    xiaoding.send_markdown(title='禅道通知', text=bug_text, at_mobiles=[mobile])


def notice_bug():
    cnx = mysql.connector.connect(user='root', password='JFwlkj2018!', buffered=True,
                                  host='192.168.40.159', database='zentaopms')
    users = cnx.cursor()
    bugs = cnx.cursor()

    users_sql = "SELECT u.realname, b.assignedTo, u.mobile, count(*) num FROM zt_bug b  \
                LEFT JOIN zt_product p ON b.product = p.id \
                LEFT JOIN zt_user u ON b.assignedTo = u.account \
                WHERE b.deleted = '0' AND b.status = 'active' AND p.status='normal' AND p.deleted='0' \
                GROUP BY u.realname \
                ORDER BY b.assignedDate"

    users.execute(users_sql)
    for u in users:
        account = u[1]

        bug_sql = "SELECT b.title, b.assignedTo FROM zt_bug b LEFT JOIN zt_product p ON b.product = p.id \
                   WHERE b.deleted = '0' \
                   AND b.`status` = 'active'  \
                   AND p.`status` = 'normal' \
                   AND p.deleted = '0' \
                   AND b.assignedTo = '%s'" % account

        bugs.execute(bug_sql)
        dingding(u, bugs)
        time.sleep(3)

    users.close()
    bugs.close()
    cnx.close()


def delete_old_job_executions(max_age=604_800):
    """This job deletes all apscheduler job executions older than `max_age` from the database."""
    DjangoJobExecution.objects.delete_old_job_executions(max_age)


def check_schedule():
    logger.info('定时器运行中...')


class Command(BaseCommand):
    def handle(self, *args, **options):
        scheduler = BackgroundScheduler(timezone=settings.TIME_ZONE)
        scheduler.add_jobstore(DjangoJobStore(), "default")

        scheduler.add_job(
            notice_bug,
            trigger=CronTrigger(day_of_week='mon-fri', hour="18", minute="00", second="00"),
            id="notice_bug",
            max_instances=1,
            # 如果任务已经存在了，就替换
            replace_existing=True,
        )

        scheduler.add_job(
            delete_old_job_executions,
            trigger=CronTrigger(hour="00", minute="00"),
            id="delete_old_job_executions",
            max_instances=1,
            replace_existing=True,
        )

        scheduler.add_job(
            check_schedule,
            trigger=CronTrigger(minute="*/10"),
            id="check_schedule",
            max_instances=1,
            replace_existing=True,
        )

        try:
            lock_name = 'scheduler_lock'
            lock = cache.get(lock_name)

            if lock is None:
                cache.set(lock_name, "lock", timeout=30)
                logger.info("开始启动 scheduler...")
                scheduler.start()
        except KeyboardInterrupt:
            logger.info("Stopping scheduler...")
            scheduler.shutdown()
            logger.info("Scheduler shut down successfully!")
