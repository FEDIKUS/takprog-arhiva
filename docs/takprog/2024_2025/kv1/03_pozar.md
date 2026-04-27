---
hide:
  - toc
---

# 3 - Požar

=== "Zadatak"
	
	| Vremensko ograničenje | Memorijsko ograničenje |
	|:-:|:-:|
	| 1000ms | 256MB |
	
	<br>
	
	Steva, glavni lik popularne igrice Rudarski zanat, našao se u lavirintu. Lavirint je $N \times M$ matrica koja sadrži prohodna polja i zidove.
	
	<br>
	
	Šunjači, zombiji i kosturi su čudovišna stvorenja koja ne vole Stevu. Kako bi mu otežali igru, oni su zapalili lavirint tako što su u nekoliko polja postavili vatru.
	
	<br>
	
	Steva nema mnogo izbora i mora reagovati brzo. Jedan njegov potez sastoji se od sledećeg:
	
	 * Prvo se vatra raširi na sva susedna **slobodna** polja. Tačnije, ako je polje $(i,j)$ sadržalo vatru, sada će sadržati i slobodna polja $(i-1,j)$, $(i+1,j)$, $(i,j-1)$ i $(i,j+1)$ koja su unutar matrice.
	
	 * Zatim, Steva izabere slobodno polje na koje će skočiti. Može da ostane na mestu ili da se pomeri na susedno **slobodno** polje (krećući se u jednom od četiri smera opisana u prethodnoj stavki).
	
	<br>
	
	Steva gubi igru ako ga uhvati vatra nakon završetka bilo kog poteza. **Ni Steva ni vatra ne mogu proći kroz zid, niti izaći iz matrice.**
	
	<br>
	
	Na svu sreću, Steva ima elitru i može leteti. Nju može iskoristiti u slobodnom polju, na samom početku, ili nakon završetka bilo kog poteza. Ovim mu neka polja do kojih može doći daju mogućnost da izađe iz lavirinta. Drugim rečima, to su sva polja do kojih može stići pre vatre. Naći broj takvih polja.
	
	<br>
	
	## Opis ulaza
	
	<br>
	
	Prva linija standardnog ulaza sadrži dva prirodna broja $N$ i $M$ - dimenzije lavirinta.
	
	<br>
	
	Narednih $N$ linija sadrže opis matrice karaktera koja predstavlja lavirint. Svaka linija sadrži $M$ karaktera. Tipovi karaktera su:
	  * $\texttt{.}$ - slobodno polje.
	  * $\texttt{*}$ - zid kroz koji se ne može proći.
	  * $\texttt{X}$ - vatra.
	  * $\texttt{S}$ - Steva; postoji tačno jedno polje koje sadrži Stevu na početku i ono je takođe slobodno za kretanje.
	
	<br>
	
	**Polja prva tri tipa mogu da se jave proizvoljan broj puta, a mogu da se i ne pojave uopšte.** Sva slova su velika i latinična.
	
	<br>
	
	## Opis izlaza
	
	<br>
	
	Na standardni izlaz ispisati samo broj polja iz kojih Steva može iskoristiti elitru. Pravila su opisana ranije u postavci.
	
	<br>
	
	## Primer 1
	
	<br>
	
	### Ulaz
	
	<br>
	
	```
	6 4
	.S..
	*.**
	..**
	....
	.***
	X...
	```
	
	<br>
	
	### Izlaz
	
	<br>
	
	```
	6
	```
	
	### Objašnjenje
	
	<br>
	
	Polja do kojih je Steva mogao doći su označena sa $\texttt{S}$. Polja koja je vatra progutala pre Stevinog dolaska označena su sa $\texttt{X}$. Napomenimo da postoje polja do kojih i Steva i vatra mogu doći u istom trenutku. Po pravilima igre, vatra će progutati Stevu i to nisu polja koja razmatramo za rešenje.
	```
	SSSS
	*S**
	XS**
	XXXX
	X***
	XXXX
	```
	
	<br>
	
	## Primer 2
	
	<br>
	
	### Ulaz
	
	<br>
	
	```
	4 6
	**.XX.
	.S...*
	.**.**
	X..X..
	```
	
	<br>
	
	### Izlaz
	
	<br>
	
	```
	3
	```
	
	### Objašnjenje
	
	<br>
	
	```
	**XXXX
	SSSXX*
	X**X**
	XXXXXX
	```
	
	<br>
	
	## Primer 3
	
	<br>
	
	### Ulaz
	
	<br>
	
	```
	3 4
	S.*.
	..*.
	**X.
	```
	
	<br>
	
	### Izlaz
	
	<br>
	
	```
	4
	```
	
	### Objašnjenje
	
	<br>
	
	```
	SS*X
	SS*X
	**XX
	```
	
	<br>
	
	## Primer 4
	
	<br>
	
	### Ulaz
	
	<br>
	
	```
	5 5
	.....
	.....
	..S..
	.....
	.....
	```
	
	<br>
	
	### Izlaz
	
	<br>
	
	```
	25
	```
	
	### Objašnjenje
	
	<br>
	
	```
	SSSSS
	SSSSS
	SSSSS
	SSSSS
	SSSSS
	```
	
	<br>
	
	## Ograničenja
	
	
	<br>
	
	$N, M \leq 1\,000$
	
	<br>
	
	Test primeri su podeljeni u četiri disjunktne grupe:
	
	- U testovima vrednim 15 poena: $N=1$;
	
	- U testovima vrednim 25 poena: $N,M \leq 10$;
	
	- U testovima vrednim 35 poena: Tačno jedno polje sadrži vatru;
	
	- U testovima vrednim 25 poena: Bez dodatnih ograničenja.
	
	<br>
	
	
	
	
	
	
=== "Rešenje"
	
	| Autor | Tekst i test primeri | Analiza rešenja | Testiranje |
	|:-:|:-:|:-:|:-:|
	| Aleksandar Višnjić | Aleksandar Višnjić | Marko Milenković | Miloš Milutinović |
	
	## Rešenje kada je $N = 1$
	
	U ovom podzadatku lavirint je niz. Steva može da se kreće potencijalno samo levo i desno. Razmatrajmo koliko daleko Steva može da stigne na desno, zato što je slučaj na levo simetričan. Ukoliko na desno Steva prvo naiđe na zid, pre bilo koje vatre, onda može Steva može iz svih polja desno od sebe a pre zida da iskoristi elitru. Ukoliko Steva na desno prvo naiđe na vatru onda može da iskoristi elitru na svim poljima strogo pre sredine segmenta od Steve do prve vatre.
	
	## Rešenje kada je $N, M \leq 10$
	
	U ovom podzadatku dovoljno je proveriti za svako polje brute-force metodom da li mu je bliži Steva ili bilo koja vatra.
	
	## Rešenje kada tačno jedno polje sadrži vatru
	
	Matricu možemo posmatrati kao graf, gde su polja matrice čvorovi grafa, a veze postoje između susednih polja, osim ukoliko je bar jedno od tih polja zid. Možemo BFS algoritmom da pronađemo rastojanje od Steve do svih slobodnih polja i isto tako još jednim BFS algoritmom da pronađemo rastojanje od jedine vatre do svih slobodnih polja. Zatim samo uporedimo u svakom polju ko je bliži i u zavisnosti od toga uračunamo to polje u rešenje.
	
	
	## Glavno rešenje
	
	Glavno rešenje je idejno jako slično prethodnom podzadatku. Samo što ćemo u ovom slučaju da koristimo BFS algoritam sa više izvora. Naime, prilikom implementacije možemo u red () dodati sve čvorove/polja koja sadrže vatru i obeležiti njihovu razdaljinu kao nula. Zatim ostatak algoritma radi identično kao i u prošlom podzadatku. Razlika je što ćemo sada imati za svako polje razdaljinu od najbližeg polja sa vatrom i tu vrednost onda uporediti sa razdaljinom od Steve.
	
	``` cpp title="03_pozar.cpp" linenums="1"
	#include <bits/stdc++.h>
	
	#define xx first
	#define yy second
	
	using namespace std;
	
	char tab[1003][1003];
	bool vis[1003][1003];
	int vdist[1003][1003];
	int sdist[1003][1003];
	
	int main()
	{
	    ios_base::sync_with_stdio(false);
	    cin.tie(0),cout.tie(0);
	
	    int n,m; cin>>n>>m;
	    for (int i=0;i<n;i++) cin>>tab[i];
	
	    for (int i=0;i<n;i++)
	        for (int j=0;j<m;j++)
	            vdist[i][j]=1e9,sdist[i][j]=vdist[i][j];
	
	    int sx,sy;
	    for (int i=0;i<n;i++)
	        for (int j=0;j<m;j++)
	            if (tab[i][j]=='S')
	                sx=i,sy=j;
	
	    queue<pair<pair<int,int>,int>> bfs;
	    for (int i=0;i<n;i++)
	        for (int j=0;j<m;j++)
	            if (tab[i][j]=='X') bfs.push({{i,j},0});
	    while (!bfs.empty())
	    {
	        int i=bfs.front().xx.xx;
	        int j=bfs.front().xx.yy;
	        int d=bfs.front().yy;
	        bfs.pop();
	        if (i<0 || i>=n || j<0 || j>=m) continue;
	        if (tab[i][j]=='*' || vis[i][j]) continue;
	        vis[i][j]=true;
	        vdist[i][j]=d;
	        bfs.push({{i+1,j},d+1});
	        bfs.push({{i-1,j},d+1});
	        bfs.push({{i,j-1},d+1});
	        bfs.push({{i,j+1},d+1});
	    }
	
	    while (!bfs.empty()) bfs.pop();
	    for (int i=0;i<n;i++)
	        for (int j=0;j<m;j++)
	            vis[i][j]=false;
	    bfs.push({{sx,sy},0});
	    while (!bfs.empty())
	    {
	        int i=bfs.front().xx.xx;
	        int j=bfs.front().xx.yy;
	        int d=bfs.front().yy;
	        bfs.pop();
	        if (i<0 || i>=n || j<0 || j>=m) continue;
	        if (tab[i][j]=='*' || vis[i][j]) continue;
	        vis[i][j]=true;
	        sdist[i][j]=d;
	        bfs.push({{i+1,j},d+1});
	        bfs.push({{i-1,j},d+1});
	        bfs.push({{i,j-1},d+1});
	        bfs.push({{i,j+1},d+1});
	    }
	
	    int ans=0;
	    for (int i=0;i<n;i++)
	        for (int j=0;j<m;j++)
	            if (sdist[i][j]<vdist[i][j]) ans++;
	
	    cout<<ans<<"\n";
	}

	```
