import math
from operaciones import validate_inputs, is_prime

def mod_inverse(a: int, m: int) -> int:
    validate_inputs(a, m, m)
    
    def extended_euclidean(a: int, b: int) -> tuple:
        if a == 0:
            return b, 0, 1
        else:
            gcd, x, y = extended_euclidean(b % a, a)
            return gcd, y - (b // a) * x, x

    gcd, x, _ = extended_euclidean(a, m)
    if gcd != 1:
        raise ValueError(f"El inverso multiplicativo de {a} módulo {m} no existe.")
    else:
        return x % m

def mod_sqrt(a: int, p: int) -> int:
    validate_inputs(a, p, p)
    if not is_prime(p):
        raise ValueError(f"{p} debe ser primo.")
    
    if pow(a, (p - 1) // 2, p) != 1:
        raise ValueError(f"{a} no tiene raíz cuadrada módulo {p}")
    
    q = p - 1
    s = 0
    while q % 2 == 0:
        q //= 2
        s += 1
    
    if s == 1:
        return pow(a, (p + 1) // 4, p)
    
    for z in range(2, p):
        if pow(z, (p - 1) // 2, p) == p - 1:
            break
    
    c = pow(z, q, p)
    r = pow(a, (q + 1) // 2, p)
    t = pow(a, q, p)
    m = s
    
    while t != 1:
        tt = t
        for i in range(1, m):
            tt = (tt * tt) % p
            if tt == 1:
                break
        b = pow(c, 1 << (m - i - 1), p)
        r = (r * b) % p
        c = (b * b) % p
        t = (t * c) % p
        m = i
    
    return r

def chinese_remainder_theorem(remainders: list, moduli: list) -> int:
    if len(remainders) != len(moduli):
        raise ValueError("El número de residuos debe ser igual al número de módulos.")
    
    total = 0
    product = math.prod(moduli)
    
    for remainder, modulus in zip(remainders, moduli):
        p = product // modulus
        total += remainder * mod_inverse(p, modulus) * p
    
    return total % product
