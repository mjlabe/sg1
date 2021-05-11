# Stupid Simple Static Site Generator

This repo is a stupid, simple, static site generator. It is very opinionated, but you can easily create static sites
with jinja templates and json files. This basically cuts the framework out of rendering.

## Getting Started

### Install

`pip3 install git+https://github.com/mjlabe/sg1.git@main`

### Setup

`sg1 start projectname`

This creates 3 folders in a directory `projectname`:

1. `templates`: These are the [jinja2](https://palletsprojects.com/p/jinja/) templates that will be rendered.

2. `content`: JSON files that specify the key value pairs used to render the templates.

3. `html`: Output directory of the rendering. This is where your beautifully* rendered html files are generated.

> *Beauty not guaranteed.

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

### Simple URLs

`sg1 urls projectname` creates a `urls` folder in `projectname` with a `urls.json` file containing all the project urls 
for ease of use in the templates.

Example:

Let's say you have a content file `posts/post.json`. The above command will add relative reference in the `urls.json` 
file like:

```json
{
  ...,
  "posts__post": "/posts/post.html",
  ...
}
```

You can then create a link in the template with `<a href="{{ urls.posts__post }}">Post</a>`.

### HTML

To generate the HTML files, run `sg1 render projectname`.

## To Do

- [x] Add `extras` field to context files that automagically includes context of a specified subfolder (to easily
use context from `example_post.json` to render the image and title in `index.html` for example).
- [ ] Pagination of extra
- [ ] Refactor and general cleanup
- [ ] Update paths for Windows
