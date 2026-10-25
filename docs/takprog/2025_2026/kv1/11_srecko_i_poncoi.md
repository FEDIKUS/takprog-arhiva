---
hide:
  - toc
---

# 11 - Srećko i pončoi

=== "Zadatak"
	
	| Vremensko ograničenje | Memorijsko ograničenje |
	|:-:|:-:|
	| 1000ms | 512MB |
	
	<br> Srećko mnogo voli pončoe i želi da ih donese nazad kući u Kigali. Dato je $n$ pončoa u ponudi i Srećko može za svaki pončo da izabere da li će ga kupiti. Pončo sa rednim brojem $i$ je težak $w_i$ i vredi $v_i$. Nažalost, količina pončoa koje Srećko može da ponese je ograničena. Preciznije, maksimalna ukupna težina svih pončoa koje on može da kupi je $W$. Pomozite Srećku da izabere koje pončoe da kupi tako da je zbir vrednosti pončoa koje je kupio maksimalan. 
	
	<br> 
	
	S obzirom da je ovaj problem veoma težak, **nije potrebno da nađete izbor koji donosi najveću sumu vrednosti izabranih pončoa**. Preciznije, u svakom test primeru biće Vam dat realan broj $\epsilon$. Neka je $opt$ najveća moguća ukupna vrednost pončoa koje Srećko može da ponese, a neka je $x$ ukupna vrednost pončoa koju ste Vi našli. Poene za dati test primer dobijate samo ako $x \ge (1 - \epsilon) \cdot opt$. <br> 
	
	## Opis ulaza
	U prvoj liniji standardnog ulaza se nalaze dva cela i jedan realan broj $N$, broj pončoa u ponudi, $W$, maksimalna ukupna težina pončoa koje Srećko kupuje, i broj $\epsilon$, zaokrugljen na dve decimala. U $i$-toj od narednih $N$ linija su data dva broja, $w_i$ i $v_i$, koji predstavljaju težinu i vrednost pončoa $i$.
	## Opis izlaza
	U prvoj liniji treba ispisati ceo broj $k$, broj pončoa koje će Srećko kupiti. U drugoj liniji je potrebno ispisati $k$ različitih brojeva koji označavaju indekse pončoa koje će Srećko da kupi.
	## Primer 1
	### Ulaz
	 ``` 
	4 10 0.20
	4 2
	6 5
	3 10
	7 4
	```   
	### Izlaz  
	 ``` 
	2
	3 4 
	 ```  
	### Objašnjenje primera
	U primeru Srećku je optimalno da uzme pončoe $2$ i $3$ koji zajedno imaju vrendost $15$, a težinu $9$. U izlazu su uzeti pončoi $3$ i $4$ koji imaju vednost $14$, a težinu $10$. Pošto je $\epsilon = 0.2$, a $15 \cdot (1-0.2) = 12 \leq 14$, za ovo rešenje biste dobili poene. Dok, na primer, izbor pončoa $1$, $2$ i $3$ nije moguć, pošto je njihova ukupna težina $4 + 6 + 3 = 13 > W = 10$.
	## Ograničenja
	
	-   $1 \leq N \leq 300$
	-   $1 \leq w_i,v_i,W \leq 10^9$
	- $\epsilon \in \{0.01, 0.1, 0.2, 0.5\}$
	
	Test primeri su podeljeni u $5$ disjunktnih grupa:
	 - U testovima vrednim $20$ poena: $n \leq 40$, $\epsilon = 0.01$.
	 - U testovima vrednim $10$ poena: $n \leq 60, \epsilon = 0.5$
	 - U testovima vrednim $20$ poena: $n \leq 60, \epsilon = 0.2$
	 - U testovima vrednim $10$ poena: $n \leq 100, \epsilon = 0.1$
	 - U testovima vrednim $40$ poena: $\epsilon = 0.01$ 
	
=== "Rešenje"
	
	| Autor | Tekst i test primeri | Analiza rešenja | Testiranje |
	|:-:|:-:|:-:|:-:|
	| Uroš Kostadinović | Uroš Kostadinović | Uroš Kostadinović | Nemanja Majski |
	
	## Rešenje kada je $N \leq 40, \epsilon = 0.01$
	U ovom podzadatku je moguće naći optimalno rešenje za Srećka. Klasično rešenje za problem ranca bi bilo složenosti $O(nW)$ , a isprobavanje svih mogućnosti za uzimanje pončoa bi bilo složenosti $O(2^n)$, što je za ograničenja presporo. Drugo rešenje bi bilo dovoljno dobro da je $n \leq 20$. Možemo da podelimo pončoe u dve grupe tako da je veličina svake manja ili jednaka od $\frac{n+1}{2}$ i na njima iskoristimo drugo rešenje. Sada smo generisali sve mogućnosti ako svi uzeti pončoi pripadaju istoj grupi i ostalo je da proverimo za rešenja gde pončoi pripadaju u obe grupe. Fiksirajmo koje smo pončoe uzeli iz prve grupe i neka je njihova težina $W_1$. Onda ćemo iz druge grupe uzeti pončoe težine maksimalno $W-W_1$ sa najvećom vrednošću. Tu vrednost možemo naći koristeći tehniku dva pokazivača. Sortirajmo mogućnosti iz prve grupe i mogućnosti iz druge grupe (odvojeno) po težini. Fiksiraćemo grupu pončoa koje pončoe uzimamo iz prve grupe opadajući po težini i redom ćemo dodavati mogućnosti iz.
	Vremenska složenost $O(2^{\frac{n}{2}}n)$
	
	## Rešenje kada $\epsilon = 0.5$.
	
	U verziji zadatka u kojoj možemo da uzmemo bilo koji realan deo nekog pončoa optimalno je da sortiramo pončoe po odnosu cene i težine i onda uzimamo svaki sledeći na redu ukoliko možemo. Na ovaj način samo jedan od pončoa koje smo uzeli neće biti ceo. Neka je $opt_{greedy}$ vrednost koju dobijemo na ovaj način ne računajući deo ne-celog pončoa. Neka je  $V_k$ pončo čiji bismo deo uzeli u drugoj verziji zadatka. Znamo da je $opt_greedy + V_k \geq opt$. Neka je $V_{max}$ najveća vrednost nekog pončoa, onda je $opt_{greedy}+V_{max} \geq opt$ pa je $max(opt_{greedy},V_{max}) \geq \frac{opt}{2}$. Uzećemo    bolju od ove dve opcije i ona će garantovano biti barem $(1-\epsilon)opt$. Vremenska složenost $O(n log n)$
	
	## Rešenje kada je $n \leq 60,\epsilon = 0.2$
	U optimalnom rešenju ćemo koristiti manje od $\frac{1}{\epsilon}$ pončoa veličine veće ili jednake od $\epsilon \cdot opt$. Možemo da prođemo kroz sve mogućnosti za te pončoe kojih ima $O(n^{\frac{1}{\epsilon}})$. Ostale elemente ćemo imati već sortirane i na isti gramziv način ćemo ih uzimati kao i u prethodnom podzadatku. Sada je razlika u tome što će pončo čiji bismo uzeli realan deo bio vrednosti maksimalno $\epsilon \cdot opt$, pa je $ans + \epsilon \cdot opt \geq opt$ tj. $ans \geq (1-\epsilon) opt$ što znači da rešenje koje smo našli odgovara. Vremenska složenost:  $O(n^{\frac{1}{\epsilon}})$
	
	## Rešenje za 100 bodova
	Umesto da primenimo klasičan problem ranca na prave vrednosti možemo da ih skaliramo po ceni gubljenja preciznosti. Neka je nova vrednosti ponča $i$ jednaka $v'_i = \lfloor \frac{v_i}{\frac{\epsilon}{n}v_{max}} \rfloor$. Primenićemo klasičan problem ranca tako što ćemo izračunati za svaki mogući zbir vrednost koja je minimalna težina skupa pončoa koji imaju tu vrednost. Za svaki pončo zanemarujemo deo njegove vrednosti koji je najviše $\frac{\epsilon}{n}v_{max}$, a pošto uzimamo maksimalno $n$ pončoa maksimalno smo zanemarili $n \frac{\epsilon}{n}v_{max} = \epsilon v_{max}$, pa je $ans+ \epsilon v_{max} \geq opt$, gde je $ans$ rešenje koje smo našli računato sa novim vrednostima pončoa. Pošto je $v_{max} \leq opt$ onda je i $ans+ \epsilon opt \geq opt$ pa je $ans \geq (1-\epsilon)opt$, što znači da rešenje koje smo našli odgovara. Nove vrednosti pončoa će biti između $0$ i $\frac{n}{\epsilon}$ pa će vremenska i memorijska složenost biti $O(\frac{n^3}{\epsilon})$.  
	
	
	``` cpp title="11_srecko_i_poncoi.cpp" linenums="1"
	#include <bits/stdc++.h>
	using namespace std;
	
	const int maxn = 305;
	const int maxs = 300000;
	const int inf = 1000000001;
	int n;
	int W;
	double eps;
	int w[maxn],v[maxn];
	int vs[maxn];
	int dp[maxn][maxs];
	bool uzo[maxn][maxs];
	int main() {
	    ios::sync_with_stdio(false);
	    cin.tie(nullptr);
	
	    cin >> n >> W >> eps;
	    for(int i = 1;i<=n;i++) cin >> w[i] >> v[i];
	
	    int vmax = 0;
	    for(int i = 1;i<=n;i++) vmax = max(vmax,v[i]);
	    //skaliranje
	    double sk = (eps * vmax) / n;
	    int vsum = 0;
	    for (int i = 1;i<=n;i++) {
	        vs[i] = (int)floor(v[i] / sk);
	        vsum+=vs[i];
	    }
	    for(int i = 0;i<=n;i++){
	        for(int s = 0;s<=vsum;s++) dp[i][s] = inf;
	    }
	    dp[0][0] = 0;
	    for (int i = 1;i<=n;i++) {
	        for (int s = 0;s<=vsum;s++) {
	            dp[i][s] = dp[i-1][s];
	            if(s>=vs[i]){
	                if(dp[i-1][s-vs[i]]+w[i]<dp[i][s]){
	                    dp[i][s] = dp[i-1][s-vs[i]]+w[i];
	                    uzo[i][s] = 1;
	                }
	            }
	        }
	    }
	    vector<int> ans;
	    int sopt = 0;
	    for (int s = 0;s<=vsum;s++){
	        if (dp[n][s]<=W) sopt = s;
	    }
	    int i = n;
	    while(i>0){
	        if(uzo[i][sopt]){
	            ans.push_back(i);
	            sopt-=vs[i];
	        }
	        i--;
	    }
	    cout<<ans.size()<<'\n';
	    for(int i : ans) cout<<i<< " ";
	    cout<<'\n';
	    return 0;
	}

	```
