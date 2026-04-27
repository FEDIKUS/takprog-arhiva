---
hide:
  - toc
---

# 3 - Takmičenje

=== "Zadatak"
	
	| Vremensko ograničenje | Memorijsko ograničenje |
	|:-:|:-:|
	| 1000ms | 256MB |
	
	Komisija želi da pozove određen broj učenika na takmičenje. Takmičari se pozivaju na osnovu rang liste koja je pažljivo sastavljana, gde je svakom takmičaru dodeljen ceo broj $a_i$ koji predstavlja uspešnost takmičara. Na listi se nalazi $N$ takmičara. 
	
	Plan komisije je da pozvane učenike poređa u novu listu na proizvoljan način i tu listu objavi. Komisiji je cilj da takmičenje bude uravnoteženo, tj. da maksimalna apsolutna razlika između uspešnosti dva takmičara koja su susedna na listi bude najmanja moguća. Oni žele da razmotre $Q$ slučajeva, gde u svakom slučaju žele da na takmičenje pozovu $k_j$ takmičara. 
	
	Vaš zadatak je da za svako $k_j$ izračunate koja je najmanja maksimalna apsolutna razlika između uspešnosti dva susedna takmičara koju možemo da dobijemo birajući nekih $k_j$ od datih $N$ takmičara i ređajući ih na neki način na novu listu.
	
	Primetite da ne tražimo da izabrani takmičari imaju najveću uspešnost, već samo da apsolutna razlika u uspešnosti dva uzastopna takmičara bude najmanja moguća.
	
	## Opis ulaza
	U prvoj liniji standardnog ulaza nalaze se dva broja cela broja, $N$ i $Q$ - broj takmičara na originalnoj listi i broj slučajeva koje komisija razmatra
	
	U drugoj liniji standardnog ulaza dato je $N$ celih brojeva $a_1, a_2, ..., a_N$, gde je $a_i$ uspešnost $i$-tog takmičara
	
	U trećoj liniji standardnog ulaza dato je $Q$ celih brojeva $k_1, k_2, ..., k_Q$, gde je $k_j$ broj takmičara koje komisija planira da pozove u $j$-tom scenariju
	
	## Opis izlaza
	Na standardni izlaz ispisati $Q$ linija. U $j$-toj liniji ispisati minimalnu vrednost maksimalne apsolutne razlike u uspešnosti dva susedna takmičara do koje se može doći ako se na takmičenje poziva $k_j$ takmičara.
	
	## Primer 1
	
	<br>
	
	### Ulaz
	
	<br>
	
	```
	6 3
	15 11 12 18 13 9
	6
	5
	3
	```
	
	<br>
	
	### Izlaz
	
	<br>
	
	```
	3
	2
	1
	```
	
	### Objašnjenje:
	U prvom slučaju je $k=6$, tj. nikoga ne treba da izbacimo, pa samo treba da odredimo permutaciju datog niza koja daje najmanju maksimalnu apsolutnu razliku između dva susedna takmičara. Jedna takva permutacija je $9$ $12$ $11$ $13$ $15$ $18$ gde vidimo da je maksimalna razlika $3$, između takmičara sa vrednostima $9$ i $12$ i sa vrednostima $15$ i $18$.
	
	U drugom slučaju je $k=5$ i tu najmanju maksimalnu apsolutnu razliku između susednih takmičara možemo da dobijemo tako što izbacimo takmičara kojem je dodeljena vrednost $18$ i preostale takmičare poređamo na sledeći način: $9$ $11$ $12$ $13$ $15$. Vidimo da je maksimalna razlika $2$, koja se dostiže između takmičara sa vrednostima $9$ i $11$ i sa vrednostima $13$ i $15$.
	
	U trećem slučaju je $k=3$ i tu rezultat možemo dobiti tako što izbacimo takmičare kojima su dodeljeni brojevi $9$, $15$ i $18$, dok ostale rasporedimo na sledeći način: $11$ $12$ $13$. Vidimo da je razlika između svaka dva susedna takmičara na listi $1$.
	## Primer 2
	
	<br>
	
	### Ulaz
	
	<br>
	
	```
	7 4
	2 2 10 3 12 16 10 
	2
	3
	4
	6
	```
	
	<br>
	
	### Izlaz
	
	<br>
	
	```
	0
	1
	4
	7
	```
	
	## Primer 3
	
	<br>
	
	### Ulaz
	
	<br>
	
	```
	6 1
	2 1000 256 13 500 123
	5
	```
	
	<br>
	
	### Izlaz
	
	<br>
	
	```
	244
	```
	
	## Ograničenja
	- $1\leq N, Q\leq2\cdot10^5$
	
	- $1\leq a_i\leq10^9$, $1\leq i\leq N$
	
	- $2\leq k_j\leq N$, $1\leq j\leq Q$
	
	Test primeri su odvojeni u $5$ disjunktnih grupa:
	
	- U testovima vrednim $11$ poena: $N\leq 20$, $Q\leq20$
	
	- U testovima vrednim $11$ poena: $Q=1$, $k_1=N$
	
	- U testovima vrednim $15$ poena: $Q=1$
	
	- U testovima vrednim $25$ poena: $Q\leq300$
	
	- U testovima vrednim $38$ poena: bez dodatnih ograničenja
	
=== "Rešenje"
	
	| Autor | Tekst i test primeri | Analiza rešenja | Testiranje |
	|:-:|:-:|:-:|:-:|
	| Marko Milenković | Anja Dožić | Anja Dožić | Aleksa Milisavljević |
	
	## Podzadatak 2: $Q=1, k_1=N$
	U ovom podzadatku ne treba da izbacimo nikoga, pa nam je jedini cilj da vidimo koja permutacija datog niza nam daje najmanju maksimalnu razliku između susednih elemenata. 
	
	Primetimo da nam je optimalno da elemente sortiramo, jer se tada svaki element nalazi između njemu dva najbliža elementa tj. kada je niz sortiran sve razlike će biti minimalne. Sada kada to znamo, možemo samo sortirati niz i jednom proći kroz njega kako bismo našli maksimalnu razliku koja se pojavljuje.
	
	Vremenska složenost: $O(N\cdot log N)$
	
	## Podzadatak 3: $Q=1$
	U ovom podzadatku koristićemo zaključak iz prethodnog zadatka, te se ovaj podzadatak svodi na pronalaženje podniza dužine $k$ u sortiranom nizu koji ima najmanju maksimalnu apsolutnu razliku između susednih elemenata. Primetimo da nema smisla uzimati nešto što nije podniz, jer izbacivanjem elemenata između dva elementa u sortiranom nizu, maksimalna razlika može da bude samo veća ili jednaka od početne.
	
	Za početak ćemo napraviti niz razlika između susednih elemenata i zatim nad njim napraviti segmentno stablo. Pomoću tog stabla ćemo naći maksimalne razlike u svim podnizima dužine $k$ i od njih izabrati najmanju.
	
	Vremenska složenost: $O(N\cdot logN)$
	
	## Podzadatak 4: $Q\leq300$
	Kao i u prošlom podzadatku, i ovde treba da nađemo podniz dužine $k_i$, za svako $1\leq i\leq Q$ koji ima najmanju maksimalnu apsolutnu razliku. Ovde ćemo za to koristiti $deque$ i niz razlika koji je korišćen i u prethodnom zadatku.
	
	U $deque$-u ćemo čuvati pozicije elemenata i dodavaćemo ih na sledeći način: ako je element na poziciji $i$ veći od elementa na poziciji sa kraja reda, poziciju sa kraja reda sklanjamo jer znamo da nam razlika na toj poziciji neće biti relevantna kada ubacimo poziciju $i$. Sklanjamo sve pozicije elementa iz reda, dok ne dođemo do prve za koju je njen element veći od elementa na poziciji $i$, kada se to desi, indeks $i$ stavljamo na kraj reda. Primetimo da će razlike poređane po redu u kom su indeksi uneseni u $deque$ biti sortirane opadajuće.
	
	Za prvih $k-1$ elemenata, samo ćemo dodavati indekse na ranije objašnjen način, dok ćemo od $k$-tog, nakon dodavanja u red, krenuti da tražimo maksimalan u odgovarajućem intervalu. To radimo tako što krećemo od početka reda, gde će se nalaziti pozicija najveće sačuvane razlike na koju smo do tog trenutka naišli i gledamo da li ona pripada podnizu koji se završava na poziciji koju u tom trenutku posmatramo. Ako ne pripada, brišemo tu poziciju sa početka reda i nastavljamo dalje dok ne naiđemo do one koja pripada. Vrednost na njoj je maksimalna vrednost za posmatrani podniz.
	
	Vremenska složenost: $O(Q\cdot N)$
	
	## Podzadatak 5: Bez dodatnih ograničenja
	Za celo rešenje, prvo ćemo sortirati niz razlika, ali tako da zapamtimo koja razlika je bila na kojoj poziciji. Nakon tog sortiranja ćemo redom da "aktiviramo" razlike od najmanje ka najvećoj i da ih spajamo u grupe ako su susedne.
	
	Kada aktiviramo razliku na poziciji $i$, proveravaćemo da li su razlike na pozicijama $i-1$ i $i+1$ aktivirane, i ako neka od njih jeste, njenu grupu spajamo sa razlikom na poziciji $i$. To spajanje možemo izvršiti primenjujući $DSU$, ili jednostavno pamteći najlevlji i najdešnji element svake grupe, i apdejtujući ih nakon spajanja.
	
	Kada spojimo dve grupe dužina $m$ i $n$ preko razlike $i$, dobićemo grupu dužine $m+n+1$ i znaćemo da je najveća razlika u njoj upravo razlika na poziciji $i$ jer je ona poslednja aktivirana a znamo da ih aktiviramo u rastućem redosledu. Tada ćemo u poseban niz $ans$, gde je $ans[i]$ najmanja maksimalna razlika koja može da se dobije za $k=i$, uneti vrednost razlike $i$ ako je ona manja od trenutne vrednosti za $ans[m+n+1]$. Na kraju moramo još jednom proći kroz niz $ans$ kako bismo popunili razlike za one dužine koje nismo dobili pri spajanju. Pošto važi da je rešenje monotono (za veće k odgovor ne može biti manji), možemo propagirati vrednosti unazad: $ans[k] = min(ans[k], ans[k+1])$.
	
	Na kraju svaki upit možemo odgovoriti u $O(1)$.
	
	Vremenska složenost: $O(N\cdot logN)$
	
	``` cpp title="03_takmicenje.cpp" linenums="1"
	#include <bits/stdc++.h>
	
	using namespace std;
	typedef long long ll;
	
	int N, Q;
	ll a[200020], k[200020], ans[200020];
	int l[200020], r[200020], len[200020];
	bool on[200020];
	pair<ll, int>d[200020];
	
	int main()
	{
	    cin>>N>>Q;
	    for(int i=1; i<=N; i++)
	    {
	        cin>>a[i];
	        ans[i]=1e9;
	    }
	    for(int i=1; i<=Q; i++)cin>>k[i];
	
	    sort(a+1, a+N+1);
	    for(int i=1; i<N; i++)d[i]={a[i+1]-a[i], i};
	    sort(d+1, d+N);
	
	    for(int i=1; i<N; i++)
	    {
	        int pos=d[i].second;
	        on[pos]=true; l[pos]=pos; r[pos]=pos; len[pos]=1;
	        if(on[pos-1])
	        {
	            l[pos]=l[pos-1];
	            r[l[pos]]=r[pos];
	            len[pos]=len[l[pos]]+1;
	            len[l[pos]]=len[pos];
	        }
	        if(on[pos+1])
	        {
	            r[pos]=r[pos+1];
	            l[r[pos]]=l[pos];
	            r[l[pos]]=r[pos];
	            len[l[pos]]+=len[r[pos]];
	            len[r[pos]]=len[l[pos]];
	            len[pos]=len[l[pos]];
	        }
	        if(ans[len[pos]+1]==1e9)ans[len[pos]+1]=d[i].first;
	    }
	    for(int i=N-1; i>1; i--)
	    {
	        ans[i]=min(ans[i+1], ans[i]);
	    }
	
	    for(int i=1; i<=Q; i++)
	    {
	        cout<<ans[k[i]]<<endl;
	    }
	    return 0;
	}

	```
