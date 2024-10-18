#!/bin/bash

HTTP="https://pskreporter.info/cgi-bin/pskdata.pl?&adif=1&days=0.01&senderCallsign="
url=`echo $HTTP$1`
name=$1
call=`echo ${name////_}`
curl --output parse/dx_spots/$call.adif "$url"
parse/parse_adif.py $call