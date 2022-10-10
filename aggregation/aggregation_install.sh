#!/bin/bash
pip install pandas
pip install -U pip setuptools wheel
pip install -U spacy
python -m spacy download en_core_web_sm
python -m pip install -U pip
python -m pip install -U matplotlib