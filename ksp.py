import math

# See https://wiki.kerbalspaceprogram.com/wiki/Tutorial:Ideal_Orbits_for_Communication_Satellites

class Body:
    def __init__(self, r, G):
        self.r = r
        self.G = G

bodies = {
    "Kerbin": Body(600000, 3.5316e12),
    "Mun": Body(200000, 6.5138398e10),
    "Minmus": (60000, 1.7658e9),
}

def orbital_period(a, g):
    """
    t: orbital period in seconds
    a: semi-major axis of the orbit in meters (typically twice the body's radius)
    g: standard gravitation parameter in m3/s2
    """
    t = 2*math.pi*(a*a*a/g)**0.5
    h = int(t/3600)
    m = int(60*(t/3600-h))
    s = int(60*(60*(t/3600-h)-m))
    return (h, m, s, t)

def seconds(h, m, s):
    return s + 60*m + 3600*h
    
def desired_altitude(t: int, body: Body):
    """
    Returns the altitude of an orbit for a desired orbital period t
    """
    a = ((body.G*t*t)/(4*math.pi*math.pi))**(1/3)
    return a - body.r

def three_commsats(body: Body, antenna_range: int):
    min_orbital_period = orbital_period(body.r*2, body.G)
    h,m,s,t = min_orbital_period
    print(f"Min Altitude: {body.r*2-body.r}")
    print(f"Min Orbital Period: {h}h {m}m {s}s (total {t}s)")
    max_a = antenna_range/math.sqrt(3)
    max_orbital_period = orbital_period(max_a, body.G)
    h,m,s,t = max_orbital_period
    print(f"Max Altitude: {max_a - body.r}")
    print(f"Max Orbital Period: {h}h {m}m {s}s (total {t}s)")

def four_commsats(body: Body, antenna_range: int):
    min_a = body.r*math.sqrt(2)
    min_orbital_period = orbital_period(min_a, body.G)
    h,m,s,t = min_orbital_period
    print(f"Min Altitude: {min_a - body.r}")
    print(f"Min Orbital Period: {h}h {m}m {s}s (total {t}s)")
    max_a = antenna_range/math.sqrt(2)
    max_orbital_period = orbital_period(max_a, body.G)
    h,m,s,t = max_orbital_period
    print(f"Max Altitude: {max_a - body.r}")
    print(f"Max Orbital Period: {h}h {m}m {s}s (total {t}s)")
