from celery import task


@task()
def demo():
    print 'celery crontab running...'
