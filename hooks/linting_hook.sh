#!/bin/bash

#Author: Daniel Yazgi
#Date: 2024-05-28

pwd
linter=$(cat linter)
echo $linter
set -e
echo $@
if [ "x$linter" == "xpylint" ]; then
   pylint $@ --rcfile=.pylintrc
   exit $?
fi


if [ "x$linter" == "xruff" ]; then
   ruff check $@
   exit $?
fi

# no options was selected
exit 1
