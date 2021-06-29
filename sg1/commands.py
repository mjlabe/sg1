import importlib
import json
import os
import sys

from sg1.render import render_files
from sg1.helpers.directory import get_directories


settings_module = os.environ.get("SETTINGS", None)
if settings_module and os.path.isfile(os.path.join(os.getcwd(), os.path.join(*settings_module.split('.')) + '.py')):
    settings = importlib.import_module(settings_module)
else:
    from sg1 import settings


def start(project):
    print('Creating Empty Project')
    project_root = os.path.join(settings.BASE_DIR, project)
    if not os.path.isdir(project_root):
        os.mkdir(project_root)
    if not os.path.isdir(os.path.join(project_root, settings.TEMPLATE_FOLDER)):
        os.mkdir(os.path.join(project_root, settings.TEMPLATE_FOLDER))
    if not os.path.isdir(os.path.join(project_root, settings.CONTENT_FOLDER)):
        os.mkdir(os.path.join(project_root, settings.CONTENT_FOLDER))
    if not os.path.isdir(os.path.join(project_root, settings.OUTPUT_FOLDER)):
        os.mkdir(os.path.join(project_root, settings.OUTPUT_FOLDER))


def walk_content(content_dir):
    urls = {}
    for root, dirs, files in os.walk(content_dir):
        rel_root = root.split(content_dir)[1]
        for name in files:
            rel_path = os.path.join(rel_root, name)
            key = rel_path.split('.json')[0]
            if key.startswith("/"):
                key = key[1:].replace('/', '__')
            if not rel_path.startswith('/'):
                rel_path = '/' + rel_path
            urls[key] = rel_path.replace('.json', '.html')
    return urls


def save_urls(urls, project_dir):
    url_file_path = os.path.join(project_dir, 'urls', 'urls.json')
    if os.path.isfile(url_file_path):
        reply = str(input('URL file already exists. Replace? (y/n): ')).lower().strip()
        if reply in ['y', 'yes']:
            pass
        elif reply in ['n', 'no']:
            print('Canceled.')
            return
        else:
            print(f'{reply} is not an option. Canceled.')
            return
    print('Saving')
    with open(url_file_path, 'w+') as url_file:
        json_urls = json.dumps(urls, indent=4) + '\n'
        url_file.write(json_urls)


def generate_urls(project=None):
    print('Generating URLS')
    project_dir, content_dir = get_directories(project)
    if not os.path.isdir(os.path.join(project_dir, 'urls')):
        os.mkdir(os.path.join(project_dir, 'urls'))
    urls = walk_content(content_dir)
    save_urls(urls, project_dir)


def add_page(filename):
    with open(os.path.splitext(filename)[0] + '.json', 'w+') as page:
        page.write('')
    paginate()


def paginate(filename=None):
    pagination_file_name = 'sg1_pagination.json'
    pagination = []
    if os.path.exists(pagination_file_name):
        with open(pagination_file_name, 'r+') as pagination_file:
            try:
                pagination = json.load(pagination_file)
            except Exception:
                raise
    else:
        with open(pagination_file_name, 'w+') as pagination_file:
            pagination_file.write('')

    # if filename:
    #     add_page(filename)

    for file in os.listdir(os.getcwd()):
        if os.path.basename(file) != pagination_file_name:
            pagination.append(os.path.basename(os.getcwd()) + '__' + os.path.splitext(file)[0])

    with open(pagination_file_name, 'r+') as pagination_file:
        pagination_json = json.dumps(pagination, indent=4) + '\n'
        pagination_file.write(pagination_json)


def render(project=None):
    render_files(project)


commands = {
    'start': start,
    'urls': generate_urls,
    # 'addpage': add_page,
    'paginate': paginate,
    'render': render,
}


def parse_command(args):
    del sys.argv[0]
    if not args:
        print('You must enter a command')
    try:
        if len(args) > 1:
            commands[args[0]](args[1])
        else:
            commands[args[0]]()
    except KeyError:
        print('Invalid command')
    except IndexError:
        print('Enter a project name')
