import os

from sg1 import settings


def get_directories(project):
    if project:
        project_dir = os.path.join(settings.BASE_DIR, project)
        content_dir = os.path.join(project_dir, settings.CONTENT_FOLDER)
    else:
        project_dir = settings.BASE_DIR
        content_dir = os.path.join(settings.BASE_DIR, settings.CONTENT_FOLDER)
    return project_dir, content_dir
