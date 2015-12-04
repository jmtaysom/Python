# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 20:20:33 2015

@author: jmtaysom
"""
import os
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument

# This section needs to be edited
for root, dirs, files in os.walk("/mydir"):
    for file in files:
        if file.endswith(".txt"):
             print(os.path.join(root, file))

# This section currently works for a single pdf.
path = r'/home/jmtaysom/Python/PDF'
old_name = "Allocating Treasure"
full_path = os.path.join(path,old_name)
fp = open(full_path, 'rb')
parser = PDFParser(fp)
doc = PDFDocument(parser)
name = doc.info[-1]['Title'].decode("utf-8") +'.pdf'
fp.close()
new_path = os.path.join(path, name)
os.rename(full_path,new_path)