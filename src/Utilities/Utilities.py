import os
import sys
from dotenv import load_dotenv

def init_dotenv():
    # Get the path of the .env file
    if getattr(sys, 'frozen', False):
        # The application is running in a PyInstaller bundle
        env_path = os.path.join(sys._MEIPASS, '.env')
    else:
        # The application is running in a normal Python environment
        env_path = get_path_from_project_root('.env')
    load_dotenv(dotenv_path=env_path)

def get_project_root():
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Get the root directory of the project by going up two levels from the script directory
    project_root = os.path.abspath(os.path.join(script_dir, '../..'))

    return project_root

# Example input: "generated/temp/temp.mp3"
# Example output: "/path/to/project/generated/temp/temp.mp3"
def get_path_from_project_root(relative_path):
    # Get the root directory of the project
    project_root = get_project_root()

    # Get the absolute path of the file by joining the project root and the relative path
    file_path = os.path.join(project_root, relative_path)

    return file_path