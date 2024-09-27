# Diccionario llamado 'informacion_personal' con datos ficticios
informacion_personal = {
    "nombre": "Luis Maigua",
    "edad": 50,
    "ciudad": "Pujili",
    "profesion": "Estudiante"
}
informacion_personal["ciudad"] = "Guayaquil"
informacion_personal["profesion"] = "Desarrollador de Software"
if "telefono" not in informacion_personal:
       informacion_personal["telefono"] = "0998765432"
if "edad" in informacion_personal:
    del informacion_personal["edad"]
print(informacion_personal)