#!/bin/bash

echo "Starting tests.."
TEST_MODE=1 python -m pytest /var/www/app/tests
