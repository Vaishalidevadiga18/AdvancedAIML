import sympy as sp

x = sp.symbols('x')
expr = sp.sin(x) + sp.cos(x)

print("Expression:", expr)
print("Derivative:", sp.diff(expr, x))
print("Integral:", sp.integrate(expr, x))
