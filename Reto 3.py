print('*********NOTAS DE UN ESTUDIANTE: 7 DEL 10% Y 3 DEL 90% ***********')
print()
print("Ingrese las 7 Notas del 10% ")
suma=0
nota=0
i=1
calificaciones1=[]
calificaciones2=[]
while i<=7:
    print("ingrese la Nota numero ",i)
    try:
        nota=float(input())
    except ValueError:
        print("No se puede ingresar caracteres")
        continue
    
    if nota<0 or nota>=11:
        print("NOTA NO VALIDA")
        continue
    elif nota==0:
        nota=1.0
    suma=suma+nota
    i+=1
    calificaciones1.append(nota)
promedio1=suma/7*0.1
print("Ingrese las 3  Notas del 90% ")
suma=0
i=1
while i<=3:
    print("ingrese la Nota numero ",i)
    
    try:
        nota=float(input())
    except ValueError:
        print("No se puede ingresar caracteres")
        continue
    if nota<0 or nota>=11:
        print("NOTA NO VALIDA")
        continue
    elif nota==0:
        nota=1.0
    suma=suma+nota
    i+=1
    calificaciones2.append(nota)
promedio2=suma/3*0.9
promediototal=promedio1+promedio2
print("las calificaciones del 10% son: ",calificaciones1) 
print("las calificaciones del 90% son: ",calificaciones2)
print("La Nota definitiva es ",round(promediototal,1))
print()