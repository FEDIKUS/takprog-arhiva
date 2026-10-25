---
hide:
  - toc
---

# 1 - Prodaja

=== "Zadatak"

	| Vremensko ograničenje | Memorijsko ograničenje |
	|:-:|:-:|
	| 1000ms | 64MB |

	Luka je prodavac u radnji misterioznih kutija. Njegova strategija prodaje je neobična: umesto da na svaku kutiju zalepi fiksnu cenu, on pogađa koliko je mušterija spremna da plati, nadajući se da će pogoditi cenu dovoljno nisku da mušterija prihvati, ali i dovoljno visoku da ostvari što veću zaradu.

	Danas je u radnju ušla mušterija spremna da za kutiju plati neki tajni iznos $X$, gde je $X$ ceo broj iz skupa $\{1, 2, \ldots, N\}$. Luka ne zna tačnu vrednost $X$, ali zna način na koji će mušterija izabrati svoju vrednost: nasumično! U radnji se nalazi kutija sa $N$ papirića sa predloženim cenama. Na svakom papiriću se nalazi jedan broj iz skupa $\{1, 2, \ldots, N\}$, a Luka, kao mudar trgovac, zna koliko ima papirića na kojima je napisan svaki broj. Obeležimo sa $A_i$ (gde je $1 \leq i \leq N$) broj papirića gde je napisan broj $i$ u kutiji. Mušterija će papirić izvući bez gledanja, te je šansa da bilo koji od $A_1 + A_2 + \ldots + A_N$ papirića bude izvučen podjednaka.

	Luka mušteriji može da predloži najviše $K$ cena. Svaki predlog $Y \in \{1, \ldots, N\}$ troši jedan od njegovih $K$ pokušaja:

	 - Ako je $Y \leq X$: mušterija prihvata ponudu, Luka zarađuje $Y$ dinara, i kupoprodaja je završena.
	 - Ako je $Y > X$: mušterija odbija (Luka to vidi) i može da predloži novu cenu ukoliko mu je ostalo još pokušaja.

	Ako Luka iscrpi svih $K$ pokušaja bez prihvaćene ponude, zarada mu je $0$. Luka igra optimalno, tako da maksimizuje očekivanu zaradu.

	Pomozite Luki da izračuna optimalnu očekivanu zaradu.

	## Opisi funkcija

	Potrebno je da implementirate funkciju

	- $Prodaja(N, K, A[\ldots])$.

	Ova funkcija će biti pozvana jednom po primeru. $N$ predstavlja dužinu opsega za cene, a $K$ predstavlja broj dozvoljenih pokušaja. Niz od $N$ nenegativnih celih brojeva $A_1, A_2, \ldots, A_N$ predstavlja brojeve papirića sa napisanim brojevima $1, 2, \ldots, N$ respektivno.

	Za fiksiranu strategiju prodavca i za svaku moguću vrednost $X = i$, neka je $z_i$ zarada koju prodavac ostvari u slučaju da je kupčeva nepoznata vrednost upravo $i$ (vrednosti $z_i$ zavise od izabrane strategije). Funkcija treba da vrati maksimalnu vrednost zbira

	$$S = A_1 \cdot z_1 + A_2 \cdot z_2 + \dots + A_N \cdot z_N,$$

	posmatrano preko svih mogućih strategija prodavca. Može se pokazati da je ovaj maksimum uvek nenegativan ceo broj.

	## Primer

	### Ulaz

	Neka je $N = 5$, $K = 2$, i $A = [1, 1, 1, 1, 1]$. Funkcija treba da vrati $12$, zbog sledećeg objašnjenja.

	### Objašnjenje primera

	Jedna od optimalnih strategija: Luka prvo predlaže $Y = 4$. Ako kupac odbije, u drugom pokušaju predlaže $Y = 2$.

	Time za svaku vrednost $X = i$ dobijamo zaradu $z_i$:

	- $X = 1$: oba predloga su odbijena, $z_1 = 0$.
	- $X = 2$ ili $X = 3$: prvi predlog je odbijen, drugi prihvaćen, $z_2 = z_3 = 2$.
	- $X = 4$ ili $X = 5$: prvi predlog je prihvaćen, $z_4 = z_5 = 4$.

	Zbir za ovu strategiju je $S = 1 \cdot 0 + 1 \cdot 2 + 1 \cdot 2 + 1 \cdot 4 + 1 \cdot 4 = 12$, i može se pokazati da je to maksimalna moguća vrednost.

	## Ograničenja

	Označimo sa $D$ sumu svih elemenata niza $A$.

	- $1 \leq N \leq 5000$
	- $0 \leq K \leq 10^9$
	- $1 \leq D \leq 10^9$
	- $0 \leq a_i \leq D$ i $\sum_{i=1}^{N} a_i = D$

	Test primeri su odvojeni u $6$ disjunktnih grupa:

	- U test primerima vrednim **10** poena: $K = 1$ i $A_1 = A_2 = \cdots = A_N$
	- U test primerima vrednim **10** poena: $K = 2$ i $A_1 = A_2 = \cdots = A_N$
	- U test primerima vrednim **10** poena: $K = 1$
	- U test primerima vrednim **25** poena: $N \leq 200$, $K \leq N$
	- U test primerima vrednim **35** poena: $K \leq N$
	- U test primerima vrednim **10** poena: bez dodatnih ograničenja

	## Detalji implementacije

	Potrebno je da pošaljete tačno jedan fajl `prodaja.cpp` koji implementira pomenutu funkciju. Osim tražene funkcije, vaš fajl može sadržati i dodatne globalne promenljive, pomoćne funkcije i dodatne biblioteke.

	Vaša funkcija mora biti sledećeg oblika:

	`long long Prodaja(int N, int K, int* A);`

	**Niz $A$ je indeksiran od 1.**

	Vašim programima je dozvoljeno da menjaju sadržaj nizova, ali ne smeju da pristupaju van granica datih nizova.

	Uz zadatak, obezbeđen vam je `template` fajl `code.cpp`, koji možete koristiti i menjati po potrebi. Takođe vam je obezbeđen program `grader.cpp`, koji služi da lakše testirate kodove.

	Ovaj program učitava sa standardnog ulaza sledeće podatke:

	- U prvom redu brojeve $N$ i $K$.
	- U drugom redu $N$ brojeva: $A[i]$.

	Zatim ovaj program poziva vašu funkciju i ispisuje vrednost $Prodaja(N, K, A)$ u jedinom redu izlaza.

	[Test primeri i prateći fajlovi sa zvaničnog takmičenja](https://nyc3.digitaloceanspaces.com/takprog/2025-26/2025-2026-sio-problems.zip).

=== "Rešenje"

	| Autor | Tekst i test primeri | Analiza rešenja | Testiranje |
	|:-:|:-:|:-:|:-:|
	| Vladimir Milenković | Vladimir Milenković | Marko Milenković | Uroš Kostadinović i Marko Milenković |

	## Rešenje kada je $K = 1$

	Ako Luka ima samo jedan pokušaj, onda je dovoljno da proba svaku moguću cenu.

	Ako ponudi cenu $Y$, mušterija će prihvatiti ponudu ako je $X \geq Y$. Broj papirića koji dovode do prihvatanja ponude je:

	$$
	A_Y + A_{Y+1} + \ldots + A_N
	$$

	Zato je očekivana zarada, pomnožena sa $D$, jednaka:

	$$
	Y \cdot (A_Y + A_{Y+1} + \ldots + A_N)
	$$

	Dakle, dovoljno je proći kroz sve vrednosti $Y$ i uzeti maksimum.

	U slučaju kada su sve vrednosti $A_i$ jednake, ovo se svodi na traženje maksimuma izraza:

	$$
	Y \cdot (N - Y + 1)
	$$

	što rešava prvi podzadatak.

	## Rešenje za male vrednosti $N$ i $K$

	Primetimo šta se dešava nakon što Luka ponudi cenu $Y$.

	Ako mušterija prihvati ponudu, prodaja se završava i Luka zarađuje $Y$ dinara. Ako je odbije, Luka sada sigurno zna da važi $X < Y$. To znači da se posle odbijene ponude problem svodi na isti problem, ali samo nad vrednostima $1,2,\ldots,Y-1$ i sa jednim pokušajem manje.

	Ovo nas prirodno dovodi do dinamičkog programiranja.

	Neka je:

	$$
	P_i = A_1 + A_2 + \ldots + A_i
	$$

	i neka je $dp[t][r]$ najveća moguća zarada pomnožena sa $D$, ako znamo da je $X \leq r$ i ako Luka ima još $t$ pokušaja.

	Ako kao prvu cenu ponudimo $Y$, gde je $1 \leq Y \leq r$, onda dobijamo:

	* za sve vrednosti $X \in [Y,r]$ mušterija prihvata ponudu, pa je doprinos
	  $$
	  Y \cdot (P_r - P_{Y-1})
	  $$

	* za sve vrednosti $X < Y$ ponuda je odbijena i ostaje nam problem sa $t-1$ pokušaja nad prefiksom $1,\ldots,Y-1$, pa je doprinos
	  $$
	  dp[t-1][Y-1]
	  $$

	Zato važi rekurencija:

	$$
	dp[t][r] =
	\max_{1 \leq Y \leq r}
	\left(
	Y \cdot (P_r - P_{Y-1}) + dp[t-1][Y-1]
	\right)
	$$

	Početno je:

	$$
	dp[0][r] = 0
	$$

	jer bez preostalih pokušaja Luka ne može ništa da zaradi.

	Ovo rešenje radi u složenosti:

	$$
	O(KN^2)
	$$

	i dovoljno je za podzadatak $N \leq 200, K \leq N$. Takođe, podzadatak $K=2$ i jednaka raspodela može se rešiti istom idejom, samo sa manjim brojem stanja.

	## Ključno zapažanje za optimizaciju

	Pogledajmo rekurenciju:

	$$
	dp[t][r] =
	\max_{1 \leq Y \leq r}
	\left(
	Y \cdot (P_r - P_{Y-1}) + dp[t-1][Y-1]
	\right)
	$$

	Sredimo izraz:

	$$
	dp[t][r] =
	\max_{1 \leq Y \leq r}
	\left(
	Y \cdot P_r + dp[t-1][Y-1] - Y \cdot P_{Y-1}
	\right)
	$$

	Za fiksirano $t$ i fiksirano $Y$, izraz je linearna funkcija po $P_r$:

	$$
	f_Y(x) = Y \cdot x + dp[t-1][Y-1] - Y \cdot P_{Y-1}
	$$

	Dakle, za svako $Y$ imamo jednu pravu, a za svako $r$ treba da nađemo maksimum vrednosti tih pravih u tački:

	$$
	x = P_r
	$$

	Ovo je klasična primena Convex Hull Trick-a.

	## Zašto je Convex Hull Trick jednostavan u ovom zadatku?

	Prave dodajemo redom po $Y$.

	Pošto je koeficijent uz $x$ jednak $Y$, nagibi pravih se dodaju u rastućem redosledu.

	Sa druge strane, upiti se rade za vrednosti:

	$$
	P_1, P_2, \ldots, P_N
	$$

	a ovaj niz je neopadajući, jer su svi $A_i \geq 0$.

	Zato možemo koristiti deque verziju Convex Hull Trick-a:

	* prave dodajemo u redosledu rastućih nagiba,
	* upite postavljamo u neopadajućem redosledu $x$,
	* beskorisne prave izbacujemo sa kraja,
	* tokom upita pomeramo pokazivač sa početka dok sledeća prava daje bolju vrednost.

	Na ovaj način svaka prava se doda i izbaci najviše jednom, pa jedan sloj dinamike računamo u $O(N)$.

	## Puno rešenje

	Još treba objasniti šta radimo ako je $K > N$.

	Nakon svake odbijene ponude, Luka mora ponuditi manju cenu da bi ta ponuda uopšte mogla biti prihvaćena. Zato u jednoj partiji ima smisla napraviti najviše $N$ različitih ponuda. Sve preko toga ne može poboljšati rezultat.

	Zato možemo odmah postaviti:

	$$
	K = \min(K, N)
	$$

	Sada koristimo dinamiku iz prethodnog dela i Convex Hull Trick optimizaciju.

	Za svaki broj pokušaja $t$ računamo novi red dinamike iz prethodnog reda. Za svaku moguću cenu $Y$ dodajemo pravu:

	$$
	f_Y(x) = Y \cdot x + dp[t-1][Y-1] - Y \cdot P_{Y-1}
	$$

	a za svaki $r$ pitamo maksimum u tački:

	$$
	x = P_r
	$$

	Tako dobijamo:

	$$
	dp[t][r] = \max_Y f_Y(P_r)
	$$

	Odgovor je:

	$$
	dp[K][N]
	$$

	odnosno optimalna očekivana zarada pomnožena sa $D$.

	## Složenost

	Pošto je $K \leq N$, a svaki sloj dinamike računamo u $O(N)$, ukupna vremenska složenost je:

	$$
	O(NK)
	$$

	odnosno u najgorem slučaju:

	$$
	O(N^2)
	$$

	Memorijska složenost je:

	$$
	O(N)
	$$

	jer je za računanje trenutnog reda dinamike dovoljno čuvati samo prethodni red.

	[Izvor analize i autorskih podataka](https://algora.petlja.org/t/2025-2026/9654/1).

	``` cpp title="prodaja.cpp" linenums="1"
	#include <iostream>
	#include <vector>
	#include <deque>
	using namespace std;
	typedef long long ll;
	const int MAXN = 5002;
	ll p[MAXN], cum_p[MAXN], D;
	ll dp[2][MAXN];

	ll m[MAXN], k[MAXN];
	int START = 0, END = 0;

	bool middle_useless (int a, int b, ll mc, ll kc) {
	    return (k[b] - k[a]) * (mc - m[b]) <= (kc - k[b]) * (m[b] - m[a]);
	}

	void add_line (ll nm, ll nk) {
	    while (END - START >= 2 && middle_useless(END - 2, END - 1, nm, nk)) {
	        END -= 1;
	    }
	    m[END] = nm;
	    k[END] = nk;
	    END += 1;
	}
	ll query_line (ll x) {
	    while (END - START >= 2 && m[START + 1] * x + k[START + 1] >= m[START] * x + k[START]) {
	        START += 1;
	    }
	    return m[START] * x + k[START];
	}

	long long Prodaja (int N, int K, int *A) {
	    K = min(N, K);

	    for (int i = 1; i <= N; i++) {
	        D += A[i];
	        cum_p[i] = D;
	    }

	    // dp[N][K] -> max value we can get knowing that price <= N, K attempts left
	    // dp[N][K] -> cum_p[N] * actual probability[N][K]

	    for (int att = 1; att <= K; att++) {
	        START = 0; END = 0;
	        int curr = att % 2, prev = 1 - curr;
	        for (int bnd = 1; bnd <= N; bnd++) {
	            add_line(bnd, dp[prev][bnd - 1] - bnd * cum_p[bnd - 1]);
	            dp[curr][bnd] = query_line(cum_p[bnd]);
	        }
	    }

	    return dp[K % 2][N];
	}
	```
