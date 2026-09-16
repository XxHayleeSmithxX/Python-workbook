# Task: File Existence
# Objective 3.1 - Construct and analyze code segments that perform file I/O
#
# Instructions:
# Use the os module to check information about "data.txt".
#
# Expected output:
# file_exists: True
# is_file: True
import os

# Step 1: Check if "data.txt" exists
file_exists = os.path.exists("data.txt")
print("file_exists:", file_exists)

# Step 2: Check if "data.txt" is a file (not a directory)
is_file = os.path.isfile("data.txt")
print("is_file:", is_file)