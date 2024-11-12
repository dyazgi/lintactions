# python-project-template
A a Template with pre-commit actions and ruff linting and some default configurations


## Setup
### Development Environment
- [Mulixina](./doc/miluxina_setup.md)
- [Freja](./doc/freja_setup.md)
- More can be added

Install  python venv and packages
```bash
./scripts/setup_venv_freja.sh
source venv/bin/activate
```


### Pre-Commit
Install pre-commit to .git each time you clone the repository:
```bash
pre-commit install # now pre-commit will run automatically on git commit!
```
Check the content of *.pre-commit-config.yaml*. The defines hooks will run pre-commit.
Three of them come from remote repositories and the third *linting-hook* is a local hook that runs the file *hook/linting_hook.py*.

 
 
