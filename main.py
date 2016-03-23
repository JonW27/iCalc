import click
import math
import random
from simpleeval import simple_eval
from fractions import Fraction

@click.group()
def cli():
    pass

@click.command()
@click.argument('number')
def sqr(number):
    """Squares the number\n
    Example: bron sqr 2 returns 2 * 2 or 4
    """
    num = int(number) ** 2
    click.echo(num)

@click.command()
@click.argument('number')
def fact(number):
    """Gets the factorial\n
     Example: bron fact 3 returns 3 * 2 * 1 or 6"""
    result = 1
    if int(number) > 0:
    	for a in range(1, (int(number) + 1)):
    		result = result * a
    else:
    	result = 0
    click.echo(result)

@click.command()
@click.argument('number')
def sin(number):
    """Gets the sin of the radians inputted\n
    Example: bron sin 1 returns 0.84...
    """
    try:
    	mod = float(number)
    except ValueError:
    	mod = int(number)
    if 0 <= mod <= 2 * math.pi:
    	click.echo(math.sin(mod))
    else:
	click.echo("Result needs to be in the range of 0 to 2 pi")

@click.command()
def pi():
    '''returns the value of pi'''
    click.echo(math.pi)

@click.command()
def v():
    '''calc/bron version number'''
    click.echo('iCalc v0.1')

def square(x):
    return x ** 2

def sine(x):
    return math.sin(x)

def cosine(x):
    return math.cos(x)

def tangent(x):
    return math.tan(x)

def arctan(x):
    return math.atan(x)

def arccos(x):
    return math.acos(x)

def arcsin(x):
    return math.asin(x)

def secant(x):
    return 1 /  math.cos(x)

def cosecant(x):
    return 1 / math.sin(x)

def cotangent(x):
    return 1 / math.tan(x)

def factorial(x):
    result = 1
    if int(x) > 0:
        for a in range(1, (int(x) + 1)):
                result = result * a
    else:
        result = 0
    return result

def sigma(x):
    result = 0
    if int(x) > 0:
        for a in range(1, (int(x) + 1)):
                result = result + a
    else:
        result = 0
    return result

def sqrt(x):
    return math.sqrt(x)

def deg2rad(x):
    return x * math.pi / 180

def deg2radf(x):
    return str(Fraction(x, 180)) + "pi"

def fib(x):
    start = 1
    beg = True
    for a in range(1, (x + 1)):
        if start == 1 and beg:
            beg = False
            prev = 0
        previous = start
        start = start + prev
        prev = previous
    return start

def prime(x):
    for i in range(3, x):
        if x % i == 0:
            return False
    return True

def floor(x):
    return math.floor(x)

def ceil(x):
    return math.ceil(x)

def rand():
    return random.random()

def randInt(x):
    return random.randinit()

def absolute(x):
    return abs(x)

def perm(x, y):
    return factorial(x) / factorial(x-y)

def comb(n, r):
    return perm(n,r) / factorial(r)

def mod(x, y):
    return x % y

@click.command()
@click.argument('expression')
def calc(expression):
    '''evaluates the expression\n
    IMPORTANT: expressions must be surrounded by single or double quotes\n
    IMPORTANT: the pi constant cannot be used as 2pi but must be stated as 2 * pi\n
    WARNING: Chemistry/Physics constants are based on their respective reference tables and may have different units. Be aware that one constant may be listed in kJ and another in J and as a result the calculation does not work out\n
    Example: "3**2" returns 9\n
    List of fxns supported are sin, cos, tan, sec, csc, cot, arcsin, arccos, arctan, fact, sum, sqr, sqrt, deg2rad, deg2radf (fractional pi form), fib, prime, floor, ceil, rand, randInt, abs, perm (permutation), comb (combination), and mod. The pi, e, heat of fusion, heat of vaporization, gravity constants along with Avogadro's number (L) and Planck's constant (h) are also supported.'''
    express = str(expression)
    click.echo(simple_eval(express, names={"pi": math.pi, "PI": math.pi, "e": math.e, "c": 3 * 10 ** 8, "h": 6.62607004 * 10 ** -34, "g": 9.81, "hf": 334, "hv": 4.18, "L": 6.022 * 10 ** 23}, functions={"sqr": square, "sin": sine, "cos": cosine, "tan":tangent, "asin":arctan, "acos":arccos, "atan":arctan, "sec":secant, "csc":cosecant, "cot":cotangent, "fact": factorial, "sum": sigma, "sigma":sigma, "sqrt":sqrt, "deg2rad":deg2rad, "deg2radf":deg2radf, "fib":fib, "prime":prime, "floor":floor, "ceil":ceil, "rand":rand, "randInt":randInt, "abs":absolute, "perm": perm, "comb": comb, "mod":mod}))

cli.add_command(fact)
cli.add_command(sqr)
cli.add_command(sin)
cli.add_command(pi)
cli.add_command(calc)
cli.add_command(v)
