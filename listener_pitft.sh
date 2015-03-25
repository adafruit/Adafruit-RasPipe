#!/usr/bin/env bash
echo "Listening on port 5280"
netcat -l 5280 -k | ./raspipe_pitft.sh
