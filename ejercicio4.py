def numero (m,x,y):
    div_x = m/x
    div_y = m/y

    if div_x % 2 ==0 and div_y % 2==0:
        print("Si es divisible con x , y ")
    else:
        print("No es divisible con x, y ")
    
m = int(input("Ingrese el numero m : "))
while m<=0 :
    m=int(input("Ingrese el numero m : "))

x = int(input("Ingrese el numero X :"))
while x<=0 :
    x = int(input("Ingrese el numero x : "))

y = int(input("Ingrese el numero y : "))
while y<=0 :
    y = int(input("Ingrese el numero y : "))

numero(m,x,y)
    
