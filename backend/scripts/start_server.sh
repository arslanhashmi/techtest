#!/bin/bash

echo "starting the service"
FLASK_APP=/var/www/app/app flask run -p 5000 -h 0.0.0.0 --reload
# tail -f /dev/null
