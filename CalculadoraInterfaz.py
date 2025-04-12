# ====== IMPORTACIONES ======
# Importamos tkinter para crear la interfaz gráfica
import tkinter as tk
# Importamos messagebox para mostrar mensajes de error
from tkinter import messagebox
# Importamos Path para manejar rutas de archivos
from pathlib import Path

# ====== CONFIGURACIÓN DE LA VENTANA PRINCIPAL ======
# Creamos la ventana principal
ventana = tk.Tk()
# Establecemos el título de la ventana
ventana.title("Calculadora")
# Definimos el tamaño inicial de la ventana
ventana.geometry("250x300") 
ventana.configure(bg="#000000")  # Fondo negro
# Deshabilitamos el redimensionamiento de la ventana
ventana.resizable(False, False)
# Obtenemos la ruta del icono relativa al archivo actual
icono_path = Path(__file__).parent / "icono.ico"
# Forma básica de colocar un icono:
# ventana.iconbitmap('ruta/al/archivo.ico')
# Sin embargo, es mejor usar Path para manejar rutas relativas
# Establecemos el icono de la ventana
ventana.iconbitmap(icono_path)

# ====== CONFIGURACIÓN DE LA PANTALLA ======
# StringVar es una clase especial de tkinter que permite crear variables
# que se actualizan automáticamente en la interfaz gráfica cuando cambian
# Cuando el valor de texto_pantalla cambie, la pantalla se actualizará sola
texto_pantalla = tk.StringVar()
# Establecemos el valor inicial de la variable como "0"
# Este valor se mostrará en la pantalla al iniciar la calculadora
texto_pantalla.set("0")

# Crear la pantalla
pantalla = tk.Entry(
    ventana,
    textvariable=texto_pantalla,    # Variable que controla el texto mostrado
    font=('Arial', 20),             # Tipo y tamaño de fuente
    justify="right",                # Alineación del texto a la derecha
    state="readonly",               # Estado de solo lectura
    width=15,                       # Ancho del campo
    bg="#000000",  # Fondo negro
    fg="black"  # Texto negro
)
# Empaquetamos la pantalla con padding horizontal y vertical
pantalla.pack(padx=10, pady=10)

# ====== FUNCIONES ======
# Función para manejar clicks en botones
def click_boton(valor):
    # Obtenemos el valor actual en la pantalla
    actual = texto_pantalla.get()
    
    if valor == "C":
        # Si presionamos C, reiniciamos la pantalla a "0"
        texto_pantalla.set("0")
    elif valor == "=":
        try:
            # Evaluamos la expresión matemática
            resultado = eval(actual)
            # Mostramos el resultado
            texto_pantalla.set(str(resultado))
        except:
            # Si hay un error, mostramos mensaje y reiniciamos
            messagebox.showerror("Error", "Operación inválida")
            texto_pantalla.set("0")
    else:
        # Para cualquier otro botón
        if actual == "0":
            # Si la pantalla muestra "0", reemplazamos con el nuevo valor
            texto_pantalla.set(valor)
        else:
            # Si no, concatenamos el nuevo valor
            texto_pantalla.set(actual + valor)

# ====== CONFIGURACIÓN DE BOTONES ======
# Marco para los botones
marco_botones = tk.Frame(ventana, bg="#000000")  # Fondo negro
# Empaquetamos el marco con padding
marco_botones.pack(padx=10, pady=10)

# Lista de botones organizados en forma de matriz 4x4
botones = [
    '7', '8', '9', '+',
    '4', '5', '6', '-',
    '1', '2', '3', '*',
    'C', '0', '=', '/'
]

# ====== CREACIÓN Y POSICIONAMIENTO DE BOTONES ======
# Inicializamos las variables para la posición de los botones en la cuadrícula
fila = 0  # Controla la fila actual
columna = 0  # Controla la columna actual

# Iteramos sobre cada botón en la lista de botones
for boton in botones:
    # Creamos una función lambda que captura el valor actual del botón
    # Lambda es una función anónima que nos permite crear una función simple en una línea
    # x=boton crea una copia del valor actual de botón para cada iteración
    # Sin esto, todos los botones usarían el último valor de 'boton'
    comando = lambda x=boton: click_boton(x)
    
    # Definimos los colores según el tipo de botón
    if boton in ['=', '+', '-', '*', '/', 'C']:
        color = "#0066cc"  # Azul para operadores
        fg_color = "white"  # Color del texto en blanco
    else:
        color = "#333333"  # Gris oscuro para números
        fg_color = "white"  # Color del texto en blanco
        
    # Creamos el botón con sus propiedades
    btn = tk.Button(
        marco_botones,  # El contenedor padre
        text=boton,     # El texto que mostrará el botón
        width=5,        # Ancho del botón
        height=2,       # Alto del botón
        font=('Arial', 12),  # Fuente y tamaño
        bg=color,       # Color de fondo
        fg=fg_color,    # Color del texto
        command=comando # Función que se ejecuta al hacer clic
    )
    # Posicionamos el botón en la cuadrícula usando grid
    btn.grid(row=fila, column=columna, padx=2, pady=2)
    
    # Actualizamos la posición para el siguiente botón
    columna += 1
    # Si llegamos al final de la fila (4 columnas)
    if columna > 3:
        columna = 0  # Volvemos a la primera columna
        fila += 1    # Avanzamos a la siguiente fila

# ====== INICIAR APLICACIÓN ======
ventana.mainloop()  # Inicia el bucle principal de la aplicación que mantiene la ventana abierta
