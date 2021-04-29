import setuptools

# setup.py is required in order to install in editable mode

# install_requires is here instead of setup.cfg for github dependency graph
# This fills a different role from requirements.txt
# https://packaging.python.org/discussions/install-requires-vs-requirements/

setuptools.setup(name="hello", install_requires=["click"])
