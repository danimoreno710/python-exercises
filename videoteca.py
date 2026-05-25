videoteca=[["Spider-Man: No Way Home", 2021, 8.2, "Acción"],
           ["el caballero de la noche", 2008, 9.0, "Acción"],
           ["interesteral", 2010, 7.5, "Ciencia ficción"],
           ["Parasitos", 2019, 8.6, "Terror"],
           ["Maestro", 2023, 6.5, "Biográfico"],
           ["Titanic", 1997, 7.8, "Romance"],
           ["avengers: endgame", 2019, 8.4, "Acción"] 
]

def contar_titulos_populares_recientes(videoteca, calificacion_minima, año_reciente):
    contador = 0
    for titulo, año, calificacion, genero in videoteca:
        if calificacion >= calificacion_minima and año >= año_reciente:
            contador += 1
    return contador

calificacion_minima = 7.5
año_reciente = 2017

resultado = contar_titulos_populares_recientes(videoteca, calificacion_minima, año_reciente)
print(f"El número de títulos populares y recientes es: {resultado}")  

for titulo, año, calificacion, genero in videoteca:
  if calificacion >= calificacion_minima and año >= año_reciente:
     print(f"Título: {titulo} | Año: {año} | Clasificación: {calificacion} | Género: {genero}")