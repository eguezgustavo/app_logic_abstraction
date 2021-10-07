import json

from flask import Flask
from task_list import get_pending_tasks
from task_list import get_all_tasks

app = Flask(__name__)


@app.route("/pending-tasks")
def pending_tasks():
    return json.dumps([task.__dict__ for task in get_pending_tasks()])


@app.route("/all-tasks")
def all_tasks():
    return json.dumps([task.__dict__ for task in get_all_tasks])

if __name__ == '__main__':
    app.run()
