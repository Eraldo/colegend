import os
from subprocess import Popen, PIPE
import signal

from celery.utils.term import colored
from invoke import run as invoke_run, task

project_name = 'colegend'
context = {
    'environment': 'development',
}


def message(text, *args, **kwargs):
    environment = context.get('environment', '---')
    c = colored(enabled=True)
    print(c.cyan('\n>> [{}] {}'.format(environment, text)), *args, **kwargs)


def run(command, *args, **kwargs):
    print('$: {}'.format(command))
    if context.get('environment') == 'development':
        return invoke_run('source ~/.virtualenvs/{}/bin/activate && {}'.format(project_name, command))
    elif context.get('environment') == 'staging':
        return invoke_run('heroku run --app {}-staging {}'.format(project_name, command), *args, **kwargs)
    elif context.get('environment') == 'production':
        return invoke_run('heroku run --app {} {}'.format(project_name, command), *args, **kwargs)


@task
def development():
    """
    Setting up development environment. (default)
    """
    context['environment'] = 'development'


@task
def staging():
    """
    Setting up staging environment.
    """
    context['environment'] = 'staging'


@task
def production():
    """
    Setting up production environment.
    """
    context['environment'] = 'production'


@task
def environment():
    """
    Show the task environment.
    """
    message('Context: ', context)


@task
def migrate():
    """
    Migrate the database.
    """
    message('migrating database')
    run('./manage.py migrate')


@task
def backup():
    """
    Backup the database. (development only)
    :return:
    """
    if context.get('environment') == 'development':
        message('backing up database')
        run('pg_dump -Fc {project} > backups/{project}_`date +%Y-%m-%d_%H%M%S`.dump'.format(project=project_name))


@task
def serve():
    """
    Starting the development server.
    """
    if context.get('environment') == 'development':
        message('Starting server')
        process = Popen(['python', './manage.py', 'runserver'], stdout=PIPE, preexec_fn=os.setsid, shell=True)
        input('press any key to stop the server')
        os.killpg(os.getpgid(process.pid), signal.SIGTERM)
    else:
        run('./manage.py runserver')


@task
def ls(path):
    """
    List the specified directory.
    :param path: The path to list.
    """
    command = 'ls {}'.format(path)

    message('listing directory')
    run(command)
