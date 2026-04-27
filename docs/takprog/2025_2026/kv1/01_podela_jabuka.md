---
hide:
  - toc
---

# 1 - Podela jabuka

=== "Zadatak"
	
	| Vremensko ograničenje | Memorijsko ograničenje |
	|:-:|:-:|
	| 1000ms | 256MB |
	
	<br>
	Tri prijatelja – Don Huan, Selektor i Varijacije – doneli su na izlet određen broj jabuka.
	Don Huan ima $a$ jabuka, Selektor $b$, a Varijacije $c$.
	
	<br> 
	
	Tokom izleta igraju jednostavnu igru: kad god neko od njih podigne ruku, to znači da želi jabuku, i druga dvojica **moraju** da mu daju po jednu jabuku. Sve radnje obavljaju timski i niko se ne buni — pravila su jasna. Pazite da je **moguće** da neki od prijatelja ima negativan broj jabuka nakon što je dao jabuku. 
	
	<br> 
	
	Posle bilo kog broja poteza, zanima ih sledeće:
	Da li je moguće da, uz pametno biranje ko diže ruku u kojim trenucima, sva trojica na kraju završe sa **istim** brojem jabuka?
	
	<br> 
	
	Ukoliko im pomogneš da odgovore na to pitanje, možda ti daju par jabuka koje podstiču specijalne veštine za rešavanje zadataka.
	
	<br>
	
	## Opis ulaza
	
	<br>
	
	U prvoj i jedinoj liniji standardnog ulaza data su tri prirodna broja $a$, $b$ i $c$ - broj jabuka svakog od drugara.
	
	<br>
	
	## Opis izlaza
	
	<br>
	
	Potrebno je ispisati jednu liniju standardnog izlaza. Ukoliko je odgovor na njihovo pitanje moguće ispisati `DA`, u suprotnom ispisati `NE`.
	
	<br>
	
	## Primer 1
	
	<br>
	
	### Ulaz
	
	<br>
	
	```
	5 3 3
	```
	
	<br>
	
	### Izlaz
	
	<br>
	
	```
	NE
	```
	
	<br>
	
	### Primer 2
	
	<br>
	
	#### Ulaz
	
	<br>
	
	```
	7 1 4
	```
	
	<br>
	
	#### Izlaz
	
	<br>
	
	```
	DA
	```
	
	<br>
	
	## Ograničenja
	
	<br>
	
	 * $0 \leq a, b, c \leq 10^9$.
	
	<br>
	
	Test primeri su podeljeni u četiri disjunktne grupe: <br>
	 * U test primerima vrednim $25$ poena, važi da Don Huan nikad neće poneti jabuke na izlet, tj. $a = 0$. <br>
	 * U test primerima vrednim $25$ poena, važi da su vrednosti $a, b$ i $c$ najviše $10$. <br>
	 * U test primerima vrednim $25$ poena, važi da su vrednosti $a, b$ i $c$ najviše $200$. <br>
	 * U test primerima vrednim $25$ poena, nema dodatnih ograničenja. <br>
	
=== "Rešenje"
	
	| Autor | Tekst i test primeri | Analiza rešenja | Testiranje |
	|:-:|:-:|:-:|:-:|
	| Miloš Milutinović | Miloš Milutinović | Vasilije Novaković | Dragan Urošević |
	
	# Rešenje kada $a,b,c \le 200$.
	
	Na početku, Don Huan ima $a$ jabuka, Selektor ima $b$ jabuka, a Varijacije ima $c$ jabuka.
	
	Nazovimo proces u kom jedan prijatelj podigne ruku i dobije jabuke njegovom operacijom.
	
	Primetimo da redosled operacija nije bitan, jer će svaki prijatelj nakon nekih operacija imati
	$k = x + 2 \cdot y - z$, gde je:
	
	$k$: broj jabuka koje neki prijatelj ima nakon nekih operacija, 
	
	$x$: broj jabuka koje je imao pre operacija, 
	
	$y$: broj sopstvenih operacija, 
	
	$z$: broj tuđih operacija.
	
	$k$ očigledno ne zavisi od redosleda operacija, jer ništa u jednačini ne zavisi od redosleda operacija.
	
	Još jedna stvar koju možemo primetiti jeste da ako svaki prijatelj sazove po jednu operaciju, to je isto kao da je niko nije sazvao. Ovo znači da ako postoji način da sva trojica imaju jednak broj jabuka na kraju, moguće je to odraditi tako da samo dvojica rade operacije.
	Pošto je sopstvena operacija jedini način da se sopstveni broj jabuka poveća, očigledno je da će dva prijatelja sa najmanjim brojem jabuka jedini izvršavati operacije.
	
	Pretpostavimo da $a \le b \le c$, ako nije možemo ih samo zameniti tako da ova nejednakost važi.
	
	Sad, ako prvo radimo operacije da povećamo $b$, pa onda da povećamo $a$, očigledno nakon operacija na $b$, $b$ i $c$ moraju da budu jednaki, jer će nakon toga operacije na $a$ smanjivati oba broja podjednako.
	
	Možemo simulirati operacije na $b$ sve dok ne bude važilo $b \ge c$. Ako $b > c$ očigledno je odgovor NE, jer će operacijama na $a$ oba podjednako da se smanje, pa nikad neće biti jednaki.
	Ako $b = c$, simuliramo operacije na $a$, sve dok ne bude važilo $a \ge b$, to jest $a \ge c$.
	Sad, iz istog razloga, ako je $a > b$ odgovor je NE, a ako je $a = b = c$, odgovor je očigledno DA.
	
	Jednom operacijom, smanjićemo razliku između brojeva za $3$, pa je najveći mogući broj operacija $a+b$.
	
	Vremenska složenost: $O(a+b)$.
	Prostorna složenost: $O(1)$.
	
	# Glavno rešenje
	
	Primetimo da proces koji smo ranije radili ne moramo da simuliramo, već možemo brže da izračunamo.
	
	Naime, izjednačavanje $b$ i $c$ će se desiti ako i samo ako je $c - b$ deljivo sa $3$, jer jedna operacija povećava $b$ za $2$, a smanjuje $c$ za $1$.
	
	Ako nije deljivo sa $3$, očigledno će odgovor biti NE.
	Ako jeste, možemo zaključiti da ćemo uraditi $(c-b)/3$ operacija na $b$. Njih možemo sve odjednom primeniti tako što oduzmemo $(c-b)/3$ od $a$ i $c$, a dodamo $2 \cdot (c-b)/3$ na $b$.
	
	Sad važi $b = c$, i svaka operacija na $a$ će smanjiti $b$ i $c$ podjednako. Isto kao za $b$ i $c$, moramo da proverimo da li je $b-a$ deljivo sa $3$. Ako jeste, ne moramo ni da radimo operacije, jer znamo da će ih one izjednačiti, pa da je odgovor DA, ako nije, odgovor je NE.
	
	Ovo rešenje je dovoljno da kod prođe, ali možemo ga učiniti još jednostavnijim.
	
	Naime, rezultat operacije na $a$ je: $a$ postaje $a+2$, $b$ postaje $b-1$, $c$ postaje $c-1$.
	Primetimo da se međusobne razlike između svaka dva elementa ostale iste po modulu $3$.
	Takođe primetimo iz prethodno navedenog procesa, da nam je odgovor NE, samo ako u nekom trenutku razlika između neka dva elementa nije deljiva sa $3$.
	
	Ovo nas dovodi do zaključka da razlika svaka dva elementa mora biti deljiva sa $3$ na početku jer se to operacijama ne menja.
	Ako jeste, pokazali smo kako se rešenje dobija, ali dovoljno je samo ispisati DA.
	Ako nije, pokazali smo da je nemoguće dobiti rešenje, tako da se ispisuje NE.
	
	Vremenska i prostorna složenost: $O(1)$.
	
	``` cpp title="01_podela_jabuka.cpp" linenums="1"
	#include <bits/stdc++.h>
	
	using namespace std;
	
	int main() {
	  ios::sync_with_stdio(false);
	  cin.tie(nullptr);
	  long long a, b, c;
	  cin >> a >> b >> c;
	  int s = (a + b + c) % 3;
	  if (s != 0) {
	    cout << "NE";
	    return 0;
	  }
	  a %= 3;
	  b %= 3;
	  c %= 3;
	  if (a != b || b != c) {
	    cout << "NE";
	  } else {
	    cout << "DA";
	  }
	  return 0;
	}

	```
