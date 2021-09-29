# Python Tool Template

Template for a stand-alone python tool or script

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [About the Template](#about-the-template)
- [Contributing to this project](#contributing-to-this-project)
  - [Git Branching strategy](#git-branching-strategy)
    - [Git Flow](#git-flow)
    - [Github Flow](#github-flow)
  - [Before commiting](#before-commiting)
  - [Work in progress branches](#work-in-progress-branches)
  - [Feature branches](#feature-branches)
  - [Before raising a PR](#before-raising-a-pr)
  - [Merging a PR](#merging-a-pr)
- [Running tests](#running-tests)
  - [Tox](#tox)
  - [PyTest](#pytest)
- [Dependency management](#dependency-management)
- [Misc.](#misc)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## About the Template

Replace this section with "About `project name`"

This provides an example for a application that can be installed with pip for use in on the command line.

In here you'll find some minimal GitHub workflows configurations, code and tests to seed a python project.

The template is compatible with python 2 and 3 for easy adoption.

## Contributing to this project

### Git Branching strategy

Do we have significant release testing focused on this repository?  If yes, use [git-flow](https://nvie.com/posts/a-successful-git-branching-model/).  Otherwise use [github-flow](https://guides.github.com/introduction/flow/).

#### Git Flow

This repository follows [git-flow](https://nvie.com/posts/a-successful-git-branching-model/).  Released code is on the `master` branch.  PRs are typically merged into `develop`.  For release code, crate a `release/<description>` branch from `develop` and open a PR into `master`.

This way we can make bugfixes to the code that is prepared for release while continuing new feature development that can merge into `develop`.  Tagging each release candidate on the `release/` branch and each releas on `master` allows us to go back and make patches where needed if we are not ready to make a new minor release based on `develop`.

#### Github Flow

This repository follows [github-flow](https://guides.github.com/introduction/flow/).  Released code is kept on the `main` branch.  New features are developed on seperate branches, but these branches should be short lived.  PRs are created from the feature branch into the `main` branch.  Significant test coverage provides confidence that newly merged features do not break the build.  Additionally, downstream dependencies are able to pin versions of this repository allowing for control over what gets released in customer applications.

### Before commiting

Setup `pre-commit` to run before each commit.

```bash
pip install pre-commit
pre-commit install
```

`pre-commit` performs the checks and actions defined in `.pre-commit-config.yaml`.

It's also a good idea to run the unit tests before commiting.  See [Running tests](#running-tests).

### Work in progress branches

It's encouraged to create a branch for work in progress.  You can use the format `<user name>/<description>` for short term or experimental work.  Pushing the branch may inspire others over invite feedback.  Since we have many people working remotely, it also helps communicate active effort and avoid duplicative work.  Since it's your own branch, feel free to rebase force push anything or anything else you want to do with that branch.

### Feature branches

`<type>/<description>` Is used for shared development branches and development that's intended to merge back into `develop`.  `<type>` Comes from the types listed in the `.gitmessage` file.  On these branches, use the `.gitmessage` template to create informative commit messages.  These can help speed along review.  And links back to the Jira ticket help others understand the context without needing to duplicate the what's written in the ticket.

### Before raising a PR

Please, organize your commits into small self-contained commits with descriptive messages (see `.gitmessage`).  This helps reviewers quickly give relevant feedback, ensuring the PR is approved as quickly as it can be.

### Merging a PR

Use merge commits to merge in changes from the PR in order to maintain history and maintain the context of review comments.  This can also help if we need to run git-bisect, sine the commits will be smaller, it is easier to pinpoint the change that resulted in a particular bug.

## Running tests

### Tox

The easiest way to run tests is with `tox`.
Simply run `tox` and it will run all of the tests for each environment both supported by the module and installed on the developer's machine.

In the below example tests passed for python 2.7 and 3.9.  Python3.8 was not installed and therefore those tests were not run.

```text
  py27: commands succeeded
ERROR:  py38: InterpreterNotFound: python3.8
  py39: commands succeeded
  report: commands succeeded
```

Tox can take a little while to run since it sets up each environment for each run of the tests.  PyTest is useful to get a shorter feedback loop.

### PyTest

Follow these steps to run tests using pytest, replacing `<ver>` with the appropriate python version.

1. Set up a virtual environment `python<ver> -m virtualenv env`
2. Activate the virtual environment
    - Linux/Mac `. env/bin/activate`
    - Windows `.\env\Scripts\Activate`
3. Install development dependencies `pip install -r .\requirements\dev-py<ver>.txt`
4. Install this repo in editable mode `pip install -e .`
5. Run the tests `pytest`

For example, on windows with python3 run:

```powershell
python3 -m virtualenv env
.\env\Scripts\Activate
pip install -r .\requirements\dev-py3.txt
pip install -e .
pytest

```

This results in the following output:

```text
3 passed in 0.07 seconds
```

After the virtual environment is set up (steps 1-4 above), calling `pytest` is all you need.
It can be useful to run a watch window in a terminal while working on the project to keep the tests running on each save. `watch -c pytest --color=yes` will keep the color highlighting and the tests running in a loop.

## Dependency management

This project uses [pip-compile-multi](https://pypi.org/project/pip-compile-multi/) for hard-pinning dependencies versions.
Please see its documentation for usage instructions.
In short, `requirements/base.in` contains the list of direct requirements with occasional version constraints (like `Django<2`)
and `requirements/base.txt` is automatically generated from it by adding recursive tree of dependencies with fixed versions.
The same goes for `test` and `dev`.

To upgrade dependency versions, run `tox -e upgrade3 -e upgrade2`.

To add a new dependency without upgrade, add it to `requirements/base.in` and run `pip-compile-multi --no-upgrade`.

For installation always use `.txt` files. For example, command `pip install -Ue . -r requirements/dev.txt` will install
this project in development mode, testing requirements and development tools.
Another useful command is `pip-sync requirements/dev.txt`, it uninstalls packages from your virtualenv that aren't listed in the file.

## Misc.

It uses `setup.cfg` with a minimal `setup.py` to minimimize redundancy.  While a lot of customation can be performed in setup.py, it is not recommended.
<https://packaging.python.org/tutorials/packaging-projects/#configuring-metadata>

Tests also run using GitHub actions:
<https://github.com/features/actions>
