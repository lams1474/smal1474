# Crear una matriz 3D que represente los datos de temperaturas
# Primera dimensión: Ciudades (3 Ciudades)
# Segunda dimensión: Días de la semana (7 días)
# Tercera dimensión: Semanas (4 semanas)
temperaturas = [
    [   # Pujili
        [   # Semana 1
            {"day": "Lunes", "temp": 16},
            {"day": "Martes", "temp": 15},
            {"day": "Miércoles", "temp": 10},
            {"day": "Jueves", "temp": 16},
            {"day": "Viernes", "temp": 9},
            {"day": "Sábado", "temp": 15},
            {"day": "Domingo", "temp": 16}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 15},
            {"day": "Martes", "temp": 14},
            {"day": "Miércoles", "temp": 18},
            {"day": "Jueves", "temp": 20},
            {"day": "Viernes", "temp": 10},
            {"day": "Sábado", "temp": 15},
            {"day": "Domingo", "temp": 9}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 17},
            {"day": "Martes", "temp": 10},
            {"day": "Miércoles", "temp": 12},
            {"day": "Jueves", "temp": 18},
            {"day": "Viernes", "temp": 24},
            {"day": "Sábado", "temp": 15},
            {"day": "Domingo", "temp": 13}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 7},
            {"day": "Martes", "temp": 20},
            {"day": "Miércoles", "temp": 14},
            {"day": "Jueves", "temp": 13},
            {"day": "Viernes", "temp": 12},
            {"day": "Sábado", "temp": 17},
            {"day": "Domingo", "temp": 9}
        ]
    ],
    [   # Latacunga
        [   # Semana 1
            {"day": "Lunes", "temp": 15},
            {"day": "Martes", "temp": 17},
            {"day": "Miércoles", "temp": 8},
            {"day": "Jueves", "temp": 12},
            {"day": "Viernes", "temp": 23},
            {"day": "Sábado", "temp": 11},
            {"day": "Domingo", "temp": 7}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 13},
            {"day": "Martes", "temp": 16},
            {"day": "Miércoles", "temp": 17},
            {"day": "Jueves", "temp": 14},
            {"day": "Viernes", "temp": 7},
            {"day": "Sábado", "temp": 18},
            {"day": "Domingo", "temp": 24}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 20},
            {"day": "Martes", "temp": 11},
            {"day": "Miércoles", "temp": 17},
            {"day": "Jueves", "temp": 15},
            {"day": "Viernes", "temp": 12},
            {"day": "Sábado", "temp": 7},
            {"day": "Domingo", "temp": 19}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 22},
            {"day": "Martes", "temp": 17},
            {"day": "Miércoles", "temp": 12},
            {"day": "Jueves", "temp": 14},
            {"day": "Viernes", "temp": 16},
            {"day": "Sábado", "temp": 7},
            {"day": "Domingo", "temp": 15}
        ]
    ],
    [   # La Mana
        [   # Semana 1
            {"day": "Lunes", "temp": 32},
            {"day": "Martes", "temp": 30},
            {"day": "Miércoles", "temp": 32},
            {"day": "Jueves", "temp": 24},
            {"day": "Viernes", "temp": 30},
            {"day": "Sábado", "temp": 22},
            {"day": "Domingo", "temp": 24}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 30},
            {"day": "Martes", "temp": 32},
            {"day": "Miércoles", "temp": 24},
            {"day": "Jueves", "temp": 22},
            {"day": "Viernes", "temp": 30},
            {"day": "Sábado", "temp": 32},
            {"day": "Domingo", "temp": 20}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 22},
            {"day": "Martes", "temp": 24},
            {"day": "Miércoles", "temp": 30},
            {"day": "Jueves", "temp": 24},
            {"day": "Viernes", "temp": 32},
            {"day": "Sábado", "temp": 22},
            {"day": "Domingo", "temp": 32}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 22},
            {"day": "Martes", "temp": 30},
            {"day": "Miércoles", "temp": 24},
            {"day": "Jueves", "temp": 22},
            {"day": "Viernes", "temp": 34},
            {"day": "Sábado", "temp": 20},
            {"day": "Domingo", "temp": 22}
        ]
    ]
]

# Calcular el promedio de temperaturas para cada ciudad y semana
ciudades = ["Pujili", "Latacunga", "La Mana"]
for ciudad_idx, ciudad in enumerate(temperaturas):
    for semana_idx, semana in enumerate(ciudad):
        suma_temperaturas = sum([dia["temp"] for dia in semana])
        promedio = suma_temperaturas / len(semana)
        print(f"Promedio de temperaturas en {ciudades[ciudad_idx]}, Semana {semana_idx + 1}: {promedio:.2f} grados")
