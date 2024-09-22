# Definiendo la función calcular_descuento
def calcular_descuento(monto_total, porcentaje_descuento=10):
    descuento = (porcentaje_descuento / 100) * monto_total
    return descuento

# Llamadas a la función
# Primera llamada: solo monto total (utiliza descuento por defecto del 10%)
monto_total_1 = 150
descuento_1 = calcular_descuento(monto_total_1)

# Segunda llamada: monto total y porcentaje de descuento proporcionado
monto_total_2 = 200
porcentaje_descuento_2 = 15
descuento_2 = calcular_descuento(monto_total_2, porcentaje_descuento_2)

# Cálculo del monto final a pagar después del descuento
monto_final_1 = monto_total_1 - descuento_1
monto_final_2 = monto_total_2 - descuento_2

# Mostrando los resultados
print(f"Compra 1: Monto total = {monto_total_1}, Descuento = {descuento_1}, Monto final = {monto_final_1}")
print(f"Compra 2: Monto total = {monto_total_2}, Descuento = {descuento_2}, Monto final = {monto_final_2}")
