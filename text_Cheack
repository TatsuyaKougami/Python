# -*- coding: utf-8 -*-
import os
import difflib

dir_path = r'C:\Users\****\Desktop\text_Check'

file1_name = 'file1.txt'
file2_name = 'file2.txt'

file1_path = os.path.join(dir_path, file1_name)
file2_path = os.path.join(dir_path, file2_name)

file1 = open(file1_path, encoding="utf-8")
file2 = open(file2_path, encoding="utf-8")

diff = difflib.HtmlDiff()

output_name = 'diff.html'
output_path = os.path.join(dir_path, output_name)

output = open(output_path, 'w', encoding="utf-8")
output.writelines(diff.make_file(file1, file2))

file1.close()
file2.close()
output.close()
