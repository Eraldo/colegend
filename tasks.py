import os
from subprocess import Popen, PIPE
import signal
from time import sleep

from celery.utils.term import colored
from invoke import run as invoke_run, task

project_name = 'colegend'
context = {
    'environment': 'development',
    'branch': 'development',
}


def message(text, *args, **kwargs):
    """
    Displaying a message for the user.
    """
    environment = context.get('environment', '---')
    c = colored(enabled=True)
    print(c.cyan('\n>> [{}] {}'.format(environment, text)), *args, **kwargs)


def local_run(command):
    print('$: {}'.format(command))
    invoke_run(command)


def heroku_run(command='run', parameters=''):
    """
    Running a command for the chosen environment on heroku.
    """
    environment = context.get('environment')
    app = project_name
    if environment == 'staging':
        app += '-staging'
    local_run('heroku {} --app {} {}'.format(command, app, parameters))


def run(command, heroku_command='run', *args, **kwargs):
    """
    Running a command for the chosen environment.
    """
    if context.get('environment') == 'development':
        return local_run('source ~/.virtualenvs/{}/bin/activate && {}'.format(project_name, command))
    elif context.get('environment') in ['staging', 'production']:
        return heroku_run(heroku_command, parameters=command, *args, **kwargs)


def git_push():
    branch = context.get('branch')
    command = 'git push origin {}'.format(branch)
    local_run(command)


@task
def development():
    """
    Setting up development environment. (default)
    """
    context['environment'] = 'development'
    context['branch'] = 'development'


@task
def staging():
    """
    Setting up staging environment.
    """
    context['environment'] = 'staging'
    context['branch'] = 'staging'


@task
def production():
    """
    Setting up production environment.
    """
    context['environment'] = 'production'
    context['branch'] = 'master'


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
def deploy():
    """
    Delopy the app to heroku.
    """
    if context.get('environment') in ['staging', 'production']:
        message('deploying the app')
        maintenance(on=True)
        git_push()
        sleep(30)
        migrate()
        maintenance(off=True)


@task
def maintenance(on=False, off=False):
    """
    Start or stop maintenance:on mode.
    """
    if context.get('environment') in ['staging', 'production']:
        if on:
            message('starting maintenance:on')
            run('', heroku_command='maintenance:on')
        elif off:
            message('stopping maintenance')
            run('', heroku_command='maintenance:off')


@task
def backup():
    """
    Backup the database. (development only)
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
