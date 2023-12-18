## Conventions

### Documentation 📃
Most of the codebase runs on sphinx-autodoc, which generates documentation from the docstrings in the codebase. The main reason why we use this is so we have an easy to, also most of the time up to date, documentation of all the projects in one place.
This proviced:
1. A centralised place for all the documentation
2. A way to easily understand why certain things are in place
3. So new people can get up to speed with the project and the team

Template for the documentation generator action can be found below:
```yaml
# Simple workflow for deploying static content to GitHub Pages
name: Deploy Documentation on Pages

on:
  # Runs on pushes targeting the default branch
  push:
    branches: ["main"]

  # Allows you to run this workflow manually from the Actions tab
  workflow_dispatch:

# Sets permissions of the GITHUB_TOKEN to allow deployment to GitHub Pages
permissions:
  contents: read
  pages: write
  id-token: write

# Allow only one concurrent deployment, skipping runs queued between the run in-progress and latest queued.
# However, do NOT cancel in-progress runs as we want to allow these production deployments to complete.
concurrency:
  group: "pages"
  cancel-in-progress: false

jobs:
  # Single deploy job since we're just deploying
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
    - name: Set up Python 3.10
      uses: actions/setup-python@v3
      with:
        python-version: "3.10"
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -U sphinx
        pip install furo
        pip install toml
        pip install sphinx-mdinclude
        
    - name: Build documentation
      run: |
        cd docs
        sphinx-apidoc -e -M --force -o . ../src/
        sphinx-build -b html ./source/ ./build/
    - name: Upload build data
      uses: actions/upload-artifact@v3
      with:
        name: documentation
        path: ./docs/build/
        
  deploy:
    needs: build
    environment:
      name: documentation
      url: ${{ steps.deployment.outputs.page_url }}
    runs-on: ubuntu-latest
    steps:
   
      - name: Checkout
        uses: actions/checkout@v3
      - name: Setup Pages
        uses: actions/configure-pages@v3
      - name: Download built directory
        uses: actions/download-artifact@v3
        with:
          name: documentation
      - name: Upload artifact
        uses: actions/upload-pages-artifact@v1
        with:
          # Upload entire repository
          path: '.'
      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v1
        with:
          folder: build

```

The action above can be updated to use other triggers, or to build from a project file.

>**Note:** The action above is a template, available as a tempalte repository (which is strongly encouraged to be used, can be found [here](https://github.com/guorbit/software-template)), however it should be updated to fit the project it is used for.

>**Note:** Modules and packages used in the codebase has to be located inside the `src` folder, otherwise the documentation generator will not be able to find them.

### Typing

Python typing is used to provide type hints so developers better understand what the code is doing, and to provide better static analysis of the codebase.

Typing is added to the codebase using the following syntax:
```python
def function_name(arg1: type, arg2: type) -> return_type:
    ...
```

Or in practice
```python
def add(a: int, b: int) -> int:
    return a + b
```

This can be use all around, such that it works for objects, as well:
```python
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

def get_person_age(person: Person) -> int:
    return person.age

```

It is recommended to set your IDEs type checker to basic to help you identify common problems.

### Linting

Linting is used to provide a consistent code style across the codebase, and to help identify common problems.

The template repository provides the necessary configuration for linting, and it is recommended to use it.
