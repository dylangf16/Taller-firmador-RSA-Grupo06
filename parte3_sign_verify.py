"""
Parte 3 — Exponente modular y "firma" sobre un entero H de prueba

Funciones:
  sign_integer(H, n, d)    -> S    donde S = pow(H, d, n)
  verify_integer(S, H, n, e) -> bool  donde verifica pow(S, e, n) == H

Validaciones: 1 < H < n (se lanza ValueError si H fuera de rango)

Ejemplo en `if __name__ == "__main__"` usando (n, d, e) típicos:
  n = 3233, e = 17, d = 2753

Pruebas: varios valores de H y comprobación de que la verificación da True.
"""


def firmar_entero(H: int, n: int, d: int) -> int:
    """Firma el entero H con la clave privada `d` módulo `n`.

    Retorna S = pow(H, d, n).
    Lanza ValueError si H no cumple 1 < H < n.
    """
    if not (1 < H < n):
        raise ValueError(f"H inválido: {H}. Debe cumplir 1 < H < n (n={n}).")
    return pow(H, d, n)


def verificar_entero(S: int, H: int, n: int, e: int) -> bool:
    """Verifica que `S` sea la firma de `H` usando la clave pública `e` módulo `n`.

    Retorna True si pow(S, e, n) == H, False en caso contrario.
    Lanza ValueError si H no cumple 1 < H < n.
    """
    if not (1 < H < n):
        raise ValueError(f"H inválido: {H}. Debe cumplir 1 < H < n (n={n}).")
    return pow(S, e, n) == H


if __name__ == "__main__":
    # Parámetros de ejemplo (resultado de la Parte 2 típica)
    n = 3233
    e = 17
    d = 2753

    test_values = [65, 123, 3000]

    for H in test_values:
        try:
            S = firmar_entero(H, n, d)
            ok = verificar_entero(S, H, n, e)
            print(f"H={H}: S={S}, verify -> {ok}")
        except ValueError as exc:
            print(f"H={H}: error -> {exc}")
