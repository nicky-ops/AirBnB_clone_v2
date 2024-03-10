#!/usr/bin/python3
"""
This fabric script generates a .tgz archive from the folder web_static
"""
from fabric.api import local
from time import strftime
from datetime import datetime


def do_pack():
    """
    This function generates a .tgz archive
    """
    filename = strftime("%Y%m%d%H%M%S")
    try:
        local("mkdir -p versions")
        local("tar -czvf versions/web_static_{}.tgz web_static/"
              .format(filename))
        return "versions/web_static_{}.tgz".format(filename)

    except Exception as e:
        return None
