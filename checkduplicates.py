# Import the os module, for the os.walk function
import os
import shutil
import hashlib
 
def all_same(items):
    return all(x == items[0] for x in items)
# Set the directory you want to start from
rootDir = '../media/meeting_reports/'
duplicate_files = {}
for dirName, subdirList, fileList in os.walk(rootDir):
	for fname in fileList:
		duplicate_files = {}
		if fname.find('.pdf') > -1:
			filename_split = fname.strip().split("_")
			if len(filename_split) > 2:
				first_file = filename_split[0]+'_'+filename_split[1]+'.pdf'
				if(first_file not in duplicate_files.keys()):
					duplicate_files[first_file] = hashlib.md5(open(dirName+'/'+first_file,'rb').read()).hexdigest()
				duplicate_files[fname] = hashlib.md5(open(dirName+'/'+fname,'rb').read()).hexdigest()
		if len(duplicate_files.keys()) > 0:
			if all_same(duplicate_files.values()):
				print dirName
				print duplicate_files


