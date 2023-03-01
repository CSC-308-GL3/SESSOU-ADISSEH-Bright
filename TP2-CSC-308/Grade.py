class Grade:
    def __init__(self, code, libelle, taux):
        self._code = code
        self._libelle = libelle
        self._taux = taux
    
    def getCode(self):
        return self._code
    
    def getLibelle(self):
        return self._libelle
    
    def tauxHoraire(self):
        return self._taux
