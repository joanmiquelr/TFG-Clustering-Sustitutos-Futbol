# ANÁLISIS DE CLUSTERING PARA LA IDENTIFICACIÓN DE SUSTITUTOS EN FÚTBOL PROFESIONAL: EL CASO DE ANTONIO RAÍLLO

Trabajo de Fin de Grado del Grado en Matemáticas — Universitat de les Illes Balears (UIB)

Aplicación de técnicas de clustering y análisis multivariante para la identificación de perfiles similares en fútbol profesional a partir de datos estadísticos de rendimiento.

---

## Descripción del proyecto

El presente proyecto tiene como objetivo aplicar técnicas de análisis de datos y aprendizaje no supervisado para identificar posibles sustitutos de un jugador de fútbol profesional a partir de estadísticas de rendimiento.

El caso de estudio utilizado es Antonio Raíllo, defensa central del RCD Mallorca. A partir de datos obtenidos mediante procesos de web scraping y recopilación estadística, se analizan jugadores pertenecientes a las principales ligas europeas con el fin de detectar perfiles similares bajo distintos enfoques metodológicos.

Para ello, se emplean técnicas de clustering, análisis exploratorio de datos y reducción de dimensionalidad, permitiendo comparar jugadores a partir de múltiples variables de rendimiento.

---

## Objetivos

- Realizar un análisis descriptivo de datos de rendimiento futbolístico.
- Aplicar técnicas de clustering jerárquico y K-Means.
- Utilizar Análisis de Componentes Principales (PCA) para la reducción de dimensionalidad.
- Identificar perfiles estadísticamente similares al jugador de referencia.

---

## Metodología

Las principales técnicas utilizadas en el desarrollo del proyecto son:

- Clustering jerárquico
- K-Means
- Análisis de Componentes Principales (PCA)

---

## Tecnologías utilizadas

### Lenguajes

- R
- Python

### Principales librerías utilizadas

#### R

- tidyverse
- ggplot2
- factoextra
- cluster
- fpc
- mclust
- dbscan
- corrplot
- GGally
- sf
- UpSetR

#### Python

- pandas
- requests
- BeautifulSoup
- rvest
- httr

---

## Fuentes de datos

Los datos utilizados en este proyecto proceden de diferentes plataformas de estadísticas futbolísticas:

- FBref
- LanusStats (GitHub)
- BeSoccer
- Transfermarkt

Todos los datos han sido utilizados exclusivamente con fines académicos y de investigación.

---

## Estructura del repositorio

```text
TFG-Clustering-Sustitutos-Futbol/
│
├── Memoria/
│   └── TFG.pdf
│
├── R_Script/
│   ├── TFG_Clustering.R
│   └── Simulacion_FM.R
│
├── Codigo_Python/
│   └── WebScraping.py
│   └── LanusStats.py
│
├── Data/
│   ├── Datos_Originales/
│   ├── Datos_Procesados/
│   └── Simulaciones_Football_Manager/
│
└── README.md
```

---

## Reproducibilidad

El repositorio incluye tanto los datos procesados como los scripts utilizados durante el análisis, permitiendo replicar las diferentes fases del proyecto.

Para ejecutar correctamente el código es necesario disponer de:

- R y RStudio
- Python
- Las librerías especificadas anteriormente

---

## Resultados

El análisis realizado permite identificar jugadores con perfiles estadísticamente similares al jugador de referencia mediante distintas técnicas de agrupamiento y reducción de dimensionalidad.

La comparación entre metodologías permite evaluar la estabilidad de los resultados y detectar perfiles recurrentes entre diferentes configuraciones del análisis.

---

## Autor

Joan Miquel Rubí Garcías  
Grado en Matemáticas  
Universitat de les Illes Balears (UIB)

---

## Disclaimer sobre el uso de inteligencia artificial

Durante la realización de este trabajo se han utilizado herramientas de inteligencia artificial como apoyo en tareas secundarias relacionadas con:

- Revisión y mejora de redacción académica
- Asistencia en programación
- Apoyo en procesos de web scraping
- Generación y adaptación de gráficos

El diseño metodológico, el análisis estadístico, la interpretación de resultados y las conclusiones han sido desarrollados íntegramente por el autor.
