#!/usr/bin/env bash
echo "Listening on port 5280"
while true; do netcat -l 5280; done | ./raspipe_pitft.sh
