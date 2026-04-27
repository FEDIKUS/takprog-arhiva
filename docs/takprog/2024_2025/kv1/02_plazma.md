---
hide:
  - toc
---

# 2 - Plazma

=== "Zadatak"
	
	| Vremensko ograničenje | Memorijsko ograničenje |
	|:-:|:-:|
	| 1000ms | 256MB |
	
	<br>
	
	Zbog nedavne nestašice Plazma keksa, brižni otac se svakog dana trudio da obraduje svoju ćerku. Ona je svako popodne, kada ga je bilo na raspolaganju, pojela jedno pakovanje keksa, dok je on svako jutro posećivao prodavnicu i kupovao sva pakovanja Plazme koja je pronašao.
	
	<br>
	
	Poznato je da je otac $N$ puta (u različitim danima) pronašao Plazmu u prodavnici, da je $i$-ti put bio $d_i$-tog dana i da je tada kupio $p_i$ pakovanja Plazme. Njegova pronalaženja Plazme su sortirana u rastućem poretku po $d_i$.
	
	<br>
	
	Otac je primetio da je posle jednog dana ćerka prestala da jede Plazmu (dok je tog i svakog prethodnog dana kada joj je Plazma bila dostupna jela po jedno pakovanje), ali nije siguran kada je to bilo. To se možda desilo i pre poslednje kupovine Plazme.
	
	<br>
	
	Pomozite ocu tako što ćete mu odgovoriti na $Q$ pitanja sledećeg oblika: ”Koliko bi pakovanja keksa ćerka pojela da je prestala da ga jede posle $k_j$-tog dana?”, pri čemu su pitanja sortirana u rastućem poretku po $k_j$.
	
	<br>
	
	## Opis ulaza
	
	<br>
	
	U prvom redu standardnog ulaza se nalaze dva broja $N$, koji predstavlja broj puta koliko je otac pronašao Plazmu, i $Q$, koji predstavlja broj pitanja. U $i$-tom od narednih $N$ redova se nalaze po dva broja $d_i$ i $p_i$ koji označavaju kog dana je $i$-ti put otac pronašao Plazmu i koliko je pakovanja tada kupio, redom. U $j$-tom od narednih $Q$ redova ulaza se nalazi po jedan broj $k_j$, koji predstavlja dan posle kog ćerka prestaje da jede Plazmu u $j$-tom pitanju.
	
	<br>
	
	## Opis izlaza
	
	<br>
	
	U $j$-tom od $Q$ redova standardnog izlaza ispisati po jedan broj, odgovor na $j$-to pitanje.
	
	<br>
	
	## Primer 1
	
	<br>
	
	### Ulaz
	
	<br>
	
	```
	2 1
	1 2
	5 10
	7
	```
	
	<br>
	
	### Izlaz
	
	<br>
	
	```
	5
	```
	
	<br>
	
	### Objašnjenje
	
	<br>
	
	Ćerka će pojesti po pakovanje Plazme u prvom, drugom, petom, šestom i sedmom danu.
	
	<br>
	
	## Primer 2
	
	<br>
	
	### Ulaz
	
	<br>
	
	```
	4 4
	5 7
	14 1000000000 
	15 1000000000 
	16 1000000000 
	3
	8
	11
	1000000000000000000
	```
	
	<br>
	
	### Izlaz
	
	<br>
	
	```
	0
	4
	7
	3000000007
	```
	
	<br>
	
	### Objašnjenje
	
	<br>
	
	* U prvom pitanju neće pojesti nijedno pakovanje keksa.
	
	* U drugom pitanju će pojesti po pakovanje keksa u petom, šestom, sedmom i osmom danu.
	
	* U trećem pitanju će pojesti po pakovanje keksa u svakom danu od petog do jedanaestog.
	
	* U četvrtom pitanju će pojesti po pakovanje keksa u svakom danu od petog do jedanaestog, kao i u svakom danu od četrnaestog do 3000000013.
	
	<br>
	
	## Ograničenja
	
	<br>
	
	* $1 \leq N,Q \leq 300,000$
	
	* $1 \leq p_i \leq 10^{9}$ za svako $i$
	
	* $1 \leq d_1< d_2<\dots< d_N\leq 10^{18}$
	
	* $1 \leq k_1< k_2<\dots< k_Q\leq 10^{18}$
	
	<br>
	
	Test primeri su podeljeni u pet disjunktnih grupa:
	
	* U testovima vrednim 10 poena: $N=3$ i $Q=1$.
	
	* U testovima vrednim 20 poena: $d_N\leq 300\,000$, $k_N\leq 300\,000$ i $Q=1$.
	
	* U testovima vrednim 20 poena: $d_N\leq 300\,000$ i $k_N\leq 300\,000$.
	
	* U testovima vrednim 20 poena: $Q=1$.
	
	* U testovima vrednim 30 poena: bez dodatnih ograničenja.
	
	<br>
	
=== "Rešenje"
	
	| Autor | Tekst i test primeri | Analiza rešenja | Testiranje |
	|:-:|:-:|:-:|:-:|
	| Vladimir Milovanović | Filip Bojković | Vladimir Milovanović | Vladimir Milovanović |
	
	### Analiza rešenja
	
	Najpre je zgodno razmotriti rešenje za jedno pitanje, odnosno za slučaj kada je $Q=1$. Neophodno je obrađivati dostave u vremenskom redosledu kako su i date, vodeći računa kada je bila poslednja dostava, broj pakovanja Plazma keksa koji je trenutno na raspolaganju, kao i ukupan broj pakovanja koji je kupljen (do tog trenutka). Kada se obrađuje nova dostava Plazme, ažurira se ukupan broj pakovanja, ali i broj pakovanja koji je na raspolaganju kako bi se uračunalo i to koliko je kutija pojedeno od poslednje kupovine, kao i nove kutije u poslednjoj kupovini. Odgovor je zapravo samo razlika između broja pakovanja Plazme koje su dostavljene i broja pakovanja koja su preostala na kraju. Kako su dostave već sortirane po vremenu, obrada jedne dostave uzima $\mathcal{O}(1)$, odnosno $\mathcal{O}(N)$ ukupno za svih $N$ dostava.
	
	Ukoliko bismo naivno posmatrali, sada je za svako od $Q$ pitanja moguće proći kroz svih $N$ dostava i dati odgovor na odgovarajući upit, ali je složenost ovakvog pristupa preskupa i iznosi $\mathcal{O}(QN)$, što je bilo dovoljno za polovinu poena na ovom zadatku. Problem je moguće rešiti i efikasnije tako što se predobradom najpre sačuvaju neophodni podaci za odgovor na svaki upit, što uzima $\mathcal{O}(N)$, a zatim binarnom pretragom po $N$ za svako pitanje odgovori na isto što će biti složenosti $\mathcal{O}(Q\log{N})$, za ukupnu složenost ovog algoritma od $\mathcal{O}(N+Q\log{N})$ što se i tražilo za maksimalan broj poena.
	
	Koristeći se tehnikom dva pokazivača, zadatak je moguće rešiti i u složenosti $\mathcal{O}(N+Q)$, iako se to nije zahtevalo za maksimalan broj poena. Ključno za ovo rešenje jeste unutar jedne petlje iterirati istovremeno i kroz dostave i kroz pitanja i vršiti odgovarajuće obrade. Pored bolje vremenske složenosti, memorijska složenost ovog algoritma je takođe niža od prethodno opisane binarne pretrage.
	
	``` cpp title="02_plazma.cpp" linenums="1"
	#include<bits/stdc++.h>
	
	using namespace std;
	using ll = long long;
	
	const int maxn=3e5+5;
	
	ll d[maxn],p[maxn],k[maxn];
	
	/*
	  dva pokazivaca O(n+q)
	  100p
	*/
	
	int main(){
	  int n,q;
	  cin>>n>>q;
	  for(int i=0;i<n;i++){
	    cin>>d[i]>>p[i];
	  }
	  for(int i=0;i<q;i++){
	    cin>>k[i];
	  }
	  ll tren = 0;
	  ll ukupno = 0;
	  ll gde = 0;
	  ll prosli = 1;
	  for(int i=0;i<q;i++){
	    while(gde<n && d[gde]<=k[i]){
	      ukupno += min(tren,d[gde]-prosli);
	      tren -= min(tren,d[gde]-prosli);
	      prosli = d[gde];
	      tren += p[gde];
	      gde++;
	    }
	
	    cout<<ukupno+min(tren,k[i]+1-prosli)<<endl;
	  }
	  return 0;
	}

	```
