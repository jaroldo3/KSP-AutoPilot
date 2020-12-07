import math
import time
import krpc
import OrbitalAscent

def main(vessel):
    countdown(vessel)
    vessel.auto_pilot.engage()

def countdown(vessel):
    # Pre-launch setup
    vessel.control.sas = False
    vessel.control.rcs = False
    vessel.control.throttle = 1.0
    # Countdown...
    print('T-3...')
    time.sleep(1)
    print('T-2...')
    time.sleep(1)
    print('T-1...')
    time.sleep(1)
    vessel.control.activate_next_stage()
    print('Launch!')
