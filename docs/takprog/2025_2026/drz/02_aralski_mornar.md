---
hide:
  - toc
---

# B2 - Aralski Mornar

=== "Zadatak"
	
	| Vremensko ograničenje | Memorijsko ograničenje |
	|:-:|:-:|
	| 1000ms | 512MB |
	
	
	<br>
	
	Aralsko more na granici Uzbekistana i Kazahstana je čuveni primer mora koje "povlači" - ostavljajući iza sebe toksičnu Aralkum pustinju. 
	 
	<br>
	
	Data je matrica dimenzija $n \times n$. Protagonsita naše priče, Aralski mornar, se nalazi u gornjem levom polju, tj. polju $(1,1)$, i hoće da stignete do donjeg desnog polja, tj. polja $(n,n)$. Svaki njegov potez je jednog od sledeća tri tipa:
	
	1. Pomeri se na desno za jedan (tj. sa polja $(i,j)$ na polje $(i,j+1)$)
	2. Pomeri se na dole za jedan (tj. sa polja $(i,j)$ na polje $(i+1,j)$)
	3. Preskoči potez (tj. čekaj na polju $(i,j)$)
	
	Za svako polje je dato da li je na njemu more ili pustinja (vrednost $1$ predstavlja more, dok vrednost $0$ predstavlja pustinju). **Pre nego što završite** svaki potez, Aralsko more se skupi, a pustinja se proširi. Formalno **svako polje u matrici koje je bilo more postaje pustinja ukoliko je barem jedno susedno polje pustinjsko, dok polja koja su bila pustinja ostaju pustinja**.
	
	<br>
	
	Dodatno, za svako polje je data _toksičnost_. Ukupna toksičnost se računa kao suma toksičnosti svih pustinjskih polja na koja ste **stali**. Dakle, ako je polje bilo morsko, pa postalo pustinja dok ste čekali na njemu, ono se **ne računa**, dok se polje $(1,1)$ računa ako i samo ako je na početku bilo pustinjsko. Minimizujte ukupnu toksičnost na putu od gornjeg levog do donjeg desnog polja.
	
	<br>
	
	## Opis ulaza
	
	<br>
	
	U prvom dat je jedan ceo broj $n$ - koji označava dimenzije matrice.
	
	Narednih $n$ redova sadrže po jednu nisku karaktera. Sve niske su dužine $n$. $j$-ti karakter u $i$-toj nisci je $1$, ako je polje $(i,j)$ na početku more, a $0$ u suprotnom. 
	
	Poslednjih $n$ redova sadrže po $n$ celih brojeva. $j$-ti broj u $i$-tom redu predstavlja $t_{i,j}$ - toksičnost polja $(i,j)$.
	
	<br>
	
	## Opis izlaza
	
	<br>
	
	U prvoj i jedinoj liniji izlaza ispisati jedan broj - minimalnu ukupnu toksičnost na putu od gornjeg levog do donjeg desnog polja.
	
	<br>
	
	## Primer 1
	
	<br>
	
	### Ulaz
	
	<br>
	
	```
	2
	11
	01
	3 -2
	15 5
	```
	
	<br>
	
	### Izlaz
	
	<br>
	
	```
	3
	```
	
	### Objašnjenje primera 1
	
	<br>
	 
	Optimalno je da prvi potez provedemo čekajući. Dok mi čekamo na prvom polju, pustinja će se proširiti sa polja $(2,1)$ na polja $(1,1)$ i $(2,2)$. U drugom potezu ćemo se pomeriti na desno. Neposredno pre kraja našeg drugog poteza, more će se potpuno povući i sva polja će postati pustinjska. Dakle, kad u drugom potezu stignemo na polje $(1,2)$, ono će već biti pustinjsko i time će nam se ukupna toksičnost povećati za $-2$. U poslednjem potezu pomerimo na dole, time stižući na cilj. Ukupna suma toksičnosti je $(-2) + 5 = 3$.
	
	<br>
	
	## Primer 2
	
	<br>
	
	### Ulaz
	
	<br>
	
	```
	2
	00
	00
	1 3
	4 5
	```
	
	<br>
	
	### Izlaz
	
	<br>
	
	```
	9
	```
	
	<br>
	
	## Ograničenja
	
	
	<br>
	
	
	- $1 \leq n \leq 1.000$
	- $-1.000.000 \leq t_{i,j} \leq 1.000.000$
	
	<br>
	
	Test primeri su podeljeni u $5$ disjunktnih grupa:
	
	   
	   - U testovima vrednim $6$ poena: važi da su sva polja pustinjska i $n \leq 10$.
	   - U testovima vrednim $13$ poena: važi da su sva polja pustinjska.
	   - U testovima vrednim $18$ poena: važi $t_{i,j} \geq 0$.
	   - U testovima vrednim $25$ poena: važi $n \leq 200$.
	   - U testovima vrednim $38$ poena: bez dodatnih ograničenja.
	
	<br>
	
=== "Rešenje"
	
	| Autor | Tekst i test primeri | Analiza rešenja | Testiranje |
	|:-:|:-:|:-:|:-:|
	| Aleksa Milisavljević | Aleksa Milisavljević | Sofija Čebašek | Marko Trajković |
	
	## Rešenje kada su sva polja pustinjska i $n \leq 10$
	Primetimo da, kako su sva polja pustinjska, ukupna toksičnost na putu od gornjeg levog do donjeg desnog polja će biti suma toksičnosti svih polja na koja je Aralski mornar stao. Mornar će ukupno napraviti $2n-2$ koraka, od kojih će $n-1$ biti pomeranje na dole, a $n-1$ pomeranje na desno. Ukupan broj različitih redosleda tih koraka je $\binom{2n-2}{n-1}$. U ovom podzadatku možemo generisati sve moguće rasporede i odrediti za koji je ukupna toksičnost najmanja.
	
	Vremenska složenost: $O(n\binom{2n-2}{n-1})$
	
	## Rešenje kada su sva polja pustinjska
	Kao u prethodnom podzadatku, ukupna toksičnost će biti suma toksičnosti svih polja na koja je mornar stao. Ovaj podzadatak se može rešiti tehnikom dinamičkog programiranja. Matrica $dp$ dimenzija $n \times n$ se definiše na sledeći način:
	
	$$
	dp_{i,j} - \text{najmanja moguća ukupna toksičnost na putu od polja } (i,j) \text{ do polja } (n,n)
	$$
	
	Elementi matrice se računaju na sledeći način:
	
	$$
	dp_{i,j}=
	\begin{cases}
	t_{i,j} & \text{ za } i=n \text{ i } j=n \\
	dp_{i,j+1}+t_{i,j} & \text{ za } i=n \text{ i } 1 \leq j \leq n-1 \\
	dp_{i+1,j}+t_{i,j} & \text{ za } 1 \leq i \leq n-1 \text{ i } j=n \\
	min(dp_{i,j+1},dp_{i+1,j})+t_{i,j} & \text{ za } 1 \leq i \leq n-1 \text{ i } 1 \leq j \leq n-1
	\end{cases}
	$$
	
	Matrica se konstruiše od poslednjih ka prvim redovima i kolonama. Rešenje zadatka je vrednost polja $dp_{1,1}$.
	
	Vremenska složenost: $O(n^2)$
	
	## Rešenje kada važi $t_{i,j} \geq 0$
	**Tvrđenje:** Nakon što mornar jednom stane na pustinjsko polje, svako sledeće polje na koje stane će sigurno biti pustinjsko. Svako polje nakon prvog stajanja na pustinju će postati pustinjsko zbog proširivanja pustinje polja na kom se mornar nalazi.
	
	Kako su toksičnosti svih polja nenegativne, u ovom podzadatku je cilj stati na što manje pustinjskih polja. Zbog toga, ni jedan potez Aralskog mornara neće biti trećeg tipa, tj. neće čekati ni na jednom polju. Koristeći pretragu u širinu (eng. *Breadth First Search*, *BFS*), koja se započinje iz svih polja koja su na početku pustinja, za svako polje je moguće odrediti trenutak u kom će postati pustinja. Neophodno je odrediti sva polja koja mogu biti prva pustinjska polja na koje će mornar stati. Pretragom u širinu iz početnog polja, možemo uporediti vreme za koje mornar stiže na to polje i vreme kada to polje postaje pustinja. Ukoliko se za vreme pretrage stigne do polja za koje je vreme kada postaje pustinja manje od vremena kada mornar staje na njega, ono je jedno od mogućih prvih pustinjskih polja na koja će mornar stati i pretraga u širinu se ne nastavlja iz tog polja. Ukupna toksičnost kada se kretanje nastavi iz nekog polja može se izračunati unapred dinamičkim programiranjem, kao u prethodnom podzadatku. Rešenje je najmanje od svih ukupnih toksičnosti za sva moguća početna pustinjska polja.
	
	Vremenska složenost: $O(n^2)$
	
	## Rešenje kada važi $n \leq 200$
	Primetimo da ukoliko mornar preskoči potez (čeka na nekom polju), trenutak u kom će prvi put stati na pustinjsko polje ne zavisi od polja na kom je čekao. Ukoliko je početno polje pustinjsko, rešenje će biti $dp_{1,1}$. Inače, može da preskoči proizvoljan broj poteza dok se nalazi na početnom polju i zatim nastavi svoje kretanje. Za svako vreme čekanja od $0$ do $2n-2$ (sva polja će postati pustinjska nakon najviše $2n-2$ poteza), zadatak ćemo rešavati kao u prethodnom podzadatku i rešenje će biti najmanja toksičnost za sva moguća vremena čekanja.
	
	Vremenska složenost: $O(n^3)$
	
	## Glavno rešenje
	Posmatrajmo sva moguća početna pustinjska polja iz trećeg podzadatka. Primetimo da sva polja na koja mornar stane pre nego što dođe do tih polja takođe mogu biti prva pustinjska na koja će stati, ukoliko na početku čeka odgovarajući broj poteza. Implementacija rešenja je slična trećem podzadatku, a rešenje je najmanja vrednost $dp_{i,j}$ za sva polja $(i,j)$ koja se posete pretragom u širinu iz polja $(1,1)$, do zaustavljanja opisanom u trećem podzadatku. Ukoliko je prvo polje pustinjsko, rešenje je $dp_{1,1}$ i nije potrebno raditi pretragu u širinu iz tog polja.
	
	Vremenska složenost: $O(n^2)$
	
	``` cpp title="02_aralski_mornar.cpp" linenums="1"
	#include<bits/stdc++.h>
	#define maxn 2005
	using namespace std;
	int t[maxn][maxn];
	char s[maxn][maxn];
	int d[maxn][maxn];
	long long dp[maxn][maxn];
	bool vis[maxn][maxn];
	vector<pair<int,int>> q;
	int main() {
	    ios_base::sync_with_stdio(false);
	    cin.tie(NULL);
	    int n;
	    cin >> n;
	    for(int i = 0; i < n; i++) {
	        cin>>s[i];
	        for(int j=0;j<n;j++) {
	            if(s[i][j]=='1') {
	                d[i][j]=5*n;
	            }
	            else {
	                d[i][j]=0;
	                vis[i][j]=true;
	                q.push_back({i,j});
	            }
	        }
	    }
	    for(int i = 0; i < n; i++) {
	        for(int j = 0; j < n; j++) {
	            cin>>t[i][j];
	        }
	    }
	    if(q.size()==0) {
	        cout<<0<<endl;
	        return 0;
	    }
	    for(int i=n-1;i>=0;i--) {
	        for(int j=n-1;j>=0;j--) {
	            if(i==n-1 && j==n-1) {
	                dp[i][j]=t[i][j];
	            }
	            else if(i==n-1) {
	                dp[i][j]=dp[i][j+1]+t[i][j];
	            }
	            else if(j==n-1) {
	                dp[i][j]=dp[i+1][j]+t[i][j];
	            }
	            else {
	                dp[i][j]=min(dp[i+1][j],dp[i][j+1])+t[i][j];
	            }
	        }
	    }
	    for(int i=0;i<q.size();i++) {
	        int x=q[i].first;
	        int y=q[i].second;
	        for(int dx=-1;dx<=1;dx++) {
	            for(int dy=-1;dy<=1;dy++) {
	                if(dx==0 && dy==0) continue;
	                if(dx!=0 && dy!=0) continue;
	                int nx=x+dx;
	                int ny=y+dy;
	                if(nx<0 || nx>=n || ny<0 || ny>=n) continue;
	                if(vis[nx][ny]) continue;
	                vis[nx][ny]=true;
	                d[nx][ny]=d[x][y]+1;
	                q.push_back({nx,ny});
	            }
	        }
	    }
	    long long ans=1e18;
	    for(int i=0;i<n;i++) {
	        for(int j=0;j<n;j++) {
	            if(s[i][j]=='1' && d[i][j]<=i+j)
	            {
	                s[i][j]='0';
	            }
	            if(i==0 && j==0) {
	                if(s[i][j]=='0') ans=min(ans,dp[i][j]);
	            }
	            else {
	                if(s[i][j]=='1' || (i>0 && s[i-1][j]=='1') || (j>0 && s[i][j-1]=='1'))
	                {
	                    ans=min(ans,dp[i][j]);
	                }
	            }
	        }
	    }
	    cout<<ans<<endl;
	    return 0;
	}

	```
