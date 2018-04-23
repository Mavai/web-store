# Verkkokauppa

## [Osoite](http://mavai.pythonanywhere.com/store/?sort=-price&)

### Ominaisuudet:

1. Tuotehaku:

   Tuotteita voi hakea syöttämällä hakusanan hakukenttään. Tuotteita haetaan sekä nimen että tuotekoodin peruseella.

2. Tuotetiedot:

   Tuotteen tiedot pääsee näkemään klikkaamalla tuotteen linkkiä.

3. Ostoskori:

   Tuotteita voi lisätä koriin haluamansa määrän ilman sivun uudelleenlatausta. Navigointipalkin oikeassa ylälaidassa on linkki ostoskoriin ja täältä näkee myös ostoskorin tämänhetkisen arvon. Ostoskorissa on listattuna kaikki siellä olevat tuotteet, niiden lukumäärä ja hinta.

4. Tuotteen lisääminen:

   Ylläpito voi lisätä, poistaa ja muokata kaupan tuotteita navigointipalkin linkistä 'Manage products'. Tämä vaatii kirjautumisen tunnuksilla joilla on vaadittavat oikeudet. Tunnus: `admin` Salasana: `sekret123`.

5. Tuotteet:

   Tuotteilla on seuraavat kentät:
   - nimi
   - hinta
   - tuotekoodi
   - tuotekuvaus
   - kuva tuotteesta


### Asennusuhjeet paikallisesti:

1. `pip install -r requirements.txt`

2. Luo .env tiedosto kansioon `mystore`.

3. Lisää .env tiedostoon haluamasi arvot seuraaville muuttujille:\
 `SECRET_KEY`,\
 `DB_ENGINE`,\
 `DB_NAME`,\
 `DB_USER`,\
 `DB_PASSWORD`,\
 `DB_HOST`

4. `python manage.py runserver`

