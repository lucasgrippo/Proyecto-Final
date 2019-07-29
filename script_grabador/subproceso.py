import sys
import subprocess

grc_script = 'top_block.py'
sdr_capture = [sys.executable, grc_script, '-i', 'Raydel.wav', '-o', 'output']


def ejecutar_script_grc(sdr_capture):
    subp = subprocess.Popen(sdr_capture, stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE)
    return subp


def terminar_script_grc(subp):
    subp.send_signal(subprocess.signal.SIGINT)
