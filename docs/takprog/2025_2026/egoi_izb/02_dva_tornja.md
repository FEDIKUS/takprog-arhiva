---
hide:
  - toc
---

# 2 - Dva tornja

=== "Zadatak"
	
	| Vremensko ograničenje | Memorijsko ograničenje |
	|:-:|:-:|
	| 1000ms | 256MB |
	
	
	
	<br>
	
	Sauron i Saruman su najbolji prijatelji. Danas su u vrtiću dobili $N$ blokova lego kockica. Od njih, $i$-ti ima visinu $h_i$. Oni žele da izgrade dva tornja slaganjem blokova jednog na drugi, tako da ti tornjevi budu **iste visine** i tako da budu **što viši**. Primetite da se jedan blok može koristiti u konstrukciji najviše jednog tornja, kao i da neki blokovi ne moraju biti upotrebljeni.
	
	<br>
	
	Ispišite maksimalnu moguću visinu tornjeva, ili $0$, ukoliko nije moguće napraviti dva tornja iste visine.
	
	<br>
	
	## Opis ulaza
	
	<br>
	
	U prvom redu dat je jedan ceo broj $N$ - broj blokova lego kockica.
	
	Naredni red sadrži $N$ celih brojeva odvojenih razmakom. Od tih brojeva, $i$-ti predstavlja $h_i$ - visinu $i$-tog bloka lego kockica.
	
	<br>
	
	## Opis izlaza
	
	<br>
	
	U prvoj i jedinoj liniji izlaza ispisati jedan broj - maksimalnu visinu tornjeva ili $0$, ukoliko nije moguće izgraditi dva tornja iste visine.
	
	<br>
	
	## Primer 1
	
	<br>
	
	### Ulaz
	
	<br>
	
	```
	8
	2 4 2 7 3 50 3 8
	```
	
	<br>
	
	### Izlaz
	
	<br>
	
	```
	13
	```
	
	### Objašnjenje primera 1
	
	<br>
	 
	Dati su blokovi visina $h = [2, 4, 2, 7, 3, 50, 3, 8]$. Sauron će iskoristiti prvi, drugi i četvrti da bi napravio toranj visine $2 + 4 + 7 = 13$. Saruman će iskoristiti treći, peti i osmi da bi napravio toranj jednake visine: $2 + 3 + 8 = 13$. Primetite da šesti i sedmi blok neće biti iskorišćeni.
	
	<br>
	
	## Primer 2
	
	<br>
	
	### Ulaz
	
	<br>
	
	```
	3
	1 2 10
	```
	
	<br>
	
	### Izlaz
	
	<br>
	
	```
	0
	```
	
	<br>
	
	## Ograničenja
	
	
	<br>
	
	
	- $1 \leq N \leq 500$
	- $1 \leq h_i \leq 100$
	
	<br>
	
	Test primeri su podeljeni u $5$ disjunktnih grupa:
	
	   
	   - U testovima vrednim $7$ poena: važi da su svi $h_i$ jednaki.
	   - U testovima vrednim $12$ poena: važi da $N \leq 100$ i $h_i = i$.
	   - U testovima vrednim $19$ poena: važi da $N \leq 17$.
	   - U testovima vrednim $32$ poena: važi da $N \leq 50$ i $h_i \leq 50$.
	   - U testovima vrednim $30$ poena: bez dodatnih ograničenja.
	
	<br>
	
=== "Rešenje"
	
	| Autor | Tekst i test primeri | Analiza rešenja | Testiranje |
	|:-:|:-:|:-:|:-:|
	| Nikola Milosavljević | Aleksa Milisavljević | Nemanja Majski | Sofija Čebašek |
	
	### Svi $h_i$ su jednaki
	
	Neka je visina svih blokova jednaka $H$. Ukoliko je $N$ parno, možemo staviti $\frac{N}{2}$ blokova na jedan i $\frac{N}{2}$ blokova na drugi toranj. Visina oba tornja je $H \cdot \frac{N}{2}$.
	
	Ukoliko je $N$ neparno, nemoguće je da svaki blok čini neki toranj, pošto bi jedan toranj imao paran, a drugi neparan broj blokova. Tako da je najbolje da se oba tornja formiraju sa $\frac{N-1}{2}$ blokova i njihova visina će biti $H \cdot \frac{N-1}{2}$.
	
	Vremenska i memorijska složenost su $O(N)$.
	
	### $N\le 100, h_i = i$
	
	Neka su $a$ i $b$ proizvoljni prirodni brojevi za koje važi $1 \le a,b \le N$. Primetimo da je $h_a + h_b = h_{a+1} + h_{b-1}$. Pretpostavimo da smo našli neki način da od prvih $m \le N-4$ blokova napravimo dva tornja iste visine. Onda možemo da dodamo blokove $m+1$ i $m+4$ na prvi toranj, a blokove $m+2$ i $m+3$ na drugi. Na taj način smo napravili dva tornja jednake visine od prvih $m+4$ blokova. Ovaj postupak nazivamo algoritmom proširivanja.
	
	Razlikujemo sledeće slučajeve:
	
	- Ukoliko je broj $N$ deljiv sa $4$, odgovor je polovina zbira svih visina. Odnosno $\frac{N \cdot (N+1)}{4}$. To možemo postići tako što samo primenjujemo algoritam proširivanja.  
	- Ukoliko je ostatak pri deljenju broja $N$ sa $4$ jednak $1$ , onda će zbir svih visina biti neparan. Tako da je nemoguće da svaki blok bude deo tornja. Ako je $N=1$, onda je odgovor $0$.  Inače možemo napraviti dva jednaka tornja od blokova sa visinama $2, 3, 4, \ldots, N$. Na prvi toranj ćemo staviti blokove $2$ i  $5$. Na drugi toranj ćemo staviti blokove $3$ i $4$. Zatim primenjujemo algoritam proširivanja da bi stavili ostale blokove. Visina oba tornja je $\frac{N \cdot (N+1) - 2}{4}$.
	- Ukoliko je ostatak pri deljenju broja $N$ sa $4$ jednak $2$ , onda će zbir svih visina biti neparan. Tako da je nemoguće da svaki blok bude deo tornja. Ako je $N=2$, onda je odgovor $0$.  Inače možemo napraviti dva jednaka tornja od blokova sa visinama $2, 3, 4, \ldots, N$. Na prvi toranj ćemo staviti blokove $2$, $3$ i  $5$. Na drugi toranj ćemo staviti blokove $4$ i $6$. Zatim primenjujemo algoritam proširivanja da bi stavili ostale blokove. Visina oba tornja je $\frac{N \cdot (N+1) - 2}{4}$.
	- Ukoliko je ostatak pri deljenju broja $N$ sa $4$ jednak $3$, moguće je da svaki blok bude deo tornja. Na prvi toranj ćemo staviti blokove $1$ i $2$. Na drugi toranj ćemo staviti blok $3$. Zatim primenjujemo algoritam proširivanja da bi stavili ostale blokove. Visina oba tornja je $\frac{N \cdot (N+1)}{4}$.
	
	Vremenska i memorijska složenost su $O(N)$.
	
	### $N \leq 17$
	
	Ukupno postoji $2^N$ načina da odaberemo koje ćemo blokove iskoristiti u nekom od tornjeva. Možemo za svaki od njih da proverimo da li je moguće od izabranih blokova napraviti dva tornja iste visine.
	
	Recimo da smo izabrali da napravimo dva tornja od blokova čije su visine $v_1, v_2, \ldots v_k$. Pitamo se da li je moguće od njih napraviti dva tornja iste visine. Dovoljno je proveriti da li može jedan toranj da bude visine $S = \frac{v_1 + v_2 + \ldots + v_k}{2}$, pošto će drugi toranj napravljen od ostalih blokova biti iste visine.
	
	Za tu proveru koristimo dinamičko progamiranje. Imamo $S \times k$ matricu $dp$, gde vrednost $dp_{i,j}$ govori o tome da li je moguće od prvih $j$ blokova napraviti toranj sa visinom $i$. Važi da je $dp_{i,j}$ moguće samo ako je moguće $dp_{i,j-1}$ ili $dp_{i-v_j,j-1}$. 
	
	Neka je $H$ najveća vrednost $h_i$. Vremenska složenost je $O(2^N \cdot N^2 \cdot H)$, a memorijska složenost je $O(N^2 \cdot H)$.    
	
	### $N, h_i \le 50$
	
	Neka je $S$ suma svih vrednosti $h_i$ u nizu.
	
	U ovom podzadatku ćemo da koristimo dinamičko programiranje. Imaćemo matricu $dp$ dimenzija $N \times \frac{S}{2} \times \frac{S}{2}$. Vrednost $dp_{i, a, b}$ predstavlja da li je moguće da koristeći samo prvih $i$ blokova napravimo dva tornja takva da je prvi visine $a$, a drugi visine $b$. Vrednost $dp_{i, a, b}$ je moguće samo ako je neka od sledećih vrednosti takođe moguća:
	 - $dp_{i-1, a, b}$, blok $i$ nije deo ni jednog tornja;
	 - $dp_{i-1, a-h_i, b}$, blok $i$ je deo prvog tornja;
	 -  $dp_{i-1, a, b-h_i}$, blok $i$ je deo drugog tornja.
	
	Takođe primetimo da dok iteriramo po $i$, nama je važan samo $dp_{i-1, a, b}$ za svako $0 \le a,b \le S$, tako da možemo pamtiti samo trenutni $dp_{i, a, b}$ i prethodni $dp_{i-1, a, b}$, čime je memorijska složenost $O(S^2)$.
	
	Vremenska složenost je $O(N \cdot S^2)$.
	
	### Bez dodatnih ograničenja
	
	U prethodnom rešenju čuvamo previše informacija. Ako je poznato da od prvih $i$ blokova možemo da napravimo da oba tornja imaju istu visinu $a$, nije nam važno da li mogu da imaju neku manju istu visinu.
	
	To je motivacija da promenimo $dp$. $dp_{i, d}$ će biti matrica dimenzije $N \times S$, gde je $dp_{i, d}$ najveća moguća  visina višeg tornja ako se od prvih $i$ blokova naprave tornjevi čija je apsolutna razkika visina tačno $d$. 
	
	Vrednost $dp_{i, d}$ je maksimum od sledećeg:
	- $dp_{i-1, d}$, blok $i$ neće činiti ni jedan toranj;
	- $dp_{i-1, d+h_i}$, blok $i$ će se staviti na niži toranj;
	- $dp_{i-1, d-h_i} + h_i$, blok $i$ će se staviti na viši toranj.
	
	Kao i u prethodnom podzadatku, kada računamo $dp_{i, d}$, za $0 \le d \le S$, nama trebaju samo vrednosti $dp_{i-1, d}$. Tako da je memorijska složenost $O(S)$, dok je vremenska složenost $O(S \cdot N)$.
	
	``` cpp title="02_dva_tornja.cpp" linenums="1"
	#include<bits/stdc++.h>
	#define maxn 1005
	#define maxh 205
	using namespace std;
	int dp[maxn*maxh];
	int tp[maxn*maxh];
	int n;
	int h[maxn];
	int main() {
	    cin.tie(0);
	    ios_base::sync_with_stdio(false);
	    cin>>n;
	    dp[0]=0;
	    for(int i=1;i<maxn*maxh;i++) {
	        dp[i]=-1e9;
	    }
	    for(int i=0;i<n;i++) {
	        cin>>h[i];
	        for(int j=0;j<maxn*maxh;j++) {
	            tp[j]=dp[j];
	        }
	        for(int j=0;j+h[i]<maxn*maxh;j++) {
	            tp[j+h[i]]=max(tp[j+h[i]],dp[j]+h[i]);
	        }
	        for(int j=0;j<maxn*maxh;j++) {
	            int c=j-h[i];
	            if(c>0) {
	                tp[c]=max(tp[c],dp[j]);
	            }
	            else {
	                tp[-c]=max(tp[-c],dp[j]-c);
	            }
	        }
	        for(int j=0;j<maxn*maxh;j++) {
	            dp[j]=tp[j];
	        }
	    }
	    cout<<dp[0]<<endl;
	    return 0;
	}

	```
