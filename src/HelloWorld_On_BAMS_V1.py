



#Permission for python program to extract files located at the root

#Access the root and unzip the files

#Convert anything if it needs to be converted... 
#Parse everything

import os
import zipfile
import sys
import tempfile

from xml import etree

#zip_file = '/Users/ryansoscia/BAMS-to-NeuroLex/src/BAMMMMMM.xml.zip'
zip_file = zipfile.ZipFile('/Users/ryansoscia/BAMS-to-NeuroLex/src/BAMMMMMM.xml.zip')


#src directory file
file_name = zipfile.ZipFile('BAMMMMMM.xml.zip')
directory = '/Users/ryansoscia/BAMS-to-NeuroLex/src/'

#data directory file 
#file_name = 
#directory = 

extract(zip_file, file_name, directory)
process(path)
write(xml, file_name)
name_file(file_name)
unzip(path)
main()


def extract(zip_file, file_name, directory):
    path = directory + os.sep + file_name

    my_file = open(path, 'w') 
    my_file.write(zip_file.read(file_name))
    my_file.close()
    return path

def process(path):
    root = etree.parse(path)
    element = root.find(".//database")
    element.attrib['clustered'] = 'true'
    
    xml = etree.tostring(root, pretty_print=True)

    return xml

def write(xml, file_name):
    my_file = open(name_file(file_name), 'w')
    my_file.write(xml)
    my_file.close()

def name_file(file_name):
    return file_name.split('.')[0] + '.xml'

def unzip(path):
    TEMP_DIR = tempfile.gettempdir()

    outer_zip = zipfile.ZipFile(path)

    for name in outer_zip.namelist():
        (dir_name, file_name) = os.path.split(name)

        if file_name != '' and file_name.endswith('.zip'):

            zip_path = extract(outer_zip, name, TEMP_DIR)
            
            inner_zip = zipfile.ZipFile(zip_path)

            for n in inner_zip.namelist():
                (dn, fn) = os.path.split(n)

                if fn == '':
                    if not os.path.exists(TEMP_DIR + os.sep + dn):
                        os.mkdir(TEMP_DIR + os.sep + dn)
                else: 
                    if fn.endswith(".xml"):
                        xml_path = extract(inner_zip, n, TEMP_DIR)
                        xml_config = process(xml_path)
                        write(xml_config, file_name)

            inner_zip.close()

    outer_zip.close()

def main():
    if (len(sys.argv) == 1):
        print 'O primeiro argumento deve ser o nome do arquivo zip a ser extraido e processado'
        #print 'the first argument must be the name of the _____ zip in order to be extracted and processed'
    else:
        unzip(sys.argv[1])
        

if __name__ == '__main__':
    main()