---
hide:
  - toc
---

# 1 - Uzumaki

=== "Zadatak"
	
	| Vremensko ograničenje | Memorijsko ograničenje |
	|:-:|:-:|
	| 4000ms | 256MB |
	
	
	Oh, ne! Na putu do izbornog takmičenja vas je napao legendarni nindža koji nosi kletvu devetorepe licice. Kako on voli ljubav i mrzi mržnju, odlučio je da vas ni pod kojim uslovom ne sme pustiti da učestvujete na predstojećem takmičenju. Zato je iskoristio svoju tajnu tehniku klonova senke kako bi pokrio sve moguće rute za beg.
	
	<br>
	
	Klonovi legendarnog nindže formiraju niz od $N$ elemenata. Zbog kompleksnosti kontrolisanja čakre, on nije uspeo da napravi savršene klonove sebe,  već $i$-ti klon ima moć $A_i$. Da bi zbunio protivnika on je odlučio da promeša svoje klonove u $Q$ operacija tri tipa:
	
	- Da promeša klonove od pozicije $L$ do pozicije $R$ tako da budu sortirani po snazi rastuće.
	- Da promeša klonove od pozicije $L$ do pozicije $R$ tako da budu sortirani po snazi opadajuće
	- Da promeša klonove od pozicije $L$ do pozicije $R$ tako da budu u tzv. Uzumaki (うずまき) poretku. Kažemo da je niz $B[1], B[2],\ldots B[t]$ u Uzumaki poretku ukoliko je $B[1]$ najmanji element niza, i niz $B[t], B[t-1],\ldots,B[2]$ je u Uzumaki poretku.
	
	<br>
	Međutim, zbog nove lokacije ovogodišnjeg takmičenja vaš nindža protivnik ne zna tačno gde se ono održava, ali vi znate. Poznato je da morate da porazite klona na poziciji $K$ da biste stigli do željene lokacije. Vaš zadatak je da odredite, nakon svih mešanja klonova, kolika je snaga klona na poziciji $K$.
	
	## Opisi funkcija
	
	Potrebno je da implementirate funkciju
	
	-   $Vrednost(N, A[\ldots], Q, T[\ldots],L[\ldots],R[\ldots],K)$
	
	Ova funkcija će biti pozvana jednom po primeru. Broj $N$ predstavnja broj klonova, dok niz $A$ predstavlja jačinu klonova u početnom nizu. Broj $Q$ označava broj mešanja koji će klonovi da izvrše. Nizovi $T,L,R$ opisuju te operacije na sledeći način: 
	- Ukoliko je $T[i]=1$ podniz od $L$ do $R$ se sortira rastuće.
	- Ukoliko je $T[i]=2$ podniz od $L$ do $R$ se sortira opadajuće.
	- Ukoliko je $T[i]=3$ podniz od $L$ do $R$ se sortira u Uzumaki poretku.
	Konačno broj $K$ označava indeks klona koga treba da porazite na kraju, odnosno čiju vrednost treba da nađete.
	   **Svi nizovi su indeksirani od 1.**
	
	## Primer
	
	Neka je $N=5$, $Q=2$,  $A=\{2,4,3,1,5\}$, $T=\{2,3\}$, $L=\{1,3\}$, $R=\{3,5\}$. Posle prve operacije ćemo prva tri elementa sortirati opadajuće, pa će niz biti $\{4,3,2,1,5\}$. Zatim ćemo poslednja tri elementa sortirati u Uzumaki redosledu i dobiti niz $\{4,3,1,5,2\}$. Stoga, ako je na primer, $K=4$ funkcija treba da vrati vrednost $5$.
	## Ograničenja
	
	-   $1 \leq N,Q \leq 100.000$
	-   $1 \leq A[i] \leq 1.000.000$
	-   $1 \leq L[i]\leq R[i] \leq N$
	-   $1 \leq T[i] \leq 3$
	-   $1 \leq K \leq N$
	
	## Podzadaci
	
	Test primeri su podeljeni u $7$ podzadatka:
	
	-   **[5 poena]:** $N,Q\le5000$, $T[i]\in\{1,2\}$
	-   **[5 poena]:** $N,Q\le5000$, $T[i] = 1$
	-   **[12 poena]:** $N,Q\le5000$
	-   **[8 poena]:** $T[i] = K = 1$
	-   **[13 poena]:** $A[i]\leq 10$, $T[i]\in\{1,2\}$
	-   **[14 poena]:** $A[i]\leq 10$
	-   **[20 poena]:** $T[i]\in\{1,2\}$
	-   **[23 poena]:** Nema dodatnih ograničenja
	
	## Detalji implementacije
	
	Potrebno je da pošaljete tačno jedan fajl  `uzumaki.cpp`  koji implementira pomenute funkcije. Osim traženih funkcija, vaš fajl može sadržati i dodatne globalne promenljive, pomoćne funkcije i dodatne biblioteke.
	
	Vaša funkcija mora biti sledećeg oblika:
	
	`int Vrednost(int N, int* A, int Q, int* T, int* L, int* R,int K);`
	
	**Vašim programima je dozvoljeno da menjaju sadržaj nizova ali ne smeju da pristupaju van granica datih nizova.**
	
	Uz zadatak, obezbeđen vam je "template" fajl  `code.cpp`  koji možete koristiti i menjati po potrebi. Takođe vam je obezbeđen program  `grader.cpp`  koji služi da lakše testirate kodove. Ovaj program učitava sa standardnog ulaza sledeće podatke:
	
	-   U prvom redu broj $N$.
	-   U narednom redu $N$ brojeva: $A[i]$.
	-   U narednom redu broj $Q$.
	-   U narednih $Q$ redova po tri broja: $T[i], L[i], R[i]$.
	-   U poslednjem redu broj $K$.
	
	Zatim ovaj program zove vašu funkciju i ispisuje rezultat koji vaša funkcija vrati.
	
	
=== "Rešenje"
	
	| Autor | Tekst i test primeri | Analiza rešenja | Testiranje |
	|:-:|:-:|:-:|:-:|
	| Pavle Martinović | Pavle Martinović | Mladen Puzić | Aleksa Milisavljević |
	
	## Prvi podzadatak
	U ovom podzadatku možemo simulirati mešanje klonova i na kraju ispisati moć klona na poziciji $K$.
	
	Za svaku operaciju, podniz klonova možemo sortirati rastuće bilo kojim efikasnim algoritmom sortiranja (složenosti $N\log N$).
	
	Vremenska složenost: $O(QN\log N)$
	Memorijska složenost: $O(N)$
	
	## Drugi podzadatak
	Slično kao prethodni podzadatak, samo za operaciju drugog tipa podniz moramo sortirati u opadajućem poretku.
	
	Vremenska složenost: $O(QN\log N)$
	Memorijska složenost: $O(N)$
	
	## Treći podzadatak
	Potrebno je primetiti da je niz u Uzumaki poretku ako i samo ako je ,,spiralno sortiran'', odnosno, da je najmanji element na prvoj poziciji, drugi najmanji na poslednjoj poziciji, treći najmanji na drugoj poziciji, četvrti najmanji na pretposlednjoj poziciji, itd.
	
	Nakon toga, slično kao prethodni podzadatak, samo za operaciju trećeg tipa možemo podniz kopirati u novi niz, sortirati rastuće, i onda poređati nazad u originalni niz u Uzumaki poretku.
	
	Vremenska složenost: $O(QN\log N)$
	Memorijska složenost: $O(N)$
	
	## Četvrti podzadatak
	Rešenje će biti najmanji element koji se nalazi u poslednjem intervalu koji sadrži prvi element (u trenutku te operacije). Onda su u opticaju svi elementi koji su na početku niza u tom intervalu, ali i svi elementi koji prethodnim operacijama završe u tom intervalu. Nazovimo ovaj interval $x_1$. 
	 
	Idemo unazad po operacijama od ovog intervala i nađimo prvi sledeći koji se seče sa intervalom $x_1$ (nazovimo ga $x_2$). Sada znamo da rešenje može biti i bilo šta iz unije $x_1 \cup x_2$, u trenutku operacije (pošto će najmanji element iz $x_2$ završiti u intervalu $x_1$ nakon operacije). Nastavljamo dalje i u uniju dodajemo sve intervale koji se seku sa dosadašnjom unijom.
	
	Na kraju ćemo imati uniju svih tih intervala, koja će predstavljati prefiks niza - odakle je najmanji broj rešenje zadatka.
	
	Vremenska složenost: $O(N + Q)$
	Memorijska složenost: $O(N + Q)$
	
	Alternativno rešenje: možemo primetiti da u bilo kom intervalu, samo najmanji element na tom intervalu ima potencijal da bude rešenje. Takođe, pošto je $t_i = 1$, rešenje će se uvek pomerati na levo. 
	
	Zbog toga, dovoljno je da za svaki interval efikasno nađemo najmanji element, i postavimo ga na prvu poziciju u tom intervalu. Na kraju, rešenje će se nalaziti na prvoj poziciji u nizu. Za ovo možemo koristiti segmentno stablo.
	
	Vremenska složenost: $O(Q\log N + N)$
	Memorijska složenost: $O(N)$
	
	## Peti podzadatak
	Pošto je $A_i$ malo, ima smisla da razmišljamo o sortiranju brojanjem (*counting sort*) - ako imamo cnt_i pojavljivanja broja $i$ u nekom intervalu i želimo da ga sortiramo rastuće, na prvih $cnt_1$ pozicija intervala postavićemo $1$, na sledećih $cnt_2$ pozicija $2$, itd. Za sortiranje opadajuće bismo samo išli obrnutim redosledom.
	
	Dakle, potrebno nam je da efikasno brojimo sve elemente na intervalu, i da ih postavljamo na uzastopne pozicije. Ovo možemo uraditi čuvanjem segmentnog stabla sa lenjom propagacijom za svaku moguću vrednost. U segmentnom stablu za neku vrednost, na pozicijama gde se nalazi ta vrednost potrebno je da se nalazi $1$, u suprotnom $0$. 
	
	Nalaženje broja pojavljivanja nekog elementa se radi zbirom na intervalu, dok se postavljanje radi lenjom propagacijom - prvo postavljanjem celog niza na nule, pa postavljanjem potrebnog intervala na jedinice.
	
	Vremenska složenost: $O(QA_i\log N + N)$
	Memorijska složenost: $O(A_iN)$
	
	## Šesti podzadatak
	Prva dva tipa operacija izvršavaćemo na isti način kao u prethodnom podzadatku - potrebno je dodatno analizirati kako efikasno postavljati elemente po Uzumaki poretku.
	
	Ukoliko je $cnt_1$ parno, prvu polovinu jedinica ćemo staviti na početak, a drugu polovinu na kraj intervala. Ukoliko je neparno, jedinicu viška stavićemo na početak.
	
	Ukoliko je $cnt_2$ parno, opet ćemo prvu polovinu dvojki staviti na početak preostalog niza, a ostatak na kraj. Ukoliko je neparno, ovaj put je nešto komplikovanije. Ukoliko smo do sad (za sve prethodne vrednosti) stavili jednako elemenata na početak i kraj niza, onda će višak element ići na početak. U suprotnom, višak element ide na kraj preostalog dela intervala.
	
	Ovakav proces nastavljamo dok ne popunimo niz.
	
	Vremenska složenost: $O(QA_i\log N + N)$
	Memorijska složenost: $O(A_iN)$
	
	## Sedmi podzadatak
	U prethodna dva podzadatka smo uspeli da generišemo ceo niz na kraju, dok ćemo ovde koristiti činjenicu da nam je potrebno da nađemo samo element na poziciji $K$.
	
	Umesto da tražimo konkretnu vrednost na toj poziciji, pokušajmo da proverimo da li će ta vrednost biti $\geq x$ za proizvoljno $x$. Sve elemente niza koji su manji od $x$ zamenimo nulama, a ostale jedinicama. Sada, ukoliko se na kraju svih operacija na poziciji $K$ nađe jedinica, onda će krajnja vrednost biti veća ili jednaka $x$. Ovo možemo proveriti primenom prethodnog podzadatka sa dve vrednosti (a čak nam je dovoljno samo jedno segmentno stablo).
	
	Sada kada možemo ovo efikasno proveriti, možemo koristiti binarnu pretragu po rešenju kako bismo našli pravu vrednost odgovora.
	
	Vremenska složenost: $O(Q\log N\log A_i + N)$
	Memorijska složenost: $O(N + Q)$
	
	## Rešenje za 100 bodova
	Kombinujemo rešenja prethodna dva podzadatka kako bismo omogućili sva tri tipa operacija.
	
	Vremenska složenost: $O(Q\log N\log A_i + N)$
	Memorijska složenost: $O(N + Q)$
	
	Alternativno rešenje: umesto segmentog stabla možemo podeliti niz na intervale nula i jedinica i održavati skup tih intervala. Svakom operacijom se broj intervala povećava za najviše 3, dok se može značajno smanjiti. Zato će ukupan broj promena ovih intervala biti $O(N + Q)$.
	
	Vremenska složenost: $O((N + Q)\log N\log A_i)$
	Memorijska složenost: $O(N + Q)$
	
	``` cpp title="01_uzumaki.cpp" linenums="1"
	#include <bits/stdc++.h>
	#define MAXN 100007
	using namespace std;
	int seg[4*MAXN], bag[4*MAXN];
	void relax(int ind, int l, int r) {
	    if(bag[ind] == -1) return;
	    seg[ind] = (r-l+1)*bag[ind];
	    if(l != r) {
	        bag[2*ind] = bag[ind];
	        bag[2*ind + 1] = bag[ind];
	    }
	    bag[ind] = -1;
	}
	inline int value(int ind,int l,int r) {
	    if(bag[ind] != -1) return (r-l+1)*bag[ind];
	    return seg[ind];
	}
	int sum(int ind, int l, int r, int lt, int rt) {
	    if(l >= lt && r <= rt) return value(ind,l,r);
	    if(r < lt || l > rt) return 0;
	    relax(ind,l,r);
	    int s = (l+r)/2;
	    return sum(2*ind,l,s,lt,rt) + sum(2*ind + 1,s + 1,r,lt,rt);
	}
	void put(int ind, int l, int r, int val, int lt, int rt) {
	    if(l >= lt && r <= rt) {
	        bag[ind] = val;
	        return;
	    }
	    if(r < lt || l > rt) return;
	    relax(ind,l,r);
	    int s = (l+r)/2;
	    put(2*ind,l,s,val,lt,rt);
	    put(2*ind + 1,s + 1,r,val,lt,rt);
	    seg[ind] = value(2*ind,l,s) + value(2*ind+1,s+1,r);
	}
	int Vrednost(int N,int *A,int Q,int *T,int *L,int *R,int K) {
	    int l = 1, r = 1000000;
	    while(l != r) {
	        int s = (l+r+1)/2;
	        put(1,1,N,0,1,N);
	        for(int i = 1; i <= N; i++) if(A[i] >= s) put(1,1,N,1,i,i);
	        for(int i = 1;i <= Q; i++) {
	            int k = sum(1,1,N,L[i],R[i]);
	            if(k == R[i] - L[i] + 1 || k == 0) continue;
	            if(T[i] == 1) {
	                put(1,1,N,0,L[i], R[i] - k);
	                put(1,1,N,1,R[i] - k + 1, R[i]);
	            }
	            if(T[i] == 2) {
	                put(1,1,N,1,L[i], L[i] + k - 1);
	                put(1,1,N,0,L[i] + k, R[i]);
	            }
	            if(T[i] == 3) {
	                int t = R[i] - L[i] + 1 - k;
	                put(1,1,N,0,L[i],L[i] + (t+1)/2 - 1);
	                put(1,1,N,1,L[i] + (t+1)/2,R[i] - t/2);
	                put(1,1,N,0,R[i] - t/2 + 1,R[i]);
	            }
	        }
	        if(sum(1,1,N,K,K)) l = s;
	        else r = s - 1;
	    }
	    return l;
	}

	```
