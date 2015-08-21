#!/bin/bash

cd /tmp/
git clone https://github.com/sass/libsass.git
git clone https://github.com/sass/sassc.git
export SASS_LIBSASS_PATH=/tmp/libsass
cd /tmp/sassc
make
sudo cp /tmp/sassc/bin/sassc /bin/
