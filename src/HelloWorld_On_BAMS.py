#import os
#import zipfile

#fh = open('BAMMMMMM.xml.zip','rb')
#print("the ZIP is of length: %s " %size(fh))

import rdflib
import os
import zipfile


#Get a Graph object
g = rdflib.Graph()

# pull in an RDF document from NeuroLex, parse, and store.
zip = zipfile.ZipFile("/Users/ryansoscia/BAMS-to-NeuroLex/src/BAMMMMMM.xml.zip")

#result = g.parse("http://neurolex.org/wiki/Special:ExportRDF/birnlex_1489", format="application/rdf+xml")
result = g.parse(extract('BAMMMMMM.xml.zip', '/Users/ryansoscia/BAMS-to-NeuroLex/src' ), format="application/rdf+xml")

print ("graph has %s statements." % len(result))






def extract(zipfilepath, extractiondir):


#def extract('BAMMMMMM.xml.zip', '/Users/ryansoscia/BAMS-to-NeuroLex/src'):
    #zip = zipfile.ZipFile(zipfilepath)
    
    #ZipFile is a class
    zip = zipfile.ZipFile('/Users/ryansoscia/BAMS-to-NeuroLex/src/BAMMMMMM.xml.zip')
    f.read(zip)
    #zip.extractall(path=/Users/ryansoscia/BAMS-to-NeuroLex/src/BAMMMMMM.xml.zip)
    
    
    unzip(sys.argv[:0])
    
    
extract('BAMMMMMM.xml.zip', '/Users/ryansoscia/BAMS-to-NeuroLex/src')