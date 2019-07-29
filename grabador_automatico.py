#!/usr/bin/env python2
from skyfield.api import Topos, load
from time import sleep
import sys
import os
import subprocess
from os import listdir
from os.path import isfile, join, getmtime, basename

ubicacion_estacion_terrena = Topos('-32.949025 S', '-60.671039 W')

grc_script = 'top_block.py'
# grc_script = os.path.join[sys.executable, grc_script]
sdr_capture = [sys.executable, grc_script, '-i', 'Raydel.wav', '-o', 'output']

subp = subprocess.Popen(sdr_capture, stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE)
sleep(10)
subp.send_signal(subprocess.signal.SIGINT)


def calcular_si_epoch_es_viejo(satellite, t):

    days = t - satellite.epoch
    print('{:.3f} days away from epoch'.format(days))
    # si la diferencia entre hoy y el epoch es mayor a 14 dias,
    # hay que recargar el TLE
    if abs(days) > 7:
        satellites = load.tle(stations_url, reload=True)
        satellite = satellites[satellite.model.satnum]
    return satellite


def calcular_si_esta_sobre_horizonte(satellite, t):
    geocentric = satellite.at(t)

    subpoint = geocentric.subpoint()
    # print('Latitude:', subpoint.latitude)
    # print('Longitude:', subpoint.longitude)
    # print('Elevation (m):', int(subpoint.elevation.m))

    difference = meteorm_2 - ubicacion_estacion_terrena
    topocentric = difference.at(t)

    alt, az, distance = topocentric.altaz()
    print('Altitude: ' + alt.dstr())
    print('Azimuth: ' + az.dstr())

    if alt.degrees > 0:
        return True
    else:
        return False


# Descargo archivo TLE del satelite
stations_url = 'http://celestrak.com/NORAD/elements/weather.txt'
satellites = load.tle(stations_url)
# satellite = satellites['METEOR-M2 2']
meteorm_2 = satellites['METEOR-M 2']

# Imprimo info del satelite y Epoch.
# El epoch es importante para saber cuando el archivo TLE deja de saber
# valido.
print(meteorm_2)
print(meteorm_2.epoch.utc_jpl())

# Cargo timescale para saber si es necesario actualizar el TLE.
ts = load.timescale()

# a partir de aca, deberia hacerce un bucle para rechequear la posicion
# de los satelites
# while True:
t = ts.now()

meteorm_2 = calcular_si_epoch_es_viejo(meteorm_2, t)

if calcular_si_esta_sobre_horizonte(meteorm_2, t) is True:
    print('Meteor m2 esta sobre el horizonte')

else:
    print('Meteor m2 no esta sobre el horizonte')

     # sleep(10)
