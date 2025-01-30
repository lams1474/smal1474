# Crear un diccionario llamado 'informacion_personal' con datos ficticios
# Las claves representan aspectos de la persona: nombre, edad, ciudad y profesión
informacion_personal = {
    "nombre": "Luis Maigua",  # Nombre de la persona
    "edad": 50,               # Edad de la persona
    "ciudad": "Pujili",        # Ciudad actual de residencia
    "profesion": "Jubilado"     # Profesión de la persona
}
# Acceder al valor asociado con la clave 'ciudad' y modificarlo
# Aquí cambiamos la ciudad de "Pujili" a "Manta"
informacion_personal["ciudad"] = "Manta"

# Modificamos la profesión de la persona en la clave 'profesion'
# Cambiamos de "Policia Nacional" a "Jubilado"
informacion_personal["profesion"] = "Policia Nacional"

# Verificar si la clave 'telefono' existe en el diccionario
# Si no existe, la agregamos con un número de teléfono ficticio
if "telefono" not in informacion_personal:
    # Como 'telefono' no está en el diccionario, lo agregamos
    informacion_personal["telefono"] = "0996813865"

# Eliminar la clave 'edad' del diccionario
# Consideramos que esta información no es necesaria
if "edad" in informacion_personal:
    del informacion_personal["edad"]

# Finalmente, imprimimos el diccionario actualizado
# Este es el resultado después de todas las operaciones
print(informacion_personal)