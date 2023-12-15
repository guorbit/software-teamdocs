# Creating project documentation

## Overview
It is important to document a project for multiple reasons:
- One it helps current people better understand the code base and practiceses used in the team
- But two also helps new people get up to speed with the project and the team

## What to document
Anything really that you think is worth documenting. But here are some key points to look out for:
- How to setup, run the project(this usually included in the README.md of the project)
- How the team operates
- How to contribute to the project
    - How code reviews are done
    - How the team communicates
    - How the team distributes work
    - etc...
- Resources that the team uses
    - Links to the tools used
    - Links to the libraries/frameworks used
    - Datasets used
    - Papers that contributed to the work

## How to document
It is fearly simple to do this. 
Most projects primarily rely on sphinx-autodoc to generate documentation from the docstrings in the codebase this is important to understand functions and objects, however for teams documentation we use markdown files. 

The structure if these files is as follows:

```
Projects/            
|---project_tree.rst    <--- Tree elements provide the navigation structure for the documentation discoverable by sphinx
|---project_overview.md <--- Overview of the page/project provides the information about the project
|---<project>/
|   |---<project>_overview.md <--- Overview of the project
|   |---<project>_<somepart>.md    <--- provides some other important information about the project, eg how the team operates

```

So to start creating the teams documentation:
1. Create a new folder in the Projects folder
2. Create a new markdown file in the new folder called `<project>_overview.md`
3. Add the following to the file:
    ```markdown
    # <Project> Overview
    <Project> is a project that does <some description of the project> other blah blah blah
    ```
    
4. Add the following to the `<project>_tree.rst` file:
    ```rst
    .. mdinclude:: <project_folder>/<project>_overview.md
    ```
    to include the markdown file you wrote the documentation in

5. Add the following to the `index.rst` file:
    ```rst
    .. toctree::
       :maxdepth: 2
       :caption: Projects

       <project_folder>/<project>_tree.rst
    ```

You are good to go 🙂
