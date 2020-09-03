# TP2 INGENIEUR EN INGENERIE GEOTECHNIQUE

# Pourcentage initial
import sys

cam_pourcentage = 100

# Liste initiale

camliste = ["le pere", "bongo", "materialiser", "teechargement",
            'geotechnique', "geotechnicien", "genie", "civil",
            "ethnies", "la garde", "foret", "cam", "kam",
            "glissement", "nivellement", "denivele", "topometrie",
            "cheminement", "ingenieur", "ingenerie"]
# NIVEAU 1
print('LE PERE BONGO AS VRAIMENT FAIT POUR CE PAYS')
cam_pseudo = input('Entrez votre pseudo: ')
camtel = False

for element in camliste:
    if element in cam_pseudo.lower():
        camtel = True
    else:
        pass
if camtel:
    print("Les dieux sont avec vous")
else:
    print("Nous doutons de vos origines; comme l'erreur n'exclut pas la valeur, nous allons materialiser"
          " ca")
    cam_pourcentage -= 30

# NIVEAU 2
print("Ma memoire est en cours de telechargement")
cam_profession = input("Entrez votre profession: ")
# Initialisation
cpt = 0
for terme in cam_profession.lower().split():
    if terme in camliste:
        cpt += 1
if cpt >= 2:
    print("L'argent lave mais m'beng rend propre")
else:
    if camtel:
        print("Mon petit je dis et j'insiste les notes c'est bien"
              " mais les relations c'est encore mieux")
        cam_pourcentage -= 40
    else:
        print("Le pere ci ne dis pas la verité")
        sys.exit()

# NIVEAU 3
print("Le cameroun est un pays de foret, mon petit quand tu vois les pays coupé"
      " carreaux carreaux la, c'est les blanc qui ont fait ca")
cam_ethni = int(input("Entrez le nombre d'ethnie au cameroun"))
if cam_ethni >= 251:
    print("L'economie camerounaise est detenue par le cameroun")
else:
    print("Mon petit ne jamais baisser la garde")
cam_plat = int(input('Entrez le nombre de mets au cameroun: '))

if cam_plat > cam_ethni:
    print("Mon petit j'ai ensigné 11 matieres et 95H impayé")
if cam_plat < cam_ethni:
    print("Le pere ci n'a pas la verité")
    cam_pourcentage -= 20

print("Mon petit les toofan continuent de chanter?")

if cam_pourcentage > 70:
    print("Cimencam, tu rejoin la constelation du boss")
elif 50 <= cam_pourcentage <= 70:
    print("Tu ne connais pas la topometrie et le cheminement")
else:
    print("Mon petit, tu n'as pas les qualité requises pour etre le boss")
