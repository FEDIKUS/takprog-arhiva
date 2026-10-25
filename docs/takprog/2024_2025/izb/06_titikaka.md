---
hide:
  - toc
---

# 6 - Titikaka

=== "Zadatak"
	
	| Vremensko ograničenje | Memorijsko ograničenje |
	|:-:|:-:|
	| 2000ms | 512MB |
	
	
	
	
	Organizatori Međunarodne informatičke olimpijade u Boliviji žele da organizuju ekskurziju na jezeru Titikaka za svojih $N$ takmičara, pa su za taj poduhvat iznajmili $M$ ležaljki. 
	Ipak, postoji jedan problem. Svaki takmičar bi želeo da isproba svaku ležaljku, što je higijenski vrlo problematično. Naime, svi takmičari i ležaljke su potencijalno prljavi na svoj jedinstven način, pa je nepoželjno da takmičari dođu u kontakt sa tuđom prljavštinom - šta ako se neko razboli i pošalje žalbu organizatorima? Isto tako, ne bi valjalo ni da neka ležaljka postane prljavija nego što jeste. 
	
	<br>
	
	Zbog toga organizatori planiraju da kupe proizvoljan broj peškira. Oni će unapred odrediti redosled kojim takmičari koriste ležaljke, i pre svakog korišćenja postavljati peškire na ležaljke tako da se ispune sledeći higijenski uslovi:
	
	- Kada takmičar legne na ležaljku, između njih mora postojati **barem jedan** peškir, a može ih biti proizvoljno mnogo.
	- Kada takmičar legne na peškir, strana na koju je legao ne sme sadržati tuđu prljavštinu.
	- Kada se peškir postavi na ležaljku, strana koja dodiruje ležaljku ne sme sadržati prljavštinu koja nije već bila na ležaljci.
	
	<br>
	
	Peškiri mogu da se prljaju, a jedan peškir je moguće iskoristiti proizvoljno mnogo puta.
	Prljavština se razmenjuje na sledeći način:
	
	
	- Kada takmičar legne na peškir, strana na koju je legao dobiće prljavštinu tog takmičara.
	- Ukoliko su dva peškira poređana jedan preko drugog, njihove dve strane koje se dodiruju međusobno razmene sve prljavštine koje sadrže.
	 - Kada se peškir postavi na ležaljku, strana koja dodiruje ležaljku dobiće prljavštinu te ležaljke
	
	<br>
	
	Pošto je sav budžet potrošen na ekskurziju, organizatori bi želeli da kupe **što manje peškira**. 
	
	<br>
	
	## Opisi funkcija
	
	Potrebno je da implementirate funkciju
	
	<br>
	
	-   $Raspored(N, M, P, T[\ldots], L[\ldots], D[\ldots],A[\ldots][\ldots],B[\ldots][\ldots])$
	
	<br>
	
	Ova funkcija će biti pozvana jednom po primeru. $N$ i $M$ redom predstavljaju broj takmičara i ležaljki, a ostali parametri vam služe za ispis rešenja.
	
	<br>
	
	 Rešenje ispisujete na sledeći način:
	 - $P$ je prirodan broj koji treba da predstavlja broj peškira koji koristite, i mora da važi $P \leq 250$.
	 - Niz $T$ je dužine $NM$, u $T[i]$, $1 \leq i \leq NM$, upisujete redni broj takmičara (od $1$ do $N$) koji tada koristi ležaljku.
	 - Niz $L$ je dužine $NM$, u $L[i]$, $1 \leq i \leq NM$, upisujete redni broj ležaljke (od $1$ do $M$) koju takmičar $T[i]$ koristi.
	- Niz $D$ je dužine $NM$, u $D[i]$, $1 \leq i \leq NM$, upisujete broj peškira (od $1$ do $P$) koji se koristi kako bi takmičar $T[i]$  iskoristio ležaljku $L[i]$. Svi iskorišćeni peškiri u jednom redu moraju biti različiti.
	- U matrici $A$ kao vrednost $A[i][j]$, $1 \leq j \leq D[i]$, upisujete redni broj $j$-tog peškira koji se koristi u $i$-tom ležanju, gde je $A[i][1]$ onaj peškir koji je u direktnom dodiru sa takmičarom, a $A[i][D[i]]$ onaj peškir koji je u direktnom dodiru sa ležaljkom.
	- U matrici $B$ kao vrednost $B[i][j]$, $1 \leq j \leq D[i]$, upisujete $0$ ako je peškir $A[i][j]$ postavljen normalno, tj. da mu prva strana dodiruje $A[i][j-1]$ a druga $A[i][j+1]$, a upisujete $1$ ako je postavljen obrnuto, tj. da mu prva strana dodiruje $A[i][j+1]$ a druga $A[i][j-1]$.
	- Matrice $A$ i $B$ imaju $NM$ redova i $250$ kolona - **ne popunjavate sva polja**, već u $i$-tom redu popunjavate samo $D[i]$ polja.
	
	<br>
	
	Obavezno je da se svaki par $(T[i], L[i])$ pojavi **tačno** jedanput, to jest da svaki takmičar svaku ležaljku iskoristi tačno jedanput.
	<br>
	
	**Svi nizovi su indeksirani od 1.**
	
	<br>
	
	## Primer
	
	Ovaj test primer je čisto demonstrativan i ne spada u onih deset koji rešavate.
	
	Neka je $N = M = 2$. Sledi rešenje koje koristi $3$ peškira:
	
	<br>
	
	Na početku prvi takmičar koristi prvu ležaljku, a između njih se postavljaju peškiri $1$ i $2$,  kojima redom prva i druga strana pokazuju nalevo. Prva strana peškira $1$ prikuplja prljavštinu od takmičara $1$, a prva strana peškira $2$ prikuplja prljavštinu ležaljke $1$.
	
	Nakon toga, prvi takmičar koristi drugu ležaljku, a između njih se postavlja peškir $3$. Prva strana peškira $3$ prikuplja prljavštinu od takmičara $1$, a druga od ležaljke $1$.
	
	Posle toga drugi takmičar koristi prvu ležaljku, a između njih se postavlja peškir $2$ u obrnutom položaju. Druga strana peškira prikuplja prljavštinu od takmičara $2$, a prva od ležaljke $1$.
	
	Na kraju, drugi takmičar koristi drugu ležaljku, a između njih se postavlja peškiri $2$ u obrnutom i $1$ u normalnom položaju. Druga strana peškira $2$ prikuplja prljavštinu od takmičara $2$, druga strana peškira $1$ prikuplja prljavštinu od ležaljke $2$, a prva strana peškira $2$ i prva strana peškira $1$ razmenjuju prljavštine koje sadrže.
	
	<br>
	
	## Ograničenja i bodovanje
	
	U tabeli dole dati su test primeri koje rešavate. Svaki test primer boduje se na sledeći način:
	- Neka je $K$ broj peškira koji vaše rešenje koristi.
	- Ukoliko važi $K > Q_1$,  na tom primeru osvajate $0$ poena.
	- Ukoliko važi $Q_1 \geq K > Q_2$, na tom primeru osvajate $5$ poena.
	- Ukoliko važi $Q_2 \geq K$, na tom primeru osvajate $10$ poena.
	
	Svi test primeri boduju se odvojeno, tj. nema podzadataka.
	
	<br>
	
	|Primer|$N$ | $M$| $Q_1$ | $Q_2$ |
	|--------|--------|--------|--------|--------|
	|1|5|5|25|10|
	|2|3|2|5|4|
	|3|1|7|6|4|
	|4|1|199|150|100|
	|5|15|20|30|21|
	|6|30|40|50|41|
	|7|60|100|91|90|
	|8|99|199|167|166|
	|9|199|200|234|233|
	|10|200|200|235|234|
	
	<br>
	
	## Detalji implementacije
	
	Potrebno je da pošaljete tačno jedan fajl  `titikaka.cpp`  koji implementira pomenute funkcije. Osim traženih funkcija, vaš fajl može sadržati i dodatne globalne promenljive, pomoćne funkcije i dodatne biblioteke.
	
	Vaša funkcija mora biti sledećeg oblika:
	
	`void Raspored(int N, int M, int *P, int* T, int *L, int* D, int** A, bool** B);`
	
	<br>
	
	**Vašim programima je dozvoljeno da menjaju sadržaj nizova ali ne smeju da pristupaju van granica datih nizova.**
	
	**Obratite pažnju da se ovi podaci, pogotovo matrice $A$ i $B$, računaju u utrošenu memoriju!**
	
	<br>
	
	Uz zadatak, obezbeđen vam je "template" fajl  `code.cpp`  koji možete koristiti i menjati po potrebi. Takođe vam je obezbeđen program  `grader.cpp`  koji služi da lakše testirate kodove. Ovaj program učitava sa standardnog ulaza sledeće podatke:
	
	- U jednom redu brojeve $N, M$.
	
	<br>
	
	Zatim ovaj program zove vašu funkciju i ispisuje rešenje u sledećem formatu:
	
	<br>
	
	```
	P
	D[1] T[1] A[1][1]x A[1][2]x ... A[1][D[1]]x L[1]
	D[2] T[2] A[2][1]x A[2][2]x ... A[2][D[2]]x L[2]
	.
	.
	.
	D[NM] T[NM] A[NM][1]x A[NM][2]x ... A[NM][D[NM]]x L[NM]
	```
	gde je `x = p` ako je `B[i][j] = 0`,  a `x = d` ako  `B[i][j] = 1`
	
	<br>
	
	Na primer, ispis rešenja gorenavedenog primera izgledao bi ovako:
	
	<br>
	
	```
	3
	2 1 1p 2d 1
	1 1 3p 2
	1 2 2d 1
	2 2 2d 1p 2
	```
	
=== "Rešenje"
	
	| Autor | Tekst i test primeri | Analiza rešenja | Testiranje |
	|:-:|:-:|:-:|:-:|
	| Marko Milenković | Jovan Bengin | Jovan Bengin | Marko Milenković, Aleksa Plavšić |
	
	Radi jednostavnosti zapisa, obrnuti peškiri biće **boldovani**. Takmičari će biti označeni sa $T_i$, ležaljke sa $L_i$.
	
	## Rešenje kada je $N=1, M=2k+1$
	Sledeća konstrukcija koristi $k + 1$, tj. $(N+M)/2$ peškira, i osvaja sve poene na ovakvim primerima:
	- Postavimo peškire $1$ do $k$ na ležaljke $1$ do $k$.
	- Takmičar, koristeći peškir $k + 1$, legne na prvih $k$ ležaljki (dakle redosled bi bio $T_1-p_{k+1}-p_i-L_i$, $1 \leq i \leq k$)
	- Takmičar, koristeći peškir $k+1$, legne na ležaljku $k+1$.
	- Peškire $1$ do $k$ obrnemo i postavimo na ležaljke $k+2$ do $2k+1$.
	- Takmičar, koristeći peškir $k + 1$, legne na ležaljke $k+2$ do $2k+1$ (dakle redosled bi bio $T_1-p_{k+1}-\mathbf{p_i}-L_i$ $k+2 \leq i \leq 2k+1$).
	
	Ovde smo koristili peškir $p_{k + 1}$ kako bismo sprečili direktan prenos prljavštine između ostalih peškira i takmičara. Tako će se i u narednim rešenjima pojavljivati tzv. džoker peškir $J$, koji će prvenstveno biti postavljan između dva peškira kako bi se sprečio prenos prljavštine između njih.
	
	## Rešenje kada je $N=3, M=2$
	Ovo rešenje spominjemo jer se na njemu zapravo zasniva glavno rešenje. Koristićemo $4$ peškira, označimo ih sa $t_1, t_2, l_1, J$. Operacije izgledaju ovako:
	- $T_1-t_1-l_1-L_1$
	- $T_2-t_2-l_1-L_1$
	- $T_3-\mathbf{t_2}-J-l_1-L_1$
	- $T_1-t_1-\mathbf{J}-\mathbf{l_1}-L_1$
	- $T_3-\mathbf{t_2}-\mathbf{l_1}-L_1$
	- $T_2-\mathbf{t_1}-\mathbf{l_1}-L_2$
	
	## Rešenje koje koristi $1+\lceil 2/3N+M/2 \rceil$ peškira
	
	Uradimo prvo za $N=3a, M=2b$. Tada možemo da takmičare podelimo u $a$ grupa od $3$, a ležaljke u $b$ grupa od $2$. Sad za svaki par grupe takmičara i grupe ležaljki možemo da primenimo gorenavedeno rešenje za $N=3, M=2$, samo treba paziti redosled kojim radimo ove operacije.
	
	Svakoj grupi takmičara dodelićemo po dva peškira, koje ćemo označavati sa $t_1$ i $t_2$. Isto tako, svakoj grupi ležaljki dodelićemo po jedan peškir $l_1$. Koristićemo i jedan džoker peškir $J$, koji ćemo postavljati tako da što kasnije moguće isprljamo obične peškire.
	 
	Može se pokazati da sledeći redosled valja:
	
	Prvo, prođemo kroz sve parove i vršimo sledeće operacije:
	- $T_1-t_1-l_1-L_1$
	- $T_2-t_2-l_1-L_1$
	
	Onda, prođemo kroz sve parove i vršimo sledeće operacije:
	- $T_3-\mathbf{t_2}-J-l_1-L_1$
	
	Zatim, prođemo kroz sve parove i vršimo sledeće operacije:
	- $T_1-t_1-\mathbf{J}-\mathbf{l_1}-L_1$
	- $T_3-\mathbf{t_2}-\mathbf{l_1}-L_1$
	
	Na kraju, prođemo kroz sve parove i vršimo sledeće operacije:
	- $T_2-\mathbf{t_1}-\mathbf{l_1}-L_2$
	
	Kada je $N=3a, M=2b$, ovo očigledno koristi $1+2/3N+M/2$ peškira. Slučajevi kad $N$ nije deljivo sa $3$ ili $M$ nije deljivo sa $2$ mogu se uraditi na isti način, sem što ćemo imati još jednu nepunu grupu na kraju. Sa njom se mogu raditi iste ove operacije, samo izbacimo one koje koriste nepostojeće takmičare/ležaljke. Tada rešenje koristi $1+\lceil 2/3N+M/2 \rceil$ peškira.
	
	Kombinovano sa rešenjem za slučaj $N=1, M=2k+1$, ovo rešenje osvaja $80$ poena.
	
	## Rešenje koje koristi $\lceil 2/3N+M/2 \rceil$ peškira
	Ideja je u suštini ista - vrši se podela u grupe od po $3$ takmičara i $2$ peškira, samo što ovaj put moramo nekako da iskoristimo peškir manje. Najbolji kandidat za izbacivanje jeste džoker peškir, koji ćemo zapravo dobiti iz nekog drugog peškira. 
	
	Konkretno, pretpostavimo da važi $N, M \geq 6$ i $N = 3a+6$, $M= 2b+2$. Izdvojićemo jednu specijalnu grupu od $6$ takmičara i jednu od $2$ peškira, a ostatak delimo kao ranije. Otprilike želimo da odradimo operacije između te dve grupe, i odatle uzeti jedan peškir koji ćemo koristiti kao džoker.
	
	Označimo $6$ specijalnih takmičara sa $T'_i$, $1 \leq i \leq 6$, ležaljka sa $L'_i$, $1 \leq i \leq 2$. Oni će koristiti $5$ peškira $p'_i$, $1 \leq i \leq 5$.
	Ostale peškire koje koriste takmičari označavamo sa $pt_i$, $1 \leq i \leq 2a$, a one koje koriste ležaljke sa $pl_i$, $1 \leq i \leq b$.
	
	Možete se (poželjno papirom i olovkom) uveriti da je sledeći redosled operacija validan:
	
	1. Sve kombinacije $T'_1-p'_2$, $T'_3-p'_3$, $T'_4-p'_4$, $T'_5-p'_5$, $T_{3i-1}-pt_{2i}$, $T_{3i-2}-pt_{2i-1}$ sa $p'_1-L'_2$, $pl_{j}-L_{2j-1}$.
	2. Dalje ćemo $p'_4$ koristiti kao džoker, označavamo ga sa $J$.
	3. Obrćemo $p'_5$, kao i sve $pt_{2i}$.
	4. Sve kombinacije $T'_6-\mathbf{p'_5}-J$, $T_{3i}-\mathbf{pt_{2i}}-J$ sa $p'_1-L'_2$, $pl_j-L_{2j-1}$.
	5. Sve kombinacije $T'_2 - p'_1$ sa $L'_2$, $pl_{j} - L_{2j-1}$.
	6. Obrćemo sve $pl_{j}$.
	7. Sve kombinacije $T'_1-p'_2$ sa $L'_1$, $\mathbf{J}-\mathbf{pl_{j}}-L_{2j}$
	8. Sve kombinacije $T'_2-p'_1$, $T'_6-\mathbf{p'_5}$, $T_{3i}-\mathbf{pt_{2i}}$ sa $p'_2-L'_1$, $\mathbf{pl_{j}}-L_{2j}$
	9. Sve kombinacije $T'_3-p'_3$, $T_{3i-2}-pt_{2i-1}$ sa $\mathbf{J}-p'_2-L'_1$, $\mathbf{J}-\mathbf{pl_j}-L_{2j}$
	10. Obrćemo peškir $p'_3$ i sve peškire $pt_{2i-1}$. 
	11. Sve kombinacije $T'_4-\mathbf{p'_3}$, $T'_5-\mathbf{J}$, $T_{3i-1}-\mathbf{pt_{2i-1}}$ sa $\mathbf{pl_{j}}-L_{2j}$,  $p'_2-L'_1$
	
	Ukupan broj iskorišćenih peškira je $5 + 2a + b = 6 + 2(N-6)/3 + (M-2)/2 = 2N/3 + M/2$. Slučajevi kad $N$ nije deljivo sa $3$ ili $M$ nije deljivo sa $2$ mogu se uraditi na isti način kao ranije - treba povećati granicu do koje iteriramo $i, j$, ali ne vršiti one operacije nad nepostojećim takmičarima ili peškirima. Može se videti da se tada koristi $\lceil 2N/3 + M/2 \rceil$ peškira.
