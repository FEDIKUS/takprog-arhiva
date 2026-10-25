---
hide:
  - toc
---

# 3 - Majnkraft Koofa

=== "Zadatak"

	| Vremensko ograničenje | Memorijsko ograničenje |
	|:-:|:-:|
	| 1000ms | 64MB |

	**Ovo je zadatak sa poznatim ulazom**. Više informacija se nalazi u samom tekstu.

	*U svakom zadatku uvek ima neka caka.*

	Ovaj zadatak nije izuzetak. Caka je upravo (u Majnkraftu) naišla na ruševinu koja je poplavljena vodom. Sada je potrebno da se ruševina renovira, a prvi korak u renovaciji je da se ukloni sva voda.

	Ruševina se sastoji od tačno $10$ prostorija. Caka će da uklanja vodu iz prostorija jednu po jednu. Odnosno, svaka prostorija je predstavljena jednim test primerom.

	Prostorija se može predstaviti kao $N \times M$ matrica u kojoj postoje tri tipa polja: zidovi, poplavljena polja i prazna polja. Na početku je svako polje ili zid ili poplavljeno polje. Cilj je pretvoriti sva poplavljena polja u prazna.

	Kako bi postigla svoj cilj, Caka će prvo da pozove još $K-1$ drugarica da joj pomognu. Sve devojke će uzeti po praznu kofu i koristiće ukupno $K$ kofa da bi uklonile vodu (ipak se ovo dešava u Majnkraftu).

	Uklanjanje vode iz ruševine vršiće u više koraka. U svakom koraku rade sledeće:

	- Izaberu najviše $K$ polja koja su trenutno poplavljena.
	- Pomoću kofa istovremeno sklone vodu sa izabranih polja. Time ta polja postaju prazna.

	Ali voda se u Majnkraftu ponaša na čudne načine. Za dva polja kažemo da su susedna ako imaju zajedničku stranicu (polje ima najviše 4 suseda). Nakon što se skloni voda iz nekog polja, dešava se sledeće:

	- Ako postoji neko polje koje je prazno, ali ima bar dva susedna polja koja su poplavljena, i to polje postaje poplavljeno.
	- Prethodno pravilo se primenjuje sve dok postoje takva polja.

	**Napomena:** Polja koja su zidovi ne smatraju se poplavljenim. Ona ostaju zidovi tokom celog procesa.

	Vaš zadatak je da odredite za Caku broj $K$, kao i niz koraka kojima može da postigne svoj cilj. Pošto Caka ne želi da dosađuje drugaricama, njena želja je da broj $K$ bude što manji.

	## Napomena

	Ovo je zadatak sa poznatim ulazom (_output-only_ zadatak). Vama su dati ulazni fajlovi (`1.in`, `2.in`, `3.in`, `4.in`, `5.in`, `6.in`, `7.in`, `8.in`, `9.in`, `10.in`), dok vi treba da pošaljete samo odgovarajuće izlazne fajlove za njih (`1.out`, `2.out`, `3.out`, `4.out`, `5.out`, `6.out`, `7.out`, `8.out`, `9.out`, `10.out`). Takođe vam je data slika kako izgleda svaki ulazni fajl (`01.bmp`, `02.bmp`, `03.bmp`, `04.bmp`, `05.bmp`, `06.bmp`, `07.bmp`, `08.bmp`, `09.bmp`, `10.bmp`). Beli pikseli predstavljaju poplavljena polja, a crni polja koja su zidovi.

	Obratite pažnju da sve fajlove morate poslati u jednom slanju. To znači da prvo treba da učitate sve izlaze koje želite da pošaljete, pa tek onda da kliknete na dugme „Pošalji”.

	Primer čitanja iz fajlova i pisanja u fajl možete videti u fajlu `main.cpp`, koji se nalazi u materijalima. On čita ulaz iz fajla `00.in` i upisuje izlaz programa u fajl `00.out`. Fajl `00.in` je primer iz teksta zadatka, on se ne boduje i ne treba da ga šaljete na Petlju.

	Pomenute materijale možete preuzeti na dnu stranice.

	## Opis ulaza

	U prvoj liniji standardnog ulaza nalaze se dva cela broja $N$ i $M$ — dimenzije matrice. Zatim je u svakom od narednih $N$ redova data niska dužine $M$ u kojoj stoji karakter `0` ako je polje poplavljeno, a u suprotnom, ako je polje zid, stoji karakter `1`.

	## Opis izlaza

	U prvoj liniji standardnog izlaza treba ispisati broj $K$ iz teksta zadatka.

	U sledećoj liniji nalazi se broj $Q$, broj koraka koje će Caka i njene drugarice da odrade.

	Nakon toga sledi $Q$ blokova, od kojih svaki opisuje jedan korak.

	Prva linija $i$-tog bloka sadrži broj $l_i$ ($1 \le l_i \le K$), broj polja iz kojih se sklanja voda u $i$-tom koraku.

	$j$-ta od sledećih $l_i$ linija sadrži dva broja $x_{i,j}$ i $y_{i,j}$. Oni označavaju da se sa polja u $x_{i,j}$-tom redu i $y_{i,j}$-toj koloni sklanja voda u $i$-tom koraku. Koordinate su indeksirane od $1$.

	**Napomena**: Zbir svih vrednosti $l_i$ u jednom izlazu ne sme da prelazi $N \cdot M$. Garantujemo da postoji optimalno rešenje koje ne prekoračuje ovu granicu.

	## Kompresija izlaza

	Pošto bi izlaz u opisanom formatu bio prevelik, potrebno je da ga kompresujete pre slanja na Petlju. Kako biste kompresovali izlaz, u materijalima vam je dat fajl `compressor.cpp`. Potrebno je da kompilirate dati fajl i pokrenete ga u istom folderu u kom se nalazi fajl sa izlaznim podacima koji želite da pošaljete na Petlju. Nakon toga, na standardni ulaz treba upisati puno ime fajla koji želite da kompresujete, uključujući i njegovu ekstenziju. Tada će biti napravljen kompresovani fajl, koji treba da pošaljete na Petlju.

	U materijalima vam je takođe dat fajl `00.out_compressed.txt`, koji predstavlja kompresovani izlaz `00.out`.

	Ukoliko pošaljete nekompresovani fajl na Petlju, rešenje će biti ocenjeno sa $0$ poena. Fajl `compressor.cpp` radi neke provere izlaza kako bi mogao da ga kompresuje, ali to što se izlazni fajl uspešno kompresuje ne znači da je tačan.

	Dozvoljeno vam je da čitate, kopirate kod i menjate fajl `compressor.cpp` po želji, ali budite pažljivi da ne promenite format kompresije. Ukoliko izlaz nije dobro kompresovan, biće ocenjen sa $0$ poena.

	## Primer

	### Ulaz

	```
	3 5
	11101
	00000
	11101
	```

	### Izlaz

	```
	3
	5
	2
	2 4
	2 5
	2
	2 3
	2 4
	1
	2 1
	3
	2 3
	2 4
	3 4
	2
	2 2
	1 4
	```

	### Objašnjenje

	Prostorija je dimenzije $3 \times 5$. Na početku su polja ($1$,$4$), ($2$,$1$), ($2$,$2$), ($2$,$3$), ($2$,$4$), ($2$,$5$) i ($3$,$4$) poplavljena, dok su ostala polja zidovi. Caka poziva još dve drugarice da joj pomognu (znači ukupno ih je $K = 3$), a vodu će ukloniti u $5$ koraka.

	U prvom koraku sklanjaju vodu iz polja ($2$,$4$) i ($2$,$5$). Kako su polja ($2$,$3$) i ($3$,$4$) poplavljena polja susedna polju ($2$,$4$), polje ($2$,$4$) ponovo postaje poplavljeno. Polje ($2$,$5$) ostaje prazno pošto ima samo jedno susedno poplavljeno polje. Trenutno poplavljena polja su ($1$,$4$), ($2$,$1$), ($2$,$2$), ($2$,$3$), ($2$,$4$) i ($3$,$4$).

	U drugom koraku sklanjaju vodu iz polja ($2$,$3$) i ($2$,$4$). Kako su polja ($1$,$4$) i ($3$,$4$) poplavljena polja susedna polju ($2$,$4$), polje ($2$,$4$) ponovo postaje poplavljeno. Kako su polja ($2$,$2$) i ($2$,$4$) poplavljena polja susedna polju ($2$,$3$), polje ($2$,$3$) takođe ponovo postaje poplavljeno. Trenutno poplavljena polja su ($1$,$4$), ($2$,$1$), ($2$,$2$), ($2$,$3$), ($2$,$4$) i ($3$,$4$).

	U trećem koraku sklanjaju vodu iz polja ($2$,$1$). Kako polje ($2$,$1$) ima samo jedno susedno poplavljeno polje, ono ostaje prazno polje. Trenutno poplavljena polja su ($1$,$4$), ($2$,$2$), ($2$,$3$), ($2$,$4$) i ($3$,$4$).

	U četvrtom koraku sklanjaju vodu iz polja ($2$,$3$), ($2$,$4$) i ($3$,$4$). Polje ($3$,$4$) nema nijedno susedno poplavljeno polje, dok polja ($2$,$3$) i ($2$,$4$) imaju jedno susedno poplavljeno polje. Zato sva tri polja ostaju prazna. Trenutno poplavljena polja su ($1$,$4$) i ($2$,$2$).

	U petom koraku sklanjaju vodu iz polja ($1$,$4$) i ($2$,$2$). Nakon ovog koraka su sva polja prazna, pa je sva voda uspešno uklonjena ovim nizom operacija.

	**Napomena**: Ovaj primer služi samo da bi se bolje objasnio zadatak. On se ne boduje i prikazano rešenje nije optimalno.

	## Bodovanje

	Ovo je zadatak sa poznatim ulazom. Postoji $10$ primera (ulaznih fajlova), i svaki treba posebno da rešite.

	Svaki primer nosi najviše $10$ poena. Neka je $K_{min}$ najmanja vrednost broja $K$ sa kojim je komisija uspela da reši primer. Ako je vrednost broja $K$ jednaka $K_{takmicar}$, broj bodova koji za taj primer osvajate je

	$$\text{min}(1 + \lfloor \frac{K_{min}}{K_{takmicar}} \cdot 9 \rfloor, 10).$$

	## Pregled test primera

	Test primere i ostale materijale za zadatak možete preuzeti na dnu stranice. Sledeća tabela sadrži osnovne informacije o svakom od test primera.

	| **Primer** | $N$ | $M$ | $$K_{min}$$ |
	|---|---:|---:|---:|
	| 1  | 9    | 47   | 2  |
	| 2  | 25   | 25   | 3  |
	| 3  | 100  | 100  | 2  |
	| 4  | 100  | 100  | 9  |
	| 5  | 200  | 200  | 20 |
	| 6  | 300  | 300  | 25 |
	| 7  | 1000 | 1000 | 17 |
	| 8  | 1000 | 997  | 14 |
	| 9  | 1000 | 1000 | 10 |
	| 10 | 1000 | 1000 | 32 |

	> Zadatak sa poznatim ulazom; predaju se izlazni fajlovi.

	[Test primeri i prateći fajlovi sa zvaničnog takmičenja](https://nyc3.digitaloceanspaces.com/takprog/2025-26/2025-2026-sio-problems.zip).

=== "Rešenje"

	| Autor | Tekst i test primeri | Analiza rešenja | Testiranje |
	|:-:|:-:|:-:|:-:|
	| Nemanja Majski | Nemanja Majski | Toni Škrijelj | Toni Škrijelj i Uroš Kostadinović |

	## Uvod

	Ovo je **output-only** zadatak: ne postoje klasični podzadaci koje rešavamo jednim programom, već za 10 poznatih ulaza treba napraviti 10 izlaza.

	Cilj je minimizovati parametar $K$ (maksimalan broj polja koje brišemo u jednom koraku).

	## Ključna opservacija

	Ako u jednom koraku obrišemo neki skup poplavljenih polja $S$, neka polja iz $S$ mogu ponovo da se poplave (imaju bar dva susedna poplavljena polja), a neka ostaju prazna.

	Ako nakon simulacije zadržimo samo polja koja su **zaista ostala prazna**, dobijamo „efektivan“ skup operacije. Zato u praksi svaku kandidat-operaciju vrednujemo simulacijom.

	## Pristup 1: Obriši svu vodu

	Najjednostavnije:
	- $K =$ broj svih poplavljenih polja,
	- jedan korak koji sadrži sva poplavljena polja.

	Ovo je korektno i daje početne poene, ali je $K$ veliki.

	## Pristup 2: Obriši komponentu po komponentu

	Umesto svega odjednom:
	- nađemo povezane komponente poplavljenih polja,
	- obrišemo jednu po jednu.

	Ovim se $K$ spušta na veličinu najveće komponente, što je obično bolje od pristupa 1.

	## Pristup 3: Prvi red

	Biramo prvi red koji ima vodu.
	U njemu uzimamo sve maksimalne uzastopne segmente poplavljenih polja i brišemo ih redom.

	Intuicija: na ivici matrice povratak vode je često slabiji, pa ovaj pristup daje bolji $K$.

	## Pristup 4: Prvi/poslednji red/kolona

	Ovo je prva opšta greedy šema:
	1. generiši više kandidata za sledeći korak,
	2. izaberi najmanji važeći skup,
	3. primeni i ponovi dok ne nestane vode.

	Kandidati su segmenti sa:
	- prvog reda sa vodom,
	- poslednjeg reda sa vodom,
	- prve kolone sa vodom,
	- poslednje kolone sa vodom.

	Ovaj pristup je brz i u praksi daje solidan baseline.

	## Pristup 5: Komponenta u traci širine 2

	Za svaki par susednih redova (i simetrično kolona):
	- posmatramo samo ta dva reda,
	- nađemo komponente vode u toj traci,
	- uzmemo najmanju komponentu kao kandidata.

	## Pristup 6: Bilo koja linija (širina 1)

	Ne ograničavamo se na ivice:
	- za svaki red/kolonu tražimo segment uzastopnih polja koji možemo ukloniti tako da posle simulacije ostane dobar efekat.

	Ovo je jače, ali zahteva pažljivu proveru uslova.

	## Pristup 7: Pravougaonik širine 2

	Umesto proizvoljne komponente u traci, direktno ispitujemo pravougaonike kod kojih je jedna dimenzija 2.
	Za svaki kandidat simuliramo operaciju i uzimamo najmanji efektivni skup.

	Ovo je sporije, ali ume da nađe bolje operacije nego pristup 5.

	## Pristup 8: Šuplji pravougaonik

	Za pravougaonik $(x_1,y_1)-(x_2,y_2)$ uzima se samo granični pojas širine 2.
	Traži se najmanji važeći takav skup.

	Ovaj pristup je težak za efikasnu implementaciju i obično se poziva tek ako brži pristupi ne daju dovoljno mali $K$.

	## Pristup 9: Pun pravougaonik

	Za fiksne dimenzije $h \times w$:
	1. uzme se sva voda u tom pravougaoniku ($S$),
	2. simulira se povratak vode i izbace polja koja su se vratila ($S' = S \\setminus T$),
	3. ako je skup ne-prazan, kandidat je za sledeći korak.

	Ovo može da pomogne na nekim slučajevima, ali je najsporiji deo pretrage.

	## Praktične optimizacije

	Da bi rešenje radilo na velikim primerima:

	- **Bound na dobar odgovor:** tražimo kandidate samo dok ne nađemo skup veličine do trenutnog cilja (npr. do `jury` bound-a).
	- **Selektivno računanje:** posle jedne operacije ponovo računamo samo redove/kolone koje su mogle da se promene.
	- **Kaskadno uključivanje pretraga:** sporije pretrage (šuplji/puni pravougaonik) pozivaju se samo ako brže pretrage ne daju dobar skup.
	- **Rad po komponentama:** na najvećim ulazima isplati se razbiti problem na edge-connected komponente vode i rešavati ih odvojeno.
	- **Višestruko pokretanje:** parametar „dobro dovoljno“ može se doterati binarnom pretragom kroz više pokretanja.

	## Zaključak

	Za ovaj output-only zadatak najbolji praktičan pristup je kombinacija više pretraga:
	- brze pretrage za većinu koraka,
	- jače (i sporije) pretrage kao fallback,
	- jake optimizacije oko re-računanja i granice za „dovoljno dobar“ skup.

	[Izvor analize i autorskih podataka](https://algora.petlja.org/t/2025-2026/9654/3).

	``` cpp title="koofa-sol.cpp" linenums="1"
	/// Note that during contest, the contestants will be implementing a much
	/// shorter code. This one is written in a way for it to be easy to expand and
	/// read and is therefore longer

	#include <bits/stdc++.h>
	#define ll long long
	using namespace std;

	bool SPLIT_INTO_COMPONENTS =
	    true; /// Do we find connected components and solve each separately
	const short MAX_N =
	    1005; /// Maximal size of a matrix that will be passed to solveMatrix
	          /// function. The original grid may be larger if we can guarantee that
	          /// all its parts are smaller
	short LOWER_BOUND =
	    10; // We know that target score is not below this value

	short curmax;
	char dx[] = {1, -1, 0, 0};
	char dy[] = {0, 0, 1, -1};

	/// Transposes a sequence of cells
	vector<pair<short, short>> transpose(const vector<pair<short, short>> &V) {
	    vector<pair<short, short>> R = V;
	    for (int i = 0; i < R.size(); i++)
	        swap(R[i].first, R[i].second);
	    return R;
	}

	struct grid;
	vector<pair<short, short>> searchLineWidth1(const grid &g, short i);
	vector<pair<short, short>> searchLineWidth2(const grid &g, short i);

	/// Counts the number of cells filled with water adjacent to some cell
	char waterNextToMe(short x, short y, const vector<vector<char>> &mat) {
	    char r = 0;
	    for (char i = 0; i < 4; i++)
	        r += (mat[x + dx[i]][y + dy[i]] == 0);
	    return r;
	}

	/// Struct that remembers the current state of the grid
	struct grid {
	    vector<vector<char>> mat;      /// Marked blocked and filled cells
	    vector<vector<int>> pref;      /// Prefix sum
	    vector<vector<short>> prefRow; /// Prefix sum for each row
	    vector<short> ans1Width;       /// Precalculated 1 width rectangle
	    vector<short> ans2Width;       /// Precalculated 2 width rectangle

	    short n, m;
	    /// Initilizes the grid
	    void init(short n, short m) {
	        mat = vector<vector<char>>(n + 5, vector<char>(m + 5, 1));
	        pref = vector<vector<int>>(n + 5, vector<int>(m + 5, 1));
	        prefRow = vector<vector<short>>(n + 5, vector<short>(m + 5, 1));
	        this->n = n;
	        this->m = m;
	        ans1Width.resize(n + 5, 0);
	        ans2Width.resize(n + 5, 0);
	    }
	    /// Recursion to remove water from cells which have at most 1 neighboring
	    /// cell filled with water
	    void removeLeafs(short x, short y, vector<vector<pair<short, short>>> &R) {
	        if (x < 1 or y < 1 or x > n or y > m or mat[x][y] == 1)
	            return;
	        if (waterNextToMe(x, y, mat) > 1)
	            return;
	        mat[x][y] = 1;
	        R.push_back({{x, y}});
	        for (char i = 0; i < 4; i++)
	            removeLeafs(x + dx[i], y + dy[i], R);
	    }
	    /// Recalculates the values of the grid after update
	    void doUpdates(short minx, short maxx, short miny, short maxy) {
	        for (short i = minx; i <= maxx; i++) {
	            prefRow[i][0] = 0;
	            for (short j = 1; j <= m; j++)
	                prefRow[i][j] = prefRow[i][j - 1] + (mat[i][j] == 0);
	        }
	        for (short i = max(1, minx - 1); i <= min((int)n, maxx + 1); i++)
	            ans1Width[i] = searchLineWidth1(*this, i).size();
	        for (short i = max(minx - 2, 1); i <= min(n - 1, maxx + 1); i++)
	            ans2Width[i] = searchLineWidth2(*this, i).size();
	    }
	    /// Performs an operation on the grid
	    void doOperation(vector<vector<pair<short, short>>> &R,
	                     const vector<pair<short, short>> &selectedCells) {
	        vector<vector<pair<short, short>>> newOperations;
	        for (auto x : selectedCells)
	            mat[x.first][x.second] = 1;
	        newOperations.push_back(selectedCells);
	        for (auto x : selectedCells)
	            for (char i = 0; i < 4; i++)
	                removeLeafs(x.first + dx[i], x.second + dy[i], newOperations);

	        short minx = 1e4;
	        short maxx = -1e4;
	        short miny = 1e4;
	        short maxy = -1e4;
	        for (auto x : newOperations) {
	            for (auto y : x) {
	                minx = min(minx, y.first);
	                maxx = max(maxx, y.first);
	                miny = min(miny, y.second);
	                maxy = max(maxy, y.second);
	            }
	            R.push_back(x);
	        }

	        doUpdates(minx, maxx, miny, maxy);
	    }
	    /// Calculates prefix sum of the grid
	    void calculatePrefixSum() {
	        for (short i = 1; i <= n; i++)
	            for (short j = 1; j <= m; j++)
	                pref[i][j] = mat[i][j] + pref[i - 1][j] + pref[i][j - 1] -
	                             pref[i - 1][j - 1];
	    }
	    /// Gets the number of blocked cells in some rectangle
	    int getSum(short minx, short maxx, short miny, short maxy) const {
	        if (minx > maxx or miny > maxy)
	            return 0;
	        minx--;
	        miny--;
	        return pref[maxx][maxy] - pref[minx][maxy] - pref[maxx][miny] +
	               pref[minx][miny];
	    }
	    /// Gets the number of blocked cells in some rectangle using prefRow prefix
	    /// sum
	    int getSumByRow(short minx, short maxx, short miny, short maxy) const {
	        int s = 0;
	        for (short x = minx; x <= maxx; x++)
	            s += prefRow[x][maxy] - prefRow[x][miny - 1];
	        return s;
	    }
	    /// Transposes a vector, auxiliary function for grid transpose
	    template <typename T> void transpose(vector<vector<T>> &mat) {
	        vector<vector<T>> mat2(mat[0].size());
	        for (int i = 0; i < mat.size(); i++)
	            for (int j = 0; j < mat[0].size(); j++)
	                mat2[j].push_back(mat[i][j]);
	        swap(mat, mat2);
	    }
	    /// Grid transpose function
	    void transpose() {
	        swap(n, m);
	        transpose(mat);
	        transpose(pref);
	        transpose(prefRow);
	        ans1Width.resize(n + 5, 0);
	        ans2Width.resize(n + 5, 0);
	        doUpdates(1, n, 1, m);
	    }
	};

	/// Recursive function that propagates water in a grid
	void waterPropagationDFS(short x, short y, vector<vector<char>> &mat) {
	    if (x < 1 or x == mat.size() - 1 or y < 1 or y == mat[0].size() - 1)
	        return;
	    if (mat[x][y] != 2)
	        return;
	    if (waterNextToMe(x, y, mat) <= 1)
	        return;
	    mat[x][y] = 0;
	    for (char i = 0; i < 4; i++)
	        waterPropagationDFS(x + dx[i], y + dy[i], mat);
	}
	/// Gives the new grid mat when the water is propagated according to the
	/// transition algorithm
	void applyWaterPropagation(vector<vector<char>> &mat) {
	    for (int i = 0; i < mat.size(); i++)
	        for (int j = 0; j < mat[0].size(); j++)
	            if (mat[i][j] == 2)
	                waterPropagationDFS(i, j, mat);
	}

	/// Section 4.6 of the solution and comments pdf
	vector<pair<short, short>> searchLineWidth1(const grid &g, short i) {
	    short bestStart = -1e4, bestEnd = -1;
	    short prevStart = -1;
	    for (short j = 1; j <= g.m; j++) {
	        if (g.mat[i][j] == 0 and
	            waterNextToMe(i, j, g.mat) - (g.mat[i][j - 1] == 0) <= 1 and
	            prevStart != -1) {
	            if (j - prevStart < bestEnd - bestStart) {
	                bestEnd = j;
	                bestStart = prevStart;
	            }
	        }
	        if (g.mat[i][j] == 0 and
	            waterNextToMe(i, j, g.mat) - (g.mat[i][j + 1] == 0) <= 1)
	            prevStart = j;
	        if (g.mat[i - 1][j] == 0 and g.mat[i + 1][j] == 0)
	            prevStart = -1;

	        if (bestEnd - bestStart + 1 <= curmax)
	            break;
	    }

	    vector<pair<short, short>> cells;
	    if (bestEnd < 0)
	        return cells;
	    for (short j = bestStart; j <= bestEnd; j++)
	        if (g.mat[i][j] == 0)
	            cells.push_back({i, j});
	    return cells;
	}
	/// Section 4.7 of the solution and comments pdf
	vector<pair<short, short>> searchLineWidth2(const grid &g, short i) {
	    short bestStart = -1e4, bestEnd = -1, x = -1, score = 1.5e4;
	    short prevStart = -1;
	    for (short j = 1; j <= g.m; j++) {
	        if ((g.mat[i][j] == 1 or g.mat[i - 1][j] == 1 or
	             g.mat[i][j + 1] == 1) and
	            (g.mat[i + 1][j] == 1 or g.mat[i + 2][j] == 1 or
	             g.mat[i + 1][j + 1] == 1)) {
	            if (prevStart != -1 and
	                g.getSumByRow(i, i + 1, prevStart, j) < score and
	                g.getSumByRow(i, i + 1, prevStart, j) != 0) {
	                bestStart = prevStart;
	                bestEnd = j;
	                score = g.getSumByRow(i, i + 1, prevStart, j);
	            }
	        }

	        if ((g.mat[i][j] == 1 or g.mat[i - 1][j] == 1 or
	             g.mat[i][j - 1] == 1) and
	            (g.mat[i + 1][j] == 1 or g.mat[i + 2][j] == 1 or
	             g.mat[i + 1][j - 1] == 1))
	            prevStart = j;

	        if (score <= curmax)
	            break;
	    }
	    vector<pair<short, short>> cells;
	    if (bestEnd < 0)
	        return cells;
	    for (short j = bestStart; j <= bestEnd; j++) {
	        if (g.mat[i][j] == 0)
	            cells.push_back({i, j});
	        if (g.mat[i + 1][j] == 0)
	            cells.push_back({i + 1, j});
	    }
	    return cells;
	}
	/// Section 4.8 of the solution and comments pdf
	vector<pair<short, short>> searchHollowRectangle(const grid &g) {

	    /// Transposing the grid to make the search run faster
	    grid h = g;
	    bool gridTransposed = false;
	    if (h.m < h.n * 0.8) {
	        h.transpose();
	        gridTransposed = true;
	    }

	    h.calculatePrefixSum();

	    static char canBe[MAX_N + 5][MAX_N + 5];

	    /**
	       Rectangle corners are numbered 0, 1, 2, 3 and they look like this:

	       01
	       23

	       For each cell we calculate what corners can be in it.

	       canBe is a bitmask, and the i-th lowest bit represents corner i. So 0011
	       can be corners numbered 0 and 1.
	    */

	    for (short i = 1; i <= h.n; i++)
	        for (short j = 1; j <= h.m; j++) {
	            canBe[i][j] = 0;
	            if (h.mat[i][j] or h.mat[i - 1][j] or h.mat[i][j - 1])
	                canBe[i][j] |= 0b0001;
	            if (h.mat[i][j] or h.mat[i - 1][j] or h.mat[i][j + 1])
	                canBe[i][j] |= 0b0010;
	            if (h.mat[i][j] or h.mat[i + 1][j] or h.mat[i][j - 1])
	                canBe[i][j] |= 0b0100;
	            if (h.mat[i][j] or h.mat[i + 1][j] or h.mat[i][j + 1])
	                canBe[i][j] |= 0b1000;
	        }

	    static char canBeRow[MAX_N + 5]; /// Can any cell in said row be the given

	    for (short i = 1; i <= h.n; i++) {
	        canBeRow[i] = 0;
	        for (short j = 1; j <= h.m and canBeRow[i] != 0b1111; j++)
	            canBeRow[i] |= canBe[i][j];
	    }

	    short xLow = -1, xHigh = -1, yLow = -1, yHigh = -1;
	    short score = 1e4;

	    for (short r1 = 1; r1 <= h.n; r1++) {
	        if ((canBeRow[r1] & 0b0011) != 0b0011)
	            continue;
	        for (short r2 = r1 + 2; r2 <= h.n; r2++) {
	            if ((canBeRow[r2] & 0b1100) != 0b1100)
	                continue;

	            short prevPos = 1;

	            for (short j = 3; j <= h.m; j++) {
	                if ((canBe[r1][j - 2] & 0b0001) == 0b0001 and
	                    (canBe[r2][j - 2] & 0b0100) == 0b0100)
	                    prevPos = j - 2;
	                if ((canBe[r1][j] & 0b0010) == 0b0010 and
	                    (canBe[r2][j] & 0b1000) == 0b1000) {
	                    short tmp = ((r2 - r1 + 1) * (j - prevPos + 1) -
	                                 max(0, r2 - r1 + 1 - 4) *
	                                     max(0, j - prevPos + 1 - 4)) -
	                                (h.getSum(r1, r2, prevPos, j) -
	                                 h.getSum(r1 + 2, r2 - 2, prevPos + 2, j - 2));
	                    if (tmp < score and tmp != 0) {
	                        xLow = r1;
	                        xHigh = r2;
	                        yLow = prevPos;
	                        yHigh = j;
	                        score = tmp;
	                    }
	                }
	                if (score <= curmax)
	                    break;
	            }
	            if (score <= curmax)
	                break;
	        }
	        if (score <= curmax)
	            break;
	    }

	    vector<pair<short, short>> R;
	    if (xLow == -1)
	        return R;

	    for (short i = xLow; i <= xHigh; i++)
	        for (short j = yLow; j <= yHigh; j++) {
	            if (i - xLow <= 1 or xHigh - i <= 1 or j - yLow <= 1 or
	                yHigh - j <= 1) {
	                if (h.mat[i][j] == 0)
	                    R.push_back({i, j});
	            }
	        }

	    cerr << R.size() << endl;

	    if (gridTransposed)
	        return transpose(R);
	    else
	        return R;
	}
	vector<pair<short, short>> searchFullRectangle(short h, short w,
	                                               const grid &gInput) {
	    grid g(gInput);

	    g.calculatePrefixSum();

	    vector<vector<char>> tmp(h + 2, vector<char>(w + 2, 1));
	    vector<pair<short, short>> R;

	    for (short i = 0; i + h <= g.n; i++)
	        for (short j = 0; j + w <= g.m; j++) {
	            if (g.getSum(i + 1, i + h, j + 1, j + w) == h * w)
	                continue;

	            for (short ii = 1; ii <= h; ii++)
	                for (short jj = 1; jj <= w; jj++)
	                    tmp[ii][jj] =
	                        2 -
	                        g.mat[i + ii][j + jj]; /// same as (mat[i+ii][j+jj]==1 ?
	                                               /// 1 : 2), but faster

	            for (short ii = 0; ii <= h + 1; ii++)
	                tmp[ii][0] = g.mat[i + ii][j];
	            for (short ii = 0; ii <= h + 1; ii++)
	                tmp[ii][w + 1] = g.mat[i + ii][j + w + 1];

	            for (short jj = 0; jj <= w + 1; jj++)
	                tmp[0][jj] = g.mat[i][j + jj];
	            for (short jj = 0; jj <= w + 1; jj++)
	                tmp[h + 1][jj] = g.mat[i + h + 1][j + jj];

	            applyWaterPropagation(tmp);

	            /// Keep only the ones that are near some outside zero

	            vector<vector<char>>
	                nearZero[2]; /// char here is used as bool, because the code
	                             /// does not compile when I put bool
	            nearZero[0].resize(h + 2, vector<char>(w + 2));
	            nearZero[1].resize(h + 2, vector<char>(w + 2));

	            for (short ii = 1; ii <= h; ii++)
	                for (short jj = 1; jj <= w; jj++) {
	                    nearZero[0][ii][jj] = (tmp[ii][jj] == 0);
	                    for (int s = 0; s < 4; s++) {
	                        nearZero[0][ii][jj] |=
	                            (tmp[ii + dx[s]][jj + dy[s]] == 0);
	                    }
	                }

	            for (short ii = 1; ii <= h; ii++)
	                for (short jj = 1; jj <= w; jj++) {
	                    nearZero[1][ii][jj] = nearZero[0][ii][jj];
	                    for (int s = 0; s < 4; s++)
	                        nearZero[1][ii][jj] |=
	                            nearZero[0][ii + dx[s]][jj + dy[s]];
	                }

	            vector<pair<short, short>> V;
	            for (short ii = 1; ii <= h; ii++)
	                for (short jj = 1; jj <= w; jj++)
	                    if (tmp[ii][jj] == 2 and nearZero[1][ii][jj])
	                        V.push_back({i + ii, j + jj});

	            /// Checking if the shrinkages near zero values lead to a bad set

	            for (short ii = 0; ii <= h + 1; ii++)
	                for (short jj = 0; jj <= w + 1; jj++)
	                    tmp[ii][jj] =
	                        g.mat[i + ii][j + jj]; /// same as (mat[i+ii][j+jj]==1 ?
	                                               /// 1 : 2), but faster

	            for (auto x : V)
	                tmp[x.first - i][x.second - j] = 1;
	            bool ok = true;
	            for (auto x : V) {
	                if (!ok)
	                    break;
	                if (waterNextToMe(x.first - i, x.second - j, tmp) > 1)
	                    ok = false;
	            }
	            if (!ok)
	                V.clear();

	            if (V.size() != 0 and (R.size() == 0 or R.size() > V.size()))
	                swap(R, V);
	        }

	//    cout << R.size() << endl;
	    return R;
	}

	/// Applies the asymmetrical searching algorithms (which are the faster ones)
	vector<pair<short, short>> searchAsymmetric(const grid &g) {
	    vector<pair<short, short>> chosenOperation;
	    /// 1 width search
	    {
	        short chosen = -1;
	        for (short i = 1; i <= g.n; i++) {
	            if (g.ans1Width[i] > 0 and
	                (chosen == -1 or g.ans1Width[i] < g.ans1Width[chosen]))
	                chosen = i;
	        }
	        if (chosen != -1)
	            chosenOperation = searchLineWidth1(g, chosen);
	    }
	    if (chosenOperation.size() <= curmax)
	        return chosenOperation;
	    /// 2 width search
	    {
	        short chosen = -1;
	        for (int i = 1; i < g.n; i++) {
	            if (g.ans2Width[i] > 0 and
	                (chosen == -1 or g.ans2Width[i] < g.ans2Width[chosen]))
	                chosen = i;
	        }
	        if (chosen != -1 and g.ans2Width[chosen] < chosenOperation.size())
	            chosenOperation = searchLineWidth2(g, chosen);
	    }
	    if (chosenOperation.size() <= curmax)
	        return chosenOperation;

	    return chosenOperation;
	}
	/// Applies the symmetrical searching algorithms (which are the slower ones)
	vector<pair<short, short>> searchSymmetric(const grid &g) {
	    vector<pair<short, short>> chosenOperation;
	    { /// Hollow rectangle search
	        vector<pair<short, short>> opr = searchHollowRectangle(g);
	        if (opr.size() < chosenOperation.size() or chosenOperation.size() == 0)
	            chosenOperation = opr;
	    }
	    if (chosenOperation.size() <= curmax)
	        return chosenOperation;

	    { /// Full rectangle search
	        for (unsigned char dim = 4; dim <= 7; dim++) {
	            vector<pair<short, short>> opr = searchFullRectangle(dim, dim, g);
	            if (opr.size() != 0) {
	                if (opr.size() < chosenOperation.size() or
	                    chosenOperation.size() == 0)
	                    chosenOperation = opr;
	                break;
	            }
	        }
	    }
	    if (chosenOperation.size() <= curmax)
	        return chosenOperation;

	    return chosenOperation;
	}

	/// Finds a sequence of operations to remove the water from the given matrix
	vector<vector<pair<short, short>>> solveMatrix(vector<vector<char>> mat) {
	    vector<vector<pair<short, short>>> R;
	    grid original;
	    original.init(mat.size() - 2, mat[0].size() - 2);
	    for (short i = 1; i <= original.n; i++)
	        for (short j = 1; j <= original.m; j++)
	            original.mat[i][j] = mat[i][j];

	    for (short i = 1; i <= original.n; i++)
	        for (short j = 1; j <= original.m; j++)
	            original.removeLeafs(i, j, R);

	    original.doUpdates(1, original.n, 1, original.m);

	    grid transposed(original);
	    transposed.transpose();

	    while (true) {
	        vector<pair<short, short>> op1 = searchAsymmetric(original);
	        if (op1.size() == 0) /// There is nothing to fill
	            break;
	        vector<pair<short, short>> chosenOperation;
	        swap(chosenOperation, op1);

	        if (chosenOperation.size() > curmax) {
	            vector<pair<short, short>> op2;
	            op2 = searchAsymmetric(transposed);
	            op2 = transpose(op2);
	            if (op2.size() < chosenOperation.size() and op2.size() != 0)
	                swap(chosenOperation, op2);
	        }

	        if (chosenOperation.size() > curmax) {
	            vector<pair<short, short>> op3;
	            op3 = searchSymmetric(original);
	            if (op3.size() < chosenOperation.size() and op3.size() != 0)
	                swap(chosenOperation, op3);
	        }

	        curmax = max(curmax, (short)chosenOperation.size());
	        original.doOperation(R, chosenOperation);
	        vector<vector<pair<short, short>>> useless;
	        transposed.doOperation(useless, transpose(chosenOperation));
	    }

	    return R;
	}

	short m, n;
	/// Recursive function that finds the whole edge-connected component of
	/// non-blocked cells to which cell (x, y) belongs to
	void findComponents(short x, short y, const vector<string> &mat,
	                    vector<vector<bool>> &visited,
	                    vector<pair<short, short>> &cords) {

	    if (x < 1 or x > n or y < 1 or y > m or mat.at(x).at(y) == '1')
	        return;

	    if (visited.at(x).at(y))
	        return;

	    visited.at(x).at(y) = true;
	    cords.push_back({x, y});
	    for (char i = 0; i < 4; i++)
	        findComponents(x + dx[i], y + dy[i], mat, visited, cords);
	}
	/// Solves a connected component
	void processComponent(vector<pair<short, short>> cords,
	                      vector<vector<pair<short, short>>> &R) {
	    if (cords.size() == 0)
	        return;
	    if (cords.size() == 1) {
	        R.push_back(cords);
	        return;
	    }
	    short minx = 1e4, maxx = -1e4, miny = 1e4, maxy = -1e4;
	    for (auto x : cords) {
	        minx = min(minx, x.first);
	        maxx = max(maxx, x.first);
	        miny = min(miny, x.second);
	        maxy = max(maxy, x.second);
	    }
	    vector<vector<char>> mat(maxx - minx + 3, vector<char>(maxy - miny + 3, 1));
	    for (auto x : cords)
	        mat[x.first - minx + 1][x.second - miny + 1] = 0;
	    vector<vector<pair<short, short>>> matRes = solveMatrix(mat);
	    for (auto &x : matRes) {
	        for (auto &y : x) {
	            y.first += minx - 1;
	            y.second += miny - 1;
	        }
	        R.push_back(x);
	    }
	}
	/// Solves a single input file
	void solveSingleTest(istream &inf, ostream &ouf) {
	    curmax = LOWER_BOUND;
	    inf >> n >> m;
	    vector<string> inputMatrix(n + 5);
	    for (int i = 1; i <= n; i++) {
	        inf >> inputMatrix[i];
	        inputMatrix[i] = "1" + inputMatrix[i] + "1111";
	    }

	    vector<vector<pair<short, short>>> R;
	    if (SPLIT_INTO_COMPONENTS) {
	        vector<vector<bool>> visited(n + 5, vector<bool>(m + 5, false));
	        for (short i = 1; i <= n; i++)
	            for (short j = 1; j <= m; j++) {
	                vector<pair<short, short>> cords;
	                findComponents(i, j, inputMatrix, visited, cords);
	                processComponent(cords, R);
	            }
	    } else {
	        vector<pair<short, short>> cords;
	        for (short i = 1; i <= n; i++)
	            for (short j = 1; j <= m; j++)
	                if (inputMatrix[i][j] == '0')
	                    cords.push_back({i, j});
	        processComponent(cords, R);
	    }
	    ouf << curmax << "\n" << R.size() << "\n";
	    for (auto x : R) {
	        ouf << x.size() << "\n";
	        for (auto y : x)
	            ouf << y.first << " " << y.second << "\n";
	    }
	    cerr << "SCORE IS " << curmax << endl;
	}
	int main(int argc, char** argv) {
	    if(argc>=2){
	        LOWER_BOUND = atoi(argv[1]);
	    }
	    solveSingleTest(cin, cout);
	    return 0;
	}
	```
