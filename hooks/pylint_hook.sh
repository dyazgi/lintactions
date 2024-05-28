#!/bin/bash

#Author: Daniel Yazgi
#Date: 2024-05-28

set -e
echo $@
pylint $@ --rcfile=.pylintrc -f json2 | python $(dirname $0)/pylint_hook.py
