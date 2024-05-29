# lintactions
A sample code to show how to use pylint, pre-commit hooks and Github actions for linting python code.

## Setup
- [Mulixina](./doc/miluxina_setup.md)
- [Freja](./doc/freja_setup.md)


## Linting commands
One can either use pylint or ruff commads.
Copy the content of *fails.txt* to *main.py*

### Run Pylint
To run pylint:
```bash
pylint *.py # this will fail
```
Make it fails: Copy the content of *passes.txt* to *main.py* and then run
```bash
pylint *.py # This will give score less than 10.
```
The only change is the module docstring was removed. We can modify all linting options in *.pylintrc* file for pylint.


### Run Ruff
To run ruff:
```bash
ruff check *.py # this will pass
```
4- Make it fails: Copy the content of *fails.txt* to *main.py* and then run
```bash
ruff check *.py
```
The only change is the module docstring was removed. We can modify all linting options in *pyproject.toml* file for ruff.




## Pre-Commit
Install pre-commit to .git each time you clone the repository:
```bash
pre-commit install # now pre-commit will run automatically on git commit!
```
Check the content of *.pre-commit-config.yaml*. The defines hooks will run pre-commit.
Three of them come from remote repositories and the third *linting-hook* is a local hook that runs the file *hook/linting_hook.py*.

To choose ruff7pylint in the linting_hook, create7modify a file names *linter* and set its value either to **ruff** to use ruff or to **pylint** for pylint.
Then, copy the content of *passes.txt* to *main.py* then
```bash
git add main.py
pre-commit run # this will pass
```

Now, copy content of *failes.txt* to *main.py* and run
```bash
git add main.py # again
pre-commit run  # this will fail
```

Fix the code and then
```bash
git add . # again
pre-commit run  # this will pass
```

Now commit and push the code
```bash
git commit -m "some message"
```
you will see that an action in github actions started to run please check the log in Actions

## Github Actions
