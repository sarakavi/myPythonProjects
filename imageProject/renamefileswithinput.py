import os

def rename_files(directory):
    try:
        # Get a list of files in the directory
        files = os.listdir(directory)
        
        # Filter out directories, we only want to rename files
        files = [f for f in files if os.path.isfile(os.path.join(directory, f))]
        
        # Sort files to ensure they are renamed in ascending order
        files.sort()
        
        # Loop through the files and rename them
        for index, filename in enumerate(files):
            # Split the filename into name and extension
            name, extension = os.path.splitext(filename)
            
            # Create a new filename with the index, padded with zeros for consistent sorting
            new_filename = f"{year}-{index + 1:01}{extension}"
            
            # Create full paths for the old and new filenames
            old_file = os.path.join(directory, filename)
            new_file = os.path.join(directory, new_filename)
            
            # Rename the file
            os.rename(old_file, new_file)
            
            print(f"Renamed '{filename}' to '{new_filename}'")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Get directory from user input
    directory = input("Enter the path to the directory: ")
    year = input("Enter the Year: ")
    rename_files(directory)
