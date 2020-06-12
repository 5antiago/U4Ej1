import tkinter as tk
from tkinter import ttk, font, messagebox
from functools import partial
class App(tk.Tk):
    
    def __init__(self):
        super().__init__()
        self.title("Calculador IMC")
        self.geometry("310x250")
        self.config(padx=10, pady=20)
        self.resizable(0,0)
        self.__altura=tk.DoubleVar()
        self.__peso= tk.DoubleVar()
        self.__imc= tk.StringVar()
        self.__imcstatus= tk.StringVar()

        #Creando los elementos
        self.__titulo=ttk.Label(self, text="Calculadora de  IMC", font= font.Font(weight="bold"))
        self.__lbalt= ttk.Label(self, text="Altura (M): ", padding=(5,5))
        self.__lbpes= ttk.Label(self, text="Peso (KG): ", padding=(5,5))
        self.__separator=ttk.Separator(self, orient=tk.HORIZONTAL)
        self.__epes = ttk.Entry(self, textvariable=self.__peso)
        self.__ealt= ttk.Entry(self, textvariable=self.__altura)
        self.__lbimc=ttk.Label(self, textvariable=self.__imc)
        self.__lblstat=ttk.Label(self, textvariable=self.__imcstatus)
        self.__btncalc= ttk.Button(self, text="Calcular", command= lambda : self.Calcular(float(self.__epes.get()), float(self.__ealt.get())))
        self.__btnclean= ttk.Button(self, text="Limpiar", command=self.clean)

        #Ubicando los elementos
        self.__titulo.place(anchor=tk.CENTER, relwidth = 0.6, relheight=0.1, relx=0.5)
        self.__lbalt.place(anchor= tk.W, relwidth=0.23, relheight=0.15, relx=0.1, rely=0.15)
        self.__lbpes.place(anchor= tk.W, relwidth=0.23, relheight=0.15, relx=0.1, rely=0.41)
        self.__ealt.place(anchor= tk.W, relwidth=0.5, relheight=0.1, relx=0.34, rely=0.15)
        self.__epes.place(anchor= tk.W, relwidth=0.5, relheight=0.1, relx=0.34, rely=0.41)
        self.__separator.place(anchor = tk.W, relwidth=1, relheight=0.01, rely= 0.55)
        self.__btncalc.place(anchor=tk.CENTER, relwidth=0.3, relheight=0.15, rely= 0.7, relx=0.35)
        self.__btnclean.place(anchor=tk.CENTER, relwidth=0.3, relheight=0.15, rely=0.7, relx=0.7)
        self.__lbimc.place(anchor= tk.CENTER, relwidth= 0.9, relheight=0.2, rely= 0.9, relx=0.5)
        self.__lblstat.place(anchor= tk.CENTER, relwidth= 0.6, relheight=0.091, rely=0.99, relx=0.5)

        self.__ealt.focus()
    
    def Calcular(self, peso, altura):
        try:
            imc = peso/(altura**2)
        except ZeroDivisionError:
            messagebox.showerror(title="Error", message="Datos incorrectos")
        else:
            self.__imc.set("Su IMC (Indice de masa corporal) es: {:.2f}".format(imc))
            if imc<18.5:
                self.__imcstatus.set("Peso Inferior al Normal")
            elif imc<24.9:
                self.__imcstatus.set("Peso Normal")
            elif imc<29.9:
                self.__imcstatus.set("Peso Superior al Normal")
            else:
                self.__imcstatus.set("Obesidad")


    def clean(self):
        self.__peso.set(0.0)
        self.__altura.set(0.0)
        self.__imc.set("")
        self.__imcstatus.set("")