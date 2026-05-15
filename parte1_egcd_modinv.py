"""
Parte 1 — Euclides extendido e inverso modular
CE-1115 Seguridad de la Información

Funciones:
  egcd(a, b)      -> (g, x, y)  con g = gcd(a,b)  y  a*x + b*y = g
  modinv(e, phi)  -> d          con (e * d) mod phi = 1
"""


def egcd(a, b):
    """Algoritmo de Euclides extendido (recursivo).

    Retorna (g, x, y) tal que g = gcd(a, b) y a*x + b*y = g.
    """
    if b == 0:
        return (a, 1, 0)
    g, x1, y1 = egcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return (g, x, y)


def modinv(e, phi):
    """Inverso modular de e modulo phi usando Euclides extendido.

    Retorna d tal que (e * d) % phi == 1.
    Lanza ValueError si e y phi no son coprimos (gcd != 1).
    """
    e = e % phi  # normalizar antes de llamar a egcd
    g, x, _ = egcd(e, phi)
    if g != 1:
        raise ValueError(
            f"e={e} no es invertible modulo phi={phi} (gcd={g}, deben ser coprimos)"
        )
    return x % phi
