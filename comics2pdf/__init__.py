# Converts .cbr and .cbz files to .pdf
#
# Use:  python comic2pdf.py
# -- Only works with comicbook files that contain JPG's (for now).
# -- The script should be in the same directory the file(s) to convert are in.
#
# Author:  MComas1
# Date:  14-09-18
# License:  You can do what you want with it.
# Mainly based on a script by Bransorem (https://github.com/bransorem/comic2pdf)
# Turned to a command-line tool by theunderdog (https://github.com/theunderdog)
# import os, sys, zipfile, patoolib
# from PIL import Image
# import PIL.ExifTags
def main_func():
    try:
        import os, sys, zipfile, patoolib
        from PIL import Image
        import PIL.ExifTags
    except Exception as ex:
        print('installing dependencies...')
        os.system('pip install pillow')
        main_func()
        quit()
    class main_class():
        def __init__(self):

            self.failed = False

        def nlog_info (self,msg, out=open("comic2pdf_log.txt","a")):
            """Print info message to stdout (or any other given output)."""
            print("patool:", msg, file=out)

        def olog_info (self,msg, out=sys.stdout):
            """Print info message to stdout (or any other given output)."""
            print("patool:", msg, file=out)

        def handlerar2(self,filein):
        	tmp_dir = os.getcwd()+"\\Teemp\\"
        	os.mkdir(tmp_dir)
        	original = sys.stdout
        	sys.stdout = open("comic2pdf_log.txt","a")
        	patoolib.util.log_info = self.nlog_info
        	patoolib.extract_archive(filein, outdir=tmp_dir)
        	newfile = filein.replace(filein[-4:],".pdf")
        	self.toPDF2(newfile,tmp_dir,7)
        	self.cleanDir(tmp_dir)
        	print("------------------------------------------------------------")

        	sys.stdout = original
        	print("\""+newfile[:-4]+"\" successfully converted!")

        def handlezip(self,filein):
        	zip_ref = zipfile.ZipFile(filein, 'r')
        	tmp_dir = os.getcwd()+"\\Teemp\\"
        	zip_ref.extractall(tmp_dir)
        	zip_ref.close()
        	newfile = filein.replace(filein[-4:],".pdf")
        	self.toPDF2(newfile,tmp_dir,0)
        	try:
        		self.cleanDir(tmp_dir)
        	except:
        		aaa = 223
        	print("\""+newfile[:-4]+"\" successfully converted!")

        def toPDF2(self,filename, newdir,ii):
        	ffiles = os.listdir(newdir)
        	if (len(ffiles) == 1):
        		self.toPDF2(filename,newdir+ffiles[0]+"\\",ii)
        	else:
        		# imagelist is the list with all image filenames
        		im_list = list()
        		firstP = True
        		im = None
        		for image in ffiles:
        			if (image.endswith(".jpg") or image.endswith(".JPG") or image.endswith(".jpeg") or image.endswith(".JPEG")):
        				im1 = Image.open(newdir+image)
        				try:
        					im1.save(newdir+image,dpi=(96,96))
        				except:
        					aaaaa = 4

        				if (firstP):
        					im = im1
        					firstP = False
        				else: im_list.append(im1)
        			else: continue
        		#print(exif)
        		im.save(filename, "PDF" ,resolution=100.0, save_all=True, append_images=im_list)
        		self.cleanDir(newdir)
        	#print("OK")

        def cleanDir(self,dir):
        	try:
        		files = os.listdir(dir)
        		for file in files:
        			os.remove(dir+"\\"+file)
        		os.rmdir(dir)
        	except: print("No dir to clean!")

        def opendir(self,directory):
        	# look at all files in directory
        	#print(os.listdir(directory))
        	for file in os.listdir(directory):
        		# file extension cbr only
        		if (file[-4:] == '.cbz' or file[-4:] == '.zip'):
        			# change to zip
        			self.handlezip(file)
        		elif (file[-4:] == '.cbr' or file[-4:] == '.rar'):
        			# change to rar
        			self.handlerar2(file)
        	if self.failed:
        		print ("WARNING: some items were skipped")


    obj = main_class()
    obj.opendir(os.getcwd())
