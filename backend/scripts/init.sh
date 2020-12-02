#!/bin/bash
script_full_path=$(dirname "$0")

python3 -m venv venv
source ${script_full_path}/dev.sh