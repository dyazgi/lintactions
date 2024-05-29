# Pylint


## Pre-Commit
Install pre-commit to .git each time you clone the repository:
```bash
pre-commit install # now pre-commit will run automatically on git commit!
```
Check the content of *.pre-commit-config.yaml*. The defines hooks will run pre-commit.
Three of them come from remote repositories and the third *linting-hook* is a local hook that runs the file *hook/linting_hook.py*.
*linting_hook* is so strict but can be modified to be more torellant, it is our choice.

To choose "pylint" in the linting _hook, create a file names *linter* and set its value to **pylint**.
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
```bash.
git add . # again
pre-commit run  # this will pass
```

Now commit and push the code
```bash
git commit -m "some message"
```
you will see that an action in github actions started to run please check the log in Actions
