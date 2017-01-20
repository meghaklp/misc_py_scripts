# Import the os module, for the os.walk function
import os
import shutil
 
# Set the directory you want to start from
rootDir = './Old'
langDir = ''
yearDir = ''
monthDir = ''
month_map = {'April':'04', 'Aug':'08', 'Dec':'12', 'dec':'12', \
			'Feb':'02','July':'07', 'June':'06', 'Mar':'03', 'May':'05', \
			'MayENG.pdf':'05', 'nov':'11', 'Nov':'11', 'oct':'10', 'Oct':'10',\
			'Sept':'09', 'Spet':'09', 'Sep':'09', 'sep':'09', 'aug':'08', 'feb':'02',\
			'Jul':'07', 'july':'07', 'jul':'07', 'jun':'06', 'Jun':'06', 'Jan':'01', \
			'May.pdf':'05', 'Aug.pdf':'08', 'feb,':'02', 'jan':'01',\
			'janeng':'01', 'July.pdf':'07', 'June.pdf':'06', 'june.pdf':'06',\
			'march':'03', 'mar':'03', 'Dec.pdf':'12', 'fab':'02'}
for dirName, subdirList, fileList in os.walk(rootDir):
 	if dirName not in ['./2016','./2015']:
		if dirName.find('Kannada_SDMC') > 0 :
			langDir = "kannada"
		elif dirName.find('English_SDMC') > 0:
			langDir = "english"
		else:
			print("First loop or Error in language : %s " % dirName)
		
		if dirName.find('2015') > 0:
			yearDir = "2015"
		elif dirName.find('2016') > 0:
			yearDir = "2016"
		else:
			print("First loop or Error in year : %s " % dirName)
		
		for fname in fileList:
			if fname.find('_') > -1:
				shutil.move(dirName+'/'+fname, dirName+'/'+fname.replace('_',' '))
			fname = fname.replace('_',' ')
			filename_split = fname.strip().split(" ")
			if filename_split[0].lower().find("klp") > -1:
				if filename_split[1].lower().find("i") > -1:
					school_id = filename_split[2]
					school_id.strip('.')
					school_id.strip(',')
					if len(filename_split)>4:
						if filename_split[3].isdigit():
							print("Error in filename at 3: %s " % dirName + fname)
						elif filename_split[3].strip() in month_map:
	   						monthDir = month_map[filename_split[3].strip()]
	   					elif filename_split[4].strip() in month_map:
	   						monthDir = month_map[filename_split[4].strip()]
	   					else:
	   						print("Error in filename at month: %s " % dirName + fname)
				else:
					school_id = filename_split[1]
					school_id.strip('.')
					school_id.strip(',')

					if len(filename_split)>3:
						if filename_split[2].isdigit():
							print("Error in filename at 2: %s " % dirName + fname)
						elif filename_split[2].strip() in month_map:
	   						monthDir = month_map[filename_split[2].strip()]
	   					elif filename_split[3].strip() in month_map:
	   						monthDir = month_map[filename_split[3].strip()]
	   					else:
	   						print("Error in filename at month: %s " % dirName + fname)
	   			if school_id.isdigit() and monthDir.isdigit():
	   				if not os.path.exists('./New/' + yearDir+'/'+monthDir+'/'+langDir+'/'):
						os.makedirs('./New/'+ yearDir+'/'+monthDir+'/'+langDir+'/')
					newFile = './New/'+ yearDir+'/'+monthDir+'/'+langDir+'/SDMC_'+school_id+'.pdf'
					if os.path.exists(newFile):
						if os.path.exists(newFile.rstrip('.pdf')+'_1'+'.pdf'):
							shutil.move(dirName+'/'+fname, newFile.rstrip('.pdf')+'_2'+'.pdf')
						else:
							shutil.move(dirName+'/'+fname, newFile.rstrip('.pdf')+'_1'+'.pdf')
					else:
						shutil.move(dirName+'/'+fname, newFile)

				else:
					print("Error in filename: %s " % dirName + fname)
			#school = School.objects.get(pk=school_id)
	   		else:
				print("Error in filename: %s " % dirName + fname)
