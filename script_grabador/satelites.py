from skyfield.api import Topos, load
from time import sleep

ubicacion_estacion_terrena = Topos('-32.949025 S', '-60.671039 W')
stations_url = 'http://celestrak.com/NORAD/elements/weather.txt'


def get_time_scale():
    return load.timescale()


def init_satelites_clima():
    satellites = load.tle(stations_url)
    return satellites


def epoch_es_viejo(satellite, t):

    days = t - satellite.epoch
    print('{:.3f} days away from epoch'.format(days))
    # si la diferencia entre hoy y el epoch es mayor a 14 dias,
    # hay que recargar el TLE
    if abs(days) > 7:
        satellites = load.tle(stations_url, reload=True)
        satellite = satellites[satellite.model.satnum]
    return satellite


def esta_sobre_horizonte(satellite, t):
    geocentric = satellite.at(t)

    subpoint = geocentric.subpoint()
    # print('Latitude:', subpoint.latitude)
    # print('Longitude:', subpoint.longitude)
    # print('Elevation (m):', int(subpoint.elevation.m))

    difference = satellite - ubicacion_estacion_terrena
    topocentric = difference.at(t)

    alt, az, distance = topocentric.altaz()
    print('Altitude: ' + alt.dstr())
    print('Azimuth: ' + az.dstr())

    if alt.degrees > 0:
        return True
    else:
        return False
