b={1:2,2:3,3:4,4:5,0:0}
c={2:2,3:3,4:4,5:5,0:0}

for k,v in b.items():
    for x,z in c.items():
        if (k,v)==(x,z):
            print (k,v)
    
