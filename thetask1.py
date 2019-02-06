import math
def list_ifname_ip():
    myfile = open('running-config.cfg')
    nameifdict=dict()

    for line in myfile:
        if "nameif" in line:
            mytemplist = line.split()

            next(myfile)
            templine = next(myfile)
            mylist= templine.split()

            if mytemplist[0]=='nameif':
                if mylist[0] == 'ip':
                    mytuple=(mylist[2:])
                    nameifdict[mytemplist[1]]=mytuple

    return (nameifdict)

ipconfigs = list_ifname_ip()
print(ipconfigs)


