p1={"nombre":"juan", "apellido":"toro","edad":18}
p2={"nombre":"carlos", "apellido":"ruibo","edad":38}
p3={"nombre":"pablo", "apellido":"raul","edad":90}
p4={"nombre":"angel", "apellido":"peña","edad":65}

l=[p1,p2,p3,p4]
for i in l:
    if i["edad"]>20 and i["edad"] <70:
        print(i["nombre"],i["apellido"])