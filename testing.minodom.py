# coding: utf-8
from xml.dom import minidom
import zipfile
zf = zipfile.ZipFile(filepath, 'r', compression=zipfile.ZIP_DEFLATED, allowZip64=True)
filename = 'ryuko_vol1.epub'
zf = zipfile.ZipFile(filepath, 'r', compression=zipfile.ZIP_DEFLATED, allowZip64=True)
filepath = 'ryuko_vol1.epub'
zf = zipfile.ZipFile(filepath, 'r', compression=zipfile.ZIP_DEFLATED, allowZip64=True)
container = zf.read('META-INF/container.xml')
print(container)
containerXml = minidom.parseString(container)
print
print(container)
print(containerXml)
containerXml.getElementsByTagName('rootfiles').first()
containerXml.getElementsByTagName('rootfiles')[0]
containerXml.getElementsByTagName('rootfiles')[0].attributes
containerXml.getElementsByTagName('rootfiles')[0].attributes['full-path']
containerXml.getElementsByTagName('rootfiles')[0].attributes.length
containerXml.getElementsByTagName('rootfile')[0].attributes.length
containerXml.getElementsByTagName('rootfile')[0].attributes['full-path']
containerXml.getElementsByTagName('rootfile')[0].attributes['full-path'].value
contentOpf = './content.opf'
zf = zipfile.ZipFile(filepath, 'r', compression=zipfile.ZIP_DEFLATED, allowZip64=True)
get_ipython().run_line_magic('doc', 'open')
help open
help(open)
get_ipython().run_line_magic('pinfo', 'open')
containerFile = open('./container.opf', 'b')
get_ipython().run_line_magic('pinfo', 'open')
containerFile = open('./container.opf', mode='b')
get_ipython().run_line_magic('pinfo', 'open')
get_ipython().run_line_magic('pinfo', 'open')
containerFile = open('./container.opf', mode='rb')
contentFile = open('./content.opf', mode='rb')
print(contentFile)
minidom.parseString(open('./content.opf'))
minidom.parseString(open('./content.opf', mode='rb'))
minidom.parseString(open('./content.opf', mode='rb').readlines())
minidom.parseString(open('./content.opf','rb'))
f = open('./content.opf','rb').read()
f
print(f)
contentXml = minidom.parseString(f)
contentXml
contentXml.firstChild.tagName
