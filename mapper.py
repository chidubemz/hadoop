#!/usr/bin/python
import sys

for line in sys.stdin:
    line=line.strip()
    fields=line.split(",")

    if len(fields)==5:
        timestamp,instance_type,platform,avail_zone,price=fields

        print("%s\t%s\t%s" % (timestamp,instance_type,price))
