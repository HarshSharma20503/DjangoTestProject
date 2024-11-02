#!/usr/bin/env bash

pip install -r requirements.txt

# Apply migrations
python manage.py migrate