
with open("my_data.txt", "w") as file:
    file.write("Hello, this is the first line.\n")
    file.write("This file is created using Python.\n")

print("File written successfully.")

with open("my_data.txt", "r") as file:
    content = file.read()
    print("\n--- File Content ---")
    print(content)

with open("my_data.txt", "a") as file:
    file.write("Adding a third line using append mode.\n")

print("\nNew line appended.")


with open("my_data.txt", "r") as file:
    updated_content = file.read()
    print("\n--- Updated File Content ---")
    print(updated_content)
