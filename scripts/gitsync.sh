#!/bin/bash

# Ensure that mydir is provided and does not contain spaces
if [ -z "$1" ] || [[ "$1" =~ \  ]]; then
  echo "Usage: $0 <directory>"
  exit 1
fi
mydir="$1"

for machine in $(ansible iem_hosts -i /home/akrherz/projects/infra-ansible/inventories --list-hosts | awk 'NR>1 {print $1}') anticyclone.agron.iastate.edu; do
  echo "-------------------- $machine ----------------------"
  ssh "mesonet@${machine}" "cd $mydir && git pull"
done
