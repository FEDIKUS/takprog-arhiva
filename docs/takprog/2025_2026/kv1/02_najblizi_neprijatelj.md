---
hide:
  - toc
---

# 2 - Najbliži neprijatelj

=== "Zadatak"
	
	| Vremensko ograničenje | Memorijsko ograničenje |
	|:-:|:-:|
	| 1000ms | 64MB |
	
	Sunce kruži oko centra Mlečnog puta, Zemlja kruži oko Sunca, Mesec kruži oko Zemlje, voda kruži u prirodi, kazaljka na satu se kreće u krug, bubanj veš mašine ima kružni presek i elektroni u najprostijem modelu kruže oko centra atoma. Tako je i najprostije rešenje svih saobraćajnih problema kružni tok.
	
	<br>
	
	Soćko se, nizom nesrećnih okolnosti, upravo našao u jednom kružnom toku. Njega možemo posmatrati kao kružnicu podeljenu na $N$ jednakih delova pri čemu je svaki deo ili zauzet nekim dostavljačem hrane na biciklu (to ćemo označavati sa "#") ili se baš Soćko nalazi u njemu (to ćemo označavati sa "+") ili se u njemu ne nalazi niko (to ćemo označavati sa ".").
	
	<br>
	
	Udaljenost Soćka do bilo kog dostavljača se definiše kao dužina manjeg od dva kružna luka između Soćka i dostavljača, izražena u broju jednakih delova.
	
	<br>
	
	Kako je Soćko odgovoran vozač, želi da drži određenu udaljenost od dostavljača hrane. Interesuje ga u datom trenutku koji je opisan, koja je minimalna udaljenost njega do nekog dostavljača hrane. Soćko je fokusiran na vožnju, tako da treba da mu pomognete oko računanja ove minimalne udaljenosti.
	
	<br>
	
	## Opis ulaza
	
	<br>
	
	U prvoj liniji standardnog ulaza se nalazi broj $N$ koji predstavlja broj jednakih delova na koji je podeljen kružni tok. U drugoj, i poslednjoj, liniji ulaza nalazi se niska dužine $N$ sastavljena od tačno jednog karaktera "+", barem jednog karaktera "#" i proizvoljno mnogo karaktera ".".
	
	<br>
	
	## Opis izlaza
	
	<br>
	
	Na prvu i jedinu liniju standardnog izlaza ispisati jedan broj koji predstavlja udaljenost Soćka do najbližeg dostavljača hrane.
	
	<br>
	
	## Primer 1
	
	<br>
	
	### Ulaz
	
	<br>
	
	```
	5
	#..+.
	```
	
	<br>
	
	### Izlaz
	
	<br>
	
	```
	2
	```
	
	<br>
	
	### Objašnjenje primera
	
	<br>
	
	Udaljenost Soćka do jednog jedinog dostavljača je $2$. Sa jedne strane je udaljenost do njega $2$, dok je sa druge $3$, ali se za udaljenost do dostavljača uzima manje rastojanje.
	
	<br>
	
	## Primer 2
	
	<br>
	
	### Ulaz
	
	<br>
	
	```
	10
	.#..#..+..
	```
	
	<br>
	
	### Izlaz
	
	<br>
	
	```
	3
	```
	
	<br>
	
	### Objašnjenje primera
	<br>
	
	Udaljenost Soćka do dostavljača je $3$ i $4$. Kako nas interesuje najmanja udaljenost, rešenje je $3$.
	
	<br>
	
	## Ograničenja
	<br>
	
	* $2 \leq N \leq 500\,000$
	
	<br>
	
	Test primeri su podeljeni u tri disjunktne grupe:
	* U primerima vrednim 25 poena: svi dostavljači se u niskoj nalaze desno od Soćka
	* U primerima vrednim 25 poena: postoji samo jedan dostavljač
	* U primerima vrednim 50 poena: nema dodatnih ograničenja
	
=== "Rešenje"
	
	| Autor | Tekst i test primeri | Analiza rešenja | Testiranje |
	|:-:|:-:|:-:|:-:|
	| Vladimir Milovanović | Filip Bojković | Sofija Čebašek | Dragan Urošević |
	
	## Rešenje kada se svi dostavljači u niskoj nalaze desno od Soćka
	Primetimo da će dostavljač najbliži Soćku biti prvi kada se krećemo po krugu u jednom od dva različita smera, počevši od pozicije na kojoj se Soćko nalazi ($s$). Najbliži dostavljači za dva smera se mogu poklapati, tj. ukoliko postoji samo jedan dostavljač on će biti najbliži za oba smera kretanja. U ovom podzadatku jedan od ta dva dostavljača će u niskoj biti prvi sa desne strane Soćka, koji se nalazi na poziciji $d_1$, a drugi će biti poslednji dostavljač u niskoj, na poziciji $d_2$. Sve pozicije možemo naći jednim prolaskom kroz datu nisku. Rastojanje između pozicija $s$ i $d_1$ u jednom smeru jednako je $d_1-s$ i predstavlja najmanje rastojanje između nekog dostavljača i Soćka, kada se u krugu krećemo u tom smeru. Za drugi smer je najmanje rastojanje između $s$ i $d_2$, koje se za taj smer računa po formuli $N-d_2+s$. Rešenje zadatka je manje od dva izračunata rastojanja. 
	
	## Rešenje kada postoji samo jedan dostavljač
	Kako postoji samo jedan dostavljač, on će ujedno biti i najbliži. Prolaskom kroz nisku nalazimo i čuvamo poziciju na kojoj se nalazi Soćko ($s$), kao i poziciju dostavljača ($d$). Dužina jednog kružnog luka između Soćka i dostavljača jednaka je $\lvert s-d\rvert$, a drugog $N-\lvert s-d\rvert$. Rešenje zadatka je manja od dužina ta dva luka.
	
	## Glavno rešenje
	Slično prvom podzadatku, potrebno je naći najbližeg dostavljača Soćku za svaki od dva smera kretanja po krugu posebno. Prolaskom kroz nisku nalazimo poziciju $s$. Za jedan smer se krećemo od pozicije $s$ ulevo kroz nisku, do prve pozicije na kojoj se nalazi dostavljač ($d_1$). Ukoliko pri traženju dođemo do početka niske, a nismo odredili $d_1$, pretragu nastavljamo od pozicije $N-1$ ulevo, pošto se pozicije nalaze na krugu (karakteri u niskoj su indeksirani od $0$). Slično, za poziciju najbližeg dostavljača pri kretanju u drugom smeru ($d_2$) pretraga se obavlja od pozicije $s$ udesno. Ukoliko se nalazimo na poziciji $N-1$, a nismo pronašli poziciju $d_2$, pretragu nastavljamo od pozicije $0$ udesno. Rastojanje između $s$ i $d_1$ pri kretanju u odgovarajućem smeru u krugu možemo dobiti brojanjem pozicija za koje smo se pomerili pri traženju pozicije $d_1$. Slično nalazimo i rastojanje između $s$ i $d_2$ u odgovarajućem smeru. Rešenje zadatka je manje od ta dva rastojanja.
	
	Drugi način za rešavanje zadatka je da se, nakon određivanja pozicije Soćka u niskoj, za svakog dostavljača izračuna rastojanje kao u prethodnom podzadatku. Rešenje zadatka je najmanje od svih izračunatih rastojanja.
	
	Vremenska složenost: $O(N)$
	
	``` cpp title="02_najblizi_neprijatelj.cpp" linenums="1"
	#include<bits/stdc++.h>
	
	using namespace std;
	
	int main(){
	    int n; cin>>n;
	    string s; cin>>s;
	    int poz = find(s.begin(),s.end(),'+')-s.begin();
	    int res = n;
	    for(int i=0;i<n;i++){
	        if(s[i]!='#') continue;
	        res = min(res,abs(i-poz));
	        res = min(res,n-abs(i-poz));
	    }
	    cout<<res;
	}

	```
