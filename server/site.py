from flask import render_template
from flask import Flask
import socket
from datetime import datetime
from sql import *
from server import Ipc
from config import *

app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404

@app.route('/')
@app.route('/index')
def index():
    con = sql_connection()
    posts = sql_table(con, False, False, 'test')
    print(posts)
    return render_template("index.html", posts=posts)

@app.route('/refresh')
def rtos():
    from server import ipslen

    con = sql_connection()
    sql_drop(con)

    while ipslen >= 0:
        try:
            my_ipc = Ipc(ips[ipslen], ipsport[ipslen], ipslen, con)
        except:
            print('Компьютер выключен или программа не запущена!')
        try:
            diskinfo = ipsdisk[ipslen]
        except:
            diskinfo = 'C:'
        my_ipc.run(diskinfo)
        ipslen = ipslen - 1
    posts = sql_table(con, False, False, 'test')
    return render_template("rtos.html")

if __name__ == '__main__':
    app.run(host="localhost", port=5555, debug=True)