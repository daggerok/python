# pyenv virtualenv
Managing virtual python environment with pyenv

## install

```bash
brew reinstall curl openssl readline sqlite3 xz zlib
curl https://pyenv.run | bash
```

## use pyenv to install

List of Python 3.x envs

```bash
pyenv install --list | grep " 3\.[678]"
```

Install exact version (3.8.18) and use it

```bash
mkdir -p path/to/python/module
cd path/to/python/module
pyenv install 3.8.17
```

Create virtual environment (with python 3.8.17) for `module-01-pyenv-virtualenv` project 

```bash
pyenv virtualenv 3.8.17 module-01-pyenv-virtualenv
```

Use virtual environment like so:

```bash
pyenv local module-01-pyenv-virtualenv
```

Verify:

```bash
python -V
#Python 3.8.17
pyenv which python
#~/.pyenv/versions/module-01-pyenv-virtualenv/bin/python
```

## rtfm
https://realpython.com/intro-to-pyenv/
