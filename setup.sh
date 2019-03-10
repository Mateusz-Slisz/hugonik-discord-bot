#!/bin/bash

set -a
. ./.env
set +a

echo "Script has been started"
python hugonik.py
