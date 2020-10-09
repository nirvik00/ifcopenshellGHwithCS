import ifcopenshell
import json
import winsound

frequency = 2500  # Set Frequency To 2500 Hertz
duration = 1000  # Set Duration To 1000 ms == 1 second
winsound.Beep(frequency, duration)

def test1():
    ifc_file = ifcopenshell.open('./Project1.ifc') # load the ifc file
    data=""
    
    t=ifc_file.by_type('IfcWall')[0].is_a('IfcWall') # True/False
    #print('t= ', t)
    data+="t = "+str(t)+"\n"

    products = ifc_file.by_type('ifcProduct')
    for prod in products:
        #print(prod.is_a()) # prints the type of element
        data+=prod.is_a() +"\n"

    # print known properties
    print('\n\nElements:')
    for prod in products:
        #print("\n\nglobal id: ", prod.GlobalId)
        data+="\n\nglobal id: "+ str(prod.GlobalId) +"\n"
        #print("name: ", prod.Name)
        data+="name: "+ prod.Name +"\n"
        for defn in prod.IsDefinedBy:
            if defn.is_a('ifcRelDefinesByProperties'):
                property_set=defn.RelatingPropertyDefinition
                print(property_set.Name)
                data += property_set.Name+"\n"
                for prop in property_set.HasProperties:
                    if prop.is_a('IfcPropertySingleValue'):
                        try:
                            print(property.Name)
                            print(property.NominalValue.wrappedValue)
                        except:
                            pass
            
        

    print('\n\nWall:')
    wall=ifc_file.by_type('IfcWall')[0]
    for defn in wall.IsDefinedBy:        
        if defn.is_a('ifcRelDefinesByProperties'):
            property_set= defn.RelatingPropertyDefinition
            print(property_set.Name)

    print("all done")
    test2(data)
                       
        
def test2(data):
    filename = "c:\\testCSPy\\abc.txt";
    with open(filename, "w") as f:
        f.writelines(data)
    print("write to file complete")


if __name__ == "__main__":
    test1()
