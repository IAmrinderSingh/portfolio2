#!/bin/bash
export FLASK_APP=$1
export FLASK_ENV=development
python -m flask run
