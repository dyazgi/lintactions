#!/bin/bash

module load env/release/2022.1
module load Python/3.10.4-GCCcore-11.3.0-bare

python --version # Python 3.10.4
python -m venv venv --system-site-packages
source ./venv/bin/activate
pip install -r requirements.txt --upgrade pip
