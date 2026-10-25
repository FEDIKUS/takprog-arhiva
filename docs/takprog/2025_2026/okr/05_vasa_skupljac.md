---
hide:
  - toc
---

# A2 - Vasa, skupljač aure

=== "Zadatak"
	
	| Vremensko ograničenje | Memorijsko ograničenje |
	|:-:|:-:|
	| 1000ms | 128MB |
	
	
	<br>
	
	Vasa ima $0$ aure. Vasi se to ne sviđa. 
	
	<br>
	
	Zato je odlučio da skuplja auru prolaskom kroz niz. Formalno, za dati niz celih brojeva $b$ dužine $k$, Vasa kreće od indeksa $i = 1$ sa aurom $a = 0$ i koeficijentom $c = 1$. Potom on prolazi kroz niz i redom skuplja aure elemenata tako što dodaje na svoju auru vrednost $c \cdot b_i$. Nakon što skupi auru elementa $i$, on može da poveća vrednost $c$ za jedan.
	
	<br>
	 
	Prirodno, Vasa želi da maksimizuje auru koju ima nakon prolaska kroz ceo niz (primetite da ova vrednost može da bude i negativna). Dodatno, Vasa želi da nakon prolaska kroz niz **vrednost $c$ bude tačno $x$**.
	
	<br>
	
	Dat je niz $p$ sa $n$ elemenata. Ispisati auru koju Vasa može da skupi za svaki podniz $b$ dužine tačno $k$. Primetite da se ova skupljanja odigravaju nezavisno.
	
	<br>
	
	## Opis ulaza
	
	<br>
	
	U prvom redu su data tri cela broja $n$ - dužina niza $p$, $k$ - dužine podnizova na kojima će Vasa skupljati auru, i $x$ - krajnja vrednost koeficijenta $c$.
	
	<br>
	
	U drugoj liniji standardnog ulaza, dato je $n$ celih brojeva. $i$-ti od njih je $p_i$ i predstavlja vrednost $i$-tog elementa niza $p$.
	
	<br>
	
	## Opis izlaza
	
	<br>
	
	U prvoj liniji ispisati $n-k+1$ brojeva, koji predstavljaju maksimalnu vrednost aure za svaki podniz dužine $k$ niza $p$.
	
	<br>
	
	## Primer 1
	
	<br>
	
	### Ulaz
	
	<br>
	
	```
	5 3 2
	1 -2 4 4 -5
	```
	
	<br>
	
	### Izlaz
	
	<br>
	
	```
	7 14 3
	```
	
	### Objašnjenje primera 1
	
	<br>
	 
	Postoje tri podniza dužine tačno $k = 3$:
	
	 - $[1, -2, 4]$ - Vasa će da poveća $c$ sa $1$ na $2$ nakon skupljanja drugog elementa niza, pa je njegova konačna aura $1 \cdot b_1 + 1 \cdot b_2 + 2\cdot b_3 = 1 \cdot 1 - 1 \cdot 2 + 2\cdot 4 = 7$.
	 - $[-2, 4, 4]$ - Vasa će da poveća $c$ sa $1$ na $2$ nakon skupljanja prvog elementa niza, pa je njegova konačna aura $1 \cdot b_1 + 2 \cdot b_2 + 2\cdot b_3 =  - 1 \cdot 2 + 2 \cdot 4 + 2\cdot 4 = 14$.
	 - $[4, 4, -5]$ - Vasa će da poveća $c$ sa $1$ na $2$ nakon skupljanja trećeg elementa niza, pa je njegova konačna aura $1 \cdot b_1 + 1 \cdot b_2 + 1\cdot b_3 = 1 \cdot 4 + 1 \cdot 4 - 1 \cdot 5 = 3$.
	
	<br>
	
	## Primer 2
	
	<br>
	
	### Ulaz
	
	<br>
	
	```
	7 4 3
	-10 2 2 -5 -4 5 7
	```
	
	<br>
	
	### Izlaz
	
	<br>
	
	```
	-12 -9 4 23
	```
	
	<br>
	
	## Ograničenja
	
	
	<br>
	
	
	- $1 \leq x \leq k \leq n \leq 200.000$.
	- $|p_i| \leq 10^9$ za svako $1 \leq i \leq n$. 
	
	<br>
	
	Test primeri su podeljeni u $6$ disjunktnih grupa:
	
	   
	   - U testovima vrednim $10$ poena: važi $n \leq 20$
	   - U testovima vrednim $10$ poena: važi $p_i \geq 0$, za $1 \leq i \leq n$.
	   - U testovima vrednim $15$ poena: važi $n \leq 300$.
	   - U testovima vrednim $15$ poena: važi $n \leq 3.000$.
	   - U testovima vrednim $20$ poena: važi $x = 2$.
	   - U testovima vrednim $30$ poena: bez dodatnih ograničenja.
	
	<br>
	
=== "Rešenje"
	
	| Autor | Tekst i test primeri | Analiza rešenja | Testiranje |
	|:-:|:-:|:-:|:-:|
	| Aleksa Danić | Aleksa Milisavljević | Aleksa Danić | Marko Trajković |
	
	## Rešenje kada je $N \leq 20$
	
	U ovom podzadatku imamo vremena da za svaki podniz fiksiramo skup indeksa na kojima se koeficijent povećava, i izračunamo Vasinu auru za svaki od tih skupova.
	
	Vremenska složenost: $O(n^2{k \choose x})$
	
	
	## Važna formula za sve naredne podzadatke
	  
	
	Posmatrajmo konkretan podniz $[l,r]$ dužine $k$. Neka je $ind_c$ prvi indeks na kom je Vasa uzeo element sa koeficijentom $c$ (u slučaju da je Vasa uzeo element $p_r$ sa koeficijentom $x-1$, neka je $ind_x=r+1$). Neka je $sum(a,b)=p_a+p_{a+1}+\dots+p_{b-1}+p_b$, ($sum(a,b)=0$ za $a>b$). Primetimo da je ukupna Vasina aura nakon prolaska kroz podniz jednaka:
	
	$\sum_{i=1}^x sum(ind_i,r)$
	
	Ovo je zbir $x$ sufiksnih suma na podnizu $[l,r]$. Kada bismo za svako $p_i$ izračunali u koliko različitih sufiksnih suma se taj element nalazi, videli bismo da je to upravo isti broj kao koeficijent ispred tog elementa koji je Vasa izabrao. Evo primera za lakše razumevanje formule na nizu $[1,2,3,4,5,6]$, gde su izabrani koeficijenti $[1,1,2,2,3,3]$:
	
	$1 \cdot 1 + 1 \cdot 2 + 2 \cdot 3 + 2 \cdot 4 + 3 \cdot 5 + 3 \cdot 6 = sum(1,6)+sum(3,6)+sum(5,6)$
	$sum(1,6)=1+2+3+4+5+6, sum(3,6)=3+4+5+6, sum(5,6)=5+6$
	
	Vidimo, na primer, da se broj $2$ pojavljuje samo jednom, u sufiksnoj sumi $sum(1,6)$, a da se broj $5$ pojavljuje u sve tri sufiksne sume. Takođe, koeficijent ispred $2$ je $1$, a koeficijent ispred $5$ je $3$.
	
	Uvedimo i oznaku $suff_i=sum(i,n)$. Tada je $sum(a,b)=suff_a-suff_{b+1}$.
	
	## Rešenje kada je $p_i \geq 0$
	
	Isplati se uzeti svaki element sa što većim koeficijentom, pa će Vasa povećavati koeficijent svaki put kad može. Rešenje za konkretan podniz $[l,r], \space r-l+1=k$ je $1p_l+2p_{l+1}+\dots+xp_{l+x-1}+xp_{l+x}+xp_{l+x+1}+\dots+xp_r=\sum_{i=l}^{l+x-1}sum(i,r)=\sum_{i=l}^{l+x-1}(suff_i-suff_{r+1})=(\sum_{i=l}^{l+x-1}suff_i)-x \cdot suff_{r+1}$. Suma koju smo dobili u ovoj formuli je suma $x$ uzastopnih elemenata niza $suff$, koju možemo brzo naći ukoliko prekalkulišemo niz prefiksnih suma nad nizom $suff$.
	Dakle, neka je $P_i=suff_1+suff_2+\dots+suff_{i-1}+suff_i$, $P_0=0$. Rešenje za interval $[l,r]$ dužine $k$ je jednako
	
	$P_{l+x-1}-P_{l-1}-x \cdot suff_{r+1}$
	
	Vremenska složenost: $O(n)$
	
	  
	
	## Rešenje kada je $n \leq 300$
	
	Sporije implementacije narednog podzadatka daju poene za ovaj podzadatak.
	
	
	## Rešenje kada je $n \leq 3000$
	
	Posmatrajmo konkretan podniz $[l,r]$ dužine $k$. Rešenje za ovaj podniz je
	
	$\sum_{i=1}^x sum(ind_i,r)=\sum_{i=1}^{x}(suff_{ind_i}-suff_{r+1})=(\sum_{i=1}^{x}suff_{ind_i})-x \cdot suff_{r+1}$
	
	Potrebno je da izaberemo niz $ind$ tako da je vrednost navedenog izraza što veća. Primetimo da je $x \cdot suff_{r+1}$ konstanta, pa je potrebno maksimizovati $\sum_{i=1}^{x}suff_{ind_i}$, ili rečima, treba nam zbir sufiksne sume koja počinje na indeksu $l$ (jer je $ind_1=l$), i $x-1$ najvećih sufiksnih suma koje počinju na indeksima između $l+1$ i $r+1$. Možemo sortirati sve ove sufiksne sume, nakon čega je lako naći zbir najvećih $x-1$.
	
	Vremenska složenost: $O(n^2 \log n)$ - dovoljno za maksimalan broj poena na ovom podzadatku
	
	Ukoliko bismo sortirali sve sufiksne sume pre fiksiranja podniza, i za svaku pamtili koji indeks joj odgovara, nakon fiksiranja podniza bismo u $O(n)$ mogli da izdvojimo samo sufiksne sume kojima odgovara indeks iz intervala $[l+1,r+1]$, i to u sortiranom poretku. Ovim pristupom izbegavamo sortiranje za svaki podniz.
	
	Vremenska složenost: $O(n^2)$
	
	## Rešenje kada je $x = 2$
	
	U prethodnom podzadatku smo videli da je potrebno da nađemo zbir $x-1$ najvećih $suff_i$ za $i \in [l+1,r+1]$.
	Dakle, u ovom podzadatku nam treba maksimum svakog intervala dužine $k$ niza $suff$. Koristićemo tehniku *sliding window*.
	
	Jedan način je da koristimo strukturu podataka poput *std::multiset* iz standardne bibliotekte programskog jezika *C++*. Ova struktura podataka, između ostalog, podržava operacije dodavanja, brisanja, i dohvatanja najvećeg elementa, sve u vremenskoj složenosti $O(\log n)$, i održava elemente u uređenom poretku (sortirane po nekom kriterijumu).
	
	Recimo da smo našli maksimum na intervalu $[l,r]$, i da su nam u *multiset*-u svi elementi na tom intervalu. Kada u *multiset* dodamo $suff_{r+1}$, a iz njega izbacimo $suff_l$, možemo naći maksimum na intervalu $[l+1,r+1]$.
	Počinjemo od intervala $[1,k]$, i ponavljajući navedeni postupak možemo efikasno naći rešenja za svaki interval dužine $k$.
	
	Vremenska složenost: $O(n \log n)$
	
	Postoji i rešenje u vremenskoj složenosti $O(n)$ koje koristi red sa dva kraja - *std::deque*, ali nije neophodno za maksimalan broj poena na ovom podzadatku.
	
	
	## Rešenje za 100 bodova
	
	
	U rešenju za 100 bodova nam treba zbir $x-1$ maksimuma svakog intervala dužine $k$ niza $suff$, ali u efikasnijoj složenosti nego u podzadatku $n \leq 3000$.
	Kao u podzadatku $x \leq 2$, koristićemo tehniku *sliding window*, i strukturu podataka *std::multiset*.
	
	Recimo da smo našli zbir $x-1$ maksimuma na intervalu $[l,r]$. Nazovimo taj zbir $S$. Neka je $large$ *multiset* čiji su elementi $x-1$ maksimuma među svim $suff_i$ za $i \in [l,r]$ (ukoliko su $x$-ti i $x-1$-vi maksimum jednaki, uzimamo broj elemenata te vrednosti takav da je $|large|=x-1$). Neka je $small$ *multiset* čiji su elementi svi $suff_i$ za $i \in [l,r]$ koji ne pripadaju $large$.
	
	Da bismo prešli na interval $[l+1,r+1]$, potrebno je dodati element $suff_{r+1}$ i izbaciti element $suff_l$ iz naših struktura, i adekvatno ažurirati $S, large$ i $small$.
	
	Hajde najpre da vidimo kako pravilno dodati element $suff_{r+1}$.
	Za početak dodajemo $suff_{r+1}$ u *multiset* $large$ i povećavamo $S$ za $suff_{r+1}$, a potom prebacujemo najmanji element *multiset*-a $large$ u *multiset* $small$ i smanjujemo $S$ za vrednost tog elementa.
	
	Nakon ovih operacija $large$ čuva $x-1$ maksimuma intervala $[l,r+1]$, $small$ čuva sve ostale elemente tog intervala, a $S$ sumu $x-1$ maksimuma.
	
	Potrebno je još obrisati element $suff_l$.
	Razlikujemo dva slučaja: kada se $suff_{l}$ nalazi u $large$ i kada se nalazi u $small$ (ukoliko se ta vrednost nalazi u oba *multiset*-a, opredelimo se za proizvoljan slučaj). Ako se nalazi u $small$, jednostavno ga obrišemo iz tog *multiset*-a. U suprotnom ga obrišemo iz $large$, smanjimo $S$ za $suff_l$, prebacimo najveći element *multiset*-a $small$ u *multiset* $large$ i povećamo $S$ za njegovu vrednost.
	
	Nakon svih operacija smo uspešno prešli sa intervala $[l,r]$ na interval $[l+1,r+1]$.
	Kao u prethodnom podzadatku, krećemo od $[1,k]$ i ponavljanjem navedenog postupka tražimo rešenje za sve intervale dužine $k$.
	
	Vremenska složenost: $O(n \log n)$
	
	``` cpp title="05_vasa_skupljac.cpp" linenums="1"
	#include<bits/stdc++.h>
	#define maxn 200005
	using namespace std;
	int n,k,x;
	int a[maxn];
	long long suf[maxn];
	set<pair<long long,int> > s;
	set<pair<long long,int> > topx;
	int main() {
	    ios::sync_with_stdio(0);
	    cin.tie(0);
	    cin>>n>>k>>x;
	    for(int i=1;i<=n;i++){
	        cin>>a[i];
	    }
	    suf[n+1]=0;
	    for(int i=n;i>=1;i--){
	        suf[i]=suf[i+1]+a[i];
	    }
	    long long val=0;
	    if(x>1)
	    {
	        for(int i=2;i<=k+1;i++) {
	            if(topx.size()<x-1) {
	                val+=suf[i];
	                topx.insert({suf[i],i});
	            }
	            else {
	                if(suf[i] > (*topx.begin()).first) {
	                    val+=suf[i]-(*topx.begin()).first;
	                    s.insert(*topx.begin());
	                    topx.erase(topx.begin());
	                    topx.insert({suf[i],i});
	                }
	                else {
	                    s.insert({suf[i],i});
	                }
	            }
	        }
	    }
	    cout<<suf[1]+val-x*suf[k+1]<<" ";
	    for(int i=2;i+k<=n+1;i++)
	    {
	        if(x>1)
	        {
	            if(suf[i + k] > (*topx.begin()).first) {
	                val+=suf[i + k]-(*topx.begin()).first;
	                s.insert(*topx.begin());
	                topx.erase(topx.begin());
	                topx.insert({suf[i + k],i + k});
	            }
	            else {
	                s.insert({suf[i + k],i + k});
	            }
	            if(s.count({suf[i],i}))
	            {
	                s.erase({suf[i],i});
	            }
	            else
	            {
	                val-=suf[i];
	                topx.erase({suf[i],i});
	                auto it=s.end();
	                it--;
	                val+=(*it).first;
	                topx.insert(*it);
	                s.erase(it);
	            }
	        }
	        cout<<suf[i] + val - x * suf[i + k]<<" ";
	    }
	}

	```
