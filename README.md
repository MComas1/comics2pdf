# comics2pdf
A script to convert comic files (cbr, cbz) to pdf, in python3. Works in Windows. Linux not tested.

## Getting Started

To use it, just place the .py script in the same directory the file(s) to convert are in and run the command:

```
python comic2pdf.py
```

### Prerequisites

Script in Python 3.6 (probably won't work with Python 2.x versions). Requires the "zipfile", "patool" and "pillow"(aka PIL) modules in order to work correctly. To install them run the following commands:

```
pip install zipfile
```
```
pip install patool
```
```
pip install pillow
```
In windows you'll need to run cmd.exe using the "run as administrator" option for those commands to work.

### Installing

Just place all the .cbr/.cbz files desired to convert to pdf in one directory, place the script in that same directory and run the following command:

```
python comic2pdf.py
```

It's a good idea to rename (before running the script) the .cbr/.cbz files that have names like "01.cbz" to "Comic Name 01.cbz", as the output .pdf will get its name from the input comic file.

## Built With

* [Python 3]

## Authors and Acknowledgments

* **MComas1**

Based on a python script by **bransorem** (https://github.com/bransorem/comic2pdf).
