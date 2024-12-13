

tipo_cambio_eur_ars = 1069.90
tipo_cambio_usd_ars = 1018.23

tipo_conversion = input("ingrese la moneda de origen para la conversión (EUR/USD): ").upper()
monto_a_convertir = float(input("Ingrese el monto a convertir: "))

# 4. Hacer el cambio de moneda.

if tipo_conversion == "EUR":
    resultado = tipo_cambio_eur_ars * monto_a_convertir
    print("El resultado de la conversión de Euro a Peso Argentinos es: ", resultado)
elif tipo_conversion == "USD":
    resultado = tipo_cambio_usd_ars * monto_a_convertir
    print("El resultado de la conversión de Dolar a Peso Argentino es: ", resultado)
else:
    print("Tipo de conversión no válido")