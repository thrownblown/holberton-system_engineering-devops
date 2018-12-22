from fabric.api import *
import sys


env.user = 'ubuntu'


@task
def pack():
    # Creates a tar gzipped archive of the current directory, the name of the
    # archive must be holbertonwebapp.tar.gz and be place in the local dir
    local("tar --exclude='*.tar.gz' -czf ../holbertonwebapp.tar.gz .")
    local("mv ../holbertonwebapp.tar.gz ./holbertonwebapp.tar.gz")


@task
def deploy():
    # Uploads the archive to the remote server in the directory /tmp/
    # Creates the directory /tmp/holbertonwebapp
    # Untars the holbertonwebapp.tar.gz archive in /tmp/holbertonwebapp
    run('mkdir -p /tmp/holbertonwebapp')
    with cd('/tmp'):
        put('holbertonwebapp.tar.gz')
    run('tar -C /tmp/holbertonwebapp -xzf /tmp/holbertonwebapp.tar.gz')
    # run('ls -l /tmp/holbertonwebapp')


@task
def clean():
    # Deletes the holbertonwebapp.tar.gz on your local machine
    local('rm ./holbertonwebapp.tar.gz')
