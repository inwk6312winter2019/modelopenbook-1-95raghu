config=open ("running-config.cfg")
readfile=config.read()
def list_ifname_ip():
    mykeynote=dict()
    for line in readfile.split():
        word=line.strip()
        if word not in mykeynote:
            mykeynote[line]=1
        else:
            mykeynote[line]+=1
    print(mykeynote)
    myownlist=[]
    for key,value in mykeynote.items():     
        if "nameif" in mykeynote:
            myownlist.append((value,key))
    print(myownlist)
list_ifname_ip()    
                 

