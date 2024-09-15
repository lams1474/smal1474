def calcular_promedio_temperaturas(temperaturas, ciudades):
    """
    Calcula y retorna el promedio de las temperaturas para cada ciudad y semana.

    :param temperaturas: Lista 3D con los datos de las temperaturas (Ciudades -> Semanas -> Días)
    :param ciudades: Lista con los nombres de las ciudades
    :return: Diccionario con los promedios de temperatura por ciudad y semana
    """
    promedios = {}

    # Iterar sobre cada ciudad
    for ciudad_idx, ciudad in enumerate(temperaturas):
        promedios[ciudades[ciudad_idx]] = []

        # Iterar sobre cada semana de esa ciudad
        for semana_idx, semana in enumerate(ciudad):
            # Sumar las temperaturas de todos los días de la semana
            suma_temperaturas = sum([dia["temp"] for dia in semana])

            # Calcular el promedio dividiendo entre el número de días de la semana
            promedio = suma_temperaturas / len(semana)

            # Guardar el promedio en el diccionario
            promedios[ciudades[ciudad_idx]].append(promedio)

    return promedios


# Datos de ejemplo
temperaturas = [
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

ciudades = ["Pujili", "Latacunga", "La Mana"]

# Llamar a la función y mostrar los resultados
promedios = calcular_promedio_temperaturas(temperaturas, ciudades)
for ciudad, promedios_semanas in promedios.items():
    for semana, promedio in enumerate(promedios_semanas):
        print(f"Promedio de temperaturas en {ciudad}, Semana {semana + 1}: {promedio:.2f} grados")
