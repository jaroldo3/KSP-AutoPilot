import math
import time
import krpc

def main(vessel, conn):
    planet = conn.space_center.bodies['Kerbin']
    turnStart = 2500
    turnEnd = 15000
    turnAngle = 0
    apoapsisTarget = 250000
    srbResources = vessel.resources_in_decouple_stage(stage=2, cumulative=False)
    srbsSeperated = False

    ut = conn.add_stream(getattr, conn.space_center, 'ut')
    altitude = conn.add_stream(getattr, vessel.flight(), 'mean_altitude')
    thrust = vessel.thrust
    mass = vessel.mass
    gravity = planet.surface_gravity
    twr = conn.add_stream(calculateTwr(thrust, mass, gravity), '')

    print('Starting Orbital Ascent')
    print(twr)
    while True:
        if altitude() > turnStart and altitude() < turnEnd:
            vessel.control.throttle = calculateTwr(vessel)
            frac = ((altitude() - turnStart) /
                    (turnEnd - turnStart))
            newTurnAngle = frac * 90
            if newTurnAngle - turnAngle > 0.5:
                turnAngle = newTurnAngle
                vessel.auto_pilot.target_pitch_and_heading(90-turnAngle, 90)
                time.sleep(1)
                print(twr)

def calculateTwr(thrust, mass, gravity):
    return thrust/(mass * gravity)
