# coding: utf-8
from glob import glob
glob('/Users/hugo/Books/')
glob('/Users/hugo/Books/*.epub')
import os
os.pathsep()
os.pathsep
os.name
os.listdir('/Users/hugo/Books/')
os.listdir('/Users/hugo/Books/*.epub')
basefilename
os.path.basename(glob('~/Books/*.epub'))
files = [os.path.basename(f) for f in  glob('~/Books/*.epub')]
print(files)
glob('~/Books/*.epub')
glob('/Users/hugo/Books/*.epub')
files = [os.path.basename(f) for f in  glob('/Users/hugo/Books/*.epub')]
print(files)
import ZipFile
import zipfile
from zipfile import ZipFi;e
from zipfile import ZipFile
ebook = ZipFile('./ryuko_vol1.epub')
ebook.infoList()
ebook.infoList
ebook
ebook.printdir()
ebook.namelist()
import re
p = re.compile('content.opf')
filtered = [f for f in ebook.namelist() if p.match(f)]
print(filtered)
ebook.namelist()
filenames = ebook.namelist()
p = re.compile('^.*\.(opf)$')
filtered = [f for f in ebook.namelist() if p.match(f)]
filtered
filtered.first()
filtered.first
filtered[0]
ebook.read(filtered[0])
from lxml import etree
doc = etree.XML(ebook.read(filtered[0]))
doc
print(doc.findtext('metadata'))
print(doc.Element("metadata"))
doc
doc.tag
doc[0]
doc = etree.fromstring(ebook.read(filtered[0]))
doc.tag
etree.tostring(doc)
doc.tag
doc.getmembers()
vars(doc)
dir(doc)
doc.tag
doc.findall('{http://www.idpf.org/2007/opf}package')
ns = {'opf': 'http://www.idpf.org/2007/opf}package'}
doc.findall('metadata', ns)
doc.findall('package', ns)
open("./container.xml")"
open("./container.xml")
from xml.dom import minidom
minidom.parseString(open('./container.xml'))
get_ipython().run_line_magic('save', '')
