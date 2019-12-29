# Diseño e implementación de sistema de recepción directa de imágenes del satelite METEOR M-2

Proyecto final de grado para la carrera de Ingenieria Electronica. Desarrollado en conjunto con el Centro de Sensores Remotos dependiente de la Escuela de Agrimensura de la Facultad de Ciencias Exactas, Ingeniería y Agrimensura de la Universidad Nacional de Rosario.

En este repositorio se incluye el código fuente desarrollado en GNURadio para el demodulador QPSK utilizado para demodular la señal del satélite METEOR-M2. También se incluye el código de un script en Python que automatiza la ejecución del flowgraph demodulador cuando el satélite se encuentra por encima del horizonte, éste script utiliza la librería [Skyfield](https://github.com/skyfielders/python-skyfield) para calcular la posición actual del satélite según el archivo TLE.

Para poder ejecutar el flowgraph es necesario tener instalado GNURadio a través de PyBOMBS. El producto final es un archivo .s que contiene los "soft-symbols" decodificado, este archivo está listo para ser decodificado a imagen, funciona con LRPTOfflineDecoder o [met_decoder](https://github.com/artlav/meteor_decoder)

**TODO:** 
- Incluir instrucciones de instalación y de uso.
- Crear otro flowgraph demodulador QPSK que funcione con el Meteor M2-2.
- Agregar el seguimiento de éste satélite en el script automatizador.

### Autores:
- Grippo, Lucas ([@lucasgrippo](https://github.com/lucasgrippo))
- Moya, Ignacio ([@mignacio](https://github.com/mignacio))
### Director:
- Ing. Arraigada, Fernando.
