#!/bin/sh

# These commands are derived from:
# https://stackoverflow.com/questions/29289785/how-to-install-docker-compose-on-windows
# this script should be run from within the boot2docker vm

tce-load -wi python
curl https://bootstrap.pypa.io/get-pip.py | sudo python - && sudo pip install -U docker-compose

echo 'su docker -c "tce-load -wi python" && curl https://bootstrap.pypa.io/get-pip.py | python - && pip install -U docker-compose' | sudo tee /var/lib/boot2docker/bootlocal.sh > /dev/null
sudo chmod +x /var/lib/boot2docker/bootlocal.sh
