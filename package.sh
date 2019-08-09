#!/bin/bash

rm -rf build dist

pipenv shell

python setup.py sdist bdist_wheel

if [ $1 == '--test' ]; then
    python -m twine upload --repository-url https://pypi.org/legacy/ dist/*
else
    python -m twine upload dist/*
fi
