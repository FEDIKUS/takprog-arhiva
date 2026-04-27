---
hide:
  - toc
---

# 5 - Dva niza

=== "Zadatak"
	
	| Vremensko ograničenje | Memorijsko ograničenje |
	|:-:|:-:|
	| 1000ms | 256MB |
	
	<br>
	
	*Najbolji poklon? Dva niza!*
	
	<br>
	
	Nakon što se Perica vratio iz svog istraživanja, ispostavilo se da mu je danas rođendan. Poklon za rođendan nije bio niz, već dva niza! Oba su se sastojala od nenegativnih celih brojeva i bila su iste dužine $N$. Označimo sa $A$ prvi niz i sa $B$ drugi niz. Oba niza su indeksirana brojevima od $1$ do $N$ redom. Kako je on najveći obožavatelj bitovskih operacija, odlučio je da smisli način da izmeri vrednost ta dva niza pomoću njih. Vrednost podniza koji se sastoji od elemenata na indeksima od $L$ do $R$ $(1 \leq L \leq R \leq N)$ jednaka je $(A_L$ $xor$ $A_{L+1}$  $xor$  $...$  $xor$  $A_R) \cdot (B_L$ $and$  $B_{L+1}$  $and$ $...$ $and$ $B_R)$, gde $xor$ predstavlja operaciju bitovske ekskluzivne disjunkcije, $and$ operaciju bitovske konjunkcije i $\cdot$ operaciju množenja. Vaš zadatak je da nađete vrednost podniza koji ima najveću vrednost - preciznije maksimalnu vrednost po svim podnizovima.
	
	<br>
	
	## Opis ulaza
	
	<br>
	
	U prvom redu standardnog ulaza, nalazi se jedan ceo broj $N$ - dužinu oba niza. U drugom redu standardnog ulaza se nalaze $N$ celih brojeva, gde $i$-ti broj predstavlja $A_i$. U trećoj i poslednjoj liniji standardnog ulaza se nalaze $N$ celih brojeva, gde $i$-ti broj predstavlja $B_i$.
	
	<br>
	
	## Opis izlaza
	
	<br>
	
	U prvoj i jedinoj liniji standardnog izlaza ispisati traženu maksimalnu vrednost. 
	
	<br>
	
	### Primer 1
	
	<br> 
	
	## Ulaz
	
	<br>
	
	```
	3
	4 5 2
	0 1 3
	```
	
	<br>
	
	## Izlaz
	
	```
	7
	```
	
	<br>
	
	### Objašnjenje
	
	Najveća vrednost se postiže za podniz $L = 2$, $R = 3$. $A_2$ $xor$ $A_3 = 7$ i $B_2$ $and$ $B_3 = 1$, pa je vrednost tog podniza $7 \cdot 1 = 7$. 
	
	<br>
	
	## Ograničenja
	
	<br>
	
	* $1 \leq N \leq 2 \cdot 10^5$
	
	* $0 \leq A_i, B_i \leq 10^9$
	
	<br>
	
	Test primeri su podeljeni u šest disjunktnih grupa: 
	
	* U testovima vrednim 4 poena: $N \leq 2000$.
	
	* U testovima vrednim 4 poena: $A_i = 1$.
	
	* U testovima vrednim 12 poena: $A_i \leq 500$.
	
	* U testovima vrednim 20 poena: $B_i = 1$.
	
	* u testovima vrednim 24 poena: $B_i \leq 3$.
	
	* U testovima vrednim 36 poena: Bez dodatnih ograničenja.
	
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
	
	Bitovska konjunkcija između $n$ elemenata $x_{1},x_{2},...,x_{n}$ definiše se kao $x_{1} \ \text{and} \ x_{2}  \ \text{and} \  ...  \ \text{and} \  x_{n} = (...(((x_{1}  \ \text{and} \  x_{2})  \ \text{and} \  x_{3}) \ \text{and} \ x_{4})...)  \ \text{and} \  x_{n}$.
	
	<br> 
	
=== "Rešenje"
	
	| Autor | Tekst i test primeri | Analiza rešenja | Testiranje |
	|:-:|:-:|:-:|:-:|
	| Miloš Milutinović | Miloš Milutinović | Miloš Milutinović | Filip Bojković |
	
	## Rešenje kada je $N \leq 2000$
	
	Fiksiramo $L$, i zatim pomeramo $R = L, L+1, \dots, N$, i prilikom pomeranja računamo $xor$ i $and$ vrednost intervala. Vremenska složenost je $O(N^2)$.
	
	## Rešenje kada je $A_i = 1$
	
	Primetimo da će optimalni interval sadržati samo jedan element, tj. $L = R$, jer izborom većeg intervala ne možemo dobiti veću vrednost ni za $xor$ ni za $and$. Odatle se vidi da je rešenje maksimalni element u nizu $B$. 
	
	## Rešenje kada je $A_i \leq 500$
	
	Uvedimo niz $pref_i = A_1$ $xor$ $A_2$ $\dots$ $xor$ $A_i$ koji ćemo nadalje koristiti.
	
	Moguće je za svako $R$ fiksirati $xor$ vrednost intervala, neka je ta vrednost $X$. Tada znamo da važi $pref_R$ $xor$ $pref_{L - 1} = X$, tj. $pref_R$ $xor$ $X = pref_{L - 1}$. Primetimo da je nama optimalno izabrati najveće $L$ koje ispunjava taj uslov. U pomoćnom nizu $aux_i$ ćemo čuvati najveće $L$ takvo da je $pref_{L - 1} = i$. Time za svako $R$ i $X$ možemo naći optimalno $L$ i izračunati vrednost tog podniza. Vremenska složenost je $O(N \cdot maxA)$, gde $maxA$ predstavlja maksimalnu vrednost za $A_i$.
	
	## Rešenje kada je $B_i = 1$
	
	U ovom podzadatku je potrebno naći interval sa najvećom $xor$ vrednosti. Ovo je standardan problem koji se rešava korišćenjem strukture podataka "trie". Krećući se redom $R = 1, 2, \dots, N$ tražićemo najveću vrednost $pref_R$ $xor$ $pref_{L - 1}$. To radimo tako što sve prefiksne $xor$-ove ubacujemo u strukturu "trie". Kada za dati broj $x$ tražimo najveći $xor$, možemo da krenemo pretragu u strukturi počev od najvišeg bita, tj. korena strukture, i u svakom trenutku ukoliko postoji sin trenutnog čvora sa bitom suprotnim u odnosu na odgovarajući bit broja $x$, u njemu nastavljamo pretragu povećavajući maksimalni $xor$ za odgovarajuću vrednost, dok ukoliko ne postoji taj sin, pretragu nastavljamo u jedinom sinu.
	
	## Rešenje kada je $B_i \leq 3$
	
	Ovaj podzadatak je namenjen jednostavnijim/neefikasnijim implementacijama rešenja za sve poene.
	
	## Glavno rešenje
	
	Primetimo da za dato $R$ postoji najviše $\log_2 A$ različitih $and$ vrednosti za interval sa datom desnom granicom. To je trivijalno dokazati, jer prilikom dodavanja broja u neki skup, $and$ vrednost tog skupa može samo "izgubiti" neke bitove, kojih je na početku moguće maksimalno imati $\log_2 maxA$. Sada možemo čuvati po jednu "trie" strukturu, u kojim ćemo čuvati prefiksne $xor$-eve, za svaki interval levih granica sa istom "and" vrednošću. Prilikom prelaska na sledeću desnu granicu, moguće je da će se neki intervali levih granica spojiti, pa je potrebno spojiti i njihove "trie" strukture. To je moguće uraditi na više načina, npr. čuvati te strukture u implicitnom obliku pa je moguće sve elemente jedne strukture direktno prebaciti u drugu, pod uslovom da prvu izbrišemo. Vremenska složenost tog dela je ukupno $O(N \cdot {\log^2 maxA})$, jer svaki element će biti prebačen najviše logaritamski broj puta u drugu "trie" strukturu i prebacivanje jednog elementa se vrši u logaritamskoj složenosti. Za kraj kako bismo našli rešenje, za svako $R$, počevši od $1$ i redom sve do $N$, prolazimo kroz segmente sa istom $and$ vrednošću i u svakom intervalu tražimo najveću vrednost za $pref_R$ $xor$ $pref_{L - 1}$. Vremenska složenost je $O(N \cdot {\log^2 maxA})$, memorijska složenost je $O(N \cdot {\log maxA})$.
	
	``` cpp title="05_dvaniza.cpp" linenums="1"
	#include <bits/stdc++.h>
	
	using namespace std;
	
	const int MAX = int(2e5);
	
	const int NODES = MAX * 31;
	
	int root[MAX], ch[NODES + 5][2], tsz;
	
	int ids[NODES + 5], stk_beg, stk_end;
	
	vector<int> vals[MAX];
	
	int newNode() {
	  int ret = ids[stk_beg];
	  stk_beg = (stk_beg + 1) % NODES;
	  return ret;
	}
	
	void delNode(int id) {
	  stk_end = (stk_end + 1) % NODES;
	  ids[stk_end] = id;
	}
	
	void InsertXor(int& node, int bit, int val) {
	  if (!node) {
	    node = newNode();
	  }
	  if (bit < 0) {
	    return;
	  }
	  int my = (val >> bit & 1);
	  InsertXor(ch[node][my], bit - 1, val);
	}
	
	int QueryMax(int node, int bit, int val) {
	  if (bit < 0) {
	    return 0;
	  }
	  int my = (val >> bit & 1);
	  if (ch[node][my ^ 1] > 0) {
	    return QueryMax(ch[node][my ^ 1], bit - 1, val) + (1 << bit);
	  } else {
	    return QueryMax(ch[node][my], bit - 1, val);
	  }
	}
	
	void Clear(int& node) {
	  if (ch[node][0] > 0) {
	    Clear(ch[node][0]);
	  }
	  if (ch[node][1] > 0) {
	    Clear(ch[node][1]);
	  }
	  delNode(node);
	  node = 0;
	}
	
	int main() {
	  ios::sync_with_stdio(false);
	  cin.tie(0);
	  {
	    stk_beg = 0;
	    stk_end = NODES - 1;
	    for (int i = 0; i < NODES; i++) {
	      ids[i] = i + 1;
	    }
	  }
	  int n;
	  cin >> n;
	  vector<int> a(n);
	  for (int i = 0; i < n; i++) {
	    cin >> a[i];
	  }
	  vector<int> b(n);
	  for (int i = 0; i < n; i++) {
	    cin >> b[i];
	  }
	  vector<int> pref(n);
	  for (int i = 0; i < n; i++) {
	    pref[i] = (i == 0 ? 0 : pref[i - 1]) ^ a[i];
	  }
	  vector<pair<int, int>> segs;
	  int64_t res = 0;
	  for (int i = 0; i < n; i++) {
	    res = max(res, a[i] * 1LL * b[i]);
	    for (auto& p : segs) {
	      p.first &= b[i];
	    }
	    {
	      // Update results
	      for (auto& p : segs) {
	        res = max(res, int64_t(QueryMax(root[p.second], 31, pref[i])) * int64_t(p.first));
	      }
	    }
	    segs.emplace_back(b[i], i);
	    InsertXor(root[i], 31, i == 0 ? 0 : pref[i - 1]);
	    vals[i].push_back(i == 0 ? 0 : pref[i - 1]);
	    {
	      // Merge equal segments
	      vector<pair<int, int>> new_segs;
	      for (int x = 0; x < int(segs.size()); x++) {
	        int y = x;
	        while (y + 1 < int(segs.size()) && segs[y + 1].first == segs[x].first) {
	          y += 1;
	        }
	        int pos = segs[x].second;
	        for (int t = x + 1; t <= y; t++) {
	          Clear(root[segs[t].second]);
	          for (int v : vals[segs[t].second]) {
	            InsertXor(root[pos], 31, v);
	            vals[pos].push_back(v);
	          }
	        }
	        new_segs.push_back(segs[x]);
	        x = y;
	      }
	      swap(segs, new_segs);
	    }
	  } 
	  cout << res << '\n';
	  return 0;
	}

	```
