Hotelliprojektia käytetään lähettämällä HTTP-pyyntöjä seuraaville apeille:

Järjestelmän käyttö vaatii käyttäjätunnuksen rekisteröinnin.
Käyttäjätunnus rekisteröidään käyttäen /users apia

/users
[POST]

Käyttäjätunnus luodaan lähettämällä käyttäjätiedot JSON-muodossa:

{
    "username": "käyttäjätunnus",
    "email": "spostiosoite",
    "password": "salasana"
}

users/<string:username>
[GET]

Käyttäjätiedot voi hakea käyttäjätunnuksen perusteella.
Huom: tunnistautuminen tapahtuu bearer tokenilla. Ilman tokenia tietoja voi hakea rajatusti.

/me
[GET]

Omat tietonsa voi tarkastaa get -pyynnöllä käyttäen omaa tokeniaan.


Käyttäjän tunnistamiseen vaadittavat JWT tokenit saa käyttämällä token apeja:

/token
[POST]

Rekisteröinnin jälkeen JWT token noudetaan HTTP POST requestilla. Oma spostiosoite sekä salasana lähetetään JSON-muodossa:

{
    "email": "spostiosoite",
    "password": "salasana"
}


/refresh
[POST]

JWT token on voimassa 15 min luonnista. Saadakseen uuden, voi voimassaolevan lähettää bearer token headerissa /refresh apille.
Näin uudelleenkirjautuminen ei ole välttämätöntä.

/revoke
[POST]

Lähettämällä tokenin bearer token headerissa /revokeen voi päättää istuntonsa.





/rooms
[GET] 
[POST]
[PUT]

GET hakee tietokannasta luodut huoneet.

POST hyväksyy JSON-muodossa tiedon huoneen vuoteiden määrästä:

{
    "roomSize": 4
}

PUT päivittää vuoteiden määrän JSONilla, kuten yllä.


/rooms/<int:room_id>
[GET]
[PUT]
[DELETE]

Hakee, päivittää tai jo luodun huoneen sen ID-numeron perusteella.


rooms/<int:room_id>/publish
[PUT]
[DELETE]

Luodut huoneet eivät näy muille käyttäjille ennen tietojen julkaisua.
PUT julkaisee, DELETE poistaa julkaisun.

rooms/<int:room_id>/free
[PUT]
[DELETE]

Huoneen varausstatusta voidaan muuttaa samoin kuin julkaisutietoa.


/reservations
[GET] 
[POST]
[PUT]

GET hakee tietokannasta luodut varaukset.

POST hyväksyy JSON-muodossa tehtävän varauksen tiedot:

{
    "title": "Huoneen 1 varaus",
    "date": "(päivämäärä)",
    "duration": "(varauksen pituus päivissä)"

}

PUT päivittää varauksen tiedot JSONilla, kuten yllä.


/reservations/<int:reservation_id>
[GET]
[PUT]
[DELETE]

Hakee, päivittää tai jo luodun varauksen sen ID-numeron perusteella.


reservations/<int:reservation_id>/publish
[PUT]
[DELETE]

Luodut varaukset eivät näy muille käyttäjille ennen tietojen julkaisua.
PUT julkaisee, DELETE poistaa julkaisun.

reservations/<int:reservation_id>/<int:room_id>/make
[PUT]
[DELETE]

PUT Liittää varauksen huoneeseen käyttäen huoneen id-numeroa.
DELETE vastaavasti poistaa tämän varauksen.




