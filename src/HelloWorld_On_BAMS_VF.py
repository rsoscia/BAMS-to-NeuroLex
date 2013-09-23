import os
import zipfile
#from zipfile import ZipFile as zip


zipName = zipfile.ZipFile("/Users/ryansoscia/BAMS-to-NeuroLex/Data/")



def extractAll(zipName):
    z = zip(zipName)
    for f in z.namelist():
        if f.endswith('/'):
            os.makedirs(f)
        else:
            z.extract(f)

if __name__ == '__main__':
    zipList = ['BAMS1.zip', 'BAMS2.zip', 'BAMS3.zip']
    for zip in zipList:
        extractAll(zipName)
        
