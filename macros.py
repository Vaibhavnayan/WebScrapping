import os
import sys

# Import System libraries
import glob
import random
import re

sys.coinit_flags = 0 # comtypes.COINIT_MULTITHREADED

# USE COMTYPES OR WIN32COM
#import comtypes
#from comtypes.client import CreateObject

# USE COMTYPES OR WIN32COM
import win32com
from win32com.client import Dispatch

scripts_dir = "/Users/vnayan/Python_Udemy/WebScrapping"
conv_scripts_dir = "/Users/vnayan/Python_Udemy/WebScrapping"
strcode = \
'''
sub test()
   msgbox "Inside the macro"
end sub
'''

#com_instance = CreateObject("Excel.Application", dynamic = True) # USING COMTYPES
com_instance = Dispatch("Excel.Application") # USING WIN32COM
com_instance.Visible = True 
com_instance.DisplayAlerts = False 

for script_file in glob.glob(os.path.join(scripts_dir, "*.xls")):
    print ("Processing: %s" % script_file)
    (file_path, file_name) = os.path.split(script_file)
    objworkbook = com_instance.Workbooks.Open(script_file)
    xlmodule = objworkbook.VBProject.VBComponents.Add(1)
    xlmodule.CodeModule.AddFromString(strcode.strip())
    objworkbook.SaveAs(os.path.join(conv_scripts_dir, file_name))

com_instance.Quit()