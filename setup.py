import setuptools

# setup.py is required in order to install in editable mode
# install_requires is here instead of setup.cfg for github dependency graph

setuptools.setup(name="hello", install_requires=["click"])
