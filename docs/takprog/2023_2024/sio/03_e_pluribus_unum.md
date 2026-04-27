---
hide:
  - toc
---

# 3 - E pluribus unum

=== "Zadatak"
	
	| Vremensko ograničenje | Memorijsko ograničenje |
	|:-:|:-:|
	| 1000ms | 256MB |
	
	Na II Bakterijadi koja se ove godine održava u gradu Meseca okupilo se $N$ bakterija. One su poznate po pristojnom ponašanju, vrednom radu i nekonzumiranju antibiotika. Sam događaj je savršena prilika da se najbolje bakterije u Rimskom carstvu združe i podele iskustva. Među njima uspostavljeno je $M$ parova susedstva (koja su po prirodi dvosmerna).
	
	<br>
	
	Na početku nultog dana (indeksiramo od nule jer među ovim bakterijama ima i programera), $i$-ta bakterija (indeksiramo od $1$ do $N$ jer među njima ima i matematičara) ima veličinu $S_i$. Tačno $N-1$ njih se hrani autotrofno, a jedna je miksotrof. Na kraju dana, svi autotrofi porastu sa $1$ (promene se akumuliraju). Miksotrof pre početka svakog dana ima dva izbora - da bude u autotrofnoj ili heterotrofnoj formi. Ako je u autotrofnoj formi, na kraju dana se i njegova veličina poveća za $1$. Ako izabere heterotrofnu formu, onda može pojesti proizvoljan broj suseda, ali sa uslovom. Neka je bakterija $i$ miksotrof u autotrofnoj formi i $j$ njen sused. $S_i$ može pojesti $S_j$ ako i samo ako $S_i \geq S_j$ (čudno bi bilo da manja bakterija pojede veću). Tada se bakteriji $i$ veličina menja sa $S_i$ na $S_i + S_j$. Dodatno, $j$ nestaje, a susedi od $j$ sada postaju susedi od $i$ (s tim da bakterija nije susedna samoj sebi). Napominjemo da u jednom danu miksotrof u heterotrofnoj formi može pojesti proizvoljan broj suseda (i starih i novih) dokle god mu veličina to dozvoljava. Moguće je da pojede i suseda kog na početku dana nije smeo, a da je u međuvremenu dovoljno narastao. Tek na kraju dana sve autotrofne bakterije narastu (i miksotrof ako je bio u toj formi - heterotrofi ne rastu). Pojedeni autotrofi ne mogu narasti.
	
	
	<br>
	
	Za datog miksotrofa, potrebno je odrediti prvi dan u kome može pojesti sve ostale bakterije ako svoje forme i jedenje suseda bira optimalno. Kako miksotrof nije poznat, na pitanje je potrebno odgovoriti za svaku bakteriju $i$ ($1 \leq i \leq N$).
	
	## Opisi funkcija
	
	Potrebno je da implementirate funkciju
	
	-   $OdrediVreme(N, M, S[\ldots],U[\ldots],V[\ldots],T[\ldots])$
	
	Ova funkcija će biti pozvana jednom po primeru. Brojevi $N$ i $M$ predstavljaju broj bakterija i broj susedstva. Niz $S$ je dužine $N$ i predstavlja veličinu svake bakterije na početku nultog dana. Nizovi $U$ i $V$ dužine $M$ predstavljaju parove susedstva. Za $i$ ($1 \leq i \leq M$), kažemo da su bakterije $U_i$ i $V_i$ susedne. Garantuje se da nijedan par nije naveden više od jednom, kao i da postoji lista poznanstava koja povezuje svake dve bakterije. Niz $T$ je dužine $N$, a vaš odgovor na pitanje iz teksta zadatka za $i$-tu bakteriju treba da upišete u $T[i]$. Tačnije, kada bi $i$-ta bakterija bila miksotrof, potrebno je odrediti prvi dan u kome može pojesti sve ostale bakterije. Ukoliko to nije moguće učiniti u konačno mnogo dana, upisati $-1$.
	   **Svi nizovi su indeksirani od 1.**
	   **Dani su indeksirani od 0.**
	 
	## Primer
	
	Neka je $N=5$, $M=4$,  $S=\{1,1,7,10,10\}$, $U=\{1,2,3,3\}$, $V=\{2,3,4,5\}$. U niz $T$ je potrebno upisati $\{5,5,1,0,0\}$. Razmotrimo slučaj kada je treća bakterija miksotrof. U nultom danu, ona bira autotrofnu formu. Tada veličine bakterija postaju $S=\{2,2,8,11,11\}$. Na početku prvog dana, miksotrof bira heterotrofnu formu. Najpre, pojede bakteriju $2$. Time veličina miksotrofa postaje $10$ i bakterija $1$ mu postaje sused. Kada i nju pojede, veličina mu se poveća na $12$. Sada je u stanju da pojede i preostale dve bakterije. Dakle, dan $1$ je prvi dan u kome može pojesti sve bakterije.
	
	<br>
	
	Neka je $N=5$, $M=7$,  $S=\{1,2,3,2,9\}$, $U=\{1,1,1,1,2,2,4\}$, $V=\{2,3,4,5,3,5,5\}$. U niz $T$ je potrebno upisati $\{-1,2,2,2,0\}$. Razmotrimo slučaj kada je četvrta bakterija miksotrof. U nultom danu bira heterotrofnu formu i pojede bakteriju $2$. Time veličina miksotrofa postaje $4$. Veličine bakterija postaju $S=\{2,-,4,4,10\}$. U prvom danu, miksotrof takođe bira heterotrofnu formu. Najpre pojede bakterije $3$ i $1$. Zatim može pojesti i $5$. Time je miksotrof pojeo sve ostale bakterije u danu $1$.
	
	## Ograničenja
	*   $2 \leq N \leq 2\cdot 10^5$
	*   $1 \leq M \leq 2\cdot 10^5$
	*   $1 \leq S_i \leq 10^9$
	
	
	## Podzadaci
	*   (7 poena): $N,M \leq 500$;
	*   (15 poena): $N\leq 40\,000$, $M = N-1$ i $U[i]=i$, $V[i]=i+1$ ($1 \leq i \leq N-1$);
	*   (12 poena): $M = N-1$ i $U[i]=i$, $V[i]=i+1$ ($1 \leq i \leq N-1$);
	*   (29 poena): $S_i \leq 20$ za $1 \leq i \leq N$;
	*   (37 poena): Bez dodatnih ograničenja.
	
	## Detalji implementacije
	
	Potrebno je da pošaljete tačno jedan fajl  `e_pluribus_unum.cpp`  koji implementira pomenute funkcije. Osim traženih funkcija, vaš fajl može sadržati i dodatne globalne promenljive, pomoćne funkcije i dodatne biblioteke.
	
	Vaša funkcija mora biti sledećeg oblika:
	
	`void OdrediVreme(int N, int M, int* S, int *U, int *V, int *T);`
	
	**Vašim programima je dozvoljeno da menjaju sadržaj nizova ali ne smeju da pristupaju van granica datih nizova.**
	
	Uz zadatak, obezbeđen vam je "template" fajl  `code.cpp`  koji možete koristiti i menjati po potrebi. Takođe vam je obezbeđen program  `grader.cpp`  koji služi da lakše testirate kodove. Ovaj program učitava sa standardnog ulaza sledeće podatke:
	
	-   U prvom redu brojevi $N$ i $M$.
	-   U narednom redu $N$ brojeva: $S[i]$.
	-   U narednih $M$ redova po $2$ broja $U[i]$ i $V[i]$.
	
	Zatim ovaj program zove vašu funkciju i ispisuje rezultat koji vaša funkcija vrati.
	
	
=== "Rešenje"
	
	| Autor | Tekst i test primeri | Analiza rеšenja | Testiranje |
	|:-:|:-:|:-:|:-:|
	| Aleksandar Višnjić | Aleksandar Višnjić | Aleksandar Višnjić | Jovan Bengin |
	
	Neka je odgovor za datog miksotrofa $T$. Primetimo da je njemu optimalno da bude autotrof od dana $0$ do dana $T-1$. Tek u danu $T$ izabere da se hrani heterotrofno, i tad odjednom pojede sve ostale bakterije. Ovo važi jer ako u prvom danu kada odluči da se hrani heterotrofno ne pojede sve ostale bakterije, mora još dana da čeka. Ovo mu kasnije onemogućava da dobija na veličini na bakterijama koje je već pojeo (samo nepojedene bakterije koje se hrane autotrofno mogu narasti). Dakle, više će narasti ako se u tom prvom danu hranio autotrofno.
	
	### Prvi podzadatak
	Za svaku bakteriju, moguće je binarno pretražiti odgovor. Kreirajmo graf i izračunajmo nove veličine nakon pretpostavljenih $T_i$ trenutaka. Trenutna bakterija $i$ u svakom trenutku bira najmanjeg suseda i pojede ga. Ukoliko ne može da pojede ni najmanjeg suseda, onda provera pada. Ako može pojesti sve ostale bakterije, onda provera prolazi. Najmanji sused se može naći preko prioritetnog reda. Vremenska složenost je $O(NM(\log N)^2)$.
	  
	
	### Drugi podzadatak
	Potrebno je brže naći odgovor za svaku bakteriju. Kada je u pitanju niz, možemo koristiti binarnu pretragu po vrednosti rešenja i pamtiti trenutnu granicu $[l_i,r_i]$ koju je bakterija $i$ pojela. Ukoliko su bakterije $l_i -1$ i $r_i+1$ veće od trenutne veličine $i$, provera pada. Inače, poješće najveći broj uzastopnih bakterija koje može pojesti ulevo, i najveći takav broj udesno. Te granice je moguće naći binarnom pretragom po prefiksnoj sumi niza. Primetimo da se nakon dve simulacije ovih koraka veličina bakterije poraste barem duplo, te je broj koraka $O(\log S)$, gde sa $S$ označavamo zbir veličina svih bakterija na početku. Ovo daje ukupnu vremensku složenost $O(N(\log N)^2 \log S)$.
	
	### Treći podzadatak
	Moguće je eliminisati binarnu po rešenju. Provera ostaje ista, s tim što u nju ubacujemo "predomišljanje". Za trenutnu bakteriju simuliramo proces i pretpostavimo njeno početno optimalno vreme sa $T_i=0$. Kad god naiđemo na situaciju gde ona ne može više narasti, "predomislimo" se i postavimo $T_i$ na najmanju vrednost koja bi joj dozvolila da pojede bar jednog suseda. Kako je ipak optimalno da bakterija čeka do tog prvog trenutka, potrebno je odgovarajuće ažurirati njenu trenutnu veličinu računajući da će joj trenutno pojedene bakterije doneti doprinos. Ovo je moguće rešiti pravilno postavljenim matematičkim formulama. Složenost je $O(N\log N \log S)$.
	  
	
	### Četvrti podzadatak
	
	Primetimo da ako bakterija može pojesti sve ostale u nekom trenutku, to će uraditi najkasnije u trenutku $20$. Tu konstantu biramo jer je to najveća veličina bakterije u ovom podzadatku. Fiksirajmo neki univerzalni trenutak $0 \leq T \leq 20$. Odjednom proveravamo koje bakterije mogu pojesti sve ostale, a koje ne mogu. Analogno sa prošlim podzadatkom, umesto povezanih segmenata pamtimo povezane komponente. Njih je moguće održati preko unije disjunktnih skupova (DSU). Komponenta može pojesti drugu ako im ukupne veličine to dozvoljavaju. Za svaku je potrebno pamtiti i skup (vector) bakterija koje mogu pojesti sve ostale u toj komponenti (očito se može desiti da samo neke imaju tu sposobnost, i sve koje to mogu će imati istu veličinu na kraju). Ako pravilno radimo spajanje manje komponente u veću, imamo rešenje složenosti $O(N T \log N)$. Ovde $T$ predstavlja najkasniji smisleni trenutak.
	  
	
	### Glavno rešenje
	Kombinujemo ideje iz prethodna dva podzadatka. Održavaćemo uniju disjunktnih skupova (DSU) sa "predomišljanjem". Unutar komponente, za svaku bakteriju sinhronizovano pamtimo njen trenutni najmanji pretpostavljen trenutak. Primetimo da im se veličine zbog različitih vremena razlikuju, ali da će najmanja bakterija upravo biti ona sa najmanjim pretpostavljenim trenutkom. Prilikom spajanja dve komponente, potrebno je dozvoliti i najmanjoj bakteriji da pojede odgovarajuću susednu bakteriju. Ako je potrebno, tu vršimo "predomišljanje" primenom odgovarajuće matematičke formule. Pošto nam je potrebno traženje minimuma i vršenje promena u kolekciji, moraćemo da koristimo strukturu podataka (poput prioritetnog reda). Nakon dva "predomišljanja", veličina bakterije se duplira. Ovim je broj takvih, za jednu bakteriju, ograničen sa $O(\log S)$. Iako pri jednom spajanju možemo izvršiti velik broj operacija, prethodno uviđanje nam amortizuje složenost, te je ukupna $O(N(\log N)^2 + N\log S)$.
	
	### Bonus
	Rešiti zadatak u složenosti $O(N(\log N + \log S))$.
	
	``` cpp title="03_e_pluribus_unum.cpp" linenums="1"
	#include <bits/stdc++.h>
	
	using namespace std;
	long long typedef ll;
	pair<int,int> typedef typ;
	
	ll sum[200005];
	int up[200005];
	priority_queue<typ,vector<typ>,greater<typ>> stanja[200005]; //(velicina,vreme) za svakog organizma u komponenti
	bool impo[200005];
	
	void dsu(int a, int b, int s)
	{
	    while (up[a]>0) a=up[a];
	    while (up[b]>0) b=up[b];
	    if (a==b) return;
	
	    if (up[a]!=-1 || sum[a]==s)
	    {
	        while (true)
	        {
	            int tt=stanja[a].top().first;
	            int ind=stanja[a].top().second;
	            int k=-up[a];
	            ll ts=sum[a]+(ll)k*tt;
	            if (ts>=s+tt) break;
	            stanja[a].pop();
	            if (impo[ind]) continue;
	
	            int x=(s+tt-ts+k-2)/(k-1);
	            stanja[a].push({tt+x,ind});
	        }
	    }
	    else impo[a]=true;
	
	    if (up[a]<up[b]) swap(a,b);
	    up[b]+=up[a],sum[b]+=sum[a],up[a]=b;
	    while (!stanja[a].empty())
	    {
	        stanja[b].push(stanja[a].top());
	        stanja[a].pop();
	    }
	}
	
	vector<int> g[200005];
	
	void OdrediVreme(int N, int M, int* S, int *U, int *V, int *T)
	{
	    for (int i=1;i<=M;i++)
	    {
	        g[U[i]].push_back(V[i]);
	        g[V[i]].push_back(U[i]);
	    }
	
	    vector<pair<int,int>> sorta;
	    for (int i=1;i<=N;i++) sorta.push_back({S[i],i});
	    sort(sorta.begin(),sorta.end());
	    vector<int> id(N+1);
	    for (int i=0;i<N;i++) id[sorta[i].second]=i;
	
	    for (int i=1;i<=N;i++) up[i]=-1;
	    for (int i=1;i<=N;i++) stanja[i].push({0,i});
	    for (int i=1;i<=N;i++) sum[i]=S[i];
	
	    for (auto p : sorta)
	    {
	        for (auto it : g[p.second])
	        {
	            if (id[it]<id[p.second]) dsu(it,p.second,p.first);
	        }
	    }
	
	    int root=1;
	    while (up[root]>0) root=up[root];
	    while (!stanja[root].empty())
	    {
	        T[stanja[root].top().second]=stanja[root].top().first;
	        stanja[root].pop();
	    }
	
	    for (int i=1;i<=N;i++) if (impo[i]) T[i]=-1;
	}

	```
