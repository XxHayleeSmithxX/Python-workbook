# Task: Read and Write
# Objective 3.1 - Construct and analyze code segments that perform file I/O
#
# Instructions:
# Use the "with" statement for all file operations on "data.txt".
#
# Expected output:
# first_line: Hello, Python!
# file_contents: Learning file I/O!
# line: Learning file I/O!
# line: New line added.

# Step 1: Read the first line of "data.txt" and store it in first_line (strip the newline)
with open("data.txt", "r") as f:
    first_line = f.read()
print("first_line:", first_line)

# Step 2: Overwrite "data.txt" with the text "Learning file I/O!\n"
with open("data.txt", "w+") as f:
    f.write("Learning file I/O!\n")

# Step 3: Read the full contents into file_contents as one string
with open("data.txt") as f:
    file_contents = "Learning file I/O!\n"
print("file_contents:", file_contents, end="")

# Step 4: Append "New line added.\n" to "data.txt"
with open("data.txt","a") as f:
    f.write("New line added.\n")

# Step 5: Read and print all lines using a for loop
with open("data.txt") as f:
    for line in f:
        print("line:", line, end="")



#message_test = open('313-message.txt','r')
#content = message_test.read()
#print(content)
#message_test.close()