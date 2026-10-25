---
hide:
  - toc
---

# 8 - Igra sa kartama

=== "Zadatak"
	
	| Vremensko ograničenje | Memorijsko ograničenje |
	|:-:|:-:|
	| 3000ms | 256MB |
	
	
	U špilu se nalazi $N$ karata. Karta na vrhu špila ima indeks $1$, a karta ispod karte $i$ ima indeks $i+1$. Na karti $i$ je napisan prirodan broj $a_i$. 
	
	<br>
	
	Igramo sledeću igru. Prvo izaberemo prirodni broj $k$ i uzmemo prvih $k$ karata u ruku. Nakon toga ponavljamo sledeći postupak dokle god je ostalo karata u špilu:
	
	
	- Povučemo prvu kartu sa vrha špila i stavimo je u našu ruku. 
	- Izaberemo neku kartu iz naše ruke (može, a ne mora biti karta koju smo upravo izvukli). Neka je na njoj napisan broj $x$. Izaberemo koliko kod hoćemo karata iz naše ruke sa brojem $x$ na njima (ali barem jednu) i odigramo te karte (više nam nisu u ruci, ali se **ne vraćaju** u špil).
	
	<br>
	
	Naš cilj je da nakon što smo odigrali sve poteze suma karata u našoj ruci bude najmanja moguća. 
	
	<br>
	
	Dat Vam je niz $a$ i $Q$ upita nad njim. Imamo dva tipa upita:
	
	
	- ``1 x`` - Naći najmanju moguću vrednost sume karata u našoj ruci ako igramo igru nad trenutnim nizom i pretpostavimo da je $k = x$. 
	
	- ``2 x y`` - Promenimo vrednost karte $x$ u $y$. Odnosno $a_x := y$. 
	
	<br>
	
	## Opis ulaza
	
	
	Prva linija ulaza sadrži brojeve $N$ i $Q$ - broj karata u špilu i broj upita.
	
	
	Druga linija ulaza sadrži $N$ brojeva $a_1, a_2, ..., a_n$ - elemente niza $a$.
	
	
	Sledećih $Q$ linija opisuje svaki od upita. Prvi broj je broj $t$, tip upita. Ako je $t=1$ onda se nakon broja $t$ nalazi broj $x$. Ako je $t=2$, onda se nakon broja $t$ nalaze brojevi $x$ i $y$.
	
	<br>
	
	## Opis izlaza
	
	
	Za svaki upit tipa $t=1$ ispisati jedan broj — odgovor na taj upit.
	
	<br>
	
	## Primer 1
	
	
	### Ulaz
	
	~~~
	6 6
	
	1 1 2 2 3 3
	1 1
	1 2
	1 3
	1 4
	1 5
	1 6
	~~~
	
	
	### Izlaz
	
	~~~
	0
	0
	0
	2
	6
	12
	~~~
	
	
	### Objašnjenje
	
	U prvom upitu ćemo na početku u ruci imati kartu sa brojem $1$. Nakon toga, vučemo kartu sa brojem $1$, pa u ruci imamo karte sa brojevima $1$ i $1$. Zatim biramo $x=1$ i odigravamo obe karte sa brojem $1$, nakon čega je naša ruka prazna. U sledećih $4$ poteza biramo broj $x$ da bude jednak broju na karti koju smo upravo izvukli i odigramo tu kartu. Na kraju svih poteza naša ruka je prazna, pa je suma svih karata u našoj ruci $0$. 
	
	U drugom upitu na početku u ruci imamo karte sa brojevima $1$ i $1$, a vučemo karte sa brojevima $2$, $2$, $3$ i $3$ redom. Igramo slično kao u prvom i trećem upitu.
	
	U trećem upitu na početku u ruci imamo karte sa brojevima $1$, $1$ i $2$. Igramo na sledeći način:
	
	- U prvom potezu povlačimo kartu sa brojem $2$. Biramo $x=1$ i odigramo obe karte sa brojem $1$. U ruci imamo dve karte sa brojem $2$. 
	- U drugom potezu povlačimo kartu sa brojem $3$. Biramo $x=2$ i odigramo obe karte sa brojem $2$. U ruci imamo jednu kartu sa brojem $3$.
	- U trećem potezu povlačimo kartu sa brojem $3$. Biramo $x=3$ i odigramo obe karte sa brojem $3$. Nemamo ni jednu kartu u ruci, pa je odgovor $0$.
	
	U četvrtom upitu ćemo na početku u ruci imati karte sa brojevima $1$, $1$, $2$ i $2$. Igramo na sledeći način:
	- U prvom potezu vučemo kartu sa brojem $3$. Biramo $x=2$ i odigramo obe karte sa brojem $2$. U našoj ruci su karte sa brojevima $1$, $1$ i $3$.
	- U drugom potezu vučemo kartu sa brojem $3$. Biramo $x=3$ i odigramo obe karte sa brojem $3$. U našoj ruci su karte sa brojevima $1$, $1$. Suma brojeva na kartama je $1 + 1 = 2$. Može se dokazati da manja suma na kraju igre nije moguća.
	
	U petom upitu ćemo na početku u ruci imati karte sa brojevima $1$, $1$, $2$, $2$ i $3$. U prvom i jedinom potezu vučemo kartu sa brojem $3$. Zatim biramo $x=3$ i odigravamo obe karte sa brojem $3$. U ruci su nam karte sa brojevima $1$, $1$, $2$, $2$, a njihova suma je $1+1+2+2 = 6$.
	
	U šestom upitu ćemo na početku u ruci imati karte sa brojevima $1$, $1$, $2$, $2$, $3$ i $3$. S obzirom sa su nam sve karte već u ruci, nećemo odigrati nijedan potez, pa je suma karata u ruci $1+1+2+2+3+3 = 12$. 
	
	<br>
	
	## Primer 2
	
	
	### Ulaz
	
	~~~
	10 4
	1 2 3 2 4 2 1 2 3 3
	1 6
	2 9 5
	2 6 5
	1 7
	~~~
	
	
	### Izlaz
	
	~~~
	0
	6
	~~~
	
	
	### Objašnjenje
	
	U prvom upitu je niz $a  = [1, 2, 3, 2, 4, 2, 1, 2, 3, 3]$. U ruci su nam karte sa brojevima $1$, $2$, $3$, $2$, $4$, $2$, a vučemo redom karte sa brojevima $1$, $2$, $3$, $3$. Postoji način igranja poteza takav da nam na kraju ruka bude prazna.
	
	U drugom upitu se menja element niza $a$ na poziciji $9$ u $5$, pa je niz $a  = [1, 2, 3, 2, 4, 2, 1, 2,$ **5** $, 3]$.
	
	 U trećam upitu se menja element niza $a$ na poziciji $6$ u $5$, pa je niz $a  = [1, 2, 3, 2, 4,$ **5** $, 1, 2, 5, 3]$.
	
	U četvrtom upitu su nam u ruci karte sa brojevima $1$, $2$, $3$, $2$, $4$, $5$, $1$, a vučemo redom karte sa brojevima $2$, $5$, $3$. Može se dokazati da će, pri optimalnoj igri, zbir karata u ruci biti $6$.
	
	## Primer 3
	
	<br>
	
	### Ulaz
	
	~~~
	11 3
	11 10 9 8 7 6 1 1 1 2 2
	1 6
	2 7 3
	1 5
	~~~
	
	
	### Izlaz
	
	~~~
	13
	9
	~~~
	
	<br>
	
	## Ograničenja
	
	- $1 \leq N, Q \leq 2\cdot10^5$
	- $1 \leq a_i \leq N$, za svako $1 \le i \le N$ 
	- $t_i \in \{1, 2\}$, za svaki upit $1\le i \le Q$
	- $1 \le x_i \le N$, za sve upite tipa $t_i=1$ za $1 \le i \le Q$
	- $1 \le x_i, y_i \le N$, za sve upite tipa $t_i = 2$ za $1 \le i \le Q$
	- Postoji barem jedan upit za koji je $t_i = 1$
	
	<br>
	
	Test primeri su podeljeni u sedam grupa:
	
	- u test primerima vrednim $10$ poena važi: $Q = 1$, $x_1 = 1$. 
	- u test primerima vrednim $10$ poena važi: $N, Q \le 5$;
	- u test primerima vrednim $30$ poena važi: $Q = 1$; 
	- u test primerima vrednim $10$ poena važi: $t_i = 1$ , za svako $1 \le i \le Q$;
	- u test primerima vrednim $10$ poena važi: Za sve upite $i$ tipa $t_i = 1$ važi $x_i \ge N -100$;
	- u test primerima vrednim $10$ poena važi: Za sve upite $i$ tipa $t_i = 1$ važi $x_i \le 100$;
	- u test primerima vrednim $20$ poena: nema dodatnih ograničenja.
	
	<br>
	
=== "Rešenje"
	
	| Autor | Tekst i test primeri | Analiza rešenja | Testiranje |
	|:-:|:-:|:-:|:-:|
	|  |  |  |  |
	
	
	``` cpp title="08_igra_sa_kartama.cpp" linenums="1"
	#include <bits/stdc++.h>
	 
	using namespace std;
	 
	struct DynamicSegmentTree{
	    using B = long long; // boundary type
	    using T = pair<long long, int>; // value type
	    const T nullval = {0, 0};
	 
	    static T merge(const T &a, const T &b){
	        return {a.first + b.first, a.second + b.second};
	    }
	 
	    // =========================
	 
	    struct Node{
	        T val;
	        int lft, rght;
	    };
	 
	    vector<Node> tree;
	    int root{};
	 
	    const B leftBound{}, rightBound{};
	 
	    DynamicSegmentTree() = default;
	 
	    explicit DynamicSegmentTree(const B leftBound_, const B rightBound_, const int reserveSize = 0) : root(newNode()), leftBound(leftBound_), rightBound(rightBound_){
	        tree.reserve(reserveSize);
	    }
	 
	    int newNode(){
	        tree.push_back(Node{nullval, -1, -1});
	 
	        return tree.size() - 1;
	    }
	 
	    void update_(const int v, const B l, const B r, const B pos, const T val){
	        if(l == r) tree[v].val = merge(tree[v].val, val);
	        else{
	            const B m = l + (r - l) / 2;
	 
	            if(pos <= m){
	                update_(tree[v].lft == -1 ? tree[v].lft = newNode() : tree[v].lft, l, m, pos, val);
	                tree[v].val = merge(tree[tree[v].lft].val, tree[v].rght == -1 ? nullval : tree[tree[v].rght].val);
	            }
	            else{
	                update_(tree[v].rght == -1 ? tree[v].rght = newNode() : tree[v].rght, m + 1, r, pos, val);
	                tree[v].val = merge(tree[v].lft == -1 ? nullval : tree[tree[v].lft].val, tree[tree[v].rght].val);
	            }
	        }
	    }
	 
	    template<typename U, typename = enable_if_t<is_convertible_v<U, T>>>
	    void update(const B pos, const U val){
	        update_(root, leftBound, rightBound, pos, (T)val);
	    }
	 
	    long long query_(const int v, const B l, const B r, const int k) const{
	        if(v == -1 || k == 0) return 0;
	        if(tree[v].val.second <= k) return tree[v].val.first;
	        if(l == r) return l * min(tree[v].val.second, k);
	 
	        const B m = l + (r - l) / 2;
	 
	        if(tree[v].rght == -1) return query_(tree[v].lft, l, m, k);
	 
	        if(tree[tree[v].rght].val.second >= k) return query_(tree[v].rght, m + 1, r, k);
	        else return tree[tree[v].rght].val.first + query_(tree[v].lft, l, m, k - tree[tree[v].rght].val.second);
	    }
	 
	    long long query(const int k) const{
	        return query_(root, leftBound, rightBound, k);
	    }
	};
	 
	void solve(){
	    int n, q;
	 
	    cin >> n >> q;
	 
	    vector<int> arr(n + 1);
	    vector<long long> sums(n + 1, 0);
	 
	    for(int i = 1; i <= n; i++){
	        cin >> arr[i];
	        sums[arr[i]] += arr[i];
	    }
	 
	    DynamicSegmentTree sgt(1, 1ll * n * n);
	 
	    for(int i = 1; i <= n; i++) if(sums[i]) sgt.update(sums[i], pair{sums[i], 1});
	 
	    long long totalsum = accumulate(arr.begin(), arr.end(), 0ll);
	 
	    while(q--){
	        int qt;
	 
	        cin >> qt;
	 
	        if(qt == 1){
	            int k;
	            cin >> k;
	 
	            cout << totalsum - sgt.query(n - k) << '\n';
	        }
	        else{
	            int i, x;
	            cin >> i >> x;
	 
	            sgt.update(sums[arr[i]], pair{-sums[arr[i]], -1});
	            sums[arr[i]] -= arr[i];
	            totalsum -= arr[i];
	            if(sums[arr[i]]) sgt.update(sums[arr[i]], pair{sums[arr[i]], 1});
	 
	            if(sums[x]) sgt.update(sums[x], pair{-sums[x], -1});
	 
	            arr[i] = x;
	 
	            sums[arr[i]] += arr[i];
	            totalsum += arr[i];
	            sgt.update(sums[arr[i]], pair{sums[arr[i]], 1});
	        }
	    }
	}
	 
	int main(){
	    ios::sync_with_stdio(false);
	    cin.tie(nullptr);
	 
	    int t=1;
	    //cin >> t;
	    while(t--) solve();
	}

	```
