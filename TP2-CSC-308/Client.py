class Client:
    def __init__(self, numero, nom, adresse, codePostale, ville, nbKm):
        self._numero = numero
        self._nom = nom
        self._adresse = adresse
        self._codePostale = codePostale
        self._ville = ville
        self._nbKm = nbKm
    
    def distance(self):
         return self._nbKm
