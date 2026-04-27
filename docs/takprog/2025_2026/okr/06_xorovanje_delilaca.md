---
hide:
  - toc
---

# A3 - Dunja, delioci i xor

=== "Zadatak"
	
	| Vremensko ograničenje | Memorijsko ograničenje |
	|:-:|:-:|
	| 1000ms | 256MB |
	
	Dok je bila u prirodi i posmatrala lisice, Dunja je naišla na bačen list papira na kome je zapisan broj $n$, a zatim $k$ različitih brojeva $d_1, d_2, \ldots, d_k$. Dunji su ovi brojevi izgledali interesantno, pa je pokušala da im pronađe značenje. Shvatila je da je skup brojeva $\{d_1, d_2, \ldots, d_k\}$ isti kao skup svih delilaca broja $n$. Drugim rečima, za svako $1 \le i \le k$ važi da $d_i$ deli $n$. Takođe važi da za svaki pozitivan ceo broj $x$ koji deli $n$ postoji jedinstven indeks $1 \le i \le k$ takav da $d_i = x$. 
	
	<br>
	
	Funkcija $\text{xor_delilaca} (x)$ je ekskluzivna disjunkcija svih delilaca broja $x$. Formalno, neka su brojevi $d_1, d_2, \ldots d_k$ svi delioci broja $x$. Onda je $\text{xor_delilaca} (x) = d_1\ \text{xor}\ d_2\ \text{xor}\ \ldots\ \text{xor}\ d_k$.
	
	<br>
	
	Dunja želi da nađe vrednosti funkcije $\text{xor_delilaca}$ za sve vrednosti $d_1, d_2, \ldots, d_k$. Kako je u prirodi i nije pored računara, a brojevi su veoma veliki, zamolila je Vas da joj pomognete.
	
	<br>
	
	## Opis ulaza
	
	<br>
	
	
	U prvoj liniji dva broja $n$ i $k$, broj $n$ iz teksta zadatka i broj delilaca broja $n$.
	
	<br>
	
	U drugoj liniji se nalazi $k$ brojeva, $d_1, d_2, \ldots, d_k$, svi delioci broja $n$. 
	
	<br>
	
	## Opis izlaza
	
	<br>
	
	U jednom redu izlaza je potrebno ispisati $k$ brojeva. $i$-ti od njih treba da ima vrednost $\text{xor_delilaca}(d_i)$.
	
	<br>
	
	## Primer 1
	
	<br>
	
	### Ulaz 1
	
	<br>
	
	```
	1 1
	1
	```
	
	<br>
	
	### Izlaz 1
	
	<br>
	
	```
	1
	```
	
	### Objašnjenje 1
	
	Jedini delilac broja $1$ je $1$. Samim time je $\text{xor_delilaca}(1) = 1$.
	
	<br>
	 
	## Primer 2
	
	<br>
	
	### Ulaz 2
	
	<br>
	
	```
	12 6
	12 1 3 6 2 4  
	```
	
	<br>
	
	### Izlaz 2
	
	<br>
	
	```
	14 1 2 6 3 7
	```
	
	### Objašnjenje 2
	
	Delioci broja $12$ su $1, 2, 3, 4, 6$ i $12$, tako da je $\text{xor_delilaca}(12) = 1\ \text{xor}\ 2\ \text{xor}\ 3\ \text{xor}\ 4\ \text{xor}\ 6\ \text{xor}\ 12 = 14$.
	
	Jedini delilac broja $1$ je $1$. Samim time je $\text{xor_delilaca}(1) = 1$.
	
	Delioci broja $3$ su $1$ i $3$, tako da je $\text{xor_delilaca}(3) = 1\ \text{xor}\ 3 = 2$.
	
	Delioci broja $6$ su $1, 2, 3$ i $6$, tako da je $\text{xor_delilaca}(6) = 1\ \text{xor}\ 2\ \text{xor}\ 3\ \text{xor}\ 6 = 6$.
	
	Delioci broja $2$ su $1$ i $2$, tako da je $\text{xor_delilaca}(2) = 1\ \text{xor}\ 2 = 3$.
	
	Delioci broja $4$ su $1, 2$ i $4$, tako da je $\text{xor_delilaca}(4) = 1\ \text{xor}\ 2\ \text{xor}\ 4 = 7$.
	
	<br>
	
	## Ograničenja
	
	
	<br>
	
	
	$1 \le n \le 10^{18}$
	
	$1 \le k \le 10^5$
	
	$1 \le d_i \le n$, za svako $1 \le i \le k$
	
	Skup brojeva $\{d_1, d_2, \ldots, d_k\}$ je isti kao skup svih delilaca broja $n$
	
	Svi brojevi $d_1, d_2, \ldots d_k$ su različiti
	
	<br>
	
	Test primeri su podeljeni u $5$ disjunktnih grupa:
	
	   
	   - U testovima vrednim $10$ poena: važi $n \le 1\ 000$
	   - U testovima vrednim $15$ poena: važi $n \leq 10^5$
	   - U testovima vrednim $15$ poena: važi $n \leq 10^7$
	   - U testovima vrednim $20$ poena: važi $n \le 10^9$
	   - U testovima vrednim $40$ poena: bez dodatnih ograničenja.
	
	<br>
	
	## Napomena
	
	<br>
	
	Operator ekskluzivne disjunkcije u Pascal-u je označen sa  `xor`, dok u C++ ga zapisujemo pomoću simbola  `^`. Ova operacija $x\ \text{xor} \ y$ se za nenegativne cele brojeve $x,y$ definiše na sledeći način. Prvo se brojevi zapišu u binarnom zapisu. Ukoliko jedan broj ima manje cifara od drugog, dopisuju mu se vodeće nule sve dok ne budu imali isti broj binarnih cifara. Tako se dobijaju dva niza binarnih cifara, označimo ih sa $a_1, \ldots, a_k$ i $b_1, \ldots b_k$. Zatim se za svaku poziciju $i \in {1, \ldots, k }$ računa $c_i$ pomoću sledećih pravila:
	
	-   Za $a_{i} = 0, b_{i} = 0$ važi $c_{i} = 0$
	-   Za $a_{i} = 0, b_{i} = 1$ važi $c_{i} = 1$
	-   Za $a_{i} = 1, b_{i} = 0$ važi $c_{i} = 1$
	-   Za $a_{i} = 1, b_{i} = 1$ važi $c_{i} = 0$
	
	Niz binarnih cifara $c_1, \ldots, c_k$ (koji možda ima vodeće nule) je binarni zapis rezultata, odnosno broja $x \ \text{xor} \ y$.
	
	
	Ekskluzivna disjunkcija je komutativna i asocijativna operacija. Odnosno, važi:
	
	- $a\ \text{xor} \ b\ =\ b\ \text{xor} \ a$
	- $(a\ \text{xor} \ b)\ \text{xor} \ c\ =\ a\ \text{xor} \ (b\ \text{xor}\ c)$
	
	<br> 
	
=== "Rešenje"
	
	| Autor | Tekst i test primeri | Analiza rešenja | Testiranje |
	|:-:|:-:|:-:|:-:|
	| Nemanja Majski | Nemanja Majski | Nemanja Majski | Aleksa Milisavljević |
	
	### $n \leq 1.000$
	
	Za svaki broj $x \in \{1, 2, \ldots, n\}$ ćemo da prođemo petljom od $1$ do $x$  kako bi našli sve njegove delioce i njihov xor. Te rezultate pamtimo u nizu. Sada da bi našli odgovor za bilo koji delilac možemo samo da ga pročitamo iz tog niza.
	
	Vremenska složenost je $O(n^2)$, a memorijska $O(n)$.
	
	### $n \leq 10^5$
	
	Recimo da tražimo sve delioce nekog broja $x$. Primetimo da ako broj $d$ deli broj $x$, onda i broj $\frac{x}{d}$ deli broj $x$. Takođe, za svaki delilac $d$ broja $x$ važi $d \le \sqrt{x}$ ili $\frac{x}{d} \le \sqrt{x}$. Samim time petlju kojom tražimo delioce možemo pustiti da iterira samo do $\sqrt{x}$, dok delioce veće od $\sqrt{x}$ nalazimo deljenjem broja $x$ sa deliocima manjim od $\sqrt{x}$. 
	
	Vremenska složenost je $O(n \sqrt{n})$, a memorijska $O(n)$.
	
	### $n \leq 10^7$
	
	Primetimo da je broj $x$ delilac brojeva $x, 2x, 3x \ldots$. Tako da kako bi našli delioce svih brojeva od $1$ do $n$ možemo ići redom kroz brojeve $i \in \{1, 2, \ldots, n\}$. Kada smo na broju $i$, mi ga dodamo brojevima $i, 2i, 3i \ldots$ kao delioca.  
	
	Takođe, nama nije važno koji su delioci nekog broja, već samo koliki je njihov xor. Zato je ideja da prvo napravimo niz $res$ gde će na početku biti $res_i = 0$ za svako $1 \le i \le n$. Zatim idemo redom kroz brojeve $1, 2, \ldots, n$. Kada smo na broju $i$, mi promenimo $res_j := res_j\ \text{xor}\ i$ za svako $j \in \{i, 2i, 3i\ldots\}$. 
	
	Na prvi pogled izgleda kao da je složenost opisanog algoritma dosta velika i da nije dovoljno brz. Ali, primetimo da za $i=x$ mi ćemo napraviti najviše $\frac{n}{x}$ koraka. To znači da mi ukupno pravimo najviše $\frac{n}{1}+\frac{n}{2}+\frac{n}{3}+\ldots+ \frac{n}{n}$ koraka. Može se dokazati da je $\frac{1}{1} +\frac{1}{2} +\frac{1}{3} +\ldots + \frac{1}{n} = O(log\ n)$ kad $n \to \infty$, pa je samim time vremenska složenost $O(n\ log\ n)$. 
	
	Memorijska složenost je $O(n)$.    
	
	### $n \leq 10^9$
	
	Primetimo da brojevi uglavnom imaju mnogo manje delilaca nego kolika je njihova vrednost. Odnosno, svi brojevi koji su manji ili jednaki $10^9$ imaju najviše $1344$ delilaca. Odnosno, to što je $n \le 10^9$ implicira i ograničenje $k \le 1344$. 
	
	Neka je $d$ delilac broja $n$. Očigledno je da su i svi njegovi delioci takođe delioci broja $n$. Tako da kako bismo našli za neki od delilaca broja $n$, neka je to broj $d$, koji su njegovi delioci, možemo proći kroz listu svih delilaca broja $n$ i proveriti da li dele broj $d$.
	
	Vremenska složenost je $O(k^2)$. Memorijska složenost je $O(k)$.
	
	### Bez dodatnih ograničenja
	
	Neka je $P$ broj prostih faktora broja $n$. Komisijsko rešenje je u složenosti $O(kP)$. Postoje i sporija rešenja koja vrede $100$ poena, ali predlažemo da probate smisliti rešenje u navedenoj složenosti.
	
	Neka je prosta faktorizacija broja $n = p_1^{\alpha_1} \cdot p_2^{\alpha_2} \cdot \ldots \cdot p_P^{\alpha_{P}$, gde su $\alpha_1, \alpha_2, \ldots, \alpha_P$ nenegativni celi brojevi, a $p_1, p_2, \ldots, p_P$ međusobno različiti prosti brojevi. Poznato je da je skup delioca broja $n$ isti kao skup svih brojeva oblika $p_1^{\beta_1} \cdot p_2^{\beta_2} \cdot \ldots \cdot p_P^{\beta_{P}}$, gde je $0 \le \beta_i \le \alpha_i$ za svako $1 \le i \le P$.
	
	Napravimo matricu $M$ dimenzija $\alpha_1 \times \alpha_2 \times \ldots \times \alpha_P$. Broju $p_1^{\beta_1} \cdot p_2^{\beta_2} \cdot \ldots \cdot p_P^{\beta_{P}}$, koji je delilac broja $n$, ćemo pridružiti polje $M_{\beta_1, \beta_2, \ldots, \beta_P}$ i tom polju ćemo dodeliti vrednost $p_1^{\beta_1} \cdot p_2^{\beta_2} \cdot \ldots \cdot p_P^{\beta_{P}}$. 
	
	Takođe ćemo napraviti matricu $res$ istih dimenzija, i brojevima pridružiti ista polja. Polje $res_{\beta_1, \beta_2, \ldots, \beta_P}$ će imati vrednost funkcije xor nad svim poljima $m_{i_1, i_2, \ldots, i_P}$ za koja važi $0 \le i_j \le \beta_j$ za svako $1 \le j \le P$. Primetiti da je rešenje zadatka za broj $d$ vrednost polja u matrici $res$ kojem je taj broj pridružen. Takođe, primetiti da je matrica $res$ matrica prefiksnog xor-a matrice $M$.
	
	Sada je problem kako brzo da izračunamo prefiksni xor matrice $m$. U standardnom načinu računanja prefiksnim xor-ova matrice, za matricu sa $S$ polja i $d$ dimenzija nam treba $O(S \cdot 2^d)$ vremena. To je previše sporo za ovaj zadatak. 
	
	Pokazaćemo kako da u dva prolaza kroz matricu izračunamo ovaj prefiksni xor za dvodimenzionalne matrice. Analogno se radi za matrice proizvoljnih dimenzija u $O(S \cdot d)$, gde je $S$ ukupna veličina matrice, a $d$ broj dimenzija matrice.
	
	Neka je $M$ matrica $n \times m$ kojoj želimo da nađemo prefiksni xor. Prvo, za svaki red $1 \le i \le n$ nađemo njegov prefiksni xor. Neka je matrica $M'$ takva da je $M_{i,j}' = M_{i, 1}\ \text{xor}\ M_{i,2}\ \text{xor}\ \ldots\ \text{xor}\ M_{i,j}$.
	
	Zatim, prolazimo kroz matricu $res$ tako da posećujemo polja redom $(1, 1), (1, 2),$ $\ldots, (1,m), (2, 1), (2,2),$ $\ldots, (2,m), (3,1),$ $\ldots (n, 1), (n,2), \ldots, (n,m)$ (ovo je najobičniji prolaz kroz matricu dvostrukom petljom). Dok radimo ovaj prolaz računamo vrednosti matrice $res$.
	
	Kada smo na polju $(i,j)$, važi: $$res_{i,j} = res_{i-1,j}\ \text{xor}\ M'_{i,j}$$.
	
	Zašto? Vrednost levo od operatora $\text{xor}$ predstavlja xor svih vrednosti u poljima $(i,j)$ za $1 \le i' < i, 1 \le j' \le j$, dok je vrednost desno od operatora $\text{xor}$ vrednost $M_{i,1}\ \text{xor}\ M_{i,2}\ \text{xor}\ M_{i,j}$. Očigledno je da oni zajedno predstavljaju xor svih polja $(i',j')$ matrice $M$ za koje važi $1 \le i' \le i, 1\le j' \le j$. 
	
	Na sličan način možemo da pređemo sa dve na tri dimenzije, pa sa tri na četiri i nadalje.
	
	Kako su polja matrice zapravo delioci broja $n$, to mnogo olakšava implementaciju. Pogledajte komisijsko rešenje.
	
	Vremenska složenost je $O(kp)$, dok je memorijska složenost $O(k)$.
	
	``` cpp title="06_xorovanje_delilaca.cpp" linenums="1"
	#include<bits/stdc++.h>
	#define ll long long
	using namespace std;
	ll n,m;
	int main(){
	    cin>>n>>m;
	    vector<ll> divs,org;
	    for(ll i=1;i<=m;i++){
	        ll x;
	        cin>>x;
	        org.push_back(x);
	    }
	    divs=org;
	    sort(divs.begin(),divs.end());
	    vector<ll> factors;
	    for(ll d:divs){
	        if(n%d==0 and d!=1){
	            factors.push_back(d);
	            while(n%d==0)
	                n/=d;
	        }
	    }
	    map<ll,ll> res;
	    for(auto d:divs)
	        res[d]=d;
	    for(ll p:factors)
	        for(ll x:divs)
	            res[x*p]^=res[x];
	    for(ll x:org)
	        cout<<res[x]<<" ";
	    return 0;
	}

	```
