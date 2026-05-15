"""
Parte 2 — Par de claves con p y q dados (sin aleatorio todavía)
CE-1115 Seguridad de la Información
"""

import math
from parte1_egcd_modinv import modinv


def generar_claves(p, q, e=None):
    """
    Genera un par de claves RSA (n, e, d) dados dos primos p y q.

    p: primer número primo
    q: segundo número primo (distinto de p)
    e: exponente público (opcional, por defecto 17)
    """
    # Validaciones
    assert p != q, "p y q deben ser distintos"

    # Paso 1: Calcular n y φ(n)
    n = p * q
    phi = (p - 1) * (q - 1)

    # Paso 2: Elegir e (por defecto 17, o 65537 si φ(n) > 65537)
    if e is None:
        e = 65537 if phi > 65537 else 17

    # Paso 3: Validar que e es coprime con φ(n) y 1 < e < φ(n)
    assert 1 < e < phi, f"e debe cumplir 1 < e < φ(n). Recibido e={e}, φ(n)={phi}"
    assert math.gcd(e, phi) == 1, f"gcd(e, φ(n)) debe ser 1. gcd({e}, {phi}) = {math.gcd(e, phi)}"

    # Paso 4: Calcular d = modinv(e, φ(n))
    d = modinv(e, phi)

    # Paso 5: Verificación
    assert (e * d) % phi == 1, f"Verificación fallida: ({e} * {d}) mod {phi} != 1"

    return n, e, d


if __name__ == "__main__":
    print("=" * 60)
    print("Parte 2: Generación de par de claves RSA")
    print("=" * 60)

    # Opción 1: Primos pequeños con e=17
    print("\n[Test 1] Primos pequeños: p=61, q=53, e=17")
    p, q = 61, 53
    n, e, d = generar_claves(p, q, e=17)

    print(f"  p = {p}")
    print(f"  q = {q}")
    print(f"  n = {n}")
    print(f"  φ(n) = {(p - 1) * (q - 1)}")
    print(f"  e (exponente público) = {e}")
    print(f"  d (exponente privado) = {d}")
    print(f"  Verificación: ({e} * {d}) mod {(p - 1) * (q - 1)} = {(e * d) % ((p - 1) * (q - 1))}")
    assert (e * d) % ((p - 1) * (q - 1)) == 1

    # Opción 2: Primos más grandes con e=65537
    print("\n[Test 2] Primos mayores: p=1009, q=1013, e=65537")
    p2, q2 = 1009, 1013
    n2, e2, d2 = generar_claves(p2, q2, e=65537)

    print(f"  p = {p2}")
    print(f"  q = {q2}")
    print(f"  n = {n2}")
    print(f"  φ(n) = {(p2 - 1) * (q2 - 1)}")
    print(f"  e (exponente público) = {e2}")
    print(f"  d (exponente privado) = {d2}")
    print(f"  Verificación: ({e2} * {d2}) mod {(p2 - 1) * (q2 - 1)} = {(e2 * d2) % ((p2 - 1) * (q2 - 1))}")
    assert (e2 * d2) % ((p2 - 1) * (q2 - 1)) == 1
