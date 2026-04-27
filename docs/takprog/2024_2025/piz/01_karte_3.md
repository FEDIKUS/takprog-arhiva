---
hide:
  - toc
---

# 1 - Karte 3

=== "Zadatak"
	
	| Vremensko ograničenje | Memorijsko ograničenje |
	|:-:|:-:|
	| 1000ms | 256MB |
	
	<br>
	
	Dat je niz sa $N$ karata. Na svakoj karti je napisan broj između $1$ i $N$, i svi napisani brojevi su različiti. Želite da karte sortirate od najmanje do najveće. Da biste to uradili, možete da *promešate* originalni niz tačno jednom. Operacija *mešanja niza karata* se definiše na sledeći način:
	
	 - Možete da zadržite isti redosled karata
	 - Po visokoj ceni od jednog bolivijana, možete da podelite niz karata na dve podsekvence (dakle podnizove u kojima ne moraju svi elementi biti uzastopni) $S_1$ i $S_2$, te potom njih rekurzivno *promešate*. Neka su rezultati *mešanja* ta dva podniza $T_1$ i $T_2$, redom. Rezultat *mešanja* celog niza je konkatenacija $T_1$ i $T_2$, tj. niz $T_1T_2$.
	
	<br>
	
	Kako nameravate da prođete na IOI u Boliviji, nemate previše bolivijana za razbacivanje. Ispišite koliko minimalno bolivijana biste morali da potrošite da biste sortirali niz karata. 
	
	Dodatno, dato je i $Q$ upita. U svakom upitu su date dve pozicije u nizu. Potrebno je zameniti karte na tim pozicijama i ispisati kolika je minimalna cena sortiranja karata nakon svakog upita.
	
	Primetite da upiti trajno menjaju redosled karata u nizu.
	
	<br>
	
	## Opis ulaza
	
	<br>
	
	Na prvoj liniji standardnog ulaza dati su celi brojevi $N$ i $Q$, koji predstavljaju broj karata u nizu i broj upita.
	
	U drugoj liniji standardnog ulaza, nalazi se niz $P$ sa $N$ celih brojeva, koji predstavljaju redosled karata u nizu. Karta na $i$-toj poziciji je upravo $P_i$.
	
	U narednih $Q$ linija, nalaze se po dva cela broja, $i$ i $j$ - koja opisuju pozicije karata u nizu koje treba zameniti.
	
	<br>
	
	## Opis izlaza
	
	<br>
	
	Na standardni izlaz treba ispisati $Q+1$ linija, koje predstavljaju minimalnu cenu pre prvog upita i minimalne cene nakon svakog od $Q$ upita.
	
	<br>
	
	## Primer 1
	
	<br>
	
	### Ulaz
	
	<br>
	
	```
	5 2
	5 4 3 2 1
	1 2
	3 5
	```
	
	<br>
	
	### Izlaz
	
	<br>
	
	```
	4
	3
	1
	```
	
	<br>
	
	### Objašnjenje
	
	<br>
	
	Pre prve operacije, niz karata je $[5,4,3,2,1]$. Primenjivaćemo operacije na sledeći način:
	 - $[5,4,3,2,1]$ - početni niz.
	 - $[4,3,2,1],[5]$ - podelili smo početni niz na dve podsekvence i platili jedan bolivijan.
	 - $[3,2,1],[4],[5]$ - podelili smo prvu podsekvencu na dve podsekvence i platili još jedan bolivijan.
	 - $[2,1],[3],[4],[5]$ - podelili smo prvu podsekvencu na dve podsekvence i platili još jedan bolivijan.
	 - $[1],[2],[3],[4],[5]$ - podelili smo prvu podsekvencu na dve podsekvence i platili još jedan bolivijan.
	
	Ukupno smo platili četiri bolivijana.
	
	Nakon prve operacije, niz karata je $[4,5,3,2,1]$.  Primenjivaćemo operacije na sledeći način:
	 - $[4,5,3,2,1]$ - početni niz.
	 - $[3,2,1],[4,5]$ - podelili smo početni niz na dve podsekvence i platili jedan bolivijan.
	 - $[2,1],[3],[4,5]$ - podelili smo prvu podsekvencu na dve podsekvence i platili još jedan bolivijan.
	 - $[1],[2],[3],[4],[5]$ - podelili smo prvu podsekvencu na dve podsekvence i platili još jedan bolivijan.
	
	Ukupno smo platili tri bolivijana.
	
	Nakon prve operacije, niz karata je $[4,5,1,2,3]$.  Primenjivaćemo operacije na sledeći način:
	 - $[4,5,1,2,3]$ - početni niz.
	 - $[1,2,3],[4,5]$ - podelili smo početni niz na dve podsekvence i platili jedan bolivijan.
	
	Ukupno smo platili jedan bolivijan.
	
	<br>
	
	## Ograničenja
	
	<br>
	
	- $1 \leq N \leq 200\,000$.
	- $0 \leq Q \leq 200\,000$.
	- $1 \leq P_i \leq N$ za sve $i=1, \dots, N$.
	- $P_i \neq P_j$ za sve $1 \leq i \neq j \leq N$.
	- U svakom upitu $1 \leq i \neq j \leq N$.
	
	<br>
	
	Test primeri su podeljeni u pet disjunktnih grupa:
	
	- U test primerima vrednim 10 poena: $N = 3$;
	- U test primerima vrednim 10 poena: $N \leq 20$;
	- U test primerima vrednim 25 poena: $N, Q \leq 2\,000$;
	- U test primerima vrednim 20 poena: U svakom upitu $j = i + 1$;
	- U test primerima vrednim 35 poena: Bez dodatnih ograničenja.
	
	<br>
	
	## Napomena
	
	<br>
	
	Prema kursu od 28.04.2025, u 11:45, jedan bolivijano vredi 14,94 dinara.
	
=== "Rešenje"
	
	| Autor | Tekst i test primeri | Analiza rešenja | Testiranje |
	|:-:|:-:|:-:|:-:|
	| Pavle Martinović | Aleksa Milisavljević | Pavle Martinović | Dimitrije Erdeljan |
	
	## Rešenje kada $N\leq 3$
	U ovom slučaju se zadatak može rešiti prostim posmatranjem slučajeva:
	- Ukoliko je špil već sortiran odgovor je očigledno $0$
	- Ukoliko je špil obrnuto sortiran ($3,2,1$) tada je odogovor jasno $2$ (npr u prvom potezu razbijemo na $2,1$ i $3$, a zatim sortiramo prvi deo sa još jednim potezom).
	- U svim ostalim slučajevima je odgovor $1$, jer uvek moguće podeliti ili na ($1$ i $2,3$ ili $1,2$ i $3$).
	Sada lako možemo rešiti zadatak tako što u svakom trenutku proverimo sve ove mogućnosti.
	## Rešenje kada je $N\leq20
	
	Posmatrajmo špilove koje dobijamo kao "listove" ovog procesa (odnosno one koje dobijemo u nekom koraku i odlučimo da ne promešamo). Da bismo rešili zadatak, svaki od tih špilova mora da bude neki niz uzastopnih brojeva. Međutim, po konstrukciji, svaki od tih špilova je podsekvenca originalnog špila. Tako da minimalan broj takvih "list" špilova možemo odrediti sledećim algoritmom:
	Idemo redom kroz špil i izdvojimo najmanji broj koji nismo do sad izvadili kada naiđemo na njega. Svaki prolzak kroz špil će nam izdvojiti jedan takav "list" špil najveće moguće dužine. Tako smo našli najmanju moguću podelu na "list" špilove. Neka označimo taj broj sa $k$.
	Primetimo da za svaki bolivijan mi pravimo jedan novi špil. Na početku imamo samo $1$ špil, a na kraju $k$, tako da nam je bilo potrebno barem $k-1$ bolivijana. Dokažimo da nam je toliko i dovoljno.
	Uzimo rastući podšpil koji smo dobili prvim prolaskom kroz niz u algoritmu opisanom gore. U prvom potezu podelimo špil na taj podšpil i ostatak. Po indukciji, drugi podšpil ćemo moći sortirati sa $k-2$ bolivijana, a kada ga spojimo sa prvim špilom dobijamo sortiran ceo špil za $k-1$ bolivijan.
	Sada možemo samo da simuliramo gornji algoritam u $O(N^2)$ te rešavamo zadatak u $O(QN^2)$.  
	
	## Rešenje kada je $N,Q\leq2000$
	Zadatak smo sveli na brzo nalaženje $k$ iz prethodnog rešenja. Posmatrajmo pozicije karata $x$ i $x+1$ u špilu. Ukoliko $x$ dolazi pre $x+1$ onda ćemo ih sigurno pokupiti u istom prolazu. Ako pak dolazi posle, onda ih sigurno nećemo pokupiti u istom prolasku. Ovo nam daje da je $k-1$ zapravo broj elemenata $x$ tako da je $x+1$ pre $x$ u nizu.
	Sa ovim znanjem, lako svaki upit možemo rešiti u $O(N)$: zapamtimo poziciju svakog elementa u prvom prolazu (nazovemo ovaj niz $P$) i onda izbrojimo broj elemenata tako da je $P[x]>P[x+1]$.
	## Rešenje kada razmenjujemo samo susedne
	
	Primetimo po prethodnom podzadataku da lako sledi da kada razmenjujemo susedne rešenje se menja samo ukoliko menjamo $x$ i $x+1$ (tad se povećava za $1$), odnosno $x+1$ i $x$ (tad se smanjuje za $1$). Stoga možemo u $O(N)$ naći inicijalno rešenje kao u prethodnom podzadatku, i zatim svaki upit rešiti u $O(1)$ jednostavnom proverom.
	
	## Glavno rešenje
	Vratimo se na niz $P$ iz trećeg podzadatka. Primetimo da ukoliko zamenimo vrednosti $x$ i $y$, tada zapravo zamenimo $P[x]$ i $P[y]$. Kada izvršimo ovu promenu, možemo da vidimo da se svako $4$ para koja nas interesuju promenilo: $(x-1,x)$, $(x,x+1)$, $(y-1,y)$ i $(y,y+1)$. Proverimo za ova $4$ para koji su promenili raspored i onda ažuriramo rešenje na odgovarajući način. Inicijalno rešenje možemo da nađemo u $O(N)$, te rešavamo ceo zadatak u $O(N+Q)$. 
	
	``` cpp title="01_karte_3.cpp" linenums="1"
	#include <bits/stdc++.h>
	#define maxn 500000
	using namespace std;
	int n,q,ans;
	int p[maxn],pos[maxn];
	bool inc(int i) {
	    return i>=2 && i<=n && pos[i-1]>pos[i];
	}
	int main() {
	    ios::sync_with_stdio(false); cin.tie(0);
	    cin>>n>>q;
	    for(int i=1;i<=n;i++) {
	        cin>>p[i];
	        pos[p[i]]=i;
	    }
	    for(int i=2;i<=n;i++) ans+=inc(i);
	    cout<<ans<<endl;
	    while(q--) {
	        int x,y;
	        cin>>x>>y;
	        set<int> s = {p[x],p[x]+1,p[y],p[y]+1};
	        for(auto v:s) ans-=inc(v);
	        swap(pos[p[x]],pos[p[y]]);
	        swap(p[x],p[y]);
	        for(auto v:s) ans+=inc(v);
	        cout<<ans<<endl;
	    }
	    return 0;
	}

	```
