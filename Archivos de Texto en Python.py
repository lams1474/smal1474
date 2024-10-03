# Escritura de Archivo de Texto:
# Abre (o crea si no existe) el archivo "my_notes.txt" en modo escritura ('w').
with open('my_notes.txt', 'w') as file:
    # Escribimos tres líneas de notas personales.
    file.write("Hoy aprendí sobre la manipulación de archivos en Python.\n")
    file.write("Es un tema útil para gestionar datos de manera eficiente.\n")
    file.write("Practicaré más para consolidar el conocimiento.\n")

# Lectura de Archivo de Texto utilizando readline():
# Abre el archivo "my_notes.txt" en modo lectura ('r').
with open('my_notes.txt', 'r') as file:
    # Lee la primera línea del archivo
    line = file.readline()
    while line:
        # Muestra la línea leída
        print(line, end='')  # 'end' evita que se añadan líneas en blanco adicionales.
        # Lee la siguiente línea
        line = file.readline()

# No es necesario cerrar explícitamente los archivos cuando se usa 'with', ya que Python lo hace automáticamente.
