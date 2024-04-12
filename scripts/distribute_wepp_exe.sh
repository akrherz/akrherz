#!/bin/sh

for name in metvm4-dc iemvs35-dc iemvs36-dc metvm6-dc arritt iem8-dc metvm2-dc metvm33-dc iemvm1 iemvm2 iemvm9; do
	scp $1 mesonet@$name:bin/
done
