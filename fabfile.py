from datetime import datetime

from fabric.api import cd, env, require, local, run
from fabric.colors import blue
from fabvenv import virtualenv


def development():
    """fab development [command]"""
    env.name = 'development'
    env.environment = env.name
    # env.hosts = ['localhost']
    env.path = './'
    # env.virtualenv_path = 'workon colegend'
    env.backup_path = './backups/development'
    env.branch = 'development'
    env.push_branch = env.branch
    env.push_remote = 'origin'
    # env.reload_cmd = ''
    env.db_name = 'colegend'
    env.db_username = ''
    env.after_deploy_url = 'http://127.0.0.1:8004/'
    env.settings = '--settings=config.settings.local'
    env.requirements = 'requirements/local.txt'


def staging():
    """fab staging [command]"""
    env.name = 'staging'
    env.environment = env.name
    env.hosts = ['eraldo@eraldo.org']
    env.path = 'staging.colegend.org/project'
    env.virtualenv_path = 'staging.colegend.org/env'
    env.backup_path = './backups/staging'
    env.branch = 'staging'
    env.push_branch = env.branch
    env.push_remote = 'origin'
    env.start_cmd = 'svc -u colegendstaging'
    env.stop_cmd = 'svc -d colegendstaging'
    env.restart_cmd = 'svc -du colegendstaging'
    env.db_name = 'colegendstaging'
    env.db_username = 'colegend'
    env.after_deploy_url = 'https://staging.colegend.org'
    env.settings = '--settings=config.settings.production'
    env.requirements = 'requirements/production.txt'


def production():
    """fab production [command]"""
    env.name = 'production'
    env.environment = env.name
    env.hosts = ['eraldo@eraldo.org']
    env.path = '~/colegend/colegend'
    env.virtualenv_path = '~/colegend/env'
    env.backup_path = '~/colegend/backups'
    env.branch = 'master'
    env.push_branch = env.branch
    env.push_remote = 'origin'
    env.start_cmd = 'svc -u ~/service/gunicorn'
    env.stop_cmd = 'svc -d ~/service/gunicorn'
    env.restart_cmd = 'svc -du ~/service/gunicorn'
    env.db_name = 'colegend'
    env.db_username = 'colegend'
    env.after_deploy_url = 'https://www.colegend.org'
    env.settings = '--settings=config.settings.production'
    env.requirements = 'requirements/production.txt'


def backup():
    """fab [environment] backup"""
    if env.name == 'development':
        local('pg_dump -Fc {db_name} '
              '> {backup_path}/{db_name}-{environment}_`date +%Y-%m-%d_%H%M%S`.dump'.format(**env))
    elif env.name in ['staging', 'production']:
        with cd(env.backup_path):
            env.timestamp = datetime.now().strftime('%Y-%m-%d_%H%M%S')
            env.backup_file = '{backup_path}/{db_name}-{environment}_{timestamp}.dump'.format(**env)

            print(blue('=> dumping database'))
            run("pg_dump -Fc -U {db_username} {db_name} > {backup_file}".format(**env))

        print(blue('=> downloading database'))
        local('scp {hosts[0]}:{backup_file} backups/{environment}/'.format(**env))


def migrate():
    with virtualenv(env.virtualenv_path):
        run("{path}/manage.py migrate {settings}".format(**env))


def enable_debug():
    with virtualenv(env.virtualenv_path):
        run("sed -i -e 's/DJANGO_DEBUG=False/DJANGO_DEBUG=True/' {path}/.env".format(**env))
    restart()


def disable_debug():
    with virtualenv(env.virtualenv_path):
        run("sed -i -e 's/DJANGO_DEBUG=True/DJANGO_DEBUG=False/' {path}/.env".format(**env))
    restart()


def test():
    """fab [environment] test"""
    with virtualenv('colegend/env'):
        print(blue('test'))
        run('python')


def logs():
    """fab [environment] push"""
    local('git push origin {push_branch}'.format(**env))


def deploy():
    with cd(env.path):
        run('git pull {push_remote} {push_branch}'.format(**env))
        with virtualenv(env.virtualenv_path):
            run('pip install -Ur {requirements}'.format(**env))
            run('./manage.py collectstatic --noinput {settings}'.format(**env))
            run('cp staticfiles '.format(**env))
            # run('./manage.py compilemessages %(settings)s'.format(**env))
    migrate()
    restart()
    ping()


def ping():
    run('echo {after_deploy_url} returned:  '
        '\>\>\>  $(curl --write-out %{{http_code}} --silent --output /dev/null {after_deploy_url})'.format(**env))


def stop():
    """fab [environment] stop"""
    run(env.stop_cmd)


def start():
    """fab [environment] start"""
    run(env.start_cmd)


def restart():
    """fab [environment] restart"""
    run(env.restart_cmd)


def push():
    """fab [environment] push"""
    local('git push origin {push_branch}'.format(**env))


def ps():
    """fab [environment] ps"""
    run('htop')


def logs():
    """fab [environment] ps"""
    run('zcat -f ~/service/gunicorn/log/main/* | tai64nlocal | less | tail')


def open():
    """fab [environment] open"""
    local('open {after_deploy_url}'.format(**env))


def create_superuser():
    """fab [environment] create_superuser"""
    with virtualenv(env.virtualenv_path):
        run('{path}/manage.py createsuperuser {settings}'.format(**env))
