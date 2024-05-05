import os

def get_project_root():
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    print("script_dir: ", script_dir)

    # Get the root directory of the project by going up two levels from the script directory
    project_root = os.path.abspath(os.path.join(script_dir, '../..'))

    return project_root

# Example input: "audio/temp/temp.mp3"
def get_path_from_project_root(relative_path):
    # Get the root directory of the project
    project_root = get_project_root()

    # Get the absolute path of the file by joining the project root and the relative path
    file_path = os.path.join(project_root, relative_path)

    return file_path