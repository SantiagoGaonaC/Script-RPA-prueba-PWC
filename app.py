import customtkinter
from matplotlib.pyplot import text
from script import leerCSV

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        #self.geometry("500x300")
        self.title("RPA - EMPRESA ABC")
        
        #Estilo de la ventana
        self.columnconfigure(0,weight=1)
        self.columnconfigure(1,weight=1)
        
        self.w_total = self.winfo_screenwidth()
        #buscar el W Y H de la pantalla
        self.h_total = self.winfo_screenheight()
        #establecer tamaño de la app como fijo
        self.w_ventana = 600 
        self.h_ventana = 400
        
        #calcular la posición
        self.p_width = round(self.w_total/2-self.w_ventana/2)
        self.p_height = round(self.h_total/2-self.h_ventana/2)
        #aplicamos geometría de la ventana
        self.geometry(str(self.w_ventana)+"x"+str(self.h_ventana)+"+"+str(self.p_width)+"+"+str(self.p_height))

        #--------Label principal
        self.text_var = customtkinter.StringVar(value="Selecciona el archivo CSV desde el botón")
        self.label = customtkinter.CTkLabel(self,
                               textvariable=self.text_var,
                               width=120,
                               height=25,
                               text_font=('',20)
                               )
        #self.label.pack(side="top",padx=40,pady=40)
        self.label.place(relx=0.5, rely=0.4, anchor=customtkinter.CENTER)
        #----------------

        #-------- Botón abrir CSV
        self.boton_abrir = customtkinter.CTkButton(self, text="Play / Abrir Archivo CSV", text_font=('',20),
                                                   command=leerCSV, width=20, height=9)
        #self.boton_abrir.grid(row=1,column=0,padx=20,pady=20)
        #self.boton_abrir.pack(side="top",padx=40,pady=40)
        self.boton_abrir.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)
        #---------

if __name__ == "__main__":
    app = App()
    app.mainloop()