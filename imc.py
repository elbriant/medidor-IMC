 # Calculo de peso ideal

print("¡Calcule su peso ideal!")
# obtener variables
Nombre = str(input("Ingrese su nombre: "))
Genero = int(input("Ingrese su genero [Hombre (1), Mujer(2)]: "))
Edad = int(input("Ingrese su edad: "))
Peso = float(input("Ingrese su peso (Kg): "))
Altura = float(input("Ingrese su altura (Mt): "))

# algunos calculos
IMC = Peso/Altura**2
pimin = 18.5 * Altura**2
pimax = 24.99 * Altura**2
pi = (pimin + pimax)/2
rec = 0
k = 0
pia =-1
alturacm = Altura*100

if Genero == 1:
    k = 4
elif Genero == 2:
    k = 2


pilorentz = alturacm-100-((alturacm-150)/k)


if Peso < pi:
    #faltan
    rec = pi - Peso
    pia = 0
elif Peso == pi:
    #peso ideal
    rec = pi
    pia = 1
elif Peso > pi:
    #sobra
    rec = Peso - pi
    pia = 2

# clasificacion de imc
IMCstatus = ""
if IMC < 16:
    IMCstatus = "Desnutrición severa"
elif IMC >= 16.1 and IMC <= 18.4:
    IMCstatus = "Destrutricion moderada"
elif IMC >= 18.5 and IMC <= 22:
    IMCstatus = "Bajo peso"
elif IMC >= 22.1 and IMC <= 24.9:
    IMCstatus = "Peso normal/ideal :)"
elif IMC >= 25 and IMC <= 29.9:
    IMCstatus = "Sobrepeso"
elif IMC >= 30 and IMC <= 34.9:
    IMCstatus = "Obesidad tipo I"
elif IMC >= 35 and IMC <= 39.9:
    IMCstatus = "Obesidad tipo II"
elif IMC > 40:
    IMCstatus = "Obesidad tipo III"

# imprimir valores finales
print(f"{Nombre} su indice de masa corporal (IMC) es [{round(IMC, 1)}], usted se encuentra en la categoria [{IMCstatus}]")
print(f"Su peso ideal minimo es [{round(pimin, 1)}] y su peso ideal maximo es [{round(pimax, 1)}] por lo cual su peso ideal promedio es [{round(pi, 1)}]")
if pia == 0:
    print(f"A usted le faltan [{round(rec, 1)}kg] para su peso ideal")
elif pia == 1:
    print("Usted se encuentra en su peso correcto!")
elif pia == 2:
    print(f"A usted le sobran [{round(rec, 1)}kg] para su peso ideal")

print(f"Su peso ideal segun la formula de lorentz: [{pilorentz}]")
