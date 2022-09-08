import sys
import os

fil = sys.argv[1]
with open(fil) as file:
    for line in file:
        print("site:s3.amazonaws.com " + "\"" + line.rstrip() + "\"")
        print("site:blob.core.windows.net " + "\"" + line.rstrip() + "\"")
        print("site:nyc3.digitaloceanspaces.com " + "\"" + line.rstrip() + "\"")
        print("site:drive.google.com " + "\"" + line.rstrip() + "\"")
