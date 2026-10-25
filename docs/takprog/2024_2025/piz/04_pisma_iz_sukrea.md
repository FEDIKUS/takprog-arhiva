---
hide:
  - toc
---

# 4 - Pisma iz Sukrea

=== "Zadatak"
	
	| Vremensko ograničenje | Memorijsko ograničenje |
	|:-:|:-:|
	| 2000ms | 64MB |
	
	Kakav bi to fudbaler Tirke bio da nema ljubavnih problema, tek nakon što je stigao u Sukre na IOI (Istraživanje ofsajda u informatici). U današnje vreme bez interneta i mobilnih telefona, jedini način da kontaktira svoju devojku u dalekoj Srbiji jeste slanjem pisma. Put do Sukrea nosi sa sobom razne pustolovine (jahanje konja, plivanje po Amazonu, penjanje uz lijane...) zbog čega je Tirke odlučio da u svojem ljubavnom pismu koristi isključivo nule i jedinice, umesto slova (ne želi saznati šta bi se desilo ukoliko se pismo ošteti, neka slova postanu nečitljiva i njegova devojka ga pogrešno razume).
	
	<br>
	
	Tirketovo pismo sadrži binarnu reč $S$. Definišimo operaciju nad jednom binarnom rečju $S$ na sledeći način: neka je $N$ dužina $S$, izaberimo segment $[l, r]$ $(1 \leq l \leq r \leq N)$ i zatim zamenimo ceo segment karaktera od $l$ do $r$ sa jednim karakterom koji je $xor$ svih karaktera na tom segmentu, gde $xor$ predstavlja operaciju bitovske ekskluzije. Preciznije, neka je reč pre opreracije bila $S_1S_2\cdots S_N$ i neka je $c = S_l \text { xor } S_{l+1} \text { xor } \cdots \text { xor } S_r$, onda $S$ postaje $S_1S_2\cdots S_{l-1} \ c \ S_{r+1}\cdots S_N$.
	
	<br>
	
	Pre nego što Tirke svoje pismo da malom Stanoju da ga pošalje za Srbiju, on mora prvo proveriti kvalitet binarne reči zapisane na njemu. Naime, kvalitet binarne reči definišemo kao broj različitih binarnih reči koje možemo dobiti primenom pomenute operacije proizvoljnan broj puta. Kako taj broj može biti veoma velik (i potencijalno otići u ofsajd), Tirketa zanima samo ostatak pri deljenju broja različitih binarnih reči koje možemo postići sa brojem $998244353$.
	
	<br>
	
	## Opis ulaza
	
	<br>
	
	U prvoj i jedinoj liniji standardnog ulaza data je binarna reč $S$.
	
	<br>
	
	## Opis izlaza
	
	<br>
	
	U prvoj i jedinoj liniji standardnog izlaza ispisati traženi broj iz teksta zadatka.
	
	<br>
	
	## Primer 1
	
	<br> 
	
	### Ulaz
	
	<br>
	
	```
	1010
	```
	
	<br>
	
	### Izlaz
	
	<br>
	
	```
	6
	```
	
	<br>
	
	## Objašnjenje
	
	<br> 
	
	Sve binarne reči koje možemo dobiti nakon primenjivanja operacije proizvoljan broj puta su $\{ 0, \ 00, \ 11, \ 101, \ 110, \ 1010 \}$, pa je onda i rešenje jednako $6$.
	
	<br>
	
	## Ograničenja 
	
	<br>
	
	- $1 \leq |S| \leq 300000$
	- $S_i \in \{0, 1\}$
	
	<br>
	
	Test primeri su podeljeni u $7$ disjunktnih grupa:
	- U testovima vrednim $5$ poena: $|S| \leq 5000$ i $S$ se sastoji samo od nula, tj. $S_i = 0$
	- U testovima vrednim $10$ poena: $|S| \leq 10$
	- U testovima vrednim $15$ poena: $|S| \leq 25$
	- U testovima vrednim $20$ poena: $|S| \leq 5000$ i $S$ se sastoji samo od jedinica, tj. $S_i = 1$
	- U testovima vrednim $15$ poena: $|S| \leq 400$
	- U testovima vrednim $15$ poena: $|S| \leq 5000$
	- U testovima vrednim $20$ poena: bez dodatnih ograničenja.
	
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
	
=== "Rešenje"
	
	| Autor | Tekst i test primeri | Analiza rešenja | Testiranje |
	|:-:|:-:|:-:|:-:|
	| Miloš Milutinović | Miloš Milutinović | Miloš Milutinović | Dragan Urošević |
	
	## Rešenje kada se $S$ sastoji samo od nula
	
	Primetimo da nikako ne možemo dobiti jedinicu, a možemo dobiti bilo koji string koji se sastoji od nula dužine od $1$ do $N$ tako da je rešenje $N$.
	
	## Rešenje kada je $|S| \leq 25$
	
	U ovom i prethodnom podzadatku možemo simulirati sva brisanja na razne načine tako što probamo odabir svih mogućih segmenata za operaciju, na primer BFS algoritmom.
	
	## Rešenje kada se $S$ sastoji samo od jedinica
	
	Posmatrajmo finalni string koji želimo da dobijemo. Potreban nam je algoritam da proverimo da li je moguće dobiti ga. Ispostavlja se da gramzivim algoritmom možemo uvek uzeti najmanji prefiks čiji je $xor$ jednak prvom karakteru, izbrišemo taj prefiks i dalje rešavamo na isti način. Ukoliko se $xor$ vrednosti početnog i finalnog stringa razlikuje svakako nije moguće, a u suptonom ukoliko je za svaki karakter finalnog stringa izabran neki segment karaktera, onda je moguće. Sada možemo raditi dinamičko programiranje gde će stanje biti $DP[dužina finalnog stringa][pozicija dokle je gridi algoritam stigao]$. Sa svake pozicije možemo dodati ili nulu ili jedinicu, i pošto su sve jedinice u početnom stringu, interval koji nas zanima će biti dužine najviše 2.
	
	## Rešenje kada je $|S| \leq 5000$
	
	Primetimo da možemo raditi isti $DP$ algoritam, samo nam je potrebno da brzo nađemo prvi segment čiji je $xor$ jednak nula ili jedan. To se lako može naći preko prefiksnih $xor$-ova.
	
	 ## Rešenje za sve poene
	
	 Možemo izbaciti dimenziju za dužinu finalnog stringa, jer je moguće iterirati po poziciji dokle je gramzivi algoritam stigao, pošto je moguće "zalepiti" sve nakon poslednjeg uzetog segmenta, gde ne dolazi do prebrojavanja istog stringa više puta.
	
	``` cpp title="04_pisma_iz_sukrea.cpp" linenums="1"
	# include <stdio.h>
	# include <stdlib.h>
	# include <string.h>
	
	# define MAXN 300300
	
	# define MOD 998244353
	
	int n;
	int res;
	char s1[MAXN];
	char s2[MAXN];
	char pxor[MAXN];
	int pos[MAXN][2];
	int dp[MAXN][2];
	
	int main() {
	  int d;
	  int k1, k2;
	  int i, j, k;
	  int xr, xr1, xr2;
	  scanf("%s", s1+1);
	  pxor[0] = 0;
	  for (i = 1; s1[i] != '\0'; i++) {
	  	s2[i] = s1[i] - '0';
	  	pxor[i] = pxor[i-1] ^ s2[i];
	  }
	  n = i - 1;
	  xr2 = pxor[n];
	  pos[n][0] = pos[n][1] = n + 1;
	  pos[n][pxor[n]] = n;
	  for (i = n - 1; i >= 0; i--) {
	  	pos[i][0] = pos[i+1][0];
	  	pos[i][1] = pos[i+1][1];
	  	pos[i][pxor[i]] = i;
	  }
	  dp[0][0] = 1;
	  k1 = 0; k2 = 1;
	  for (i = 1; i <= n; i++) {
	    for (xr = 0; xr < 2; xr++) {
	      j = pos[i][pxor[i-1] ^ xr];
	//  	      printf("A: d, i, j = %d, %d, %d\n", d, i, j);
	//  	      printf("B: d, i, j = %d, %d, %d\n", d, i, j);
	  	  if (j <= n) {
	  	    for (xr1 = 0; xr1 < 2; xr1++) {
	  	      dp[j][xr1 ^ xr] += dp[i-1][xr1];
	          if (dp[j][xr1 ^ xr] >= MOD)
	            dp[j][xr1 ^ xr] -= MOD;
	        }
		  }	
	    }
	    res += dp[i][xr2];
	    if (res >= MOD)
	      res -= MOD;
	  }
	  printf("%d\n", res);
	  return 0;
	}

	```
