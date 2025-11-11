import random

class Bottiglia:
    def __init__(self, contenuto: str, materiale: str):
        self.contenuto = contenuto
        self.materiale = materiale
        self.percentuale_contenuto = 100        
    
    
    def bevi(self):
        diminuzione = random.randint(1, 100)
        self.percentuale_contenuto -= diminuzione
        
        # la percentuale non scende sotto 0
        if self.percentuale_contenuto < 0:
            self.percentuale_contenuto = 0

    def controlla_contenuto(self) -> str:
        if self.percentuale_contenuto == 0:
            return f"La bottiglia di {self.contenuto} è vuota."
        else:
            return f"La bottiglia di {self.contenuto} è piena al {self.percentuale_contenuto}%."
        
    def riempi_bottiglia(self):
        self.percentuale_contenuto = 100

#test
b1 = Bottiglia("acqua", "plastica")
print(b1.controlla_contenuto())
b1.bevi() #random
print(b1.controlla_contenuto())
b1.riempi_bottiglia()   
print(b1.controlla_contenuto())

print("--------------------------------")

b2 = Bottiglia("vino", "vetro")
print(b2.controlla_contenuto())
b2.bevi() #random
print(b2.controlla_contenuto())
b2.riempi_bottiglia()
print(b2.controlla_contenuto())

