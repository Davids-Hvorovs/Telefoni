

class Telefons:

    def __init__(self, tips, modelis,marka, razosanas_gads,cena):

        self.tips = tips
        self.modelis = modelis
        self.marka = marka
        self.razosanas_gads = razosanas_gads
        self.cena = cena

    def info(self):
        print(f"{self.modelis}  {self.marka}")
    def mainitCenu(self, jaunaCena):
        print(f"{self.modelis} {self.marka} tika mainīta cena uz {jaunaCena}Eiro")
        self.cena = jaunaCena

