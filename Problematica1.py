import math

def main():
    radio = float(input("Ingrese el radio del criculo: "))
    
    area_del_circulo = math.pi * math.pow(radio, 2)
    
    print(f"El area del circulo es: {area_del_circulo}")
    
main()
