#!/usr/bin/env python

import os
from setuptools import setup
from setuptools import find_packages


if __name__ == "__main__":
    setup(name="db-sqlite3",
          version="0.0.1",
          description="sqlite3 driver for db",
          author="John Evans",
          author_email="lgastako@gmail.com",
          url="https://github.com/lgastako/db-sqlite3",
          install_requires=["db"],
          py_modules=["db_sqlite3"],
          provides=["db_sqlite3"])
