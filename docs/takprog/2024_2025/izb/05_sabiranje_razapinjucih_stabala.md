---
hide:
  - toc
---

# 5 - Sabiranje razapinjućih stabala

=== "Zadatak"
	
	| Vremensko ograničenje | Memorijsko ograničenje |
	|:-:|:-:|
	| 500ms | 256MB |
	
	Dat je povezan graf sa $N$ čvorova i $M$ grana. Svaka grana ima svoju vrednost, koja je na početku jednaka $0$. Ptičica sa grane nam je šapnula jednu veoma zanimljivu operaciju. Naime, dozvoljeno nam je da izaberemo bilo koje razapinjuće stablo datog grafa, i da svim granama povećamo vrednost za tačno $1$. Kako vrednosti ne bi mogle da postanu prevelike, dat je i broj $K$. Svaki put kada povećamo vrednost neke grane, ukoliko ona postane tačno $K$, vrednost te grane će se vratiti na $0$.
	
	<br>
	
	Razapinjuće stablo grafa od $N$ čvorova definišemo kao skup od $N - 1$ različite grane tog grafa, tako da ukoliko samo njih ostavimo u grafu, postojaće put između svaka dva čvora. Preciznije, dobićemo povezan graf koji će predstavljati stablo.
	
	<br>
	
	Potrebno je naći broj različitih grafova koje možemo dobiti primenom date operacije neograničen broj puta. Dva grafa su različita ukoliko postoji barem jedna grana čija se vrednost razlikuje u prvom i drugom grafu. Kako taj broj može biti velik, potrebno je naći ostatak pri deljenju tog broja sa brojem $10^9 + 7$.
	
	## Opisi funkcija
	
	Potrebno je da implementirate funkciju 
	
	- $Sabiranje(N, M, K, U[\ldots], V[\dots])$
	
	Ova funkcija će biti pozvana jednom po primeru. Broj $N$ predstavlja broj čvorova, $M$ broj grana i $K$ je broj iz teksta zadatka. Nizovi $U$ i $V$  dužine $M$ predstavljaju grane grafa. **Svi nizovi su indeksirani od 1.**
	
	## Primer
	
	Neka je $N = 5, \ M = 5, \ K = 2, \ U = \{1, 2, 3, 4, 5\}, \ V = \{2, 3, 4, 2, 4 \}$. Rešenje za ovaj primer je $8$. Skupovi indeksa grana koje možemo izabrati u jednoj operaciji su: $\{1, 2, 3, 5 \}, \ \{1, 2, 4, 5\}, \ \{1, 3, 4, 5\}$.
	
	## Ograničenja
	
	* $1 \leq N, M \leq 200.000$
	* $2 \leq K \leq 10^{18}$
	* $1 \leq U_i \neq V_i \leq N$
	* graf je povezan
	* nema ponovljenih grana
	
	## Podzadaci
	
	Test primeri su podeljeni u $6$ podzadataka:
	
	-   **[12 poena]:** $M = N$
	-   **[10 poena]:** $K = 2, N \leq 9, M \leq 11$
	-   **[10 poena]:** $K = 2, N \leq 200$
	-   **[24 poena]:** $K = 2$
	-   **[20 poena]:** $N \leq 2.000$
	-   **[24 poena]:** Nema dodatnih ograničenja
	
	## Detalji implementacije
	
	Potrebno je da pošaljete tačno jedan fajl  `sabiranje.cpp`  koji implementira pomenute funkcije. Osim traženih funkcija, vaš fajl može sadržati i dodatne globalne promenljive, pomoćne funkcije i dodatne biblioteke.
	
	Vaša funkcija mora biti sledećeg oblika:
	
	`int Sabiranje(int N, int M, long long K, int* U, int* V);`
	
	**Vašim programima je dozvoljeno da menjaju sadržaj nizova ali ne smeju da pristupaju van granica datih nizova.**
	
	Uz zadatak, obezbeđen vam je "template" fajl  `code.cpp`  koji možete koristiti i menjati po potrebi. Takođe vam je obezbeđen program  `grader.cpp`  koji služi da lakše testirate kodove. Ovaj program učitava sa standardnog ulaza sledeće podatke:
	
	- U prvom redu brojeve $N, M, K$.
	- U narednih $M$ redova po $2$ broja $U[i]$ i $V[i]$.
	
	Zatim ovaj program zove vašu funkciju i ispisuje rezultat koji vaša funkcija vrati.
	
=== "Rešenje"
	
	| Autor | Tekst i test primeri | Analiza rešenja | Testiranje |
	|:-:|:-:|:-:|:-:|
	| Pavle Martinović | Miloš Milutinović | Miloš Milutinović | Nemanja Majski |
	
	Posmatramo sve operacije mod $K$. Nađimo blokove ovog grafa. Naravno, možemo da biramo razapinjuće stablo u svakom bloku nezavisno. Primetimo da postoji način da izaberemo dve grane u istom bloku i jednu povećamo za jedan a drugu smanjimo za $1$. Pošto u jednom bloku za svake dve grane $e_1$ i $e_2$ postoji ciklus koji ih sadrži, možemo da nađemo neko stablo $T$ koje sadrži taj ciklus bez $e_2$ i na njega primenimo operaciju jednom, a na $T - e_1 + e_2$ $K - 1$ puta. Ovo nam kaže da ako nam je fiksirana suma grana u svakom bloku, onda možemo da radimo operacije da sve sem jedne grane možemo proizvoljno izabrati (a poslednja grana je tada fiksirana). Primetimo takođe da za blok veličine $A$, jedna operacija menja sumu u tom bloku za tačno $+(A - 1)$. To znači da ako smo primenili ukupno $t$ $mod$ $K$ puta operaciju, u bloku veličinu $A$ je suma $t \cdot (A-1)$, što uzima ukupno $K / NZD(K, \ A - 1)$ vrednosti. Ali nije baš nezavisno, nego je izbor periodičan sa periodom NZS ovog gore po svim blokovima, što je $K$ $/$ $NZD(K, \ veličina bloka_1 - 1, veličina bloka_2 - 1, \cdots)$. Tako da je odgovor $K ^ {M - broj blokova} \cdot K / NZD(K, \ veličina bloka_1 \ - \ 1, \ veličina bloka_2 \ - \ 1, \cdots)$.
	
	``` cpp title="05_sabiranje_razapinjucih_stabala.cpp" linenums="1"
	#include <bits/stdc++.h>
	
	using namespace std;
	
	const int md = 1e9 + 7;
	
	int add(int x, int y) {
	  return x + y < md ? x + y : x + y - md;
	}
	
	int mul(int x, int y) {
	  return x * 1LL * y % md;
	}
	
	int ckpow(int x, int k) {
	  int y = 1;
	  while (k) {
	    if (k & 1) {
	      y = mul(y, x);
	    }
	    x = mul(x, x);
	    k >>= 1;
	  }
	  return y;
	}
	
	long long GCD(long long a, long long b) {
	  if (b == 0) {
	    return a;
	  } else {
	    return GCD(b, (a % b));
	  }
	}
	
	vector<vector<int>> biconnected_components(const vector<vector<int>> &adj) {
	    int N = adj.size(), timer = 0;
	    vector<int> tin(N), low(N), parent(N);
	    vector<vector<int>> components;
	    stack<int> st;
	
	    auto pop_component = [&](int u) -> void {
	        components.push_back({ u });
	        for (;;) {
	            int v = st.top();
	            st.pop();
	            components.back().push_back(v);
	            if (parent[v] == u) break;
	        }
	    };
	
	    auto dfs = [&](auto &self, int u, int p = -1) -> void {
	        parent[u] = p;
	        tin[u] = low[u] = ++timer;
	        st.push(u);
	        int children = 0;
	
	        for (int v : adj[u]) {
	            if (v == p) continue;
	            if (tin[v]) low[u] = min(low[u], tin[v]);
	            else {
	                self(self, v, u);
	                low[u] = min(low[u], low[v]);
	                if (low[v] >= tin[u] && p != -1)
	                    pop_component(u);
	                ++children;
	            }
	        }
	
	        if (p == -1) {
	            if (children == 0) components.push_back({ u });
	            for (int i = 0; i < children; ++i)
	                pop_component(u);
	            st.pop();
	        }
	    };
	
	    for (int i = 0; i < N; ++i)
	        if (!tin[i]) dfs(dfs, i);
	
	    return components;
	}
	
	int Sabiranje(int N, int M, long long K, int*U, int*V) {
	
	    vector<vector<int>> adj(N);
	    for (int i = 1; i <= M; ++i) {
	        int u = U[i], v = V[i];
	        --u; --v;
	        adj[u].push_back(v);
	        adj[v].push_back(u);
	    }
	
	    auto comps = biconnected_components(adj);
	
	
	    int pw = ckpow(K % md, M - int(comps.size()));
	
	    long long g = K;
	
	    for (auto &comp : comps) {
	      g = GCD(g, int(comp.size()) - 1);
	    }
	
	    g = K / g;
	
	    g %= md;
	
	    return mul(pw, g);
	}

	```
