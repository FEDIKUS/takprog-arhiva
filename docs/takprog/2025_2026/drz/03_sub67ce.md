---
hide:
  - toc
---

# B3 - Sub67ce

=== "Zadatak"
	
	| Vremensko ograničenje | Memorijsko ograničenje |
	|:-:|:-:|
	| 2000ms | 512MB |
	
	<br>
	
	Deno ima 0 aure. Denu se to ne sviđa.
	
	<br>
	
	Deno je, poslednjih 6-7 sati proveo skrolujući na Instagramu, pa ga je zabolela glava. U međuvremenu je izludeo od 67 mozgotrula (eng.brainrot), i oseća se loše jer nije produktivno proveo poslednjih 6-7 sati, ali to i nije toliko loše, samo ako i ostali ljudi provode svoje vreme na isti način (nije bitno da bude dobar, samo da bude bolji od ostalih). Zato je odlučio da pokuša ceo svet da navuče na 67 mozgotrul (eng. brainrot). 
	
	<br>
	
	Naime, on je zamislio nisku od $N$ karaktera, gde je svaki karakter '6' ili '7'. On ovu nisku planira da podeli sa celim svetom kako bi ih navukao, ali potrebno mu je da bude dovoljno trula. On tvrdi da je "trulost" niske, jednaka broju njenih (ne nužno kontinualnih) podsekvenci dužine 2, za koje važi da je prvi karakter podsekvence '6', a drugi '7'.
	
	Vasa se zabrinuo jer se Deno nije javljao na telefon poslednjih 6-7 sati, pa je došao kod njega u posetu da proveri da li je sve kako treba, ali zatekao je zamišljenu nisku zapisanu na tabli. On je odmah znao o čemu se radi, pa je odlučio da testira Dena tako što mu je zamenio neke karaktere iz niske sa znakom "?", dok Deno nije gledao. Kad se Deno osvrnuo, naljutio se na Vasu, pa je odlučio da ga pita $Q$ upita, gde je $i$-ti upit glasio ovako:
	
	 - ako posmatraš nisku $B = s_{L_i} s_{L_{i} + 1} ... s_{R_i}$, za date brojeve $L_i$ i $R_i$, i za svaki karakter '?' u $B$ odlučiš da li ga menjaš u '6' ili u '7', kolika je maksimalna trulost niske $B$ koju možeš dobiti?
	
	<br>
	
	Dok Vasa proverava da li je Denu dobro, Vama je podario čast odgovaranja na Denova pitanja.
	
	<br>
	
	## Opis ulaza
	
	<br>
	
	U prvoj liniji standardnog ulaza nalaze se dva broja: $N$ i $Q$ - veličina niske, i broj upita.
	
	<br>
	
	U drugoj liniji standardnog ulaza nalazi se $s$ - niska dužine $N$, gde je svaki karakter '6', '7' ili '?'.
	
	<br>
	
	U narednih $Q$ linija standardnog ulaza nalaze se po dva broja: $L_i$ i $R_i$, $(L_i \leq R_i)$ - parametri $i$-tog upita.
	
	<br> 
	
	## Opis izlaza
	
	<br>
	
	Na standardni izlaz ispisati $Q$ linija.
	
	U $i$-toj liniji ispisati jedan broj $x_i$ - odgovor na $i$-ti upit.
	
	<br>
	
	## Primer 
	
	<br>
	
	### Ulaz
	
	<br>
	
	```
	10 7
	67???67?76
	1 5
	2 4
	5 6
	2 10
	1 10
	4 8
	3 9
	```
	
	<br>
	
	### Izlaz
	
	<br>
	
	```
	5
	1
	0
	12
	16
	6
	12
	```
	
	<br>
	
	## Objašnjenje primera
	
	U prvom upitu, posmatramo podnisku "67???"
	
	Od svih kombinacija kojim možemo zameniti upitnike, najvišu trulost nam daje "67677", kod kog imamo $5$ podsekvenci: {{1, 2}, {1, 4}, {1, 5}, {3, 4}, {3, 5}}.
	
	Drugi upit je za podnisku "7??". Možemo zameniti u "766", "767", "776", i "777", gde "767" ima trulost $1$, a sve ostale imaju trulost $0$, pa je odgovor $1$.
	
	Treći upit je za podnisku "?6". Sa kojim god karakterom zamenili upitnik, dobićemo trulost $0$.
	
	
	## Ograničenja
	
	<br>
	
	- $1 \leq N, Q \leq 300.000$
	- $1 \leq L_i \leq R_i \leq N$, za svako $1 \leq i \leq Q$
	
	<br>
	
	Test primeri su odvojeni u $7$ disjunktnih grupa:
	
	- U test primerima vrednim **6** poena: svi karakteri niske su '?'
	- U test primerima vrednim **6** poena: $N, Q \leq 100$
	- U test primerima vrednim **7** poena: $N, Q \leq 500$
	- U test primerima vrednim **7** poena: ni jedan karakter nije '?'
	- U test primerima vrednim **12** poena: $N \leq 1000, Q \leq 10.000$
	- U test primerima vrednim **20** poena: $L_i = 1$  za svako $1 \leq i \leq Q$
	- U test primerima vrednim **42** poena: bez dodatnih ograničenja.
	
	<br>
	
=== "Rešenje"
	
	| Autor | Tekst i test primeri | Analiza rešenja | Testiranje |
	|:-:|:-:|:-:|:-:|
	| Vasilije Novaković | Vasilije Novaković | Vasilije Novaković | Miloš Milutinović |
	
	<br>
	
	Za početak razmislimo kako bi smo za potpuno poznatu nisku (bez upitnika), izračunali trulost na spor način.
	
	Nazovimo podnisku trulom, ako je dužine 2 i prvi karakter je 6 a drugi 7 (trulost niske je broj njenih trulih podniski)
	
	Možemo izbrojati koliko trulih podniski postoji, koje počinju nekim konkretnim karkaterom na poziciji $i$.
	
	Ako važi $s_i = 7$, tad postoji 0 trulih podniski kojima je prvi karkater $i$, a ako je $s_i = 6$, tad je broj trulih podniski koje počinju na toj poziciji, jednak broju pozicija $j, j \gt i, s_j = 7$.
	
	Tada je trulost niske upravo jednaka sumi trulih podniski koje počinju na poziiji $i, 1 \leq i \leq N$. 
	
	Primetimo odavde da nam je samo bitno za svaku šesticu, koliko ima sedmica nakon nje.
	
	<br>
	
	## Podzadatak 1: svi karakteri niske su '?'
	
	<br>
	
	Primetimo da je optimalno da sve upitnike koje zamenimo u 6, stavimo pre svih upitnika koje zamenimo u 7.
	
	Nazovimo poziciju poslednjeg upitnika koji ćemo promeniti u šesticu "granica upitnika".
	
	Dokaz za ovo je jednostavan: ako postoje dva upitnika, koji su zamenjeni za 7 i 6, tako da se sedmica nalazi pre šestice, onda posmatrajući način na koji računamo trulost niske, možemo primetiti da ako zamenimo umesto toga prvi upitnik u 6 a drugi u 7, trulost će se sigurno povećati barem za 1, i nikad se neće smanjiti.
	
	Dakle, za bilo koje dve pozicije na kojima su upitnici, i zamenili smo prvi u 7 i drugi u 6, uvek možemo povećati trulost tako što im zamenimo vrednosti, a kad ne postoje ovakvi parovi, to znači da se sve šestice nalaze pre svih sedmica.
	
	Nakon što je ustanovljeno da ćemo neki prefiks upitnika pretvoriti u 6 a ostale vrednosti u 7, treba uzeti optimalan raspored.
	
	Formalnije, recimo da odgovaramo na upit od $L$ do $R$. Pošto su u ovom podzadatku sve upitnici, to znači da odgovaramo na upit sa $x = R - L + 1$ upitnika. 
	
	Ako zamenimo $A$ upitnika u $6$, a $B$ upitnika u $7$, tada važi $A + B = x$, a trulost je jednaka proizvodu $A \cdot B$
	
	Poprilično je intuitivno, ali se može i dokazati pomoću nejednakosti za aritmetičku i geometrijsku sredinu, da ćemo prvu polovinu zameniti u šestice, a drugu polovinu u sedmice, a ako $x$ nije deljiv sa 2, nije bitno da li ćemo broj u sredini zameniti u 6 ili 7, jer će rezultat biti isti.
	
	Vremenska složenost $O(1)$ po upitu. 
	
	Ukupna vremenska složenost je $O(N+Q)$
	
	Prostorna složenost $O(N)$
	
	<br>
	
	## Podzadatak 2: $N, Q \leq 100$
	
	<br>
	
	U ovom podzadatku možemo iskoristiti obzervaciju iz prethodnog, a to je da ćemo neki prefiks upitnika zameniti sa 6, a ostale upitnike sa 7.
	
	Možemo fiksirati granicu gde će nam šestice prestati, to jest sedmice početi, i za tako dobijenu nisku izračunati trulost na način opisan u početku zadatka.
	
	Sad se svodi na izračunavanje trulosti fiksirane niske (bez upitnika), što ovaj podzadatak dozvoljava u $O(N^2)$, iako je moguće uraditi to značajno brže.
	
	Složenost: $O(N^3 \cdot Q)$
	
	Prostorna složenost $O(N)$
	
	<br>
	
	## Podzadatak 3: $N, Q \leq 500$
	
	<br>
	
	Ovaj podzadatak možemo uraditi isto kao i prethodni, samo što ćemo za fiksnu granicu trulost izračunati brže, u $O(N)$, što dovodi finalnu složenost na $O(N^2 \cdot Q)$.
	
	Prostorna složenost $O(N)$
	
	<br>
	
	## Podzadatak 4: ni jedan karakter nije '?'
	
	<br>
	
	
	<br>
	
	U ovom podzadatku je potrebno brzo odgovarati na upite, ali nam je cela niska već fiksna.
	
	Prvo nađimo način da brzo odgovaramo na upite gde je $L = 1$:
	
	Možemo izračunati niz $prefAns$, gde je $prefAns_i$ jednak odgovoru na upit $L = 1, R = i$.
	
	Ovaj niz možemo lako izračunati u $O(N)$, koristeći ideju iz prethodnog podzadatka.
	
	Sad razmatramo kako da nađemo trulost od $L$ do $R$, koristeći ovaj niz:
	
	Ako uzmemo samo $prefAns_R$, izbrojaćemo više nego što treba, jer će šestice koje se nalaze pre pozicije $L$, da dodaju na trulost.
	
	Svaka šestica koja se nalazi pre pozicije $L$ će dodati na trulost broj sedmica između njene pozicije i pozicije $R$. Ovo se dalje može razložiti na broj sedmica između njene pozicije i $L-1$ + broj sedmica između pozicija $L$ i $R$. Kad posmatramo sve šestice zajedno i grupišemo prvi član to je zapravo $prefAns_{L-1}$, dok je drugi član zapravo proizvod broja šestica od $1$ do $L-1$ i broja sedmica od $L$ do $R$. Broj šestica i sedmica možemo naći koristeći odvojene prefiksne sume, ali konačna formula za odgovor na upit od $L$ do $R$ je:
	
	- $prefAns_R - prefAns_{L-1} - cnt6[1:L-1] \cdot cnt7[L:R]$
	
	Vremenska složenost $O(N + Q)$
	
	Prostorna složenost $O(N)$
	
	<br>
	
	## Podzadatak 5: $N, Q \leq 2000$
	
	<br>
	
	Koristeći ideju iz prethodnog podzadatka, najlakše rešenje za ovaj podzadatak je da fiksiramo granicu gde prestajemo upitnike da pretvaramo u 6, i počinjemo da ih pretvaramo u 7, nezavisno od upita, i da izračunamo one iste nizove za svaku od tih granica, kojih ima najviše $N$.
	
	Nakon što to uradimo, odgovor na upit može da se radi na isti način, tako što fiksiramo granicu i uzmemo maksimalni odgovor po svakoj granici za neki upit, jer odgovor možemo da nađemo u $O(1)$.
	
	Vremenska složenost $O(N \cdot (N + Q))$.
	
	Prostorna složenost $O(N^2)$
	
	<br>
	
	## Podzadatak 6: $L_i = 1$
	
	<br>
	
	U ovom podzadatku se svaki upit radi na prefiksu niske.
	
	Možemo sortirati upite po $R$ i odgovarati na njih offline. 
	
	Primetimo da kako desna granica upita raste, naša granica gde prestajemo da stavljamo šestice nikako ne može da se smanji, može samo da se povećava ili da ostane ista.
	
	<br>
	
	Dokaz: zamislimo da se desna granica povećava jedan po jedan karakter, a da je trenutna granica na kojoj prestajemo da stavljamo 6 i krećemo da stavljamo 7 jednaka $x$. Ako nam se sad desna granica upita poveća sa jedan, to znači da je novi karakter koji smo dobili ili 6 ili 7 ili ?. Ako je karakter 6, on ne može da utiče na odgovor jer je poslednji, pa ne postoji ni jedna sedmica posle njega. Dakle dovoljno je rešiti slučaj gde je 7, jer ako je upitnik sigurno ćemo ga zameniti za 7.
	
	<br>
	
	Ako je poslednji karakter 7, to znači da će doprinos šestica koje su levo da se poveća, što znači da sigurno nije optimalno smanjiti broj šestica sad, jer bi u suprotnom bilo optimalno i za prethodnu granicu.
	
	Ovo nam može dati intuiciju kako će se trulost ponašati kad pomeramo granicu upitnika. 
	
	Može se dokazati da će pomeranjem granice upitnika desno, trulost prvo **strogo** da raste, pa da dostigne maksimum, i više granica može da daje maksimalnu trulost (što se može videti na primeru ???), ali će one biti jedna do druge, i nakon maksimuma će **strogo** da opada.
	
	<br>
	
	Dokaz je sledeći:
	
	Posmatrajmo kako se trulost menja kad granicu pomerimo sa $i-1$-og na $i$-ti upitnik (pretvorimo $i$-ti upitnik u 6 umesto u 7).
	
	Trulost će se smanjiti za broj šestica pre tog upitnika (upitnike pre tog smatramo za šestice takođe), ali povećati za broj sedmica nakon njega (upitnike nakon smatramo za sedmice).
	
	Kako pomeramo granicu na desno, broj šestica levo će da raste bar za 1, a broj sedmica će se smanjiti bar za 1 (jer smo baš taj konkretan upitnik upravo pretvorili sa 7 u 6, pa kad se pomerimo još na desno sigurno će se povećati broj šestica za barem 1, isto tako kad se prebacimo na sledeći upitnik, on je pre prebacivanja bio 7, a sad posmatramo sve desno od njega, pa nam se broj sedmica smanjio bar za 1).
	
	Ovo znači da će faktor koji se oduzima da raste, dok će faktor koji se dodaje da se smanjuje, i jedini slučaj kad trulost ostaje ista, je kad su ta dva faktora jednaka (što ne mora da se desi), što je sigurno maksimum jer je pre toga faktor koji se oduzima sigurno bio manji od faktora koji povećava, a nakon toga je faktor koji se oduzima sigurno veći pa će trulost da nastavi strogo da opada.
	
	<br>
	
	Znajući ovo, kako nam se desna granica upita pomera u desno, možemo da pomeramo našu granicu upitnika sve dok trulost raste.
	
	Kako bi brzo izračunali trulost za određenu granicu, treba imati dodatno izračunato i:
	
	- ukupan broj sedmica nakon svakog upitnika koji se nalazi u prvih $i$ pozicija: $prefq7[i]$
	- ukupan broj šestica koji se nalazi pre svakog upitnika, u poslednjih $i$ pozicija: $sufq6[i]$
	
	Nakon toga je moguće za neku granicu $x$ izračunati trulost tako što je podelimo zbir sledećih delova:
	
	- Koliko svaka šestica ima sedmica nakon sebe (računamo isto kao u četvrtom podzadatku)
	
	- Proizvod broja upitnika koje pretvaramo u šestica i broja upitnika koje pretvaramo u sedmice.
	
	- Koliko ukupno ima sedmica nakon svih upitnika koje pretvaramo u šestice.
	
	- Koliko ukupno ima šestica pre svih upitnika koje pretvaramo u sedmice.
	
	Svaki od ovih brojeva je moguće izračunati u $O(1)$ za neku datu granicu, nakon što smo prethodno pomenute nizove izračunali pre svih upita.
	
	Vremenska složenost: $O(N + Q \cdot log(Q))$
	
	Prostorna složenost: $O(N + Q)$
	
	<br>
	
	## Rešenje bez dodatnih ograničenja
	
	
	<br>
	
	Koristeći konkavnost funkcije trulosti u zavisnosti od granice upitnika, možemo doći na ideju da radimo za svaki upit binarnu pretragu po granici upitinika.
	
	Izračunaćemo trulost za dve susedne granice upitnika:
	
	- Ako je trulost jednaka za obe granice, to znači da nam ta granica daje maksimalnu trulost
	- Ako je trulost veća za drugu granicu, to znači da trulost još raste nakon ispitane granice, pa možemo otići u desnu polovinu pretrage.
	- Ako je trulost manja za drugu granicu, to znači da će samo još više da opada nakon ispitane granice, pa treba otići u levu polovinu pretrage.
	
	Za način računanja trulosti u zavisnosti od granice, pogledati prethodni podzadatak.
	
	Vremenska složenost: $O(N + Q \cdot log(N))$.
	
	Prostorna složenost: $O(N)$.
	
	<br>
	
	
	
	
	
	
	``` cpp title="03_sub67ce.cpp" linenums="1"
	#include <iostream>
	#include <vector>
	#include <algorithm>
	
	using namespace std;
	
	const int N = 300003;
	long long prefAns[N], prefq7[N], sufq6[N],cnt6[N], cnt7[N], cntq[N];
	vector<int> qs;
	
	void solve(){
		int n, q;
		cin >> n >> q;
		string s;
		cin >> s;
	   s = "$" + s;
	   for(int i = 1; i<=n; i++){
	        if(s[i] == '?')qs.push_back(i);
	   }
	   for(int i = 1; i<=n; i++){
	   	cnt6[i] = cnt6[i-1] + (s[i] == '6');
	   	cnt7[i] = cnt7[i-1] + (s[i] == '7');
	   	cntq[i] = cntq[i-1] + (s[i] == '?');
	   	prefAns[i] = prefAns[i-1] + (s[i] == '7'? cnt6[i]:0);
	   }
	   for(int i = 1; i<=n; i++){
	   	prefq7[i] = prefq7[i-1] + (s[i] == '?'? cnt7[n]-cnt7[i] : 0);
	   }
	   for(int i = n; i>=1; i--){
	   	sufq6[i] = sufq6[i+1] + (s[i] == '?'? cnt6[i] : 0);
	   }
		while(q--){
			int l, r;
			cin >> l >> r;
			long long add = prefAns[r] - prefAns[l-1] - cnt6[l-1] * (cnt7[r] - cnt7[l-1]);
			if(cntq[r] - cntq[l-1] == 0){
				cout << add << '\n';
				continue;
			}
			if(cntq[r] - cntq[l-1] == 1){
				int indx = *lower_bound(qs.begin(), qs.end(), l);
				cout << add + max(cnt6[indx] - cnt6[l-1], cnt7[r] - cnt7[indx]) << '\n';
				continue;
			}
	      long long ans = prefq7[r] - prefq7[l-1] - (cntq[r] - cntq[l-1]) * (cnt7[n] - cnt7[r]);
	      int L = lower_bound(qs.begin(), qs.end(), l) - qs.begin();
	      int R = (upper_bound(qs.begin(), qs.end(), r) - qs.begin()) - 1;
	      /*
	      for(int mid = L; mid <= R; mid++){
	      	long long ans = 0;
	      	ans1 += prefq7[granica1 - 1] - prefq7[l-1];
	      	ans1 += sufq6[granica1] - sufq6[r+1];
	      	ans1 += (cntq[granica1 - 1] - cntq[l - 1]) * (cntq[r] - cntq[granica1 - 1]);
	
	      }
	      */
	      
	      while(L<=R){
	      	int mid = L+R >> 1;
	      	int granica1 = qs[mid], granica2 = qs[mid+1];
	      	long long ans1 = 0, ans2 = 0;
	      	ans1 += prefq7[granica1 - 1] - prefq7[l-1];
	      	ans1 += sufq6[granica1] - sufq6[r+1];
	      	ans2 += prefq7[granica2 - 1] - prefq7[l-1];
	      	ans2 += sufq6[granica2] - sufq6[r+1];
	      	//? - ?
	      	ans1 += (cntq[granica1 - 1] - cntq[l - 1]) * (cntq[r] - cntq[granica1 - 1]);
	      	ans2 += (cntq[granica2 - 1] - cntq[l - 1]) * (cntq[r] - cntq[granica2 - 1]);
	      	//? -> 6
	      	ans1 -= (cntq[granica1 - 1] - cntq[l - 1]) * (cnt7[n] - cnt7[r]);
	      	ans2 -= (cntq[granica2 - 1] - cntq[l - 1]) * (cnt7[n] - cnt7[r]);
	      	//? -? 7
	      	ans1 -= (cntq[r] - cntq[granica1 - 1]) * cnt6[l-1];
	      	ans2 -= (cntq[r] - cntq[granica2 - 1]) * cnt6[l-1];
	      	if(ans1 == ans2){
	      		ans = max(ans, ans1);
	      		break;
	      	}
	      	else if(ans1 > ans2){
	      		ans = max(ans, ans1);
	      		R = mid-1;
	      	}
	      	else{
	      		ans = max(ans, ans2);
	      		L = mid + 1;
	      	}
	      }
	      cout << ans + add << '\n';
		}
		
	}
	
	int main(){
	  ios_base::sync_with_stdio(0);
	  cin.tie(0);
	  solve();
	  return 0;
	}

	```
