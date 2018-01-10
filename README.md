autopylint
==========

A python-based application to automatically correct errors and
warnings identified by pylint.

Installation
============
```
python setup.py install
```

A better way is to make a user-specific installation like this:
```
python setup.py install --user
```

On OSX, you would then modify your path like this:
```
export PATH=$PATH:~/Library/Python/2.7/bin
```
to get `autopylint` in your path.

Usage
=====
```
pylint some/directory > lintfile
autopylint lintfile
```
