#!/bin/bash

python3 -m pip install build

python3 -m build

pip3 install dist/event_generator-0.0.1-py3-none-any.whl
