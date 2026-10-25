---
hide:
  - toc
---

# 5 - Intergalaktički konflikt dva

=== "Zadatak"

	| Vremensko ograničenje | Memorijsko ograničenje |
	|:-:|:-:|
	| 2000ms | 64MB |

	O, ne! Započeo je već drugi po redu konflikt između Nišovaca i Marsovaca! Ovog puta su se umešali i pacifistički orijentisani Baki i Hepiju, starosedaoci Taškenta, kojima su ovi konflikti već dojadili i žele što pre da ga spreče. Pomozite Bakiju i Hepiju da okončaju Intergalaktičke konflikte jednom za svagda tako što ćete predvideti plan napada Marsovaca!

	Ovog puta se bitka odvija u "Spoljašnjem Obodu" na planeti Taškent koja se može predstaviti kao duž dužine $M$. U bitci učestvuje $N$ Nišovaca i $N$ Marsovaca. Svaki od učesnika bitke se na početku nalazi na nekoj celobrojnoj tački duži $\{0,1,\dots M-1\}$. Moguće je da više učesnika bitke bude na istoj tački. Na početku pozicija $i$-tog Marsovca je $A[i]$ a pozicija $i$-tog Nišovca je $B[i]$.

	Marsovci poseduju kolektivnu sposobnost teleportacije koju mogu iskoristiti jednom pre početka napada. Marsovci biraju broj $X$ iz skupa $\{0,1,\dots M-1\}$ nakon čega će pozicija $i$-tog Marsovca postati $A[i]:=(A[i]+X) \text{ mod } M$. Nakon toga svaki od Marsovaca napada tačno jednog Nišovca i nikoja dva Marsovca ne napadaju istog Nišovca. Svaki Marsovac može da se kreće po Taškentu tako što ako je trenutno na poziciji $X$ može da se pomeri na poziciju $(X-1) \text{ mod } M$ ili $(X+1) \text{ mod } M$ i time prelazi distancu $1$. U opštem slučaju, ako Marsovac želi da pređe sa pozicije $p$ na poziciju $q$ minimalna distanca koju mora da pređe će biti jednaka $\text{min}(|p-q|,M-|p-q|)$. Marsovci će napasti tako što će izabrati napad u kome ukupna distanca koju svi Marsovci pređu zajedno bude minimalna. Vaš zadatak je da izračunate kolika je ukupna distanca koju će svi Marsovci preći.

	## Opisi funkcija

	Potrebno je da implementirate funkciju

	-   $Konflikt(N, M, A[\ldots], B[\ldots])$

	Ova funkcija će biti pozvana jednom po primeru. Broj $N$ predstavlja broj Nišovaca i broj Marsovaca. Broj $M$ predstavlja veličinu duži Taškenta. Niz $A$ predstavlja pozicije Marsovaca na početku. Niz $B$ predstavlja pozicije Nišovaca na početku. Ova funkcija treba da vrati ukupnu distancu koju svi Marsovci pređu u napadu.
	   **Svi nizovi su indeksirani od 1.**

	## Primer

	Neka je $N=3$, $M=20$,  $A=\{0,6,2\}$, $B=\{5,19,7\}$. Marsovci biraju $X = 1$ za teleportaciju. Nakon toka pozicije Marsovaca postaju $\{1,7,3\}$. Prvi Marsovac će napasti drugog Nišovca i preći distancu $2$, drugi Marsovac će napasti trećeg Nišovca i preći distancu $0$ i treći Marsovac će napasti prvog Nišovca i preći distancu $2$. Ukupna distanca koju su Marsovci prešli u napadu je $4$.
	## Ograničenja

	-   $1 \leq N\leq 5000$
	-   $1 \leq M \leq 10^9$
	-   $0 \leq A[i] < M$
	-   $0 \leq B[i] < M$

	## Podzadaci

	Test primeri su podeljeni u $8$ podzadatka:

	-   **[5 poena]:** $N \le 10$, $M \le 20$
	-   **[12 poena]:** $N \le 500$, $M \le 500$
	-   **[12 poena]:** $A[i] < \frac{M}{4}$, $B[i] < \frac{M}{4}$
	-   **[23 poena]:** $N \le 500$
	-   **[18 poena]:** Ukupna distanca koju Marsovci pređu biće najviše $10^4$ i $N \leq 2000$
	-   **[30 poena]:** Nema dodatnih ograničenja

	## Detalji implementacije

	Potrebno je da pošaljete tačno jedan fajl  `konflikt.cpp`  koji implementira pomenute funkcije. Osim traženih funkcija, vaš fajl može sadržati i dodatne globalne promenljive, pomoćne funkcije i dodatne biblioteke.

	Vaša funkcija mora biti sledećeg oblika:

	`long long Konflikt(int N, int M, int* A, int *B);`

	**Vašim programima je dozvoljeno da menjaju sadržaj nizova ali ne smeju da pristupaju van granica datih nizova.**

	Uz zadatak, obezbeđen vam je "template" fajl  `code.cpp`  koji možete koristiti i menjati po potrebi. Takođe vam je obezbeđen program  `grader.cpp`  koji služi da lakše testirate kodove. Ovaj program učitava sa standardnog ulaza sledeće podatke:

	-   U prvom redu broj $N$.
	-   U narednom redu $N$ brojeva: $A[i]$.
	-   U narednom redu $N$ brojeva: $B[i]$.

	Zatim ovaj program zove vašu funkciju i ispisuje rezultat koji vaša funkcija vrati.

	[Test primeri i prateći fajlovi sa zvaničnog takmičenja](https://nyc3.digitaloceanspaces.com/takprog/2025-26/2025-2026-sio-problems.zip).

=== "Rešenje"

	| Autor | Tekst i test primeri | Analiza rešenja | Testiranje |
	|:-:|:-:|:-:|:-:|
	| Uroš Kostadinović | Uroš Kostadinović | Toni Škrijelj | Toni Škrijelj |

	## Podzadatak 1: $N \le 10$, $M \le 20$

	Pošto su i $N$ i $M$ mali, možemo da isprobamo sve mogućnosti.

	Za svako $X \in \{0,1,\dots,M-1\}$ računamo nove pozicije Marsovaca
	$A'[i] = (A[i] + X) \bmod M$.
	Zatim za fiksirano $X$ rešavamo optimalno pariranje Marsovaca i Nišovaca DP-om po bitmasci:
	$dp[\text{mask}]$ je minimalna cena kada su već upareni Nišovci iz `mask`,
	a sledeći Marsovac je određen brojem postavljenih bitova.

	Cena jednog para je ciklusna distanca
	$\min(|p-q|, M-|p-q|)$.

	Ukupna složenost:
	$O(M \cdot 2^N \cdot N)$.

	## Podzadatak 2: $N \le 500$, $M \le 500$

	Ključna opservacija: kada sortiramo pozicije Marsovaca i Nišovaca, optimalno pariranje je ciklusni pomak jednog sortiranog niza u odnosu na drugi.
	Dakle, dovoljno je probati sve pomake $t \in [0, N)$.

	U ovom podzadatku možemo i dalje probati svako $X \in [0, M)$.
	Za fiksirane $X$ i $t$ cenu računamo u $O(N)$.

	Ukupno:
	$O(M \cdot N^2)$, što prolazi za date granice.

	## Podzadatak 3: $A[i] < M/4$, $B[i] < M/4$

	Pošto su sve tačke u prvoj četvrtini kruga, možemo posmatrati da nema „prelaska preko nule“.
	Tada je problem isti kao na pravoj.

	Za svaki pomak $t$ definišemo:
	$D_i = A_i - B_{(i+t)\bmod N}.$

	Za fiksiran $t$ treba minimizovati:
	$\sum_i |D_i - X|.$
	Ovo je klasičan oblik, minimum se postiže za medijanu niza $D$.

	Zato:
	1. formiramo $D$,
	2. sortiramo ga,
	3. uzmemo medijanu,
	4. izračunamo sumu apsolutnih odstupanja.

	Uzimamo minimum po svim $t$.

	Složenost:
	$O(N^2 \log N)$.

	## Podzadatak 4: $N \le 500$

	Sada moramo potpuno korektno obraditi krug.
	Rešenje je proširenje prethodne ideje.

	Za fiksni pomak $t$:
	1. računamo
	   $D_i = (A_{(i+t)\bmod N} - B_i) \bmod M,\quad D_i \in [0,M),$
	2. sortiramo $D$,
	3. pravimo udvostručeni niz
	   $E = D \cup (D+M),$
	4. gledamo sve prozore dužine $N$ u $E$.

	Svaki prozor predstavlja izbor „sa koje strane kruga“ ide svaki element.
	Za prozor je optimalni $X$ njegova medijana.
	Cenu prozora računamo preko prefiksnih suma u $O(1)$.

	Ukupno:
	$O(N^2 \log N)$ (sortiranje po svakom $t$).

	## Podzadatak 5: ukupna distanca $\le 10^4$ i $N \le 2000$

	Ovaj podzadatak takođe rešava algoritam iz podzadatka 4.

	Praktična optimizacija: čuvamo trenutni najbolji odgovor kao gornju granicu.
	Pri računanju trenutne cene, čim parcijalna suma pređe tu granicu, možemo prekinuti tu granu.
	Pošto je garantovano da je odgovor mali, ovo značajno ubrzava rad u praksi.

	## Podzadatak 6: bez dodatnih ograničenja (glavno rešenje)

	Glavno rešenje je isti pristup kao u podzadatku 4:
	- sortiranje $A$ i $B$,
	- prolaz po svim pomacima $t$,
	- konstrukcija $D$, zatim $E = D \cup (D+M)$,
	- minimum po prozorima dužine $N$ uz medijanu i prefiksne sume.

	Složenost je:

	$ O(N^2 \log N) $

	što je dovoljno za $N \le 5000$ uz pažljivu implementaciju.

	[Izvor analize i autorskih podataka](https://algora.petlja.org/t/2025-2026/9654/5).

	``` cpp title="konflikt-sol.cpp" linenums="1"
	#include <bits/stdc++.h>

	using namespace std;

	const long long inf = 1000000000000000LL;
	const long long mx = 4000000000;
	int n;
	long long m;
	const int maxn = 5005;
	long long a[maxn],b[maxn];
	long long c[2*maxn];
	long long ps[2*maxn];

	long long sum(int l,int r){
	    return l==0?ps[r]:ps[r]-ps[l-1];
	}
	long long get(int l,int r){
	    int mid = (l+r)/2;
	    if(n%2==0){
	        return sum(mid+1,r)-sum(l,mid);
	    }
	    return sum(mid+1,r) - sum(l,mid-1);
	}

	long long Konflikt(int N,int M,int *A,int *B){
	    n = N,m = M;
	    for(int i = 0;i<n;i++) a[i] = A[i+1];
	    for(int i = 0;i<n;i++) b[i] = B[i+1];
	    sort(a,a+n);
	    sort(b,b+n);
	    long long ans = inf;
	    for(int t = 0;t<n;t++){
	        for(int i = 0;i<n;i++)  c[i] = (m+a[(i+t)%n]-b[i])%m;
	        sort(c,c+n);
	        for(int i = 0;i<n;i++) c[i+n] = c[i]+m;
	        ps[0] = c[0];
	        for(int i = 1;i<2*n;i++) ps[i] = ps[i-1] + c[i];
	        for(int i = n-1;i<2*n;i++){
	            ans = min(ans,get(i-n+1,i));
	        }
	    }
	    return ans;
	}
	```
