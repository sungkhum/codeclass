def y():
    """ y does this function exist? 
          ** just to illustrate a function that takes no inputs...
              and always returns 1  - Morgan Conbere
    """
    return 1

def w(x):
    """ w computes thrice its input plus one
          ** plus it offers a chance to use the word "thrice" 
        input x: any number (int or float)
    """
    return 3*(x+1)

def t(x):
    """ t computes thrice its input plus one
          ** and shows how python is more precise than English
        input x: any number (int or float)
    """
    return 3*x + 1

def r(x,y):
    """ r shows some less-common arithmetic operators
        input x: any number (int or float)
        input y: any number (int or float, more likely int)
    """
    return ( x**2 % y ) + 2

def f(a,b):
    """ f demonstrates the use of conditionals (if/elif/else)
          ** and that input parameters' names don't matter
        input a: any number (int or float)
        input b: any number (int or float)
    """
    if a < b:
        return (b-1) * (b-2)
    else:
        return (a+42) * (b+42)

print(r(3,4))