#!/bin/bash

module load Python/3.10.4-env-hpc1-gcc-2022a-eb
python --version # Python 3.10.4
python -m venv venv --system-site-packages
source ./venv/bin/activate
pip install -r requirements.txt --upgrade pip
