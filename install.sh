#!/bin/bash
git clone https://github.com/IanRichardDavies/stevens.git
cd stevens
conda env create -f environment.yml
source activate stevens
poetry install
python manage.py runserver
