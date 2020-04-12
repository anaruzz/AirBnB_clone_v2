#!/usr/bin/python3
# Script that generates a .tgz archive from the contentd of web_static folder

from fabric.api import local, run
from datetime import datetime


n = datetime.now()


def do_pack():
    """
    compress files to .tgz format
    """
    local(mkdir versions)
    file_name = 'versions/web_static_{}{}{}{}{}{}.tgz'\
            .format(n.year, n.month, n.day, n.hour, n.minute, n.second)
    compress = local("tar -cvzf" + file_name + "/web_static")
    if compress.succeeded:
        return file_name
    return None
