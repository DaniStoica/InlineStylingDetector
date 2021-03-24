# Inline Styling Detector

This small but efficient Python program aims to detect Inline Styling in HTML files.

# About

The program was developed in Python 3.9.1. 

The result of parsing the project directory will be a JSON file with a structure specially designed to represent a properties file for Dx-Platform.

# Requirements

You must have Python installed on your machine.
In order to be able to see the results from output file, you must download Dx-Platform and upload the properties file in there.

# Installation

You can download or clone our project from Github

..or Docker



# How To Use It

1. Copy the "parser.py" and "inline-style-detector.sh/bat" files to **the same directory as the project directory**.
For example:
![example](https://user-images.githubusercontent.com/48685393/112371832-bc55b680-8ce7-11eb-8171-ff3db919eebe.png)

2. Run inline-style-detector.sh/bat 
3. Type in your project directory name ( for previous example: "ExampleProject" ) and hit Enter
4. Your result.json file will be generated in the same folder

Output file structure:
![json](https://user-images.githubusercontent.com/48685393/112372627-b2808300-8ce8-11eb-8c47-30c906c81d2f.png)

**Make sure your project has .html files to avoid generating an empty json file**

# License 

Distributed under the Apache License 2.0
