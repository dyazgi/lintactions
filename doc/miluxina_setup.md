# Mulixina setup
below is steps to use pylint/ruff and pre-commit hooks
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

python --version # Python 3.10.4
python -m venv venv --system-site-packages
source ./venv/bin/activate
pip install -r requirements.txt --upgrade pip
```
