---
hide:
  - toc
---

# 4 - Vasilije mrzi geometriju

=== "Zadatak"

	| Vremensko ograničenje | Memorijsko ograničenje |
	|:-:|:-:|
	| — | — |

	Vasilije, kao i svaki normalan programer, mrzi geometriju, i našao se u nezgodnoj situaciji.

	Naime, dok je Vasilije bio u izlasku sa svojom devojkom Milicom, ona mu je rekla da voli geometriju.

	Vasilije se na ovu rečenicu jako zbunio, pa je Milica odlučila da mu objasni lepotu geometrije. Kako bi uspela u ovome, ona je zatražila od Vasilija da joj napiše na papir $N$ **različitih** tačaka u ravni:

	$T_i = (x_i, y_i), \quad 1 \le i \le N, -10^9 \leq x_i, y_i \leq 10^9$

	Ona će za to vreme zamisliti neku permutaciju: $p = (p_1, p_2, \dots, p_N)$ brojeva od $1$ do $N$, i igra kreće.

	Vasilije može da pita Milicu sledeće pitanje:

	Za izabrana tri različita indeksa $i, j, k$, kakav je obilazak tačaka:
	$T_{p_i}, T_{p_j}, T_{p_k}$?

	Odgovor može biti jedan od sledeća tri:

	- $1$, ako je obilazak pozitivan,
	- $-1$, ako je obilazak negativan,
	- $0$, ako su tačke kolinearne.

	Za tri tačke $A$, $B$ i $C$ kažemo da su **kolinearne** ako postoji prava koja prolazi kroz sve tri tačke.

	Ako tačke $A$, $B$ i $C$ nisu kolinearne, kažemo da je obilazak $A \to B \to C$ **pozitivan** ako se tačka $C$ nalazi sa leve strane usmerene prave od $A$ ka $B$, a **negativan** ako se nalazi sa desne strane te usmerene prave.

	Vasilije želi da osvoji Miličino srce, i misli da će to uraditi uspešno ako pogodi njenu permutaciju sa što manje pitanja.

	Pomozite Vasiliju da nađe strategiju kojom će ovo uspešno uraditi.

	### Opis funkcija

	Potrebno je da implementirate funkcije:

	 - $ZapisiTacke(N)$

	gde je $N$ broj tačaka. Funkcija treba da zapiše tačke na kojima će se igrati igra.

	 - $Resi(N, Q)$

	gde je $N$ broj tačaka, a $Q$ dozvoljeni broj pitanja. Funkcija treba da odredi Miličinu permutaciju $p$.

	Vaš program može da koristi funkciju

	 - $Pitaj(i, j, k)$

	koja vraća odgovor na pitanje kakav je obilazak tačaka $T_{p_i}, T_{p_j}, T_{p_k}$.

	Indeksi $i$, $j$ i $k$ moraju biti međusobno različiti brojevi između $1$ i $N$.

	Funkcija $Pitaj(i, j, k)$ vraća:

	- $1$, ako je obilazak $T_{p_i} \to T_{p_j} \to T_{p_k}$ pozitivan,
	- $-1$, ako je obilazak $T_{p_i} \to T_{p_j} \to T_{p_k}$ negativan,
	- $0$, ako su tačke $T_{p_i}$, $T_{p_j}$ i $T_{p_k}$ kolinearne.

	Tačke su indeksirane od $1$ do $N$.

	Permutacija $p$ je fiksirana pre pokretanja vaše funkcije i ne menja se tokom izvršavanja programa.

	### Primer

	Jedan primer može izgledati ovako:

	Neka je $N = 5$.

	Koristeći funkciju `ZapisiTacke`, možete zapisati sledećih 5 tačaka:

	$T_1 = (0, 0)$, $T_2 = (1, 0)$, $T_3 = (2, 0)$, $T_4 = (0, 1)$, $T_5 = (1, -1)$,

	Neka je Miličina permutacija:

	$p = [5, 3, 4, 2, 1]$

	Tada, na primer:

	- `Pitaj(2, 4, 5)` posmatra obilazak $T_{p_2} \to T_{p_4} \to T_{p_5}$, odnosno $T_3 \to T_2 \to T_1$.
	  Pošto su ove tri tačke kolinearne, funkcija vraća $0$.

	- `Pitaj(1, 2, 4)` posmatra obilazak $T_5 \to T_3 \to T_2$.
	  Tačka $T_2$ se nalazi sa leve strane usmerene prave od $T_5$ ka $T_3$, pa funkcija vraća $1$.

	- `Pitaj(5, 2, 1)` posmatra obilazak $T_1 \to T_3 \to T_5$.
	  Tačka $T_5$ se nalazi sa desne strane usmerene prave od $T_1$ ka $T_3$, pa funkcija vraća $-1$.

	Ovaj primer služi samo za ilustraciju načina na koji funkcija `Pitaj` radi. U stvarnim test primerima, permutacija $p$ je skrivena od takmičara.

	Nakon što Vasilije koristeći dovoljno funkcija pitaj, sazna permutaciju $p$, funkcija `Resi` treba da vrati: {$X, 5, 3, 4, 2, 1$}, gde $X$ može biti bilo koja vrednost koja staje u opseg `c++`  tipa `int` .

	### Ograničenja

	Važi:

	$4 \le N \le 1000$

	Test primeri su podeljeni u nekoliko podzadataka. U svakom podzadatku je dato ograničenje $Q$, koje predstavlja dozvoljen broj poziva funkcije $Pitaj$.

	- **[5 poena]**: $p$ =  $[1, 2, 3, \dots, N]$ ili $p$ = $[N, N-1, \dots, 1]$, $N \leq 200, Q = 20000$.

	- **[20 poena]**: $p_1 = 1$, $N \leq 200, Q = 25000$.

	- **[15 poena]**: $N \leq 50, Q = 150000$.

	- **[20 poena]**: $N \leq 200, Q = 25000$.

	- **[20 poena]**: $Q = 24000$.

	- **[20 poena]**: $Q = 9400$.

	### Detalji implementacije

	Potrebno je da pošaljete tačno jedan fajl koji implementira pomenutu funkciju. Osim tražene funkcije, vaš fajl može da sadrži i dodatne globalne promenljive, pomoćne funkcije i dodatne biblioteke.

	Vaše funkcije moraju biti sledećeg oblika:

	- `vector<pair<int, int>> ZapisiTacke(int N)`

	- `vector<int> Resi(int N, int Q)`

	Funkcija `ZapisiTacke` treba da vrati tačke kao niz parova indeksiran od 1, dužine $N+1$, gde je prva vrednost para $x$ koordinata, a druga vrednost $y$ koordinata.

	Funkcija `Resi` treba da vrati pronađenu permutaciju $p$ kao niz indeksiran od 1, dužine $N+1$.

	Vaš program mora uključivati header `code.h`, u kom je definisana funkcija `Pitaj` sledećeg potpisa:

	- `int Pitaj(int i, int j, int k)`

	Uz zadatak, obezbeđen vam je `template` fajl `code.cpp` koji možete koristiti i menjati po potrebi. Takođe vam je obezbeđen program `grader.cpp` koji služi da lakše testirate kodove.

	Ovaj program učitava sa standardnog ulaza sledeće podatke:

	U prvom redu nalaze se brojevi $N$ i $Q$.

	Zatim ovaj program poziva vašu funkciju `ZapisiTacke` kako bi dobila tačke na kojima će se igrati igra.

	U sledećem redu nalazi se permutacija $p_1, p_2, \dots, p_N$.

	Zatim ovaj program poziva vašu funkciju `Resi` i štampa povratnu vrednost na ekran. Ukoliko vaše rešenje koristi funkciju `Pitaj` više od $Q$ puta, biće prekinuto sa statusom RTE (runtime error).

	> Vremensko i memorijsko ograničenje nisu navedeni u dostupnom materijalu.

	[Test primeri i prateći fajlovi sa zvaničnog takmičenja](https://nyc3.digitaloceanspaces.com/takprog/2025-26/2025-2026-sio-problems.zip).

=== "Rešenje"

	| Autor | Tekst i test primeri | Analiza rešenja | Testiranje |
	|:-:|:-:|:-:|:-:|
	| Vasilije Novaković | Vasilije Novaković | Vasilije Novaković | Miloš Milutinović |

	## Rešenje kad $p$ =  $[1, 2, 3, \dots, N]$ ili $p$ = $[N, N-1, \dots, 1]$, $N \leq 200, Q = 20000$

	Ovaj podzadatak može biti rešen koristeći jedan poziv funkcije `Pitaj`.

	Pošto je obilazak tri tačke samo smer u kom bismo obilazili opisani krug trougla koji one formiraju, veoma je jasno da važi da ako obrnemo redosled tačaka kojim obilazimo, i smer će se obrnuti.

	Ovo znači da bi bilo koja uređena trojka tačaka koje bi u permutaciji $p$ =  $[1, 2, 3, \dots, N]$ davala pozitivan smer obilaska, davala negativan smer obilaska u permutaciji $p$ = $[N, N-1, \dots, 1]$, i obratno.

	Dakle za ovaj podzadatak dovoljno je da među tačkama imamo bar jednu trojku koja nije kolinearna, i da znamo koji bi bio njihov obilazak nekim redosledom. Zatim pitamo za smer obilaska ove tri tačke u tom istom redosledu, i ako se poklapa sa našim, odgovor je $p$ =  $[1, 2, 3, \dots, N]$, a ako se ne poklapa onda je $p$ = $[N, N-1, \dots, 1]$.

	## Analiza malih slučajeva

	Da bismo nastavili dalje sa rešenjem, potrebno je da pažljivo izaberemo tačke koje ćemo uzeti.

	Upit za orijentaciju 3 tačke je poprilično apstraktan, pa možemo izgraditi osećaj za dobru konstrukciju razmišljanjem o malim slučajevima:

	Zašto je u zadatku $N \geq 4$?

	Uzmimo $N = 3$:

	- Ako uzmemo kolinearne tačke, bilo koji upit nam vraća $0$, što nam ne daje nikakve informacije o permutaciji.

	- Ako uzmemo tri tačke koje nisu kolinearne, za svaku trojku $(i, j, k)$, sve rotacije bilo koje permutacije daju nam identične odgovore na upit, pa ih ne možemo nikako razlikovati, što znači da je zadatak nerešiv za $N = 3$.

	Prvi slučaj se proširuje dalje i za veći broj tačaka: ako su sve tačke kolinearne, ne možemo nikako razlikovati nijedne dve permutacije.

	Međutim, drugi slučaj nam nalaže, da za veći broj tačaka moramo imati neke kolinearne tačke kako bismo mogli da razlikujemo između permutacija koje su rotacije jedna druge.

	Sad uzmimo $N = 4$

	Razmišljajući o kolinearnim tačkama, možemo zaključiti da postoje 3 različite konstrukcije:

	1. Sve $4$ tačke leže na jednoj pravoj.
	2. Ne postoje kolinearne trojke.
	3. Postoji tačno jedna kolinearna trojka, a četvrta tačka ne leži na istoj pravoj kao i one.

	Razmatranjem $N = 3$ odmah možemo odbaciti slučajeve $1$ i $2$, što nam ostavlja slučaj gde jedna tačka odstupa od prave.

	Dalje rešavanje imajući ovu konstrukciju napisaćemo u sledećem podzadatku, jer je suština ove analize bila da nađemo dobru konstrukciju.

	## Rešenje kad $p_1 = 1$, $N \leq 200, Q = 25000$

	Razmotrimo generalizaciju konstrukcije koju smo smislili u analizi malih slučajeva: stavićemo $N - 1$ tačku na istu pravu, dok ćemo prvu tačku staviti van te prave. Radi jednostavnosti, možemo staviti sve tačke na $x$-osu, gde će $i$-ta tačka $T_i = (i, 0)$, dok ćemo našu specijalnu tačku staviti bilo gde na $y=1$ (iznad ostalih tačaka)

	Pošto važi $p_1 = 1$, mi odmah znamo koja tačka nam je specijalna, jer je samo možemo staviti kao prvu tačku.

	Možemo sad primetiti da, pošto se specijalna tačka nalazi iznad svih ostalih, `Pitaj(specijalna, x, y)` će vratiti odgovor $1$ ako se $T_{p_x}$ nalazi levo u odnosu na pravu koju čine prve dve tačke, što znači ako se $T_{p_y}$ nalazi desno na $x$-osi u odnosu na $T_{p_x}$. Važi i suprotno za odgovor $-1$.

	Na ovaj način možemo videti da li je $p_x < p_y$, jer smo ispisali tačke tako da leva tačka ima manji indeks od desne.

	Ovo nam dozvoljava da nađemo zasebno svako $x$, gde se on nalazi u permutaciji, što nam samim tim jednoznačno određuje i samu permutaciju.

	Pošto ovaj način traženja poretka tačaka zahteva $n^2 / 2$ upita, ovo se komotno uklapa u ograničenja podzadatka.

	## Rešenje kad $N \leq 50, Q = 150000$

	U ovom podzadatku važi $Q > N^3$ što nam dozvoljava da uradimo svaki mogući upit.

	Posmatramo istu konstrukciju kao i prošli podzadatak. Razlika je što u ovom podzadatku imamo više upita, ali ne znamo specijalnu tačku od početka.

	Kako bi smo mi našli koja je to specijalna tačka, možemo primetiti da će odgovor na upit za ovu konstrukciju biti $0$ ako i samo ako specijalna tačka nije deo tog upita.

	U ovom podzadatku imamo mogućnost da probamo svaki mogući upit, pa možemo proći kroz sve upite i naći tačku koja se nalazi isključivo u upitima gde odgovor nije $0$.

	Možemo na isti način kao i u prethodnom podzadatku naći skrivenu permutaciju.

	## Rešenje kad $N \leq 200, Q = 25000$

	Ovaj podzadatak zahteva od nas da brže nađemo specijalnu tačku.

	Kako bi smo to uradili, možemo upitivati redom tačke $i, i+1, i+2$: ako je odgovor na upit $1$ ili $-1$, to znači da je jedna od ove $3$ tačke specijalna, nakon što smo sveli broj mogućih specijalnih tačaka na $3$ u $O(N)$ upita, lako možemo zaključiti koja od te $3$ je zapravo specijalna, tako što pitamo svaki par dve od te $3$ tačke sa nekom sporednom tačkom (koja je sigurno na pravoj), i ako je odgovor $0$, onda je tačka koju smo izostavili iz upita specijalna.

	Koristeći ovaj način traženja uspešno nalazimo specijalnu tačku nakon najviše $N + 1$ upita.

	Nalazak tražene permutacije rešava se na isti način kao i u prethodna dva podzadatka.

	## Rešenje kad $Q = 24000$

	Za ovaj podzadatak moramo u manjem broju upita da nađemo permutaciju. U suštini, mi ne moramo direktno za svako $x$ zasebno da nalazimo koliko tačaka ima levo od $T_{p_x}$, već tačke možemo sortirati sve u isto vreme koristeći bilo koji sorting algoritam sa poređenjem, gde svako poređenje unutar sortiranja košta jedan upit. Za ovaj podzadatak možemo iskoristiti skoro bilo koji algoritam sortiranja koji koristi $O(N \cdot log_2 N)$ poređenja.

	Nakon što smo sortirali tačke možemo proći kroz svako $x$ kako bi našli koliko ima tačaka levo od $p_x$. Iako ovo može da se uradi i u linearnoj složenosti nije potrebno za ovaj zadatak.

	Za jednostavnu implementaciju možemo napraviti našu funkciju poređenja koja koristi `Pitaj` kako bi znala kako da uporedi dve tačke, i ovu funkciju možemo proslediti `std::sort` funkciji čime postižemo da ne moramo da implementiramo nijedan specifičan sorting algoritam za ovaj podzadatak.

	## Rešenje kad $Q = 9400$

	Za $N = 1000$, $log_2 N$ je malo ispod $10$, što znači da bi $N \cdot log_2 N$ bilo oko $10000$ upita. Trenutni algoritam preko ovoga ima i traženje specijalne tačke koje zahteva $O(N)$ upita, dovodeći nas do oko $11000$ upita.

	Kako bi smo ovaj broj upita smanjili na ispod $9400$, potrebno je, prvo, da nađemo algoritam sortiranja u $O(N \cdot log_2 N)$ sa dovoljno malim, garantovanim brojem poređenja.

	Posmatrajmo kako funkcioniše algoritam `merge sort`. Kad spajamo dva dela, veličina $x$ i $y$, ovaj algoritam će napraviti $x+y-1$ poređenje u najgorem slučaju, gde je najgori slučaj se oba dela prazne dok ne dođu do stanja gde oba imaju po jedan element, gde će nakon poređenja oba ta elementa moći da se ubace u spojeni, sortirani niz.

	Ovo je najgori slučaj zato što smo za svaki element osim poslednjeg napravili po jedno poređenje. Ali opet, postoji tačno $\lceil log_2 N \rceil$ nivoa merge sort-a, i svaki element će biti upoređen na svakom nivou najviše jednom, što merge sort algoritmu daje relativno mali broj poređenja, koji smo upravo ograničili na $N \cdot \lceil log_2 N \rceil$ poređenja.

	Međutim, broj poređenja je još niži, zbog toga što prethodna granica računa da je broj poređenja $x + y$ za spajanje, a ne $x + y - 1$.

	Na najnižem nivou, algoritam spaja $N$ delova veličine $1$, u $N/2$ delova veličine $2$. Ovo znači da na tom nivou mi ne pravimo $N$ poređenja, nego $N - N / 2$ poređenja. Sličnom logikom možemo za pretposlednji nivo dobiti $N - N / 4$, i tako dalje.

	Kad prosumiramo ovo za sve nivoe, dobijamo ukupno: $N \cdot \lceil log_2 N \rceil - N + 1$, i ovim smo efektivno smanjili broj upita za $N$, što nas dovodi do oko $10000$ upita.

	Kako bismo dalje spustili broj upita ispod $9400$, možemo primetiti da specijalnu tačku možemo pronaći u najviše $N/3 + 4$ upita, umesto $N + 1$, tako što ako za $i, i+1, i+2$ dobijemo da su kolinearne, ne moramo da proveravamo ni za $i+1, i+2, i+3$ niti za $i+2, i+3, i+4$, već možemo odmah preći na $i+3, i+4, i+5$. Jedini izuzetak ovde jeste da moramo ručno proveriti $N-2, N-1, N$ jer se može desiti da nam je specijalna tačka na mestu $N$ a da smo dobili odgovor $0$ na $N-4, N-3, N-2$. Ovom optimizacijom smo smanjili broj upita za još $2 \cdot N / 3$, što je dovoljno da uz `merge sort` uspešno odredi bilo koju permutaciju u manje od $9300$ upita.

	[Izvor analize i autorskih podataka](https://algora.petlja.org/t/2025-2026/9654/4).

	``` cpp title="vasa_mrzi_geometriju-sol.cpp" linenums="1"
	#include <iostream>
	#include <vector>
	#include <utility>
	#include <algorithm>
	#include "code.h"

	using namespace std;

	int specijalna = -1;

	bool uporedi(int a, int b){
	    return Pitaj(specijalna, a, b) > 0;
	}

	vector<int> merge_sort(vector<int> v, bool (*cmp)(int, int)){
	    if(v.size() <= 1)return v;
	    int mid = v.size()/2;
	    vector<int> l(v.begin(), v.begin() + mid);
	    vector<int> r(v.begin() + mid, v.end());
	    l = merge_sort(l, cmp);
	    r = merge_sort(r, cmp);
	    vector<int> res;
	    int i = 0, j = 0;
	    while(i < l.size() && j < r.size()){
	        if(cmp(l[i], r[j])){
	            res.push_back(l[i]);
	            i++;
	        }
	        else{
	            res.push_back(r[j]);
	            j++;
	        }
	    }
	    while(i < l.size()){
	        res.push_back(l[i]);
	        i++;
	    }
	    while(j < r.size()){
	        res.push_back(r[j]);
	        j++;
	    }
	    return res;
	}

	vector<pair<int, int>> ZapisiTacke(int n){
	    vector<pair<int, int>> v;
	    v.push_back({0, 0});
	    v.push_back({0, 1});
	    for(int i=2; i<=n; i++){
	        v.push_back({i, 0});
	    }
	    return v;
	}

	vector<int> Resi(int n, int q){
	    int ind = -1;
	    for(int i = 1; i+2 <= n; i+=3){
	        int ans = Pitaj(i, i+1, i+2);
	        if(ans != 0){
	            ind = i;
	            break;
	        }
	    }
	    if(Pitaj(n-2, n-1, n) != 0){
	        ind = n - 2;
	    }
	    //sad se specijalna tacka nalazi medju {ind, ind+1, ind+2}
	    if(ind == 1){
	        if(Pitaj(1, 2, 4) == 0)specijalna = 3;
	        else if(Pitaj(1, 3, 4) == 0)specijalna = 2;
	        else specijalna = 1;
	    }
	    else{
	        if(Pitaj(ind, ind+1, 1) == 0)specijalna = ind+2;
	        else if(Pitaj(ind, ind+2, 1) == 0)specijalna = ind+1;
	        else specijalna = ind;
	    }
	    // P[specijalna] = 1
	    vector<int> res;
	    for(int i = 1; i<=n; i++){
	        if(i != specijalna)res.push_back(i);
	    }

	    res = merge_sort(res, uporedi);

	    vector<int> ret(n+1);
	    ret[specijalna] = 1;
	    vector<int> pozicija(n+1);
	    for(int i = 0; i<res.size(); i++){
	        pozicija[res[i]] = i+2;
	    }
	    for(int i = 1; i<=n; i++){
	        if(i == specijalna)continue;
	        ret[i] = pozicija[i];
	    }
	    return ret;
	}
	```
