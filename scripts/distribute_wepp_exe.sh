#!/bin/sh

for name in metvm4-dc iemvs101 metvm6-dc arritt iemvs102 iem8-dc metvm2-dc metvm33-dc; do
	scp wepp mesonet@$name:bin/
done
