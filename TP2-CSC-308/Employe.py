from datetime import datetime

class Employe:
    def __init__(self, numero, nom, qualification, dateEmbauche):
        self._numero = numero
        self._nom = nom
        self._qualification = qualification
        self._dateEmbauche = dateEmbauche
    
    def coutHoraire(self):
        anciennete = self.getAnciennete(self._dateEmbauche)
        if anciennete < 5:
            coeff = 1.0
        elif anciennete < 11:
            coeff = 1.05
        elif anciennete < 16:
            coeff = 1.08
        else:
            coeff = 1.12
        return self.qualification.tauxHoraire() * coeff
    
    def getNumero(self):
        return self._numero
    
    def getNom(self):
        return self._nom
    
    def getQualification(self):
        return self._qualification
    
    def getDateEmbauche(self):
        return self._dateEmbauche
    
    def getAnciennete(self, date):
        date_format = '%Y-%m-%d'
        date_fournie = datetime.strptime(date, date_format).date()
        date_du_jour = datetime.now().date()
        anciennete =  date_du_jour -  date_fournie
        return anciennete
