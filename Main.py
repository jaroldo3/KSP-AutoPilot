
import krpc
import Launch
import OrbitalAscent
conn = krpc.connect(name='Main')
vessel = conn.space_center.active_vessel
print(vessel.name)
Launch.main(vessel)
OrbitalAscent.main(vessel, conn)
