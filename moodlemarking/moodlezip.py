#!/usr/bin/env python3
import os
import sys
import argparse
import zipfile

def zip_files(root_directory, output_zip, verbose):
    # Create a zip file for storing the renamed files
    with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        # Loop through all subfolders
        for foldername in os.listdir(root_directory):
            folder_path = os.path.join(root_directory, foldername)

            # Check if it's a directory
            if os.path.isdir(folder_path):
                if verbose:
                    print(f"Examining subdirectory: {folder_path}")

                # Get a list of files in the "File submissions" folder
                submissions_folder = os.path.join(folder_path, "File submissions")
                files = os.listdir(submissions_folder)

                if verbose:
                    print(f"    In the 'File submissions' folder are {files}")

                # Dictionary to store file extensions and their counts
                extension_counts = {}

                for file in files:
                    # Split the foldername using underscore as separator
                    parts = foldername.split('_')

                    # Ensure it has at least 2 parts (ZZZZ and Xyyyyyyyy)
                    if len(parts) >= 2:
                        new_filename = parts[1]  # Get the Xyyyyyyyy part
                        _, extension = os.path.splitext(file)

                        # Check if the file is not hidden and the extension is not empty
                        if not file.startswith(".") and extension:
                            # Check if the extension is already in the dictionary
                            if extension in extension_counts:
                                # If it is, exit with an error message
                                print(f"Error: Duplicate extension found in '{submissions_folder}': {extension}")
                                sys.exit(1)

                            # If not, add it to the dictionary
                            extension_counts[extension] = 1

                            # Add the renamed file to the zip archive
                            file_path = os.path.join(submissions_folder, file)
                            zipf.write(file_path, arcname=f"{new_filename}{extension}")

                            if verbose:
                                print(f"    Added to zip: {file_path} as {new_filename}{extension}")
                                
def main():
    parser = argparse.ArgumentParser(description="Add renamed files to a zip archive.")
    parser.add_argument("root_directory", help="The root directory containing subdirectories.")
    parser.add_argument("output_zip", help="Name of the output zip file.")
    parser.add_argument("--verbose", action="store_true", help="Print diagnostic messages.")

    args = parser.parse_args()
    zip_files(args.root_directory, args.output_zip, args.verbose)

if __name__ == "__main__":
    main()
