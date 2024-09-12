print("ejemplo de funciones")
def hola():
 print("Alguien uso la funcion hola")
def chat(mensa):
 print(mensa)
def ellacontesta(mensa):
 print(f"chat ella :{mensa}")
def escribenombre(ap,n):
 print(f"tu nombre completo es :{n} {ap}")
def suma(a,b):
 s=a+b
 return s
def resta(a,b):
 s=a-b
 return s
def multi(a,b):
 s=a*b
 return s
def divicion(a,b):
 s=a/b
 return s
##DIEGO ALI LEDEZMA CARBAJAL
hola()
chat("que bonita estas mi amor")
ellacontesta("gracias")
escribenombre("ledezma","ali")
print("operacion suma")
c1=int(input("ingresa un numero"))
c2=int(input("ingresa un numero"))
damesuma=suma(5,7)
print(f"la suma de {c1} + {c2} = {damesuma}")
print("operacion resta")
c3=int(input("ingresa un numero"))
c4=int(input("ingresa un numero"))
dameresta=resta(5,7)
print(f"la resta de {c3} - {c4} = {dameresta}")
print("operacion multiplicacion")
c5=int(input("ingresa un numero"))
c6=int(input("ingresa un numero"))
damemulti=multi(5,7)
print(f"la multiplicacion de {c5} * {c6} = {damemulti}")
print("operacion divicion")
c7=int(input("ingresa un numero"))
c8=int(input("ingresa un numero"))
damediv=divicion(5,7)
print(f"la divicion de {c7} + {c8} = {damediv}")

