""" simple hello server as a demo for DevSecOps training """

import argparse
import datetime
from flask import Flask, request, render_template

DEFAULT_SERVER_PORT = 8086

app = Flask(__name__, static_url_path='', static_folder='static')
app.config['SECRET_KEY'] = 'theS3cr3tKey'


@app.route("/", methods=['GET', 'POST'])
def index():
    """ main entry point into the web app """
    if request.method == 'POST':
        return "In Post"

    return render_template("index.html")


def parse_args():
    """ parse arguments for default overrides """
    parser = argparse.ArgumentParser(
        usage="python3 %(prog)s [options",
        description="Run the Simple Hello Server"
    )

    parser.add_argument("-p", "--port",
                        help=f'Listen port, defeault {DEFAULT_SERVER_PORT}',
                        default=DEFAULT_SERVER_PORT)

    return parser.parse_args()


if __name__ == "__main__":
    now = datetime.datetime.now()
    print(now.strftime("%d/%B/%Y %T %z"))

    args = parse_args()

    app.run(host="0.0.0.0", port=args.port)
