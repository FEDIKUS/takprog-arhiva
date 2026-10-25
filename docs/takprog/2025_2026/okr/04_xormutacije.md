---
hide:
  - toc
---

# A1 - Xormutacije 2

=== "Zadatak"
	
	| Vremensko ograničenje | Memorijsko ograničenje |
	|:-:|:-:|
	| 1500ms | 256MB |
	
	Perica se našao u veoma nezgodnoj poziciji. On je od svog profesora dobio niz pozitivnih celih brojeva $A_1, A_2, \cdots, A_N$ dužine $N$. Kako svaka osoba ima svoje preference po pitanju bitovskih operacija, tako i Peričin profesor više voli bitovsku operaciju $and$ u odnosu na operaciju $xor$, što je veoma retka pojava.
	
	<br>
	
	Kako bi Perica udovoljio svom profesoru on će mu pokloniti jedan dobar niz brojeva. Niz brojeva $S_1, S_2, \cdots, S_M$ je dobar ukoliko za svaki par brojeva $(i, j) \ (1 \leq i \leq j \leq M)$ važi $S_i \ and \ S_j > S_i \ xor \ S_j$. 
	
	<br>
	
	Pomozite Perici da odgovori na $Q$ upita, gde je u svakom upitu dat podniz $A_L, A_{L+1}, \cdots, A_R$ početnog niza, gde je odgovor na upit dužina najduže dobre podsekvence tog podniza. Preciznije, potrebno je naći najveće $K$ tako da postoji niz indeksa $L \leq i_1 < i_2 < \cdots < i_K \leq R$ takav da je niz $A_{i_1}, A_{i_2}, \cdots, A_{i_K}$ dobar.
	
	<br>
	
	## Opis ulaza
	
	<br>
	
	U prvoj liniji standardnog ulaza data su dva cela broja $N$ i $Q$, broj elemenata niza i broj upita redom.
	
	<br>
	
	U drugoj liniji standardnog ulaza dato je $N$ celih brojeva $A_i$, članovi niza $A$.
	
	<br>
	
	U narednih $Q$ linija standardnog ulaza data su po dva cela broja $L$ i $R$, koji označavaju podniz $A_L, A_{L+1}, \cdots, A_R$.  
	
	<br>
	
	## Opis izlaza
	
	<br>
	
	U $Q$ linija standardnog izlaza potrebno je ispisati rešenje za svaki upit. U $i$-toj liniji se nalazi odgovor na $i$-ti upit. 
	
	<br>
	
	## Primer 1
	
	<br>
	
	### Ulaz
	
	<br>
	
	```
	5 3
	1 2 1 3 2
	1 5
	1 4
	2 3
	```
	
	<br>
	
	### Izlaz
	
	<br>
	
	```
	3
	2
	1
	```
	
	<br>
	
	## Objašnjenje
	
	<br>
	
	U prvom upitu najduži dobar niz je $(2, \ 3, \ 2)$. Kako važi $2 \ and \ 2 > 2 \ xor \ 2$, $2 \ and \ 3 > 2 \ xor \ 3$ i $3 \ and \ 3 > 3 \ xor \ 3$, taj niz je dobar. U drugom upitu najduži dobar niz je $(2, \ 3)$, dok je u trećem upitu najduži dobar niz $(2)$.
	
	<br>
	
	## Ograničenja
	
	<br>
	
	- $1 \leq N, \ Q \leq 5 \cdot 10^5$
	- $1 \leq A_i \leq 10^9$
	- $1 \leq L \leq R \leq N$
	
	<br>
	
	Test primeri su podeljeni u $6$ disjunktnih grupa:
	
	- U testovima vrednim 10 poena: $N, Q \leq 10$
	- U testovima vrednim 15 poena: $A_i \leq 8$
	- U testovima vrednim 20 poena: svi članovi niza $A$ su stepeni dvojke, tj. $A_i = 2^{B_i}$ za neki niz $B$ 
	- U testovima vrednim 20 poena: $N, Q \leq 5000$
	- U testovima vrednim 15 poena: $N, Q \leq 10^5$
	- U testovima vrednim 20 poena: bez dodatnih ograničenja. 
	
	<br>
	
	## Napomena
	
	<br>
	
	Operator ekskluzivne disjunkcije u Pascal-u je označen sa  `xor`, dok u C++ ga zapisujemo pomoću simbola  `^`. Ova operacija $x\ \text{xor} \ y$ se za nenegativne cele brojeve $x,y$ definiše na sledeći način. Prvo se brojevi zapišu u binarnom zapisu. Ukoliko jedan broj ima manje cifara od drugog, dopisuju mu se vodeće nule sve dok ne budu imali isti broj binarnih cifara. Tako se dobijaju dva niza binarnih cifara, označimo ih sa $a_1, \ldots, a_k$ i $b_1, \ldots b_k$. Zatim se za svaku poziciju $i \in {1, \ldots, k }$ računa $c_i$ pomoću sledećih pravila:
	
	-   Za $a_{i} = 0, b_{i} = 0$ važi $c_{i} = 0$
	-   Za $a_{i} = 0, b_{i} = 1$ važi $c_{i} = 1$
	-   Za $a_{i} = 1, b_{i} = 0$ važi $c_{i} = 1$
	-   Za $a_{i} = 1, b_{i} = 1$ važi $c_{i} = 0$
	
	Niz binarnih cifara $c_1, \ldots, c_k$ (koji možda ima vodeće nule) je binarni zapis rezultata, odnosno broja $x \ \text{xor} \ y$.
	
	<br> 
	
	Operator konjunkcije u Pascal-u je označen sa `and`, dok u C++ ga zapisujemo pomoću simbola `&`. Ova operacija $x\ \text{and} \ y$ se za nenegativne cele brojeve $x,y$ definiše na sledeći način. Prvo se brojevi zapišu u binarnom zapisu. Ukoliko jedan broj ima manje cifara od drugog, dopisuju mu se vodeće nule sve dok ne budu imali isti broj binarnih cifara. Tako se dobijaju dva niza binarnih cifara, označimo ih sa $a_1, \ldots, a_k$ i $b_1, \ldots b_k$. Zatim se za svaku poziciju $i \in \{1, \ldots, k \}$ računa $c_i$ pomoću sledećih pravila:
	
	* Za $a_{i} = 0, b_{i} = 0$ važi $c_{i} = 0$
	* Za $a_{i} = 0, b_{i} = 1$ važi $c_{i} = 0$
	* Za $a_{i} = 1, b_{i} = 0$ važi $c_{i} = 0$
	* Za $a_{i} = 1, b_{i} = 1$ važi $c_{i} = 1$
	
	Niz binarnih cifara $c_1, \ldots, c_k$ (koji možda ima vodeće nule) je binarni zapis rezultata, odnosno broja $x \ \text{and} \  y$.
	
	<br> 
	
=== "Rešenje"

	| Autor | Tekst i test primeri | Analiza rešenja | Testiranje |
	|:-:|:-:|:-:|:-:|
	| Miloš Milutinović | Miloš Milutinović | Miloš Milutinović | Aleksa Milisavljević |
	
	## Rešenje kada $N, Q \leq 10$

	Možemo za svaki podniz izabrati koje elemente želimo da koristimo u nizu, i za dobijeni niz proverimo da li je on dobar koristeći grubu silu. Složenost $O(Q N^2 2^N).$

	## Rešenje kada su svi elementi stepeni dvojke

	Primetimo da ako uzmemo dva ista elementa za njih očigledno važi $X = X \ and \ X > X \ xor \ X = 0$. Takođe ukoliko uzmemo dva različita elementa za njih važi $0 = X \ and \ Y < X \ xor \ Y = X + Y$. Time se dobija da je dovoljno naći element koji se najviše puta pojavljuje. To se može uraditi tako što se svaki član niza zameni kao $A_i = log_2{A_i}$. Kako je sada $0 \leq A_i \leq 30$, možemo napraviti prefiksne sume po broju pojavljivanja svakog elementa i odgovoriti upite lako. Složenost $O((N + Q) log_2{A})$.

	## Rešenje kada $N, Q \leq 5000$

	Ukoliko izaberemo dva elementa čiji su najveći bitovi različiti, tada uslov očigledno neće važiti, jer $and$ neće sadržati taj bit dok $xor$ hoće. Slično ukoliko su im najveći bitovi isti, $and$ će sadržati taj bit dok $xor$ neće. Time dobijamo uslov da je niz dobar ukoliko svaki par brojeva ima isti najveći bit. Sada svaki član niza zamenimo njegovim najvećim bitom. Za svaki upit potrebno je odgovoriti sa najvećim brojem pojavljivanja nekog elementa u podnizu. To možemo lako uraditi grubom silom. Složenost $O(N Q)$.

	## Glavno rešenje

	Kombinovaćemo prethodne dve ideje. Nakon zamene svakog elementa sa njegovim najvećim bitom važiće $0 \leq A_i \leq 30$. Sada možemo napraviti prefiksne sume kao u podzadatku gde je svaki element stepen dvojke i na isti način odgovoriti upite. Složenost $O((N + Q) log_2{A})$.
