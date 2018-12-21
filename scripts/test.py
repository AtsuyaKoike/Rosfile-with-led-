#!/usr/bin/env python
import sys
import time

while(1):
    with open("/dev/myled0", mode="w") as dev:
        dev.write("1\n")
    time.sleep(1)
    with open("/dev/myled0", mode="w") as dev:
        dev.write("0\n")
    time.sleep(1)

