#!/usr/bin/python

# Python Imports
import re, string

# Load my cdf file, read-only (r flag)
f = open("disks.csv", "r")
# Create a tuple of lines from this file
lines = f.readlines()

# Create a variable to keep track of totals
total_space = 0.0
total_my_space = 0.0

# Iterate over the tuple, we skip the first line, since it is a header
for line in lines[1:]:
    # We split each line into a tuple which we call tokens.
    tokens = re.split(",", string.strip(line))
    space = float(tokens[2])  # This column contains the mount size
    my_space = float(tokens[3])  # This column contains my usage

    # Add to our running totals
    total_space = total_space + space
    total_my_space = total_my_space + my_space

print("Total Space is: %5.2f" % (total_space,))
print("Total My Space is: %5.2f" % (total_my_space,))
