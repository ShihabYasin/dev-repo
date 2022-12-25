import re
import os


def remove_extra_spaces(string):
  return re.sub(' +', ' ', string)


def get_columns_from_text(file_path, delimeter=' ', columns="3"):

    output_filename = "897893247582hghs.txt"
    if os.path.exists(output_filename):
        os.remove(output_filename)
        # print("File removed successfully.")

    with open(file_path, 'r') as f:
        lines = f.readlines()
    for line in lines:
        line = remove_extra_spaces(line).strip()
        print(line, file=open(output_filename, 'a'))

    # os.system(f"""cat {output_filename}""")
    os.system(f"""cut -d'{delimeter}' -f{columns} < {output_filename}""")

    if os.path.exists(output_filename):
        os.remove(output_filename)


# def get_columns_from_text(file_path='', delimeter=' ', columns="1,2"):
#     os.system(f"""cut -d'{delimeter}' -f{columns} < {file_path}""")
