---
hide:
  - toc
---

# 4 - Daltonizacija

=== "Zadatak"
	
	| Vremensko ograničenje | Memorijsko ograničenje |
	|:-:|:-:|
	| 2000ms | 128MB |
	
	
	<br>
	
	Braća Dalton su ponovo pobegla iz ozloglašenog teksaškog zatvora!
	
	Prvom prilikom su zaustavili voz i u njemu pronašli niz sa $N$ nft-ova. $i$-ti nft ima vrednost $a_i$. Odlučili su da podele ove nft-ove na nesvakidašnji način. Braće ima $M$ i oni redom ciklično uzimaju po jedan nft - ili sa početka ili sa kraja niza. Oni ponavljaju ovaj proces dokle god ima nft-ova na raspolaganju. Kako nisu mnogo složni, svaki brat se pita koliko bi novca najviše mogao da zaradi, ukoliko bi se preostala braća urotila protiv njega i donosila odluke tako da minimizuju njegov profit (bez obzira što to možda nije optimalno za njihovu individualnu dobit).
	 
	<br>
	
	## Opis ulaza
	
	<br>
	
	U prvoj liniji standardnog ulaza data su dva cela broja $N$ i $M$, redom broj nft-ova u nizu i broj braće.
	
	<br>
	
	U drugoj i poslednjoj liniji standardnog ulaza, nalazi se niz $a$ koji se sastoji od $N$ celih brojeva.
	
	<br>
	
	## Opis izlaza
	
	<br>
	
	U jednoj liniji standardnog izlaza ispišite $M$ vrednosti. $i$-ta vrednost predstavlja profit $i$-tog brata, ukoliko se preostala braća urote protiv njega.
	
	
	<br>
	
	## Primer 1
	
	<br>
	
	### Ulaz
	
	<br>
	
	```
	3 3
	1 2 3
	```
	
	<br>
	
	### Izlaz
	
	<br>
	
	```
	3 2 1
	```
	
	### Objašnjenje
	
	<br>
	
	Pošto je $N = M$, svaki brat će dobiti po jedan nft:
	* Prvi brat je prvi na potezu i može da uzme treći nft koji ima vrednost $3$.
	* Drugi brat igra posle prvog. Da bi sprečio drugog brata da uzme nft sa vrednošću $3$, prvi brat će ga pokupiti u prvom potezu. Drugi brat će onda moći da uzme nft koji ima vrednost $2$.
	* Treći brat je poslednji. Prva dva brata će izabrati nft-ove tako da njemu ostane nft sa minimalnom vrednošću - tj. nft sa vrednošću $1$.
	
	<br>
	
	## Primer 2
	
	<br>
	
	### Ulaz
	
	<br>
	
	```
	13 4
	12 6 4 7 3 9 12 5 4 9 12 7 12
	```
	
	<br>
	
	### Izlaz
	
	<br>
	
	```
	26 23 19 19
	```
	
	<br>
	
	## Ograničenja
	
	
	<br>
	
	
	- $1 \leq M \leq N \le 10.000$ 
	
	- $1 \leq a_i \leq 100.000$ za svako $1 \leq i \leq N$
	
	
	<br>
	
	Test primeri su podeljeni u $6$ disjunktnih grupa:
	
	
	   - U testovima vrednim $4$ poena: važi $a_i = 1$ za svako $1 \leq i \leq N$ i $N \leq 300$
	   - U testovima vrednim $8$ poena: važi $N \leq 20$
	   - U testovima vrednim $16$ poena: važi $M = 2$ i $N \leq 300$
	   - U testovima vrednim $24$ poena: važi $N \leq 300$
	   - U testovima vrednim $32$ poena: važi $N \leq 4.000$
	   - U testovima vrednim $16$ poena: bez dodatnih ograničenja.
	
	<br>
	
	
	
	
=== "Rešenje"
	
	| Autor | Tekst i test primeri | Analiza rešenja | Testiranje |
	|:-:|:-:|:-:|:-:|
	| Marko Milenković | Aleksa Milisavljević | Aleksa Milisavljević | Miloš Milutinović |
	
	## Rešenje kada je $a_i = 1$ za svako $1 \leq i \leq N$ i $N \leq 300$
	U ovom podzadatku važi da svi nft-ovi imaju istu vrednost, te je svakom bratu potpuno svejedno da li uzima nft sa početka ili nft sa kraja. $i$-ti brat će ukupno imati onoliko nft-a u vrednosti koliko puta će biti na potezu.
	
	## Rešenje kada je $N \leq 20$
	U ovom podzadatku za svakog brata možemo da rekurzivno simuliramo sve moguće njegove odluke i odluke ostalih. Ovo rešenje radi u vremenskoj složenosti $O(N \cdot 2^N)$.
	
	## Rešenje kada je $M = 2$ i $N \leq 300$
	U ovom podzadatku postoje samo dva brata, te važi da je obojici cilj da prikupe što više (tj. ne moramo da analiziramo njihove profite nezavisno). Za ovaj i naredne podzadatke rešenje pronalazimo korišćenjem tehnika dinamičkog programiranja. Označimo sa $s(l,r)$ sumu $a_l + a_{l+1} + ... + a_{r-1} + a_r$. Neka je $dp[i][l][r]$ zarada $i$-tog brata ako su ostali nft-ovi na pozicijama između $l$ i $r$ i brat $i$ je na potezu. Primetimo da u tom slučaju je zarada brata koji nije $i$-ti upravo $s(l,r)-dp[i][l][r]$, tj. uzeće sve ono što nije uzeo $i$-ti brat. Tada je $dp[1][l][r] = \max(a_l + (sum(l+1,r) - dp[2][l+1][r]),a_r + (sum(l,r-1) - dp[2][l][r-1]))$ i slično tome $dp[2][l][r] = \max(a_l + (sum(l+1,r) - dp[1][l+1][r]),a_r + (sum(l,r-1) - dp[1][l][r-1]))$. Primetimo da je dinamičko programiranje neophodno konstruisati rastuće u odnosu na dužinu intervala $[l,r]$.
	
	Konačno prvi brat će imati ukupno $dp[1][1][N]$, dok će drugi imati $sum(1,N) - dp[1][1][N]$. Ovo rešenje radi u vremenskoj složenosti $O(N^2)$ i memorijskoj složenosti $O(N^2)$.
	
	## Rešenje kada je $N \leq 300$
	U ovom podzadatku moramo da generalizujemo rešenje iz prethodnog podzadatka. Primetimo prvo da broj nft-ova koji su preostali u nizu jednoznačno određuje brata koji je na potezu. Neka je $b(l,r)$ brat koji je na potezu ako su ostali samo nft-ovi između pozicija $l$ i $r$. Ovim eliminišemo jednu dimenziju dinamičkog programiranja iz prethodnog podzadatka. Dakle, $dp[l][r]$ predstavlja profit brata $b(l,r)$ ukoliko se preostala braća urote protiv njega. Neka je $b(l,r)=i$. On će u tom potezu izabrati ili $a_l$ ili $a_r$. Pretpostavimo da je izabrao $a_l$. Primetimo da se nakon poteza preostale braće broj nft-ova u nizu smanjio za tačno $M-1$. Prema tome, naredni put kada brat $i$ bude na potezu, preostaće mu da bira sa početka ili sa kraja jednog od intervala $[l+1,r-M+1]$, $[l+2,r-M+2]$, ..., $[l+M-1,r-1]$, $[l+M,r]$. Kako su se preostalih $M-1$ braće urotili protiv njega, znamo da su oni odluke donosili tako da njegova ukupna zarada bude što manja moguća. Dakle, bratu $i$ će preostati interval sa najmanjom zaradom, tj. zaradiće $\min(dp[l+1][r-M+1],...,dp[l+M][r])$. Slična analiza radi i u slučaju da on odabere nft $a_r$. Konačno, ovo dinamičko programiranje možemo da računamo formulom: $dp[l][r] = \max(a_l + \min(dp[l+1][r-M+1],...,dp[l+M][r]), a_r + \min(dp[l][r-M],...,dp[l+M-1][r-1]))$.
	
	Da bi dobili rešenje za $i$-tog brata, moramo da analiziramo intervale kada će on biti prvi put na potezu i da odaberemo onaj koji ima najmanju vrednost, tj. $\min(dp[1][N-i+1],dp[2][N-i+2],...,dp[i][N])$. Ovo rešenje radi u vremenskoj složenosti $O(N^3)$ i memorijskoj složenosti $O(N^2)$.
	
	## Rešenje kada je $N \leq 4.000$
	U ovom podzadatku možemo da primetimo da je moguće iskoristiti strukturu podataka na rešenju iz prethodnog podzadatka. Primetimo da intervali od kojih tražimo onaj sa minimalnom vrednošću u formuli za računanje dinamičkog programiranja svi imaju istu dužinu i da su ti intervali uzastopni sa tom dužinom (tj. počeci svaka dva susedna se razlikuju za tačno $1$). Prema tome, možemo da konstruišemo segmentno stablo za svaku dužinu. U svakom čvoru segmentnog stabla čuvamo minimum za neki uzastopni skup intervala.
	
	Ovo rešenje radi u vremenskoj složenosti $O(N^2 \log N)$ i memorijskoj složenosti $O(N^2)$.
	
	## Glavno rešenje
	U ovom podzadatku moramo da optimizujemo vremensku i memorijsku složenost iz prethodnog podzadatka. Prvo, primetimo da je računanje rešenja za svakog brata potpuno nezavisno i da se ne oslanja na vrednosti dinamičkog programiranja za ostalu braću. Primetimo i da rešenje za $i$-tog brata isključivo zavisi od njegovog prvog sledećeg poteza. Prema tome, možemo svakog brata da procesiramo nezavisno i rastuće po dužini intervala koji razmatramo. Pretpostavimo da smo izračunali rešenje za sve intervale dužine $d$. U narednom koraku računamo rešenje za sve intervale dužine $d+M$. Čim to rešenje izračunamo, podaci o dužini $d$ nam više ne trebaju. Jedan način da izračunamo rešenje za intervale dužine $d+M$ je da primenimo strukturu iz prethodnog podzadatka. Ovim dobijamo rešenje vremenske složenosti $O(N^2 \log N)$ i memorijske složenosti $O(N)$.
	
	Da bi optimizovali i vremensku složenost, moramo da primetimo i da je broj intervala u svakom od minimuma dinamičkog programiranja tačno $M$. Prema tome možemo da primenimo _sliding window_ tehniku. Procesiramo grupu od prvih $M$ uzastopnih intervala dužine $d$. Potom se pomerimo na desno za jednu poziciju (tj. izbacimo prvi interval iz grupe i ubacimo prvi naredni). Procesiraćemo na ovaj način jednu po jednu grupu od $M$ intervala dužine $d$ i svaki put pronalaziti minimum.
	
	Održavaćemo _deque_ (tj. red sa dva kraja). Kada se pomerimo na desno za jedan, prvo proverimo da li je interval na početku reda još uvek deo grupe. Ukoliko nije, izbacimo ga. Potom posmatramo element sa kraja reda. Sve dok element sa kraja reda ima veću ili jednaku vrednost od novog intervala u grupi, možemo da ga obrišemo sa kraja. Ovo je tačno, jer nas interesuje samo minimum, a kako se pomeramo na desno, taj interval sa većom vrednošću će biti izbačen pre intervala koji je upravo dodat u grupu koju razmatramo, te, prema tome, on nikada neće biti bolji izbor. Kada izbrišemo sve intervale sa kraja koji su imali veću ili jednaku vrednost, dodamo novi interval na kraj. Primetimo da ova konstrukcija garantuje da element koji je ispred novododatog ima strogo manju vrednost od njega. Prema tome, najmanja vrednost u celom redu je zapravo element na početku reda.
	
	Ovo rešenje radi u vremenskoj složenosti $O(N^2)$ i memorijskoj složenosti $O(N)$.
	
	``` cpp title="04_daltonizacija.cpp" linenums="1"
	#include<bits/stdc++.h>
	#define maxn 12000
	using namespace std;
	int n,m;
	int a[maxn];
	int dp[maxn];
	int ans[maxn];
	deque<pair<int,int> > dq;
	int main() {
	    cin.tie(0); ios_base::sync_with_stdio(false);
	    cin>>n>>m;
	    for(int i=0;i<n;i++) cin>>a[i];
	    for(int fl=0;fl<m;fl++) {
	        int l=fl;
	        for(int i=0;i+l<n;i++) dp[i]=max(a[i],a[i+l]);
	        while(l+m<n) {
	            dq.clear();
	            for(int i=n-1-l;i>=0;i--) {
	                while(!dq.empty() && dq.front().first>=dp[i]) dq.pop_front();
	                dq.push_front({dp[i],i});
	                if(dq.back().second==i+m) dq.pop_back();
	                dp[i]=dq.back().first;
	            }
	            l+=m;
	            for(int i=0;i+l<n;i++) dp[i]=max(a[i]+dp[i+1],a[i+l]+dp[i]);
	        }
	        ans[n-l]=1e9;
	        for(int i=0;i+l<n;i++) ans[n-l]=min(ans[n-l],dp[i]);
	    }
	    for(int i=1;i<=m;i++) cout<<ans[i]<<" ";
	    return 0;
	}

	```
