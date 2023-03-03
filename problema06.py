#Enunciado: un restaurante ofrece un descuento del 10% para consumo de hasta s/. 100.00 
# #y un descuento del 20 % para consumos mayores, para ambos casos se aplica un 
# #impuesto del 19%. Determinar el monto del descuento, el impuesto y el importe a pagar.

impuesto = 1.19
descuento = 1.10
descuento2 = 1.20
monto_des = 0.0
monto_imp = 0.0
monto_pag = 0.0
consumo = 0.0

#lectura de datos 

consumo = float(input(">>> Ingrese el monto del consumo: "))

#calculos
if (consumo < 100):
    monto_des = (consumo * descuento) - consumo
    monto_imp = (consumo * impuesto) - consumo
    monto_pag = consumo - monto_imp + monto_des
else: 
    monto_des = (consumo * descuento2) - consumo
    monto_imp = (consumo * impuesto) - consumo
    monto_pag = consumo - monto_imp + monto_des

print("El monto del descuento es: %0.2f"%(monto_des))
print("El monto del impuesto es: %0.2f"%(monto_imp))
print("El monto a cancelar es: %0.2f"%(monto_pag))
    
