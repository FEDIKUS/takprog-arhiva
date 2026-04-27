---
hide:
  - toc
---

# 1 - Raspored

=== "Zadatak"
	
	| Vremensko ograničenje | Memorijsko ograničenje |
	|:-:|:-:|
	| 1000ms | 256MB |
	
	<br>
	
	Grupa turista je odlučila da vidi svih $N$ eksponata jednog muzeja. Kako eksponata ima mnogo, žele da poseta muzeju bude dobro isplanirana. Grupa će u svakom od $N$ vremenskih trenutaka posetiti tačno jedan eksponat.
	
	<br>
	
	Kustos muzeja želi da pomogne svim turistima koji dolaze tako što će spremiti raspored za zajednički obilazak cele grupe. Zato je svakog od $M$ turista pitao u kom vremenskom intervalu bi želeo da bude organizovana poseta svakom eksponatu. Preciznije, $j$-ti turista želi da trenutak posete $i$-tog eksponata $T_i$ pripada intervalu $[L_{j,i},R_{j,i}]$.
	
	<br>
	
	Kustosu nije ostalo mnogo vremena do sutrašnjeg obilaska muzeja. Pomozite mu da napravi raspored koji će ispunjavati želje svih turista ili prijavite da takav raspored ne postoji.
	
	<br>
	
	## Opis ulaza
	
	<br>
	
	U prvoj liniji standardnog ulaza učitavaju se dva broja $N$ i $M$ - broj eksponata u muzeju i broj turista koji čine grupu.
	
	Narednih $2M$ linija sadrži po $N$ brojeva. Prvih $M$ linija sadrži po $N$ brojeva koji predstavljaju leve granice $L_{j,i}$, a narednih $M$ linija sadrži po $N$ brojeva koji predstavljaju desne granice $R_{j,i}$ opisanih intervala - turista $j$ želi da vreme posete $i$-tog eksponata bude između trenutaka $L_{j,i}$ i $R_{j,i}$. ($1 \leq j \leq M$, $1 \leq i \leq N$).
	
	
	<br>
	
	## Opis izlaza
	
	<br>
	
	Jedina linija standardnog izlaza treba da sadrži $N$ brojeva razdvojenih razmakom $T_1,...,T_N$, gde $T_i$ za $i \in [1,N]$ predstavlja vreme posete $i$-tog eksponata, tako da ono ispunjava uslove svih turista. Ukoliko postoji više rasporeda koji ispunjavaju zadate uslove, ispisati bilo koji. Ukoliko takav raspored ne postoji, na standardni izlaz ispisati $-1$.
	
	<br>
	
	## Primer 1 
	
	<br>
	
	### Ulaz
	
	<br>
	
	```
	4 3
	1 1 2 2
	1 1 3 2
	2 1 3 2
	
	3 2 4 4
	4 3 4 4
	4 4 4 4
	```
	
	<br>
	
	### Izlaz
	
	<br>
	
	```
	3 1 4 2
	```
	### Objašnjenje primera 1
	
	<br>
	
	Posmatrajmo prvi eksponat. Za prikazani raspored je $T_1=3$, pa važi $L_{1,1} \leq T_1 \leq R_{1,1}, L_{2,1} \leq T_1 \leq R_{2,1}$ i $L_{3,1} \leq T_1 \leq R_{3,1}$. Slično važi i za ostale eksponate. 
	
	<br>
	
	## Primer 2 
	
	<br>
	
	### Ulaz
	
	<br>
	
	```
	5 4
	1 2 1 4 5
	2 1 2 4 4
	1 1 2 4 5
	2 2 2 4 4
	
	3 4 4 5 5
	4 5 4 5 5
	4 5 3 5 5
	5 3 4 5 5
	```
	
	<br>
	
	### Izlaz
	
	<br>
	
	```
	-1
	```
	
	<br>
	
	## Primer 3 
	
	<br>
	
	### Ulaz
	
	<br>
	
	```
	3 2
	1 1 1
	1 1 1
	
	2 3 1
	2 3 3
	```
	
	<br>
	
	### Izlaz
	
	<br>
	
	```
	2 3 1
	```
	
	<br>
	
	## Ograničenja
	
	<br>
	
	- $1 \leq N \cdot M \leq 10^6$
	- $1 \leq L_{i,j} \leq R_{i,j} \leq N$
	
	<br>
	
	Test primeri su podeljeni u $7$ disjunktnih grupa:
	
	- U test primerima vrednim $5$ poena: $L_{j,i}=R_{j,i}$;
	- U test primerima vrednim $5$ poena: $N,M \leq 10$;
	- U test primerima vrednim $9$ poena: $N \leq 10$;
	- U test primerima vrednim $10$ poena: $M=1$ i $L_{j,i}=1$;
	- U test primerima vrednim $15$ poena: $M=1$ i $R_{j,i}-L_{j,i} \leq 1$;
	- U test primerima vrednim $25$ poena: $N \leq 1000$;
	- U test primerima vrednim $31$ poen: nema dodatnih ograničenja.
	
	<br>
	
=== "Rešenje"
	
	| Autor | Tekst i test primeri | Analiza rešenja | Testiranje |
	|:-:|:-:|:-:|:-:|
	| Pavle Martinović | Sofija Čebašek, Marko Trajković | Marko Trajković | Aleksa Milisavljević |
	
	## Rešenje kada je $L_{j,i}=R_{j,i}$
	U ovom podzadatku svaki turista će želeti da poseti svaki eksponat u tačno jednom trenutku. Rešenje će postojati ako i samo ako za svaki eksponat, svi turisti žele da ga posete u istom trenutku i trenuci posete svih eksponata čine permutaciju brojeva od $1$ do $N$. 
	
	Vremenska složenost: $O(NM)$
	
	## Rešenje kada je $N,M\leq10$
	Ukoliko rešenje postoji, trenuci u kojima smo posećivali eksponate će činiti permutaciju brojeva od $1$ do $N$. Za svaku permutaciju možemo proveriti da li ispunjava želje svih turista. Ukoliko takva permutacija postoji, ona će biti rešenje, u suprotnom, nema rešenja.
	
	Vremenska složenost: $O(N!\cdot NM)$
	
	## Rešenje kada je $N\leq 10$
	Vreme posete svakog eksponata će pripadati odgovarajućim intervalima svih turista, pa će pripadati i njihovom preseku. Preciznije, svaki eksponat će pripadati intervalu $[l_i,r_i]$ gde je:
	$$
	    l_i=\max_{1\leq j \leq M}L_{j,i} \\
	    r_i=\min_{1\leq j \leq M}R_{j,i} \text{.}
	$$ 
	Ukoliko za neki eksponat važi $l_i>r_i$ rešenje ne postoji, u suprotnom, kao u prethodnom podzadatku, za svaku permutaciju $t$ možemo proveriti da li ispunjava uslove, tj. da li važi $l_i\leq t_i \leq r_i$.
	
	Vrednosti $l_i$ i $r_i$ ćemo u nastavku nazivati leva granica i desna granica eksponata $i$.
	
	Vremenska složenost: $O(N!\cdot N + NM)$
	
	## Rešenje kada je $M=1$ i $L_{j,i}=1$ 
	Primetimo da nam se uvek isplati da prvo posećujemo eksponate sa najmanjim $r_i$ koje nismo posetili do sada. Sortiramo eksponate po desnoj granici. Oblazićemo ih redom od onih sa najmanjom ka onima sa najvećom desnom granicom. Ukoliko ovakav obilazak zadovoljava uslove, on će biti rešenje. U suprotnom, rešenje ne postoji.
	
	Vremenska složenost: $O(NM+N\log N)$
	
	## Rešenje kada je $M=1$ i $R_{j,i}-L_{j,i}\leq1$ 
	Posmatrajmo eksponat koji ćemo prvo posetiti. Za njega mora da važi $l_i=1$. Analogno prethodnom podzadatku, izabraćemo onaj sa najmanjim $r_i$. Krenućemo redom, od prvog do $N$-tog trenutka. U $i$-tom trenutku ćemo posmatrati neposećene eksponate kojima je leva granica $i$ ili $i-1$ tj. one čiji intervali sadrže trenutak $i$. Izabraćemo onaj sa najmanjom desnom granicom. Ukoliko takav eksponat ne bude postojao u nekom trenutku, nema rešenja. U suprotnom, konstruisali smo jedno rešenje.
	
	Vremenska složenost: $O(NM+N\log N)$
	
	## Rešenje kada je $N\leq1000$ 
	Možemo uopšiti rešenje prethodnog podzadatka. Razmatraćemo trenutke redom, od prvog do $n$-tog kao u prošlom podzadatku. U $i$-tom trenutku ćemo izabrati eksponat sa najmanjom desnom granicom među svim eksponatima koje nismo posetili i čiji intervali sadrže trenutak $i$. Ako takav eksponat ne postoji, nema rešenja, a u suprotnom smo ovim postupkom konstruisali jedno rešenje.
	
	Vremenska složenost: $O(NM+N^2)$
	
	## Glavno rešenje
	Primetimo da eksponate možemo sortirati po njihovoj levoj granici i obrađivati u tom redosledu. Ovakvim pristupom i korišćenjem struktura `std::set` ili `std::priority_queue` možemo efikasno čuvati sve eksponate u čijim intervalima je trenutak $i$ kao i efikasno naći onaj sa najmanjom desnom granicom. 
	
	Vremenska složenost: $O(NM+N\log N)$
	
	``` cpp title="01_raspored.cpp" linenums="1"
	#include <bits/stdc++.h>
	
	using namespace std;
	
	vector<int> T,lmax,rmin;
	vector<vector<int> > L,R; 
	
	int main()
	{
	    ios::sync_with_stdio(false); cin.tie(0); cout.tie(0);
	    int N,M;
	    cin >> N >> M;
	    T.resize(N+1);
	    lmax.resize(N+1,1);
	    rmin.resize(N+1,N);
	    L.resize(M+1);
	    R.resize(M+1);
	    for (int i=1;i<=M;i++)
	    {
	        L[i].resize(N+1);
	        R[i].resize(N+1);
	        for (int j=1;j<=N;j++)
	            cin >> L[i][j];
	    }
	    for (int i=1;i<=M;i++)
	    {
	        for (int j=1;j<=N;j++)
	        {
	            cin >> R[i][j];
	            lmax[j]=max(lmax[j],L[i][j]);
	            rmin[j]=min(rmin[j],R[i][j]);
	        }
	    }
	    vector<pair<pair<int,int>,int> > intervali;
	    for (int i=1;i<=N;i++)
	    {
	        intervali.push_back({{lmax[i],rmin[i]},i});
	        if (lmax[i]>rmin[i])
	        {
	            cout << -1 << "\n";
	            return 0;
	        }
	    }
	    sort(intervali.begin(),intervali.end());
	    int pos=0;
	    priority_queue<pair<int,int>,vector<pair<int,int> >,greater<pair<int,int> > > q;
	    for (int i=1;i<=N;i++)
	    {
	        while (pos<N && intervali[pos].first.first==i)
	        {
	            q.push({intervali[pos].first.second,intervali[pos].second});
	            pos++;
	        }
	        if (q.empty() || q.top().first<i)
	        {
	            cout << -1 << "\n";
	            return 0;
	        }
	        T[q.top().second]=i;
	        q.pop();
	    }
	    for (int i=1;i<=N;i++)
	        cout << T[i] << " ";
	    cout << "\n";
	    return 0;
	}

	```
