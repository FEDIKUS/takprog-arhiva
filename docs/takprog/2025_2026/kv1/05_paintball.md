---
hide:
  - toc
---

# 5 - Pejntbol

=== "Zadatak"
	
	| Vremensko ograničenje | Memorijsko ograničenje |
	|:-:|:-:|
	| 1000ms | 64MB |
	
	<br>
	
	Komisija je odlučila da ode na dugo zasluženi tim bilding - pejntbol. 
	
	<br>
	
	Ipak, u jezgru ove premorene organizacije došlo je do određenih neslaganja između setera i testera zadataka. Naime, pojedini testeri i seteri bi voleli da budu u različitim timovima kako bi konačno razjasnili nesuglasice oko zadataka iz prošle sezone.
	
	<br>
	
	Ukupno imamo $N$ članova Komisije. Dato je $M$ takvih parova članova Komisije. Moguće je da je isti član Komisije za neke zadatke bio seter, za neke druge tester. Nije moguće da je isti član Komisije i seter i tester za isti zadatak.
	
	<br>
	
	Potrebno je odrediti da li je moguće podeliti Komisiju u dva tima, tako da se bar $\lfloor M/2\rfloor$ želja ispuni?
	
	<br>
	
	Ukoliko jeste, ispisati takvu podelu. U suprotnom ispisati $-1$.
	
	<br>
	
	## Opis ulaza
	
	<br>
	
	U prvoj liniji standardnog ulaza data su dva prirodna broj $N$ i $M$, broj članova Komisije i broj njihovih želja.
	
	<br>
	
	U narednih $M$ linija standardnog ulaza, nalaze se po dva prirodna broja - $A_i$ i $B_i$ (za $i = 1,2,\ldots,M$). Oni predstavljaju dva člana Komisije koji bi želeli da budu u različitim timovima. 
	
	<br>
	
	## Opis izlaza
	
	<br>
	
	Ukoliko je moguće podeliti Komisiju u dva tima, tako da se ispuni barem $\lfloor  M/2 \rfloor$ njihovih želja, u prvom redu standardnog izlaza ispisati dva prirodna broja $P$ i $D$ - veličine ova dva tima.
	
	U drugom redu standardnog izlaza ispisati $P$ prirodnih brojeva - članove Komisije koji pripadaju prvom timu.
	
	U trećem redu standardnog izlaza ispisati $D$ prirodnih brojeva - članove Komisije koji pripadaju drugom timu.
	
	Ukoliko takva podela ne postoji, ispisati $-1$.
	
	<br>
	
	
	## Primer 1
	
	<br>
	
	### Ulaz
	
	<br>
	
	```
	4 7
	1 2
	1 3
	1 4
	2 3
	2 4
	3 4
	4 3
	```
	
	<br>
	
	### Izlaz
	
	<br>
	
	```
	2 2
	1 2
	3 4
	```
	
	<br>
	
	### Primer 2
	
	<br>
	
	#### Ulaz
	
	<br>
	
	```
	4 1
	1 4
	```
	
	<br>
	
	#### Izlaz
	
	<br>
	
	```
	1 3
	1
	2 3 4
	```
	
	<br>
	
	## Ograničenja
	
	<br>
	
	 - $1 \leq N \leq 1.000$.
	 - $0 \leq M \leq \frac{N(N-1)}{2}$
	 - $1 \leq A_i, B_i \leq N$ i $A_i \neq B_i$ za $i = 1,2,\ldots,M$
	
	<br>
	
	
	U testovima vrednim $50$ poena: važi $n \leq 100$.
	
	<br>
	
=== "Rešenje"
	
	| Autor | Tekst i test primeri | Analiza rešenja | Testiranje |
	|:-:|:-:|:-:|:-:|
	| Marko Milenković | Marko Milenković | Marko Milenković | Vasilije Novaković |
	
	## Potpuno Rešenje 
	
	Modelovaćemo rešenje u terminima teorije grafova. Članovi Komisije su čvorovi, a veze između setera i testera usmerene grane. Cilj je podeliti čvorove u dva tima, tj. dve particije, tako da barem $\lfloor M/2\rfloor$ grana postoji između particija.
	
	Raspodelimo čvorove (članove Komisije) u dve particije (dva tima) proizvoljno. Ukoliko postoji čvor koji ima više suseda u svojoj particiji, nego u drugoj, prebacimo ga u drugu. Ovaj proces ponavljamo sve dok postoje takvi čvorovi.
	
	### Zašto se procedura završava?
	
	Svako prebacivanje čvora iz jedne u drugu particiju povećava broj grana između particija. Najviše je moguće $M$ ovakvih grana, pa će procedura u nekom trenutku morati da se završi.
	
	### Zašto je algoritam tačan?
	
	Kada se procedura završi to znači da svaki čvor $v$ ima barem $deg(v)$ suseda u drugoj particiji, gde je $deg(v)$ ukupan broj suseda koje taj čvor ima. Na osnovu Leme o rukovanju, znamo da je suma svih stepena (broj suseda) čvorova jednak dvostrukom broju grana. Odavde sledi da smo ispunili barem $M/2$ želja. 
	
	``` cpp title="05_paintball.cpp" linenums="1"
	#include <iostream>
	#include <cstdio>
	using namespace std;
	
	const long MaxN = 1001;
	
	long n, m;
	
	long susedCnt[MaxN];
	long sused[MaxN][MaxN]; // broj cvorova je mali pa mozemo i ovako da pamtimo listu suseda
	
	bool grupa[MaxN];    // da li pripada prvoj grupi?
	long grupaCnt[MaxN]; // koliko cvor gadja unutar svoje grupe
	bool dobar[MaxN]; // da li je cvor u listi dobrih ili losih cvorova
	
	// lista suseda zadovoljenih i nezadovoljenih cvorova
	long nxt[MaxN];
	long prv[MaxN];
	
	// pocetak liste
	int goodStart, badStart;
	
	
	char fileIn[] = "mika.in";
	char fileOut[] = "mika.out";
	
	
	void ubaci(int &list, int k)
	{
	    if (list == -1)
	    {
	        // prazna lista
	        list = k;
	        prv[k] = -1;
	        nxt[k] = -1;
	    }
	    else
	    {
	        // na pocetak
	        prv[list] = k;
	        nxt[k] = list;
	        prv[k] = -1;
	        list = k;
	    }
	}
	
	void izbaci(int &list, int k)
	{
	    if (list == k)
	    {
	        list = nxt[list];
	        if (list != -1)
	            prv[list] = -1;
	    }
	    else
	    {
	        nxt[prv[k]] = nxt[k];
	        if (nxt[k] != -1)
	            prv[nxt[k]] = prv[k];
	    }
	}
	
	
	// dodaje nov cvor u odgovarajucu listu
	void novCvor(int k)
	{
	    if (grupaCnt[k] > susedCnt[k] / 2)
	    {
	        // los cvor
	        dobar[k] = false;
	        ubaci(badStart, k);
	    }
	    else
	    {
	        // dobar cvor
	        dobar[k] = true;
	        ubaci(goodStart, k);
	    }
	}
	
	
	void transfer()
	{
	    int v = badStart;
	
	    // posle prebacivanja, cvor postaje dobar
	    dobar[v] = true;
	    izbaci(badStart, v);
	    ubaci(goodStart, v);
	
	
	    for (int i = 0; i < susedCnt[v]; i++)
	    {
	        int w = sused[v][i];
	        if (grupa[w] == grupa[v])
	        {
	            // bili ista grupa, vise nisu
	            grupaCnt[w]--;
	            grupaCnt[v]--;
	
	            // mozda je postao dobar
	            if (!dobar[w] && (grupaCnt[w] <= susedCnt[w] / 2))
	            {
	                // izbacujemo ga iz liste losih, i guramo u listu dobrih
	                dobar[w] = true;
	                izbaci(badStart, w);
	                ubaci(goodStart, w);
	            }
	        }
	        else
	        {
	            // postali su ista grupa
	            grupaCnt[w]++;
	            grupaCnt[v]++;
	
	            // mozda je cvor w postao los
	            if (dobar[w] && (grupaCnt[w] > susedCnt[w] / 2))
	            {
	                // izbacujemo ga iz liste dobrih, i guramo u listu losih
	                dobar[w] = false;
	                izbaci(goodStart, w);
	                ubaci(badStart, w);
	            }
	        }
	    }
	
	    // promeni grupu
	    grupa[v] = !grupa[v];
	}
	
	
	int main()
	{   
	    cin >> n >> m;
	
	    for (int i = 0; i < n; i++)
	    {
	        grupaCnt[i] = 0;
	        susedCnt[i] = 0;
	
	        // inicijalna grupa
	        if (i < n/2) grupa[i] = true;
	        else grupa[i] = false;
	    }
	
	    for (long i = 0; i < m; i++)
	    {
	        long a, b;
	        cin >> a >> b;
	        a--; b--;
	
	        sused[a][susedCnt[a]++] = b;
	        sused[b][susedCnt[b]++] = a;
	
	        if (grupa[a] == grupa[b])
	        {
	            grupaCnt[a]++;
	            grupaCnt[b]++;
	        }
	    }
	
	    goodStart = -1;
	    badStart = -1;
	    for (int i = 0; i < n; i++)
	        novCvor(i);
	
	    // prebacujemo iz jedne grupe u drugu, dokle god mozemo
	    while (badStart != -1)
	    {
	        transfer();
	    }
	
	    int grupa1 = 0, grupa2 = 0;
	    for (int i = 0; i < n; i++)
	    {
	        if (grupa[i])
	            grupa1++;
	        else
	            grupa2++;
	    }
	
	    cout << grupa1 << ' ' << grupa2 << '\n';
	
	    for (int i = 0; i < n; i++)
	        if (grupa[i]) cout << (i+1) << ' ';
	    cout << '\n';
	    for (int i = 0; i < n; i++)
	        if (!grupa[i]) cout <<  (i+1) << ' ';
	    cout << '\n';
	
	    return 0;
	}

	```
