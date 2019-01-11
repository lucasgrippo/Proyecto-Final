# Instalación de GNU Radio en ubuntu desde 0

> agregar "sudo" al principio de todo

### actualizar administrador de paquetes
    apt update
    apt upgrade


### administrador de paquetes para python
    apt install python-pip
> es necesario para poder instalar pybombs y gnuradio 

### instalar python 2.7
    apt install python2.7

## GNU Radio y PyBOMBS
### instalar pybombs (administrador de paquetes de gnuradio)
    pip install pybombs

### instalar recetas de pybombs
    pybombs recipes add gr-recipes git+https://github.com/gnuradio/gr-recipes.git

### creamos directorio prefix para almacenar allí la instalación
#### sube un directorio, tendría que ser /home
    cd ..
#### y creo el directorio /prefix    
    mkdir prefix/

### luego en el sub-directorio /default instalamos gnuradio con gr-osmosdr
    pybombs prefix init -a default prefix/default/ -R gnuradio-default
    
> este comando tarda muchísimo tiempo, varias horas, así que paciencia

### ejecutar gnuradio-companion

    cd prefix/default/
    source ./setup_env-sh
    
    gnuradio-companion
