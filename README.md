# Python Tool Template

Template for a stand-alone python tool or script

This provides an example for a script that can be installed with pip for use on the command line.

In here you'll find some minimal github workflows configurations, code and tests to seed a python project.

Template is compatable with python 2 and 3 for easy adoption.

Tests use pytest and pytest coverage.
* https://docs.pytest.org/en/stable/
* https://pypi.org/project/pytest-cov/

Code is formatted using Black
* https://pypi.org/project/black/

Static Analysis is performed with prospector
https://pypi.org/project/prospector/

It uses `requirements.in` and `requirements.txt` to split out the basic requirements from the pinned requirements, allowing for an easy update of the pinned requirements.
https://modelpredict.com/wht-requirements-txt-is-not-enough


It uses `setup.cfg` without `setup.py` for a more straight-forward install.  `setup.py` can be added if customization is needed, but is not recommened.
https://packaging.python.org/tutorials/packaging-projects/#configuring-metadata
