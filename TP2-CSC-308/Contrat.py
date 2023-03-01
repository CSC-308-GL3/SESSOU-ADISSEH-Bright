class Contrat:
    def __init__(self, numero, date, client, montantContrat):
        self._numero = numero
        self._date = date
        self._client = client
        self._montantContrat = montantContrat
        self._interventions = []
        self._nbIntervention = 0
    
    def montant(self):
        return self._montantContrat
    
    def setIntervention(self,interventions):
        self.interventions=interventions
    
    def ecart(self):
        coutTotal = 0
        for intervention in self.interventions:
            coutTotal += intervention.fraisKm(self._client.distance()) + intervention.fraisMo()
        return self.montantContrat - coutTotal





