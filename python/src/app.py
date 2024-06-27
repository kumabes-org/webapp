from flask import Flask, render_template, request, redirect, session, flash, url_for
import datetime
import json
import socket


app = Flask(__name__)


@app.route("/")
def index():
    application_version = "0.0.1"
    host_address=None
    host_name=socket.gethostname()
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    host_address=s.getsockname()[0]
    s.close()
    return render_template("index.html", titulo="python/flask - webapp", application_version=application_version, host_address=host_address, host_name=host_name)

app.run(host="0.0.0.0", port=5000, debug=True)