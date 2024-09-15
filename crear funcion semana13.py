def calcular_promedio_temperaturas(datos_ciudades, nombres_ciudades):
    """
    Calcula y retorna el promedio de las temperaturas para cada ciudad y semana.

    :param datos_ciudades: Lista 3D con los datos de las temperaturas (Ciudades -> Semanas -> Días)
    :param nombres_ciudades: Lista con los nombres de las ciudades
    :return: Diccionario con los promedios de temperatura por ciudad y semana
    """
    promedios_ciudades = {}  # Almacenar los resultados de promedios por ciudad

    # Iterar sobre cada ciudad
    for indice_ciudad, ciudad_datos in enumerate(datos_ciudades):
        promedios_ciudades[nombres_ciudades[indice_ciudad]] = []

        # Iterar sobre cada semana de esa ciudad
        for indice_semana, semana_datos in enumerate(ciudad_datos):
            # Sumar las temperaturas de todos los días de la semana
            suma_temperaturas_semana = sum([dia["temp"] for dia in semana_datos])

            # Calcular el promedio dividiendo entre el número de días de la semana
            promedio_temperatura = suma_temperaturas_semana / len(semana_datos)

            # Guardar el promedio en el diccionario
            promedios_ciudades[nombres_ciudades[indice_ciudad]].append(promedio_temperatura)

    return promedios_ciudades


# Datos de ejemplo
datos_temperaturas = [
    [
        # Pujili
        [{"day": "Lunes", "temp": 16}, {"day": "Martes", "temp": 15}, {"day": "Miércoles", "temp": 10},
         {"day": "Jueves", "temp": 16},
         {"day": "Viernes", "temp": 9}, {"day": "Sábado", "temp": 15}, {"day": "Domingo", "temp": 16}],
        [{"day": "Lunes", "temp": 15}, {"day": "Martes", "temp": 14}, {"day": "Miércoles", "temp": 18},
         {"day": "Jueves", "temp": 20},
         {"day": "Viernes", "temp": 10}, {"day": "Sábado", "temp": 15}, {"day": "Domingo", "temp": 9}],
        [{"day": "Lunes", "temp": 17}, {"day": "Martes", "temp": 10}, {"day": "Miércoles", "temp": 12},
         {"day": "Jueves", "temp": 18},
         {"day": "Viernes", "temp": 24}, {"day": "Sábado", "temp": 15}, {"day": "Domingo", "temp": 13}],
        [{"day": "Lunes", "temp": 7}, {"day": "Martes", "temp": 20}, {"day": "Miércoles", "temp": 14},
         {"day": "Jueves", "temp": 13},
         {"day": "Viernes", "temp": 12}, {"day": "Sábado", "temp": 17}, {"day": "Domingo", "temp": 9}]
    ],
    [
        # Latacunga
        [{"day": "Lunes", "temp": 15}, {"day": "Martes", "temp": 17}, {"day": "Miércoles", "temp": 8},
         {"day": "Jueves", "temp": 12},
         {"day": "Viernes", "temp": 23}, {"day": "Sábado", "temp": 11}, {"day": "Domingo", "temp": 7}],
        [{"day": "Lunes", "temp": 13}, {"day": "Martes", "temp": 16}, {"day": "Miércoles", "temp": 17},
         {"day": "Jueves", "temp": 14},
         {"day": "Viernes", "temp": 7}, {"day": "Sábado", "temp": 18}, {"day": "Domingo", "temp": 24}],
        [{"day": "Lunes", "temp": 20}, {"day": "Martes", "temp": 11}, {"day": "Miércoles", "temp": 17},
         {"day": "Jueves", "temp": 15},
         {"day": "Viernes", "temp": 12}, {"day": "Sábado", "temp": 7}, {"day": "Domingo", "temp": 19}],
        [{"day": "Lunes", "temp": 22}, {"day": "Martes", "temp": 17}, {"day": "Miércoles", "temp": 12},
         {"day": "Jueves", "temp": 14},
         {"day": "Viernes", "temp": 16}, {"day": "Sábado", "temp": 7}, {"day": "Domingo", "temp": 15}]
    ],
    [
        # La Mana
        [{"day": "Lunes", "temp": 32}, {"day": "Martes", "temp": 30}, {"day": "Miércoles", "temp": 32},
         {"day": "Jueves", "temp": 24},
         {"day": "Viernes", "temp": 30}, {"day": "Sábado", "temp": 22}, {"day": "Domingo", "temp": 24}],
        [{"day": "Lunes", "temp": 30}, {"day": "Martes", "temp": 32}, {"day": "Miércoles", "temp": 24},
         {"day": "Jueves", "temp": 22},
         {"day": "Viernes", "temp": 30}, {"day": "Sábado", "temp": 32}, {"day": "Domingo", "temp": 20}],
        [{"day": "Lunes", "temp": 22}, {"day": "Martes", "temp": 24}, {"day": "Miércoles", "temp": 30},
         {"day": "Jueves", "temp": 24},
         {"day": "Viernes", "temp": 32}, {"day": "Sábado", "temp": 22}, {"day": "Domingo", "temp": 32}],
        [{"day": "Lunes", "temp": 22}, {"day": "Martes", "temp": 30}, {"day": "Miércoles", "temp": 24},
         {"day": "Jueves", "temp": 22},
         {"day": "Viernes", "temp": 34}, {"day": "Sábado", "temp": 20}, {"day": "Domingo", "temp": 22}]
    ]
]

nombres_ciudades = ["Pujili", "Latacunga", "La Mana"]

# Llamar a la función y mostrar los resultados
resultados_promedios = calcular_promedio_temperaturas(datos_temperaturas, nombres_ciudades)
for ciudad, promedios in resultados_promedios.items():
    for semana, promedio_semana in enumerate(promedios):
        print(f"Promedio de temperaturas en {ciudad}, Semana {semana + 1}: {promedio_semana:.2f} grados")
