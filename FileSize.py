import os
   
def list_directory_contents(path):
    try:
        if not os.path.exists(path):
            return "The provided directory path does not exist."
       
        print(f"Contents of the directory '{path}':\n")
        for entry in os.listdir(path):
            entry_path = os.path.join(path, entry)
            if os.path.isdir(entry_path):
                print(f"Directory: {entry}")
            else:
                print(f"File: {entry}")
    except Exception as e:
        print(f"An error occurred: {e}")

list_directory_contents(".")

def report_file_sizes(directory):
    try:
        if not os.path.exists(directory):
            return "The provided directory path does not exist."
            
        if not os.path.isdir(directory):
            return "The provided path is not a directory."
            
        print(f"Files and their sizes in the directory '{directory}':\n")
        for entry in os.listdir(directory):
            entry_path = os.path.join(directory, entry)
            if os.path.isfile(entry_path):
                size = os.path.getsize(entry_path)
                print(f"File: {entry} - Size: {size} bytes")
    except Exception as e:
        print(f"An error occurred: {e}")
    
# report_file_sizes(".")
    




# Problem Statement: Develop a Python script that counts the number of files of each extension type in a directory. For instance, in a directory with five '.txt' files and three '.py' files, the script should report "TXT: 5" and "PY: 3".
# Expected Outcome: The script should accurately count and display the number of files for each extension type in the specified directory. Handle different cases of file extensions (e.g., '.TXT' and '.txt' should be considered the same).
    
def count_file_extensions(directory):
    try:
        if not os.path.exists(directory):
            return "The provided directory path does not exist."
        if not os.path.isdir(directory):
            return "The provided path is not a directory."
            
        extension_counts = {}
        
        for entry in os.listdir(directory):
            entry_path = os.path.join(directory, entry)
            if os.path.isfile(entry_path):
                _, extension = os.path.splitext(entry)
                extension = extension.lstrip('.').upper()  
                extension_counts[extension] = extension_counts.get(extension, 0) + 1
        print(extension_counts)
    except Exception as e:
        print(f"An error occurred: {e}")    

# count_file_extensions(".")

