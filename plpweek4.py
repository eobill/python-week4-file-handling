def modify_file_content(content):
    """
    Modify the content of the file as needed.
    For this example, let's convert the text to uppercase.
    """
    return content.upper()

def main():
    # Ask the user for the filename to read
    filename = input("Enter the filename to read: ")
    
    try:
        # Attempt to open and read the file
        with open(filename, 'r') as file:
            content = file.read()
        
        # Modify the content
        modified_content = modify_file_content(content)
        
        # Write the modified content to a new file
        new_filename = 'plpweek4.txt'
        with open(new_filename, 'w') as new_file:
            new_file.write(modified_content)
        
        print(f"Content successfully modified and written to '{new_filename}'")
    
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except PermissionError:
        print(f"Error: The file '{filename}' cannot be read due to permission issues.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
