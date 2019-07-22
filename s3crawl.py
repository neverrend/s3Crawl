#!/usr/bin/env python3
# Crawls an s3 bucket for a regex hit

import re
import sys
import urllib.request
import urllib.parse


#if len(sys.argv) < 2:
#    sys.exit(0)

# Replace the URL here. Make sure &continuation-token= is at the end
url = "http://<URL HERE>/?list-type=2&continuation-token="

# Enter the first token
contToken = urllib.parse.quote("")

# Put the name of the key you are looking for here
contReg = re.compile("")

# Dont change this. This finds the next continuation token
contKey = re.compile("(?:<NextContinuationToken>)(.+)(?:<\/NextContinuationToken>)")

# For Counts
x = 0

while True:
    req = urllib.request.urlopen(url+contToken)
    res = req.read().decode("utf-8")

    found = contReg.search(res)
    if found:
        print("Key Found: " + url + contToken + "\n")
        sys.exit(0)
   
    newContTok = urllib.parse.quote(contKey.search(res).group(1))
    contToken = newContTok
    
    x += 1
    print("New Token! #{} {}".format(x, contToken))
