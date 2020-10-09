import winsound
import ifcopenshell
import json
import os


### set the same dir name in grasshopper
dirpath="C:\\nir_dev\\xyz" # 1. USER - SET DIRECTORY 
outfilename = dirpath+"\\abc.txt"     # 2. USER - SET OUTPUT FILENAME

#####   prints to screen - picked up by c# in GH
#####   write it to intermediate file - picked up by c# in GH

#### some ifcopenshell functions
ifc_file = ifcopenshell.open(dirpath+'\\Project1.ifc') # 2. USER - SET IFC FILENAME # NOT related to GH
data="directory: "+str(dirpath)+"\n"
products = ifc_file.by_type('ifcProduct')
for prod in products:
    data+=prod.is_a() +"\n"
print("output filepath\\name: ", outfilename)
with open(outfilename, "w") as f:
    f.writelines(data)

print(data)


print("write to file complete")

frequency = 250  
duration = 1000  
winsound.Beep(frequency, duration)



