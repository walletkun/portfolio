#!/bin/bash

source $PWD/py3/bin/activate 
python -m unittest discover -v tests/

