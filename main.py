from tkinter import *
from tkinter import ttk
import xml.etree.ElementTree as ET

class parserXmlToPy(ttk.Frame):

    def __init__(self, main_window):

        super().__init__(main_window)
        main_window.title("Arbol XML")
        main_window.geometry("500x500")
        self.vistaArbol = ttk.Treeview(self)
        self.arbol = ET.parse('Cartelera_Cine.xml')
        self.raiz = self.arbol.getroot()
        self.nodo_principal = self.vistaArbol.insert("", END, None, text=self.raiz.tag)
        self.insertando_vistaArbol(self.raiz, parent=self.nodo_principal)
        self.vistaArbol.pack(fill=BOTH, expand=True)
        self.pack(fill=BOTH, expand=True)

    def insertando_vistaArbol(self, raiz, parent=""):
        for child in raiz:
            node_name = child.tag
            item = self.vistaArbol.insert(parent, END, None, text=node_name)
            if len(child) > 0:
                self.insertando_vistaArbol(child, parent=item)
            else:
                if (child.text != None):
                    self.vistaArbol.insert(item, END, None, text=child.text)


root = Tk()
app = parserXmlToPy(root)
app.mainloop()