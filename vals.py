import numpy as np
import sympy as sp
import mpmath as mp

mp.dps = 1000
constants = {
"lightspeed": mp.mpf("299792458"),
"plancklength": mp.mpf("1.61622938e-35"),
"planckmass": mp.mpf("2.176470e-8"),
"plancktime": mp.mpf("5.39116e-44"),
"planckcharge": mp.mpf("1.875545956e-18"),
"plancktemp": mp.mpf("1.416808e+32"),
"gravconst": mp.mpf("6.67408e-11"),
"planckconst": mp.mpf("6.626070040e-34"),
"redplanckconst": mp.mpf("6.626070040e-34")/mp.pi,
"vacpermea": 4*mp.pi*mp.mpf("1e-7"),
"vacpermit": 1/(4*mp.pi*mp.mpf("1e-7")*299792458**2),
"charimpedance": 4*mp.pi*mp.mpf("1e-7")*299792458,
"coulconst": 1/(4*mp.pi*(1/(4*mp.pi*mp.mpf("1e-7")*299792458**2))),
"elemcharge": mp.mpf("1.6021766208e-19")
}
class Electron():
	def __init__(self,pos,vel,acc):
		self.mass = mp.mpf("0.511e+6")
		self.charge = mp.mpf(-1)
		self.spin = mp.mpf(1/2)
		self.pos = np.array(pos)
		self.vel = np.array(vel)
		self.acc = np.array(acc)
	def update(self):
		self.pos += self.vel
		self.vel += self.acc
	def show(self):
		return 0


class Muon():
	def __init__(self,pos,vel,acc):
		self.mass = mp.mpf('105.67e+6')
		self.charge = mp.mpf(-1)
		self.spin = mp.mpf(1/2)
		self.pos = np.array(pos)
		self.vel = np.array(vel)
		self.acc = np.array(acc)
	def update(self):
		self.pos += self.vel
		self.vel += self.acc
	def show(self):
		return 0


class Tau():
	def __init__(self,pos,vel,acc):
		self.mass = mp.mpf("1.7768e+9")
		self.charge = mp.mpf(-1)
		self.spin = mp.mpf(1/2)
		self.pos = np.array(pos)
		self.vel = np.array(vel)
		self.acc = np.array(acc)
	def update(self):
		self.pos += self.vel
		self.vel += self.acc
	def show(self):
		return 0


class Neutrino():
	def __init__(self,neutrinotype,pos,vel,acc):
		self.type = neutrinotype
		if(type == "electron"):
			self.mass = mp.mpf("2.2")
		if(type == "muon"):
			self.mass = mp.mpf("1.7e+6")
		if(type == "tau"):
			self.mass = mp.mpf("15.5e+6")
		self.charge = mp.mpf("0")
		self.spin = mp.mpf("1/2")
		self.pos = np.array(pos)
		self.vel = np.array(vel)
		self.acc = np.array(acc)
	def update(self):
		self.pos += self.vel
		self.vel += self.acc
	def show(self):
		return 0


class Z():
	def __init__(self,pos,vel,acc):
		self.mass = mp.mpf("91.19e+9")
		self.charge = mp.mpf(0)
		self.spin = mp.mpf(1)
		self.pos = np.array(pos)
		self.vel = np.array(vel)
		self.acc = np.array(acc)
	def update(self):
		self.pos += self.vel
		self.vel += self.acc
	def show(self):
		return 0


class W():
	def __init__(self,charge,pos,vel,acc):
		self.mass = mp.mpf("80.39e+9")
		self.charge = mp.mpf(charge)
		self.spin = mp.mpf(1)
		self.pos = np.array(pos)
		self.vel = np.array(vel)
		self.acc = np.array(acc)
	def update(self):
		self.pos += self.vel
		self.vel += self.acc
	def show(self):
		return 0


class Photon():
	def __init__(self,pos,vel,acc):
		self.mass = mp.mpf("0")
		self.charge = mp.mpf(0)
		self.spin = mp.mpf(1)
		self.pos = np.array(pos)
		self.vel = np.array(vel)
		self.acc = np.array(acc)
	def update(self):
		self.pos += self.vel
		self.vel += self.acc
	def show(self):
		return 0


class Gluon():
	def __init__(self,pos,vel,acc):
		self.mass = mp.mpf(0)
		self.charge = mp.mpf(0)
		self.spin = mp.mpf(1)
		self.pos = np.array(pos)
		self.vel = np.array(vel)
		self.acc = np.array(acc)
	def update(self):
		self.pos += self.vel
		self.vel += self.acc
	def show(self):
		return 0


class Higgs():
	def __init__(self,pos,vel,acc):
		self.mass = mp.mpf("125.09e+9")
		self.charge = mp.mpf(0)
		self.spin = mp.mpf(0)
		self.pos = np.array(pos)
		self.vel = np.array(vel)
		self.acc = np.array(acc)
	def update(self):
		self.pos += self.vel
		self.vel += self.acc
	def show(self):
		return 0


class Up():
	def __init__(self,pos,vel,acc):
		self.mass = mp.mpf("2.4e+6")
		self.charge = mp.mpf("2/3")
		self.spin = mp.mpf("1/2")
		self.pos = np.array(pos)
		self.vel = np.array(vel)
		self.acc = np.array(acc)
	def update(self):
		self.pos += self.vel
		self.vel += self.acc
	def show(self):
		return 0


class Charm():
	def __init__(self,pos,vel,acc):
		self.mass = mp.mpf("1.275e+9")
		self.charge = mp.mpf("2/3")
		self.spin = mp.mpf("1/2")
		self.pos = np.array(pos)
		self.vel = np.array(vel)
		self.acc = np.array(acc)
	def update(self):
		self.pos += self.vel
		self.vel += self.acc
	def show(self):
		return 0


class Top():
	def __init__(self,pos,vel,acc):
		self.mass = mp.mpf("172.44e+6")
		self.charge = mp.mpf("2/3")
		self.spin = mp.mpf("1/2")
		self.pos = np.array(pos)
		self.vel = np.array(vel)
		self.acc = np.array(acc)
	def update(self):
		self.pos += self.vel
		self.vel += self.acc
	def show(self):
		return 0


class Down():
	def __init__(self,pos,vel,acc):
		self.mass = mp.mpf("4.8e+6")
		self.charge = mp.mpf("-1/3")
		self.spin = mp.mpf("1/2")
		self.pos = np.array(pos)
		self.vel = np.array(vel)
		self.acc = np.array(acc)
	def update(self):
		self.pos += self.vel
		self.vel += self.acc
	def show(self):
		return 0


class Strange():
	def __init__(self,pos,vel,acc):
		self.mass = mp.mpf("95e+6")
		self.charge = mp.mpf("-1/3")
		self.spin = mp.mpf("1/2")
		self.pos = np.array(pos)
		self.vel = np.array(vel)
		self.acc = np.array(acc)
	def update(self):
		self.pos += self.vel
		self.vel += self.acc
	def show(self):
		return 0


class Bottom():
	def __init__(self,pos,vel,acc):
		self.mass = mp.mpf("4.18e+9")
		self.charge = mp.mpf("-1/3")
		self.spin = mp.mpf("1/2")
		self.pos = np.array(pos)
		self.vel = np.array(vel)
		self.acc = np.array(acc)
	def update(self):
		self.pos += self.vel
		self.vel += self.acc
	def show(self):
		return 0


particles = {
	"fermions": {
		"quarks":{
			"up":Up,
			"down": Down,
			"charm": Charm,
			"strange": Strange,
			"top": Top,
			"bottom": Bottom
		},
		"leptons":{
			"electron": Electron,
			"muon": Muon,
			"tau": Tau,
			"neutrino": Neutrino
		}
	},
	"bosons": {
		"gauge": {
			"W":W,
			"Z":Z,
			"photon": Photon,
			"gluon": Gluon
		},
		"scalar": {
			"higgs": Higgs
		}
	}
}

equations = {

}
