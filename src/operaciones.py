def mod_add(a, b, p):
    return (a + b) % p

def mod_subtract(a, b, p):
    return (a - b) % p

def mod_multiply(a, b, p):
    return (a * b) % p

def mod_divide(a, b, p):
    try:
        inverso = pow(b, -1, p)  # Inverso multiplicativo de b mod p
        return (a * inverso) % p
    except ValueError:
        raise ValueError("No se puede dividir por este valor en el módulo dado")

def mod_power(base, exponent, p):
    return pow(base, exponent, p)

def evaluate_expression(expression, p):
    # Implementar evaluación de expresiones
    pass