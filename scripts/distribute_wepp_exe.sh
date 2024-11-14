#!/bin/sh

for name in metvm2-dc iemvs35-dc iemvs36-dc metvm6-dc metvm32-dc metvm33-dc arritt iem8-dc metvm2-dc metvm33-dc iemvm0 iemvm1 iemvm2; do
	scp $1 mesonet@$name:bin/
done
