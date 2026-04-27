---
hide:
  - toc
---

# 6 - Baki i Srećko

=== "Zadatak"
	
	| Vremensko ograničenje | Memorijsko ograničenje |
	|:-:|:-:|
	| 1000ms | 256MB |
	
	<br> Baki i Srećko se trenutno nalaze u centru Kigalija. Baki iz nama nepoznatih razloga ne voli da bude u blizini Srećka. Budući da Baki ne zna da se snađe u prostoru, potrebna mu je vaša pomoć da se udalji što je više moguće od njega! <br> Kigali se može predstaviti kao Dekartov koordinatni sistem čije apsolutne vrednosti koordinata ne prelaze $10^{18}$. Centar Kigalija je tačka $(0,0)$. Baki ima $n$ različitih mogućnosti za pomeraje i za svaki od njih bira da li će ga izvršiti ili ne. Pomeraj $i$ je određen brojevima $x_i$ i $y_i$. Ako se Baki trenutno nalazi na koordinatama $(X,Y)$, posle pomeraja $i$ će se nalaziti na koordinatama $(X+x_i,Y+y_i)$. Pošto se Srećko ne pomera pomozite Bakiju da izabere koje pomeraje da izvrši tako da maksimizuje Euklidsku distancu od svoje krajnje pozicije do (0,0) tako što ćete ispisati  koliko pomeraja treba da uradi i indekse tih pomeraja.<br> 
	## Opis ulaza  
	U prvoj liniji standardnog ulaza dat je ceo broj $n$, broj mogućih pomeraja. <br> U narednih $n$ linija standardnog ulaza, nalaze se po dva cela broja - $x_i,y_i$. Linija $i+1$ opisuje pomeraj $i$.
	## Opis izlaza  
	U prvoj liniji standardnog izlaza ispišite $k$ - broj pomeraja koje Baki treba da uradi da bi se maksimalno udaljio od Srećka. U sledećem redu ispišite $k$ brojeva koji predstavljaju indekse pomeraja koje Baki treba da izvrši. Ako postoji više validnih rešenja ispisati bilo koje.
	## Primer 1
	### Ulaz
	 ``` 
	3 
	4 7
	-2 -4
	-2 5 
	```   
	### Izlaz  
	 ```
	2
	1 3 
	 ```  
	## Primer 2  
	### Ulaz  
	```   
	4
	3 3
	-3 3
	-3 -3
	3 -3
	   ```   
	### Izlaz  
	``` 
	2
	1 2
	 ```   
	### Objašnjenje primera
	U primeru 2 postoji više validnih rešenja. Npr. možemo odabrati da Baki uradi pomeraje $3$ i $4$ i dobili bismo isto rastojanje Bakija od Srećka.
	## Ograničenja  
	- $1 \leq n \leq 300.000$  
	- $-10^{9} \leq x_i,y_i \leq 10^{9}$
	
	Test primeri su podeljeni u $5$ disjunktnih grupa:
	 - U testovima vrednim $10$ poena: važi $n \leq 20$.
	 - U testovima vrednim $20$ poena: važi $n,x_i \leq 500$. 
	 - U testovima vrednim $40$ poena: važi $n \leq 1000$.  
	 - U testovima vrednim $30$ poena: bez dodatnih ograničenja. 
	
	
	
=== "Rešenje"
	
	| Autor | Tekst i test primeri | Analiza rešenja | Testiranje |
	|:-:|:-:|:-:|:-:|
	| Uroš Kostadinović | Uroš Kostadinović | Uroš Kostadinović | Vladimir Milenković |
	
	## Rešenje kada je $N \leq 20$
	
	Možemo testirati svih $2^{20}$ mogućnosti za izbore pomeraja i izaberemo najbolju (svaki pomeraj ili uzmemo ili ne uzmemo). Vremenska složenost $O(2^{n})$.
	
	## Rešenje kada $n, |x_i| \leq 500$.
	
	Dovoljno je da za svaku moguću vrednost $X$, sumu svih pomeraja po $x$ koordinati, proverimo slučajeve kada je $Y$, suma svih pomeraja po $y$ koordinati, maksimalna i minimalna. Te vrednosti možemo izračunati slično kao u problemu ranca, gde su $x_i$ težine predmeta, a $y_i$ vrednosti. Problem nastaje kada treba da čuvamo vrednosti i za negativne vrednosti $X$. To možemo uraditi tako što vrednost za $X$, umesto na indeksu $X$, čuvamo na indeksu $X + |X|_{max}$, gde $|X|_{max}$ označava maksimalnu apsolutnu vrednost $X$. Vremenska složenost $O(n \sum |x_i|)$. Memorijska složenost $O(n \sum |x_i|)$.
	
	## Rešenje kada je $n \leq 1000$
	
	Zadatak se može preformulisati na sledeći način: Dato je $n$ vektora. Izabrati podskup ovih vektora tako da njihov zbir ima najveću moguću dužinu. Pretpostavimo da smo za sada uzeli skup vektora $I = \{ v_{i_1},v_{i_2}...v_{i_k} \}$ i neka je njihov zbir $v_I$. Posmatrajmo kakva će biti dužina vektora ako u skup dodamo vektor $u$. Važi $|v_I + u|^2 =  |v_i|^2 +|u|^2 + 2(v_i\cdot u) = |v_i|^2 +|u|^2 + 2|v_I||u|\cos\theta$, gde je ugao $\theta$ ugao koji formiraju vektori $v_I$ i $u$, a $v_i\cdot u$ skalarni proizvod vektora $v_i$ i $u$. Ako je $\cos\theta > 0$ onda nam se dodavanjem vektora $u$ u skup $I$ dužina vektora povećava. Posmatrajmo kakva će biti dužina vektora ako iz skupa izbacimo vektor $u$. Važi $|v_I - u|^2 =  |v_i|^2 +|u|^2 - 2(v_i\cdot u) = |v_i|^2 +|u|^2 - 2|v_I||u|\cos\theta$. Ako je $\cos\theta < 0$ onda nam se izbacivanjem vektora $u$ iz skupa $I$ dužina vektora povećava. Ovo znači da ćemo u optimalnom rešenju uzeti sve vektore s jedne strane prave koja je normalna na taj vektor. Dovoljno je da fiksiramo pravu koja će biti normalna na rezultujući vektor i onda uzmemo sve vektore s jedne  njene strane. Pošto ima beskonačno mnogo pravih kroz $(0,0)$ ne možemo da probamo svaku od njih. Dovoljno je da proverimo sve prave koje su određene sa $(0,0)$ i nekim od mogućih pomeraja, tj. prolazi kroz $(0,0)$ i $(x_i,y_i)$. Sada je potrebno voditi računa na to da nećemo uzeti vektore sve sa jedne strane od neke prave, već sve vektore s jedne strane neke prave koji nisu kolinearni sa njom i sve vektore koji su na toj pravoj i u istom su smeru.  Za svaku od $2n$ mogućnosti ($2n$ jer je bitno s koje strane uzimamo vektore) ćemo za svaki od $n$ vektora proveriti da li je na određenoj strani nje. Vremenska složenost $O(n^2)$.
	
	## Rešenje za 100 bodova
	Koristićemo istu ideju kao u rešenju prethodnog podzadatka. Možemo primetiti da ako sortiramo sve vektore oko $(0,0)$ po uglu koji određuju sa $x$ osom ćemo uvek pri fiksiranju neke prave uzeti neki uzastopni interval vektora, ili neki prefiks i sufiks. Ako u prethodnom rešenju fiksiramo redom prave u sortiranom poretku drugu granicu intervala možemo održavati koristeći tehniku dva pokazivača. Vremenska složenost $O(n \log n + n)$. Napomena: Vektore možemo da sortiramo po uglu tako što prvo sortiramo vektore iznad $x$ ose po koeficijentu prave $(0,0),(x_i,y_i)$, a onda isto za vektore ispod $x$ ose. Može doći do greške u kodu ako ne izbacimo vektore oblika $(0,0)$ iz opticaja.
	
	
	``` cpp title="06_najvektor.cpp" linenums="1"
	#include <bits/stdc++.h>
	using namespace std;
	
	const int maxn = 300005;
	
	int n;
	long long x[maxn], y[maxn];
	int id[maxn];
	bool tu[maxn];
	long long xnew[maxn], ynew[maxn];
	int koj[maxn];
	vector<int> ids[maxn];
	
	bool gore(int i){
	    if(y[i] > 0) return false;
	    if(y[i] == 0 && x[i] > 0) return false;
	    return true;
	}
	
	long long cross(int i, int j){
	    return x[i] * y[j] - x[j] * y[i];
	}
	
	bool cmp(int i, int j){
	    if(gore(i) != gore(j)) return gore(i) < gore(j);
	    return cross(i, j) > 0;
	}
	
	int nxt(int i){
	    if(i == n) return 1;
	    return i + 1;
	}
	
	bool oke(int i, int r){
	    long long cr = cross(i, r);
	    return (cr > 0) || (cr == 0 && gore(i) == gore(r));
	}
	
	void tc(){
	    cin >> n;
	
	    long long cX = 0, cY = 0;
	    long long optans = 0;
	    int optl = -1, optr = -1;
	
	    int m = 0;
	    for(int i = 1; i <= n; i++){
	        long long A, B;
	        cin >> A >> B;
	        if(A == 0 && B == 0) continue;
	        ++m;
	        x[m] = A;
	        y[m] = B;
	        koj[m] = i;
	    }
	
	    n = m;
	    iota(id + 1, id + 1 + n, 1);
	    sort(id + 1, id + 1 + n, cmp);
	
	    m = 0;
	    int last = 1;
	    long long cx = x[id[1]];
	    long long cy = y[id[1]];
	    //sve vektore u istom pravcu pretvaramo u jedan
	    for(int i = 2; i <= n; i++){
	        if(cross(id[last], id[i]) == 0 && gore(id[last]) == gore(id[i])){
	            cx += x[id[i]];
	            cy += y[id[i]];
	        } else {
	            m++;
	            xnew[m] = cx;
	            ynew[m] = cy;
	            for(int k = last; k < i; k++){
	                ids[m].push_back(koj[id[k]]);
	            }
	            last = i;
	            cx = x[id[i]];
	            cy = y[id[i]];
	        }
	    }
	
	    m++;
	    xnew[m] = cx;
	    ynew[m] = cy;
	    for(int k = last; k <= n; k++){
	        ids[m].push_back(koj[id[k]]);
	    }
	
	    n = m;
	    for(int i = 1; i <= n; i++){
	        x[i] = xnew[i];
	        y[i] = ynew[i];
	    }
	
	    int r = 0;
	    optl = 1;
	    optr = n;
	    cX = 0;
	    cY = 0;
	
	    for(int i = 1; i <= n; i++){
	        //prava (0,0) (x_i,y_i)
	        while(!tu[nxt(r)] && oke(i, nxt(r))){
	            r = nxt(r);
	            tu[r] = true;
	            cX += x[r];
	            cY += y[r];
	            if(cX * cX + cY * cY > optans){
	                optans = cX * cX + cY * cY;
	                optl = i;
	                optr = r;
	            }
	        }
	
	        tu[i] = false;
	        cX -= x[i];
	        cY -= y[i];
	
	        if(cX * cX + cY * cY > optans){
	            optans = cX * cX + cY * cY;
	            optl = i + 1;
	            optr = r;
	        }
	    }
	
	    int i = optl;
	    vector<int> ans;
	
	    while(optl != -1){
	        for(int k : ids[i]) ans.push_back(k);
	        i = nxt(i);
	        if(i == nxt(optr)) break;
	    }
	
	    cout << ans.size() << '\n';
	    for(int v : ans) cout << v << " ";
	    cout << '\n';
	}
	
	int main(){
	    ios_base::sync_with_stdio(false);
	    cin.tie(nullptr);
	
	    int t = 1;
	    while(t--){
	        tc();
	    }
	    return 0;
	}

	```
