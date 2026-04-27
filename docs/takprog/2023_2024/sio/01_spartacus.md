---
hide:
  - toc
---

# 1 - Spartacus

=== "Zadatak"
	
	| Vremensko ograničenje | Memorijsko ograničenje |
	|:-:|:-:|
	| 1000ms | 256MB |
	
	Kao što znate, u toku je 18. Senatska Informatička Olimpijada. Konzul Olimpijade ima jedan ozbiljan problem. Naime, takmičar po imenu Spartak je formirao grupu takmičara koji se bune protiv preteških zadataka na takmičenjima! Kako bi sačuvali anonimnost, svaki od $N$ takmičara u grupi je identifikovan jedinstvenim brojem između $1$ i $N$.
	
	Kao demokratsko rešenje, Konzul je odlučio da Spartaka diskvalifikuje sa takmičenja, kako ne bi pravio dalje probleme. Ipak, Spartakova družina je jedna uglavnom jako plemenita grupa takmičara i ukoliko Konzul diskvalifikuje takmičara $i$, takmičar $p[i]$ će ustati i reći "Ja sam Spartak!" - nakon čega Konzul mora diskvalifikovati i njega. Ovaj proces se nastavlja do trenutka kad se ne javi niko ko nije već diskvalifikovan. Mogu da postoje i takmičari za koje se niko ne bi javio i za njih važi $p[i] = 0$.
	
	Konzul je odradio svoj posao i na osnovu tajnih informacija za svakog takmičara $i$ odredio vrednost spartanstva - $s[i]$, koja predstavlja koliko je Konzul siguran da je baš to Spartak (u nekoj mernoj jedinici koja se meri celim brojevima). Dodatno, Konzul je i svakom takmičaru (na osnovu njegovih objava na Algori i Diskordu) odredio vrednost $k[i]$, koja predstavlja koliko bi njihova diskvalifikacija bila kontraverzna.
	
	Vaš zadatak je sada da pomognete Konzulu, tako što ćete izabrati skup takmičara maksimalne zbirne vrednosti spartanstva, čija zbirna kontraverza ne prelazi $K$. Tačno ovaj skup takmičara će biti diskvalifikovan, tako da je neophodno da ne postoji takmičar van skupa, koji bi se javio kao Spartak umesto nekog takmičara koji jeste u skupu.
	
	## Opisi funkcija
	
	Potrebno je da implementirate funkciju
	
	- $MaxSpartanstvo(N, K, p[\ldots], s[\ldots], k[\ldots])$
	
	Ova funkcija će biti pozvana jednom po primeru. Broj $N$ predstavlja broj takmičara, a $K$ najveću dozvoljenu kontroverzu. 
	
	Niz $p$ predstavlja predstavljaju umesto koga bi se $i$-ti takmičar javio, odnosno $p[i] = 0$ ukoliko se ne bi javio ni umesto koga. Niz $s$ predstavlja vrednosti spartanstva, dok niz $k$ predstavlja kontroverznosti takmičara.
	
	Potrebno je vratiti jedan ceo broj, ukupnu vrednost spartanstva izabranog skupa takmičara. 
	
	**Svi nizovi su indeksirani od 1.**
	
	## Primer
	
	Neka je:
	- $N=4$, $K=10$
	- $p=\{0, 1, 1, 2\}$
	- $s=\{2, 2, 5, 10\}$
	- $k=\{3, 2, 1, 5\}$.
	
	Konzul bira skup takmičara $\{1, 2, 4\}$, čija je ukupna kontroverznost $10$, a spartanstvo $14$. Nije moguće dobiti veće spartanstvo sa kontroverznošću najviše $10$.
	
	Potrebno je, dakle, vratiti 14.
	
	## Ograničenja
	
	* $1 \leq N  \leq 2\cdot 200$
	* $0 \leq K \leq 500$
	* $0 \leq p[i] \leq N$, za $i = 1, 2, \ldots, N$
	* $p[i] \neq i$, za $i = 1, 2, \ldots, N$
	* $0 \leq s[i] \leq 1000$, za $i = 1, 2, \ldots, N$
	* $0 \leq k[i] \leq K$, za $i = 1, 2, \ldots, N$
	
	## Podzadaci
	
	Test primeri su podeljeni u $5$ podzadatka:
	
	-   **[6 poena]:** $N \leq 20$
	-   **[3 poena]:** $p[i] = i-1$, za $1 \leq i \leq N$
	-   **[15 poena]:** Svaki takmičar ima nekog drugog takmičara umesto kojeg bi se javio
	-   **[37 poena]:** Ne postoji takmičar koji bi se ponovo javio da je spartak nakon što je diskvalifikovan
	-   **[39 poena]:** Nema dodatnih ograničennja
	
	## Detalji implementacije
	
	Potrebno je da pošaljete tačno jedan fajl  `spartacus.cpp`  koji implementira pomenute funkcije. Osim traženih funkcija, vaš fajl može sadržati i dodatne globalne promenljive, pomoćne funkcije i dodatne biblioteke.
	
	Vaša funkcija mora biti sledećeg oblika:
	
	`int MaxSpartanstvo(int N, int K, int* p, int* s, int* k);`
	
	**Vašim programima je dozvoljeno da menjaju sadržaj nizova ali ne smeju da pristupaju van granica datih nizova.**
	
	Uz zadatak, obezbeđen vam je "template" fajl  `code.cpp`  koji možete koristiti i menjati po potrebi. Takođe vam je obezbeđen program  `grader.cpp`  koji služi da lakše testirate kodove. Ovaj program učitava sa standardnog ulaza sledeće podatke:
	
	- U prvom redu brojevi $N$ i $K$.
	- U drugom redu $N$ brojeva: $p[i]$.
	- U trećem redu $N$ brojeva: $s[i]$.
	- U četvrtom redu $N$ brojeva: $k[i]$.
	
	Zatim ovaj program zove vašu funkciju i ispisuje rezultat koji vaša funkcija vrati.
	
=== "Rešenje"
	
	| Autor | Tekst i test primeri | Analiza rеšenja | Testiranje |
	|:-:|:-:|:-:|:-:|
	| Marko Milenković | Mladen Puzić i Marko Milenković | Marko Milenković | Aleksandar Višnjić |
	
	###  $N \leq 20$
	
	U ovom podzadatku je dovoljno da isprobamo svih $2^N$ mogućih podskupova takmičara. Za svaki mogući podskup proverićmo da li je zbir njihove kontraverze manji od $K$ i da li za svakog takmičara $i$ u tom podskupu važi i da je $p[i]$ (osim kad je $p[i] = 0$) takođe u tom skupu. Među svim podskupovima u kojima to važi uočimo onaj sa najvećim zbirnim spartanstvom i ispišemo tu vrednost.
	
	### $p[i] = i-1$, za $1 \leq i \leq N$
	
	U ovom podzadatku je jasno da ćemo moći da izaberemo samo prvih nekoliko takmičara, da bismo ispunili uslov zatvorenosti (ako izaberemo $i$, moramo da izaberemo i $p[i]$). Tako da je rešenje da sabiramo spartanstva počev od prvog takmičara dokle god je njihova ukupna kontraverza manja od $K$. Na kraju ispišemo zbirno spartanstvo.
	
	
	### Svaki takmičar ima različitog takmičara koji bi se javio na njihovu diskvalifikaciju
	
	U ovom podzadatku je ključno da takmičare posmatramo kao čvorove u usmerenom grafu, a usmerena grana postoji između čvorova $i$ i $p[i]$ za $1 \leq i \leq N$. Kako je $p[1], p[2], \ldots, p[N]$ permutacija brojeva $1,2,\ldots,N$, zaključujemo zapravo da će formiran graf biti unija nekoliko ciklusa. Glavna ideja, koja će služiti i za naredne podzadatke, jeste da ako izaberemo jednog takmičara iz ciklusa, onda moramo da ih izaberemo sve (jer će se ciklično javljati). Stoga, potrebno je uočiti sve cikluse i svaki ciklus "kompresovati" u po jedan čvor (jedan ciklus takmičara možemo posmatrati kao jednog takmičara čija su kontraverza i spartanstvo jednaki zbiru svih takmiara iz ciklusa). Sada zadatak rešavamo kao poznat problem ranca.
	
	### Ne postoji takmičar koji bi se ponovo javio da je spartak nakon što je diskvalifikovan
	
	Ovaj podzadatak je u neku ruku suprotan prethodnom, jer možemo zaključiti da nećemo imati cikluse. Sada imamo usmereno stablo i zadatak rešavamo dinamičkim programiranjem nad stablom. Neka je $dp[i][j]$ rešenje za podstablo čvora $i$, ukoliko je zbirna kontraverza u podstablu $j$. Prelaz će nam zatim biti $$dp[i][j + k[i]] = max(dp[i][j+k[i]], dp[i][j + k[i] - l] + dp[y][l])$$, gde su $y$ sva deca čvora $i$, a $l$ vrednost koju iteriramo od $0$ do $j$. Početno stanje nam je naravno $dp[i][k[i]] = s[i]$.
	
	
	### Rešenje bez dodatnih ograničenja
	
	U ovom podzadatku uklapamo ideje iz prethodna dva. Potrebno je da uočimo sve cikluse i kompresujemo ih u jedan čvor, što npr. možemo uraditi Tardžanovim algoritmom. Zatim primenjujemo dinamičko programiranje iz prethodnoh podzatka.
	
	``` cpp title="01_spartacus.cpp" linenums="1"
	#include <iostream>
	#include <vector> 
	#include <cassert>
	
	using namespace std;
	
	const int MAXN = 201;
	const int MAXK = 501;
	const int INF = 1000000000;
	
	vector<int> adj[MAXN];
	bool in_cycle[MAXN];
	int K, deg_in[MAXN], dp[MAXN][MAXK], s[MAXN], k[MAXN];
	
	void solveDP(int node) {
	    for (int kk = 0; kk < min(K+1, k[node]); kk++) {
	        dp[node][kk] = -INF;
	    }
	    for (int kk = k[node]; kk <= K; kk++) {
	        dp[node][kk] = s[node];
	    }
	    for (auto x : adj[node]) {
	        solveDP(x);
	        for (int kk = K; kk >= 0; kk--) {
	            for (int l = 0; l <= kk; l++) {
	                dp[node][kk] = max(dp[node][kk], dp[node][kk-l] + dp[x][l]);
	            }
	        }
	    }
	
	}
	
	int MaxSpartanstvo(int N, int _K, int p[], int _s[], int _k[]) {
	    K = _K;
	    p[0] = 0;
	    s[0] = 0;
	    k[0] = 0;
	    for (int i = 1; i <= N; i++) {
	        adj[p[i]].push_back(i);
	        deg_in[p[i]]++;
	        in_cycle[i] = true;
	        s[i] = _s[i];
	        k[i] = _k[i];
	    }
	    vector<int> q;
	    for (int i = 1; i <= N; i++) {
	        if (deg_in[i] == 0) {
	            q.push_back(i);
	        }
	    }
	    while (!q.empty()) {
	        int leaf = q.back(); q.pop_back();
	        in_cycle[leaf] = false;
	        deg_in[p[leaf]]--;
	        if (deg_in[p[leaf]] == 0) {
	            q.push_back(p[leaf]);
	        }
	    }
	    for (int i = 1; i <= N; i++) {
	        if (in_cycle[i]) {
	            int cur = i, sumS = 0, sumK = 0;
	            vector<int> neighbours;
	            do {
	                sumS += s[cur];
	                sumK += k[cur];
	                for (auto x : adj[cur]) {
	                    if (!in_cycle[x]) {
	                        neighbours.push_back(x);
	                        p[x] = i;
	                    }
	                }
	                cur = p[cur];
	            } while (cur != i);
	            do {
	                in_cycle[cur] = false;
	                cur = p[cur];
	            } while (cur != i);
	            p[i] = 0;
	            s[i] = sumS;
	            k[i] = sumK;
	            adj[i] = neighbours;
	            adj[0].push_back(i);
	        }
	    }
	
	    solveDP(0);
	    return dp[0][K];
	}

	```
