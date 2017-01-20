# Import the os module, for the os.walk function
import os
import shutil
 
# Set the directory you want to start from
rootDir = './June_eng'
monthDir = ''
fileCnt = 0
newFileCnt = 0
for dirName, subdirList, fileList in os.walk(rootDir):
	for fname in fileList:
		if fname.find('.pdf') > -1:
			#print dirName
			monthDir = dirName.split('\\')[2]
			#print monthDir
			filename_split = fname.strip().split("_")
			school_id = filename_split[0]
			#print school_id
			newFileName = 'SDMC_'+school_id+'.pdf'
			#print newFileName
			fileCnt = fileCnt + 1
			if school_id.isdigit() and monthDir.isdigit():
				if not os.path.exists('./pdfs/2016/'+monthDir+'/english/'):	
					os.makedirs('./pdfs/2016/'+monthDir+'/english/')
				if os.path.exists('./pdfs/2016/'+monthDir+'/english/'+newFileName):
					#print "Came here"
					if os.path.exists('./pdfs/2016/'+monthDir+'/english/'+newFileName.rstrip('.pdf')+'_1'+'.pdf'):
						shutil.copy(dirName+'/'+fname, './pdfs/2016/'+monthDir+'/english/'+newFileName.rstrip('.pdf')+'_2'+'.pdf')
					else:
						shutil.copy(dirName+'/'+fname, './pdfs/2016/'+monthDir+'/english/'+newFileName.rstrip('.pdf')+'_1'+'.pdf')
					newFileCnt = newFileCnt + 1
				else:
					shutil.copy(dirName+'/'+fname, './pdfs/2016/'+monthDir+'/english/'+newFileName)
					newFileCnt = newFileCnt + 1	
			else:
				print school_id
				print("Error in filename at month: %s " % dirName + fname)
				print("Error in filename: %s " % dirName + fname)
print fileCnt, newFileCnt