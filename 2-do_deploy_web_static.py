#!/usr/bin/python3
'''Fabric module'''
from fabric.api import env, run, put
from os import path

env.hosts = ['35.231.45.150', '34.74.42.82']


def do_deploy(archive_path):
    '''Distributes an archive to your web servers,
    using the function do_deploy'''
    filename = archive_path[9:-4]

    if not path.exists(archive_path):
        return False
    if put(archive_path, "/tmp/").failed:
        return False
    if run("sudo rm -rf /data/web_static/releases/{}/"
           .format(filename)).failed:
        return False
    if run("sudo mkdir -p /data/web_static/releases/{}/"
           .format(filename)).failed:
        return False
    if run('sudo tar -zxf /tmp/{} -C /data/web_static/releases/{}/'
           .format(filename + ".tgz", filename)).failed:
        return False
    if run('sudo rm /tmp/{}'.format(filename + '.tgz')).failed:
        return False
    if run('sudo mv /data/web_static/releases/{}/web_static/*'
           ' /data/web_static/releases/{}/'
           .format(filename, filename)).failed:
        return False
    if run('sudo rm -rf /data/web_static/releases/{}/web_static'
           .format(filename)).failed:
        return False
    if run('sudo rm -rf /data/web_static/current').failed:
        return False
    if run('sudo ln -s /data/web_static/releases/{}/ /data/web_static/current'
           .format(filename)).failed:
        return False
    return True
