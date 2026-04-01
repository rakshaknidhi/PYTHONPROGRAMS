# Take file names from user
source = input("Enter source file name: ")
destination = input("Enter destination file name: ")

# Open source file
with open(source, "r") as file1:
    lines = file1.readlines()

# Open destination file
with open(destination, "w") as file2:
    for line in lines:
        # Skip comments and empty lines
        stripped = line.strip()
        if not stripped.startswith("#") and stripped != "":
            file2.write(line)

# Print both files content
print("\n--- Source File Content ---")
with open(source, "r") as file1:
    print(file1.read())

print("\n--- Destination File Content (No Comments) ---")
with open(destination, "r") as file2:
    print(file2.read())