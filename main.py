from math import sqrt
from typing import Literal


class LinearError(Exception):
    """An error has occured the linear function."""
    pass

class QuadraticError(Exception):
    """An error has occured the quadratic function."""
    pass

class NotLinearWithTwoVariablesError(Exception):
    """A system of linear equations with two variables is a linear equation with one variable. """
    pass

def linear_one_variable(a: int | float = 0, b: int | float = 0, solution: bool = False):
    """
    ENG
    ---------
    Solves the linear equation with one variable. Accepts the values a and b from formula "ax + b = 0" and an optional argument solution, which displays the solution on the console. Returns False in case of failure, with root of the linear equation or True(any root) in case of success.
    
    RU
    ---------
    Решает линейное уравнение с одной переменной. Принимает аргументы a и b из формулы "ax + b = 0" и необязательный аргумент solution, который отвечает за вывод решения на консоль. Возвращает False в случае неудачи, корень уравнения или True(любой корень) в случае успеха.
    """
    try:
        if a == 0 and b != 0:
            if solution:
                print('No roots.')
            return False
        elif a == 0 and b == 0:
            return True
        if solution:
            print("Any roots.")
        else:
            b = -b
            x = -b / a
            if solution:
                print(f"Root:  x = -b / a = x = {-b} / {a} = {x}.")
            return x
    except TypeError:
        raise TypeError("a and b must be int, not another type.")
    except Exception as e:
        raise LinearError(f"an error has occured the linear function - {e}.")

def linear_two_variables(a1: int | float = 0, b1: int | float = 0, c1: int | float = 0, a2: int | float = 0, b2: int | float = 0, c2: int | float = 0, solution: bool = False):
    """
    ENG
    ---------
    Solves a system of linear equations with two variables. Accepts the arguments a1, b1, c1 and a2, b2, c2 from the formula 

    {a1 * x + b1 * y = c1, 

    {a2 * x + b2 * y = c2. 

    and the optional argument solution, which displays the solution on the console. Returns False in case of failure, a tuple with the roots of the linear equation (x and y), or True (any root) in case of success.
    
    RU
    ---------
    Решает систему линейных уравнений с двумя переменными. Принимает аргументы a1, b1, c1 and a2, b2, c2 из формулы

    {a1 * x + b1 * y = c1, 

    {a2 * x + b2 * y = c2.

    и необязательный аргумент solution, который отвечает за вывод решения на консоль. Возвращает False в случае неудачи, кортеж с корнями уравнения(x и y) или True(любой корень) в случае успеха.
    """
    try:
        if a1 == 0 or b1 == 0 or a2 == 0 or b2 == 0:
            raise NotLinearWithTwoVariablesError("For given arguments, a system of linear equations with two variables is a linear equation with one variable.\nTo solve linear equations with one variable, use the linear_one_variable function.")
        if c2 != 0 and (a1 / b1) == (b1 / b2) and (a1 / a2) != (c1 / c2):
            if solution:
                print("No roots.")
            return False
        elif c2 != 0 and a1 / b1 == b1 / b2 == c1 / c2:
            if solution:
                print("Any roots.")
            return True
        else:
            factor = a2 / a1
            a1, b1, c1, a2, b2, c2 = map(float, [a1, b1, c1, a2, b2, c2])
            if solution:
                first_equation = f"Old: {a1}x + {b1}y = {c1}. New: {a1 * factor}x + {b1 * factor}y = {c1 * factor}."
                second_equation = f"Old: {a2}x + {b2}y = {c2}. New: {a2 * factor}x + {b2 * factor}y = {c2 * factor}."
            a1 *= factor
            b1 *= factor
            c1 *= factor
            if a1 + a2 != 0:
                a1 = -a1
                b1 = -b1
                c1 = -c1
            if solution:
                print(f"Equating the equation, by multiplying it by {factor}:\n{first_equation}\n{second_equation}\nA new system of linear equations:\n{a1}x - {-b1}y = {c1},\n{a2}x + {b2}y = {c2}.")
            b = b1 + b2
            c = c1 + c2
            if solution:
                print(f"Adding the systems. Result: {b}y = {c}")
            if b == 0 and c != 0:
                if solution:
                    print("No roots.")
                    return False
            if b == 0 and c == 0:
                if solution:
                    print("Any roots.")
                    return True
            b = -b
            y = -c / b
            if abs(y) == 0:
                y = abs(y)
            if solution:
                print(f"Root y: y = -b / a = {-c} / {b} = {y}.")
            a1 = -a1
            b1 = -b1
            c1 = -c1
            if solution:
                print(f"Substituting 'y' into the equation {a1}x + {b1}y = {c1}:\n{a1}x + ({b1} * {y}) = {c1}.")
            b1 = b1 * y
            b1 = -b1 + c1
            x = b1 / a1
            if abs(x) == 0:
                x = abs(x)
            if solution:
                print(f"Root x: x = -b / a = {b1} / {a1} = {x}.")
        return x, y
    except TypeError:
        raise TypeError("a1, b1, c1 and a2, b2, c2 must be int, not another type.")



def quadratic(a: int | float = 0, b: int | float = 0, c: int | float = 0, solution: bool = False) -> (tuple[float, float] | float | Literal[False]):
    """
    ENG
    --------
    Solves the quadratic equation. Accepts the values a, b, and c from formula "a(x ** 2) + bx + c = 0" and an optional argument solution, which displays the solution on the console. Returns False in case of failure, or with 1 or 2 roots of a quadratic equation in case of success.

    RU
    --------
    Решает квадратное уравнение. Принимает аргументы a, b и с из формулы "a(x ** 2) + bx + c = 0" и необязательный аргумент solution, который отвечает за вывод решения на консоль. Возвращает False в случае неудачи или кортеж с 1 или 2 корнями уравнения в случае успеха.
    """
    try:
        d = (b ** 2) - 4 * a * c
        if solution:
            print(f"Discriminant: (b ** 2) - 4 * a * c = ({b} ** 2) - 4 * {a} * {c} = {d}.")
        if d > 0:
            x1 = (-b - sqrt(d)) / 2 * a
            x2 = (-b + sqrt(d)) / 2 * a
            if solution: 
                print(f"First root: x1 = (-b - sqrt(d)) / 2 * a = ({-b} - {sqrt(d)} / 2 * {a} = {x1}.")
                print(f"Second root: x2 = (-b + sqrt(d)) / 2 * a = ({-b} + {sqrt(d)}) / 2 * {a} = {x2}.")
                print(f"Roots: {x1}, {x2}.")
            return x1, x2
        elif d == 1:
            x = -b / 2 * a
            print(f"Root: x = -b / 2 * a = {-b} / 2 * {a} = {x}.")
            print(f"Root: {x}.")
            return x
        elif d < 0 :
            if solution:
                print('No roots.')
            return False
    except TypeError:
        raise TypeError("a, b and c must be int, not another type.")
    except Exception as e:
        raise QuadraticError(f"an error has occured the quadratic function - {e}.")

