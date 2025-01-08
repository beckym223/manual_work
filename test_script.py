import subprocess
import os
import logging
def git_commit(path: str, message = "hello")->None:
    """
    Commit changes from a specific file or directory in the repository to Git.

    Args:
        path (str): The file or directory containing the changes to commit.
        message (str): The commit message.
    """
    msg:str = message if message is not None else f"Modified {path}"
    try:
        if not os.path.exists(path):
            subprocess.run(["git", "rm", path], check=True,capture_output=True)
            # do something here to check if it's 
        elif os.path.isdir(path):
            # Stage changes in the specified directory
            subprocess.run(["git", "add", f"{path}/."], check=True)
        elif os.path.isfile(path):
            # Stage changes in the specified file
            subprocess.run(["git", "add", path], check=True)
        else:
            raise ValueError(f"The specified path '{path}' is neither a file nor a directory.")
        
        # Check if there are any staged changes
        result = subprocess.run(
            ["git", "diff", "--cached", "--quiet"],
            check=False,
            capture_output=True
        )
        
        if result.returncode == 1:  # Changes are staged
            subprocess.run(["git", "commit", "-m", msg], check=True)
            logging.info(f"Committed changes from {path} with message: '{msg}'")
        else:
            logging.info(f"No changes to commit in directory: {path}")
    
    except subprocess.CalledProcessError as e:
        logging.error(f"Git operation failed: {e}")
        raise
def main(name):
    with open('test.txt','a') as f:
        f.write(name)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 5:
        print("Usage: python text_cleaning.py <source_dir> <dest_dir> <log_file> <commit_changes>")
        sys.exit(1)

    name = sys.argv[1]
    # dest_dir = sys.argv[2]
    # log_file = sys.argv[3]
    # commit_changes = sys.argv[4].lower() == "true"

    main(name)