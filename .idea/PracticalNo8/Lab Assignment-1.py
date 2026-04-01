import os

if not os.path.exists("input.txt"):
    with open("input.txt", "w") as f:
        f.write("This is sample text")

with open("input.txt", "r") as file1:
    content = file1.read()

upper_content = content.upper()

with open("output.txt", "w") as file2:
    file2.write(upper_content)

print("Done successfully")