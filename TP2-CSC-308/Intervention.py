
class Intervention:
    def __init__(self, numero, date, duree, tarifkm, technicien):
        self._numero = numero
        self._date = date
        self._duree = duree
        self._tarifkm = tarifkm
        self._technicien = technicien
    
    def affiche(self):
        print("numero :" + self._numero + " " + "date :" + self._date + " " + "durée :" + self._duree + " "
              + "frais kilomètre :" + self.fraisKm() + " " + "cout de main-d'oeuvre :" + self.fraisMo() + " "
              + "Technicien :", self.technicien.getNom())
    
    def fraisKm(self, dist):
        return self._tarifkm * dist
    
    def fraisMo(self):
        return self._duree * self._technicien.coutHoraire()
