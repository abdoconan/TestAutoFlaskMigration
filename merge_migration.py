from typing import List, Tuple, Dict
import os

from src import create_app
from flask import current_app
from alembic.script.base import ScriptDirectory, Script
from alembic.config import Config

def filter_migration_files(file_path: str) -> List[str]:
    """
    Retrieves paths to migration files from a file containing file paths.

    Args:
        file_path (str): Path to the file containing all file paths.

    Returns:
        list: List of paths filtered to include only migration files in the 'migration/revision' path with a '.py' extension.
    """
    with open(file_path, 'r') as file:
        changed_files = file.readlines()

    folders : Dict[str, str] = {
        "grandparent_folder" : "migrations", 
        "parent_folder" : "versions"
    }

    # Strip whitespace characters and filter paths
    filtered_paths: List[str] = []
    for path in changed_files:
        path = path.strip()
        parent_folder = os.path.basename(os.path.dirname(path)).lower()
        grandparent_folder = os.path.basename(os.path.dirname(os.path.dirname(path))).lower()
        if (grandparent_folder == folders["grandparent_folder"]
            and parent_folder == folders["parent_folder"]
            and os.path.isfile(path) and path.lower().endswith('.py')):
            filtered_paths.append(path)
    return filtered_paths


def main():
    file_path: str  = "changed_files.txt"
    valid_paths: List[str] =  filter_migration_files(file_path)
    if len(valid_paths) < 1:
        print("No migrations found")
        return 


    ## create app context
    app = create_app()
    with app.app_context():
        ## geting app configuration
        config: Config = current_app.extensions['migrate'].migrate.get_config("migrations")

        ## creat script manager
        script: ScriptDirectory = ScriptDirectory.from_config(config)

        ## check if there is multiple heads 
        if len(script.get_heads()) < 2:
            print(f"the number of heads is less than two. no need for modification")
            return
        
    
        heads: Tuple[Script, ...] = script.get_revisions(script.get_heads())
        heads[0].down_revision
        print(heads)
        if len(heads) != 1:
            print("multiple head detected")
        else:
            print("everthing is fine")
        print(script.get_revisions("1e5695910a2c"))

            
if __name__ == "__main__":
    main()

    

