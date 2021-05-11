import importlib
import os
import json
from jinja2 import Environment, FileSystemLoader

from sg1.helpers.directory import get_directories

settings_module = os.environ.get("SETTINGS", None)
if settings_module and os.path.isfile(os.path.join(os.getcwd(), os.path.join(*settings_module.split('.')) + '.py')):
    settings = importlib.import_module(settings_module)
else:
    from sg1 import settings


class TemplateError(Exception):
    def __init__(self, path):
        super().__init__(f"You must include the template path in {path}.")


def render_page(content, content_file_path, urls, project_path):
    print(f"Rendering {content_file_path} content to static file.")
    parent_dir = os.path.basename(os.path.dirname(content_file_path))
    if parent_dir == 'content':
        parent_dir = ''
    output_path = os.path.join(project_path,
                               settings.OUTPUT_FOLDER,
                               parent_dir)
    env = Environment(loader=FileSystemLoader(os.path.join(project_path, settings.TEMPLATE_FOLDER)))
    try:
        template = env.get_template(content.pop('template'))
    except KeyError:
        raise TemplateError(path=content_file_path)
    if not os.path.exists(output_path):
        os.mkdir(output_path)
    with open(os.path.join(output_path, os.path.basename(content_file_path).split('.')[0] + '.html'), 'w+') as file:
        html = template.render(
            content=content,
            urls=urls
        )
        file.write(html)


def get_urls(project_dir):
    urls_path = os.path.join(project_dir, 'urls', 'urls.json')
    if os.path.isdir(urls_path):
        with open(urls_path, 'r') as urls_file:
            return json.load(urls_file)
    return {}


def get_extras_content(project, page_content: dict) -> dict:
    if "extras" in page_content.keys():
        for extra in page_content['extras']:
            proj_dir = os.path.join(settings.BASE_DIR, project)
            extra_path = os.path.join(proj_dir, settings.CONTENT_FOLDER, extra)
            if os.path.isfile(extra_path):
                with open(extra_path, 'r') as content_json:
                    page_content[extra.replace("/", "__").replace('.json', '')] = json.load(content_json)
            else:
                for content_file in os.listdir(extra_path):
                    if os.path.isfile(os.path.join(proj_dir, extra_path, content_file)):
                        with open(os.path.join(proj_dir, extra_path, content_file), 'r') as content_json:
                            key = extra.replace("/", "__") + '__' + content_file.replace("/", "__").replace('.json', '')
                            page_content[key] = json.load(content_json)
        del(page_content['extras'])
    return page_content


def render_files(project=None):
    project_dir, content_dir = get_directories(project)
    if os.path.isdir(content_dir):
        for root, _, files in os.walk(content_dir):
            for file in files:
                content_file_path = os.path.join(root, file)
                with open(content_file_path, 'r') as content_json:
                    page_content = json.load(content_json)
                    content = get_extras_content(project, page_content)
                    render_page(content=content,
                                project_path=project_dir,
                                content_file_path=content_file_path,
                                urls=get_urls(project_dir))
        return
    print('Must create posts directory or specify custom path in settings')
