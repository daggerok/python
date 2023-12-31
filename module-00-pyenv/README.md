# pyenv
Managing multiple python versions with pyenv

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
pyenv install 3.8.18
```

Use python 3.8.18 locally

```bash
pyenv local 3.8.18
```

Verify:

```bash
python -V
#Python 3.8.18
pyenv which python
#~/.pyenv/versions/3.8.18/bin/python
```

![](./pyenv-pyramid.webp)

## rtfm
https://realpython.com/intro-to-pyenv/
