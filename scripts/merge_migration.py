with open('changed_files.txt', 'r') as file:
    changed_files = file.readlines()

# Process the list of changed files
for changed_file in changed_files:
    print(changed_file.strip())