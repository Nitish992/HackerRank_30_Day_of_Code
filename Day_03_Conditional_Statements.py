#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input())
    if (n%2 != 0):
        print("Weird")
    elif n in range(2,5):
        print("Not Weird")
    elif n in range(5,21):
        print("Weird")
    else:
        print("Not Weird")
