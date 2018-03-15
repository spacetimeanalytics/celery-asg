# -*- coding: utf-8 -*-
"""
Celery ASG

Usage:
  celery-asg --asg-name=<auto-scaling-group-name> --broker=<celery-broker-url> [--queue=<queue-name>] [--dry-run]

Options:
  -h --help      Show this screen.
  --version      Show version.
"""

from docopt import docopt
from celeryasg import __version__
from celeryasg.core import CeleryASG


def run(asg_name, broker, queue_name, dryrun=False):
    celery = CeleryASG(asg_name=asg_name, broker=broker)
    inactive_instances = celery.find_inactive_instances()
    for instance in inactive_instances:
        print('Shuting down: {}'.format(instance['InstanceId']))
        celery.shutdown_instance(instance, dryrun=dryrun)

    print('Auto balancing ASG...')
    n = celery.auto_balance(dryrun=dryrun)
    if n:
        print('Desired changed to {}'.format(n))


def entrypoint():
    args = docopt(__doc__, version=__version__)

    run(args['--asg-name'],
        args['--broker'],
        args['--queue'],
        args['--dry-run'])


if __name__ == '__main__':
    entrypoint()
