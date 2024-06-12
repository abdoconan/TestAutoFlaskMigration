
from src import create_app
from flask_migrate import current, heads


if __name__ == "__main__":
    # with open('changed_files.txt', 'r') as file:
    #     changed_files = file.readlines()

    # # Process the list of changed files
    # for changed_file in changed_files:
    #     print(changed_file.strip())
    with create_app().app_context():
        heads(directory="migrations", verbose=False)

    

