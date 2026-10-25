---
hide:
  - toc
---

# 2 - Gradovi

=== "Zadatak"

	| Vremensko ograničenje | Memorijsko ograničenje |
	|:-:|:-:|
	| 1000ms | 256MB |

	U državi Bajtoviji postoji $N$ mesta koja su povezana sa $M$ dvosmernih puteva. Garantuje se da je moguće stići od bilo kojeg mesta do bilo kog drugog mesta korišćenjem jednog ili više puteva. Put $i$ povezuje mesta $U[i]$ i $V[i]$ i ima dužinu $2^i$. $K$ od datih $N$ mesta su gradovi, dok su preostala sela. *Izolovanost* nekog sela je rastojanje do najbližeg grada.

	U cilju razvoja, kralj Bajtovije želi da neka od datih sela proglasi gradovima, tako da se izolovanost najizolovanijeg sela minimizuje. U okviru budžeta Batjovije, vlada je odobrila proglašavanje tačno $Q$ sela u gradove.

	Pronađite sela koja treba proglasiti gradovima, tako da se izolovanost najizolovanijeg sela minimizuje. **Ukoliko ima više rešenja, pronađite bilo koje**.

	## Opisi funkcija

	Potrebno je da implementirate funkciju

	- $Gradovi(N, M, K, Q, U[\ldots], V[\dots], G[\dots], S[\dots])$

	Ova funkcija će biti pozvana jednom po primeru. Broj $N$ predstavlja broj mesta u Bajtoviji, $M$ broj puteva, $K$ je broj gradova, dok je $Q$ broj sela koja je potrebno proglasiti gradovima. Nizovi $U$ i $V$  dužine $M$ predstavljaju mesta koja su povezana. Niz $G$ dužine $K$ predstavlja listu gradova. U niz $S$ je potrebno upisati $Q$ sela koja će biti proglašena gradovima. **Svi nizovi su indeksirani od 1.**

	## Primer

	Neka je $N = 5, \ M = 5, \ K = 2, \ Q = 1, \ U = \{1, 2, 3, 4, 5\}, \ V = \{2, 3, 4, 2, 4 \}, \ G = \{2, 4 \}$. U ovom primeru postoje $2$ grada, a jedno selo je potrebno proglasiti gradom. Ukoliko mesto $5$ proglasimo gradom, najizlovanije selo postaje selo $3$ sa izolovanošću $2^2 = 4$.

	## Ograničenja

	* $2 \leq N, M \leq 200.000$
	* $0 \leq K \leq N$
	* $1 \leq Q \leq N$
	* $1 \leq K + Q \leq N$
	* $1 \leq U_i \neq V_i \leq N$
	* Bajtovija je povezana
	* Svaki put povezuje različit par gradova

	## Podzadaci

	Test primeri su podeljeni u $6$ podzadataka:

	-   **[4 poena]:** $M = N, Q = 1$, put $i$ povezuje mesta $i$ i $i+1$, za $i < N$, a put $N$ povezuje mesto $N$ i mesto $1$
	-   **[9 poena]:** $M = N, Q = 1$, putevi povezuju mesta ciklično (tj. putevi su permutacija puteva iz prethodnog podzadatka)
	-   **[11 poena]:** $K = 1, Q = 1$
	-   **[28 poena]:** $Q = 1$
	-   **[12 poena]:** $N, Q \leq 1.000$
	-   **[36 poena]:** Nema dodatnih ograničenja

	## Detalji implementacije

	Potrebno je da pošaljete tačno jedan fajl  `gradovi.cpp`  koji implementira pomenutu funkciju. Osim tražene funkcije, vaš fajl može sadržati i dodatne globalne promenljive, pomoćne funkcije i dodatne biblioteke.

	Vaša funkcija mora biti sledećeg oblika:

	`void Gradovi(int N, int M, int K, int Q, int* U, int* V, int* G, int* S);`

	**Vašim programima je dozvoljeno da menjaju sadržaj nizova ali ne smeju da pristupaju van granica datih nizova.**

	Uz zadatak, obezbeđen vam je "template" fajl  `code.cpp`  koji možete koristiti i menjati po potrebi. Takođe vam je obezbeđen program  `grader.cpp`  koji služi da lakše testirate kodove. Ovaj program učitava sa standardnog ulaza sledeće podatke:

	- U prvom redu brojeve $N, M, K, Q$.
	- U narednih $M$ redova po $2$ broja $U[i]$ i $V[i]$.
	- U narednom redu $K$ vrednosti koje predstavljaju elemente niza $G$.

	Zatim ovaj program zove vašu funkciju i ispisuje vrednosti $S[1],S[2],$ $...$ $,$ $S[Q]$, koje vaša funkcija upiše u njega.

	[Test primeri i prateći fajlovi sa zvaničnog takmičenja](https://nyc3.digitaloceanspaces.com/takprog/2025-26/2025-2026-sio-problems.zip).

=== "Rešenje"

	| Autor | Tekst i test primeri | Analiza rešenja | Testiranje |
	|:-:|:-:|:-:|:-:|
	| Jovan Bengin | Aleksa Milisavljević | Jovan Bengin | Marko Milenković |

	## Podzadatak 1: $M=N,Q=1$, put $i$ povezuje mesta $i$ i $i+1$, za $i<N$, a put $N$ povezuje mesto $N$ i mesto $1$

	Posmatrajmo put $N$. On je dužine $2^N$, dok je suma dužina ostalih puteva $2^1$ $+$ $2^2$ $+ \dots + 2^{N-1}$ = $2^N - 2$. Dakle, bilo koja ruta koja koristi put $N$  duža je od bilo koje rute koja ga ne koristi.

	Razmotrimo slučaj $K = 0$. Neka smo neko selo $k$ proglasili za grad. Primetimo da uvek možemo birati rutu iz sela ka gradu koja izbegava granu $N$. Drugim rečima, iz sela $i < k$ bi se išlo rutom $i \to i +1 \to \dots \to k - 2 \to k - 1$, a iz sela $j > k$ rutom $j \to j - 1 \to \dots \to k + 1 \to k$.

	Put $N-1$ će sigurno biti deo neke rute, pa je naš cilj da proglasimo grad tako da minimizujemo dužinu rute koja sadrži put $N-1$. Ovo radimo tako što proglasimo mesto $N - 1$ za grad -- tada je najveća izolovanost upravo $2^{N-1}$.

	Šta se dešava u slučaju $K \geq 1$? Tada postojeći gradovi dele ceo graf na uzastopne intervale sela. Ilustracije radi, posmatrajmo interval $i, i + 1, \dots, j$, gde su $i$ i  $j$ gradovi, $i+1, \dots j-1$ sela, a važi $i<j-1$ (kako bi u intervalu postojalo bar jedno selo). Slično kao pre, put $j-1$ neće biti korišćen ni u jednoj ruti, jer sve rute u ovom intervalu mogu ići ka gradu $i$.

	Ukoliko proglasimo selo $j-1$ za grad, nećemo koristiti ni put $j-2$, pa će najveća izolovanost u ovom intervalu biti $2^i + 2^{i+1} + \dots$ $+ 2^{j-3}$, dobijena rutom od $j-2$ do $i$ Ukokiko ipak ne proglasimo nijedno selo u intervalu gradom, najveća izolovanost biće $2^i + 2^{i+1} + \dots$ $+ 2^{j-2}$, dobijena rutom od $j-1$ do $i$.

	Slučaj kada komponenta prolazi kroz granu $N$, tj. gde ne važi $i < j$, malo je komplikovaniji, ali se dolazi do istog zaključka: izolovanost celog grafa zavisiće od treće najduže grane jednog intervala po izboru, kao i od druge najteže grane svih ostalih intervala.  Prema tome, grad je potrebno proglasiti u onom intervalu sa najvećom vrednosti dužine druge najduže grane.

	Vremenska složenost: $O (N)$

	## Podzadatak 2:  $M=N,Q=1$, putevi povezuju mesta ciklično

	Ovaj podzadatak se razlikuje od prethodnog po tome što su dužine puteva permutovane.

	Posmatrajmo ponovo slučaj $K = 0$.  Slično kao pre, put dužine $2^N$ neće biti korišćen, pa ga možemo ignorisati, ali put dužine $2^{N-1}$ hoće, pa želimo da minimizujemo dužinu rute koja ga koristi. Neka je, bez umanjenja opštosti, put $N$ težine $2^N$, a put $k$ dužine $2^{N-1}$, gde je $1 < k < N - 1$.  Novi grad $t$ koji proglasimo deliće graf na dve komponente sela, $1, \dots, t -1$ i $t+1, \dots, N$. Najveća izolovanost dobija se dužom od dve rute: one od $1$ do $t$ i one od $N$ do $t$. Ako je $t  > k$, onda je prva ruta duža (jer sadrži put dužine $2^{N-1}$, u suprotnom je druga ruta duža.

	Ukoliko biramo $t > k$, cilj je da minimizujemo dužinu prve rute, pa želimo što manje $t$. Ukoliko biramo $t \leq k$, želimo da minimizujemo dužinu druge rute, pa biramo što veće $t$. Drugim rečima, $t$ će uvek biti ili $k$ ili $k + 1$. Izbor između ova dva sela zavisi od dužina ruta $1 \to 2 \to ... \to k$ i $N \to N - 1 \to ... \to k + 1$, jer granu $k$ želimo da spojimo sa kraćom od ove dve rute. Njihove dužine mogu se lako uporediti prema tome gde se nalazi grana dužine $2^{N-3}$.

	Posmatrajmo sada slučaj $K \geq 1$. Rešenje lako sledi iz ranije navedenih zaključaka. Ponovo ćemo imati uzastopne intervale sela. U svakom intervalu možemo ignorisati put najveće dužine. Kako ne bismo koristili ni drugi najduži put, moramo proglasiti gradom bilo koje selo između prvog i drugog najdužeg puta u tom intervalu. Dakle, izolovanost celog grafa ponovo zavisi od treće najduže grane nekog intervala, kao i od druge najduže grane svih ostalih intervala. Biramo onaj interval sa najvećom vrednosti dužine druge najduže grane.

	Vremenska složenost: $O(N)$

	## Podzadatak 3: $K=1,Q=1$

	Posmatrajmo minimalno razapinjuće stablo datog grafa. Neka je grana $u - v$ u grafu, a nije u stablu. Ona ima težinu veću od svih grana na ruti od $u$ do $v$ u stablu, a pošto su sve težine različiti stepeni dvojke, ona ima i težinu veću od sume težina svih tih grana. Prema tome, ne može učestvovati ni u jednoj najkraćoj ruti između dva čvora, pa je za izolovanost potrebno razmatrati samo grane na minimalnom razapinjućem stablu.

	Možemo posmatrati grad kao koren stabla. Ponovo nam je želja da eliminišemo najtežu granu u stablu. Ovo omogućavamo proglašavanjem bilo kog sela u podstablu ispod te grane. Sada nam problem predstavlja druga najteža grana. Ukoliko je ona van tog podstabla, nebitno je koji čvor u podstablu biramo za grad, jer ne utiče na maksimalnu izolovanost. Ukoliko ipak jeste u podstablu, važi, kao i ranije, da je optimalno proglasiti jedan od čvorova na krajevima te grane. Između ta dva čvora izbor zavisi od najteže grane u njihovim odgovarajućim podstablima.

	Vremenska složenost: $O (N + M)$

	## Podzadatak 4: $Q=1$

	Ukoliko je $K = 0$, nađemo minimalno razapinjuće stablo, u njemu najtežu granu, i istim postupkom kao ranije biramo koji od dva čvora na njenim krajevima proglašavamo za grad.

	U slučaju $K \geq 2$, potrebno je iz svakog sela naći najkraću rutu do njegovog najbližeg grada. Sve te rute zajedno čine šumu, tj. skup stabala u kom svako stablo ima tačno jedan grad, koji predstavlja njegov koren.

	Ova šuma se može dobiti malom modifikacijom Kruskalovog algoritma za konstrukciju minimalnog razapinjućeg stabla, ukoliko primetimo da tokom konstrukcije nema razloga spajati dve komponente koje obe sadrže grad. Naime, svakom čvoru u obe komponente je već dodeljen najbliži grad, pa spajanjem tih komponenti ne dobijamo ništa. Kao što je pokazano u prethodnom podzadatku, grane van minimalnog razapinjućeg stabla ne učestvuju u najkraćim rutama, te se ovim algoritmom država korektno deli na povezane komponente.

	Proglašavanjem novog grada dobićemo novu povezanu komponentu sa korenom u tom gradu. Primetimo da, zbog svojstva da su težine grana različiti stepeni dvojke, novu komponentu će činiti čvorovi iz tačno jedne stare. Preciznije, ti čvorovi su iz komponente u kojoj se nalazio taj grad pre proglašavanja. Dakle, proglašavanjem novog grada sečemo jednu komponentu na dve, pa rešenje možemo naći na sličan način kao u prethodnom podzadatku, samo što umesto celog stabla posmatramo onu komponentu koja sadrži najtežu granu.

	Vremenska složenost: $O (N + M)$

	## Podzadatak 5: $N, Q \leq 1000$

	Ovaj podzadatak je namenjen rešenjima zadatka koja ne uspevaju da neki od koraka urade u potkvadratnoj vremenskoj složenosti.

	## Glavno rešenje

	Primetimo da za svaki grad koji proglasimo, možemo eliminisati najtežu granu tačno jednom. Dakle, pomoću $Q$ proglašavanja možemo eliminisati $Q$ najtežih grana date razapinjuće šume. Izbrišimo te grane i posmatrajmo novodobijene komponente. Postojaće tačno $Q$ novih komponenti bez grada, u kojima treba proglasiti neko selo.

	Posmatrajmo novu najtežu granu. Ukoliko je ona u komponenti koja već ima grad, nebitno je gde ćemo proglasiti $Q$ novih gradova (dok god su u odgovarajućim komponentama). Ukoliko je u komponenti koja nema grad, ponovo je potrebno birati između dva čvora na krajevima te grane, na isti način kao u ranijim rešenjima. Što se tiče ostalih komponenti, gradove možemo proglasiti bilo gde u njima.

	Što se tiče implementacije rešenja, nije neophodno konstruisati celu šumu Kruskalovim algoritmom i nakon toga brisati grane. Nama je poznato da će šuma sadržati $N - max(K, 1)$ grana, te da će nakon brisanja Q grana imati $N - K - Q$. Dakle, dovoljno je vršiti samo $N - K - Q$ dodavanja grana. Dalje, tokom rada algoritma možemo za svaku komponentu pamtiti trenutnog kandidata za grad, kao i najtežu granu u njoj. Kod komponenti koje imaju predodređen grad, to je i kandidat, a za komponente bez njega računamo optimalnog kandidata tokom rada algoritma. Kada spajamo dve komponente i jedna od njih već ima predodređen grad, dodeljujemo ga i njihovoj uniji. Ukoliko nijedna nema predodređen grad, optimalan kandidat u njihovoj uniji je onaj od dva čvora na povezujućoj grani koji pripada komponenti sa većom najtežom granom.

	Vremenska složenost: $O(N + M)$

	[Izvor analize i autorskih podataka](https://algora.petlja.org/t/2025-2026/9654/2).

	``` cpp title="gradovi.cpp" linenums="1"
	#include <bits/stdc++.h>
	#define maxn 200005
	using namespace std;

	vector<int> comp[maxn];
	int me[maxn];
	int nd[maxn];
	int cc[maxn];
	int sl[maxn];

	void Gradovi(int N, int M, int K, int Q, int* U, int* V, int* G, int* S)
	{
	    int cnt = N - K;
	    for(int i=1;i<=N;i++){
	        comp[i].push_back(i);
	        me[i]=0;
	        cc[i]=i;
	        nd[i]=i;
	    }
	    for(int i=1;i<=K;i++){
	        sl[G[i]]=1;
	    }
	    for(int i=1;i<=M && cnt>Q;i++){
	        int x=U[i];
	        int y=V[i];
	        if(cc[x] == cc[y]) continue;
	        int p=cc[x];
	        int q=cc[y];
	        if(comp[q].size() > comp[p].size()) {
	            swap(p,q);
	            swap(x,y);
	        }
	        if(sl[p] == 0 || sl[q] == 0) cnt--;
	        for(auto z:comp[q]){
	            comp[p].push_back(z);
	            cc[z]=p;
	        }
	        if(me[q]>me[p]) {
	            nd[p]=y;
	        }
	        else {
	            nd[p]=x;
	        }
	        me[p]=i;
	        sl[p]+=sl[q];
	        comp[q].clear();
	    }
	    for(int i=1;i<=N;i++){
	        if(cc[i] == i && sl[i] == 0)
	        {
	            S[cnt] = nd[i];
	            cnt--;
	        }
	    }
	}
	```
