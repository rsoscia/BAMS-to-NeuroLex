import os
import zipfile
import sys

#zipName = zipfile.ZipFile("/Users/ryansoscia/BAMS-to-NeuroLex/Data/")
#zipName = zipfile.ZipFile('/Users/ryansoscia/BAMS-to-NeuroLex/Data/')

zip1 = zipfile.ZipFile("/Users/ryansoscia/BAMS-to-NeuroLex/Data/BAMS1.zip")
zip2 = zipfile.ZipFile("/Users/ryansoscia/BAMS-to-NeuroLex/Data/BAMS2.zip")
zip3 = zipfile.ZipFile("/Users/ryansoscia/BAMS-to-NeuroLex/Data/BAMS3.zip")


zipfile.read(zipfile.ZipFile("/Users/ryansoscia/BAMS-to-NeuroLex/Data/BAMS3.zip"))



#zipList = [zip1, zip2, zip3]

#for f in zipList.namelist():
#	if f.endswith('/'):
#		os.makedirs(f)
#	else:
#		zipList.extract(f)

#if __name__ == 'main':
#	zipList = ['BAMS1.zip', 'BAMS2.zip', 'BAMS3.zip']
#	for zipfile in zipList:
#		extractAll(zipName)



#ZipFile.read(zip1)
#extract(zip1)