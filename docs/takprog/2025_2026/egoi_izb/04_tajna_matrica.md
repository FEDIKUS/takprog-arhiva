---
hide:
  - toc
---

# 4 - Tajna matrica

=== "Zadatak"
	
	| Vremensko ograničenje | Memorijsko ograničenje |
	|:-:|:-:|
	| 1000ms | 256MB |
	
	Postoji matrica sa $n \times m$ elemenata, kojima vrednosti nisu poznate. Vaš zadatak je da *što približnije* odredite vrednosti date matrice.
	
	<br>
	
	Neka je prava vrednost polja $(i,j)$ jednaka $a_{i,j}$. Poznato vam je i da su vrednosti $a_{i,j}$ pozitivni celi brojevi. Pored toga, jedino što vam je unapred poznato o matrici je da je  $a_{i,j} \geq a_{i+1,j}$ i $a_{i,j} \geq a_{i,j+1}$.
	
	<br>
	
	Na raspolaganju vam je i $q$ upita: koja je vrednost polja $(i,j)$, tj. $a_{i,j}$. 
	
	<br>
	
	Ispisati procenjenu vrednost sume svih polja matrice sa multiplikativnom greškom najviše $2$ (tj. ako je prava suma $S$, treba ispisati broj između $\frac{S}{2}$ i $2S$).
	
	<br>
	
	## Opis funkcija
	
	<br>
	
	Potrebno je da implementirate funkciju
	
	* $\text{ProceniSumu}(n, m, q)$
	
	gde su $n$ i $m$ dimenzije matrice, $q$ dozvoljeni broj pitanja, a funkcija treba da vrati procenu sume matrice.
	
	<br>
	
	Vaš program može da koristi funkciju
	
	* $\text{Pitaj}(i, j)$
	
	koja vraća vrednost polja $(i,j)$, tj. $a_{i,j}$
	
	<br>
	
	**Redovi i kolone su indeksirani od 1.**
	
	<br>
	
	## Primer
	
	<br>
	
	Neka je $n = 2$, $m = 2$, $q = 2$ i tajna matrica $a$ je:
	
	```
	25 22
	23 20
	```
	
	<br>
	
	Ukoliko pozovemo $\text{Pitaj}(1, 1)$, kao povratnu vrednost, dobićemo $25$. Ukoliko pozovemo $\text{Pitaj}(2, 2)$, kao povratnu vrednost, dobićemo $20$. Tada zbog uslova o monotnosti znamo da je $20 \leq a_{1,2} \leq 25$ i slično $20 \leq a_{2,1} \leq 25$. Prema tome, znamo da je prava vrednost sume matrice $85 \leq S \leq 95$. Bila koja vrednost iz ovog intervala je tačna procena sume.
	
	<br>
	
	**Primetite da ovo nije pravi primer na kojem će vaše rešenje biti ocenjivano (jer je po ograničenjima $q \geq 50$), već služi da ilustruje postavljanja pitanja.**
	
	<br>
	
	## Ograničenja
	
	<br>
	
	* $1 \leq a_{i,j} \leq 10^{14}$
	* $1 \leq n \cdot m \leq 10^4$
	* $50 \leq q \leq 10^4$
	
	<br>
	
	Test primeri su podeljeni u $4$ podzadatka:
	
	* **[8 poena]:** $1 \leq a_{i,j} \leq 2$
	* **[13 poena]:** $q = n \cdot m$
	* **[35 poena]:** $n \leq 10^4$, $m = 1$
	* **[44 poena]:** Bez dodatnih ograničenja
	
	<br>
	
	## Detalji implementacije
	
	<br>
	
	Potrebno je da pošaljete tačno jedan fajl koji implementira pomenutu funkciju. Osim tražene funkcije, vaš fajl može da sadrži i dodatne globale promenljive, pomoćne funkcije i dodatne biblioteke.
	
	<br>
	
	U jeziku `C++`, vaša funkcija mora biti sledećeg oblika:
	
	`long long ProceniSumu(int n, int m, int q)`
	
	U jeziku `Python`, vaša funkcija mora biti sledećeg oblika:
	
	`ProceniSumu(n, m, q, Pitaj)`
	
	<br>
	
	Ukoliko implementirate rešenje u `C++`, vaš program mora uključivati `code.h`, iz kojeg može pozivati funkciju $\text{Pitaj}$ sledećeg potpisa, u jeziku `C++`:
	
	`long long Pitaj(int i, int j)`
	
	U jeziku `Python`, funkcija ima potpis:
	
	`Pitaj(i, j)`
	
	<br>
	
	Uz zadatak, obezbeđeni su vam i "template" fajlovi `code.cpp` i `code.py` koje možete koristiti i menjati po potrebi. Takođe su vam obezbeđeni i programi `grader.cpp` i `grader.py` koji služe da bi lakše testirali kodove. Oni sa standardnog ulaza učitavaju sledeće podatke:
	
	* U prvom redu, brojeve $n$, $m$ i $q$
	* U narednih $n$ redova po $m$ celobrojnih vrednosti. $j$-ti broj u $i$-tom redu predstavlja $a_{i,j}$.
	
	Zatim ovaj program poziva vašu funkciju i štampa povratnu vrednost na ekran. Ukoliko vaše rešenje koristi funkciju $\text{Pitaj}$ više od $q$ puta, biće prekinuto sa statusom `RTE` (runtime error).
	
	<br>
	
	## Napomena
	
	<br>
	
	**Ne smete ispisivati ništa na standardni izlaz. Neophodno je samo vratiti procenjenu vrednost sume.**
	
=== "Rešenje"
	
	| Autor | Tekst i test primeri | Analiza rešenja | Testiranje |
	|:-:|:-:|:-:|:-:|
	| Marko Milenković | Aleksa Milisavljević | Marko Milenković | Dragan Urošević |
	
	### Podzadatak 1: $1 \leqa_{ij} \leq 2$
	U ovom podzadatku maksimalna suma može da se desi kada je matrica puna samo dvojkama, a minimalna kada je puna samo jedinicama. Primetićemo da bilo koja matrica između ove dve zadovoljava uslov. Dovoljno je ispisati onda samo $nm$.
	
	Vremenska složenost: $O(1)$, broj upita: $0$.
	
	### Podzadatak 2: $q=nm$
	U ovom podzadatku pitaćemo za svako polje u matrici i ispisati tačnu sumu.
	
	Vremenska složenost: $O(nm)$, broj upita: $nm$.
	
	### Podzadatak 3: $m=1$
	
	U ovom podzadatku rešavamo slučaj kada je matrica zapravo niz. Zarad lakše analize pretpostavimo da je $n=2^k$ stepen dvojke. Posmatrajmo sledeću sumu:
	
	$a_1 + a_2 + a_4 + a_4 + a_8 + a_8 + a_8 + a_8 + a_{16} + \ldots + a_{2^k}$
	
	Očigledno je da je naša suma manja ili jednaka pravoj jer znamo da je niz rastuć. S druge strane, ukoliko pomnožimo ceo izraz sa dva, dobijamo:  $2a_1 > a_1$, $2a_2 \geq a_2 + a_3$, $8a_4 \geq a_4 + a_5 + a_6+ a_7$. Ovo pokazuje da naša aproksimativna suma nije duplo manja od prave sume. Ovim završavamo dokaz tačnosti.
	
	U slučaju kada $n$ nije stepen dvojke, pitaćemo i za vrednost poslednjeg elementa i njime popuniti od prethodnog stepena dvojke do kraja.
	
	Vremenska složenost: $O(n)$, broj upita: $\lceil \log_2(n) \rceil$
	
	### Podzadatak 5: Bez dodatnih ograničenja
	
	Uopštićemo ideju iz prethodnog podzadatka. Pokušaćemo da uzmemo samo polja čiji je i red i kolona stepen dvojke i njima aproksimirati kvadrat levo-gore do prethodnih izabranih polja. Ponovo aproksimativna suma je manja ili jednaka originalnoj, ali istim principom kao u prethodnom podzadatku dobijemo da je aproksimativna suma veća ili jednaka četvrtini originalne sume.
	
	Ipak, dovoljno je da samo pomnožimo celu našu aproksimativnu sumu sa dva. Onda je naša nova aproksimativna suma najviše dupla prava suma, a barem polovina prave sume.
	
	Vremenska složenost: $O(nm)$, broj upita: $\lceil \log_2(n)\rceil \cdot \lceil \log_2(m) \rceil$
	
	
	### Napomena
	
	Naravno, moguće je postići bolje vremenske složenosti, ali kako su dimenzije matrice male, to nije neophodno za ovaj zadatak.
	
	``` cpp title="04_tajna_matrica.cpp" linenums="1"
	#include<bits/stdc++.h>
	#include "code.h"
	
	using namespace std;
	
	long long ProceniSumu(int n, int m, int q) {
	    vector<vector<long long>> a(n, vector<long long>(m));
	    a[n-1][m-1]=1;
	    bool inc=true;
	    for(int i=0;(1<<i)<=n;i++) {
	        for(int j=0;(1<<j)<=m;j++) {
	            a[(1<<i)-1][(1<<j)-1]=Pitaj(1<<i,1<<j);
	        }
	    }
	    long long s=0;
	    for (int i=n-1;i>=0;i--) {
	        for(int j=m-1;j>=0;j--) {
	            if(i<n-1) a[i][j]=max(a[i][j],a[i+1][j]);
	            if(j<m-1) a[i][j]=max(a[i][j],a[i][j+1]);
	            s+=a[i][j];
	        }
	    }
	    return 2*s;
	}

	```
