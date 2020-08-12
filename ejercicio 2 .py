print("ingrese la longitud ancho del poligono, indicar si es un cuadrado o un rectangulo ")

longitud = float(input("longitud: "))
ancho = float(input("ancho: "))
poligono = str(input("cuadrado o rectangulo: "))

if poligono == "cuadrado" : 
    area = longitud * ancho
    print("el area del cuadrado es : " , str(area))

if poligono == "rectangulo" :
     perimetro = longitud*2 + ancho*2
     print("el perimetro del rectangulo es : " , str(perimetro))   
