---
hide:
  - toc
---

# 6 - Turris inclinata

=== "Zadatak"
	
	| Vremensko ograničenje | Memorijsko ograničenje |
	|:-:|:-:|
	| 1000ms | 256MB |
	
	
	
	Rimsko carstvo je došlo i prošlo, a iza sebe je ostavila mnoge ruševine kojima se ljudi i dan danas dive. Jedna od tih ruševina **nije** krivi toranj u Pizi.  Međutim, arhitektura ove zgrade, koja je inspirisana rimskom, i to što se nalazi na teritoriji današnje Italije je bilo dovoljno da prevari našeg junaka Milojka. Milojko je spremajući se za 18. SIO odlučio da uradi zadatke sa XVIII SIO (senatska informatička olimpijada), a kad je video da su mu ti zadaci preteški, shvatio je da je najbolji način da vežba tako što proba da se popne na dotični krivi toranj.
	
	<br>
	
	Toranj ima $N$ spratova i vrh koji označavamo sa $N+1$, i Milojko kreće da se penje od sprata $X$. Zbog nagiba krivog tornja,  lako je moguće pasti dok se penje. Zato za svaki sprat postoji broj $P[i]$, i važi da ukoliko je Milojku $K$-ti put da pokušava da se popne sa sprata $i$ na sprat $i+1$, on uspe ako i samo ako $P[i]$ deli $K$. Ukoliko ne uspe, on pada na sprat $\max(X,F[i])$. Milojku je cilj, naravno, da se popne na vrh tornja. Svaki pokušaj penjanja jednog sprata traje jednu sekundu (uzrok njegovog padanja sa tornja se može potražiti u njegovoj brzini penjanja).
	
	<br>
	
	Kako se plaši da ne zakasni na 18. SIO, razmatra $Q$ mogućih scenarija za vrednost $X$ za svoju vežbu, i pita se koliko bi mu vremena bilo potrebno da se popne na vrh tornja u tom slučaju. Kako je ovaj broj veliki, potrebno ga je naći po modulu $10^9+7$. S obzirom da ga ne vidite među svojom konkurencijom, izgleda da on sam nije znao da reši ovaj zadatak... 
	
	## Opisi funkcija
	
	Potrebno je da implementirate funkciju
	
	-   $Penjanje(N, Q, P[\ldots],F[\ldots],U[\ldots],O[\ldots])$
	
	Ova funkcija će biti pozvana jednom po primeru. Brojevi $N$, $Q$ predstavljaju broj spratova i broj scenarija. Nizovi $P$ i $F$ dužine $N$ su kao opisani u tekstu zadatka. Niz $U$ je dužine $Q$, i $U[i]$ predstavlja $X$ u $i$-tom scenariju, i vaš odgovor za taj scenario potrebno je da upišete u $O[i]$.
	   **Svi nizovi su indeksirani od 1.**
	
	## Primer
	
	Neka je $N=6$, $Q=2$,  $P=\{4,2,1,2,1,4\}$, $F=\{1,2,1,3,2,5\}$, $U=\{1,4\}$. U prvom slučaju će Milojko krenuti od dna i pokušati da penje spratove u sledećem redosledu $1,1,1,1,2,2,3,4,3,4,5,6,5,6,5,6,5,6,$ nakon čega će se popeti na vrh Tornja, što znači da mu je trebalo $18$ sekundi. U drugom slulaju će posetiti spratove redom $4,4,5,6,5,6,5,6,5,6,$ što znači da će mu trebati $10$ sekundi. Znači vaš program treba da upiše $O=\{18,10\}$.
	## Ograničenja
	
	-   $1 \leq N,Q \leq 300.000$
	-   $1 \leq P[i] \leq 1.000.000.000$
	-   $1 \leq F[i] \leq i$
	-   $1 \leq U[i] \leq N$
	
	## Podzadaci
	
	Test primeri su podeljeni u $5$ podzadatka:
	
	-   **[4 poena]:** $N\le20$, $Q\le 50$, $P[i]=2$
	-   **[11 poena]:** $N\le2.500$, $Q\le 20$
	-   **[17 poena]:** $N\le300.000$, $Q\le 20$
	-   **[32 poena]:** $F[i]\ge i-10$
	-   **[36 poena]:** Nema dodatnih ograničenja
	
	## Detalji implementacije
	
	Potrebno je da pošaljete tačno jedan fajl  `turris_inclinata.cpp`  koji implementira pomenute funkcije. Osim traženih funkcija, vaš fajl može sadržati i dodatne globalne promenljive, pomoćne funkcije i dodatne biblioteke.
	
	Vaša funkcija mora biti sledećeg oblika:
	
	`void Penjanje(int N, int Q, int* P, int* F, int* U,int* O);`
	
	**Vašim programima je dozvoljeno da menjaju sadržaj nizova ali ne smeju da pristupaju van granica datih nizova.**
	
	Uz zadatak, obezbeđen vam je "template" fajl  `code.cpp`  koji možete koristiti i menjati po potrebi. Takođe vam je obezbeđen program  `grader.cpp`  koji služi da lakše testirate kodove. Ovaj program učitava sa standardnog ulaza sledeće podatke:
	
	-   U prvom redu brojevi $N$ i $Q$.
	-   U narednom redu $N$ brojeva: $P[i]$.
	-   U narednom redu $N$ brojeva: $F[i]$.
	-   U narednih $Q$ redova po $1$ broj: $U[i]$.
	
	Zatim ovaj program zove vašu funkciju i ispisuje rezultat koji vaša funkcija vrati.
	
=== "Rešenje"
	
	| Autor | Tekst i test primeri | Analiza rеšenja | Testiranje |
	|:-:|:-:|:-:|:-:|
	| Pavle Martinović | Pavle Martinović | Aleksa Milisavljević | Aleksa Milisavljević |
	
	## Rešenje kada $N\le20$, $Q\le 50$, $P[i]=2$
	U ovom podzadatku možemo da simuliramo proces penjanja na toranj. Složenost $O(Q \cdot 2^N)$.
	
	## Rešenje kada $N\le2.500$, $Q\le 20$
	Primetimo prvo da čim prvi put pređemo neki sprat uspešno, to znači da na svim spratovima do njega imamo $0$ pokušaja po modulu odgovarajućeg sprata. Svaki upit rešavamo nezavisno. Neka je $dp[i]$ potreban ukupan broj pokušaja da pređemo $i$-ti sprat, ukoliko na svim manjim imamo $0$ neuspešnih pokušaja. Tada je $dp[i] = dp[j] + dp[j+1] + ... + dp[i-1]$, gde je $j = max(X, F[i])$. Konačno rešenje je $dp[X] + dp[X+1] + ... + dp[N]$. Složenost ovog rešenja je $O(N^2 \cdot Q)$.
	
	## Rešenje kada je $N\le300.000$, $Q\le 20$
	Svaki upit rešavamo nezavisno. Primetimo da možemo optimizovati rešenje prethodnog podzadatka korišćenjem prefiksnih suma. Složenost ovog rešenja je $O(N \cdot Q)$.
	
	## Rešenje kada je $F[i]\ge i-10$
	Neka je $pref[i] = dp[1] + dp[2] + ... + dp[i]$. Primetimo da je rešenje linearna kombinacija $pref[X-1], pref[X+1], pref[X+2], ..., pref[X+10]$. Možemo da procesiramo vrednosti $X$ opadajuće i ažuriramo koeficijente ove linearne kombinacije. Složenost ovog rešenja je $O(N + Q)$.
	
	## Glavno rešenje
	Primetimo da možemo da simuliramo proces od poslednjeg sprata. Za svaki sprat pamtimo koliko smo puta morali da ga pređemo. Inicijalizujmo ovu promenljivu na $1$ za svaki sprat i označimo je sa $T[i]$. Poslednji sprat moramo da pređemo tačno $T[N] = 1$. Međutim, pošto ćemo napraviti $P[N]-1$ neuspešnih pokušaja, ovo znači da smo sve spratove od $F[N]$ do $N-1$ morali da pređemo barem još $P[N] - 1$ puta više, tj. $T[i]$ se povećava za $P[N] - 1$ za sve $F[N] \leq i \leq N-1$. Prema tome pretposlednji sprat smo morali da pređemo $T[N-1] = 1 + (P[N] - 1)$. Međutim, pošto smo napravili $P[N-1] - 1$ neuspešan pokušaj za svaki uspešan, ovo povećava $T[i]$ za  $T[N-1] \cdot (P[N-1] - 1)$ za $F[N-1] \leq i \leq N-2$. Ovo povećavanje možemo simulirati dodavanjem vrednosti za koliko treba promeniti prefiks na odgovarajući element ili korišćenjem segmentnog stabla. Konačno, odgovor na upit je $T[X] \cdot P[X] + T[X+1] \cdot P[X+1] + ... + T[N] \cdot P[N]$. Ovu sumu možemo efikasno pronaći korišćenjem sufiksnih suma. Složenost ovog rešenja je $O(N + Q)$.
	
	``` cpp title="06_turris_inclinata.cpp" linenums="1"
	#include <bits/stdc++.h>
	#define MOD 1000000007
	#define MAXN 300007
	using namespace std;
	long long val[MAXN], dp[MAXN];
	void Penjanje(int N,int Q,int *P,int *F,int *U,int *O)
	{
	    for(int i=1;i<=N+1;i++) dp[i]=val[i]=0;
	    dp[N]=1;
	    for(int i=N;i>=1;i--)
	    {
	        val[i]=(val[i+1]+P[i]*dp[i])%MOD;
	        dp[i-1]=(dp[i-1]+P[i]*dp[i])%MOD;
	        dp[F[i]-1]=(dp[F[i]-1]+(1+MOD-P[i])*dp[i])%MOD;
	    }
	    for(int i=1;i<=Q;i++) O[i]=val[U[i]];
	}

	```
