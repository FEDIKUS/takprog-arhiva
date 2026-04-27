---
hide:
  - toc
---

# A2 - Kodforses blog

=== "Zadatak"
	
	| Vremensko ograničenje | Memorijsko ograničenje |
	|:-:|:-:|
	| 1000ms | 256MB |
	
	Panta je odlučio da postane bloger na popularnom programerskom sajtu kodforses. Upravo je napisao svoj prvi blog. Blog ima svoju uvaženost, koja je ceo broj. Kada se tek napravi, blog ima uvaženost $0$.
	
	<br>
	
	Pantin blog će vitedi $n$ ljudi. Nakon što pročita blog, svaki čovek će imati mišljenje o tome koliko je taj blog dobar i koju uvaženost zaslužuje, neka je ta uvaženost $a$. Nakon toga će pogledati kolika je trenutna uvaženost bloga. Ako je trenutna uvaženost manja ili jednaka $a$, on će da kaže da mu se svideo blog i uvaženost bloga će biti povećana za $1$. Ukoliko je trenutna uvaženost bloga veća od $a$, onda će da kaže da mu se nije svideo blog i uvaženost bloga će biti smanjena za $1$. 
	
	<br>
	
	Panti je poznato da će $n$ ljudi videti njegov blog. Radi jednostavnosti, ljudima su dodeljeni brojevi od $1$ do $n$, ali to ne mora biti redosled kojim će oni da vide blog. Čovek sa brojem $i$ smatra da uvaženost bloga treba da bude $a_i$. Panta ne zna kojim će redom tih $n$ ljudi videti blog, a zanima ga da li postoji redosled takav da nakon što svi ljudi vide blog, njegova uvaženost bude tačno $k$.
	
	<br>
	
	Nekad je Panti važno samo da li postoji takav redosled, a nekad želi i da mu odredite sam redosled. To oznavača broj $t$ koji može imati vrednosti $0$ ili $1$. Ako je $0$, onda Pantu zanima samo da li takav redosled postoji. Ukoliko je $1$, onda ga takođe zanima i primer takvog redosleda. Ako ima više redosleda nakon kojih je uvaženost bloga $k$, **možete ispisati bilo koji**.
	
	## Opis ulaza
	
	<br>
	
	Prva linija standardnog ulaza sadrži broj $t$ - oznaku da li Pantu zanima i konkretan redosled kojim će ljudi videti blog.
	
	<br>
	
	Druga linija sadrži dva cela broja, $n$ i $k$ - broj ljudi koji će da vide blog i željena uvaženost.
	
	<br>
	
	Treća linija sadrži $n$ brojeva $a_1, a_2, \ldots, a_n$ - mišljenja ljudi o tome koliku uvaženost blog treba da ima. 
	
	<br>
	
	
	## Opis izlaza
	
	<br>
	
	U prvoj liniji standardnog izlaza je potrebno ispisati `DA ` uokoliko postoji traženi redosled, a `NE ` ukoliko takav redosled ne postoji.
	
	<br>
	
	Ukoliko je $t=1$, u drugoj liniji treba ispisati $n$ brojeva koji predstavljaju redosled kojim će ljudi da vide blog. 
	
	<br>
	
	Ukoliko je $t=0$, svakako smete ispisati redosled kojim će ljudi da vide blog, ali se neće uzimati u obzir radi bodovanja.
	
	<br>
	
	Ukoliko postoji više redosleda koji dovode do toga da uvaženost bloga bude tačno $k$, **ispisati bilo koji**.
	
	<br>
	
	## Primer 1
	
	<br>
	
	### Ulaz
	
	<br>
	
	```
	1
	5 3
	2 2 4 -1 3
	```
	
	<br>
	
	### Izlaz
	
	<br>
	
	```
	DA
	2 2 4 -1 3
	```
	
	<br>
	
	### Objašnjenje 
	
	Na samom početku će uvaženost bloga biti $0$. Nakon toga se dešava sledeće:
	- Prva osoba koja vidi blog smatra da njegova uvaženost treba da bude $2$. Zato će reći da joj se sviđa blog i njegova uvaženost postaje $1$.
	- Druga osoba koja vidi blog smatra da njegova uvaženost treba da bude $2$. Zato će reći da joj se sviđa blog i njegova uvaženost postaje $2$.
	- Treća osoba koja vidi blog smatra da njegova uvaženost treba da bude $4$. Zato će reći da joj se sviđa blog i njegova uvaženost postaje $3$.
	- Četvrta osoba koja vidi blog smatra da njegova uvaženost treba da bude $-1$. Zato će reći da joj se ne sviđa blog i njegova uvaženost postaje $2$.
	- Peta osoba koja vidi blog smatra da njegova uvaženost treba da bude $3$. Zato će reći da joj se sviđa blog i njegova uvaženost postaje $3$.
	
	<br>
	
	## Primer 2
	
	<br>
	
	### Ulaz
	
	<br>
	
	```
	0
	5 3
	2 2 4 -1 3
	```
	
	<br>
	
	### Izlaz
	
	<br>
	
	```
	DA
	```
	
	<br>
	
	### Objašnjenje 
	
	Indentično kao primer 1, ali je $t = 0$.
	
	<br>
	
	## Primer 3
	
	<br>
	
	### Ulaz
	
	<br>
	
	```
	1
	1 0
	1
	```
	
	<br>
	
	### Izlaz
	
	<br>
	
	```
	NE
	```
	
	<br>
	
	### Objašnjenje 
	
	Samo jedna osoba će videti blog pa ona mora biti prva. Blog na početku ima uvaženost $0$, a nakon što ga osoba sa mišljenjem $1$ vidi njegova uvaženost će biti $1$.
	
	<br>
	
	## Primer 4
	
	<br>
	
	### Ulaz
	
	<br>
	
	```
	1
	7 3
	2 2 -1 -2 3 6 -5 
	```
	
	<br>
	
	### Izlaz
	
	<br>
	
	```
	DA
	2 -5 -2 -1 6 3 2
	```
	
	<br>
	
	### Objašnjenje 
	
	Na samom početku će uvaženost bloga biti $0$. Nakon toga se dešava sledeće:
	- Prva osoba koja vidi blog smatra da njegova uvaženost treba da bude $2$. Zato će reći da joj se sviđa blog i njegova uvaženost postaje $1$.
	- Druga osoba koja vidi blog smatra da njegova uvaženost treba da bude $-5$. Zato će reći da joj se ne sviđa blog i njegova uvaženost postaje $0$.
	- Treća osoba koja vidi blog smatra da njegova uvaženost treba da bude $-2$. Zato će reći da joj se ne sviđa blog i njegova uvaženost postaje $-1$.
	- Četvrta osoba koja vidi blog smatra da njegova uvaženost treba da bude $-1$. Zato će reći da joj se sviđa blog i njegova uvaženost postaje $0$.
	- Peta osoba koja vidi blog smatra da njegova uvaženost treba da bude $6$. Zato će reći da joj se sviđa blog i njegova uvaženost postaje $1$.
	- Šesta osoba koja vidi blog smatra da njegova uvaženost treba da bude $3$. Zato će reći da joj se sviđa blog i njegova uvaženost postaje $2$.
	- Sedma osoba koja vidi blog smatra da njegova uvaženost treba da bude $2$. Zato će reći da joj se sviđa blog i njegova uvaženost postaje $3$.
	
	Postoje i drugi redosledi osoba kojima se postiže krajna uvaženost $3$, a Vi možete ispisati bilo koju.
	
	<br>
	
	## Ograničenja
	
	<br>
	
	 $t \in \{0,\ 1\}$
	 
	 $1 \le n \le 200\ 000$
	 
	 $-n \le k \le n+1$
	 
	 $-n \le a_i \le n$, za svako $1 \le i \le n$
	
	<br>
	
	Test primeri su podeljeni u devet disjunktnih grupa:
	 - U test primerima vrednim $3$ poena, važi $a_1 = a_2 = \ldots = a_n$;
	 - U test primerima vrednim $7$ poena, važi $n \le 8$;
	 - U test primerima vrednim $12$ poena, važi $n\le 500$, $a_i \in \{-1,\ 1\}$ za svako $1 \le i \le n$;
	 - U test primerima vrednim $13$ poena, važi $n\le 500$, $a_i = i$ za svako $1 \le i \le n$;
	 - U test primerima vrednim $10$ poena, važi da krajna uvaženost bloga ne može biti veća od $k$;
	 - U test primerima vrednim $13$ poena, važi $t = 0$;
	 - U test primerima vrednim $15$ poena, važi $n \le 500$;
	 - U test primerima vrednim $9$ poena, važi $n \le 5000$;
	 - U test primerima vrednim $18$ poena nema dodatnih ograničenja;
	 
	
=== "Rešenje"
	
	| Autor | Tekst i test primeri | Analiza rešenja | Testiranje |
	|:-:|:-:|:-:|:-:|
	| Nemanja Majski | Nemanja Majski | Anja Dožić | Anja Dožić |
	
	## Podzadatak 1: $a_1=a_2=...=a_n$
	Kako svi ljudi koji vide blog smatraju da njegova uvaženost treba da bude ista, u ovom podzadatku nam redosled kojim će ga oni videti neće biti važan, te možemo samo jednom proći kroz niz i izračunati koliku uvaženost će blog imati na kraju. Uvaženost koju smo izračunali je jedina uvaženost koju blog može imati, pa nam ostaje jedino da je uporedimo sa $k$.
	
	Vremenska složenost: $O(n)$
	
	## Podzadatak 2: $n\leq8$
	U ovom podzadatku je $n$ dovoljno malo, pa možemo da generišemo sve moguće redoslede kojima ljudi mogu da vide blog. Proći ćemo po jednom kroz svaki redosled i izračunati uvaženost koju on donosi. Ako naiđemo na redosled koji donosi uvaženost $k$, ispisujemo njega i ne proveravamo dalje.
	
	Vremenska složenost: $O(n\cdot n!)$
	
	## Podzadatak 5: krajnja uvaženost ne može biti veća od $k$
	Primetimo da ćemo maksimalnu uvaženost dobiti ako niz poređamo neopadajuće. Dakle, ako možemo dostići vrednost $k$, dostići ćemo je neopadajuće sortiranim nizom.
	
	Vremenska složenost: $O(n\cdot logn)$
	
	## Podzadatak 6: $t=0$
	Kao što smo u petom podzadatku videli, najveću uvaženost nam daje neopadajuće sortiran niz, slično možemo pokazati da najmanju daje niz koji sortiran nerastuće. Kako svaka rotacija dva elemnta menja uvaženost za $2, -2$ ili $0$, možemo zaključiti da je moguće naći permutaciju koja daje uvaženost $k$, za svako $k$ koje je između minimalne i maksimalne vrednosti i ima istu parnost kao i one (nerastući niz možemo odbiti od neopadaućeg konačnim brojem rotacija, gde svaka rotacija stvara novu permutaciju čija je vrednost u datom opsegu).
	
	Vremenska složenost: $O(n\cdot logn)$
	
	## Podzadatak 7: $n\leq500$
	Zamena mesta dva uzastopna elementa može da promeni uvaženost za $2, -2$ ili $0$. Dakle, ako krenemo od neopadajuće sortiranog niza koji ima maksimalnu uvaženost, i sortiramo ga Bubble sort-om nerastuće, svaka zamena mesta će menjati uvaženost za najviše $2$ po apsolutnoj vrednosti, i na kraju će je spustiti do minimalne moguće uvaženosti (kada niz potpuno sortiramo nerastuće). Odatle zaključujemo da će u nekom trenutku u sortiranju uvaženost morati da dostigne $k$ (prethodno proverimo da li je $k$ moguće dostići kao što smo radili i u šestom podzadatku), pa ćemo kada se to desi ispisati tu permutaciju niza.
	
	Vremenska složenost: $O(n^3)$
	
	## Podzadatak 9: bez dodatnih ograničenja
	Za celo rešenje, koristićemo se idejom iz sedmog podzadatka, samo ćemo je optimizovati.
	
	Radićemo dve binarne pretarge. Prva binarna pretraga služiće nam da odredimo koliko najviše elemenata sa kraja možemo da stavimo na početak u nerastućem poretku tako da uvaženost bude veća ili jednaka od $k$. Ona nam zamenjuje prvi deo Bubble sort-a, gde ćemo samo neke od elemenata poređati na početak niza. Zatim, sa fiksiranim brojem elemenata koje smo prebacili, radimo drugu binarnu pretragu. Ona će nam služiti da odredimo na koju poziciju stavljamo element koji je na kraju niza nakon prebacivanja, tj. zameniće nam ostatak soritranja (znamo da ta pozicija mora biti negde između njegove trenutne pozicije i prebačenih elemenata, jer bi u suprotnom i on bio prebačen).
	
	U trenutku kada dobijemo redosled čija je uvaženost $k$, ispisujemo ga.
	
	Vremenska složenost: $O(n\cdot logn)$
	
	## Drugi način
	U šestom podzadatku smo videli kako možemo da odredimo da li uvaženost može da dostigne $k$ ili ne. Ako smo zaključili da može, dalje lako možemo videti da nam onda treba da tačno $\frac{n-k}{2}$ ljudi smanji uvaženost, dok je njih $\frac{n+k}{2}$ povećava. Očigledno, izabraćemo $\frac{n-k}{2}$ najmanjih $a_i$ da budu oni koji spuštaju uvaženost, dok će je ostatak povećavati (ovaj izbor je dobar jer ako veći broj smanjuje uvaženost, smanjivaće je i manji; slično, ako manji broj povećava uvaženost, povećavaće je i veći). Sada nam ostaje samo da odredimo raspored kojim će oni da vide blog.
	
	Počećemo tako što ćemo ređati ljude koje smo odredili da podižu uvaženost u neopadajućem poretku sve dok ne naiđemo na nekog ko zbog svoje vrednosti $a_i$ treba da je spusti ili dok ih ne poređamo sve. Ako smo naišli na osobu koju smo odredili da treba da podiže uvaženost, a ona je zbog svoje vrednosti $a_i$ spušta, umesto nje krećemo da ređamo u nerastućem poretku one koje smo odredili da treba da spuštaju uvaženost. Znamo da će bar prvi kog postavimo spuštati uvaženost jer je po odabiru sigurno manji ili jednak $a_i$. Njih ređamo dok ih ne poređamo sve ili dok ne dođemo u situaciju da neki od njih podiže uvaženost zbog svoje vrednosti $a_i$. U toj situaciji ponovo krećemo da neopadajuće ređamo one koje smo odredili da podižu uvaženost. Nastavljamo postupak dok ne poređamo svh $n$ ljudi.
	
	Zašto ova konstrukcija radi? Zbog načina na koji ih ređamo, jasno je da će jedna od dve grupe "ispuniti svoj zadatak" prva, i da ćemo ostale iz druge grupe morati samo da poređamo kako je opisano ranije. Bez umanjenja opštosti, neka smo poređali sve ljude koje smo odredili da podižu uvaženost i ostalo nam je $m$ onih koji treba da je spuštaju. Kako smo ljude koji treba da spuštaju uvaženost ređali u nerastućem poretku, to znači da nam je ostalo $m$ najmanjih vrednosti $a_i$. Takođe, znamo da nam je uvaženost u tom trenutku $k+m$. Ako $m$ najmanjih ne bi moglo da smanji uvaženost na $k$, ni jedna druga $m-$torka takođe ne bi mogla, pa samim tim ne bismo mogli da dobijemo uvaženost $k$ za dati blog, što ne može da se desi jer smo na početku proverili da li je moguće dostići datu uvaženost. Analogno se dobija i za slučaj kada nam na kraju ostane $l$ ljudi koje smo odredili da podižu uvaženost.
	
	Vremenska složenost: $O(n\cdot logn)$
	
	``` cpp title="05_codeforces_blogovi.cpp" linenums="1"
	#include<bits/stdc++.h>
	#define ll long long
	using namespace std;
	const int maxn = 2e5+5;
	int n,k;
	int izracunaj(const vector<int> &v){
	    int r=0;
	    for(auto x:v)
	        if(r<=x)
	            r++;
	        else
	            r--;
	    return r;
	}
	vector<int> niz;
	void rezultat(vector<int> v){
	    cout<<"DA\n";
	    for(int i=0;i<v.size();i++)
	        cout<<v[i]<<" \n"[i==v.size()-1];
	    exit(0);
	}
	vector<int> generisi(int celih, int tren){
	    /*
	    0 <= celih <= n-1
	    0 <= tren <= n-celih-1
	
	    A..[tren]...|B....|C.|D..[celih]...
	
	    rD + A + C + B
	    */
	    vector<int> A;
	    for(int i=0;i<tren;i++)
	        A.push_back(niz[i]);
	    vector<int> B;
	    for(int i=tren;i<n-celih-1;i++)
	        B.push_back(niz[i]);
	    vector<int> C;
	    C.push_back(niz[n-celih-1]);
	    vector<int> D;
	    for(int i=n-celih;i<n;i++)
	        D.push_back(niz[i]);
	    reverse(D.begin(),D.end());
	
	    vector<int> R;
	    for(int x:D) R.push_back(x);
	    for(int x:A) R.push_back(x);
	    for(int x:C) R.push_back(x);
	    for(int x:B) R.push_back(x);
	
	    return R;
	}
	int main(){
	    int t;
	    cin>>t>>n>>k;
	    if(n%2 != k%2){
	        cout<<"NE\n";
	        return 0;
	    }
	    for(int i=1;i<=n;i++){
	        int x;
	        cin>>x;
	        niz.push_back(x);
	    }
	    sort(niz.begin(),niz.end());
	    int ub = izracunaj(niz);
	    if(ub==k)
	        rezultat(niz);
	    reverse(niz.begin(), niz.end());
	    int lb = izracunaj(niz);
	    if(lb==k)
	        rezultat(niz);
	
	
	    if(k<lb or k>ub){
	        cout<<"NE\n";
	        return 0;
	    }
	
	    int dg=0,gg=n-1,celih,sred;
	    while(dg<=gg){
	        sred=(dg+gg)/2;
	        vector<int> tmp = generisi(sred,0);
	        int v = izracunaj(tmp);
	        if(v==k)
	            rezultat(tmp);
	        if(v<k){
	            dg=sred+1;
	            celih = sred;
	        }
	        else
	            gg=sred-1;
	    }
	
	    int tren;
	    dg = 0;
	    gg = celih-n-1;
	    while(dg<=gg){
	        sred=(dg+gg)/2;
	        vector<int> tmp = generisi(celih,sred);
	        int v = izracunaj(tmp);
	        if(v==k)
	            rezultat(tmp);
	        if(v<k){
	            dg=sred+1;
	        }
	        else
	            gg=sred-1;
	    }
	    exit(-1);
	}

	```
