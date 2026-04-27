---
hide:
  - toc
---

# 2 - Najveća pojava

=== "Zadatak"
	
	| Vremensko ograničenje | Memorijsko ograničenje |
	|:-:|:-:|
	| 1000ms | 256MB |
	
	<br>
	
	Komisija mora u jako kratkom roku da izabere reprezentaciju za IOI (Ispitivanje Ofsajda na Internetu) u Sukreu! Na raspolaganju su $n$ takmičara i za svakog takmičara je poznato koliko je iskusan - i to je predstavljeno po jednim celim brojem, $a_i$ za $i=1,2,\ldots,n$.
	
	<br>
	
	Da bi reprezentacija bila legitimna po Pravilniku Ofsajd Olimpijada, ona mora biti izabrana kao **uzastopni podniz** takmičara na raspolaganju, čija je **suma iskustva jednaka nuli**.
	
	<br>
	
	Komisija želi da pošalje najbalansiraniji tim na IOI. Balansiranost jednog legitimnog tima se definiše kao **broj pojava najčešćeg elementa** u nizu iskustava izabranog tima (dakle posmatramo pojavljivanja samo u podnizu koji smo izabrali kao tim). **Garantuje se da postoji bar jedan legitiman izbor tima.**
	
	<br>
	
	U koliko pomognete Komisiji, dobićete priliku da rešavate naredni zadatak, koji će vas *možda* kvalifikovati za besplatnu kartu do Sukrea!
	
	<br>
	
	## Opis ulaza
	
	<br>
	
	Na prvoj liniji standardnog ulaza dati su celi brojevi $n$, koji predstavljaju broj takmičara.
	
	<br>
	
	U drugoj liniji standardnog ulaza, nalazi se niz $a$ sa $n$ celih brojeva, koji predstavljaju iskustva takmičara. Takmičar na $i$-toj poziciji ima $a_i$ iskustva.
	
	<br>
	
	## Opis izlaza
	
	<br>
	
	Na standardni izlaz treba ispisati jednu liniju, koja predstavlja broj pojava najčešćeg elementa u izabranom legitimnom podnizu iskustva takmičara.
	
	<br>
	
	## Primer 1
	
	<br>
	
	### Ulaz
	
	<br>
	
	```
	2
	1 -1
	```
	
	<br>
	
	### Izlaz
	
	<br>
	
	```
	1
	```
	
	<br>
	
	### Objašnjenje
	
	<br>
	
	Jedini legitimni tim je tim sa svim takmiračima. Kako se obe jačine (i $1$ i $-1$) javljaju tačno jednom, odgovor je $1$.
	
	<br>
	
	## Primer 2
	
	<br>
	
	### Ulaz
	
	<br>
	
	```
	5
	1 2 0 -2 -1
	```
	
	<br>
	
	### Izlaz
	
	<br>
	
	```
	1
	```
	
	<br>
	
	### Objašnjenje
	
	<br>
	
	Postoji tri legitimna tima u ovom primeru.
	
	<br>
	
	Prvi legitiman tim je samo element $0$. Najčešći element u ovom podnizu je očigleno $0$ i broj pojava najčešćeg elementa je $1$.
	
	<br>
	
	Drugi legitiman tim je podniz $2,0,-2$. Svi elementi u ovom podnizu se podjednako često javljaju i broj pojava najčešćeg elementa je onda takođe $1$.
	
	<br>
	
	Treći legitiman tim je ceo niz $1,2,0,-2,-1$. Svi elementi u ovom podnizu se podjednako često javljaju i broj pojava najčešćeg elementa je onda takođe $1$.
	
	<br>
	
	Dakle najbalansiraniji legitiman tim je bilo koji od ova tri i njegova balansiranost je $1$. 
	
	<br>
	
	## Primer 3
	
	<br>
	
	### Ulaz
	
	<br>
	
	```
	20
	1 1 -1 0 0 1 0 -1 -1 -1 0 1 0 0 1 1 0 0 -1 -1
	```
	
	<br>
	
	### Izlaz
	
	<br>
	
	```
	8
	```
	
	<br>
	
	### Objašnjenje
	
	<br>
	
	Legitimni tim sa najviše pojava je tim sa takmičarima čiji su indeksi od 4 do 19. Najčešći element u ovom podnizu je element $0$, koji se javlja $8$ puta.
	
	<br>
	
	## Primer 4
	
	<br>
	
	### Ulaz
	
	<br>
	
	```
	5
	-4294967296 -4294967296 -4294967296 -4294967296 12884901888
	```
	
	<br>
	
	### Izlaz
	
	<br>
	
	```
	3
	```
	
	<br>
	
	### Objašnjenje
	
	<br>
	
	Legitimni tim sa najviše pojava je tim sa takmičarima čiji su indeksi od 2 do 5. Najčešći element u ovom podnizu je element $-4294967296$, koji se javlja $3$ puta.
	
	<br>
	
	## Ograničenja
	
	<br>
	
	- $1 \leq n \leq 200\,000$.
	- $\mid a_i \mid \leq 10^{12}$.
	- Garantuje se da postoji bar jedan legitiman izbor tima.
	<br>
	
	Test primeri su podeljeni u pet disjunktnih grupa:
	
	- U test primerima vrednim 9 poena: $n \leq 100$;
	- U test primerima vrednim 10 poena: $n \leq 500$;
	- U test primerima vrednim 23 poena: $n \leq 2000$;
	- U test primerima vrednim 25 poena: Najviše $1000$ različitih vrednosti iskustva se pojavljuju $2$ ili više puta u celom nizu;
	- U test primerima vrednim 33 poena: Bez dodatnih ograničenja.
	
	<br>
	
=== "Rešenje"
	
	| Autor | Tekst i test primeri | Analiza rešenja | Testiranje |
	|:-:|:-:|:-:|:-:|
	| Nemanja Majski | Tekst: Marko Milenković; test primeri: Nemanja Majski | Dimitrije Erdeljan | Pavle Martinović |
	
	## Rešenje kada $N\leq 100$
	
	U ovom slučaju, možemo ispitati sve podnizove niza $a_i$, za svaki od
	njih izračunati sumu, i ako je suma $0$ pronaći najveći element.
	Da bi našli najveći element, potrebno je da izbrojimo koliko puta se
	pojavljuje svaki broj u nizu. Pošto su brojevi veliki, neophodno je da
	ne trošimo memoriju na pojavljivanja brojeva kojih nema u nizu -- ovo
	možemo uraditi ili korišćenjem prikladne strukture (npr. `std::map` iz
	standardne biblioteke), ili tako što na početku izvršavanja zamenimo
	najmanji broj u nizu sa $0$, sledeći najmanji sa $1$, i tako dalje.
	
	Ukupno ispitujemo $\mathcal{O}(N^2)$ podnizova, i za svaki nam je
	potrebno $\mathcal{O}(N \log N)$ ako koristimo `std::map` (moguće je i
	$\mathcal{O}(N)$ sa drugim strukturama), za ukupnu vremensku složenost
	$\mathcal{O}(N^3 \log N)$.
	
	## Rešenje kada $N\leq 2000$
	
	Za veće $N$, neophodno je da ne ispitujemo svaki podniz. Primetimo da
	je od legitimnih podnizova koji počinju sa $a_i$, najbalansiraniji
	najduži, odnosno onaj koji se završava sa $a_j$ gde je $j$ najveće.
	Sa ovom optimizacijom, ispitujemo $\mathcal{O}(N)$ nizova, po jedan za
	svako $i$, i ukupna vremenska složenost (koristeći pristup iz prošlog
	podzadatka) je $\mathcal{O}(N^2 \log N)$.
	
	U ovom podzadatku, najveće $j$ za koje je $a_i, a_{i+1}, \dots, a_j$
	balansiran možemo naći tako što krenemo od $a_i$ i pamtimo sumu svih
	elemenata do $j$. Za kompletan zadatak će nam trebati efikasniji
	algoritam: izračunamo prefiksne sume
	
	$$ p_i = a_1 + a_2 + \dots + a_i $$
	
	u jednom prolazu kroz niz koristeći $p_1 = a_1$, $p_{i+1} = p_i +
	a_{i+1}$, i tražimo kraj niza $j$ kao najveći indeks gde $p_j = p_i$.
	
	## Glavno rešenje
	
	Rešenje iz prošlog podzadatka nam daje $N$ kandidata za legitimne
	podnizove koji mogu biti najbalansiraniji. Primenićemo još jednu
	optimizaciju: ako je jedan od kandidata potpuno sadržan u drugom,
	sigurno nije najbalansiraniji. Nazovimo početke i krajeve preostalih
	podnizova $(i_1, j_1), (i_2, j_2), \dots$, i sortirajmo ih tako da
	$i_1 < i_2 < \dots$. Zbog ove optimizacije, takođe važi $j_1 < j_2 <
	\dots$.
	
	Sada možemo koristiti tehniku dva pokazivača da ih sve ispitamo.
	Potrebna nam je efikasna struktura u kojoj ćemo pratiti elemente
	trenutnog podniza, koja podržava dodavanje, izbacivanje, i upit za
	najčešći element. Kada pređemo na $k+1$-vi podniz, izbacimo elemente u
	$a$ od $i_k$ do $i_{k+1}-1$, i dodamo one od $j_k+1$ do $j_{k+1}$.
	Svaki element ćemo ubaciti i izbaciti po jednom, tako da nam treba
	ukupno $\mathcal{O}(N)$ operacija nad strukturom.
	
	Jedan način da implementiramo ovu strukturu je da brojimo elemente
	podniza na isti način kao ranije ($\mathcal{O}(\log N)$ po upitu sa
	`std::map`), i da brojeve pojavljivanja čuvamo u `std::set`, koji nam
	daje $\mathcal{O}(\log N)$ ubacivanje, izbacivanje, i upit za najveću
	vrednost. Kada se broj pojavljivanja nekog elementa promeni, iz `set`-a
	samo izbacimo stari broj pojavljivanja i ubacimo novi.
	
	Sa $\mathcal{O}(N)$ `map` i `set` operacija složenosti
	$\mathcal{O}(\log N)$, ukupna složenost je $\mathcal{O}(N \log N)$.
	
	## Napomena
	
	Zadatak je moguće rešiti i Moovim algoritmom uz pažljivu implementaciju.
	
	``` cpp title="02_najveca_pojava.cpp" linenums="1"
	#include<bits/stdc++.h>
	#define ll long long
	using namespace std;
	const int maxn=1e6+5;
	vector<pair<ll,ll>> inter;
	ll niz[maxn],n,pref[maxn];
	map<ll,ll> poc,kraj,kol;
	multiset<ll> S;
	int main(){
	   ios_base::sync_with_stdio(false);
	   cin.tie(0);
	   cin>>n;
	   for(int i=1;i<=n;i++)
	      cin>>niz[i];
	   for(int i=1;i<=n;i++)
	     pref[i]=pref[i-1]+niz[i];
	   for(int i=1;i<=n;i++){
	      kraj[pref[i]]=i;
	      if(poc.find(pref[i])==poc.end())
	         poc[pref[i]]=i+1;
	   }
	   poc[0]=1;
	   for(int i=1;i<=n;i++)
	      inter.push_back({poc[pref[i]],kraj[pref[i]]});
	   sort(inter.begin(),inter.end());
	   ll maxr=inter[0].second;
	   for(int i=0;i<inter.size();i++){
	      maxr=max(maxr,inter[i].second);
	      inter[i].second=maxr;
	   }
	   ll l=0,r=0;
	   kol[0]=1;
	   S.insert(1);
	   for(int i=1;i<=n;i++)
	      S.insert(0);
	   ll res=1;
	   for(int i=0;i<inter.size();i++){
	      while(r<inter[i].second){
	         r++;
	         ll br=niz[r];
	         S.erase(S.find(kol[br]));
	         kol[br]++;
	         S.insert(kol[br]);
	      }
	      while(l<inter[i].first){
	         l++;
	         ll br=niz[l-1];
	         S.erase(S.find(kol[br]));
	         kol[br]--;
	         S.insert(kol[br]);
	      }
	      res=max(res,*S.rbegin());
	   }
	   cout<<res<<"\n";
	}

	```
