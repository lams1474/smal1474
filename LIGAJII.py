import random
import itertools

class Campeonato:
    def __init__(self, clubes):
        self.clubes = clubes
        self.fixture = self.generar_fixture()
        self.tabla_posiciones = {club: {"PJ": 0, "PG": 0, "PE": 0, "PP": 0, "GF": 0, "GC": 0, "Puntos": 0} for club in clubes}
        self.tarjetas = {club: {"Amarillas": 0, "Rojas": 0} for club in clubes}
        self.planillas = {}

    def generar_fixture(self):
        """Generar fixture de partidos para todos los clubes en una liga de ida y vuelta."""
        partidos = list(itertools.combinations(self.clubes, 2))
        random.shuffle(partidos)  # Para darle aleatoriedad al fixture
        return partidos

    def registrar_partido(self, local, visitante, goles_local, goles_visitante):
        """Registra los resultados de un partido y actualiza la tabla de posiciones."""
        if local not in self.tabla_posiciones or visitante not in self.tabla_posiciones:
            print("Club no encontrado en el campeonato.")
            return

        # Actualización de tabla de posiciones
        self.tabla_posiciones[local]["PJ"] += 1
        self.tabla_posiciones[visitante]["PJ"] += 1
        self.tabla_posiciones[local]["GF"] += goles_local
        self.tabla_posiciones[local]["GC"] += goles_visitante
        self.tabla_posiciones[visitante]["GF"] += goles_visitante
        self.tabla_posiciones[visitante]["GC"] += goles_local

        if goles_local > goles_visitante:
            self.tabla_posiciones[local]["PG"] += 1
            self.tabla_posiciones[local]["Puntos"] += 3
            self.tabla_posiciones[visitante]["PP"] += 1
        elif goles_local < goles_visitante:
            self.tabla_posiciones[visitante]["PG"] += 1
            self.tabla_posiciones[visitante]["Puntos"] += 3
            self.tabla_posiciones[local]["PP"] += 1
        else:
            self.tabla_posiciones[local]["PE"] += 1
            self.tabla_posiciones[visitante]["PE"] += 1
            self.tabla_posiciones[local]["Puntos"] += 1
            self.tabla_posiciones[visitante]["Puntos"] += 1

    def registrar_tarjeta(self, club, tipo, cantidad=1):
        """Registra tarjetas amarillas o rojas para un club."""
        if club in self.tarjetas:
            if tipo == "Amarilla":
                self.tarjetas[club]["Amarillas"] += cantidad
            elif tipo == "Roja":
                self.tarjetas[club]["Rojas"] += cantidad
        else:
            print("Club no encontrado.")

    def registrar_planilla_jugadores(self, club, jugadores):
        """Registra los jugadores que participan en un partido."""
        self.planillas[club] = jugadores

    def mostrar_fixture(self):
        """Muestra el fixture de los partidos."""
        print("\nFixture del Campeonato:")
        for i, partido in enumerate(self.fixture, 1):
            print(f"Partido {i}: {partido[0]} vs {partido[1]}")

    def mostrar_tabla_posiciones(self):
        """Muestra la tabla de posiciones actualizada."""
        print("\nTabla de Posiciones:")
        print(f"{'Club':<15}{'PJ':<5}{'PG':<5}{'PE':<5}{'PP':<5}{'GF':<5}{'GC':<5}{'Puntos':<7}")
        for club, datos in sorted(self.tabla_posiciones.items(), key=lambda x: x[1]["Puntos"], reverse=True):
            print(f"{club:<15}{datos['PJ']:<5}{datos['PG']:<5}{datos['PE']:<5}{datos['PP']:<5}{datos['GF']:<5}{datos['GC']:<5}{datos['Puntos']:<7}")

    def mostrar_tarjetas(self):
        """Muestra el conteo de tarjetas amarillas y rojas de cada club."""
        print("\nTarjetas por Club:")
        print(f"{'Club':<15}{'Amarillas':<10}{'Rojas':<7}")
        for club, tarjetas in self.tarjetas.items():
            print(f"{club:<15}{tarjetas['Amarillas']:<10}{tarjetas['Rojas']:<7}")

    def mostrar_planillas(self):
        """Muestra la planilla de jugadores registrada por cada club."""
        print("\nPlanilla de Jugadores:")
        for club, jugadores in self.planillas.items():
            print(f"\n{club}:")
            for jugador in jugadores:
                print(f" - {jugador}")

# Inicialización de datos
clubes = [
    "Club A", "Club B", "Club C", "Club D", "Club E", "Club F",
    "Club G", "Club H", "Club I", "Club J", "Club K", "Club L"
]

# Crear campeonato
campeonato = Campeonato(clubes)

# Mostrar el fixture
campeonato.mostrar_fixture()

# Registrar algunos partidos
campeonato.registrar_partido("Club A", "Club B", 2, 1)
campeonato.registrar_partido("Club C", "Club D", 0, 0)
campeonato.registrar_partido("Club E", "Club F", 3, 2)

# Registrar tarjetas
campeonato.registrar_tarjeta("Club A", "Amarilla", 2)
campeonato.registrar_tarjeta("Club B", "Roja", 1)

# Registrar planilla de jugadores
campeonato.registrar_planilla_jugadores("Club A", ["Jugador 1", "Jugador 2", "Jugador 3"])
campeonato.registrar_planilla_jugadores("Club B", ["Jugador 4", "Jugador 5", "Jugador 6"])

# Mostrar tabla de posiciones
campeonato.mostrar_tabla_posiciones()

# Mostrar tarj