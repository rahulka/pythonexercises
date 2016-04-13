import math

square = lambda x: x*x

sqrtOfSumOfSquares = lambda x, y: math.sqrt(square(x) + square(y))

avg = lambda *args: sum(args)/len(args)

