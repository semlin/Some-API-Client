# INFINITE_ISS

Petit soft dev en vitesse pour me familiariser avec les API.

Pas de pré requis spécial à part la lib requests qui sert à communiquer avec l'API.

Par défaut la ville ciblée est PARIS mais vous pouvez la changer en modifiant les coordonnées de PARIS par celle de votre ville.
Vous pouvez aussi changer Paris par le nom de votre ville mais pensez à le faire à chaque fois que paris apparais dans le programme.

### Debian

* apt update -y && apt upgrade -y && apt install python pip -y
* pip install requests

### HOW ADD CITY

Tu peux te service de ce liens pour chopper les coordoné GPS de ta ville.
http://www.coordonneesgps.net/coordonnees-gps/

Tu as besoins d'extraire la latitude et la longitude et d'inclure les paramètres dans la ligne qui suis.
Rajoute aussi au début le nom de ta ville.
* "city":{"latit":"0.00","longit":"0.00"},
Ensuite tu peux rajouter cette ligne (partout sauf à la dernière ligne) dans le fichier "someCity.json".
