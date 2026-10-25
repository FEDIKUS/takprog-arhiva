---
hide:
  - toc
---

# B1 - Nameštaljka

=== "Zadatak"
	
	| Vremensko ograničenje | Memorijsko ograničenje |
	|:-:|:-:|
	| 1000ms | 64MB |
	
	<br>
	
	Dobrodošli na Izbor za Međunarodnu Olimpijadu iz Sajber Bezbednosti! Da biste prošli na Olimpijadu potrebno je da hakujete šifru na dvokrilnim vratima.
	
	<br>
	
	Oba krila zahtevaju po šifru koja se sastoji od po $n$ prirodnih brojeva. Odnosno, prvo krilo zahteva brojeve $a_1, a_2, \ldots, a_n$, a drugo krilo brojeve $b_1, b_2, \ldots, b_n$. Vi na raspolaganju imate brojeve $1,2,\ldots,2n$ i to svaki od njih tačno jednom.
	
	<br>
	
	Naravno, ne znate koja je šifra, ali imate bekdor! Znate da ako namestite brojeve tako da se maksimizuje suma:
	
	$$\mid a_1 - a_2 \mid + \mid a_2 - a_3\mid + \ldots + \mid a_{n-1} - a_n\mid + \mid b_1 - b_2\mid + \mid b_2 - b_3\mid + \ldots + \mid b_{n-1} - b_n\mid$$
	
	Onda će se oba krila otvoriti.
	
	<br>
	
	Ispišite nizove $a$ i $b$ koji postižu maksimalnu sumu.
	
	## Opis ulaza
	
	<br>
	
	U prvoj i jedinoj liniji standardnog ulaza dat je jedan prirodan broj $n$ - broj elemanata u svakom od dva niza.
	
	<br>
	
	
	## Opis izlaza
	
	<br>
	
	U prvoj liniji standardnog izlaza potrebno je ispisati $n$ brojeva - $a_1, a_2, \ldots, a_n$.
	
	U drugoj liniji standardnog izlaza potrebno je ispisati $n$ brojeva - $b_1, b_2, \ldots, b_n$.
	
	**Potrebno je da svi ispisani brojevi budu međusobno različiti i iz skupa $1,2,\ldots,2n-1,2n$.**
	
	Ukoliko postoji više rešenja, ispisati bilo koje.
	
	
	## Primer 1
	
	<br>
	
	### Ulaz
	
	<br>
	
	```
	2
	```
	
	<br>
	
	### Izlaz
	
	<br>
	
	```
	1 3
	4 2
	```
	
	<br>
	
	### Objašnjenje 
	
	Suma koju postižu ova dva niza je $\mid 1-3 \mid + \mid 4-2 \mid = 2 + 2 = 4$. Može se pokazati da je ovo optimalno.
	
	<br>
	
	## Ograničenja
	
	<br>
	
	 - $2 \leq n \leq 100.000$.
	
	<br>
	
	Test primeri su podeljeni u četiri disjunktne grupe:
	 - U test primerima vrednim $10$ poena, važi da $n \leq 5$.
	 - U test primerima vrednim $10$ poena, važi da $n \leq 12$.
	 - U test primerima vrednim $25$ poena, važi da $n \leq 1000$.
	 - U test primerima vrednim $55$ poena, nema dodatnih ograničenja.
	
=== "Rešenje"
	
	| Autor | Tekst i test primeri | Analiza rešenja | Testiranje |
	|:-:|:-:|:-:|:-:|
	|  |  |  |  |
	
	Da bi napravili najveću moguću sumu, neophodno je da brojevi u oba
	niza budu naizmenično veći pa manji, odnosno da je ili $a_1 > a_2$,
	$a_2 < a_3$, $a_3 > a_4$, ..., ili $a_1 < a_2$, $a_2 > a_3$, $a_3 <
	a_4$, i tako dalje. U suprotnom, imali bismo tri broja $a_{i-1} < a_i <
	a_{i+1}$ (ili u obrnutom poretku, gde je dokaz isti), i nije teško
	dokazati da bi menjanje mesta $a_{i-1}$ i $a_i$ povećalo sumu.
	
	Pretpostavimo za sada da oba niza počinju malim brojem, odnosno $a_1 <
	a_2$, $a_2 > a_3$, ..., $b_1 < b_2$, $b_2 > b_3$, ... Suma koju
	maksimizujemo je onda
	
	$$ |a_1 - a_2| + |a_2 - a_3| + ... + |b_1 - b_2| + |b_2 - b_3| + ... =
	-a_1 + 2a_2 - 2a_3 + 2a_4 + ... - b_1 + 2b_2 - 2b_3 + ... $$
	
	Iz ovoga vidimo da redosled brojeva nije bitan, osim što brojevi na
	neparnim indeksima smanjuju sumu, brojevi na parnim povećavaju, i da se
	prvi i poslednji broj u nizu "broje" duplo manje. Da bi maksimizovali
	sumu, prvo ćemo rasporediti brojeve na sva mesta osim prvog i
	poslednjeg, tako da na neparna uvek stavljamo najmanji broj koji još nije
	raspoređen, a na parna najveći. Na kraju preostale brojeve postavljamo
	na početak i kraj niza, opet vodeći računa o parnosti (manje na neparne
	indekse, veće na parne).
	
	Da bi dovršili rešenje, potrebno je još da ponovimo istu proceduru za
	preostale oblike nizova (gde jedan ili oba od $a_i, b_i$ počinje
	velikim brojem, u kom slučaju na neparne indekse postavljamo velike
	brojeve) i od četiri dobijena rešenja ispišemo ono koje daje najveću
	sumu.
	
	``` cpp title="01_cikcak.cpp" linenums="1"
	#include <bits/stdc++.h>
	
	using namespace std;
	
	const int maxN = 1e6 + 10;
	
	int a[maxN], b[maxN];
	
	int main()
	{
	    int n;
	    cin >> n;
	
	    int upper = 2*n;
	    int lower = 1;
	
	    for (int i = 2; i < n; i++) {
	        if (i % 2 == 0) 
	            a[i] = upper--; 
	        else 
	            a[i] = lower++;
	    }
	
	
	    for (int i = 2; i < n; i++) {
	        if (i % 2 == 1) 
	            b[i] = upper--; 
	        else 
	            b[i] = lower++;
	    }
	
	    a[1] = lower++;
	    b[1] = upper--;
	    if (n % 2 == 1) {
	        a[n] = lower++;
	        b[n] = lower++;
	    } else {
	        b[n] = lower++;
	        a[n] = lower++;
	    }
	
	
	    for (int i = 1; i <= n; i++) {
	        printf("%d ", a[i]);
	    }
	
	    printf("\n");
	
	    for (int i = 1; i <= n; i++) {
	        printf("%d ", b[i]);
	    }
	
	    printf("\n");
	
	    return 0;
	}

	```
