#!/bin/bash

set -e

cd /src

locust --master -f ./tests/"${TARGET_TEST_FILE_NAME}".py --host="${TARGET_BASE_URL}"
