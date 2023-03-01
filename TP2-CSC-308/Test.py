import datetime

from Client import Client
from Employe import Employe
from Intervention import Intervention
from Contrat import Contrat
from Grade import Grade


date_du_jour = datetime.datetime.now()

grade = Grade('001', 'Niveau 3', 12)

date_embauche = datetime.datetime(2015, 1, 17).date()

employe = Employe(1, 'SESSOU', grade,  date_embauche)

date_intervention = datetime.datetime(2015, 1, 17).date()

client = Client(1,"Koffi", "Boulevard du 8eme","05BP07","Lomé","18")

intervention = Intervention(1,  date_intervention, 5, 8.3, employe)

contrat = Contrat(1, date_embauche, client, 800.000)

contrat.setIntervention([intervention])

ecart = contrat.ecart()
