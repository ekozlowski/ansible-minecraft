from fabric import api as fab
from contextlib import contextmanager

@contextmanager
def with_vagrant():
    with fab.settings(user="vagrant",host_string="127.0.0.1:2222",key_filename=".vagrant/machines/minecraft/virtualbox/private_key"):
        yield

def ping(ip):
    with with_vagrant():
        return fab.run('ping -c 4 {}'.format(ip))

def save():
    with with_vagrant():
        fab.sudo('/etc/init.d/minecraft backup')
        fab.get(remote_path='/svr/minecraft-server/backups/*', local_path="/Users/e003070/Dropbox/minecraft_backups")
        
def restore():
    with with_vagrant():
        fab.put(remote_path='/svr/minecraft-server/backups/', local_path="/Users/e003070/Dropbox/minecraft_backups")



