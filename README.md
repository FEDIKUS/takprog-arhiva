# Takprog Archive

Nezvanična arhiva zadataka i rešenja sa srpskih srednjoškolskih takmičenja iz informatike.

## Pokretanje

```sh
docker network create web  # samo ako mreža ne postoji
docker compose up -d --build
```

Arhiva je dostupna na `http://localhost:8083/arhiva/`. Docker image gradi statički sajt i služi ga preko Nginx-a.

Za lokalni razvoj:

```sh
pip install -r requirements-archive.txt
mkdocs serve
```

## Izvori

Arhiva je nastala na osnovu [Olympicode arhive](https://github.com/olympicode/olympicode-site), koju su sakupili i uredili **Mladen Puzić**, Aleksandar Višnjić i Bogdan Petrović. Zadržana je izvorna [CC BY-SA 4.0 licenca](LICENSE). Pojedinačne zasluge navedene su uz zadatke.
