#!/bin/bash

set -e

cd /src

locust --worker --processes -1 -f - --master-host "locust-master"