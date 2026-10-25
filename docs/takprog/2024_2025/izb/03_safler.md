---
hide:
  - toc
---

# 3 - Šafler

=== "Zadatak"
	
	| Vremensko ograničenje | Memorijsko ograničenje |
	|:-:|:-:|
	| 1500ms | 256MB |
	
	Čuveni šafler karata mister Šafl je konačno došao u vaš grad. Da bi ga impresionirali odlučili ste da rešite problem traženja *šaflnesa* špila. Pred tobom se nalazi $N$ karata gde je na $i$-toj karti zapisan broj $A_i$. *Šaflnes* špila predstalja broj mogućih rasporeda karata koji se mogu dobiti primenom zamena karata. Te zamene se ne mogu raditi na bilo koji način, već za svako $1 \leq i \leq N-1$ će se **tačno** jednom zameniti karte $A_i$ i $A_{i+1}$. Naravno, različitim redosledom biranja $i$-ova za zamene, možemo dobiti različite finalne rasporede karata. 
	
	<br>
	
	Potrebno je naći *šaflnes* datog špila karata. Preciznije, potrebno je naći koliko rasporeda datih karata možemo dobiti primenjivanjem gore navedenih zamena. Kako taj broj može biti velik, potrebno je naći ostatak pri deljenju tog broja sa brojem $998244353$.
	
	## Opisi funkcija
	
	Potrebno je da implementirate funkciju 
	
	- $Safler(N, A[\ldots])$
	
	Ova funkcija će biti pozvana jednom po primeru. Broj $N$ predstavlja broj karata. Niz $A$ dužine $N$ predstavlja zapisane brojeve na kartama. **Niz $A$ je indeksiran od 1.**
	
	## Primer
	
	Neka je $N = 3, \ A = \{2, 1, 1\}$. Ukoliko prvo zamenimo $A_2$ i $A_3$ i nakon toga zamenimo $A_{1}$ i $A_2$ dobijamo niz $\{1, 2, 1\}$. Takođe možemo prvo zameniti $A_{1}$ i $A_2$ i nakon toga $A_2$ i $A_3$ čime dobijamo niz $\{1, 1, 2\}$. Kako su ova dva niza različita rešenje za ovaj primer je $2$.
	
	## Ograničenja
	
	* $1 \leq N \leq 500.000$
	* $1 \leq A_i \leq N$
	
	## Podzadaci
	
	Test primeri su podeljeni u $6$ podzadataka:
	
	-   **[6 poena]:** Svi elementi niza $A$ su različiti
	-   **[4 poena]:** $N \leq 8$
	-   **[15 poena]:** $N \leq 100$
	-   **[29 poena]:** $N \leq 500$
	-   **[20 poena]:** $N \leq 5.000$
	-   **[26 poena]:** Nema dodatnih ograničenja
	
	## Detalji implementacije
	
	Potrebno je da pošaljete tačno jedan fajl  `safler.cpp`  koji implementira pomenute funkcije. Osim traženih funkcija, vaš fajl može sadržati i dodatne globalne promenljive, pomoćne funkcije i dodatne biblioteke.
	
	Vaša funkcija mora biti sledećeg oblika:
	
	`int Safler(int N, int* A);`
	
	**Vašim programima je dozvoljeno da menjaju sadržaj nizova ali ne smeju da pristupaju van granica datih nizova.**
	
	Uz zadatak, obezbeđen vam je "template" fajl  `code.cpp`  koji možete koristiti i menjati po potrebi. Takođe vam je obezbeđen program  `grader.cpp`  koji služi da lakše testirate kodove. Ovaj program učitava sa standardnog ulaza sledeće podatke:
	
	- U prvom redu broj $N$.
	- U narednom redu $N$ brojeva $A_i$.
	
	Zatim ovaj program zove vašu funkciju i ispisuje rezultat koji vaša funkcija vrati.
	
=== "Rešenje"
	
	| Autor | Tekst i test primeri | Analiza rešenja | Testiranje |
	|:-:|:-:|:-:|:-:|
	| Mihailo Jančević | Miloš Milutinović | Filip Bojković uz veliku pomoć Mihaila Jančevića | Dragan Urošević |
	
	## Svi elementi su različiti
	Pošto su svi elementi različiti, a nas interesuje samo broj različitih nizova koje možemo da dobijemo, same vrednosti elemenata nam nisu bitne, pa će svi nizovi dužine $n$ imati isto rešenje. Neka je $s_n$ rešenje za nizove dužine $n$. Primetimo da kada dodajemo novi element na kraj niza je jedino bitno da li operaciju menjanja poslednja dva elementa radimo pre ili posle operacije menjanja pretposlednjeg i trećeg od pozadi. Ako smo prvo zamenili poslednji i pretposlednji element, onda se prvih $n-2$ elemenata zajedno sa originalnim poslednjim ponašaju kao niz dužine $n-1$ sa svim različitim elementima. Ako smo prvo zamenili pretposlednji i treći od pozadi, onda se prvih $n-1$ elemenata ponašaju kao niz dužine $n-1$ sa svim različitim elementima, pri čemu će se u nekom trenutku zameniti poslednja dva elementa i to neće imati nikakve posledice na ostatak niza. Odavde sledi da je $s_n=2\cdot s_{n-1}$ za $n>2$ (jer smo koristili barem tri elementa u gorenavedenoj tranziciji). Očigledno je $s_1=s_2=1$.
	
	Vremenska složenost: $O(N)$
	Memorijska složenost: $O(N)$
	
	## $N\leq 8$
	U ovom podzadatku je dovoljno isprobati sve moguće rasporede operacija. Kako imamo $N-1$ mogućih operacija, broj mogućih rasporeda za te operacije je $(N-1)!$ i za svaki od tih rasporeda treba da vidimo koji niz dobijamo i da eliminišemo duplikate.
	
	Vremenska složenost: $O(N!)$
	Memorijska složenost: $O(2^N)$
	
	## Šta dalje?
	Posmatrajmo zamenu na pozicijama $i$ i $i+1$, ona će prebaciti tačno jedan element sa leve na desnu stranu i tačno jedan element sa desne na levu stranu. Primetimo da je to jedini način da neki element iz $[1,i]$ pređe u $[i+1,N]$ i obrnuto. Kako se ta zamena mora dogoditi, za svaki prefiks će tačno jedan element preći iz njega u njemu odgovarajući sufiks, i jedan element iz tog sufiksa će preći u prefiks. Ovo nas navodi da probamo da rešimo zadatak dinamičkim programiranjem sa sledećim stanjima: $dp_{i,j,k} = \text{broj različitih permutacija za prvih }i\text{ elemenata ako u taj prefiks uđe }j{ i iz njega izađe }k$.
	
	Potrebno je pronaći tranzicije. Udahnimo duboko i posmatrajmo dva slučaja:
	- $k\neq A_i$:
	
	> Kako $k$ mora da dođe do pozicije $i$ pre nego što izađe iz prefiksa dužine $i$, tako su nam sve zamene između pozicije gde se nalazi $k$ i $i$-te pozicije jednoznačno određene i one baš prebacuju $a_i$ u prefiks prvih $i-1$ elemenata i iz njega izbacuje $k$. Tako dobijamo:
	> $dp_{i,j,k} = dp{i-1,A_i,k}$
	
	- $k = A_i$:
	
	>    - Ako se zamena $(i-1,i)$ desila pre zamene $(i,i+1)$:
	>    > u ovom slučaju je jasno da se prefiks prvih $i-1$ elemenata ponaša izolovano i da je rešenje $dp_{i-1,A_i,A_i}$.
	>
	>    - Ako se zamena $(i,i+1)$ desila pre zamene $(i-1,i)$:
	>    > Kako je $j$ ušao u prefiks dužine $i$ pre nego što se desila zamena $(i-1,i)$, to će $j$ ući u u prefiks dužine $i-1$, dok će iz njega može izaći bilo koji element. U prevodu, rešenje je $\sum_{x\text{ u prefiksu dužine }i-1}dp_{i-1,j,x}$. 
	>
	>   - Sada primetimo da je moguće da smo u prošla dva slučaja neke rasporede brojali dva puta. To je jedino moguće ako u prvom slučaju $A_i$ uđe i izađe (iz prefiksa $i-1$) i ako u drugom slučaju $j$ uđe i izađe (iz prefiksa $i-1$) ili ako je $A_i=j$.
	>   > - Uradimo prvo slučaj kada je $A_i=j$:
	>   >   > Ovo je zapravo slučaj u kome je $A_{i-1}=A_i=A_{i+1}$, tada se ceo prvi slučaj sadrži u drugom i samo je potrebno oduzeti $dp_{i-1,A_i,A_i}$.
	>   > - Sada razmatramo šta se dešava kada $A_i\neq j$:
	>   >   > Prvo primetimo da nije moguće da se u oba prebrojavanja zamena $(i-2,i-1)$ desila pre zamene $(i-1,i)$, tako je u nekom slučaju $A_{i-1}$ baš element koji izlazi iz prefiksa dužine $i-1$ pa je $A_{i-1}=A_i$ ili $A_{i-1}=j$.
	>   >   > - $A_{i-1}=A_i$:
	>   >   >   > Detaljnim razmatranjem ovog slučaja dobijamo da je višak $dp_{i-2,A_i,j}$.
	>   >   > - $A_{i-1}=j$:
	>   >   >   > Detaljnim razmatranjem ovog slučaja dobijamo da je višak $dp_{i-2,j,A_i}$.
	
	Sada možemo da izdahnemo i rezimiramo:
	```python
	if k != A[i]:
	    dp[i][j][k] = dp[i-1][A[i]][k]
	else:
	    dp[i][j][k] = dp[i-1][A[i]][A[i]] + sum([dp[i-1][j][x] for x in range(1,N+1)])
	    if A[i] == j:
	        dp[i][j][k] -= dp[i-2][A[i]][j]
	    elif A[i-1] == j:
	        dp[i][j][k] -= dp[i-2][j][A[i]]
	```
	
	## $N\leq 100$
	Naivnom implementacijom gorenavedenih tranzicija dobijamo rešenje ovog podzadatka.
	
	Vremenska složenost: $O(N^4)$
	Memorijska složenost: $O(N^3)$
	
	## $N\leq 500$
	Polunaivnom implementacijom gorenavedenih tranzicija dobijamo rešenje ovog podzadatka.
	
	Vremenska složenost: $O(N^3)$
	Memorijska složenost: $O(N^3)$
	
	## $N\leq 5000$
	Za rešenje ovog podzadatka primetimo da $dp_{i,j,k}$, kada je $k\neq A_i$, ne zavisi od $j$. Možemo sada napraviti dve tabele:
	- $dp^1$ za slučaj kada je $k\neq c$
	> $dp^1_{i,k} := dp_{i,j,k}$ za $k\neq c$ i $dp^1_{i,k} := 0$ za $k=c$
	- $dp^2$ za slučaj kada je $k=c$:
	> $dp^2_{i,j} := dp_{i,j,c}$
	
	Efikasnim računanjem ove dve tabele dobijamo rešenje ovog podzadatka.
	
	Vremenska složenost: $O(N^2)$
	Memorijska složenost: $O(N^2)$
	
	## $N\leq 500000$
	
	Za celo rešenje je dovoljno primetiti da skoro sve promene koje se dešavaju između $dp^1_i$ i $dp^1_{i+1}$ kao i između $dp^2_i$ i $dp^2_{i+1}$ se dešavaju paralelno. Tako možemo da, umesto da za svako $i$ računamo ceo niz iznova, primetimo da su nam potrebna samo prethodna dva niza i da na njima podržavamo operacije: ”promeni element na jednoj poziciji”, ”dodaj broj na sve elemente niza”, ”oduzmi ceo niz od drugog”. Za detalje možete pogledati implementaciju komisijskog rešenja.
	
	Vremenska složenost: $O(N)$
	Memorijska složenost: $O(N)$
	
	
	``` cpp title="03_safler.cpp" linenums="1"
	#include <bits/stdc++.h>
	
	using namespace std;
	
	const int md = 998244353;
	
	int add(int x, int y) {
	  return x + y < md ? x + y : x + y - md;
	}
	
	int sub(int x, int y) {
	  return x >= y ? x - y : x - y + md;
	}
	
	int mul(int x, int y) {
	  return x * 1LL * y % md;
	}
	
	const int N = 500005;
	
	int a[N], dp1[N], coeff[N], all_add[N], ft[N], lst[N];
	vector<pair<int, int>> upd1[N];
	vector<pair<int, int>> upd2[N];
	vector<array<int, 3>> chn[N];
	vector<array<int, 3>> qs[N];
	
	int get1(int i, int k) {
	  int t = int(upd1[k].size()) - 1;
	  while (t >= 0 && upd1[k][t].first > i) {
	    t -= 1;
	  }
	  if (t < 0) {
	    return 0;
	  }
	  return upd1[k][t].second;
	}
	
	int get2(int i, int j) {
	  if (i < 0) {
	    return 0;
	  }
	  int ret = all_add[i];
	  {
	    int t = int(upd2[j].size()) - 1;
	    while (t >= 0 && upd2[j][t].first > i) {
	      t -= 1;
	    }
	    if (t >= 0) {
	      ret = add(ret, upd2[j][t].second);
	    }
	  }
	  if (i >= 2) {
	    int t = int(chn[j].size()) - 1;
	    while (t >= 0 && chn[j][t][0] > i) {
	      t -= 1;
	    }
	    if (t >= 0) {
	      ret = sub(ret, chn[j][t][1]);
	      ret = sub(ret, mul(chn[j][t][2], coeff[i] - coeff[chn[j][t][0] - 1]));
	    } 
	  }
	  return ret;
	}
	
	int query(int i, int j, int k) {
	  int c = a[i];
	  if (k != c) {
	    return get1(i, k);
	  } else {
	    return get2(i, j); 
	  }
	}
	
	int Safler(int n, int*A) {
	  for (int i = 0; i < n; i++) {
	    a[i] = A[i + 1] - 1;
	    assert(0 <= a[i] && a[i] < n);
	  }
	  all_add[0] = 1;
	  int tot = 0;
	  for (int i = 1; i + 1 < n; i++) {
	    coeff[i] = coeff[i - 1];
	    int c = a[i];
	    int s = tot;
	
	    
	
	    qs[i + 2].push_back({i, a[i - 1], get2(i - 1, c)});
	    tot = sub(tot, dp1[a[i - 1]]);
	    dp1[a[i - 1]] = get2(i - 1, c); // dp2[i - 1][c];
	    tot = add(tot, dp1[a[i - 1]]);
	    upd1[a[i - 1]].emplace_back(i, get2(i - 1, c));
	
	
	    tot = sub(tot, dp1[c]);
	    qs[i + 2].push_back({i, c, 0});
	    dp1[c] = 0;    
	    upd1[c].emplace_back(i, 0);
	
	    s = sub(s, get1(i - 1, a[i - 1])); 
	    s = add(s, query(i - 1, c, c));
	
	    all_add[i] = add(all_add[i - 1], s);
	
	
	    for (auto& [p, x, v] : qs[i]) {
	      if (chn[x].empty()) {
	        chn[x].push_back({1, 0, 0});
	      } 
	      chn[x].push_back({i, add(chn[x].back()[1], mul(coeff[i - 1] - coeff[chn[x].back()[0] - 1], chn[x].back()[2])), v});
	    }
	
	    if (i >= 2 && a[i - 1] == c) {
	      coeff[i] += 1;
	      if (upd2[a[i - 2]].empty()) {
	        upd2[a[i - 2]].emplace_back(-1, 0);
	      }
	      upd2[a[i - 2]].emplace_back(i, add(upd2[a[i - 2]].back().second, sub(get1(i - 2, a[i - 2]), get2(i - 2, c))));
	      if (upd2[c].empty()) {
	        upd2[c].emplace_back(-1, 0);
	      }
	      upd2[c].emplace_back(i, add(upd2[c].back().second, query(i - 2, c, c)));
	    } else if (i >= 2) {
	      if (upd2[a[i - 1]].empty()) {
	        upd2[a[i - 1]].emplace_back(-1, 0);
	      }
	      upd2[a[i - 1]].emplace_back(i, sub(upd2[a[i - 1]].back().second, query(i - 2, a[i - 1], c)));
	    }
	    if (upd2[c].empty()) {
	      upd2[c].emplace_back(-1, 0);
	    }
	    upd2[c].emplace_back(i, sub(upd2[c].back().second, query(i - 1, c, c)));
	  }
	  int res = 0;
	  for (int i = 0; i < n; i++) {
	    res = add(res, query(n - 2, a[n - 1], i));
	  }
	  return res;
	}

	```
