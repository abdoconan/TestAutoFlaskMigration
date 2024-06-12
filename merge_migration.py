from typing import List, Tuple, Dict, Optional
from collections.abc import Iterable
import os
import re

from src import create_app
from flask import current_app
from alembic.script.base import ScriptDirectory, Script
from alembic.script.revision import _RevIdType
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


def classify_heads_as_current_and_merged(heads: Tuple[Script, ...]
                                         , valid_paths: List[str]
                                        ) -> Tuple[Script, List[Script]]:
    """
    Classifies migration heads as current and merged based on the provided list of valid paths.

    Args:
        heads (Tuple[Script, ...]): A tuple of Script objects representing migration heads.
        valid_paths (List[str]): A list of valid paths that contain migration revisions.

    Returns:
        Tuple[Script, List[Script]]: A tuple containing the current head and a list of merged heads.
    """
    current_head: Optional[Script] = None
    merged_heads: List[Script] = []
    for head in heads:
        if any(head.revision in path for path in valid_paths):
            merged_heads.append(head)
        else:
            current_head = head
    return current_head, merged_heads


def get_earliest_revision(revision_ids: Optional[_RevIdType]) -> Optional[str]:
    """
    Retrieves the earliest revision ID from a list of revision IDs.

    Args:
    - revision_ids (Optional[RevIdType]): A revision ID or a list of revision IDs.

    Returns:
    - Optional[str]: The earliest revision ID if available, else None.
    """
    if revision_ids is None:
        return None  # No revision IDs provided

    if isinstance(revision_ids, str):
        return revision_ids  # Single revision ID provided

    if isinstance(revision_ids, Iterable):
        if len(revision_ids) > 0:
            return revision_ids[0]  # Return the earliest revision ID from the list
        else:
            return None  # Empty list provided


def get_earliest_revision_downverision(merged_head: Script
                          , valid_paths: List[str]
                          , script: ScriptDirectory
                        ) -> Tuple[str, str]:
    """
    Get the earliest downrevision given a merged script head.

    Args:
    - merged_head (Script): The merged script head to start from.
    - valid_paths (List[str]): List of valid file paths containing revision information.
    - script (ScriptDirectory): The script directory containing revision history.

    Returns:
    - Tuple[str, str]: 
        - The earliest downrevision ID found in the valid paths.
        - the revision_id of the file
    """
    earliest_revision: Optional[str] = get_earliest_revision(merged_head.down_revision)

    revision_id = merged_head.revision
    for path in valid_paths:
        if earliest_revision in path:
            ## this means that there is multiple revisions in the same merge and need to get the first one.
            revision_script  = script.get_revision(earliest_revision)
            print(f"revision_script: {revision_script}")
            _, revision_id = get_earliest_revision_downverision(revision_script, valid_paths, script)
    path = next(filter(lambda path: revision_id in path, valid_paths))
    return path, merged_head.revision
    
def change_downrevision_file(file_path: str, revision_id: str):
    with open(file_path, 'r') as file:
        script = file.read()

    # Use regular expressions to find and replace the down_revision value
    pattern = r"(down_revision = ')([^']+')"
    replacement = r"\g<1>" + revision_id + r"'"
    script = re.sub(pattern, replacement, script)

    # Write the modified script back to the file
    with open(file_path, 'w') as file:
        file.write(script)

def main():
    file_path: str  = "changed_files.txt"
    valid_paths: List[str] =  filter_migration_files(file_path)
    if len(valid_paths) < 1:
        print("No migrations found")
        return 

    print(f"valid_paths: {valid_paths}")

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
        current_head, merged_heads = classify_heads_as_current_and_merged(heads, valid_paths)

        print(f"current_head: {current_head}")
        print(f"merged_heads: {merged_heads}")


        path_directory = os.getcwd()
        revision_id: str =  current_head.revision
        for merged_head in merged_heads:
            print(f"merged_head: {merged_head}")
            earlies_file_path, rev_id =  get_earliest_revision_downverision(merged_head, valid_paths, script)
            full_path_to_file =  os.path.join(path_directory, os.path.normpath(earlies_file_path))
            print(f"file_path: {full_path_to_file}")
            print(f"rev_id: {rev_id}")
            print(f"revision_id: {revision_id}")
            change_downrevision_file(full_path_to_file, revision_id)
            revision_id = rev_id


            
if __name__ == "__main__":
    main()

    

