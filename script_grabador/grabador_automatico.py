#!/usr/bin/env python2
from time import sleep
import satelites
import subproceso

# inicializo array de satelites
sats = satelites.init_satelites_clima()

meteorm_2 = sats['METEOR-M 2']
# Imprimo info del satelite y Epoch.
# El epoch es importante para saber cuando el archivo TLE deja de saber
# valido.
print(meteorm_2)
print(meteorm_2.epoch.utc_jpl())

# Cargo timescale para saber si es necesario actualizar el TLE.
ts = satelites.get_time_scale()

script_esta_corriendo = False

while True:
    t = ts.now()

    # chequeo que el epoch no sea viejo, el TLE pierde precision con el pasar
    # del tiempo
    meteorm_2 = satelites.epoch_es_viejo(meteorm_2, t)

    if satelites.esta_sobre_horizonte(meteorm_2, t) is True:
        print('Meteor m2 esta sobre el horizonte')
        if script_esta_corriendo is False:
            subp = subproceso.ejecutar_script_grc()
            script_esta_corriendo = True
    else:
        print('Meteor m2 no esta sobre el horizonte')
        if script_esta_corriendo is True:
            subproceso.terminar_script_grc(subp)
            script_esta_corriendo = False

    sleep(30)
