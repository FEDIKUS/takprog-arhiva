---
hide:
  - toc
---

# B3 - Abakus 2

=== "Zadatak"
	
	| Vremensko ograničenje | Memorijsko ograničenje |
	|:-:|:-:|
	| 1000ms | 256MB |
	
	
	<br>
	
	Komisija za srednjoškolska takmičenja iz programiranja je pre skoro cele decenije konstatovala: *"Stari Vavilonci su koristili jednu varijantu naprave Abakus za komplikovana matematička izračunavanja..."*. Vi ste sada pronašli taj Abakus (logično, pronašli ste ga na 3000m nadmorske visine u komisijskom gnezdu, gde se čuvaju stara takmičenja).
	
	<br>
	
	Ono što je malo poznato, jeste da Abakus nudi i zadatak. Kao nagradu za rešavanje zadatka, Abakus će Vas vratiti u davnu 2016-tu (što je jako dobro, jer znate rešenja svih zadataka sa prošlih takmičenja).
	
	<br>
	
	Abakus može da za zadati prirodan broj da izračuna proizvod njegovih cifara (na primer, za broj $123$, Abakus bi vratio vrednost $6=1\cdot 2\cdot 3$. Slično, za vrednost $1024$, Abakus bi vratio vrednost $0=1\cdot 0\cdot 2\cdot 4$). Vaš zadatak je da za zadat broj $n$ izračunate koliko različitih vrednosti bi Abakus vratio ukoliko bi mu se uneli brojevi $1,2,\ldots,n$.
	
	<br>
	
	Kako biste bili sasvim sigurni u Vaše rešenje, morate da odgovorite na $T$ upita, gde u svakom upitu dobijete broj $n$ i za svaki upit rešavate opisani zadatak. Ako pogrešite, Abakus Vas vraća u 2006-tu umesto 2016-te, a te zadatke već niste uvežbali...
	 
	<br>
	
	## Opis ulaza
	
	<br>
	
	U prvoj liniji standardnog ulaza dat je prirodan broj $T$, broj upita.
	
	<br>
	
	U narednih $T$ linija standardnog ulaza, nalazi se po jedan prirodan broj - $n$. 
	
	<br>
	
	## Opis izlaza
	
	<br>
	
	Za svaki od $T$ upita treba ispisati jednu liniju standardnog izlaza koja sadrži jedan ceo broj - broj različitih vrednosti koje će Abakus ispisati za unete brojeve $1,2,\ldots,n$.
	
	<br>
	
	## Primer 1
	
	<br>
	
	### Ulaz
	
	<br>
	
	```
	3
	1
	10
	13
	```
	
	<br>
	
	### Izlaz
	
	<br>
	
	```
	1
	10
	10
	```
	
	### Objašnjenje
	
	<br>
	 
	   - U prvom upitu, Abakusu dajemo samo broj $1$, njegov proizvod cifara jednak je $1$ i to je jedina vrednost koju će Abakus vratiti. Ispis je onda $1$.
	   - U drugom upitu, Abakusu dajemo brojeve $1,2,3,4,5,6,7,8,9,10$ i proizvodi cifara ovih brojeva su redom $1,2,3,4,5,6,7,8,9,0$ - i tu imamo $10$ različitih vrednosti, pa i ispisujemo $10$.
	   - U trećem upitu, Abakusu dajemo brojeve $1,2,3,4,5,6,7,8,9,10,11,12,13$ i proizvodi cifara ovih brojeva su redom $1,2,3,4,5,6,7,8,9,0,1,2,3$ - i tu imamo ponovo $10$ različitih vrednosti, pa i ispisujemo $10$. (Primetimo da su poslednja tri vraćena broja duplikati, pa ispis nije $13$).
	
	<br>
	
	## Primer 2
	
	<br>
	
	### Ulaz
	
	<br>
	
	```
	1
	111
	```
	
	<br>
	
	### Izlaz
	
	<br>
	
	```
	37
	```
	
	<br>
	
	## Ograničenja
	
	
	<br>
	
	
	- $1 \leq T \leq 200.000$
	- $1 \leq n \leq 10^{18}$ 
	
	
	<br>
	
	Test primeri su podeljeni u $8$ disjunktnih grupa:
	
	   
	   - U testovima vrednim $5$ poena: važi $n \leq 10$
	   - U testovima vrednim $5$ poena: važi $n \leq 100$.
	   - U testovima vrednim $10$ poena: važi $n \leq 10.000$.
	   - U testovima vrednim $10$ poena: važi $n \leq 1.000.000$.
	   - U testovima vrednim $10$ poena: važi $n \leq 10^9$.
	   - U testovima vrednim $10$ poena: važi $n \leq 10^{12}$.
	   - U testovima vrednim $10$ poena: važi $T = 1$.
	   - U testovima vrednim $10$ poena: važi $T \leq 1.000$.
	   - U testovima vrednim $30$ poena: bez dodatnih ograničenja.
	
	<br>
	
=== "Rešenje"
	
	| Autor | Tekst i test primeri | Analiza rešenja | Testiranje |
	|:-:|:-:|:-:|:-:|
	| Marko Milenković | Marko Milenković | Marko Milenković | Miloš Milutinović |
	
	### $N \leq 1.000.000$
	
	Za najmanja ograničenja, gde je $N$ do milion, možemo primeniti direktnu simulaciju ("brut fors"). Potrebno je proći kroz svaki prirodni broj $i$ od $1$ do $n$, izračunati proizvod njegovih cifara i taj rezultat ubaciti u strukturu podataka koja čuva samo jedinstvene vrednosti (na primer std::set u C++-u). Proizvod cifara se računa jednostavnim izdvajanjem poslednje cifre (operacija % 10) i celobrojnim deljenjem (operacija / 10) sve dok broj ne postane nula. Na kraju, rešenje je veličina skupa u koji smo smeštali proizvode. Vremenska složenost ovog pristupa je $O(N \cdot \log_{10} N)$, što se za $N=10^6$ izvršava dovoljno brzo.
	
	### $N \leq 10^{12}$
	
	
	Direktna iteracija je prespora. Primetimo da redosled cifara ne utiče na njihov proizvod. Na primer, brojevi $124$, $421$ i $214$ svi daju isti proizvod $8$. To znači da je dovoljno posmatrati samo kombinacije cifara, a ne sve permutacije. Možemo koristiti rekurzivnu pretragu da generišemo nizove cifara koje su neopadajuće. Time osiguravamo da svaku kombinaciju cifara obradimo samo jednom. Za svaki generisani niz cifara, najmanji broj koji se od njih može sastaviti dobija se nadovezivanjem tih cifara u rastućem poretku. Ako je taj najmanji broj manji ili jednak zadatom $N$, njegov proizvod cifara ubacujemo u skup rešenja.
	
	
	### Bez dodatnih ograničenja
	
	Možemo primetiti da se proizvod cifara sastoji od proizvoda prostih brojeva $2,3,5,7$, jer se svaki broj može predstaviti preko proste faktorizacije, a prosti brojevi posle $7$ ne čini cifre (dvocifreni su).
	
	Računaćemo koji je najmanji prirodan broj čiji je proizvod cifara jednak $2^a3^b5^c7^d$, a onda iterirati po svim mogućnostima brojeva $a,b,c,d$. Sve ove brojeve čuvamo u sortiranoj listi.
	
	Da bismo napravili što manji broj, gledamo da ispoštujemo dva pravila:
	
	1) Pakujemo proste činioce u što veće brojeve - dakle $2^3$ u $8$, $3^2$ u $9$, a ako nam ostanu neka dvojka i trojka posle toga, pakujemo ih u $6$. Ako nakon toga ostanu dvojke, pakujemo ih u četvorku. Može se proveriti da su ovo jedine mogućnosti.
	
	2) Sortiramo cifre rastuće da bismo ostvarili što manji broj.
	
	Dodatno imamo specijalne slučajeve za $1$ i $10$, jer oni prvi proizvode brojeve $1$ i $0$. Dalje iteriramo po četvorci $a,b,c,d$ i pritom pazimo da ne pređemo granicu velikih brojeva u C++-u.
	
	Sve radimo pre ikakvog unosa i onda možemo binarnom pretragom da pronađemo za svako $N$ koji je prvi broj koji je manji od $N$. 
