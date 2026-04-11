from math import sqrt


class LinearError(Exception):
    pass

class QuadraticError(Exception):
    pass

class equation():
    """ENG
    ---------

    A class that allows you to solve quadratic and linear equations.

    Methods:
        linear_one_variable: solves the linear equation with one variable.
        quadratic: solves the quadratic equation.
    
    RU
    ---------

    Класс, позваоляющий решать квадратные и линейные уравнения.

    Методы:
        linear_one_variable: решает линейное уравнение с одной переменной.

        quadratic: решает квадратное уравнение.
    """

    def linear_one_variable(self, a: int, b: int, solution: bool = False):
        """
        ENG
        ---------
        Solves the linear equation with one variable. Accepts the values a and b from formula "ax + b = 0" and an optional argument solution, which displays the solution on the console. Returns a tuple with None in case of failure or with 1 root of a linear equation or with True(any root) in case of success.
        
        RU
        ---------
        Решает линейное уравнение. Принимает аргументы a и b из формулы "ax + b = 0" и необязательный аргумент solution, который отвечает за вывод решения на консоль. Возвращает кортеж с None в случае неудачи или кортеж с 1 корнем уравнения или с True(любой корень) в случае успеха.
        """
        try:
            if a == 0 and b != 0:
                return None
            elif a == 0 and b == 0:
                return True
            else:
                b = -b
                x = -b / a
                if solution:
                    print(f"Root:  x = -b / a = x = -{b} / {a} = {x}.")
                return x
        except TypeError:
            raise TypeError("a and b must be int type, not other.")
        except Exception as e:
            raise LinearError(f"an error has occured the linear function - {e}.")
    
    def quadratic(self, a: int, b: int, c: int, solution: bool=False):
        """
    ENG
    --------
    Solves the quadratic equation. Accepts the values a, b, and c from formula "ax + bx + c = 0" and an optional argument solution, which displays the solution on the console. Returns a tuple with None in case of failure, or with 1 or 2 roots of a quadratic equation in case of success.
    
    RU
    --------
    Решает квадратное уравнение. Принимает аргументы a, b и с из формулы "ax + bx + c = 0" и необязательный аргумент solution, который отвечает за вывод решения на консоль. Возвращает кортеж с None в случае неудачи или кортеж с 1 или 2 корнями уравнения в случае успеха.
    """
        try:
            d = (b ** 2) - 4 * a * c
            if solution:
                print(f"Discriminant: (b ** 2) - 4 * a * c = ({b} ** 2) - 4 * {a} * {c} = {d}.")
            if d > 0:
                x1 = (-b - sqrt(d)) / 2 * a
                x2 = (-b + sqrt(d)) / 2 * a
                if solution: 
                    print(f"First root: x1 = (-b - sqrt(d)) / 2 * a = (-{b} - {sqrt(d)} / 2 * {a} = {x1}.")
                    print(f"Second root: x2 = (-b + sqrt(d)) / 2 * a = (-{b} + {sqrt(d)}) / 2 * {a} = {x2}.")
                    print(f"Roots: {x1}, {x2}.")
                return x1, x2
            elif d == 1:
                x = -b / 2 * a
                print(f"Root: x = -b / 2 * a = -{b} / 2 * {a} = {x}.")
                print(f"Root: {x}.")
                return x
            elif d < 0 :
                if solution:
                    print('No roots.')
                return None
        except TypeError:
            raise TypeError("a, b and c must be int type, not other.")
        except Exception as e:
            raise QuadraticError(f"an error has occured the quadratic function - {e}.")
