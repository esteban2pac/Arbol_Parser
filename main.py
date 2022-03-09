from tkinter import *
from tkinter import ttk
import xml.etree.ElementTree as ET


class parserXmlToPy(ttk.Frame):

    def __init__(self, main_window):

        super().__init__(main_window)
        main_window.title("Arbol XML")
        main_window.geometry("500x500")
        self.treeview = ttk.Treeview(self)
        self.tree = ET.parse('Cartelera_Cine.xml')
        self.raiz = self.tree.getroot()
        self.nodo_principal = self.treeview.insert("", END, None, text=self.raiz.tag)
        self.insert_treeview(self.raiz, parent=self.nodo_principal)
        self.treeview.pack(fill=BOTH, expand=True)
        self.pack(fill=BOTH, expand=True)

    def insert_treeview(self, raiz, parent=""):
        for child in raiz:
            node_name = child.tag
            item = self.treeview.insert(parent, END, None, text=node_name)
            if len(child) > 0:
                self.insert_treeview(child, parent=item)
            else:
                if (child.text != None):
                    self.treeview.insert(item, END, None, text=child.text)


root = Tk()
app = parserXmlToPy(root)
app.mainloop()