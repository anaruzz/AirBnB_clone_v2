#!/usr/bin/python3
# Script that generates a .tgz archive from the contentd of web_static folder

from fabric.api import local, run
from datetime import datetime
from os import path


def do_pack():
    """
    compress files to .tgz format
    """

    n = datetime.now()
    file_name = 'versions/web_static_{}{}{}{}{}{}.tgz'\
                .format(n.year, n.month, n.day, n.hour, n.minute, n.second)
    compress = local('mkdir -p versions')
    compress = local("tar -cvzf" + file_name + " web_static")
    if compress.succeeded:
        return file_name
    return None


def do_deploy(archive_path):
    if not path.exists(archive_path):
        return False
    val = True
    a = put(archive_path, "/tmp/")
    if a.failed:
        val = False

    new_comp = archive_path.split("/")[-1]
    new_folder = ("/data/web_static/releases/" + new_comp.split(".")[0])
    b = run("sudo mkdir -p {}".format(new_folder))
    if b.failed:
        val = False

    c = run("sudo tar -xzf /tmp/{} -C {}".format(new_comp, new_folder))
    if c.failed:
        val = False

    d = run("sudo rm /tmp/{}".format(new_comp))
    if d.failed:
        val = False

    e = run("sudo mv {}/web_static/* {}/".format(new_folder, new_folder))
    if e.failed:
        val = False
    f = run("sudo rm -rf {}/web_static".format(new_folder))
    if f.failed:
        val = False

    g = run('sudo rm -rf /data/web_static/current')
    if g.failed:
        val = False

    h = run("sudo ln -s {} /data/web_static/current".format(new_folder))
    if h.failed:
        val = False

    return val
