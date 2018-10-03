import requests
import json
from md5_hash_light import app, db
from md5_hash_light.models import Task, StatusType
from md5_hash_light.schema import task_schema
from md5_hash_light.tasks import calculate_hash_some_hash


def submit_task():
    task, errors = task_schema.load(requests.form)
    if errors:
        return json({'errors': errors}), 400

    db.session.add(Task(**task))
    db.session.commit()

    calculate_hash_some_hash.delay(task['id'])
    return json({'id': task['id']}), 201


def check_task():
    task = None
    if 'id' in requests.args:
        task = Task.query.filter_by(id=requests.args['id']).first()
    if not task:
        return json({'status': 'not found'}), 404

    responce = {'status': task.status}
    if task.status == StatusType.DONE:
        responce['url'] = task.url
        responce['md5'] = task.md5

    return json(**responce)
