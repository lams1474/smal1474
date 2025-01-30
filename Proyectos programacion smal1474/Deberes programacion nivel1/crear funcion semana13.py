def promedio_temperaturas(temperaturas, ciudades, ciudad_especifica=None):
    """
    Calcula el promedio de las temperaturas de múltiples ciudades durante varias semanas.

    Args:
    temperaturas (list): Una lista 3D de temperaturas donde:
                         1ra dimensión: Ciudades
                         2da dimensión: Semanas
                         3ra dimensión: Días de la semana con su temperatura.
    ciudades (list): Lista de nombres de las ciudades correspondientes a las temperaturas.
    ciudad_especifica (str, optional): Nombre de una ciudad específica para calcular el promedio de sus semanas.
                                       Si no se especifica, se calculará para todas las ciudades.

    Returns:
    dict: Diccionario con los promedios de cada ciudad por semana.
    """
    promedios = {}

    for ciudad_idx, ciudad in enumerate(temperaturas):
        nombre_ciudad = ciudades[ciudad_idx]

        if ciudad_especifica and nombre_ciudad != ciudad_especifica:
            continue  # Si se especifica una ciudad, omitimos las otras

        promedios[nombre_ciudad] = []

        for semana_idx, semana in enumerate(ciudad):
            suma_temperaturas = sum([dia["temp"] for dia in semana])
            promedio = suma_temperaturas / len(semana)
            promedios[nombre_ciudad].append({
                "Semana": semana_idx + 1,
                "Promedio": round(promedio, 2)
            })

    return promedios


# Ejemplo de uso:
temperaturas = [
    # Pujili
    [
        [{"day": "Lunes", "temp": 16}, {"day": "Martes", "temp": 15}, {"day": "Miércoles", "temp": 10},
         {"day": "Jueves", "temp": 16}, {"day": "Viernes", "temp": 9}, {"day": "Sábado", "temp": 15},
         {"day": "Domingo", "temp": 16}],
        [{"day": "Lunes", "temp": 15}, {"day": "Martes", "temp": 14}, {"day": "Miércoles", "temp": 18},
         {"day": "Jueves", "temp": 20}, {"day": "Viernes", "temp": 10}, {"day": "Sábado", "temp": 15},
         {"day": "Domingo", "temp": 9}],
        [{"day": "Lunes", "temp": 17}, {"day": "Martes", "temp": 10}, {"day": "Miércoles", "temp": 12},
         {"day": "Jueves", "temp": 18}, {"day": "Viernes", "temp": 24}, {"day": "Sábado", "temp": 15},
         {"day": "Domingo", "temp": 13}],
        [{"day": "Lunes", "temp": 7}, {"day": "Martes", "temp": 20}, {"day": "Miércoles", "temp": 14},
         {"day": "Jueves", "temp": 13}, {"day": "Viernes", "temp": 12}, {"day": "Sábado", "temp": 17},
         {"day": "Domingo", "temp": 9}]
    ],
    # Latacunga
    [
        [{"day": "Lunes", "temp": 15}, {"day": "Martes", "temp": 17}, {"day": "Miércoles", "temp": 8},
         {"day": "Jueves", "temp": 12}, {"day": "Viernes", "temp": 23}, {"day": "Sábado", "temp": 11},
         {"day": "Domingo", "temp": 7}],
        [{"day": "Lunes", "temp": 13}, {"day": "Martes", "temp": 16}, {"day": "Miércoles", "temp": 17},
         {"day": "Jueves", "temp": 14}, {"day": "Viernes", "temp": 7}, {"day": "Sábado", "temp": 18},
         {"day": "Domingo", "temp": 24}],
        [{"day": "Lunes", "temp": 20}, {"day": "Martes", "temp": 11}, {"day": "Miércoles", "temp": 17},
         {"day": "Jueves", "temp": 15}, {"day": "Viernes", "temp": 12}, {"day": "Sábado", "temp": 7},
         {"day": "Domingo", "temp": 19}],
        [{"day": "Lunes", "temp": 22}, {"day": "Martes", "temp": 17}, {"day": "Miércoles", "temp": 12},
         {"day": "Jueves", "temp": 14}, {"day": "Viernes", "temp": 16}, {"day": "Sábado", "temp": 7},
         {"day": "Domingo", "temp": 15}]
    ],
    # La Mana
    [
        [{"day": "Lunes", "temp": 32}, {"day": "Martes", "temp": 30}, {"day": "Miércoles", "temp": 32},
         {"day": "Jueves", "temp": 24}, {"day": "Viernes", "temp": 30}, {"day": "Sábado", "temp": 22},
         {"day": "Domingo", "temp": 24}],
        [{"day": "Lunes", "temp": 30}, {"day": "Martes", "temp": 32}, {"day": "Miércoles", "temp": 24},
         {"day": "Jueves", "temp": 22}, {"day": "Viernes", "temp": 30}, {"day": "Sábado", "temp": 32},
         {"day": "Domingo", "temp": 20}],
        [{"day": "Lunes", "temp": 22}, {"day": "Martes", "temp": 24}, {"day": "Miércoles", "temp": 30},
         {"day": "Jueves", "temp": 24}, {"day": "Viernes", "temp": 32}, {"day": "Sábado", "temp": 22},
         {"day": "Domingo", "temp": 32}],
        [{"day": "Lunes", "temp": 22}, {"day": "Martes", "temp": 30}, {"day": "Miércoles", "temp": 24},
         {"day": "Jueves", "temp": 22}, {"day": "Viernes", "temp": 34}, {"day": "Sábado", "temp": 20},
         {"day": "Domingo", "temp": 22}]
    ]
]

ciudades = ["Pujili", "Latacunga", "La Mana"]

# Calcular el promedio para todas las ciudades
promedios_todas = promedio_temperaturas(temperaturas, ciudades)
print(promedios_todas)

# Calcular el promedio solo para la ciudad de Pujili
promedios_pujili = promedio_temperaturas(temperaturas, ciudades, ciudad_especifica="Pujili")
print(promedios_pujili)
