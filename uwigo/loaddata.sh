#!/bin/bash

echo "## LOAD INITIAL DATA ## "

python manage.py loaddata tickets/fixtures/users.json
python manage.py loaddata tickets/fixtures/tickets.json