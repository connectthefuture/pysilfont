#!/usr/bin/env python
'Demo script for use of ETWriter'
__url__ = 'http://github.com/silnrsi/pysilfont'
__copyright__ = 'Copyright (c) 2015 SIL International (http://www.sil.org)'
__license__ = 'Released under the MIT License (http://opensource.org/licenses/MIT)'
__author__ = 'David Raymond'

from silfont.core import execute
import silfont.etutil as etutil
from xml.etree import cElementTree as ET

argspec = [('outfile1',{'help': 'output file 1','default': './xmlDemo.xml','nargs': '?'}, {'type': 'outfile'}),
            ('outfile2',{'help': 'output file 2','nargs': '?'}, {'type': 'outfile', 'def':'_2.xml'}),
            ('outfile3',{'help': 'output file 3','nargs': '?'}, {'type': 'outfile', 'def':'_3.xml'})]

def doit(args) :
    ofile1 = args.outfile1
    ofile2 = args.outfile2
    ofile3 = args.outfile3

    xmlstring = "<item>\n<subitem hello='world'>\n<subsub name='moon'>\n<value>lunar</value>\n</subsub>\n</subitem>"
    xmlstring += "<subitem hello='jupiter'>\n<subsub name='moon'>\n<value>IO</value>\n</subsub>\n</subitem>\n</item>"

    # Using etutil's xmlitem class
    
    xmlobj = etutil.xmlitem()
    xmlobj.etree = ET.fromstring(xmlstring)
    
    etwobj = etutil.ETWriter(xmlobj.etree)
    etwobj.serialize_xml(xmlobj.write_to_xml)
    
    ofile1.write(xmlobj.outxmlstr)
    
    # Just using ETWriter
    
    etwobj = etutil.ETWriter( ET.fromstring(xmlstring) )
    etwobj.serialize_xml(ofile2.write)
    
    # Changing parameters
    
    etwobj = etutil.ETWriter( ET.fromstring(xmlstring) )
    etwobj.indentIncr = "    "
    etwobj.indentFirst = ""
    etwobj.serialize_xml(ofile3.write)
    
    # Close files and exit
    ofile1.close()
    ofile2.close()
    ofile3.close()
    return

execute("",doit, argspec)
