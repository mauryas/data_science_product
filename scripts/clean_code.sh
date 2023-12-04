#!/bin/bash

# Exit script if any command fails
set -e
# Enable debug output
set -x

# Format imports
# Sort imports one per line, so autoflake can remove unused imports
isort --force-single-line-imports app

# Remove unused imports and variables, format code
autoflake --remove-all-unused-imports --recursive --remove-unused-variables --in-place app --exclude=__init__.py
isort app
black --line-length 79 app

# Linting
# Type checking
# mypy app #TODO uncomment and solve the errors
# Check code format
black -l 79 app --check
# Check imports
isort app
# Style checks
flake8 --exclude=.git,__pycache__,.ipynb_checkpoints,./.eggs/* --ignore=E123,E126,E501,W503