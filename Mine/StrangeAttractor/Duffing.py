import numpy as np

class particle:
    def __init__(self,position,velocity,mass,a,b,f0,omega,gamma):
        self.time = 0
        self.position = position
        self.velocity = velocity
        self.mass = mass
        self.forceparams = {} 
        self.forceparams['a'] = a
        self.forceparams['b'] = b
        self.forceparams['f0'] = f0
        self.forceparams['omega'] = omega
        self.forceparams['gamma'] = gamma
        self.force = (-self.forceparams['gamma']*self.velocity
                +2*self.forceparams['a']*self.position
                -4*self.forceparams['b']*self.position**3
                +self.forceparams['f0']*np.cos(self.forceparams['omega']*self.time))

    def runge_kutta(self,dt):
        k1 = dt*self.force/self.mass
        l1 = dt*self.velocity
        k2 = dt*(1/self.mass*(-self.forceparams['gamma']*(self.velocity+k1/2)
              +2*self.forceparams['a']*(self.position+l1/2)
              -4*self.forceparams['b']*(self.position+l1/2)**3
              +self.forceparams['f0']*np.cos(self.forceparams['omega']*(self.time+dt/2))))
        l2 = dt*(self.velocity+k1/2)
        k3 = dt*(1/self.mass*(-self.forceparams['gamma']*(self.velocity+k2/2)
              +2*self.forceparams['a']*(self.position+l2/2)
              -4*self.forceparams['b']*(self.position+l2/2)**3
              +self.forceparams['f0']*np.cos(self.forceparams['omega']*(self.time+dt/2))))
        l3 = dt*(self.velocity+k2/2)
        k4 = dt*(1/self.mass*(-self.forceparams['gamma']*(self.velocity+k3)
              +2*self.forceparams['a']*(self.position+l3)
              -4*self.forceparams['b']*(self.position+l3)**3
              +self.forceparams['f0']*np.cos(self.forceparams['omega']*(self.time+dt))))
        l4 = dt*(self.velocity+k3)
        self.velocity = self.velocity+(k1+2*(k2+k3)+k4)/6
        self.position = self.position+(l1+2*(l2+l3)+l4)/6
        self.time = self.time+dt




