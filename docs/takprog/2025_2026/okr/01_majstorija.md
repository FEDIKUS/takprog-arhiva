---
hide:
  - toc
---

# B1 - Majstorija

=== "Zadatak"
	
	| Vremensko ograničenje | Memorijsko ograničenje |
	|:-:|:-:|
	| 1000ms | 256MB |
	
	<br>
	
	Svi znaju da je Mars svetski putnik. A samo svetskim putnicima se dešavaju nezgode. Ovoga puta, iskusni komisionar se izgubio na ostrvu punom ljutih takmičara. 
	
	<br>
	
	Da bi bio vidljiv i da bi ga Komisija spasila sa ostrva svojim službenim helikopterom, on mora da nacrta u pesku matricu dimenzija $N \times M$. U svako polje te matrice ucrtaće ili broj $0$ ili broj $1$. 
	
	<br>
	
	Ipak, nije tako prosto. Da bi se opravdalo trošenje goriva za helikopter, Marsova matrica mora da zadovolji uslove:
	
	- u redu $i$ (za $i=1,2,\ldots,N$), suma brojeva mora da bude deljiva sa $i$
	- u koloni $j$ (za $j=1,2,\ldots,M$), suma brojeva mora da bude deljiva sa $j$
	- svaki red i svaka kolona moraju da imaju po barem jednu jedinicu u sebi
	
	<br>
	
	Pomognite Marsu tako što ćete mu reći da li je moguće da nacrta takvu matricu, i ako je moguće, dajte mu primer jedne bilo koje takve matrice. Inače, moraće da čita žalbe ljutih takmičara.
	
	## Opis ulaza
	
	<br>
	
	U prvoj liniji standardnog ulaza dat je jedan prirodan broj $T$ - broj test primera.
	
	<br>
	
	U narednih $T$ linija standardnog ulaza data su dva prirodna broja $N$ i $M$ - broj redova i kolona matrice u tom test primeru.
	
	<br>
	
	
	## Opis izlaza
	
	<br>
	
	Za $i$-ti (za $i = 1,2,\ldots, T$) test primer:
	 - ukoliko ne postoji tražena matrica, ispisati $-1$
	 - u suprotnom, ispisati **bilo koju matricu** koja zadovoljava uslove zadatka.
	
	
	## Primer 1
	
	<br>
	
	### Ulaz
	
	<br>
	
	```
	2
	1 6
	4 4
	```
	
	<br>
	
	### Izlaz
	
	<br>
	
	```
	-1
	1 1 1 1
	1 0 0 1
	1 0 1 1
	1 1 1 1
	```
	
	<br>
	
	### Objašnjenje 
	
	Može se pokazati da ne postoji nijedna matrica dimenzija $N= 1, M = 6$, koja zadovoljava uslove zadatka.
	
	<br>
	
	U drugom primeru, kada je $N = M = 4$, onda možemo videti da je suma brojeva:
	- u prvom redu jednaka $4$, što je deljivo sa jedan
	- u drugom redu jednaka $2$, što je deljivo sa dva
	- u trećem redu jednaka $3$, što je deljivo sa tri
	- u četvrtom redu jednaka $4$, što je deljivo sa četiri
	
	Takođe, možemo izračunati da je suma brojeva:
	- u prvoj koloni jednaka $4$, što je deljivo sa jedan
	- u drugoj koloni jednaka $2$, što je deljivo sa dva
	- u trećoj koloni jednaka $3$, što je deljivo sa tri
	- u četvrtoj koloni jednaka $4$, što je deljivo sa četiri
	
	Time smo našli matricu koja zadovoljava uslove.
	
	<br>
	
	## Ograničenja
	
	<br>
	
	 - $1 \leq T \leq 3$
	 - $1 \leq N\cdot M \leq 1.000.000$.
	
	<br>
	
	Test primeri su podeljeni u četiri disjunktne grupe:
	 - U test primerima vrednim $10$ poena, važi da $NM \leq 20$.
	 - U test primerima vrednim $10$ poena, važi da $NM \leq 30$.
	 - U test primerima vrednim $25$ poena, važi da $NM \leq 45$.
	 - U test primerima vrednim $55$ poena, nema dodatnih ograničenja.
	
=== "Rešenje"
	
	| Autor | Tekst i test primeri | Analiza rešenja | Testiranje |
	|:-:|:-:|:-:|:-:|
	| Marko Milenković | Marko Milenković | Marko Milenković | Aleksa Milisavljević |
	
	### $NM \leq 20$
	
	U ovom podzadatku možemo proveriti za svaku konfiguraciju matrice da li zadovoljava uslove. Odnosno, za svako polje matrice imamo dve opcije - ili je nula ili je jedinica u njemu. Ukupno onda imamo $2^{NM}$ opcija. Isprobavanjem svake od tih opcija možemo da utvrdimo da li postoji validna.
	
	Složenost ovog pristupa je $\mathcal{O}(NM2^{NM})$.
	
	### $NM \leq 30$
	
	Iz uslova da broj jedinica u redu $i$ mora biti deljiv brojem $i$, možemo da zaključimo da neki redovi moraju da budu prilično puni. Na primer, poslednji red i poslednja kolona moraju biti skroz popunjeni. Uz ovu konstataciju možemo smanjiti broj mogućnosti u prethodnom podzadatku.
	
	
	### $NM \leq 45$
	
	Možemo primetiti da nema mnogo opcija koje nam daju $NM \leq 45$. Za ovaj podzadatak možemo da izračunamo na svom računaru (koristeći prethodne optimizacije) i to sačuvamo u memoriju.
	
	### Bez dodatnih ograničenja
	
	Lako primećujemo da ukoliko je $N \neq M$, rešenje ne postoji. Zašto? Neka važi da ima više redova nego kolona (simetrično rezonovanje radi u suprotnom slučaju). Onda poslednjni red mora da ima barem $N$ jedinica (da bi ispunio deljivost, a setimo se, ne sme da ima nula jedinica po tekstu zadatka). Međutim, kako ima $M < N$ kolona, to je nemoguće. Dakle, na dalje rezonujemo samo slučaj $N = M$.
	
	Postoji više odgovarajućih konstrukcija za rešavanje ovog zadatka. Čini se da je najprostija da se jedinice stave na sporednoj dijagonali matrice i na sva polja ispod nje. Formalni uslov bi bio, popunimo jedinicama sva polja za koja važi $i + j >= N+1$. Onda će red/kolona $i$ imati tačno $i$ jedinica. 
	
	
	Vremenska složenost je $O(NM)$. 
	
	``` cpp title="01_majstorija.cpp" linenums="1"
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
	
	signed main()
	{
		ios_base::sync_with_stdio(false); 
		cin.tie(nullptr); 
		cout.tie(nullptr); 
		cerr.tie(nullptr);	
	
		int t;
		cin >> t;
	
		while(t--){
			int n, m;
			cin >> n >> m;
	
	
			if (n != m){
				cout << "-1\n";
				continue;
			}
	
			for (int i = 1; i <= n; ++i){
				for (int j = 1; j <= m; ++j){
					if (i + j >= n + 1)
						cout << "1 ";
					else 
						cout << "0 ";
				}
				cout << '\n';
			}
		}
	}

	```
