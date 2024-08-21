def mezclar_diccionario(a,b):
    diccionario=a.copy()

    for c,v  in b.items():
        if c not in diccionario:
            diccionario[c]=v
    return diccionario

d={"a":1,"b":2,"c":3}
a={"b":2,"c":3,"d":4}

solucion=mezclar_diccionario(d,a)
print(solucion)