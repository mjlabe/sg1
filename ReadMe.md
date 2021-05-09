# Stupid Simple Static Site Generator

This repo is a stupid, simple, static site generator. It is very opinionated, but you can easily create static sites
with jinja templates and json files. This basically cuts the framework out of rendering.

## Getting Started

### Install

`pip3 install git+https://github.com/mjlabe/sg1.git@main`

### Setup

`sg1 start projectname`

This creates 3 folders in a directory `projectname`:

1. `templates`: These are the [jinja2](https://palletsprojects.com/p/jinja/) templates that will be rendered

2. `content`: JSON files that specify the key value pairs used to render the templates

3. `html`: Output directory of the rendering. This is your beautifully* rendered html files

> *Beauty is not guaranteed.

### Templates

See the [jinja2 documentation](https://palletsprojects.com/p/jinja/)

### Content

Example:

```json
# index.json
        
{
  "template": "index.html",
  "posts": [
    {
      "title": "test",
      "location": "location",
      "summary": "summary",
      }
    }
    ...    
  ]
}
```

The only required field is `template` which is the relative path from the `templates` folder.

The rest is whatever you want, just make sure the variables are in the template (`{{variable}}`).

### HTML

Profit
