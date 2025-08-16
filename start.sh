#!/bin/bash

# Rodar o script Python
python anti_sleep.py

# Rodar o Django com Gunicorn
gunicorn setup.wsgi:application --bind 0.0.0.0:$PORT