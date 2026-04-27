---
hide:
  - toc
---

# 4 - Prijateljski trkači

=== "Zadatak"
	
	| Vremensko ograničenje | Memorijsko ograničenje |
	|:-:|:-:|
	| 1000ms | 256MB |
	
	<br> Nakon što je komisija odlučila da kvalifikacije 2025. godine traju mnogo duže nego inače, takmičarima je, nakon mnogo zadataka, postalo dosadno. Kako bi komisija motivisala takmičare da se vrate nazad na zadatke, odlučila je da napravi trku, čiji je cilj da takmičari odmore svoje moždane vijuge. Naravno, komisija mora da komplikuje sve što radi, pa je odlučila da ova trka ne bude obična. Trka se odvija na teritoriji Srbije, koju naravno, zamišljamo kao beskonačnu ravan (ne brinite, takmičari neće trčati beskonačno dugo).
	Dato je n početnih tačaka, i iz svake tačke istovremeno, kreće da trči 4 takmičara, po jedan u svakom smeru: severno, južno, istočno i zapadno. Svi takmičari trče istom brzinom, svake sekunde, takmičar koji se nalazio na poziciji (x,y), preći će na poziciju:
	
	* (x+1,y) ako se kreće severno, 
	
	* (x-1,y) ako se kreće južno,
	
	* (x,y+1) ako se kreće istočno,
	
	* (x,y-1) ako se kreće zapadno.
	
	Ako se više takmičara, u istom vremenskom trenutku, nađe na istoj poziciji, oni će se pozdraviti, svaki sa svakim, i nastaviće da trče. Međutim, pošto su im moždane vijuge premorene, i pošto su programeri, oni ne vole da provode mnogo vremena sa drugim ljudima, pa će nakon pozdrava nastaviti da trče svojim putem, a sam pozdrav može se smatrati kao da traje 0 sekundi.
	
	Takođe, pošto programeri vole samo cele brojeve, oni će se pozdraviti sa drugim programerima samo ako se nađu u isto vreme, na istoj poziciji, koja ima celobrojne koordinate.
	
	Pošto je komisija veoma dobro upoznata sa problemom umornih moždanih vijuga, oni znaju da je socijalna interakcija ključna za njihovo odmaranje, pa ih zanima, koliko ukupno pozdrava će se desiti tokom trajanja ove trke.
	
	
	
	## Opis ulaza
	
	U prvoj liniji standardnog ulaza unosi se ceo broj $N$, broj tačaka. U narednih $N$ linija nalaze se koordinate tačaka $(x_i, y_i)$.
	
	
	## Opis izlaza
	
	Potrebno je ispisati jedan broj - koliki je ukupan broj pozdrava koji će se desiti tokom trke.
	
	
	## Primer 1
	
	
	### Ulaz
	```
	2
	1 1
	2 2
	```
	###
	
	### Izlaz
	```
	2
	```
	
	
	### Objašnjenje
	Iz tačaka $(1,1)$ i $(2,2)$ istovremeno kreću po $4$ takmičara u sva četiri smera. Nakon jedne sekunde, takmičar iz $(1,1)$, koji se kretao severno, će naići na takmičara iz $(2,2)$ koji se kretao zapadno, u tački $(2,1)$. Takođe, u tački $(1,2)$ će se naći takmičar iz $(1,1)$, koji se kreće istočno, i takmičar iz $(2,2)$ koji se kreće južno. Nakon ova dva susreta može se dokazati da se ni jedna dva takmičara više neće susreti na istoj poziciji celobrojnih koordinata, u isto vreme.
	
	
	
	## Ograničenja
	
	- $2 \leq N \leq 200.000$
	
	- $-10^{9} \leq x_i, y_i \leq 10^{9}$
	
	- Za svaki test primer se garantuje da će se sve tačke međusobno razlikovati.
	
	
	## Podzadaci
	
	Podzadaci su podeljeni u $5$ disjunktnih grupa:
	
	- U test primerima vrednim $10$ poena: $N \le 2$.
	
	- U test primerima vrednim $20$ poena: $N \le 1.000$.
	
	- U test primerima vrednim $20$ poena: svi $y_i$ su jednaki.
	
	- U test primerima vrednim $20$ poena: $-1.000 \le x_i, y_i \le 1.000$.
	
	- U test primerima vrednim $30$ poena: bez dodatnih ograničenja.
	
	
	
	
	
=== "Rešenje"
	
	| Autor | Tekst i test primeri | Analiza rešenja | Testiranje |
	|:-:|:-:|:-:|:-:|
	| Nikola Milosavljević | Vasilije Novaković | Filip Bojković | Dragan Urošević |
	
	Svaka dva trkača će se najviše jednom sresti. Hajde da proverimo sve međusobne početne položaje takmičara i da li će se pozdraviti: 
	1. ista $x$ koordinata: kako bi se susreli moraju biti usmereni jedan ka drugome i udaljeni paran broj pozicija
	2. nije 1. i ista $y$ koordinata: simetrično slučaju 1.
	3. nije 1. ni 2. i prvi se kreće na gore: jedino može da se sretne sa nekim koji se kreće u levo ili desno i to ako se nalaze na istoj $y=x+n$ dijagonali za neko $n\in\mathbb{Z}$ ili na istoj $y=-x+n$ dijagonali zavisno od smera kretanja
	3. nije 1. ni 2. ni 3. i prvi se kreće na dole: simetrično slučaju 3.
	
	## N = 2
	
	Proverimo za svaka dva trkača uslove odozgo i izbrojimo broj susreta.
	
	## N $\leq$ 1000
	
	Proverimo za svaka dva trkača uslove odozgo i izbrojimo broj susreta. Vremenska složenost je $\mathcal{O}\left(N^2\right)$
	
	## Svi $y_i$ su jednaki
	
	Kako je svima $y$ koordinata ista, pozdraviće se oni parovi koji su udaljeni za paran broj pozicija (po $x$ koordinati). To su samo oni parovi kojima je $x$ koordinata parna i oni parovi kojima je $x$ koordinata neparna. Rešenje je dato formulom ${\text{broj parnih x}\choose{2}}\cdot{\text{broj neparnih x}\choose{2}}$ (${a}\choose{b}$ predstavlja [binomni koeficijent](https://sr.wikipedia.org/sr-ec/%D0%91%D0%B8%D0%BD%D0%BE%D0%BC%D0%BD%D0%B8_%D0%BA%D0%BE%D0%B5%D1%84%D0%B8%D1%86%D0%B8%D1%98%D0%B5%D0%BD%D1%82), odnosno za $b=2$ je samo $\frac{a\cdot\left(a-1\right)}{2}$) i vremenska složenost je $\mathcal{O}\left(N\right)$ jer samo treba da izbrojimo broj parnih i broj neparnih $x$ koordinata.
	
	## $\left|x_i\right|,\left|y_i\right|\leq 1000$
	
	Ovaj podzadatak služi za neefikasnu implementaciju glavnog rešenja (bez korišćenja mapa na primer)
	
	## Glavno rešenje
	
	Ovo rešenje predstavlja efikasnu implementaciju prethodnih ideja.
	
	Za parove tačaka sa istom $x$ ili $y$ koordinatom već znamo šta da radimo. Samo je potrebno da brojimo pojavljivanja isključivo za one $x$ ili $y$ koordinate na kojima se nalaze neke tačke i to možemo uraditi korišćenjem mape u C++.
	
	Potrebno je takođe izbrojati za sve dijagonale na kojima se nalazi neka tačka koliko se tačaka nalazi na njoj. Možemo primetiti da je svaka dijagonala oblika $y=x+n$ jedinstveno određena brojem $y-x$ koji je isti za sve tačke na njoj, dok je svaka dijagonala oblika $y=-x+n$ jedinstveno određena brojem $y+x$ koji je isti za sve tačke na njoj. Ove brojeve možemo koristiti kao ključeve za mapu i lako brojati koliko ima tačaka na kojoj dijagonali. Za pojedinačnu dijagonalu rešenje je $2\cdot {\text{broj tačaka}\choose{2}}$ jer se za svaki par tačaka pozdravljaju dva para takmičara (ispod i iznad dijagonale).
	
	```c++
	int n; cin>>n;
	map<int,int> xparno,xneparno,yparno,yneparno,dijagonalaplus,dijagonalaminus;
	for(int i=0;i<n;i++){
	  int x,y; cin>>x>>y;
	
	  dijagonalaplus[x+y]++;
	  dijagonalaminus[x-y]++;
	
	  if(y&1) xneparno[x]++;
	  else xparno[x]++;
	
	  if(x&1) yneparno[y]++;
	  else yparno[y]++;
	}
	
	long long resenje=0;
	for(auto [_,cnt]:dijagonalaplus) resenje+=(long long)cnt*(cnt-1);
	for(auto [_,cnt]:dijagonalaminus) resenje+=(long long)cnt*(cnt-1);
	for(auto [_,cnt]:xparno) resenje+=(long long)cnt*(cnt-1)/2;
	for(auto [_,cnt]:xneparno) resenje+=(long long)cnt*(cnt-1)/2;
	for(auto [_,cnt]:yparno) resenje+=(long long)cnt*(cnt-1)/2;
	for(auto [_,cnt]:yneparno) resenje+=(long long)cnt*(cnt-1)/2;
	cout<<resenje;
	```
	
	``` cpp title="04_prijateljski_trkaci.cpp" linenums="1"
	#include<bits/stdc++.h>
	
	using namespace std;
	
	map<int, int> glavnaD, sporednaD, Xp, Xn, Yp, Yn;
	
	int main(){
		ios_base::sync_with_stdio(0);
		cin.tie(0);
		int n;
		cin >> n;
		int x[n], y[n];
		for(int i = 0; i < n; i++){
			cin >> x[i] >> y[i];
			glavnaD[x[i] + y[i]]++;
			sporednaD[x[i] - y[i]]++;
			if(x[i] & 1)Xn[y[i]]++;
			else Xp[y[i]]++;
			if(y[i] & 1)Yn[x[i]]++;
			else Yp[x[i]]++;
		}
		long long answer = 0;
		for(auto p : glavnaD){
			answer += p.second * 1ll * (p.second-1);
		}
		for(auto p : sporednaD){
			answer += p.second * 1ll * (p.second - 1);
		}
		for(auto p : Xp){
			answer += p.second * 1ll * (p.second-1)/2;
		}
		for(auto p : Xn){
			answer += p.second * 1ll * (p.second - 1)/2;
		}
		for(auto p : Yp){
			answer += p.second * 1ll * (p.second-1)/2;
		}
		for(auto p : Yn){
			answer += p.second * 1ll * (p.second - 1)/2;
		}
		cout << answer << '\n';
	
	}

	```
