---
hide:
  - toc
---

# A3 - Intergalaktički sukob

=== "Zadatak"
	
	| Vremensko ograničenje | Memorijsko ograničenje |
	|:-:|:-:|
	| 1500ms | 256MB |
	
	O, ne! U toku je intergalaktički konflikt između Marsovaca i Nišovaca! Pomozite Nišovcima da naprave plan napada na Marsovce i time okončaju konflikt!
	
	<br>
	
	Trenutno se odvija bitka u Sukreu, dalekoj galaksiji koju možemo predstaviti kao dvodimenzionu ravan. U bici učestvuje $N$ svemirskih brodova Nišovaca i $M$ svemirskih brodova Marsovaca. Svi svemirski brodovi se nalaze na dve **paralelne** prave tako da su svi svemirski brodovi Nišovaca kolinearni, kao i svi svemirski brodovi Marsovaca. Moguće je da se te dve prave poklapaju, kao i da se više svemirskih brodova nađe na istoj koordinati.
	
	<br> 
	
	Nišovci žele da izvrše napad sa svojih K brodova, čiji su indeksi uzastopni, na K brodova Marsovaca, čiji su indeksi takođe uzastopni. Formalno, Nišovski brodovi sa indeksima $i, i+1\dots i+K-1$ će napasti Marsovske brodove sa indeksima $j,j+1\dots j+K-1$ za neko $i \in \{1,2\dots N-K+1\}$ i $j \in \{1,2\dots M-K+1\}$. Svaki od svemirskih brodova Nišovaca će se zaputiti ka tačno jednom svemirskom brodu Marsovaca i pri tome će preći euklidsku distancu između njih. Nikoja dva broda Nišovaca se neće zaputiti ka istom brodu Marsovaca. Budući da su Nišovci veoma lenji, pomozite im tako što ćete napraviti plan napada na Marsovce tako da je maksimalna distanca koju je neki svemirski brod Nišovaca prešao minimalna.
	
	<br> 
	
	Euklidska distance između tačaka sa koordinatama $(x_1,y_1)$ i $(x_2,y_2)$ se definiše kao: $\sqrt{(x_1-x_2)^2+(y_1-y_2)^2}$.
	
	<br> 
	
	**Napomena:** Za svako $1 < i < N$ važi da tačka na kojoj se nalazi brod $i$ Nišovaca pripada duži koju formiraju tačke na kojima se nalaze brodovi Nišovaca $i-1$ i $i+1$. Analogno, za svako $1 < i < M$ važi da tačka na kojoj se nalazi brod $i$ Marsovaca pripada duži koju formiraju tačke na kojima se nalaze brodovi Marsovaca $i-1$ i $i+1$.
	
	<br> 
	
	## Opis ulaza
	
	<br>
	
	Prva linija standardnog ulaza sadrži brojeve $N,M,K$ - broj svemirskih brodova Nišovaca, broj svemirskih brodova Marsovaca i broj svemirskih brodova koji će učestvovati u napadu.
	
	<br>
	
	Sledećih $N$ linija sadrže po dva broja $x_i$ i $y_i$ - koordinate na kojima se nalazi $i$-ti brod Nišovaca.
	
	<br>
	
	Sledećih $M$ linija sadrže po dva broja $x'_i$ i $y'_i$ - koordinate na kojima se nalazi $i$-ti brod Marsovaca.
	
	<br>
	
	
	## Opis izlaza
	
	<br>
	
	U prvoj liniji standardnog izlaza je potrebno ispisati kvadrat maksimalne distance koju je neki Nišovac prešao u napadu.
	
	<br>
	
	U $i$-toj od sledećih K linija potrebno je ispisati po dva broja, $x_i$ i $y_i$. Oni označavaju da će  svemirski brod Nišovaca sa indeksom $x_i$ napasti svemirski brod Marsovaca sa indeksom $y_i$
	
	<br> 
	
	Ukoliko postoji više plana napada tako da je maksimalna distanca koju je neki svemirski brod Nišovaca prešao minimalna, ispisati bilo koji.
	
	<br>
	
	## Primer 1
	
	
	### Ulaz
	
	<br>
	
	```
	3 2 2
	3 1
	5 1
	7 1
	1 5
	7 5
	```
	
	<br>
	
	### Izlaz
	
	<br>
	
	```
	20
	1 1
	2 2
	```
	
	<br>
	
	### Objašnjenje 
	
	Prvi brod Nišovaca napada prvi brod Marsovaca, što znači da će iz tačke $(3, 1)$ krenuti ka tački $(1, 5)$. Kvadrat ove udaljenosti je: $(3-1)^2+(1-5)^2 = 20$.
	
	Drugi brod Nišovaca napada drugi brod Marsovaca, što znači da će iz tačke $(5, 1)$ krenuti ka tački $(7, 5)$. Kvadrat ove udaljenosti je: $(5-7)^2+(1-5)^2 = 20$.
	
	Ako bi napad bio izvršen sa svemirskim brodovima na indeksima $2$ i $3$, bar jedan od njih bi prešao distancu čiji je kvadrat veći od $20$.
	
	<br>
	
	## Primer 2
	
	
	### Ulaz
	
	<br>
	
	```
	3 3 1
	1 4
	7 22
	9 28
	7 26
	8 29
	10 35
	```
	
	<br>
	
	### Izlaz
	
	<br>
	
	```
	2
	3 2
	```
	
	<br>
	
	## Ograničenja
	
	<br>
	 
	 $1 \le N,M,K \le 200\ 000$
	 
	 $K \le \text{min}(N,M)$
	 
	Koordinate svemirskih brodova su celi brojevi u intervalu $[1,10^9]$
	
	Sve tačke na kojima su svemirski brodovi Nišovaca leže na jednoj pravi. Sve tačke na kojima su svemirski brodovi Marsovaca leže na pravi paralelnoj sa njom.
	
	Za svako $1 < i < N$ važi da tačka na kojoj se nalazi brod $i$ Nišovaca pripada duži koju formiraju tačke na kojima se nalaze brodovi Nišovaca $i-1$ i $i+1$. Analogno, za svako $1 < i < M$ važi da tačka na kojoj se nalazi brod $i$ Marsovaca pripada duži koju formiraju tačke na kojima se nalaze brodovi Marsovaca $i-1$ i $i+1$.
	
	<br>
	
	Test primeri su podeljeni u osam disjunktnih grupa:
	 - U test primerima vrednim $3$ poena, važi $N,M \le 10$
	 - U test primerima vrednim $7$ poena, važi $N,M \le 1000$;
	 - U test primerima vrednim $10$ poena, važi $N,M \le 3000$;
	 - U test primerima vrednim $5$ poena, važi da su ili sve $x$ koordinate brodova Nišovaca manje od svih $x$ koordinata brodova Marsovaca, ili obrnuto. Važi i da su prave na kojima leže svemirski brodovi paralelne sa $x$-osom.
	 - U test primerima vrednim $8$ poena, važi $K = 1$
	 - U test primerima vrednim $12$ poena, važi $N,M \leq 50\ 000$ i $K \leq 10$ 
	 - U test primerima vrednim $40$ poena, važi $N,M \leq 50\ 000$ 
	 - U test primerima vrednim $15$ poena nema dodatnih ograničenja;
	
=== "Rešenje"
	
	| Autor | Tekst i test primeri | Analiza rešenja | Testiranje |
	|:-:|:-:|:-:|:-:|
	|  |  |  |  |
	
	
	``` cpp title="06_buenas_tackas.cpp" linenums="1"
	#include "bits/stdc++.h"
	#define x first
	#define y second
	
	using namespace std;
	
	using ll = long long;
	using pll = pair<ll,ll>;
	
	const ll maxn = 1000005;
	const ll mxdis = 2000000000000000000LL; //2*10^18
	ll n,m,k;
	pll a[maxn];
	pll b[maxn];
	
	ll dist(ll i,ll j){
	    ll dx = a[i].x-b[j].x; dx*=dx;
	    ll dy = a[i].y-b[j].y; dy*=dy;
	    return dx+dy;
	}
	ll L[maxn],R[maxn];
	bool bad[maxn];
	deque<ll> mn,mx;
	ll Ar = -1,Br = -1;
	bool check(ll dis){
	    ll j = 1;
	    for(ll i = 1;i<=n;i++){
	        while(j+1<=m&&dist(i,j)>dis&&dist(i,j)>=dist(i,j+1)) j++;
	        if(dist(i,j)>dis) bad[i] = 1;
	        else bad[i] = 0;
	        L[i] = j-i;
	    }
	    j = m;
	    for(ll i = n;i>=1;i--){
	        while(j>=2&&dist(i,j)>dis&&dist(i,j-1)<=dist(i,j)) j--;
	        if(dist(i,j)>dis) bad[i] = 1;
	        else bad[i] = 0;
	        R[i] = j-i;
	    }
	    mn.clear();
	    mx.clear();
	    ll cnt_bad = 0;
	    for(ll i = 1;i<=n;i++){
	        if(i>=k+1){
	            if(!mn.empty()&&mn.front()==i-k) mn.pop_front();
	            if(!mx.empty()&&mx.front()==i-k) mx.pop_front();
	            cnt_bad-=bad[i-k];
	        }
	        while(!mn.empty()&&R[i]<=R[mn.back()]) mn.pop_back();
	        mn.push_back(i);
	        while(!mx.empty()&&L[i]>=L[mx.back()]) mx.pop_back();
	        mx.push_back(i);
	        cnt_bad+=bad[i];
	        if(i>=k&&cnt_bad==0){
	            if(!mx.empty()&&!mn.empty()&&L[mx.front()]<=R[mn.front()]){
	                ll d = L[mx.front()];
	                Ar = i;
	                Br = i+d;
	                return 1;
	            }
	        }
	    }// sa kojim - i \in [L[i],R[i]] 
	    return 0;
	}
	ll ida[maxn];
	ll idb[maxn];
	int main(){
	    ios_base::sync_with_stdio(0); cin.tie(0);
	    cin >> n >> m >> k;
	    for(ll i = 1;i<=n;i++) cin >> a[i].x >> a[i].y;
	    for(ll i = 1;i<=m;i++) cin >> b[i].x >> b[i].y;
	    iota(ida+1,ida+1+n,1);
	    iota(idb+1,idb+1+m,1);
	    if(a[1]>a[n]){
	        reverse(a+1,a+1+n);
	        reverse(ida+1,ida+1+n);
	    }
	    if(b[1]>b[m]){
	        reverse(b+1,b+1+m);
	        reverse(idb+1,idb+1+m);
	    }
	    ll tl = 0,tr = mxdis,mid,rez = mxdis;
	    while(tl<=tr){
	        mid = (tl+tr)/2;
	        if(check(mid)){
	            rez = mid;
	            tr = mid-1;
	        }else tl = mid+1;
	    }
	    check(rez);
	    cout<<rez<<'\n';
	    for(ll i = 0;i<k;i++){
	        cout<<ida[Ar-i]<<" "<<idb[Br-i]<<'\n';
	    }
	    return 0;
	}

	```
