---
hide:
  - toc
---

# 10 - Perica i novogodišnje stablo

=== "Zadatak"
	
	| Vremensko ograničenje | Memorijsko ograničenje |
	|:-:|:-:|
	| 500ms | 256MB |
	
	Dato je $n$ tačaka u jediničnom kvadratu $[0,1]\times [0,1]$. Skup tih $n$ tačaka zvaćemo $P$. Neka je $MST$ najmanje razapinjuće stablo$^2$ nad kompletnim grafom nad ovim tačkama, gde težinu grana između tačaka $i$ i $j$ sa koordinatama $(x_i,y_i)$ i $(x_j,y_j)$ računamo kao Menhetn distancu, tj. $|x_i-x_j|+|y_i-y_j|$. Garantuje se da je $MST$ nad ovim grafom jedinstven.
	<br>
	Velikom Perici se svidelo kako izgleda ovaj $MST$, i pošto se bliži Nova godina i potrebno mu je novogodišnje stablo, želi da ima isto takvo stablo kod kuće. Kod kuće nema puno prostora pa bi hteo da stablo u njegovoj kući ima najviše $\frac{18}{\epsilon^2}$ tačaka. Pošto njemu nije bitna veličina, već naprotiv samo oblik stabla želi da $MST$ i stablo u njegovoj kući budu $\epsilon$-slični.
	
	Vaš zadatak je da izaberete podskup tačaka $Q \subseteq P$, i neko razapinjuće stablo$^1$ $T$ (ne nužno minimalno) nad kompletnim grafom nad $Q$:
	
	1.  Q ima najviše $\frac{18}{\epsilon^2}$ tačaka
	    
	2.  $MST$ i $T$ su $\epsilon$-slični.
	    
	Za dva razapinjuća stabla kažemo da su $\epsilon$-slični, ako za svaku tačku na prvom stablu postoji bar jedna tačka na drugom stablu na Menhetn distanci najviše $\epsilon$ i za svaku tačku na drugom stablu postoji bar jedna tačka na prvom stablu na Menhetn distanci najviše $\epsilon$. Pod tačke na nekom stablu misli se na sve čvorove i svaku tačku na svakoj grani iz stabla. Grana između čvorova $i$ i $j$ je duž koja spaja $(x_i,y_i)$ i $(x_j,y_j)$.<br> 
	$^1$ Razapinjuće stablo nad grafom sa $m$ čvorova sa skupom grana $E$ je skup $F \subseteq E$ veličine $m-1$ tako da je za svaki od $m$ čvorova izabrana bar jedna grana koja sadrži taj čvor. <br>
	$^2$ Minimalno razapinjuće stablo za graf je ono razapinjuće stablo za taj graf koje ima minimalni zbir težina svih grana u njemu.
	
	## Opis ulaza  
	U prvoj liniji standardnog ulaza dat je ceo broj $n$, broj tačaka. <br> U drugoj liniji dat je broj $\epsilon$ na 10 decimala. U narednih $n$ linija standardnog ulaza nalaze se po dva broja na 10 decimala - $x_i,y_i$, koordinate tačke $i$ . 
	## Opis izlaza  
	U prvoj liniji standardnog izlaza ispišite $|Q|$ - veličinu izabranog podskupa. U sledećem redu ispišite $k$ brojeva koji predstavljaju indekse tačaka koje su u tom skupu. U sledećih $k-1$ linija ispisati po dva broja koji predstavljaju grane koje su u izabranom razapinjućem stablu $T$. 
	## Primer 1
	### Ulaz
	 ``` 
	5 0.2500000000000
	0.4000000000000 0.5000000000000
	0.5000000000000 0.2500000000000
	0.3000000000000 1.0000000000000
	1.0000000000000 0.6000000000000
	0.9000000000000 0.4000000000000
	```   
	### Izlaz  
	 ```
	4
	1 2 3 5
	1 2
	2 5
	1 3 
	 ```  
	### Objašnjenje primera
	U ovom primeru $MST$ tačaka čine grane $(4,5), (1,2), (2,5), (1,3)$. Za tačku $4$ van stabla $T$ tačka $5$ je na distanci najviše $\epsilon$. Za tačke na grani $(4,5)$ koja je u $MST$ je tačka $5$ na distanci najviše $\epsilon$. Za ostale tačke (čvorove, i tačke na granama). svaka je sama sebi na distanci $0$, tj. najviše $\epsilon$. U ovom primeru je moguće da Perica uzme ceo $MST$, tj. svih 5 tačaka. Ovaj primer je ilustrativan, u test primerima koji se boduju nije moguće dobiti $\epsilon = 0.25$ u ulazu.
	## Ograničenja  
	- $1 \leq n \leq 20000$  
	- $0 \leq x_i,y_i \leq 1$
	- $10^{-3} \leq \epsilon \leq 1$
	
	Test primeri su podeljeni u $5$ disjunktnih grupa:
	 - U testovima vrednim $10$ poena: važi $n \leq 20, \epsilon = 0.01$.
	 - U testovima vrednim $20$ poena: važi $n \leq 1000$ i $\epsilon = 0.2$.  
	 - U testovima vrednim $20$ poena: važi $\epsilon = 10^{-3}$  
	 - U testovima vrednim $50$ poena: $\epsilon = 0.05$ ili $\epsilon = 0.1$. 
	
=== "Rešenje"
	
	| Autor | Tekst i test primeri | Analiza rešenja | Testiranje |
	|:-:|:-:|:-:|:-:|
	| Marko Milenković | Uroš Kostadinović | Uroš Kostadinović | Aleksa Danić i Marko Milenković |
	
	## Rešenje kada je $\epsilon = 10^{-3}$
	
	U ovom slučaju dovoljno je naći $MST$ za ove tačke. Za svaku tačku ćemo dodati samo određene grane koje je sadrže i primeniti Kruskalov algoritam za $MST$. Posmatrajmo neku tačku $A$ i podelimo ravan u $8$ kvadranta tako da je $A$ u centru. Nikada u $MST$-u neće biti optimalno da uzmemo dve grane koje sadrže $A$, npr. grane koje spajaju tačke $A$ i $B$ i tačke $A$ i $C$, iz istog oktanta jer će važiti $dist(B,C) \leq max(dist(A,B),dist(A,C))$, gde $dist(X,Y)$ označava Menhetn distancu između tačaka $X$ i $Y$. Ovo znači da možemo za svaku tačku posmatrati samo po najkraću granu u svakom oktantu. Potrebno je još pronaći za svaku tačku koja joj je najbliža u svakom njenom oktantu. Pretpostavimo da tražimo samo najbližu tačku u jednom oktantu, ostali slučajevi su isti do na rotaciju. Distanca od tačke $A$ do neke tačke iz njenog oktanta, npr. $B$, će biti $B_x-A_x+B_y-A_y = (B_x+B_y)-(A_x+A_y)$. Za svako $k$ čuvaćemo u Fenvikovom stablu minimalnu vrednost zbira koordinata tačaka koje smo prošli do sad koje imaju razliku $x$ i $y$ koordinate manju od $k$. Sortiraćemo tačke prvo po $y$ koordinati opadajuće i ići redom kroz njih. Kada želimo da nađemo najbližu tačku u oktantu za tačku $A$ samo ćemo naći vrednost u Fenvikovom stablu za $k = A_x-A_y$ i nakon toga ažurirati vrednost na poziciji $A_x-A_y$ sa $A_x+A_y$. Nakon što dodamo sve grane ćemo primeniti Kruskalov algoritam za nalaženje $MST$-a. Vremenska složenost: $O(nlogn)$.
	
	## Rešenje za 100 bodova
	
	Podelimo $[0,1]^2$ na kvadratiće stranice dužine $\frac{\epsilon}{3}$. Kontrakovaćemo graf tako što će nam u novom grafu čvorovi biti kvadratići, a grana između dva kvadrata biti najmanja distanca neke tačke iz prvog i neke tačke iz drugog. Neka je $F$ minimalno razapinjuće stablo ovog kontrakovanog grafa. Stablo $F$ ćemo naći tako što ćemo prvo za svaki kvadratić sve tačke u njemu spojiti po ceni $0$ i onda primeniti Kruskalov algoritam posmatrajući sve iste grane kao u prethodnom podzadatku. Zbog ovoga svaka grana u $F$ mora da bude i u $MST$ i svaka grana iz $MST$ dužine veće od $\frac{2\epsilon}{3}$ mora da bude i u $F$. Tačke iz grana iz originalnog grafa koje smo dodali u $F$ će nam činiti skup $Q$, a grane iz originalnog grafa koje smo dodali u $F$ će nam zajedno sa proizvoljnim granama unutar kvadratića činiti stablo $T$. Svaka grana iz $T$ ili pripada $MST$-u ili cela pripada nekom kvadratiću koji sadrži tačku iz $MST$, pa svaka tačka na $T$ ima sebi $\epsilon$-blizu tačku iz $MST$. Jedine grane iz $MST$ koje nisu u $T$ imaju dužinu maksimalno $\frac{2\epsilon}{3}$. Posmatrajmo jednu takvu granu koja spaja tačke $A$ i $B$. Neka je tačka $C$ na toj grani i neka joj je bez umanjenja opštosti tačka $A$ bliža od tačke $B$, tj. $dis(A,C) \leq \frac{\epsilon}{3}$. Za tačku $A$ postoji tačka $X$ iz njenog kvadratića koja je na distanci  maksimalno $\frac{2\epsilon}{3}$, pa će zbog nejednakosti trougla važiti $dis(C,X) \leq dis(C,A)+dis(A,X) \leq \frac{\epsilon}{3} + \frac{2\epsilon}{3} = \epsilon$, što znači da stablo $T$ zadovoljava uslov zadatka. Vremenska složenost: $O(nlogn)$.
	
	``` cpp title="10_laganje.cpp" linenums="1"
	#define here cerr<<"===========================================\n"
	#define dbg(x) cerr<<#x<<": "<<x<<endl;
	#include "bits/stdc++.h"
	//#include <ext/pb_ds/tree_policy.hpp>
	//#include <ext/pb_ds/assoc_container.hpp>
	#define ld long double
	#define ll long long
	#define llinf 100000000000000000LL // 10^17
	#define pb push_back
	#define popb pop_back
	#define fi first
	#define sc second
	#define endl '\n'
	#define pll pair<ll,ll>
	#define pld pair<ld,ld>
	#define all(a) a.begin(),a.end()
	#define ceri(a,l,r) {cerr<<#a<<": ";for(ll i_ = l;i_<=r;i_++) cerr<<a[i_]<< " ";cerr<<endl;}
	#define cer(a) {cerr<<#a<<": ";for(ll x_ : a) cerr<<x_<< " ";cerr<<endl;}
	#define yes cout<<"YES"<<endl
	#define no cout<<"NO"<<endl
	#define si(s) (ll)(s.size())
	
	#define daj_mi_malo_vremena ios_base::sync_with_stdio(false);cerr.tie(0);cout.tie(0);cin.tie(0);
	
	using namespace std;
	mt19937_64 rng(chrono::steady_clock::now().time_since_epoch().count());
	ll rnd(ll l,ll r){
	    return uniform_int_distribution<ll>(l,r)(rng);
	}
	
	struct Point{
	    ld x, y;
	    ll id;
	};
	const ll maxn = 100005;
	const ll maxm = 505;
	ll n;
	ld eps;
	Point a[maxn];
	vector<pll> edg;
	ll dsu[maxn];
	ll root(ll i){
	    while(dsu[i]!=i){
	        dsu[i] = dsu[dsu[i]];
	        i = dsu[i];
	    }
	    return i;
	}
	bool upd(ll i,ll j){
	    i = root(i);
	    j = root(j);
	    if(i==j) return 0;
	    dsu[i] = j;
	    return 1;
	}
	ll dis(pll c){
	    ll i = c.fi,j = c.sc;
	    return floor(100000000000000000LL*(abs(a[i].x-a[j].x) + abs(a[i].y-a[j].y)));
	}
	vector<pll> ans;
	ll m = 500;
	ll klk;
	vector<ll> gr[maxm][maxm];
	vector<ll> akt[maxm*maxm];
	struct Fenwick {
	    const ld INF = 1e9;
	    vector<pair<ld,int>> t;
	    int n;
	
	    Fenwick(int n) : n(n), t(n+1, {INF, -1}) {}
	
	    void update(int i, pair<ld,int> v) {
	        for (; i <= n; i += i & -i)
	            t[i] = min(t[i], v);
	    }
	
	    pair<ld,int> query(int i) {
	        pair<ld,int> res = {INF, -1};
	        for (; i > 0; i -= i & -i)
	            res = min(res, t[i]);
	        return res;
	    }
	};
	ld malo = 1e-18;
	ll id[maxn];
	vector<pll> manhattan_mst(vector<Point> p) {
	    int n = p.size();
	    vector<pll> edges;
	    for (int rep = 0; rep < 4; rep++) {
	        sort(p.begin(), p.end(), [](auto &a, auto &b) {
	            if(abs(a.y-b.y)>1e-18) return a.y<b.y;
	            if(abs(a.x-b.x)>1e-18) return a.x<b.x;
	            return false;
	        });
	        vector<ll> ys(n);
	        for (int i = 0; i < n; i++) ys[i] = floor(100000000000000000LL*(p[i].y - p[i].x));
	        vector<ll> cp = ys;
	        sort(cp.begin(), cp.end());
	        cp.erase(unique(cp.begin(), cp.end()), cp.end());
	        for (int i = 0; i < n; i++) ys[i] = lower_bound(cp.begin(), cp.end(), ys[i]) - cp.begin() + 1;
	        Fenwick fw(n + 5);
	        for (int i = n-1; i >= 0; i--) {
	            int key = ys[i];
	            auto best = fw.query(key);
	            if (best.second != -1) {
	                int j = best.second;
	                ld dist = best.fi-p[i].x-p[i].y;
	                edges.emplace_back(p[i].id, p[j].id);
	            }
	            fw.update(key, {p[i].x + p[i].y, i});
	        }
	        for (auto &pt : p) {
	            ld tx = pt.x;
	            pt.x = pt.y;
	            pt.y = tx;
	        }
	        if (rep == 1) {
	            for (auto &pt : p) pt.x = -pt.x;
	        }
	    }
	    return edges;
	}
	ll kod(ll x,ll y){
	    x++; y++;
	    return (m+1)*(y-1)+x;
	}
	vector<Point> sve;
	long double truncate(long double x) {
	    const long double factor = 1e17;
	    return std::trunc(x * factor) / factor;
	}
	bool tu[maxn];
	void tc(){
	    cin >> n >> eps;
	    for(ll i = 1;i<=n;i++){
	        cin >> a[i].x >> a[i].y;
	        a[i].id = i;
	    }
	    klk = 18/(eps*eps);
	    if(klk>=n){
	        dbg(eps);
	        for(ll i = 1;i<=n;i++) sve.pb(a[i]);
	         vector<pll> edg = manhattan_mst(sve);
	        sort(all(edg),[](auto &a,auto &b){
	            return dis(a)<dis(b);
	        });
	        iota(dsu+1,dsu+1+n,1);
	        vector<bool> tu(n+1,0);
	        for(pll p : edg){
	            ll i = p.fi,j = p.sc;
	            if(upd(i,j)){
	                ans.pb({i,j});
	            }
	        }
	        cout<<si(ans)+1<<endl;
	        for(ll i = 1;i<=n;i++) cout<<i<<" ";
	        cout<<endl;
	        for(pll p : ans) cout<<p.fi<< " "<<p.sc<<endl;
	        return;
	    }
	    ld str = eps/3;
	    str = truncate(eps/3);
	    m = floor(3/eps);
	    ll dodo = 0;
	    for(ll i = 1;i<=n;i++){
	        ll xi = floor(a[i].x/str);
	        ll yi = floor(a[i].y/str);
	        bool dodaj = 1;
	        if(xi>=m||yi>=m) dodaj = 0;
	        dodo+=dodaj;
	        if(dodaj){
	            gr[xi][yi].pb(i);
	            id[i] = kod(xi,yi);
	            sve.pb(a[i]);
	        }
	    }
	    vector<pll> edg = manhattan_mst(sve);
	    sort(all(edg),[](auto &a,auto &b){
	        return dis(a)<dis(b);
	    });
	    iota(dsu+1,dsu+1+n,1);
	    for(ll i = 0;i<=m;i++){
	        for(ll j = 0;j<=m;j++){
	            for(ll k = 0;k+1<si(gr[i][j]);k++){
	                upd(gr[i][j][k],gr[i][j][k+1]);
	            }
	        }
	    }
	    for(pll p : edg){
	        ll i = p.fi,j = p.sc;
	        if(id[i]==0||id[j]==0) continue;
	        if(upd(i,j)){
	            ans.pb({i,j});
	            akt[id[i]].pb(i);
	            akt[id[j]].pb(j);
	        }
	    }
	    iota(dsu+1,dsu+1+n,1);
	    for(pll p : ans) upd(p.fi,p.sc);
	    for(ll i = 0;i<=(m+1)*(m+1);i++){
	        sort(akt[i].begin(), akt[i].end());
	        akt[i].erase(unique(akt[i].begin(), akt[i].end()), akt[i].end());
	        for(ll k = 1;k<si(akt[i]);k++){
	            if(upd(akt[i][0],akt[i][k])){
	                ans.pb({akt[i][0],akt[i][k]});
	            }
	        }
	    }
	    vector<bool> tu(n+1,0);
	    for(pll p : ans) tu[p.fi] = tu[p.sc] = 1;
	    cout<<si(ans)+1<<endl;
	    for(ll i = 1;i<=n;i++) if(tu[i]) cout<<i<<" ";
	    cout<<endl;
	    for(pll p : ans) cout<<p.fi<<" "<<p.sc<<endl;
	}
	int main(){
		daj_mi_malo_vremena
	    int t; t = 1;
	    while(t--){
	        tc();
	    }
		return 0;
	}

	```
