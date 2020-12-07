import math
import time
import krpc

def main(vessel, conn):
    turnStart = 2500
    turnEnd = 15000
    turnAngle = 0
    apoapsisTarget = 250000
    srbResources = vessel.resources_in_decouple_stage(stage=2, cumulative=False)

    ut = conn.add_stream(getattr, conn.space_center, 'ut')
    altitude = conn.add_stream(getattr, vessel.flight(), 'mean_altitude')
    srbFuel = conn.add_stream(srbResources.amount, 'SolidFuel')

    print('Starting Orbital Ascent')

    while True:
        if srbFuel() < .01:
            print('stage')
        if altitude() > turnStart and altitude() < turnEnd:
            frac = ((altitude() - turnStart) /
                    (turnEnd - turnStart))
            newTurnAngle = frac * 90
            if newTurnAngle - turnAngle > 0.5:
                turnAngle = newTurnAngle
                vessel.auto_pilot.target_pitch_and_heading(90-turnAngle, 90)
