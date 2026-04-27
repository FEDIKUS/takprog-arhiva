---
hide:
  - toc
---

# 1 - Prosek i medijana

=== "Zadatak"
	
	| Vremensko ograničenje | Memorijsko ograničenje |
	|:-:|:-:|
	| 1000ms | 256MB |
	
	Veljku je dosadno na času matematike i odlučio je da se igra brojevima umesto da sluša profesora. Tokom svoje igre, naišao je na problem koji nije mogao da reši.
	
	<br>
	
	Veljko je u svesci napisao dva prirodna broja $a$ i $b$. On želi da dopiše još jedan broj $c$, ali takav da trojka brojeva $a, b, c$ bude lepa.
	
	<br>
	
	Prosek trojke brojeva $a, b, c$ je zbir svih vrednosti te trojke, podeljen sa $3$, $\text{prosek}(a, b, c) = \dfrac{a+b+c}{3}.$
	
	<br>
	
	Medijana trojke brojeva $a, b, c$, u oznaci $\text{medijana}(a,b,c)$, je druga najmanja, odnosno druga najveća od vrednosti $a$, $b$ i $c$. To znači da ako bismo napisali vrednosti brojeva $a$, $b$ i $c$ od najmanje do najveće, medijana je ona koja bi bila u sredini (zato se i zove medijana).
	
	<br>
	
	Medijanu tri broja možemo takođe definisati na sledeći način: ako sa $\min(a,b,c)$ označimo najmanju od vrednosti brojeva $a, b, c$, a sa $\max(a,b,c)$ najveću od vrednosti brojeva $a, b, c$, onda važi da je $\text{medijana}(a,b,c) = a+b+c-\min(a,b,c)-\max(a,b,c)$.
	
	<br>
	
	Veljko smatra da je trojka brojeva $a, b, c$ lepa ako važi $\text{prosek}(a,b,c) \le \text{medijana}(a,b,c)$. Pomozite mu tako što ćete izračunati najveći broj $c$ za koji je trojka $a, b, c$ lepa. Može se dokazati da takav broj uvek postoji.
	
	<br>
	
	Kako biste lakše shvatili prethodne funkcije, pogledajte primere trojki na kraju teksta zadatka.
	<br>
	## Opis ulaza
	
	<br>
	
	U prvoj i jedinoj liniji standardnog ulaza se nalaze celi brojevi $a$ i $b$.
	
	<br>
	
	## Opis izlaza
	
	<br>
	
	U prvoj i jedinoj liniji standardnog izlaza ispisati jedan broj - najveću vrednost $c$ tako da trojka $a, b, c$ bude lepa.
	
	<br>
	
	
	## Primer 1
	
	<br>
	
	### Ulaz
	
	<br>
	
	```
	1 2
	```
	
	<br>
	
	### Izlaz
	
	<br>
	
	```
	3
	```
	
	### Objašnjenje
	
	<br>
	
	Trojka 1, 2, 3 je lepa. Može se dokazati da ne postoji broj $c$ veći od $3$ za koji je trojka $1, 2, c$ lepa.
	 
	<br>
	
	## Primer 2
	
	<br>
	
	### Ulaz
	
	<br>
	
	```
	63 12
	```
	
	<br>
	
	### Izlaz
	
	<br>
	
	```
	114
	```
	
	<br>
	
	## Primer 3
	
	<br>
	
	### Ulaz
	
	<br>
	
	```
	1000000000 10000000000
	```
	
	<br>
	
	### Izlaz
	
	<br>
	
	```
	19000000000
	```
	<br>
	
	## Ograničenja
	
	<br>
	
	$1 \le a, b \le 10^{18}$
	
	<br>
	
	Test primeri su podeljeni u $5$ disjunktnih grupa:
	
	- U test primerima vrednim $20$ poena važi: $a, b \le 100$
	- U test primerima vrednim $20$ poena važi: $a = b$ i $a, b \le 10^9$
	- U test primerima vrednim $20$ poena važi: $a < b$ i $a,b \le 10^9$
	- U test primerima vrednim $20$ poena važi: $a, b \le 10^9$
	- U test primerima vrednim $20$ poena nema dodatnih ograničenja.
	
	<br>
	
	## Primeri trojki
	
	<br>
	
	Trojka $(1, 2, 3)$:
	- $\text{prosek}(1,2,3) = \dfrac{1+2+3}{3} = 2$,
	- $\text{medijana}(1, 2, 3) = 2$.
	
	Kako je $\text{prosek}(1,2,3) \le \text{medijana}(1,2,3)$, ova trojka je lepa.
	
	<br>
	
	Trojka $(10, 100, 1000)$:
	- $\text{prosek}(10,100,1000) = 370$,
	- $\text{medijana}(10, 100, 1000) = 100$.
	
	Kako je $\text{prosek}(10,100,1000) > \text{medijana}(10,100,1000)$, ova trojka nije lepa.
	
	<br>
	
	Trojka $(20, 8, 20)$:
	- $\text{prosek}(20,8,20) = 16$,
	- $\text{medijana}(20, 8, 20) = 20$.
	
	Kako je $\text{prosek}(20,8,20) \le \text{medijana}(20,8,20)$, ova trojka je lepa.
	
	<br>
	
=== "Rešenje"
	
	| Autor | Tekst i test primeri | Analiza rešenja | Testiranje |
	|:-:|:-:|:-:|:-:|
	| Nemanja Majski | Nemanja Majski | Vladimir Milovanović | Vladimir Milovanović |
	
	### Glavno rešenje
	
	Bez smanjenja opštosti, pretpostavimo da za dva zadata broja $a$ i $b$ važi $a \le b$ (ukoliko to prilikom učitavanja i nije slučaj jednostavno možemo zameniti vrednosti promenljivama $a$ i $b$). Pošto se u zadatku traži najveći broj $c$ za koji važi $\text{prosek}(a,b,c) \le \text{medijana}(a,b,c)$, to zahtevano $c$ sigurno neće biti manje od $a$ i $b$, odnosno imamo $a \le b \le c$, pa je $\text{medijana}(a,b,c) = b$, a kako je $\text{prosek}(a, b, c) = \dfrac{a+b+c}{3} \le b$, što je ekvivalentno $a+b+c \le 3b$, dobija se $c \le 2b-a$, odnosno $c = 2b-a$, što se i tražilo u zadatku. Vremenska složenost ovog rešenja je konstantna $\mathcal{O}(1)$ i ne zavisi od vrednosti $a$, $b$ i $c$.
	
	Izvorni kod u programskom jeziku Pajton mogao bi izgledati recimo:
	
	```python
	a, b = sorted(map(int,input().split()))
	print(2*b-a)
	```
	
	ili
	
	```python
	a, b = map(int,input().split())
	print(2*max(a,b)-min(a,b))
	```
	
	dok je za maksimalan broj poena u programskim jezicima C i C++, odnosno C# i Java, bilo neophodno promenljive $a$ i $b$ deklarisati kao `long long`, odnosno `long`, respektivno, pošto već mogu uzimati vrednosti do $10^{18}$.
	
	``` cpp title="01_prosek_i_medijana.cpp" linenums="1"
	#include<bits/stdc++.h>
	#define ll long long
	using namespace std;
	ll a,b;
	int main(){
	    cin>>a>>b;
	    cout<<max(a,b)*2-min(a,b)<<"\n";
	    return 0;
	}

	```
