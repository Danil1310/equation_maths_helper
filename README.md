# equation_maths_helper #

# ENG #

A module that allows you to solve quadratic and linear equations.

## How to use? ##

### Importing ###

First, import the equation_maths_helper module.


    import equation_maths_helper

For convenience, we recommend importing all necessary methods from the module at once.


    from equation_maths_helper import linear_one_variable, quadratic
    
### The `linear_one_variable` method ###

The `linear_one_variable` method allows you to solve linear equations with a single variable.


 The method accepts the coefficients `a` and `b` from the formula `ax + b = 0`. It also has an additional `solution` parameter, which is responsible for outputting a step-by-step solution to the console. By default it is set to `False`. The method returns `False` if it fails (there are no roots), the root of the equation, or `True` if the root is any number.


Example of using the method:

    from equation_maths_helper import linear_one_variable
    equation_answer = linear_one_variable(a=1, b=1, solution=True)
    print(equation_answer)


Output the solution to the console:

    Root: x = -b / a = x = 1 / 1 = 1.0.
    1.0
### The `quadratic` method ###

The `quadratic` method allows you to solve quadratic equations.


The method accepts the coefficients `a`, `b`, and `c` from the formula `a(x ** 2) + bx + c = 0`. It also has an additional parameter `solution`, which is responsible for displaying the step-by-step solution on the console. By default, it is set to `False`. The method returns `False` if it fails (no roots) or a tuple with 1 or 2 roots of the equation.


An example of using the method:

    from equation_maths_helper import quadratic
    equation_answer = quadratic(a=1, b=1, c=1, solution=True)
    print(equation_answer)


Output of the solution to the console:

    Discriminant: (b ** 2) - 4 * a * c = (-5 ** 2) - 4 * 1 * 6 = 1.
    First root: x1 = (-b - sqrt(d)) / 2 * a = (5 - 1.0) / 2 * 1 = 2.0.
    Second root: x2 = (-b + sqrt(d)) / 2 * a = (5 + 1.0) / 2 * 1 = 3.0.
    Roots: 2.0, 3.0.
    (2.0, 3.0)
 
# RU #

Модуль, позволяющий решать квадратные и линейные уравнения.

## Как использовать? ##

### Импорт ###

Первым делом импортируйте модуль equation_maths_helper.


    import equation_maths_helper

Для удобства рекомендуем сразу импортировать все необходимые методы из модуля.


    from equation_maths_helper import linear_one_variable, quadratic

### Метод `linear_one_variable` ###

Метод `linear_one_variable` позволяет решать линейные уравнения с одной переменной.


Метод принимает коэффициенты `a` и `b` из формулы `ax + b = 0`. Также у него есть дополнитеьный параметр `solution`, который отвечает за вывод пошагового решения на консоль. По умолчанию он равен `False`. Метод возвращает `False` в случае неудачи(нет корней), корень уравнения или `True`, если корень любое число.


Пример использования метода:

    from equation_maths_helper import linear_one_variable
    equation_answer = linear_one_variable(a=1, b=1, solution=True)
    print(equation_answer)


Вывод решения на консоль:

    Root:  x = -b / a = x = 1 / 1 = 1.0.
    1.0

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
