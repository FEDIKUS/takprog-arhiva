---
hide:
  - toc
---

# 5 - Viae Romanae

=== "Zadatak"
	
	| Vremensko ograničenje | Memorijsko ograničenje |
	|:-:|:-:|
	| 1000ms | 256MB |
	
	Drevna poslovica kaže:
	
	<br>
	
	                                                     "Svi putevi vode u Rim."
	
	<br>
	
	Ono što je poznato tek nekolicini je poreklo ove izreke. Čitanje ovog zadatka vam neće nimalo pomoći da se nađete u toj privilegovanoj grupi. 
	
	<br>
	
	Rimsko carstvo ima $N$ gradova i $M$ **neusmerenih** puteva. Od njih, $i$-ti put je između gradova $U[i]$ i $V[i]$ i ima dužinu $W[i]$. Rim je, kao prestonica, označen sa rednim brojem $1$. Garantuje se da je iz Rima moguće stići do bilo kog drugog grada. 
	
	<br>
	
	Braća Romul i Rem žive u Rimu (tj. gradu sa indeksom $1$). Nažalost, ova braća su u svađi. Zato su odlučili da svako treba da krene svojim putem. Romul želi da stigne u grad $X$, a Rem želi da stigne u grad $Y$. Kako žele da što pre stignu do svojih odredišta, obojica će izabrati najkraći put. Međutim, pošto su u zavadi, oni bi po svaku cenu želeli da izbegnu međusobne susrete. 
	
	Zato su odlučili da unapred dogovore plan puta, tako da obojica stignu do svojih odredišta najkraćim putem, a da se u preseku njihovih puteva nalazi **što je manje moguće različitih gradova**. Primetite da je u preseku uvek barem $1$ grad (sam Rim).
	
	<br>
	
	Istorija je zabeležila čak $Q$ svađa između Romula i Rema! Za svaku odgovorite na pitanje koliko će se gradova nalaziti u preseku, ukoliko optimalno dogovore puteve kojima će se kretati.
	
	## Opisi funkcija
	
	Potrebno je da implementirate funkciju
	
	-   $Putevi(N, M, Q, U[\ldots], V[\ldots], W[\ldots], X[\ldots], Y[\ldots], Ans[\ldots])$
	
	Ova funkcija će biti pozvana jednom po primeru. Brojevi $N$, $M$, $Q$ predstavljaju broj gradova, broj puteva i broj svađa. Nizovi $U$, $V$ i $W$ dužine $M$ su kao opisani u tekstu zadatka. Nizovi $X$ i $Y$ su dužine $Q$, i $X[i]$ predstavalja grad u koji Romul želi da stigne tokom $i$-te svađe, dok $Y[i]$ predstavlja grad u koji Rem želi da stigne tokom $i$-te svađe. Vaš odgovor za tu svađu treba da upišete u $Ans[i]$.
	   **Svi nizovi su indeksirani od 1.**
	
	## Primer
	
	Neka je $N=4$, $M=5$, $Q=3$,  $U=\{1,2,2,1,4\}$, $V=\{2, 3, 4, 3, 3\}$, $W=\{2, 3, 5, 5, 4\}$, $X = \{2,3,2\}$, $Y=\{4,4,2\}$. Tokom prve svađe, Romul želi da stigne u grad $2$, dok Rem želi da stigne u grad $4$. Najkraći put od Rima do grada $2$ je jedinstven i to je $1 - 2$. Najkraći put od Rima do grada $4$ je takođe jedinstven i to je $1 - 2 - 4$. U preseku ova dva puta su dva grada, grad $1$ i grad $2$. Tokom druge svađe, Romul želi da stigne u grad $3$, dok Rem želi da stigne u grad $4$. Ovaj put će Romul izabrati put $1 - 3$, dok će Rem izabrati put $1 - 2 - 4$. U preseku ova dva puta je jedan grad, Rim. Tokom treće svađe, obojica žele da stignu u grad $2$. Obojica će izabrati isti put, $1 - 2$. Prema tome, srešće se ukupno dva puta, u gradu $1$ i u gradu $2$. Konačno $Ans=\{2,1,2\}$.
	## Ograničenja
	
	-  $1 \leq N \leq 100.000$
	-  $1 \leq M \leq 200.000$
	-  $1 \leq Q \leq 200.000$
	-  $1 \leq U[i] \neq V[i] \leq N$
	-  Nema ponavljanja puteva, tj. za $i \neq j$ važi $\{U[i],V[i]\} \neq \{U[j],V[j]\}$.
	-  Garantuje se da je od Rima moguće stići do svakog drugog grada.
	-   $1 \leq W[i] \leq 1.000.000.000$
	-   $1 \leq X[i], Y[i] \leq N$
	
	## Podzadaci
	
	Test primeri su podeljeni u $7$ podzadatka:
	
	-   **[4 poena]:** $M \leq 15 $, $ Q \leq 1.000 $
	-   **[9 poena]:** $N, M, Q \leq 200$
	-   **[11 poena]:** $N, M \leq 2.000$, $Q \leq 5.000$
	-   **[13 poena]:** $N, M \leq 3.000$
	-   **[6 poena]:** $M = N - 1$ i svaki grad je povezan sa najviše $2$ puta
	-   **[15 poena]:** $M = N - 1$
	-   **[42 poena]:** Nema dodatnih ograničenja
	
	## Detalji implementacije
	
	Potrebno je da pošaljete tačno jedan fajl  `omnes_viae_romam_ducunt.cpp`  koji implementira pomenutu funkciju. Osim tražene funkcije, vaš fajl može sadržati i dodatne globalne promenljive, pomoćne funkcije i dodatne biblioteke.
	
	Vaša funkcija mora biti sledećeg oblika:
	
	`void Putevi(int N, int M, int Q, int* U, int* V, int* W, int* X, int* Y, int* Ans);`
	
	**Vašim programima je dozvoljeno da menjaju sadržaj nizova ali ne smeju da pristupaju van granica datih nizova.**
	
	Uz zadatak, obezbeđen vam je "template" fajl  `code.cpp`  koji možete koristiti i menjati po potrebi. Takođe vam je obezbeđen program  `grader.cpp`  koji služi da lakše testirate kodove. Ovaj program učitava sa standardnog ulaza sledeće podatke:
	
	-   U prvom redu brojevi $N$, $M$ i $Q$.
	-   U narednih $M$ redova po tri broja: $U[i]$, $V[i]$ i $W[i]$.
	-   U narednih $Q$ redova po dva  broja: $X[i]$ i $Y[i]$.
	
	Zatim ovaj program zove vašu funkciju i ispisuje rezultat koji vaša funkcija vrati.
	
=== "Rešenje"
	
	| Autor | Tekst i test primeri | Analiza rеšenja | Testiranje |
	|:-:|:-:|:-:|:-:|
	| Aleksa Milisavljević | Aleksa Milisavljević | Aleksa Milisavljević | Pavle Martinović |
	
	## Rešenje kada je $M \leq 15 $, $ Q \leq 1.000 $
	Simuliramo odabir svih parova puteva. Složenost ovog rešenja je $O(Q \cdot 2^N)$.
	
	## Rešenje kada je $N, M, Q \leq 200$
	Neka je $T(u)$ skup čvorova $v$ takvih da svaki najkraći put od $1$ do $u$ prolazi kroz $v$. Primetimo da ovakav skup možemo pronaći izbacivanjem svakog čvora iz grafa i proveravanjem da li se povećalo rastojanje do čvora $u$. Primetimo da je rešenje upravo $|T(X[i]) \cap T(Y[i])|$. Ovakve skupove je moguće pronaći korišćenjem Dijkstrinog algoritma. Za svaki upit, možemo da pronađemo $T(X[i])$ i $T(Y[i])$ i potom njihov presek. Složenost ovog rešenja je $O(Q \cdot N \cdot M \log M)$.
	
	
	
	## Rešenje kada je $N, M \leq 2.000$, $Q \leq 5.000$
	Potrebno je da optimizujemo rešenje prethodnog zadatka tako što ćemo pronaći skupove $T(u)$ pre odgovaranja na upite. Složenost ovog rešenja je $O(N \cdot M \log M + N \cdot Q)$.
	
	
	
	## Rešenje kada je $N, M \leq 3.000$
	Ovaj podzadatak ima dva rešenja. Možemo optimizovati prethodni korišćenjem bitseta. Za alternativno rešenje, koje navodi na rešenje celog zadatka, možemo primetiti da skupovi $T$ formiraju strukturu stabla. Naime, za svako $u$, postoji jedinstveno $v \in T(u)$ tako da $T(u) = T(v) \cup \{u\}$. Označimo takvo $v$ sa $p(u)$ i formirajmo stablo u kojem je roditelj čvora $u$ upravo $p(u)$. Odgovor na upit je dubina najdubljeg zajedničkog pretka (LCA) čvorova $X[i]$ i $Y[i]$. Složenost ovog rešenja je $O(N \cdot M \log M + Q \log N)$.
	
	
	## Rešenje kada $M = N - 1$ i svaki grad je povezan sa najviše $2$ puta
	Graf možemo predstaviti kao niz. Odgovor na upit je veličina preseka dva intervala. Složenost ovog rešenja je $O(N + Q)$.
	
	
	## Rešenje kada je $M = N - 1$
	Odgovor na upit je dubina najdubljeg zajedničkog pretka (LCA) čvorova $X[i]$ i $Y[i]$. Složenost ovog rešenja je $O(N \cdot M \log M + Q \log N)$.
	
	
	## Glavno rešenje
	Za celo rešenje moramo da optimizujemo proces konstrukcije stabla iz četvrtog podzadatka. Primetimo da stablo možemo da konstruišemo paralelno sa izvršavanjem Dijkstrinog algoritma. Neka je čvor koji procesiramo u nekom koraku upravo $u$. Neka je $S(u)$ skup čvorova $v$ takvih da je grana $v - u$ na nekom najkraćem putu od $1$ do $u$. Primetimo da je tada $p(u) = LCA(S(u))$, gde je $LCA(X)$ najdublji zajednički predak svih čvorova iz skupa $X$. Primetimo da smo sve čvorove iz skupa $S(u)$ već obradili. Prema tome, možemo da dodamo čvor $u$ u stablo, kao dete čvora $p(u)$ i da ažuriramo $LCA$ tabelu. Složenost ovog rešenja je $O(M \log M + Q \log N)$.
	
	``` cpp title="05_viae_romanae.cpp" linenums="1"
	#include <bits/stdc++.h>
	#define MAXN 200007
	#define MAXL 18
	using namespace std;
	int d[MAXN], lca[MAXN][MAXL];
	void addChild(int u,int v) {
	    d[v] = d[u] + 1;
	    lca[v][0] = u;
	    for(int i = 1; i < MAXL; i++) lca[v][i] = lca[lca[v][i - 1]][i - 1];
	}
	int findLca(int u, int v) {
	    if(d[u] > d[v]) swap(u, v);
	    int k = MAXL;
	    while(k--) {
	        if((d[v]-d[u])&(1<<k)) v = lca[v][k];
	    }
	    if(u==v) return u;
	    k = MAXL - 1;
	    while(lca[u][0]!=lca[v][0]) {
	        if(lca[u][k]!=lca[v][k]) {
	            u = lca[u][k];
	            v = lca[v][k];
	        }
	        k--;
	    }
	    return lca[u][0];
	}
	vector<pair<int,int> > g[MAXN];
	long long dist[MAXN];
	bool vis[MAXN];
	priority_queue<pair<long long,int> > pq;
	void dijkstra(int n) {
	    for(int i=2;i<=n;i++)  dist[i]=1e18;
	    pq.push({-dist[1],1});
	    while(!pq.empty()) {
	        int u=pq.top().second;
	        pq.pop();
	        if(!vis[u]) {
	            vis[u]=true;
	            int par=-1;
	            for(auto pr:g[u]) {
	                int v=pr.first;
	                int w=pr.second;
	                if(dist[v]>dist[u]+w) {
	                    dist[v]=dist[u]+w;
	                    pq.push({-dist[v],v});
	                }
	                if(dist[u]==dist[v]+w) {
	                    if(par==-1) par=v;
	                    else par=findLca(par,v);
	                }
	            }
	            if(u!=1) addChild(par,u);
	        }
	    }
	}
	void Putevi(int N, int M, int Q, int* U, int* V, int* W, int* X, int* Y, int* Ans)
	{
	    for(int i=1;i<=M;i++) {
	        g[U[i]].push_back({V[i],W[i]});
	        g[V[i]].push_back({U[i],W[i]});
	    }
	    dijkstra(N);
	    for(int i=1;i<=Q;i++) Ans[i] = d[findLca(X[i],Y[i])] + 1;
	}

	```
