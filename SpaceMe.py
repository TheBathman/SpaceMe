import tkinter


class Igra():

	def __init__ (self):
		#za začetek bo igra na plošči 6x6
		#S (Size) bo vrednost, ki jo bo igralec imel možnost nastaviti v menuju z drsnikom
		#zaenkrat bo S fiksno določen
		S=6
		self.plosca = [[None for y in range(S)] for x in range(S)]
		self.zgodovina = []


	def veljavne_poteze(self):
		#preveri vse veljavne poteze, če jih za enega igralca ne več, konča igro
	def naredi_potezo(self, i, j):
		#sprovede potezo igralca, ki je na vrsti
	def trenutno_stanje(self):
		#preveri trenutno stanje in posodobi števec zasedenosti
	def shrani_pozicijo(self):
		#shrani spremembo, da se lahko vračamo po potezah

class Clovek_rdeci():
	
	def __init__(self):

	def igraj(self):
		#Na potezi čakamo na gui
		pass
	def klik(self, i, j):
		#naredimo potezo
		self.gui.naredi_potezo(i, j)

class Clovek_modri():
	
	def __init__(self):

	def igraj(self):
		#Na potezi čakamo na gui
		pass
	def klik(self, i, j):
		#naredimo potezo
		self.gui.naredi_potezo(i, j)

class Gui():

	def __init__(self,master):

	def resetiraj_igro(self, rdeci, modri):
		#ponastavi igro na začetek
	
	def pobarvaj_rdece(self, i, j):
		#pobarva i j polje rdeče
	def pobarvaj_modro(self, i, j):
		#pobarvaj i j polje modro

	def konec(self, zmagovalec):
		#napiše kdo je zmagal

	def klik(self, event):
		#tistemu, ki je na potezi podamo koordinate klika

	def naredi_potezo(self, i, j):
		#naredi potezo, če je sploh veljavna

	def quit():
		#zapre aplikacijo
		root.quit()

#manjka še on top "menu" okno
if __name__ == "__main__":
	root = tkinter.Tk()
	root.title("SpaceMe")
	#manjkajo stavri, za katere ne vem kaj bodo počele

	root.mainloop()
