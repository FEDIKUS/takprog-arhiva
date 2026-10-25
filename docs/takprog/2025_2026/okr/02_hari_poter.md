---
hide:
  - toc
---

# B2 - Hari Poter

=== "Zadatak"
	
	| Vremensko ograničenje | Memorijsko ograničenje |
	|:-:|:-:|
	| 1000ms | 128MB |
	
	
	<br>
	
	Hari Poter se nalazi u lavirintu u kojem se tokom četvrtog dela (valjda?) trkao sa drugim čarobnjacima. Trenutna deonica lavirinta izgleda kao jedan veoma dugačak hodnik orijentisan od juga ka severu. Hari je okrenut ka severu. Formalno, hodnik možemo da zamislimo kao brojevnu pravu, sa Harijem na koordinati $0$ i okrenutim ka pozitivnim brojevima. Sa obe strane mu prilaze njegovi arhineprijatelji, dementori. Svake sekunde Hari može da napravi jedan od sledeća tri poteza:
	
	<br>
	
	 1. Baci čin ka severu, čime ukloni najbližeg dementora ispred sebe.
	 2. Baci čin ka jugu, čime ukloni najbližeg dementora iza sebe.
	 3. Pomeri se za jedno polje ka severu.
	
	<br>
	 
	Primetite da Hari može da baci čin u nekom smeru čak i kada ne postoji dementor u tom smeru. Nakon što Hari izvede svoj potez, svi dementori koji preostanu mu se približe za jedno polje. Kada dementori sustignu Harija, on više ne može da se kreće i baca čini. Hari **ne sme da napravi dva poteza istog tipa za redom** ~~jer inače zadatak ne bi bio dovoljno težak~~. Pored toga, **Hari može da izvrši najviše $10^6$ poteza** pre nego što se previše umori.
	
	<br>
	
	Ispisati koliko najviše dementora Hari može da eliminiše, pre nego što ga sustignu ili se previše umori. Dodatno, ispisati i redosled poteza koje Hari treba da izvrši da bi to postigao. Ukoliko ima više mogućih redosleda, ispisati bilo koji. 
	
	<br>
	
	## Opis ulaza
	
	<br>
	
	U prvoj liniji standardnog ulaza dat je ceo broj $N$, broj dementora.
	
	<br>
	
	U drugoj liniji standardnog ulaza, dato je $N$ celih brojeva. $i$-ti od njih je $x_i$ i predstavlja poziciju $i$-tog dementora. 
	
	<br>
	
	## Opis izlaza
	
	<br>
	
	U prvoj liniji ispisati maksimalan broj dementora $d$ koje Hari može da eliminiše. U drugoj liniji ispisati nisku karaktera $s$. Svi karakteri ove niske moraju biti $1$, $2$ ili $3$. $i$-ti karakter, $s_i$, predstavlja potez koju Hari treba da napravi u $i$-tom koraku.
	
	<br>
	
	## Primer 1
	
	<br>
	
	### Ulaz
	
	<br>
	
	```
	2
	-5 5
	```
	
	<br>
	
	### Izlaz
	
	<br>
	
	```
	2
	2321
	```
	
	### Objašnjenje primera 1
	
	<br>
	 
	U prvom primeru postoje dva dementora. Jedan se nalazi na poziciji $-5$, drugi se nalazi na poziciji $5$. Hari će u prvom potezu baciti čin ka jugu i time eliminisati dementora na poziciji $-5$. Nakon toga će mu se dementor sa pozicije $5$ približiti za jedno polje i pomeriti se na poziciju $4$. U drugom potezu, Hari će se pomeriti za jedno polje ka severu i naći se na poziciji $1$. Nakon Harijevog poteza, dementor ispred njega će mu se približiti i pomeriti sa pozicije $4$ na poziciju $3$. U trećem potezu, Hari će baciti čin ka jugu. Pošto se iza njega ne nalazi nijedan dementor, čin neće nikoga eliminisati. Nakon trećeg poteza, dementor sa pozicije $3$ će se pomeriti na poziciju $2$. U četvrtom potezu, Hari će baciti čin ka severu i eliminisati i drugog dementora. Prema tome, moguće je eliminisati oba dementora. Primetite i da je `12` takođe bio validan redosled operacija, kojim se eliminišu oba dementora.
	
	<br>
	
	## Primer 2
	
	<br>
	
	### Ulaz
	
	<br>
	
	```
	2
	-1 1
	```
	
	<br>
	
	### Izlaz
	
	<br>
	
	```
	1
	1
	```
	
	<br>
	
	### Objašnjenje primera 2
	
	<br>
	 
	U drugom primeru ponovo postoje dva dementora. Jedan se nalazi na poziciji $-1$, drugi se nalazi na poziciji $1$. Primetimo da Hari može da eliminiše najviše jednog dementora po potezu. Pošto su mu oba dementora susedna, nakon prvog poteza, jedan od ta dva dementora će ga sustići. Hari će u prvom potezu baciti čin ka severu i time eliminisati dementora na poziciji $1$. Nakon toga će mu se dementor sa pozicije $-1$ približiti za jedno polje i pomeriti se na poziciju $0$. U tom trenutku, dementori su ga sustigli i Hari više ne može da povlači poteze. Prema tome, maksimalan broj dementora koje je moguće eliminisati je $1$.
	
	<br>
	
	## Ograničenja i bodovanje
	
	
	<br>
	
	
	- $1 \leq n \leq 200.000$.
	- $|x_i| \leq 10^9$ i $x_i \neq 0$, za $1 \leq i \leq n$.
	- $x_i \neq x_j$ za $i \neq j$.
	- Niz $x$ ne mora biti sortiran.
	- Ukupan broj ispisanih poteza može da bude najviše $10^6$.
	
	<br>
	
	Test primeri su podeljeni u $5$ disjunktnih grupa:
	
	   
	   - U testovima vrednim $10$ poena: važi $n \leq 10$
	   - U testovima vrednim $15$ poena: važi $x_i < 0$, za $1 \leq i \leq n$.
	   - U testovima vrednim $20$ poena: važi $x_i > 0$, za $1 \leq i \leq n$.
	   - U testovima vrednim $15$ poena: važi $|x_i|$ je parno, $1 \leq i \leq n$.
	   - U testovima vrednim $40$ poena: bez dodatnih ograničenja.
	
	<br>
	
	Ukoliko u datom primeru tačno ispišete maksimalan broj dementora $d$, ali ne i rekonstrukciju, dobijate $40\%$ bodova za taj primer.
	
	<br>
	
	## Napomena
	
	
	<br>
	
	Ukoliko ispišete preko $10^6$ poteza, dobijate najviše $40\%$ bodova za taj primer (ukoliko je broj dementora tačan). Slično, ukoliko nastavite da ispisujete poteze nakon što dementori sustignu Harija, dobijate najviše $40\%$ bodova za taj primer.
	
	<br>
	
=== "Rešenje"
	
	| Autor | Tekst i test primeri | Analiza rešenja | Testiranje |
	|:-:|:-:|:-:|:-:|
	| Marko Milenković | Aleksa Milisavljević | Anja Dožić | Aleksa Danić i Marko Milenković |
	
	## Podzadatak 1: $n\leq10$
	Primetimo da Hariju nikada neće biti optimalno da napravi dva vezana poteza koja neće ukloniti dementore. Dakle, najveći broj poteza koje Hari može da napravi u ovom podzadatku je  $2n$. Kako je $n$ malo, možemo isprobati sve moguće sekvence koje zadovoljavaju uslove zadatka (ima ih $3\cdot2^{2n}$) i videti u kojoj će broj dementora koje Hari može da ukloni biti najveći.
	
	Vremenska složenost: $O(2^{2n})$
	
	## Podzadatak 2: $x_i<0$, za $1\leq i\leq n$
	Kako u ovom podzadatku ne postoje dementori severno od Harija, njemu je uvek bezbedno da napravi korak napred (tj. korak ka severu). Primetimo da će mu u ovom slučaju optimalna strategija biti da na smenu ponavlja akcije $2$ i $3$, tj. da prvo ukloni najbližeg južnog dementora i zatim se pomeri korak severno i to ponavlja dok ne ukloni sve dementore.
	
	Hari će u ovom podzadatku sigurno moći da ukloni sve dementore jer nakon što na početku ukloni najbližeg sebi i zatim se pomeri korak napred, najbliže što je prvi sledeći najbliži dementor mogao da priđe je tačno jedan korak iza Harija, pa će Hari moći da ga ukloni u narednom potezu.
	
	Vremenska složenost: $O(n)$
	
	## Podzadatak 3: $x_i>0$, za $1\leq i\leq n$
	U ovom podzadatku, svi dementori će se nalaziti severno od Harija, te njemu nikada neće biti optimalno da napravi korak napred i približi im se. Odatle zaključujemo da će mu u ovom slučaju optimalna strategija biti da na smenu ponavlja akcije $1$ i $2$, tj. da prvo ukloni najbližeg severnog dementora i zatim baci čin ka jugu "u prazno".
	
	Za razliku od prethodnog podzadatka, ovde ne možemo garantovati da će Hari moći da ukloni sve dementore. Prvo ćemo sortirati niz dementora. Primetimo da Hari $i$-tog dementora može da ukloni nakon tačno $2i-1$ poteza, dakle pošto se Hari ne kreće, dovoljno je da se $i$-ti dementor nalazi na nekom polju koje je manje od $2i-1$ i on će ga sustići. Rešenje dobijamo nakon što prođemo kroz niz dementora proveravajući da li neki od njih može da sustigne Harija. Nakon što naiđemo na prvog koji može da ga sustigne, ispisujemo broj dementora koje je Hari do tog trenutka uklonio i ranije opisanu sekvencu poteza. Ako ni jedan ne može da ga sustigne, ispisujemo broj dementora i sekvencu.
	
	Vremenska složenost: $O(n\cdot\log n)$
	
	## Podzadatak 4: $|x_i|$ je parno za $1\leq i\leq n$
	Slično kao i u prethodnom podzadatku, ako Hari na smenu ponavlja akcije $1$ i $2$, on će $i$-tog dementora na severu ukloniti nakon tačno $2i-1$ poteza, dok će $j$-tog dementora na jugu ukloniti nakon tačno $2j$ poteza. Ova strategija nam garantuje da će Hari moći da ukloni sve dementore u ovom podzadatku, jer se oni nalaze samo na parnim poljima, tj. $i$-ti dementor na severu nikada neće biti na polju bližem od $2i$, kao što ni $j$-ti dementor na jugu nikada neće biti na polju bližem od $2j$.
	
	Vremenska složenost: $O(n)$
	
	## Podzadatak 5: Celo rešenje
	Primetimo sada da je Hariju optimalno da napravi korak napred jedino kada je na to primoran tj. kada je već bacio čin ka jugu i ima jednog dementora tačno iza sebe. U svakom drugom slučaju, bacanje čini ka severu će mu se više isplatiti jer time uklanja dementora severno ako postoji i siguran je da ga nijedan dementor neće stići.
	
	Dakle, moraćemo da proverimo dve mogućnosti: kada je Harijevo prvo bacanje čini ka severu i kada je Harijevo prvo bacanje čini ka jugu (u prethodnom podzadatku nam to nije bilo važno jer su svi dementori bili na parnim poljima što nam je ostavljalo dovoljno prostora za odabir strane prve čini). Čuvaćemo dva sortirana niza koordinata, pozitivne i negativne, i paralelno proveravati da li neki dementor može da sustigne Harija ako baca naizmenično čini ka severu pa ka jugu (tj. ka jugu pa ka severu u drugom slučaju). Primetimo da ne moramo da apdejtujemo ceo niz pozicija dementora posle svakog poteza, već da jednostavno možemo dobiti trenutnu poziciju željenog dementora tako što na nju dodamo ili oduzmemo broj poteza koje smo napravili u zavisnosti od toga da li je dementor južno ili severno od Harija. Ako se ispostavi da ga dementor koji je južno od njega stiže, sledeći potez će mu umesto čini ka severu biti pomeranje u napred i zatim ponovo čin ka jugu. Taj broj poteza apdejtujemo i nastavljamo da proveravamo dok Hari ne ukloni sve dementore ili dok ga dementor ispred njega ne sustigne jer od njega nema način da pobegne.
	
	Vremenska složenost: $O(n\cdot\log n)$
	
	``` cpp title="02_hari_poter.cpp" linenums="1"
	#include<bits/stdc++.h>
	#define maxn 200005
	using namespace std;
	int n;
	int x[maxn];
	set<int> pos;
	set<int> neg;
	vector<int> k[3];
	int simulate(int fst) {
	    int ret = 0;
	    int off = 0;
	    int p = 0;
	    pos.clear();
	    neg.clear();
	    for(int i = 1; i <= n; i++) {
	        if(x[i] > 0) pos.insert(x[i]);
	        else neg.insert(-x[i]);
	    }
	    off = 0;
	    p = 0;
	    while(!pos.empty() || !neg.empty()) {
	        if(!pos.empty()) {
	            int v=(*pos.begin())-off;
	            if(v<=p) {
	                break;
	            }
	        }
	        if(!neg.empty()) {
	            int v=-(*neg.begin())+off;
	            if(v>=p) {
	                break;
	            }
	        }
	        if(k[fst].empty()) {
	            k[fst].push_back(fst);
	            if(fst==1) {
	                if(!pos.empty()) {
	                    pos.erase(pos.begin());
	                    ret++;
	                }
	            }
	            else {
	                if(!neg.empty()) {
	                    neg.erase(neg.begin());
	                    ret++;
	                }
	            }
	        }
	        else {
	            if(k[fst].back() == 3) {
	                k[fst].push_back(2);
	                if(!neg.empty()) {
	                    neg.erase(neg.begin());
	                    ret++;
	                }
	            }
	            else {
	                bool must_move = false;
	                if(!neg.empty()) {
	                    int v=-(*neg.begin())+off;
	                    if(v + 1 >= p) {
	                        must_move = true;
	                    }
	                }
	                if(must_move && k[fst].back() == 2) {
	                    k[fst].push_back(3);
	                    p++;
	                }
	                else {
	                    if(k[fst].back() == 1) {
	                        k[fst].push_back(2);
	                        if(!neg.empty()) {
	                            neg.erase(neg.begin());
	                            ret++;
	                        }
	                    }
	                    else {
	                        k[fst].push_back(1);
	                        if(!pos.empty()) {
	                            pos.erase(pos.begin());
	                            ret++;
	                        }
	                    }
	                }
	            }
	        }
	        off++;
	    }
	    return ret;
	}
	int main() {
	    ios::sync_with_stdio(0);
	    cin.tie(0);
	    cin >> n;
	    for (int i = 1; i <= n; i++) {
	        cin >> x[i];
	    }
	    int ans1 = simulate(1);
	    int ans2 = simulate(2);
	    if(ans1 > ans2) {
	        cout << ans1 << "\n";
	        for(auto v : k[1]) {
	            cout << v ;
	        }
	        cout<<endl;
	    }
	    else {
	        cout << ans2 << "\n";
	        for(auto v : k[2]) {
	            cout << v ;
	        }
	        cout<<endl;
	    }
	
	    return 0;
	}

	```
