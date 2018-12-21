from fabric import task
from fabric import Connection


user = 'ubuntu'
c = Connection(user=user)


@task
def pack(local):
    # Creates a tar gzipped archive of the current directory, the name of the
    # archive must be holbertonwebapp.tar.gz and be place in the local dir
    local.run('tar -czf ../holbertonwebapp.tar.gz .')
    local.run('mv ../holbertonwebapp.tar.gz ./holbertonwebapp.tar.gz')


@task
def deploy(loacl):
    # Uploads the archive to the remote server in the directory /tmp/
    # Creates the directory /tmp/holbertonwebapp
    # Untars the holbertonwebapp.tar.gz archive in /tmp/holbertonwebapp
    c.run('mkdir -p /tmp/holbertonwebapp')
    c.put('holbertonwebapp.tar.gz', remote='/tmp/')
    c.run('tar -C /tmp/holbertonwebapp -xzf /tmp/holbertonwebapp.tar.gz')


@task
def clean(local):
    # Deletes the holbertonwebapp.tar.gz on your local machine
    local.sudo('./holbertonwebapp.tar.gz')
