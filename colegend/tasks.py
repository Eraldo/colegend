import subprocess

__author__ = 'eraldo'


# SCRIPT SETUP

tasks = {}
domain = ''
env = {}
local_hosts = ['EroBookPro.local']
remote_hosts = ['lepus.uberspace.de']


def task(task_function):
    tasks[task_function.__name__] = task_function
    return task_function


def print_headline(text):
    separator = '=' * 42
    print(separator)
    print(text.upper())
    print(separator)


def print_command(command):
    separator = '-' * 42
    print(separator)
    print(env['host'] + "$ " + command)
    print(separator)
    print()


def run(command, silent=False, hidden=False):
    if not hidden:
        print_command(command)
    output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True, universal_newlines=True)
    if not silent and not hidden:
        print(output)
    return output


def get_host():
    return run('echo $HOSTNAME', hidden=True).rstrip('\n')


def configure():
    host = get_host()
    if host in local_hosts:
        env['domain'] = 'development'
        env['local'] = True
        env['remote'] = False
    elif host in remote_hosts:
        env['domain'] = 'production'
        env['local'] = False
        env['remote'] = True
    else:
        raise Exception("Host '{}' is not supported.".format(host))
    env['host'] = host


# HELPER TASKS

@task
def hello():
    run('echo "hello world"')


@task
def git_pull():
    run('git pull')


@task
def pip_install():
    command = 'pip install -r ../requirements/{}.txt'.format(env['domain'])
    run(command)


@task
def collect_static():
    if env['remote']:
        command = './manage.py collectstatic --noinput'
        command += ' --settings=configuration.settings.{}'.format(env['domain'])
        run(command)


@task
def migrate():
    command = './manage.py migrate'
    if env['remote']:
        command += ' --settings=configuration.settings.{}'.format(env['domain'])
    run(command)


@task
def makemigrations():
    command = './manage.py makemigrations'
    if env['remote']:
        command += ' --settings=configuration.settings.{}'.format(env['domain'])
    run(command)


@task
def get_logg():
    if env['remote']:
        command = 'tail ~/service/gunicorn/log/main/current | tai64nlocal'
        run(command)


@task
def update_bower():
    commands = [
        'cd website/static/website',
        'npm update -g --prefix=$HOME bower',
        'bower update',
        'cd ../../../',
    ]
    run(' && '.join(commands))


@task
def backup():
    run('python ../local/db_backup.py')


@task
def restart():
    if env['remote']:
        run('svc -du ~/service/gunicorn/')


@task
def shell():
    run('./manage.py shell_plus --settings=configuration.settings.{}'.format(env['domain']))


def db_pull():
    if env['local']:
        run('python ../local/db_pull.py')


# TASKS

@task
def deploy():
    git_pull()
    pip_install()
    collect_static()
    migrate()
    restart()
    print_command("Done")


# SCRIPT START

def main():
    import argparse
    parser = argparse.ArgumentParser()

    parser.add_argument('command', action='store')

    args = parser.parse_args()

    command = args.command

    configure()

    if command in tasks:
        print_headline("TASK: " + command)
        tasks.get(command)()
    else:
        print("Command '{}' not in: {}.".format(command, list(tasks.keys())))


if __name__ == "__main__":
    main()
