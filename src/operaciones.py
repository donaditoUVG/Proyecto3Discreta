import logging

# Configuración del logging
logging.basicConfig(filename='calculadora_modular.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

def validate_inputs(a, b, p):
    """
    Valida que las entradas sean enteros y que p sea un número primo positivo.
    """
    if not all(isinstance(x, int) for x in (a, b, p)):
        raise ValueError("Todos los argumentos deben ser enteros.")
    if p <= 1:
        raise ValueError("El módulo p debe ser un número primo mayor que 1.")
    if not is_prime(p):
        raise ValueError(f"{p} no es un número primo.")

def is_prime(n):
    """
    Verifica si un número es primo.
    """
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def mod_add(a, b, p):
    try:
        validate_inputs(a, b, p)
        result = (a + b) % p
        logging.info(f"Suma modular: {a} + {b} ≡ {result} (mod {p})")
        return result
    except ValueError as e:
        logging.error(f"Error en suma modular: {str(e)}")
        raise

def mod_subtract(a, b, p):
    try:
        validate_inputs(a, b, p)
        result = (a - b) % p
        logging.info(f"Resta modular: {a} - {b} ≡ {result} (mod {p})")
        return result
    except ValueError as e:
        logging.error(f"Error en resta modular: {str(e)}")
        raise

def mod_multiply(a, b, p):
    try:
        validate_inputs(a, b, p)
        result = (a * b) % p
        logging.info(f"Multiplicación modular: {a} * {b} ≡ {result} (mod {p})")
        return result
    except ValueError as e:
        logging.error(f"Error en multiplicación modular: {str(e)}")
        raise

def mod_divide(a, b, p):
    try:
        validate_inputs(a, b, p)
        if b == 0:
            raise ValueError("División por cero no está permitida.")
        # Encontrar el inverso multiplicativo de b
        b_inv = pow(b, -1, p)
        result = (a * b_inv) % p
        logging.info(f"División modular: {a} / {b} ≡ {result} (mod {p})")
        return result
    except ValueError as e:
        logging.error(f"Error en división modular: {str(e)}")
        raise

def mod_power(base, exponent, p):
    try:
        validate_inputs(base, exponent, p)
        if exponent < 0:
            raise ValueError("El exponente debe ser no negativo.")
        result = pow(base, exponent, p)
        logging.info(f"Potencia modular: {base}^{exponent} ≡ {result} (mod {p})")
        return result
    except ValueError as e:
        logging.error(f"Error en potencia modular: {str(e)}")
        raise

def evaluate_expression(expression, p):
    try:
        validate_inputs(p, p, p)  # Validamos que p sea un entero primo
        # Aquí iría la lógica para evaluar la expresión
        # Por ahora, solo evaluaremos expresiones simples
        result = eval(expression) % p
        logging.info(f"Evaluación de expresión: {expression} ≡ {result} (mod {p})")
        return result
    except Exception as e:
        logging.error(f"Error al evaluar la expresión: {str(e)}")
        raise ValueError(f"Error al evaluar la expresión: {str(e)}")