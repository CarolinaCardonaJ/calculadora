from tkinter import ttk

from tkinter import *
#Logica de Sistemas
#Semestre 1 
#Doris Carolina Cardona Juárez
#0907-19-12584
class Desk:

    def __init__(self, window):

        # Initializations

       

        #ancho

        ancho = 800

       

        #alto

        alto = 600

       

        # asignamos la ventana a una variable de la clase llamada wind

        self.wind = window

 

        #le asignamos el ancho y el alto a la ventana con la propiedad geometry

        self.wind.geometry(str(ancho)+'x'+str(alto))

 

        #centramos el contenido

        self.wind.columnconfigure(0, weight=1)

        # creamos un contenedor

        frame = LabelFrame(self.wind, text = 'Examen Final')

        frame.grid(row = 0, column = 0, columnspan = 3, pady = 20)

       

        # creamos un etiqueta

        Label(frame, text = 'Primer numero: ').grid(row = 1, column = 0)

       

        #creamos un input donde ingresar valores

        self.var1 = Entry(frame)

        self.var1.focus()

        self.var1.grid(row = 1, column = 1)

        # creamos un etiqueta

        Label(frame, text = 'Segundo numero: ').grid(row = 2, column = 0)

       

        #creamos un input donde ingresar valores

        self.var2= Entry(frame)

        self.var2.focus()

        self.var2.grid(row = 2, column = 1)


        # creamos un etiqueta

        Label(frame, text = 'Tercer numero : ').grid(row = 3, column = 0)

        #creamos un input donde ingresar valores

        self.var3 = Entry(frame)

        self.var3.focus()

        self.var3.grid(row = 3, column = 1)



        #Primer boton para ejecutar  I,II,III

        Button(frame, text = 'Sumar', command = self.sumar).grid(row = 5, columnspan = 2, sticky = W + E)

         #Segundo boton para ejecutar I,II


        Button(frame, text = 'Restar', command = self.restar).grid(row = 6, columnspan = 2, sticky = W + E)

     
        #designamos un área para mensajes

        self.message = Label(text = '', fg = 'red')

        self.message.grid(row = 3, column = 0, columnspan = 2, sticky = W + E)

       

    # creamos una función para validar que los campos no esten en blanco

    def validation(self):

        return len(self.var1.get()) != 0 and len(self.var2.get()) != 0


    # esta es la función que ejecuta la primer boton

    def sumar(self):

        if self.validation():

            resultado = float( self.var1.get() ) + float( self.var2.get() )

            self.message['text'] = 'La suma de las 2 variables es: {}'.format(resultado)

        else:

            self.message['text'] = 'los campos son requeridos'
            
def restar(self):

        if self.validation():

            resultado = float( self.var1.get() ) - float( self.var2.get() )

            self.message['text'] = 'La resta de las 2 variables es: {}'.format(resultado)

        else:

            self.message['text'] = 'los campos son requeridos'


#validamos si estamos en la aplicación inicial

if __name__ == '__main__':

   

    #asignamos la propiedad de tkinter a la variable window

    window = Tk()

   

    #en la variable app guardamos la clase Desk y le enviamos como parametro la ventana

    app = Desk(window)

 

    #ejecutamos un mainloop para que se ejecute la ventana

    window.mainloop()