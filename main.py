 # This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
import os


def bulk_rename(folder_path, prefix):
    try:
        files = os.listdir(folder_path)
        count = 1

        for file in files:
            old_path = os.path.join(folder_path, file)

            if os.path.isfile(old_path):
                extension = os.path.splitext(file)[1]
                new_name = f"{prefix}_{count}{extension}"
                new_path = os.path.join(folder_path, new_name)

                os.rename(old_path, new_path)
                print(f"Renamed: {file} → {new_name}")
                count += 1

        print("\nAll files renamed successfully!")

    except Exception as e:
        print("Error:", e)


# User Input
path = input("Enter folder path: ")
prefix = input("Enter new file prefix: ")

bulk_rename(path, prefix)
