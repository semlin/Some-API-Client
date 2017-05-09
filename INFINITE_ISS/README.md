# INFINITE_ISS

Pré requis : lib requests à installer avec pypi qui sert à communiquer avec l'API.

Instruction d'utilisation disponible uniquement sur Jessie.
Fonctionnement assuré sur Jessie et Stretch (même procédure).

### Debian

* apt update -y && apt upgrade -y && apt install python pip git -y
* pip install requests
* git clone https://github.com/semlin/Some-API-Client.git
* cd Some-API-Client/INFINITE_ISS && python infinite.py

### HOW ADD CITY

Tu peux te servir de ce lien pour chopper les coordonés GPS de ta ville.

* http://www.coordonneesgps.net/coordonnees-gps/

Tu as besoins d'extraire la latitude et la longitude et d'inclure les paramètres dans la ligne qui suis.

Rajoute aussi au début le nom de ta ville.

* "city":{"latit":"0.00","longit":"0.00"},

Tout ceci dans le fichier "someCity.json".
