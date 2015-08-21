#!/bin/bash

# Compiles sass to css
# This is a separate script so the iteration time is faster than `docker-compose up` on stylesheet changes
mkdir -p static/build
./bin/sassc -m -t compressed sass/main.scss static/build/main.min.css
