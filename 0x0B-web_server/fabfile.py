import fabric
from fabric import task
from fabric import Connection
#import zipfile
import os.path



user = 'ubuntu'
c = Connection('ubuntu@35.243.217.174')


@task
def pack(c):
    # Creates a tar gzipped archive of the current directory, the name of the
    # archive must be holbertonwebapp.tar.gz and be place in the local dir
    print('pack')
    c.run('uname -s')

@task
def deploy(c):
    # Uploads the archive to the remote server in the directory /tmp/
    # Creates the directory /tmp/holbertonwebapp
    # Untars the holbertonwebapp.tar.gz archive in /tmp/holbertonwebapp
    print('deploy')
    c.run('uname -s')

@task
def clean(c):
    # Deletes the holbertonwebapp.tar.gz on your local machine
    print('clean')
    c.run('uname -s')
