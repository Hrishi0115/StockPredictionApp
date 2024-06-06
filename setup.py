# description

# standard Python script used for packaging this project
# it defines the metadata about the project (name, version, dependencies, etc.).

# editable install mode

# install your project?
# making your project available as a Python package within your virtual environment - allows you to import your project's modules and packages in your scripts
# as if they were installed packages, without needing to copy files around

# Detailed explanation of "installing your project"
# Normal installation: when you install a package using `pip install package_name`, `pip` copies the package's files into your virtual environment's 
# `site-packages` directory. You can then import the package from anywhere in your environment
# Editable Installation (`pip install -e .`): Instead of copying the files, `pip` creates a symbolic link in the `site-packages` directory that points 
# to your project directory. This means changes you make in your project directory are immediately available without needing to reinstall



# when you install a project in editable mode using `pip install -e .`- it allows you to make changes to your code and have those changes immediately reflected
# without reinstalling the package.
# This is particularly useful during development because it simplifies the process of testing and modifying your code.

# How It Works:

# Symbolic Link: pip install -e . creates a symbolic link from the site-packages directory of your virtual environment to your project directory.
# Immediate Changes: Any changes you make to your source code are immediately available when you run your scripts, as the symbolic link points directly
# to your project directory.

from setuptools import setup, find_packages

def parse_requirements(filename):
    with open(filename, 'r') as file:
        return file.read().splitlines()


setup(
    name='stockpredictionapp',
    version='0.1',
    packages=find_packages(),
    install_requires=parse_requirements('requirements.txt') 
)

# use `pipreqs . --force ` to update requirements.txt when new dependencies are added
# dependencies refer to external packages/software that your project needs to function properly