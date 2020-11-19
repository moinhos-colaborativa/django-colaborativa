# Sandbox

Django project to maintain the mainly app

## Steps

```bash
# Install the Open edX Juniper Python version
LDFLAGS="-L/usr/lib/openssl-1.0" CFLAGS="-I/usr/include/openssl-1.0" pyenv install -v 3.5.2

# Set the python version
pyenv local 3.5.2

# Install the pipenv environment
pip install pipenv

# Install the Open edX Juniper Django version
pipenv install django==2.2.15

# Enable the shell
pipenv shell


```