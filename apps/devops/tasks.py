# ~*~ coding: utf-8 ~*~
from celery import shared_task
import json
from .utils import run_AdHoc
from ansible.cli.galaxy import GalaxyCLI


@shared_task
def ansible_install_role(role_name):
    task_tuple = []
    #: 新建一个任务列表  执行shell 任务
    task_tuple.extend([
        ('shell', 'ansible-galaxy install -f {}'.format(role_name))
    ])
    #: Task Name
    task_name = 'ansible-galaxy Install Role {}'.format(role_name)

    summary, result = run_AdHoc(task_tuple, pattern='all',
                                task_name=task_name)
    #: 失败返回0 成功返回1
    if summary['failed']:
        return False
    return True