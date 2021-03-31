from tkinter import *
# opens the file and reads 1st line and assigns that value to "guardado1"..
ler = open("texto.txt", "r")
guardado1 = ler.readline()
guardado2 = ler.readline()
ler.close()

print (guardado1 + guardado2)
#this command is associated with a button, and it assigns 2 variables to the user input and writes/saves it on the text file
def actualizar():
    variavel1 = e1.get()
    variavel2 = e2.get()
    print("First Name: %s\nLast Name: %s" % (variavel1, variavel2))
    escrever = open("texto.txt", "w+")
    escrever.write(variavel1)
    escrever.write(variavel2)
    escrever.close()


#this creates the window that pops up, it writes the saved values in the respective input boxes, if there is none saved it will be a blank
master = Tk()
Label(master, text="valor1").grid(row=0)
Label(master, text="valor2").grid(row=1)
e1 = Entry(master)
e2 = Entry(master)
e1.insert(10, guardado1)
e2.insert(10, guardado2)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
Button(master, text='Sair', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
Button(master, text='Actualizar', command=actualizar).grid(row=3, column=1, sticky=W, pady=4)