#!/usr/bin/env python3
import os, sys, argparse, zipfile, re

pattern = r'^X[0-9a-fA-F]{8}$'

def workonfolder(foldername, folder_path, zipf, verbose):
    if verbose:
        print(f"Examining subdirectory: {folder_path}")

    # Get a list of files in the "File submissions" folder
    submissions_folder = os.path.join(folder_path, "File submissions")
    try:
        files = os.listdir(submissions_folder)
    except FileNotFoundError:
        # Handle the case where the "File submissions" folder doesn't exist
        print(f"Warning: 'File submissions' folder not found in {foldername}. Skipping.", file=sys.stderr)
        return

    if verbose:
        print(f"    In the 'File submissions' folder are {files}")

    # Remove the mac custom attributes file
    files = [file for file in files if file != '.DS_Store']
    num_files = len(files)
    if num_files == 0:
        print(f"Error: No submission file found in {foldername}. Halting.", file=sys.stderr)
        sys.exit(1)
    elif num_files > 1:
        print(f"Error. More than one file found in {foldername}. Halting.", file=sys.stderr)
        sys.exit(1)

    # Split the foldername using underscore as separator
    parts = foldername.split('_')
    # Ensure it has at least 2 parts (ZZZZ and Xyyyyyyyy)
    if len(parts) >= 2:
        new_filename = parts[-1]  # Get the Xyyyyyyyy part
        if not re.match(pattern, new_filename):
            print(f"Error: Student folder {foldername} does not conform to naming convention. Halting.", file=sys.stderr)
            sys.exit(1)
    else:
        print(f"Error: Student folder {foldername} does not conform to naming convention. Halting.", file=sys.stderr)
        sys.exit(1)

    for file in files:
        _, extension = os.path.splitext(file)

        # Add the renamed file to the zip archive
        file_path = os.path.join(submissions_folder, file)
        zipf.write(file_path, arcname=f"{new_filename}{extension}")

        if verbose:
            print(f"    Added to zip: {file_path} as {new_filename}{extension}")

def zip_files(root_directory, output_zip, verbose):
    # Create a zip file for storing the renamed files
    with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        # Loop through all subfolders
        for foldername in os.listdir(root_directory):
            folder_path = os.path.join(root_directory, foldername)

            # Check if it's a directory
            if os.path.isdir(folder_path):
                workonfolder(foldername, folder_path, zipf, verbose)
                                
def main():
    parser = argparse.ArgumentParser(description="Creates a zipped file of marked submissions from a "\
                                     "folder of marked downloaded Moodle submissions.")
    parser.add_argument("root_directory", help="The root directory containing one folder per student "\
                        "submission.")
    parser.add_argument("output_zip", help="Name of the output zip file.")
    parser.add_argument("--verbose", action="store_true", help="Print diagnostic messages.")

    args = parser.parse_args()
    zip_files(args.root_directory, args.output_zip, args.verbose)

if __name__ == "__main__":
    main()
