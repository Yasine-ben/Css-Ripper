import re
import os

def main(input_file):
    # read the input file and extract all class and id names
    with open(input_file, 'r') as f:
        text = f.read()

    class_regex = r"(?<=className=['\"])[\w\d\s-]+(?=['\"])"
    id_regex = r"(?<=id=['\"])[\w\d\s-]+(?=['\"])"
    classes = re.findall(class_regex, text)
    ids = re.findall(id_regex, text)

    # write the extracted class and id names to a new CSS file
    filename = os.path.splitext(input_file)[0] + ".css"
    with open(filename, 'w') as f:
        for class_name in classes:
            f.write(f".{class_name} {{}}\n")
        for id_name in ids:
            f.write(f"#{id_name} {{}}\n")