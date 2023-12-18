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
It is fearly simple to do this. And it can be done in only a few steps.
1. Create a new folder in the `projects` folder.

Under that folder create a new markdown file called `<project>_overview.md`. This file will contain the overview of the project. This is the file that will be displayed on the projects page.
Secondly create a new rst file called `<project>_tree.rst`. This file will contain the navigation tree for the projects docs.
The structure if these files is as follows:

```
Projects/            
|---project_tree.rst    <--- Tree elements provide the navigation structure for the documentation discoverable by sphinx
|---project_overview.md <--- Overview of the page/project provides the information about the project
|---<project>/
|   |---<project>_overview.md <--- Overview of the project
|   |---<project>_tree.rst <--- Navigation tree for the project
|   |---<project>_<somepart>.md    <--- provides some other important information about the project, eg how the team operates

```

The `<project>_tree.rst` file should contain the following:
```rst
.. mdinclude:: <project>_overview.md
```

The `<project>_overview.md` file should contain the following:
```markdown
# <Project>

<Project> is a project that does <some description of the project> other blah blah blah
```

2. Populate the projects brief description in the `<project>_overview.md` file

3. Populate the `<project>_tree.rst` file with your projects rst file similarly:
```rst
.. _projects:

.. toctree::
   :maxdepth: 2
   :caption: Projects:

   utilities/utilities_tree.rst
   <project>/<project>_tree.rst

```

You are good to go 🙂

### Local/Repository documentation
This documentation should only contain the following:
- How to setup the project (Readme.md)
- How to run the project (Readme.md)
- Autodoc (Sphinx, so all the functions and classes are documented)

>**Note:** It is important to create docstrings for everything you write. This isn't just helpfor for other people but helps you as well when months later you forgot what that piece of code was.

The autodoc pipeline is available the template repository, set for auto deploy on every push to the main branch.

Code has to be documented the Sphinx documentation style.
