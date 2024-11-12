# torchtainer
A prototype Apptainer container with PyTorch and other common dependencies installed to be run on HPC facilties.


## Setup
### Development Environment
- [Mulixina](./doc/miluxina_setup.md)
- [Freja](./doc/freja_setup.md)
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

## How to
1- write the suitable sysyem  config file similar to *config/miluxina.sh*
2- lin kthe file
```bash
ln -sf facilities/meluxina.sh  cli.sh
chmod +x cli.sh
```

1- python venv and dependencies
```bash
sbatch ./cli.sh  prep_venv
```
