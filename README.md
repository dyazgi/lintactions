# lintactions
A sample code to show how to use pylint, pre-coomit hooks and Github actions for linting python code.

## Pylint
below is steps to use pylint and pre-commit hooks
1- First, run this piece of code. You can set the project name directly but for security reason I do it this way

```bash
partition=cpu # cpu or gpu
project=$(groups | xargs -n1 | grep 177)
salloc  -A ${project} -p ${partition} -q default  -t 1:00:00
```

2- In the compute node:
```bash
module load env/release/2022.1
module load Python/3.10.4-GCCcore-11.3.0-bare
module load Ninja/1.10.2-GCCcore-11.3.0
module load NVHPC/22.7-CUDA-11.7.0

python --version # Python 3.10.4
python -m venv venv --system-site-packages
source ./venv/bin/activate
pip install -r requirements.txt --upgrade pip
```
3- Run pylint
```bash
pylint *.py # this will pass
```
4- Make it fails: Copy the content of *fails.txt* to *main.py* and then run
```bash
pylint *.py # This will give score less than 10.
```
The only change is:
```python
# Before
    except ValueError as err:
        print(f"Error: {err}")
# After
    except ValueError as e:
        print(f"Error: {e}"
```
We can modify all linting options in *.pylintrc* file.


## Pre-Commit
Install pre-commit to .git each time you clone the repository:
```bash
pre-commit install # now pre-commit will run automatically on git commit!
```
Check the content of *.pre-commit-config.yaml*. The defines hooks will run pre-commit.
Three of them come from remote repositories and the third *pylint-hook* is a local hook that runs the file *hook/pylint_hook.py*.
*pylint_hook* is so strict but can be modified to be more torellant, it is our choice.

Copy the content of *passes.txt* to *main.py* then
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

Not commit the code
```bash
git commit -m "some message"
```
you will that an action in github actions started to run please check the log
