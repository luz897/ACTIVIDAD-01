import numpy as np
import matplotlib.pyplot as plt


def graficar(funcion, variable, min_val, max_val):
    try:
        x = np.linspace(min_val, max_val, 400)
        funcion_modificada = funcion.replace('^', '**')
        variables = {variable: x}
        y = eval(funcion_modificada, {}, variables)
        
        
        y_max = np.max(y)
        x_max = x[np.argmax(y)]
        
        y_min = np.min(y)
        x_min = x[np.argmin(y)]
        
        
        plt.plot(x, y, label=f'{funcion} con {variable}', color='blue')
        plt.title(f'f({variable}) = {funcion}')
        plt.xlabel(variable)
        plt.ylabel(f'f({variable})')
        
       
        plt.plot(x_max, y_max, 'ro')  
        plt.text(x_max, y_max, f'Max: ({x_max:.2f}, {y_max:.2f})', fontsize=12, ha='right', color='red')  
        
        
        plt.plot(x_min, y_min, 'go')  
        plt.text(x_min, y_min, f'Min: ({x_min:.2f}, {y_min:.2f})', fontsize=12, ha='right', color='green')  
        
        plt.legend()
        plt.grid(True)
        plt.show()

    except Exception as e:
        print(f"Ocurrio un error: {e}")

funcion = input("Ingrese la funcion f(x): ")
variable = input("Ingrese la variable: ")
min_val = float(input(f"Intervalo minimo para {variable}: "))
max_val = float(input(f"Intervalo maximo para {variable}: "))

graficar(funcion, variable, min_val, max_val)
