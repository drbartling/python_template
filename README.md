# Python Template

Template for a stand-alone python tool or script

## About the Template

Replace this section with "About `project name`"

This template sets up a python project using poetry to manage dependencies, pytest for unit testing, pyinstaller for building an executable, and wix for creating a windows installer for distribution.

## Getting Started

### Setup
- Install the latest version of python
	- MacOS: `brew install python`
	- Windows: `winget install Python.Python.3.11`
	- Ubuntu: `sudo apt install python`
- Install [poetry](https://python-poetry.org/)
	- [Installation Instructions](https://python-poetry.org/docs/#installation)
- Install project dependencies:
	- `poetry install`
- Activate project virtual environment:
	- `poetry shell`
- Run the example program
	- `hello Bob`

### Testing

```bash
pytest
```

### Building Executable

```bash
python tools/app_build.py
```

### Building An Installer

- Install build dependencies
	- Windows: `winget install WixToolset.AdditionalTools`
-
