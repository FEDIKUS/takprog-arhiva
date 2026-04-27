---
hide:
  - toc
---

# A1 - Ekskluzivni Kamp

=== "Zadatak"
	
	| Vremensko ograničenje | Memorijsko ograničenje |
	|:-:|:-:|
	| 1000ms | 256MB |
	
	<br>
	
	Drevni član Komisije Mars ne voli takmičare koji:
	1) su iz Niša
	2) se takođe zovu Marko
	
	Naročito ne toleriše oba istovremeno. Potrebna mu je pomoć kako bi sputao sve one koji ispunjavaju oba uslova.
	
	<br>
	
	Mars vodi $N$ takmičara na kamp, od kojih (nažalost) je $S$ onih koji ispunjavaju uslove i koje želi da sputa. Između takmičara postoji $M$ kanala komunikacije, tako da se informacije mogu prenositi direktno ili preko drugih takmičara.
	
	<br>
	
	Mars želi da isključi što više kanala, ali da sistem komunikacije i dalje omogućava da svaki takmičar može (možda posredno) da komunicira sa svakim drugim. Dodatno, pošto želi da što kasnije dobiju informacije, svaki od $S$ izabranih takmičara mora imati tačno jedan preostao kanal komunikacije (odnosno, može direktno da komunicira samo sa tačno jednim drugim takmičarom preko preostalih kanala).
	<br>
	
	Ako je moguće izabrati takav podskup kanala komunikacije, ispisati skup sa minimalnim brojem kanala komunikacije koji zadovoljava uslov. Ukoliko ima više takvih, ispisati bilo koji. U suprotnom ispisati `-1`.
	
	## Opis ulaza
	
	<br>
	
	U prvoj liniji standardnog ulaza dat je jedan prirodan broj $T$ - broj test primera.
	
	<br>
	
	U prvoj liniji ulaza svakog test primera nalaze se tri broja $N, M, S$.
	
	<br>
	
	U drugoj liniji svakog test primera se nalazi $S$ prirodnih brojeva koji predstavljaju takmičare koje Mars želi da sputa.
	
	<br>
	
	U narednih $M$ linija svakog test primera se nalaze po dva prirodna broja $A_i$ i $B_i$. Ovo označava da postoji direktna linija komunikacije između takmičara $A_i$ i $B_i$.
	
	## Opis izlaza
	
	<br>
	
	Ukoliko ne postoji odgovarajući skup kanala komunikacije, u prvom i jedinom redu standardnog izlaza test primera ispisati `-1`.
	
	Ukoliko postoji, u prvom redu standardnog izlaza test primera ispisati broj izabranih kanala komunikacije $K$.
	
	U narednih $K$ linija standardnog izlaza test primera ispisati po dva prirodna broja $A_i$ i $B_i$, koji označavaju izabrani kanal komunikacije.
	
	Ukoliko ima više rešenja, ispisati bilo koje.
	
	## Primer 1
	
	<br>
	
	### Ulaz
	
	<br>
	
	```
	2 
	5 4 3
	1 4 5
	1 2
	2 3
	3 4
	3 5
	6 5 2
	5 6
	1 2
	3 4
	2 5
	4 6
	5 6
	```
	
	<br>
	
	### Izlaz
	
	<br>
	
	```
	4
	1 2
	2 3
	3 4
	3 5
	-1
	```
	
	<br>
	
	### Objašnjenje 
	
	U prvom primeru, Mars može zadržati sve kanale komunikacije. Na ovaj način svih $S$ takmičara koji su iz Niša i zovu se Marko imaju samo jednog takmičara sa kojim komuniciraju i može se pokazati da ovo nije izvodljivo sa manje kanala. 
	
	U drugom primeru nije moguće izabrati kanale tako da se ispune uslovi zadatka. Kampa neće ni biti.
	
	<br>
	
	## Ograničenja
	
	<br>
	
	 - $1 \leq T \leq 3$
	 - $3 \leq N \leq 100.000$.
	 - $1 \leq M \leq 200.000$.
	 - $1 \leq S \leq N$.
	 - $1 \leq A_i, B_i \leq N$, za sve $i = 1,2,\ldots,M$.
	 - Garantuje se da u ulaznoj konfiguraciji svaka dva takmičara mogu da komuniciraju, potencijalno preko nekih drugih (posrednih) kanala komunikacija.
	
	<br>
	
	Test primeri su podeljeni u šest disjunktnih grupa:
	 - U test primerima vrednim $10$ poena, važi da $N \leq 10, M \leq 20$.
	 - U test primerima vrednim $10$ poena, važi da $S \leq 2$.
	 - U test primerima vrednim $10$ poena, važi da $M = N-1$.
	 - U test primerima vrednim $20$ poena, važi da $S \geq N-2$.
	 - U test primerima vrednim $15$ poena, važi da $N,M \leq 2000$.
	 - U test primerima vrednim $35$ poena, nema dodatnih ograničenja.
	
=== "Rešenje"
	
	| Autor | Tekst i test primeri | Analiza rešenja | Testiranje |
	|:-:|:-:|:-:|:-:|
	| Marko Milenković | Marko Milenković | Marko Milenković | Andrej Ivašković |
	
	### Uvod
	
	Zadatak možemo da modelujemo kao graf. Kako tražimo minimalni podgraf koji je povezan, struktura koju tražimo stablo. 
	
	### $N \leq 10, M \leq 20$
	
	U ovom podzadatku možemo da probamo sve podskupove grana, njih $2^M$ i za svaki odabir grana proverimo da li je podgraf povezan i da li su $S$ čvorovi listovi. Složenost ovog pristupa je $(N+M)2^M$ 
	
	### $S \leq 2$
	
	Ukoliko je $S = 1$, onda je potrebno da povežemo ceo graf bez jednog izabranog čvora. Ukoliko je to moguće, onda samo dodamo granu do tog jednog čvora, inače ne postoji rešenje.
	
	Ukoliko je $S = 2$, fiksiramo jednu granu iz prvog čvora, jednu granu iz drugog čvora. Zatim proverimo da li je graf bez ova dva čvora povezan.
	
	### $M = N - 1$
	
	Kako je graf povezan i ima $N-1$ grana, to znači da je stablo. U ovom slučaju ili je ceo graf zadovoljavajući ili ne postoji rešenje, jer izbacivanje barem jedne grane iz stabla prekida povezanost grafa.
	
	### $S \geq N - 2$
	
	Ukoliko je $S = N - 1$, onda bi trebalo da u razapinjućem stablu da imamo samo jedan čvor koji nije list. Potrebno je samo proveriti da li je ovaj čvor povezan direktno sa svim ostalim. Usputno, ovakav graf se naziva zvezda.
	
	Ukoliko je $S = N - 2$, onda dva čvora koji ne moraju da budu listovi moraju da budu povezani granom i svi ostali čvorovi su direktno povezani na barem jedan od ova dva čvora. Ukoliko nešto od ovoga ne važi, rešenje ne postoji.
	
	### $N, M \leq 2000$
	
	Ovaj podzadatak se rešava identično kao naredni, ali je dozvoljena neoptimalna implementacija rešenja.
	
	
	### Bez dodatnih ograničenja
	
	Ako postoji rešenje, onda je u pitanju razapinjuće stablo i izabrani čvorovi su podskup listova tog stabla. To znači da kada uklonimo svih $S$ čvorova, izabrani podgraf ostaje stablo. Dakle, možemo da izbrišemo iz ulaznog grafa sve specijalne čvorove i proverimo da li je graf povezan. 
	
	
	Vremenska složenost je $O(N+M)$. 
	
	``` cpp title="04_fini_cvorovi.cpp" linenums="1"
	#include <bits/stdc++.h>
	
	using namespace std;
	
	void solve() {
	    int n, m, s;
	    cin >> n >> m >> s;
	    
	    vector<int> S(s);
	    vector<bool> in_s(n + 1, false);
	    for (int i = 0; i < s; ++i) {
	        cin >> S[i];
	        in_s[S[i]] = true;
	    }
	
	    vector<vector<int>> adj(n + 1);
	    for (int i = 0; i < m; ++i) {
	        int u, v;
	        cin >> u >> v;
	        adj[u].push_back(v);
	        adj[v].push_back(u);
	    }
	
	    if (n == 2) {
	        if (m >= 1) {
	            cout << 1 << " " << 2 << "\n";
	        } else {
	            cout << -1 << "\n";
	        }
	        return;
	    }
	
	    if (s == n) {
	        cout << -1 << "\n";
	        return;
	    }
	
	    int start = -1;
	    for (int i = 1; i <= n; ++i) {
	        if (!in_s[i]) {
	            start = i;
	            break;
	        }
	    }
	
	    vector<bool> vis(n + 1, false);
	    vector<int> q;
	    q.push_back(start);
	    vis[start] = true;
	    
	    vector<pair<int, int>> tree_edges;
	
	    int head = 0;
	    int not_s_visited = 1;
	    
	    while (head < (int)q.size()) {
	        int u = q[head++];
	        for (int v : adj[u]) {
	            if (!in_s[v] && !vis[v]) {
	                vis[v] = true;
	                q.push_back(v);
	                tree_edges.push_back({u, v});
	                not_s_visited++;
	            }
	        }
	    }
	
	    if (not_s_visited < n - s) {
	        cout << -1 << "\n";
	        return;
	    }
	
	    for (int i = 0; i < s; ++i) {
	        int u = S[i];
	        bool attached = false;
	        for (int v : adj[u]) {
	            if (!in_s[v]) {
	                tree_edges.push_back({u, v});
	                attached = true;
	                break;
	            }
	        }
	        if (!attached) {
	            cout << -1 << "\n";
	            return;
	        }
	    }
	
	    cout << n-1 << '\n';
	    for (auto edge : tree_edges) {
	        cout << edge.first << " " << edge.second << "\n";
	    }
	}
	
	int main() {
	    ios_base::sync_with_stdio(false); 
	    cin.tie(nullptr); 
	    cout.tie(nullptr); 
	    cerr.tie(nullptr);    
	    
	    int t;
	    cin >> t;
	
	    while (t--) {
	        solve();
	    }
	
	    return 0;
	}

	```
