#!/usr/bin/env python3
# Crawls an s3 bucket for a regex hit

import re
import sys
import urllib.request
import urllib.parse


def main():
    if len(sys.argv) < 3:
        print(usage())
        sys.exit(0)

    url = sys.argv[1]
    GETparams= "?list-type=2&continuation-token="
    contToken = urllib.parse.quote(sys.argv[2])
    contReg = re.compile(sys.argv[3])

    # Dont change this. This finds the next continuation token
    contKey = re.compile("(?:<NextContinuationToken>)(.+)(?:<\/NextContinuationToken>)")

    # For Counts
    x = 0
    space = " "

    #print(url+GETparams+contToken)

    print("\nLooking for the key!")

    while True:
        req = urllib.request.urlopen(url + GETparams + contToken)
        res = req.read().decode("utf-8")

        found = contReg.search(res)
        if found:
            print(found)
            if contReg.match(res):
                print("\nKey Found: " + url + GETparams + contToken + "\n")
       
        newContTok = urllib.parse.quote(contKey.search(res).group(1))
        contToken = newContTok
        if not newContTok:
            sys.exit(0)
         
        print("\rPlease Wait{}".format("." * x), end="")
        sys.stdout.flush()
        x += 1

def usage():
    print("$ ./s3Crawler.py <url> <first continuation token> <key to look for>")

if __name__ == "__main__":
    main()
