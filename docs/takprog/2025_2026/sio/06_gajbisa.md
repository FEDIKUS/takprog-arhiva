---
hide:
  - toc
---

# 6 - Gajbiša

=== "Zadatak"

	| Vremensko ograničenje | Memorijsko ograničenje |
	|:-:|:-:|
	| 5000ms | 512MB |

	Petrić je krenuo na IOI i, kao svaki ozbiljan takmičar, poneo je svoju omiljenu igračku, kauboja Gajbišu.

	Na putu do takmičenja imao je presedanje u Parizu. Dok je žurio sa jednog leta na drugi, Petrić je slučajno izgubio Gajbišu. Nikome nije sasvim jasno kako, ali Gajbiša je nekako završio u Luvru.

	Luvr je ogroman, ali na sreću, Gajbiša je primetio da se raspored prostorija i hodnika može predstaviti kao težinsko stablo sa korenom u čvoru $1$. Čvorovi predstavljaju prostorije, grane hodnike, a težine grana njihove dužine.

	Gajbiša je čuo da se svaki dobar bumerang uvek vrati nazad. Pošto i on želi da se vrati Petriću, odlučio je da pronađe najveći bumerang u Luvru.

	Međutim, Luvr nije miran ni na trenutak. Čuvari pomeraju eksponate, postavljaju ograde i menjaju putanje kroz muzej. Zato se dužine pojedinih hodnika vremenom menjaju.

	Posle svake promene dužine nekog hodnika, Gajbiša želi da zna kolika je najveća moguća težina bumeranga u trenutnom stablu. Promene su trajne, odnosno svaka naredna promena se primenjuje na stablo dobijeno posle prethodnih promena.

	Bumerang u stablu se dobija na sledeći način. Prvo se izabere jedan čvor, koji zovemo **centar bumeranga**. Zatim se iz tog čvora izaberu tri puta koji kreću u tri različita smera. To znači da svaki od ta tri puta počinje u centru, ali nakon toga odmah odlazi u različitu granu stabla.

	Putevi ne smeju imati zajedničke čvorove osim samog centra bumeranga. Svaki od tri puta mora sadržati bar jednu granu.

	Težina jednog puta jednaka je zbiru težina grana na tom putu. Težina bumeranga jednaka je zbiru težina sva tri izabrana puta.

	Pomozite Gajbiši da posle svake promene težine grane odredi najveću moguću težinu bumeranga.

	## Opisi funkcija
	`void Bumerang(int n, int q, int* p, int* w, int* s, int* k, long long* ans);`

	Ova funkcija će biti pozvana tačno jednom po test primeru.

	Broj $n$ predstavlja broj čvorova u stablu, a broj $q$ predstavlja broj promena težina grana.

	Niz $p$ opisuje stablo. Za svaki čvor $i$, broj $p[i]$ predstavlja roditelja čvora $i$. Važi $p[1] = 0$, jer je čvor $1$ koren stabla.

	Niz $w$ opisuje početne težine grana. Za svaki čvor $i > 1$, broj $w[i]$ predstavlja težinu grane između čvorova $i$ i $p[i]$. Važi $w[1] = 0$.

	Nizovi $s$ i $k$ opisuju promene težina grana. U $j$-toj promeni, težina grane između čvora $s[j]$ i njegovog roditelja $p[s[j]]$ postaje $k[j]$.

	Posle svake promene potrebno je izračunati najveću moguću težinu bumeranga. Odgovor posle $j$-te promene treba upisati u $ans[j]$.

	**Svi nizovi su indeksirani od 1.**

	## Primer

	Neka je:

	$n = 6$, $q = 3$

	$p = [0, 1, 1, 1, 2, 2]$

	$w = [0, 3, 4, 5, 2, 1]$

	Promene su:

	$s = [5, 4, 2]$

	$k = [10, 1, 8]$

	Posle prve promene, težina grane između čvorova $5$ i $2$ postaje $10$. Najveća moguća težina bumeranga je $22$.

	Posle druge promene, težina grane između čvorova $4$ i $1$ postaje $1$. Najveća moguća težina bumeranga je $18$.

	Posle treće promene, težina grane između čvorova $2$ i $1$ postaje $8$. Najveća moguća težina bumeranga je $23$.

	Zato funkcija treba da upiše:

	$ans = [22, 18, 23]$

	## Ograničenja

	- $1 \leq n, q \leq 2\cdot 10^5$
	- $p[1] = 0$
	- Za svako $i > 1$ važi $1 \leq p[i] \leq n$
	- Niz $p$ opisuje stablo sa korenom u čvoru $1$
	- $w[1] = 0$
	- Za svako $i > 1$ važi $1 \leq w[i] \leq 10^9$
	- Za svako $j$ važi $2 \leq s[j] \leq n$
	- Za svako $j$ važi $1 \leq k[j] \leq 10^9$
	- U stablu postoji bar jedan bumerang

	## Podzadaci

	Test primeri su podeljeni u 7 podzadataka:

	-   **[6 poena]:** $n, q \leq 200$.
	-   **[8 poena]:** Stablo je zvezda, odnosno postoji čvor koji je povezan sa svim ostalim čvorovima.
	-   **[10 poena]:** $q = 1$.
	-   **[12 poena]:** $n, q \leq 5000$.
	-   **[12 poena]:** Svaka promena menja težinu grane koja je povezana sa listom.
	-   **[12 poena]:** Posle svake promene postoji optimalan bumerang čiji je centar čvor $1$.
	-   **[40 poena]:** Bez dodatnih ograničenja.

	## Detalji implementacije

	Potrebno je da pošaljete tačno jedan fajl `gajbisa.cpp` koji implementira pomenutu funkciju. Osim tražene funkcije, vaš fajl može sadržati i dodatne globalne promenljive, pomoćne funkcije i dodatne biblioteke.

	Vaša funkcija mora biti sledećeg oblika:

	`void Bumerang(int n, int q, int* p, int* w, int* s, int* k, long long* ans);`

	Vašim programima je dozvoljeno da menjaju sadržaj nizova, ali ne smeju da pristupaju van granica datih nizova.

	Uz zadatak, obezbeđen vam je `template` fajl `code.cpp`, koji možete koristiti i menjati po potrebi. Takođe vam je obezbeđen program `grader.cpp`, koji služi da lakše testirate kodove.

	Ovaj program učitava sa standardnog ulaza sledeće podatke:

	- U prvom redu brojeve $N$ i $Q$.
	- U drugom redu $N$ brojeva: $p[i]$.
	- U trećem redu $N$ brojeva: $w[i]$.
	- U četvrtom redu $Q$ brojeva: $s[j]$.
	- U petom redu $Q$ brojeva: $k[j]$.

	Zatim ovaj program poziva vašu funkciju i ispisuje vrednosti $ans[1], ans[2], \ldots, ans[Q]$, svaku u posebnom redu.

	[Test primeri i prateći fajlovi sa zvaničnog takmičenja](https://nyc3.digitaloceanspaces.com/takprog/2025-26/2025-2026-sio-problems.zip).

=== "Rešenje"

	| Autor | Tekst i test primeri | Analiza rešenja | Testiranje |
	|:-:|:-:|:-:|:-:|
	| Marko Milenković | Marko Milenković | Marko Milenković | Miloš Milutinović |

	## Rešenje kada je $n, q \leq 200$

	Za početak, primetimo da će krajevi sva tri puta u optimalnom bumerangu uvek biti listovi. Zaista, ako se neki put završava u čvoru koji nije list, taj put možemo produžiti bar još jednom granom, čime se ukupna težina bumeranga povećava, jer su sve težine grana pozitivne.

	Zato je jedno jednostavno rešenje sledeće. Posle svake promene težine grane, možemo za svaki čvor da pretpostavimo da je centar bumeranga. Iz tog čvora posmatramo sve grane koje izlaze iz njega. Za svaku takvu granu nađemo najduži put koji kreće tom granom i završava se u nekom listu. Ako čvor ima bar tri takva smera, kandidat za odgovor je zbir tri najveće dobijene vrednosti.

	Ovo možemo uraditi potpuno naivno, pokretanjem DFS-a iz svakog čvora. Složenost je dovoljno dobra za ovaj podzadatak.

	## Rešenje kada je stablo zvezda

	Ako je stablo zvezda, onda je centar bumeranga očigledno centar zvezde. Svaki put u bumerangu sastoji se od tačno jedne grane. Dakle, posle svake promene potrebno je samo znati tri najveće težine grana u stablu.

	Ovo možemo održavati pomoću multiset-a. Kada se promeni težina neke grane, staru vrednost izbacimo, novu ubacimo, a odgovor je zbir tri najveća elementa u multiset-u.

	Složenost po promeni je $O(\log n)$.

	## Rešenje kada je $q = 1$, ili kada je $n, q \leq 5000$

	Za ove podzadatke dovoljno je posle svake promene ponovo izračunati najbolji bumerang u trenutnom stablu.

	Postoji više načina da se ovo uradi. Jedan način je da za svaki čvor nađemo tri najbolja puta ka listovima, pri čemu ta tri puta moraju krenuti u tri različita smera iz tog čvora. To se može uraditi DFS-om i rerutiranjem dinamike na stablu.

	Jednostavnije za implementaciju je koristiti ideju iz punog rešenja, ali bez ikakve dinamičke strukture. Posle svake promene ponovo napravimo Euler tour i izračunamo odgovor. Ovo daje složenost $O(n)$ ili $O(n \log n)$ po promeni, u zavisnosti od implementacije, što je dovoljno za ove podzadatke.

	## Ključno zapažanje

	Umesto da direktno posmatramo centar bumeranga, posmatraćemo tri lista koji su krajevi tri puta bumeranga.

	Neka su ta tri lista $a, b, c$. Težina bumeranga je jednaka težini minimalnog podstabla koje povezuje ova tri lista. Drugim rečima, to je zbir težina grana u stablu koje dobijamo kada spojimo $a$, $b$ i $c$.

	Ako stablo ukorenimo u nekom čvoru koji nije list, i ako listove $a, b, c$ posmatramo u DFS poretku, neka važi:

	$$
	fst[a] < fst[b] < fst[c]
	$$

	Neka je:

	$$
	x = lca(a, b)
	$$

	i

	$$
	y = lca(b, c)
	$$

	Tada je centar bumeranga zapravo onaj od čvorova $x$ i $y$ koji je bliži korenu, odnosno koji ima manju dubinu.

	Zato težinu bumeranga možemo zapisati kao:

	$$
	dep[a] + dep[b] + dep[c] - dep[x] - dep[y] - \min(dep[x], dep[y])
	$$

	Ovo možemo prepisati kao maksimum dve vrednosti:

	$$
	dep[a] - 2dep[x] + dep[b] - dep[y] + dep[c]
	$$

	i

	$$
	dep[a] - dep[x] + dep[b] - 2dep[y] + dep[c]
	$$

	Zato se u rešenju pojavljuju baš dva niza koeficijenata:

	$$
	(1, -2, 1, -1, 1)
	$$

	i

	$$
	(1, -1, 1, -2, 1)
	$$

	Prva, treća i peta pozicija predstavljaju listove $a, b, c$, dok druga i četvrta pozicija predstavljaju čvorove $lca(a,b)$ i $lca(b,c)$.

	## Euler tour

	Napravićemo standardni Euler tour stabla. Svaki čvor upišemo kada prvi put uđemo u njega, a zatim ga ponovo upišemo svaki put kada se vratimo u njega iz nekog deteta.

	Za ovako dobijen niz važi važna osobina: ako su $u$ i $v$ dva čvora i ako je $fst[u] < fst[v]$, onda se $lca(u,v)$ nalazi kao čvor najmanje dubine na delu Euler tour-a između $fst[u]$ i $fst[v]$.

	Ovo nam savršeno odgovara, jer u formulama iznad čvorovi $x$ i $y$ imaju negativne koeficijente. Dakle, kada maksimizujemo izraz, za poziciju sa koeficijentom $-1$ ili $-2$ automatski će biti izabran čvor najmanje dubine na odgovarajućem intervalu, odnosno LCA.

	## Puno rešenje

	Potrebno je dinamički održavati maksimum izraza oblika:

	$$
	c_0 dep[v_0] + c_1 dep[v_1] + c_2 dep[v_2] + c_3 dep[v_3] + c_4 dep[v_4]
	$$

	gde je:

	$$
	v_0, v_1, v_2, v_3, v_4
	$$

	rastući podniz Euler tour-a, a koeficijenti su jedan od dva niza:

	$$
	(1, -2, 1, -1, 1)
	$$

	ili

	$$
	(1, -1, 1, -2, 1)
	$$

	Dodatno, pozicije sa pozitivnim koeficijentom moraju biti listovi, i to njihova prva pojava u Euler tour-u. Pozicije sa negativnim koeficijentom mogu biti bilo koji čvorovi.

	Ovo možemo održavati segment tree-jem.

	U svakom čvoru segment tree-ja čuvamo dinamiku:

	$$
	dp[t][i][j]
	$$

	gde je $t$ jedan od dva niza koeficijenata, a $i, j$ označavaju da smo u tom segmentu izabrali podniz koji odgovara koeficijentima od $i$ do $j-1$.

	Pošto imamo samo $5$ koeficijenata, broj stanja je mali. Za svaki od dva tipa imamo samo:

	$$
	\binom{6}{2} = 15
	$$

	stanja.

	Kada spajamo dva sina segment tree-ja, radimo standardno spajanje dinamike nad podnizovima:

	$$
	dp[i][j] = \max_{k=i}^{j} left[i][k] + right[k][j]
	$$

	Ovo znači da neki prefiks traženog podniza uzimamo iz levog deteta, a ostatak iz desnog deteta.

	## Početne vrednosti u listu segment tree-ja

	Neka jedna pozicija Euler tour-a predstavlja čvor $v$.

	Ako je trenutni koeficijent pozitivan, onda tu poziciju smemo iskoristiti samo ako je $v$ list i ako je ovo prvo pojavljivanje tog lista u Euler tour-u.

	Ako je koeficijent negativan, onda tu poziciju smemo iskoristiti uvek.

	Na taj način segment tree tačno bira tri lista i dva LCA čvora između njih.

	## Obrada promene težine grane

	Kada se promeni težina neke grane za $\Delta$, promene se dubine svih čvorova u jednoj podgrani. Zbog toga ukorenjujemo stablo i za svaku granu znamo koji njen kraj je niže u stablu.

	Ako se promeni grana koja vodi ka čvoru $v$, onda se dubine svih čvorova u podstablu čvora $v$ promene za $\Delta$.

	U Euler tour-u sva pojavljivanja čvorova iz tog podstabla čine jedan interval, pa je dovoljno uraditi range add na segment tree-ju.

	Ako se svim dubinama u nekom segment tree čvoru doda vrednost $\Delta$, onda se vrednost stanja koje koristi koeficijente od $i$ do $j-1$ povećava za:

	$$
	\Delta \cdot (c_i + c_{i+1} + \ldots + c_{j-1})
	$$

	Zato je dovoljno da unapred izračunamo prefiksne sume koeficijenata i lazy propagation radi direktno nad svim stanjima.

	## Odgovor

	Odgovor posle svake promene je maksimum dve vrednosti u korenu segment tree-ja:

	$$
	dp[0][0][5]
	$$

	i

	$$
	dp[1][0][5]
	$$

	Prva vrednost odgovara slučaju kada je $lca(a,b)$ bliži korenu, a druga slučaju kada je $lca(b,c)$ bliži korenu.

	## Složenost

	Euler tour ima dužinu $O(n)$, tačnije najviše $2n-1$.

	U svakom čvoru segment tree-ja čuvamo konstantan broj stanja, jer je broj koeficijenata uvek $5$. Zato je memorijska složenost:

	$$
	O(n)
	$$

	Svaka promena težine grane je jedan range add nad segment tree-jem, pa je vremenska složenost po promeni:

	$$
	O(\log n)
	$$

	Ukupna složenost je:

	$$
	O((n+q)\log n)
	$$

	sa veoma malom konstantom, jer svaki čvor segment tree-ja ima samo $2 \cdot 15$ stanja.

	[Izvor analize i autorskih podataka](https://algora.petlja.org/t/2025-2026/9654/6).

	``` cpp title="gajbisa.cpp" linenums="1"
	#include <bits/stdc++.h>
	using namespace std;

	using ll = long long;

	const int MAXV = 200000 + 5;
	const int MAXEUL = 2 * MAXV;
	const int L = 5;
	const int S = 15;

	int idd[L + 1][L + 1];

	ll c[2][L] = {
	    { 1, -2,  1, -1, 1},
	    { 1, -1,  1, -2, 1}
	};

	ll pref[2][L + 1];

	int eu[MAXEUL], fst[MAXV], lst[MAXV];
	ll dep[MAXV];
	bool leaf[MAXV];

	ll getv(const ll *d, int t, int i, int j){
	    if(i == j) return 0;
	    if(i > j) return INT64_MIN;
	    return d[t * S + idd[i][j]];
	}

	template<int MAXN>
	struct segtr{
	    struct node{
	        ll d[2 * S];
	        ll lazy;

	        void clear(){
	            for(int i = 0; i < 2 * S; ++i) d[i] = INT64_MIN;
	            lazy = 0;
	        }

	        node& operator+=(const node& other){
	            node res;
	            res.clear();

	            for(int t = 0; t < 2; ++t){
	                for(int i = 0; i <= L; ++i){
	                    for(int j = i + 1; j <= L; ++j){
	                        ll best = INT64_MIN;

	                        for(int k = i; k <= j; ++k){
	                            ll x = getv(d, t, i, k);
	                            ll y = getv(other.d, t, k, j);

	                            if(x <= INT64_MIN / 2 || y <= INT64_MIN / 2) continue;

	                            best = max(best, x + y);
	                        }

	                        res.d[t * S + idd[i][j]] = best;
	                    }
	                }
	            }

	            *this = res;
	            return *this;
	        }

	        node operator+(const node& other) const{
	            node tmp = *this;
	            return tmp += other;
	        }

	        void add_lazy(ll x){
	            lazy += x;

	            for(int t = 0; t < 2; ++t){
	                for(int i = 0; i <= L; ++i){
	                    for(int j = i + 1; j <= L; ++j){
	                        int pos = t * S + idd[i][j];

	                        if(d[pos] <= INT64_MIN / 2) continue;

	                        d[pos] += x * (pref[t][j] - pref[t][i]);
	                    }
	                }
	            }
	        }
	    };

	    node a[2 * MAXN + 5];
	    int n;

	    inline int lc(int pos){
	        return pos + 1;
	    }

	    inline int rc(int pos, int l, int mid){
	        return pos + 2 * (mid - l + 1);
	    }

	    void init(int _n){
	        n = _n;
	        build(1, 1, n);
	    }

	    void make_leaf(int pos, int ind){
	        a[pos].clear();

	        int v = eu[ind];

	        for(int t = 0; t < 2; ++t){
	            for(int i = 0; i < L; ++i){
	                bool ok = false;

	                if(c[t][i] < 0){
	                    ok = true;
	                }else{
	                    ok = leaf[v] && fst[v] == ind;
	                }

	                if(ok){
	                    a[pos].d[t * S + idd[i][i + 1]] = c[t][i] * dep[v];
	                }
	            }
	        }
	    }

	    void build(int pos, int l, int r){
	        if(l == r){
	            make_leaf(pos, l);
	            return;
	        }

	        int mid = (l + r) / 2;

	        int Lc = lc(pos);
	        int Rc = rc(pos, l, mid);

	        build(Lc, l, mid);
	        build(Rc, mid + 1, r);

	        a[pos] = a[Lc] + a[Rc];
	    }

	    void push(int pos, int l, int r){
	        if(a[pos].lazy == 0 || l == r) return;

	        int mid = (l + r) / 2;

	        int Lc = lc(pos);
	        int Rc = rc(pos, l, mid);

	        a[Lc].add_lazy(a[pos].lazy);
	        a[Rc].add_lazy(a[pos].lazy);

	        a[pos].lazy = 0;
	    }

	    void add(int l, int r, ll x){
	        add(l, r, x, 1, 1, n);
	    }

	    void add(int l, int r, ll x, int pos, int rl, int rr){
	        if(l <= rl && rr <= r){
	            a[pos].add_lazy(x);
	            return;
	        }

	        push(pos, rl, rr);

	        int mid = (rl + rr) / 2;

	        int Lc = lc(pos);
	        int Rc = rc(pos, rl, mid);

	        if(l <= mid) add(l, r, x, Lc, rl, mid);
	        if(mid < r) add(l, r, x, Rc, mid + 1, rr);

	        a[pos] = a[Lc] + a[Rc];
	    }

	    ll get_ans(){
	        return max(
	            a[1].d[0 * S + idd[0][L]],
	            a[1].d[1 * S + idd[0][L]]
	        );
	    }
	};

	segtr<MAXEUL> tr;

	void Bumerang(int n, int q, int* p, int* w, int* s, int* k, long long* ans){
	    int ptr = 0;

	    for(int i = 0; i <= L; ++i){
	        for(int j = 0; j <= L; ++j){
	            idd[i][j] = -1;
	        }
	    }

	    for(int i = 0; i <= L; ++i){
	        for(int j = i + 1; j <= L; ++j){
	            idd[i][j] = ptr++;
	        }
	    }

	    for(int t = 0; t < 2; ++t){
	        pref[t][0] = 0;

	        for(int i = 0; i < L; ++i){
	            pref[t][i + 1] = pref[t][i] + c[t][i];
	        }
	    }

	    struct edge{
	        int to, w;
	    };

	    vector<vector<edge>> g(n + 1);

	    for(int i = 2; i <= n; ++i){
	        g[i].push_back({p[i], w[i]});
	        g[p[i]].push_back({i, w[i]});
	    }

	    int root = 1;

	    for(int i = 1; i <= n; ++i){
	        if((int)g[i].size() > 1){
	            root = i;
	            break;
	        }
	    }

	    for(int i = 1; i <= n; ++i){
	        leaf[i] = ((int)g[i].size() == 1);
	    }

	    vector<int> par(n + 1, 0), it(n + 1, 0);
	    vector<ll> cur(n + 1, 0);

	    for(int i = 1; i <= n; ++i){
	        cur[i] = w[i];
	    }

	    int m = 0;

	    vector<int> st;
	    st.push_back(root);

	    par[root] = 0;
	    dep[root] = 0;

	    fst[root] = ++m;
	    eu[m] = root;

	    while(!st.empty()){
	        int v = st.back();

	        if(it[v] == (int)g[v].size()){
	            lst[v] = m;
	            st.pop_back();

	            if(!st.empty()){
	                eu[++m] = st.back();
	            }

	            continue;
	        }

	        edge e = g[v][it[v]++];

	        if(e.to == par[v]) continue;

	        par[e.to] = v;
	        dep[e.to] = dep[v] + e.w;

	        fst[e.to] = ++m;
	        eu[m] = e.to;

	        st.push_back(e.to);
	    }

	    tr.init(m);

	    for(int qq = 1; qq <= q; ++qq){
	        int v = s[qq];
	        int u = p[v];

	        int down = (par[v] == u ? v : u);

	        ll delta = (ll)k[qq] - cur[v];
	        cur[v] = k[qq];

	        tr.add(fst[down], lst[down], delta);

	        ans[qq] = tr.get_ans();
	    }
	}
	```
