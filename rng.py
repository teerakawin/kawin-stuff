#! /usr/bin/env python3
# hi welcome to tis code
import random
import sys

VERSION = "1.0"

if len(sys.argv) > 1:
    if sys.argv[1] == "-v":
        print(f"kawin's rng {VERSION}")
        sys.exit()
    elif sys.argv[1] == "--version":
        print(f"kawin's rng {VERSION}")
        sys.exit()
    if sys.argv[1] == "-h":
        print("Kawin's rng")
        print("   -v, --version show version")
        print("   -h, --help    show help message")
        sys.exit()
    if sys.argv[1] == "--help":
        print("Kawin's rng")
        print("   -v, --version show version")
        print("   -h, --help    show help message")
        sys.exit()

number = random.randint(1, 1000)
print(number)
