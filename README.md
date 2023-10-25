# Moodle Marking Tools

[Moodle](https://moodle.org) is a learning management system. It can be used to coordinate marking
of student work via 'assignments'. 

Online marking is easily accomplished for certain filetypes, such as MS Word. But mathematicians
will find it easier to download submissions in bulk, mark offline, then upload back to Moodle.

The tools in this package are designed to make this process more streamlined.

## Installation

Assuming you have a modern Python installation, just type
```
pip install moodlemarking
```
at the command prompt to install this package. **Note**: if this doesn't work, try
```
pip3 install moodlemarking
```

## Process

### Marking

* From the relevant Moodle assignment, select the submissions you wish to mark, then click 'Grading
  Action'.
* Click 'Export grading sheet' to download a CSV file of blank grades.
* Go through the proces above, selecting, 'Download submissions' from the 'Grading Action' dropdown.
  This downloads a folder of submissions.
* Mark the submissions by annotating the original submission files.
* Enter marks in the downloaded grading sheet.

### Preparing feedback for upload
* Open the command prompt / terminal.
* Type `moodlezip <root_directory> <output_zip>` where `<root_directory>` is the location of the
  folder containing the marked student submissions and `<output_zip>` is the name of the zip file
  (to be created) that will contain the feedback, ready for upload.

### Uploading marks and feedback
* Return to Moodle. Select the relevant assignment and click 'Grading Action'.
* Click 'Upload grading worksheet' and select the CSV file you edited in the previous part of the
  process.
* Again click 'Grading Actions' and select 'Upload feedback files in a zip'. Select the zip file
  you created in 'Preparing feedback for upload'.

## Adding margins

I include a separate helper tool that adds a left margin to PDFs. This margin can be used for 
additional comments.

To use the tool, simply type
```
add_margin <source_file> <output_file>
```
at the command prompt. This adds a 200-pixel blank left margin. You may specify the width of
the left margin as:
```
add_margin <source_file> <output_file> -m MARGIN_WIDTH
```

## Building the package

If you want to work on this Python package, first clone the repository then create a Python
virtual environment in the root directory via the following (you may need to replace `python` with
`python3` below if you run macOS):
```
python -m venv .venv
```
Activate the environment with
```
source .venv/bin/activate
```
To install the dependencies, run
```
pip install -r requirements.txt
```
Build the package with
```
python setup.py sdist
```

You can install this in your virtual environment by
```
pip install .
```

