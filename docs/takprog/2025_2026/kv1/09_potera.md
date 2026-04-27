---
hide:
  - toc
---

# 9 - Potera

=== "Zadatak"
	
	| Vremensko ograničenje | Memorijsko ograničenje |
	|:-:|:-:|
	| 1000ms | 256MB |
	
	<br>
	
	[Tom i Džeri](https://sr.wikipedia.org/wiki/%D0%A2%D0%BE%D0%BC_%D0%B8_%D0%8F%D0%B5%D1%80%D0%B8) se nalaze u kući žene čije lice ne vidimo. Kuća ima $N$ soba i neke od soba su međusobno povezane usmerenim hodnicima (moguće je ići kroz hodnik samo u određenom smeru).  
	
	<br>
	
	Žena čije lice ne vidimo traži od Toma da uhvati Džerija. Za sobu $i$ ($i = 1,2,\ldots, N$) Tom zna da će dobiti $K_i$ litara mleka ako baš u toj sobi uhvati Džerija. Broj $K_i$ je moguće i negativan, što znači da će Tom izgubiti mleko ako u toj sobi uhvati Džerija (npr. niko ne voli miša u spavaćoj sobi).  
	
	<br>
	
	Tom želi da malo optimizuje ovaj problem, kako je kuća prevelika. Za skup soba $S$ kažemo da je njegov kvalitet jednak sumi mleka koju bi Tom dobio (ili izgubio) ukoliko bi uhvatio Džerija u ovim sobama. Toma interesuje da li postoji skup soba pozitivnog kvaliteta iz kog ne izlazi nijedan hodnik (kako Džeri ne bi imao gde da pobegne). Ukoliko ima više ovakvih skupova, potrebno je pronaći onaj sa najvećim kvalitetom.
	
	<br>
	
	## Opis ulaza
	
	<br>
	
	U prvoj liniji standardnog ulaza dat je jedan prirodan broj $T$ - broj test primera.
	
	<br>
	
	U prve dve linije standardnog ulaza svakog test primera data su dva prirodna broja $N$ i $M$ - broj soba u kući i broj tunela između soba.
	
	<br>
	
	U trećoj liniji standardnog ulaza svakog test primera dato je $N$ celih brojeva - $K_1, K_2, \ldots, K_N$ - koliko litara po sobi Tom može dobiti ako u toj sobi uhvati Džerija.
	
	<br>
	
	U narednih $M$ linija standardnog ulaza test primera, nalaze se po dva prirodna broj - $A_i$ i $B_i$ (za $i = 1,2,\ldots,M$). Oni predstavljaju dve sobe koje su povezane usmerenim hodnikom, tj. moguće je doći od sobe $A_i$ do sobe $B_i$ hodnikom, ali ne i obratno. 
	
	<br>
	
	## Opis izlaza
	
	<br>
	
	Potrebno je ispisati $T$ redova standardnog izlaza. Red $i$ predstavlja ispis za $i$-ti test primer.
	
	Za svaki test primer potrebno je ispisati jedan ceo broj:
	- $-1$ ukoliko ne postoji traženi skup
	- kvalitet traženog skupa (skup pozitivnog kvaliteta iz koga ne ide hodnik, maksimalnog kvaliteta ukoliko ih ima više)
	<br>
	
	
	## Primer 1
	
	<br>
	
	### Ulaz
	
	<br>
	
	```
	1
	5 4
	2 -3 -1 3 2
	0 1
	0 2
	2 3
	4 2
	```
	
	<br>
	
	### Izlaz
	
	<br>
	
	```
	4
	```
	
	<br>
	
	### Primer 2
	
	<br>
	
	#### Ulaz
	
	<br>
	
	```
	1
	4 3
	1 1 -1 -1
	0 2
	0 3
	1 3
	```
	
	<br>
	
	#### Izlaz
	
	<br>
	
	```
	-1
	```
	
	<br>
	
	## Ograničenja
	
	<br>
	
	 - $1 \leq T \leq 10$
	 - $1 \leq N \leq 500$.
	 - $0 \leq M \leq \frac{N(N-1)}{2}$.
	 - Garantuje se da zbirno u svih $T$ test primera važi $0 \leq \sum_{i=1}^T N_i\cdot M_i \leq 1.000.000$
	 - $\mid K_i \mid \leq 2^{10}$ za $i = 1,2,\ldots,N$.
	 - $1 \leq A_i, B_i \leq N$ i $A_i \neq B_i$ za $i = 1,2,\ldots,M$.
	
	<br>
	
	Test primeri su podeljeni u četiri disjunktne grupe:
	 - U test primerima vrednim $28$ poena, važi da nije moguće doći od jedne sobe do druge sobe na više od jednog načina, čak iako bismo ignorisali usmerenost hodnika.
	 - U test primerima vrednim $12$ poena, važi da su vrednosti $K_i$ jednake ili $1$ ili $-1$, za $i = 1,2,\ldots,N$.
	 - U test primerima vrednim $40$ poena, važi da $K_i \neq 0$, za $i = 1,2,\ldots,N$.
	 - U test primerima vrednim $20$ poena, nema dodatnih ograničenja.
	
=== "Rešenje"
	
	| Autor | Tekst i test primeri | Analiza rešenja | Testiranje |
	|:-:|:-:|:-:|:-:|
	| Marko Milenković | Marko Milenković | Marko Milenković | Uroš Kostadinović i Vasilije Novaković |
	
	## Rešenje kada važi da nije moguće doći od jedne sobe do druge sobe na više od jednog načina, čak iako bismo ignorisali usmerenost hodnika
	
	Sobe modelujemo kao čvorove, a hodnike između njih kao usmerene grane. 
	
	Ovo znači da je dati graf usmerena šuma. Ovaj podzadatak onda možemo rešiti dinamičkim programiranjem. Za svako podstablo možemo da čuvamo maksimalnu sumu ako uzmemo ili ne uzmemo. Zatim, nezavisno rešavamo po komponentama i proverimo da li je najbolja suma pozitivna. Ovo je moguće uraditi u složenosti $O(N)$.
	
	
	## Potpuno Rešenje 
	
	
	Zadatak ćemo rešiti algoritmom najvećeg protoka (max-flow). Sobe modelujemo kao čvorove, a hodnike između njih kao usmerene grane. Dodaćemo i veštački izvor i ušće. Za svaki čvor $i$, ukoliko mu je $K_i$ pozitivan, dodamo granu od izvora do $i$ sa kapacitetom $K_i$. Ukoliko mu je $K_i$ negativan, dodajemo granu od $i$ do ušća sa kapacitetom $-K_i$. 
	
	Za svaka dva čvora koja su povezana u grafu, dodajemo tu granu koja ih povezuje i stavljamo joj kapacitet beskonačno (u praksi stavimo neki jako veliki broj, npr. INT32_MAX). Zatim, Ford-Fulkersonovim algoritmom nalazimo najveći protok $f$.
	
	Od sume svih pozitivnih vrednosti $K_i$ oduzimamo $f$. Vrednost koju dobijemo obeležimo sa $X$. Ukoliko je $X$ pozitivno, ispisujemo to kao rešenje, a inače štampamo $-1$.
	
	### Dokaz tačnosti
	
	Ispunjavamo uslov zatvorenosti skupa $S$ sa postojanjem beskonačnih grana. Na osnovu dualnosti između najvećeg protoka i minimalnog preseka (min-cut-max-flow duality), možemo da zaključimo da u minimalnom preseku sigurno se neće naći grana beskonačnog kapaciteta. 
	
	Ukoliko neko pozitivno $K_i$ nije u $S$, onda "plaćamo" tu cenu u preseku, jer se oduzima od svih pozitivnih, pa praktično kao da samo nismo izabrali tu sobu. Ukoliko je neko negativno $K_i$ u $S$, onda njegovu vrednost plaćamo ponovo u preseku, jer doprinosi negativnu vrednost.
	
	``` cpp title="09_potera.cpp" linenums="1"
	///1
	#include <bits/stdc++.h>
	
	using namespace std;
	
	#define int ll
	typedef long long ll;
	typedef long double ld;
	typedef pair<int, int> pi;
	typedef pair<ll, ll> pl;
	typedef vector<int> vi;
	typedef vector<ll> vl;
	typedef vector<double> vd;
	typedef vector<bool> vb;
	typedef vector<char> vc;
	typedef vector<string> vs;
	typedef vector<pi> vp;
	typedef vector<pl> vpl;
	
	
	const int inf = INT32_MAX;
	const int maxn = 512;
	
	// ==================== MAX FLOW (Ford-Fulkerson, DFS) ====================
	
	struct Edge {
	    int to;          // destination node
	    long long cap;   // remaining capacity
	    int rev;         // index of the reverse edge in graph[to]
	};
	
	vector<Edge> graph[maxn];
	bool used[maxn];     // visited array for DFS
	int N_nodes;         // number of nodes currently used in the graph
	
	void init(int n) {
	    // nodes are [0..n-1] plus sink = n and target = n+1
	    N_nodes = n + 2;
	    for (int i = 0; i < N_nodes; ++i) {
	        graph[i].clear();
	        used[i] = 0;
	    }
	}
	
	void add_edge(int from, int to, long long cap) {
	    Edge fwd = {to, cap, (int)graph[to].size()};
	    Edge rev = {from, 0,   (int)graph[from].size()};
	    graph[from].push_back(fwd);
	    graph[to].push_back(rev);
	}
	
	long long dfs(int v, int t, long long f) {
	    if (v == t) return f;
	    used[v] = true;
	    for (auto &e : graph[v]) {
	        if (!used[e.to] && e.cap > 0) {
	            long long ret = dfs(e.to, t, min(f, e.cap));
	            if (ret > 0) {
	                e.cap -= ret;
	                graph[e.to][e.rev].cap += ret;
	                return ret;
	            }
	        }
	    }
	    return 0;
	}
	
	long ff(int s, int t) {
	    long long maxflow = 0;
	    const long long INF_FLOW = (long long)4e18;
	    while (true) {
	        // reset visited
	        for (int i = 0; i < N_nodes; ++i) used[i] = false;
	        long long f = dfs(s, t, INF_FLOW);
	        if (f == 0) break;
	        maxflow += f;
	    }
	    return (long)maxflow;
	}
	
	// ============================ MAIN TEMPLATE ============================
	
	signed main()
	{
	    ios_base::sync_with_stdio(false); 
	    cin.tie(nullptr); 
	    cout.tie(nullptr); 
	    cerr.tie(nullptr);    
	
	
	    int test;
	    cin >> test;
	
	    while(test--){
	        int n, m;
	        cin >> n >> m;
	
	        init(n);
	        int sink = n, target = n+1;
	
	        vi s(n);
	        int sum = 0;
	        for (int i = 0; i < n; ++i){
	            cin >> s[i];
	            if (s[i] >= 0)
	                sum += s[i];
	
	            if (s[i] >= 0)
	                add_edge(sink, i, s[i]);
	            else
	                add_edge(i, target, -1 * s[i]);
	        }
	
	        for (int i = 0; i < m; ++i){
	            int u, v;
	            cin >> u >> v;
	
	            add_edge(u, v, inf);
	        }
	
	        long flow = ff(sink, target);
	
	        sum -= flow;
	
	        if (sum <= 0)
	            cout << "-1\n";
	        else
	            cout << sum << '\n';
	    }
	}

	```
