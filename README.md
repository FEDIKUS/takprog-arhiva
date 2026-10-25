# Takprog Archive

Nezvanična arhiva zadataka i rešenja sa srpskih srednjoškolskih takmičenja iz informatike, uz materijale za takmičarsko programiranje. Sajt koristi Material for MkDocs, sa izgledom inspirisanim [Takprog sajtom](https://takprog.petlja.org/srednjaskola).

## Lokalni pregled

```sh
python3 -m venv .venv
source .venv/bin/activate
pip install mkdocs-material mkdocs-literate-nav
python3 scripts/nav_gen.py
mkdocs serve
```

Pre objavljivanja proverite izgradnju komandom `mkdocs build --strict`. Navigaciju i pregled sezona generiše `scripts/nav_gen.py` iz zadataka u `docs/takprog/`.

GitHub Actions objavljuje sajt na GitHub Pages pri izmeni grane `main` ili `master`. Domen nije unapred podešen; ako koristite sopstveni domen, podesite ga u GitHub Pages i dodajte odgovarajući `docs/CNAME`.

Ispravke i dopune predložite u [repozitorijumu](https://github.com/FEDIKUS/olympicode-site).

## Prednost izvora

Pri usaglašavanju sadržaja i zasluga, originalne Takprog arhive imaju prednost nad kopijama u Olympicode repozitorijumu: te arhive su izvor zvaničnih rešenja objavljenih na Algori. Pre usaglašavanja autora analize proverite da li je u pitanju ista analiza. Autor ideje zadatka, autor teksta i testova, autor analize i tester ostaju odvojene uloge.

## Poreklo arhive

Arhiva je nastala na osnovu [Olympicode arhive](https://github.com/olympicode/olympicode-site), koju su sakupili, organizovali i uredili Mladen Puzić, Aleksandar Višnjić i Bogdan Petrović.

Pojedinačne zasluge navedene su uz zadatke i materijale. Repozitorijum zadržava izvornu licencu [CC BY-SA 4.0](LICENSE).
