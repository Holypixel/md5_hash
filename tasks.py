from sqlalchemy import func

from md5_hash_light import app, celery, db
from md5_hash_light.models import Task, StatusType
from md5_hash_light.utils import calculate_hash_by_file, dowanload_file, remove_file, send_email


@celery.task
def calculate_hash_some_hash(task_uuid):
    task = Task.query.filter_by(id=task_uuid).first()
    if not task:
        return

    task.status = StatusType.RUNNING
    task.started_at = func.now()
    db.session.commit()

    try:
        task.md5 = get_hash(task.url)
    except Exception:
        task.status = StatusType.FAIL
    else:
        task.status = StatusType.DONE
    task.finished_at = func.now()
    db.session.commit()




def get_hash(url):
    path = dowanload_file(url)
    md5 = calculate_hash_by_file(path)
    remove_file(path)
    return md5
