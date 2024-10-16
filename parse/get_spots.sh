#!/bin/bash

HTTP="https://pskreporter.info/cgi-bin/pskdata.pl?&adif=1&days=0.01&senderCallsign="
url=`echo $HTTP$1`
curl --output parse/dx_spots/$1.adif "$url"
parse/parse_adif.py $1