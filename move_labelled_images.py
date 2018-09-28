import cv2
import glob
import shutil

xml_files = glob.glob('augmented/*.xml')

for xml_file in xml_files:
	print(xml_file)
	jpg_file = xml_file.replace('.xml', '.jpg')
	try:
		shutil.move(xml_file, 'images/')
		shutil.move(jpg_file, 'images/')
	except:
		print(xml_file, jpg_file)
		continue