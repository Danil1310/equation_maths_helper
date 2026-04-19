# equation_maths_helper #

# ENG #

A module that allows you to solve quadratic and linear equations.

## How to use? ##

### Installing and importing ###

First, install the equation_maths_helper module using the `pip` package manager.


    pip install equation_maths_helper

After that, you can import it:


    import equation_maths_helper

For convenience, we recommend importing all methods from the module at once.


    from equation_maths_helper import *

### The `str_in_eq` method ###

The `str_in_eq` method converts the received string into an equation (finds the coefficients). 


The method takes a string with a linear equation (`ax + bx = 0`), a system of linear equations with two variables (`a1x + b1x = c1, a2x + b2x = c2`), or a quadratic equation (`ax + bx = 0`), and the `format` argument, which determines the type of equation. Signs in equations are written with a space, systems are written with a comma, and the square is denoted as `x`. Returns a tuple with the coefficients of the equation.


 Example of using the method:

    from equation_maths_helper import str_in_eq
    equation = str_in_eq('1x + 6x - 5 = 0', 'quadratic')
    print(equation)


 Output the coefficients to the console:

    (1.0, 6.0, -5.0)
    
### The `linear_one_variable` method ###

The `linear_one_variable` method allows you to solve linear equations with a single variable.


The method accepts the coefficients `a` and `b` from the formula `ax + b = 0`. It also has an additional `solution` parameter, which is responsible for outputting a step-by-step solution to the console. By default it is set to `False`. The method returns `False` if it fails (there are no roots), the root of the equation, or `True` if the root is any number.


An example of using the method:

    from equation_maths_helper import linear_one_variable
    equation_answer = linear_one_variable(a=1, b=1, solution=True)
    print(equation_answer)


Output the solution to the console:

    Root: x = -b / a = x = -1 / 1 = -1.0.
    -1.0
    
### The `linear_two_variables` method ###

The `linear_two_variables` method allows you to solve systems of linear equations with two variables.

The method takes the coefficients `a1`, `b1`, `c1` and `a2`, `b2`, `c2` from the formula

    {a1 * x + b1 * y = c1, 
    {a2 * x + b2 * y = c2.

and an optional argument `solution`, which is responsible for displaying the solution on the console. By default, it is set to `False`. Returns `False` in case of failure, a tuple with the roots of the equation (x and y), or `True`(any root) in case of success.


An example of using the method:

    from equation_maths_helper import linear_two_variables
    equation_answer = linear_two_variables(a1=1, b1=-3, c1=11, a2=2, b2=4, c2=-8, solution=True)
    print(equation_answer)

Output the solution to the console:

    Equating the equation, by multiplying it by 2.0:
    Old: 1.0x + -3.0y = 11.0. New: 2.0x + -6.0y = 22.0.
    Old: 2.0x + 4.0y = -8.0. New: 4.0x + 8.0y = -16.0.
    A new system of linear equations:
    -2.0x - -6.0y = -22.0,
    2.0x + 4.0y = -8.0.
    Adding the systems. Result: 10.0y = -30.0
    Root y: y = -b / a = 30.0 / -10.0 = -3.0.
    Substituting 'y' into the equation 2.0x + -6.0y = 22.0:
    2.0x + (-6.0 * -3.0) = 22.0.
    Root x: x = -b / a = 4.0 / 2.0 = 2.0.
    (2.0, -3.0)
 
### The `quadratic` method ###

The `quadratic` method allows you to solve quadratic equations.


The method accepts the coefficients `a`, `b`, and `c` from the formula `a(x ** 2) + bx + c = 0`. It also has an additional parameter `solution`, which is responsible for displaying the step-by-step solution on the console. By default, it is set to `False`. The method returns `False` if it fails (no roots) or a tuple with 1 or 2 roots of the equation.


An example of using the method:

    from equation_maths_helper import quadratic
    equation_answer = quadratic(a=1, b=1, c=1, solution=True)
    print(equation_answer)


Output the solution to the console:

    Discriminant: (b ** 2) - 4 * a * c = (-5 ** 2) - 4 * 1 * 6 = 1.
    First root: x1 = (-b - sqrt(d)) / 2 * a = (5 - 1.0) / 2 * 1 = 2.0.
    Second root: x2 = (-b + sqrt(d)) / 2 * a = (5 + 1.0) / 2 * 1 = 3.0.
    Roots: 2.0, 3.0.
    (2.0, 3.0)
 
# RU #

Модуль, позволяющий решать квадратные и линейные уравнения.

## Как использовать? ##

### Установка и импорт ###

Первым делом установите модуль equation_maths_helper через менеджер пакетов `pip`.


    pip install equation_maths_helper

После этого вы сможете его импортировать:

    import equation_maths_helper

Для удобства рекомендуем сразу импортировать все методы из модуля.


    from equation_maths_helper import *

### Метод `str_in_eq` ###

Метод `str_in_eq` переводит полученную строку в уравнение(находит коэффициенты). 


Метод принимает строку с линейным уравнением(`ax + bx = 0`), с системой линейных уравнений с двумя переменными(`a1x + b1x = c1, a2x + b2x = c2`) или с квадратным уравнением(`ax + bx = 0`) и аргумент `format`, отвечающий за тип уравнения. Знаки в уравнениях пишутся через пробел, системы пишутся через запятую, квадрат обозначается как `x`. Возвращает кортеж с коэффициентами уравнения.


Пример использования метода:

    from equation_maths_helper import str_in_eq
    equation = str_in_eq('1x + 6x - 5 = 0', 'quadratic')
    print(equation)


Вывод коэффициентов на консоль:

    (1.0, 6.0, -5.0)
    
### Метод `linear_one_variable` ###

Метод `linear_one_variable` позволяет решать линейные уравнения с одной переменной.


Метод принимает коэффициенты `a` и `b` из формулы `ax + b = 0`. Также у него есть дополнитеьный параметр `solution`, который отвечает за вывод пошагового решения на консоль. По умолчанию он равен `False`. Метод возвращает `False` в случае неудачи(нет корней), корень уравнения или `True`, если корень любое число.


Пример использования метода:

    from equation_maths_helper import linear_one_variable
    equation_answer = linear_one_variable(a=1, b=1, solution=True)
    print(equation_answer)


Вывод решения на консоль:

    Root:  x = -b / a = x = -1 / 1 = -1.0.
    -1.0

### Метод `linear_two_variables` ###

Метод `linear_two_variables` позволяет решать системы линейных уравнений с двумя переменными.

Метод принимает коээфициенты `a1`, `b1`, `c1` and `a2`, `b2`, `c2` из формулы

    {a1 * x + b1 * y = c1, 
    {a2 * x + b2 * y = c2.

и необязательный аргумент `solution`, который отвечает за вывод решения на консоль. По умолчанию он равен `False`. Возвращает `False` в случае неудачи, кортеж с корнями уравнения(x и y) или `True`(любой корень) в случае успеха.


Пример использования метода:

    from equation_maths_helper import linear_two_variables
    equation_answer = linear_two_variables(a1=1, b1=-3, c1=11, a2=2, b2=4, c2=-8, solution=True)
    print(equation_answer)

Вывод решения на консоль:

    Equating the equation, by multiplying it by 2.0:
    Old: 1.0x + -3.0y = 11.0. New: 2.0x + -6.0y = 22.0.
    Old: 2.0x + 4.0y = -8.0. New: 4.0x + 8.0y = -16.0.
    A new system of linear equations:
    -2.0x - -6.0y = -22.0,
    2.0x + 4.0y = -8.0.
    Adding the systems. Result: 10.0y = -30.0
    Root y: y = -b / a = 30.0 / -10.0 = -3.0.
    Substituting 'y' into the equation 2.0x + -6.0y = 22.0:
    2.0x + (-6.0 * -3.0) = 22.0.
    Root x: x = -b / a = 4.0 / 2.0 = 2.0.
    (2.0, -3.0)

### Метод `quadratic` ###

Метод `quadratic` позваоляет решать квадратные уравнения.


Метод принимает коэффициенты `a`, `b` и `c` из формулы `a(x ** 2) + bx + c = 0`. У него тоже есть дополнитеьный параметр `solution`, который отвечает за вывод пошагового решения на консоль. По умолчанию он равен `False`. Метод возвращает `False` в случае неудачи(нет корней) или кортеж с 1 или 2 корнями уравнения.


Пример использования метода:

    from equation_maths_helper import quadratic
    equation_answer = quadratic(a=1, b=1, c=1, solution=True)
    print(equation_answer)


Вывод решения на консоль:


    Discriminant: (b ** 2) - 4 * a * c = (-5 ** 2) - 4 * 1 * 6 = 1.
    First root: x1 = (-b - sqrt(d)) / 2 * a = (5 - 1.0) / 2 * 1 = 2.0.
    Second root: x2 = (-b + sqrt(d)) / 2 * a = (5 + 1.0) / 2 * 1 = 3.0.
    Roots: 2.0, 3.0.
    (2.0, 3.0)
