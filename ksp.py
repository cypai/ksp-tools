pi = 3.14159265

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
    t = 2*pi*(a*a*a/g)**0.5
    h = int(t/3600)
    m = int(60*(t/3600-h))
    s = int(60*(60*(t/3600-1)-m))
    return (h, m, s, t)

def print_prd(a, g):
    h, m, s, t = orbital_period(a, g)
    print(f"{h}h {m}m {s}s")
