import logging
import time
import random
from django.conf import settings
from django.core.cache import cache
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from django.core.management.base import BaseCommand
from django_apscheduler.jobstores import DjangoJobStore
from django_apscheduler.models import DjangoJobExecution
import mysql.connector
from dingtalkchatbot.chatbot import DingtalkChatbot
from django.core.management import call_command
logger = logging.getLogger('django')


def dingding(mobile, text):
    webhook = 'https://oapi.dingtalk.com/robot/send?' \
              'access_token=da5e3827feba9cb2eed57dfb2a4d6272d92c6a331f377931f6e801a97b3f55ae'
    xiaoding = DingtalkChatbot(webhook)
    xiaoding.send_markdown(title='禅道通知', text=text, at_mobiles=[mobile])


def notice_bug():
    logger.info('通知未解决的bug')
    cnx = mysql.connector.connect(user='root', password='JFwlkj2018!', buffered=True,
                                  host='192.168.40.159', database='zentaopms')
    users = cnx.cursor()
    bugs = cnx.cursor()

    users_sql = "SELECT u.realname, b.assignedTo, u.mobile, count(*) num FROM zt_bug b  \
                LEFT JOIN zt_product p ON b.product = p.id \
                LEFT JOIN zt_user u ON b.assignedTo = u.account \
                WHERE b.deleted = '0' AND b.status = 'active' AND p.status='normal' \
                      AND p.deleted='0' AND u.deleted = '0' \
                GROUP BY u.realname \
                ORDER BY num DESC"
    users.execute(users_sql)

    report_text = '# 禅道 bug 统计 \n------\n'
    i = 0
    for u in users:
        i = i + 1
        realname = u[0]
        account = u[1]
        mobile = u[2]
        count = u[3]

        report_text = report_text + '%s. %s: %s \n' % (i, realname, count)

        bug_sql = "SELECT b.title, b.assignedTo FROM zt_bug b LEFT JOIN zt_product p ON b.product = p.id \
                   WHERE b.deleted = '0' \
                   AND b.`status` = 'active'  \
                   AND p.`status` = 'normal' \
                   AND p.deleted = '0' \
                   AND b.assignedTo = '%s'" % account
        bugs.execute(bug_sql)

        bug_text = '# %s %s 个 bug 未解决 \n------\n' % (realname, count)
        for b in bugs:
            bug_text = bug_text + '- %s \n' % b[0]

        dingding(mobile, bug_text)
        time.sleep(3)

    dingding('18682077880', report_text)
    users.close()
    bugs.close()
    cnx.close()


def delete_old_job_executions(max_age=604_800):
    logger.info('清理定时任务执行记录')
    DjangoJobExecution.objects.delete_old_job_executions(max_age)


def check_schedule():
    logger.info('定时器运行中 ...')


def clear_token():
    logger.info('从数据库中删除过期 token')
    call_command('cleartokens')


def handle_schedule():
    scheduler = BackgroundScheduler(timezone=settings.TIME_ZONE)
    scheduler.add_jobstore(DjangoJobStore(), "default")

    logger.info("开始启动定时器 ...")
    scheduler.start()

    scheduler.add_job(
        notice_bug,
        trigger=CronTrigger(day_of_week='mon-fri', hour="20", minute="00", second="00"),
        id="notice_bug",
        max_instances=1,
        # 如果任务已经存在了，就替换
        replace_existing=True,
    )

    scheduler.add_job(
        delete_old_job_executions,
        trigger=CronTrigger(day_of_week='mon', hour="01", minute="00", second="00"),
        id="delete_old_job_executions",
        max_instances=1,
        replace_existing=True,
    )

    scheduler.add_job(
        clear_token,
        trigger=CronTrigger(hour="01", minute="30", second="00"),
        id="clear_token",
        max_instances=1,
        replace_existing=True,
    )

    scheduler.add_job(
        check_schedule,
        trigger=CronTrigger(minute="*/30"),
        id="check_schedule",
        max_instances=1,
        replace_existing=True,
    )


class Command(BaseCommand):
    def handle(self, *args, **options):

        lock_name = 'scheduler_lock'
        sleep_time = random.uniform(0, 9)
        logger.info('等待时间: %f s' % sleep_time)
        time.sleep(sleep_time)
        lock = cache.get(lock_name)

        if lock is None:
            cache.set(lock_name, "lock", timeout=30)
            handle_schedule()
        else:
            logger.info('定时器已经在运行')
