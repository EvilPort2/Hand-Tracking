import shutil
import glob
import random

xml_files = glob.glob('images/*.xml')
random.shuffle(xml_files)
random.shuffle(xml_files)
random.shuffle(xml_files)

for n, xml_file in enumerate(xml_files):
	if n < int(len(xml_files)*0.5):
		shutil.move(xml_file, 'images/train/')
	else:
		shutil.move(xml_file, 'images/test/')