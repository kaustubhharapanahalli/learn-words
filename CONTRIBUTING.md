# Contributing

I welcome contribution in several forms, like:

- Documentation
- New feature requests
- Testing
- Feature development
- Improvement features issues
- etc.

## Environment setup

This project uses tools like black, isort, pylint, pydocstyle, mypy, pre-commit to ensure maintenance of code quality.

### Pre-requisites

1. Install [Python](https://www.python.org/downloads) on your local machine.
2. If you are using Windows or Mac for development, install [Docker Desktop](https://www.docker.com/products/docker-desktop). If you are using Ubuntu, install [Docker](https://docs.docker.com/engine/install/ubuntu/).

### Development

1. Create a virtual environment using either [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/) or [venv](https://docs.python.org/3/tutorial/venv.html) on your local machine and activate it.

   - Creation of virtual environment using virtualenvwrapper.

   ```bash
   pip install virtualenvwrapper-win
   mkvirtualenv <env_name>
   setprojectdir </root/path/to/the/project>
   ```

   - Creation of virtual environment using venv.

   ```bash
   venv <env_name>
   source <env_name>/bin/activate
   ```

2. Install all the required packages:

   ```bash
   pip install -r requirements/all.txt
   ```

3. Install Git pre-commit hooks to enable code quality checks when making a Git commit:

   ```bash
   pre-commit install
   ```
