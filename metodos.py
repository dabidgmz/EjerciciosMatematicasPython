from sympy import diff, symbols, sympify, lambdify
from tkinter import messagebox

class Metodos:
    @staticmethod
    def euler_mejorado(x0, y0, h, xf, fxy):
        f = lambdify(['x', 'y'], sympify(fxy)) 
        xn = x0
        yn = y0
        resultado = []

        while xn < xf:
            yn1_est = yn + h * f(xn, yn) 
            xn1 = xn + h
            yn1 = yn + (h / 2) * (f(xn, yn) + f(xn1, yn1_est)) 
        
            resultado.append({
                "n": len(resultado),
                "Xn": xn,
                "Yn": yn,
                "(Yn+1)*": yn1_est,
                "Xn+1": xn1,
                "Yn+1": yn1
            })

            xn = xn1
            yn = yn1

        return resultado
    
    @staticmethod
    def runge_kutta(x0,y0,h,xf,fxy):
        f = lambdify(['x', 'y'], sympify(fxy))
        xn=x0
        yn=y0
        resultado =[]

        while xn < xf:
            k1=f(xn,yn)
            k2=f(xn+h/2,yn+(h*k1)/2)
            k3=f(xn+h/2,yn+(h*k2)/2)
            k4=f(xn+h,yn+h*k3)

            yn1= yn+(h/6)*(k1+2*k2+2*k3+k4)
            xn1=xn+h
            resultado.append({
                "n":len(resultado),
                "Xn":xn,
                "Yn":yn,
                "K1":k1,
                "K2":k2,
                "K3":k3,
                "K4":k4,
                "Yn+1":yn1
            })
            xn=xn1
            yn=yn1

        return resultado

            