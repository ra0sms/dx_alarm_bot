#!/bin/bash

HTTP="https://pskreporter.info/cgi-bin/pskdata.pl?adif=1&days=0.01&senderCallsign="
url=`echo $HTTP$1`
echo $url
curl --output parse/$1.adif "$url"
parse/parse_adif.py $1