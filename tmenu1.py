#
#  - Contributor -  Michael Ebanks
#
#
#
import locationlist as loclist
#
#
#
#
def menu():
    print(" Choices")
    print("1 - New York State\n2 - New York City\n3 - Washington\n4 - Seattle\n5 - California\n6 - Los Angeles\n7 - Texas\n8 - Houston\n9 - Illinois\n10 - Chicago")

    while True:
        try:
            selection=int(input("Please Select:"))
            if int(selection) >= 1 and selection <= 10:
                break
            else:
                raise
        except:
            print("------------")
            print("[[[ Please Choose 1 - 10  ]]]")
            print("------------")
            continue
    return selection


def getloc(selection):
    if int(selection) ==1:
        fname = loclist.locations[0]
        loccoordinates = loclist.locations[1]
    elif selection == 2:
        fname = loclist.locations[2]
        loccoordinates = loclist.locations[3]
    elif selection == 3:
        fname = loclist.locations[4]
        loccoordinates = loclist.locations[5]
    elif selection == 4:
        fname = loclist.locations[6]
        loccoordinates = loclist.locations[7]
    elif selection == 5:
        fname = loclist.locations[8]
        loccoordinates = loclist.locations[9]
    elif selection == 6:
        fname = loclist.locations[10]
        loccoordinates = loclist.locations[11]
    elif selection == 7:
        fname = loclist.locations[12]
        loccoordinates = loclist.locations[13]
    elif selection == 8:
        fname = loclist.locations[14]
        loccoordinates = loclist.locations[15]
    elif selection == 9:
        fname = loclist.locations[16]
        loccoordinates = loclist.locations[17]
    elif selection == 10:
        fname = loclist.locations[18]
        loccoordinates = loclist.locations[19]
    else:
        print("------------")
        print("[[[ EXIT ]]]")
        print("------------")
        exit(1)
    return({"locID" : fname, "coordinates": loccoordinates})


# selection = menu()
# locinfo = getloc(selection)
#mylocname = locinfo["file_name"]
#mycoordinates = locinfo["loccoordinates"]
#print("LOCATION:    " + str(mylocname))
#print("COORDINATES: " + str(mycoordinates))

