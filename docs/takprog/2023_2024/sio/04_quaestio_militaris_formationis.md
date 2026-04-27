---
hide:
  - toc
---

# 4 - Quaestio militaris formationis

=== "Zadatak"
	
	| Vremensko ograničenje | Memorijsko ograničenje |
	|:-:|:-:|
	| 1000ms | 256MB |
	
	Postoji niz $A$ sa $N$ elemenata. Međutim, vama je poznat isključivo broj elemenata niza $A$, ali ne i njihove vrednosti. Možete da postavite najviše $Q$ pitanja formata "Ukoliko bi niz $A$ bio sortiran neopadajuće, koja vrednost bi se našla na poziciji $i$", gde je $1 \leq i \leq N$. 
	
	<br>
	
	Odgovorite na $T$ upita oblika: "Koliko elemenata niza $A$ je **strogo manje** od $X$".
	
	<br>
	
	## Opis funkcija
	
	<br>
	
	Potrebno je da implementirate funkciju
	
	<br>
	
	* $\text{BrojManjih}(N, Q, T, X, O)$
	
	<br>
	
	Ova funkcija će biti pozvana jednom po primeru. $N$ predstavlja broj elemenata niza $A$. $Q$ predstavlja broj pitanja koje možete da postavite. $T$ predstavlja broj upita. U $i$-tom upitu ($1 \leq i \leq T$), potrebno je odgovoriti na pitanje: "Koliko elemenata niza $A$ je strogo manje od $X[i]$" i taj odgovor upisati u $O[i]$.
	   **Svi nizovi su indeksirani od 1.**
	
	<br>
	
	Vaš program može da koristi funkciju
	
	<br>
	
	$\text{Pitaj}(i)$
	
	<br>
	
	koja kao odgovor vraća vrednost elementa niza $A$ na poziciji $i$.
	
	
	
	<br>
	
	## Ograničenja
	
	<br>
	
	* $1 \leq A[i] \leq 10^9$
	* $1 \leq X[i] \leq 10^9$
	* $1 \leq T \leq 10$
	
	<br>
	
	## Podzadaci
	
	<br>
	
	Test primeri su podeljeni u $3$ podzadatka.
	
	<br>
	
	* **[10 poena]:** $1 \leq N \leq 1000$, $Q = 10000$
	* **[20 poena]:** $1 \leq N \leq 1000$, $Q = 1000$
	* **[70 poena]:** $1 \leq N \leq 100000$, $Q = 200$
	
	<br>
	
	## Detalji implementacije
	
	<br>
	
	Potrebno je da pošaljete tačno jedan fajl koji implementira pomenutu funkciju. Osim tražene funkcije, vaš fajl može da sadrži i dodatne globale promenljive, pomoćne funkcije i dodatne biblioteke.
	
	<br>
	
	Vaša funkcija mora biti sledećeg oblika:
	
	<br>
	
	`void BrojManjih(int N, int Q, int T, int* X, int* O)`
	
	<br>
	
	Vaš program mora ulljučivati header `code.h`, u kom je definisana funkcija $\text{Pitaj}$ sledećeg potpisa:
	
	<br>
	
	`int Pitaj(int i)`
	
	<br>
	
	Uz zadatak, obezbeđen vam je "template" fajl `code.cpp` koji možete koristiti i menjati po potrebi. Takođe vam je obezbeđen program `grader.cpp` koji služi da lakše testirate kodove. Ovaj program učitava sa standardnog ulaza sledeće podatke:
	
	
	<br>
	
	* U prvom redu brojeve $N$, $Q$ i $T$.
	* U drugom redu niz $A$ sa $N$ elemenata.
	* U trećem redu niz $X$ sa $T$ elemenata.
	
	<br>
	
	Ovaj program potom zove vašu funkciju i ispisuje odgovor na standardni izlaz.
	
	<br>
	
	Ukoliko vaše rešenje koristi funkciju $\text{Pitaj}$ više od $Q$ puta, biće prekinuto sa statusom `RTE` (runtime error). Takođe, ukoliko vaše rešenje pozove funkciju $\text{Pitaj}$ sa argumentom $i$ za koji ne važi $1 \leq i \leq N$,  biće prekinuto sa statusom `RTE` (runtime error).
	
=== "Rešenje"
	
	| Autor | Tekst i test primeri | Analiza rеšenja | Testiranje |
	|:-:|:-:|:-:|:-:|
	| Pavle Martinović | Marko Šišović | Pavle Martinović | Dragan Urošević |
	
	## Rešenje kada $N\leq 10$
	Naprosto za svaku od $N!$ permutacija možemo izračunati koliko inverzija daju. Složenost $O(N^2N!)$.
	## Rešenje kada nije potrebno naći niz slabosti
	Neka definišimo distancu $d$ dve prermutacije $p,q$ kao najmanji broj zamena susednih elemenata da bi se stiglo od jednog do drugog. Ako $id$ označava permutaciju identitete, znamo da je $d(id,p)$ zapravo broj inverzija permutacije $p$. Takođe jedna trivijalna opservacija je da je $d(p,q)=d(r\circ p,r\circ q)$ jer u ovom slučaju samo menjamo $i$ sa $r[i]$ u obe permutacije, što očigledno nikako ne menja problem. Označimo sa $r^{-1}$ inverznu permutaciju permutacije $r$. Za date permutacije $p$ i $q$, nama je potrebna minimalna vrednost $\max\{d(id,r\circ p),d(id,r\circ q)\}$ po svim $r$, odnosno $\max\{d(r^{-1},p),d(r^{-1},q)\}$. Pošto je očigledno $d(p,r^{-1})+d(r^{-1},q)\ge d(p,q)$ (možemo da dobijemo $q$ od $p$ tako što prvo dobijemo $r^{-1}$ u minimalnom broju poteza pa onda odatle $q$ u minimalnom broju poteza), znamo da je tražena vrednost barem $\lceil\frac{d(p,q)}{2}\rceil$. Međutim, ovu vrednost je moguće dobiti, prosto uzmemo najkraći niz zamena susednih koji vodi od $p$ do $q$ i onda kad smo na pola toga stanemo i proglasimo tu permutaciju za $r^{-1}$ (i odatle pronađemo $r$). Sada nam je potrebna samo vrednost $d(p,q)=d(id,p^{-1}q)$ što je samo broj inverzija ove permutacije i lako se može naći u $O(N^2)$ proverom po svim parovima, ili $O(N\log N)$ standardnim načinim preko Fenvikovog stabla.
	## Rešenje kada je $N\leq 3000$
	Tražimo permutaciju $a=p^{-1}r^{-1}$ tako da je $\max\{d(id,a),d(a,p^{-1}q)|\}=\lceil\frac{d(p,q)}{2}\rceil$, iz čega ćemo lako konstruisati šta je $r$. Za ovo je potrebno da izaberete vaš omiljeni algoritam sortiranja koji radi u kvadratnom vremenu i radi tako što samo menja susedne elemente ako su u inverziji (na primer "bubble sort"), krenete da sortirate permutaciju $p^{-1}q$ i stanete na pola. Složenost $O(N^2)$.
	## Glavno rešenje
	Rešenje ćemo naći nalaženje pogodnog kvadratnog algoritma, čije brojanje inverzija možemo da simuliramo brže od kvadratnog. Standardno traženje broja inverzija preko Fenvikovog stabla će nam posle $i$-tog poteza naći broj inverzija u prefiksu dužine $i$. Međutim, ovo je upravo broj inverzija koji je izvršio "insertion sort" kada je završio sa $i$-tim elementom, a ovaj sort je jedan od onih koji menja samo susedne koji su u inverziji. Tako da možemo da radimo računanje broja inverzija permutacije $p^{-1}q$ standardnim algoritmom Fenvikovim stablom, i kad se desi da broj inverzija pređe polovinu svih inverzija, sortiramo taj prefiks, i onda uradimo sa $i$-tim tačno onoliko zamena koliko nam treba da bi distanca bila tačno pola. Složenost $O(N\log N)$.
	
	``` cpp title="04_quaestio_militaris_formationis.cpp" linenums="1"
	#include <bits/stdc++.h>
	using namespace std;
	
	void init(long long* tree, int N){
	    for (int i = 0; i <= N; i++){
	        tree[i] = 0;
	    }
	}
	
	int getSum(long long* tree, int idx){
	    long long sum = 0;
	    while (idx > 0){
	        sum += tree[idx];
	        idx -= idx & (-idx);
	    }
	    return sum;
	}
	
	void update(long long* tree, int N, int idx, int val){
	    while (idx <= N){
	       tree[idx] += val;
	       idx += idx & (-idx);
	    }
	}
	
	vector<int> inverse(vector<int> perm){
	    vector<int> perm_inv(perm.size());
	    for(int i = 0; i < perm.size(); i++){
	        perm_inv[perm[i] - 1] = i + 1;
	    }
	    return perm_inv;
	}
	
	vector<int> compose(vector<int> p, vector<int> q){
	    vector<int> res;
	    for(int i = 0; i < q.size(); i++){
	        res.push_back(p[q[i] - 1]);
	    }
	    return res;
	}
	
	long long count_inversions(vector<int> p){
	    long long *tree = new long long[p.size() + 1];
	    init(tree, p.size());
	    long long invcnt = 0;
	    for (int i = p.size() - 1; i >= 0; i--){
	        invcnt += getSum(tree, p[i] - 1);
	        update(tree, p.size(), p[i], 1);
	    }
	    delete[] tree;
	    return invcnt;
	}
	
	
	void Formacija(int N, int* P, int* Q, int* R, long long& Slabost){
	    vector<int> p, q, r;
	    for (int i = 1; i <= N; i++){
	        p.push_back(P[i]);
	        q.push_back(Q[i]);
	    }
	
	    vector<int> pinv = inverse(p);
	    vector<int> pinv_q = compose(pinv, q);
	    long long pinv_q_inversions = count_inversions(pinv_q);
	
	    long long inv_cnt = 0;
	    int i;
	    long long *tree = new long long[N + 1];
	    init(tree, N);
	    for(i = 0; i < N; i++){
	        int cur_inv_cnt = i - getSum(tree, pinv_q[i]);
	        if(inv_cnt + cur_inv_cnt >= pinv_q_inversions/2){
	            break;
	        }
	        inv_cnt += cur_inv_cnt;
	        update(tree, N, pinv_q[i], 1);
	    }
	    delete[] tree;
	
	    vector<int> pinv_rinv;
	    pinv_rinv = pinv_q;
	    sort(pinv_rinv.begin(), pinv_rinv.begin() + i);
	    int operations_remaining = pinv_q_inversions/2 - inv_cnt;
	    for(int j = i; j > i - operations_remaining; j--){
	        swap(pinv_rinv[j], pinv_rinv[j - 1]);
	    }
	
	    vector<int> rinv = compose(p, pinv_rinv);
	    r = inverse(rinv);
	
	    for (int i = 0; i < N; i++){
	        R[i+1] = r[i];
	    }
	    Slabost = (pinv_q_inversions + 1)/2;
	}

	```
