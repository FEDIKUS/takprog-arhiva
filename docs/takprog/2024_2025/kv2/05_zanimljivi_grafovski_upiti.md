---
hide:
  - toc
---

# 5 - Zanimljivi grafovski upiti

=== "Zadatak"
	
	| Vremensko ograničenje | Memorijsko ograničenje |
	|:-:|:-:|
	| 8500ms | 1024MB |
	
	Dat je graf sa $N$ čvorova i $M$ grana, gde svaki čvor $i$ ima vrednost $A_i$. 
	
	<br>
	
	Definišimo $S(a, b)$ - niz vrednosti $A_v$ za sve čvorove $v$ koji se nalaze na bar jednom prostom putu od čvora $a$ do čvora $b$.  Prost put od čvora $a$ do čvora $b$ je niz različitih čvorova $v_1, v_2, ..., v_k$, gde je $v_1 = a$ i $v_k = b$ i za svako $1 \leq i \leq k-1$ važi da su $v_i$ i $v_{i+1}$ povezani granom.
	
	<br>
	
	Dato je $Q$ upita oblika $(a, b)$, potrebno je naći $median(S(a, b))$, gde $median(A)$ predstavlja medijanu niza $A$. Medijana niza $A_1, A_2, ..., A_m$ predstavlja element $A_{\lceil m/2 \rceil}$ kada $A$ sortiramo rastuće, gde $m$ predstavlja dužinu niza $A$. Oznaka $\lceil x \rceil$ predstavlja zaokruživanje na najmanji ceo broj veći od ili jednak $x$.
	
	<br>
	
	Upiti se generišu na sledeći način. Neka je niz $ans_i$ odgovor na $i$-ti upit i $ans_0 = 0$. Za svaki upit su nam data po dva broja $a_1$ i $b_1$. Onda je: $a = (a_1 + ans_{i - 1} * P - 1) \% N + 1$ i $b = (b_1 + ans_{i - 1} * P - 1) \% N + 1$, gde je $i$ broj upita i $P$ dati parametar. 
	
	<br>
	
	## Opis ulaza
	
	<br>
	
	U prvoj liniji standardnog ulaza data su četiri cela broja $N$, $M$, $Q$ i $P$, redom broj čvorova u grafu, broj grana u grafu, broj upita i parametar za generisanje upita.
	
	<br>
	
	U drugoj liniji standardnog ulaza dato je $N$ celih brojeva $A_i$, gde $i$-ti broj predstavlja vrednost čvora $i$.
	
	<br>
	
	U narednih $M$ linija standardnog ulaza data su po dva cela broja $u$ i $v$, koji označavaju da postoji grana između čvorova $u$ i $v$.
	
	<br>
	
	U narednih $Q$ linija standardnog ulaza data su po dva cela broja $a_1$ i $b_1$, dva broja pomoću kojih izračunavamo vrednosti $a$ i $b$.
	
	<br>
	
	**Napomena:** Obratiti pažnju na veliku količinu podataka na ulazu. 
	
	<br>
	
	## Opis izlaza
	
	<br>
	
	U $Q$ linija standardnog izlaza potrebno je ispisati rešenje za svaki upit. U $i$-toj liniji se nalazi odgovor na $i$-ti upit. 
	
	<br>
	
	## Primer 1
	
	<br>
	
	### Ulaz
	
	<br>
	
	```
	6 6 7 0
	1 2 3 4 5 6
	1 2
	2 4
	4 3
	3 1
	5 4
	4 6
	1 1
	2 1
	1 4
	4 6
	5 6
	5 1
	3 5
	```
	
	<br>
	
	### Izlaz
	
	<br>
	
	```
	1
	2
	2
	4
	5
	3
	3
	```
	<br>
	
	### Objašnjenje
	
	<br>
	
	Jedini put od čvora $1$ do čvora $1$ je put koji sadrži samo čvor 1. Tako da je $S(1,1) = {1}$, a njegova medijana je 1.
	
	Od čvora $2$ do čvora $4$ postoje $2$ puta. 2, 4 i 2, 1, 3, 4. $S(1,2) = {1, 2, 3, 4}$, a njegova medijana je 2.
	
	<br>
	
	## Primer 2
	
	<br>
	
	### Ulaz
	
	<br>
	
	```
	6 7 3 1
	7 8 9 10 11 12
	1 2
	1 3
	2 3
	3 4
	4 5
	4 6
	5 6
	1 6
	1 2
	5 3
	```
	
	<br>
	
	### Izlaz
	
	<br>
	
	```
	9
	11
	8
	```
	
	<br>
	
	### Objašnjenje
	
	<br>
	
	Vrednosti $a$ i $b$ su redom ($1$, $6$), ($4$, $5$) i ($4$, $2$).
	
	<br>
	
	## Ograničenja
	
	- $1 \leq N, M, Q \le 500.000$
	- $0 \leq P \leq 1$
	
	- $1 \leq A_i \le 10^9$
	
	- $1 \leq u, v \le N$, $u \neq v$
	
	- $1 \leq a_1, b_1 \leq N$
	
	- Može postojati više grana između neka dva čvora
	
	- Graf je povezan, tj. postoji prost put između svaka dva čvora
	
	<br>
	
	Test primeri su podeljeni u 8 disjunktnih grupa:
	
	 - U testovima vrednim 5 poena: $N, Q \leq 2.000$ i graf će biti stablo
	 - U testovima vrednim 5 poena: $N, Q \leq 2.000$
	 - U testovima vrednim 5 poena: $A_i \leq 3$
	 - U testovima vrednim 15 poena: graf će biti stablo
	 - U testovima vrednim 15 poena: $N, Q \leq 100.000$ i $P = 0$
	 - U testovima vrednim 15 poena: $N, Q \leq 100.000$
	 - U testovima vrednim 15 poena: $P = 0$
	 - U testovima vrednim 25 poena: bez dodatnih ograničenja.
	  
	<br>
	
	
=== "Rešenje"
	
	| Autor | Tekst i test primeri | Analiza rešenja | Testiranje |
	|:-:|:-:|:-:|:-:|
	| Miloš Milutinović | Miloš Milutinović, Nemanja Majski, Toni Škrijelj | Miloš Milutinović | Aleksa Milisavljević |
	
	## Rešenje kada je $N, Q \leq 2.000$ i graf je stablo
	
	Možemo pustiti DFS algoritam od čvora $a$ do čvora $b$ i naći sve vrednosti na tom putu. Zatim je lako odrediti medijanu.
	
	## Rešenje kada je $N, Q \leq 2.000$
	
	Ovaj podzadatak je namenjen implementacijama sa lošijim složenostima.
	
	## Rešenje kada je graf stablo
	
	U ovom podzadatku i za naredne će nam biti potrebna struktura podataka perzistentno segmentno stablo. Za svaki čvor ćemo čuvati verziju segmentnog stabla u kome će biti vrednosti čvorova na putu od korena stabla do baš tog čvora. Ovo je moguće napraviti tokom jednog DFS obilaska. Zatim da bi odgovorili na upite, možemo uraditi šetnju nad perzistentnim stablom, konkretnije nad $pst_a + pst_b - pst_{LCA(a,b)} - pst_{par_{LCA(a,b)}}$, gde $pst_v$ označava verziju perzistentnog segmentnog stabla za čvor $v$, $LCA(a,b)$ najnižeg zajedničkog pretka čvorova $a$ i $b$ i $par_v$ roditelja čvora $v$. 
	
	## Kako dalje?
	
	Možemo koristiti *block-cut* stablo. To stablo se dobija kada izbrišemo sve artikulacione tačke i svaku komponentu koju dobijemo, nakon brisanja, nazovemo jednim blokom. Zatim svaki blok predstavimo kao nov čvor i njega povežemo sa svim čvorovima unutar tog bloka i susednim artikulacionim tačkama. Lako se vidi da će to zapravo predstavljati stablo. Nakon njegove konstrukcije primetimo da svi čvorovi čvorovi koji se nalaze na nekom prostom puty od čvora $a$ do čvora $b$ se zapravo nalaze na prostom putu od čvora $a$ do čvora $b$ u *block-cut* stablu, ukoliko kažemo da "blok" čvor predstavlja sve njegove susedne čvorove.
	
	## Rešenje kada je $A_i \leq 3$
	
	Nakon konstrukcije možemo pamtiti broj pojavljivanja svake vrednosti na putu od korena do svakog čvora. Zatim je lako odgovoriti na upite.
	
	## Rešenje kada je $N, Q \leq 100.000$ i $P = 0$
	
	Moguće je primeniti paralelnu binarnu pretragu po rešenju i čuvati segmentno stablo koje će nam čuvati koliko imamo pojavljivanja čvorova sa vrednostima $A_v \leq mid$ ako je $mid$ trenutni parametar u paralelnoj binarnoj pretrazi, od korena do svakog čvora. Vremenska složenost je $O((N + Q) \cdot {{\log^2 N}})$.
	
	## Rešenje kada je $N, Q \leq 100.000$
	
	Rešenje za ovaj podzadatak je isto kao rešenje celog zadatka, osim što je dozvoljeno koristiti binarnu pretragu po rešenju umesto šetnje po segmentnom stablu.
	
	## Glavno rešenje
	
	Moguće je napraviti perzistentno segmentno stablo nad *block-cut* stablom i upite odgovarati isto kao u podzadatku gde je graf zapravo stablo. Vremenska složenost je $O((N + Q) \cdot {\log N})$.
	
	``` cpp title="05_zanimljivi_grafovski_upiti.cpp" linenums="1"
	#include<bits/stdc++.h>
	#define ll long long
	using namespace std;
	const int maxn=5e5+5,logg=18;
	int N,M,Q,P,niz[maxn],niz2[maxn],PST_SIZE;
	map<int,int> encode;
	int brc[maxn],ccount,bc_par[maxn],croot[maxn];
	int rod[maxn],decode[maxn],dub[maxn],dp[maxn];
	int lcniz[2*maxn],st[(1<<21)+5],in[maxn],out[maxn],vrem=0;
	vector<int> stablo[maxn],poz[maxn],vrednosti[maxn];
	vector<int> koji[maxn],graf[maxn],backedge[maxn],dfst[maxn],red;
	void kompresuj(){
	   for(int i=1;i<=N;i++)
	      niz2[i]=niz[i];
	   sort(niz2+1,niz2+1+N);
	   encode[niz2[1]]=1;
	   decode[1]=niz2[1];
	   int br=1;
	   for(int i=2;i<=N;i++){
	      if(niz2[i]==niz2[i-1])
	         continue;
	      br++;
	      encode[niz2[i]]=br;
	      decode[br]=niz2[i];
	   }
	   for(int i=1;i<=N;i++)
	      niz[i]=encode[niz[i]];
	}
	void dfs0(int gde,int pret,int d){
	   red.push_back(gde);
	   rod[gde]=pret;
	   dub[gde]=d;
	   dfst[pret].push_back(gde);
	   for(int x:graf[gde]){
	      if(dub[x]==0)
	         dfs0(x,gde,d+1);
	      else
	         backedge[gde].push_back(x);
	   }
	}
	void build(int gde,int root,int pret,int comp){
	   croot[comp]=root;
	   brc[gde]=comp;
	   for(int x:dfst[gde]){
	      if(x==pret)
	         continue;
	      if(dp[x]<dub[gde]){ /// Nalaze se u istoj komponenti
	         build(x,root,gde,comp);
	         continue;
	      }
	 
	      ++ccount;
	      bc_par[ccount]=comp;
	 
	      if(dp[x]==dub[gde]){ /// Gde je artikulaciona i razdvaja komponentu ispod, pravimo novu komponentu, sa root-om gde
	         build(x,gde,gde,ccount);
	         continue;
	      }
	      /// Most
	      build(x,x,gde,ccount);
	   }
	}
	void napravi_stablo(){
	   dfs0(1,0,1);
	   reverse(red.begin(),red.end());
	   for(int x:red){
	      dp[x]=dub[x];
	      for(int y:backedge[x])
	         dp[x]=min(dp[x],dub[y]);
	      for(int y:dfst[x])
	         dp[x]=min(dp[x],dp[y]);
	   }
	   reverse(red.begin(),red.end());
	   build(1,1,1,++ccount);
	   for(int i=1;i<=N;i++)
	      koji[brc[i]].push_back(i);
	   for(int i=1;i<=ccount;i++)
	      stablo[bc_par[i]].push_back(i);
	}
	int spoj(int a,int b){
	   if(in[a]<in[b])
	      return a;
	   return b;
	}
	void buildst(){
	   int k=(1<<(logg+2));
	   for(int i=k;i<k+vrem;i++)
	      st[i]=lcniz[i-k+1];
	   for(int i=k-1;i>=1;i--)
	      st[i]=spoj(st[i*2],st[i*2+1]);
	}
	int obicanget(int lg,int dg,int gde=1,int lc=1,int dc=(1<<(logg+2))){
	   if(lg==lc and dg==dc){
	      return st[gde];
	   }
	   int sred=(lc+dc)/2;
	   if(dg<=sred)
	      return obicanget(lg,dg,gde*2,lc,sred);
	   if(lg>sred)
	      return obicanget(lg,dg,gde*2+1,sred+1,dc);
	   int v1,v2;
	   v1=obicanget(lg,sred,gde*2,lc,sred);
	   v2=obicanget(sred+1,dg,gde*2+1,sred+1,dc);
	   return spoj(v1,v2);
	}
	int lca(int a,int b){
	   return obicanget(min(in[a],in[b]),max(out[a],out[b]));
	}
	int kapar(int x,int lc){
	   auto it=upper_bound(poz[lc].begin(),poz[lc].end(),in[x]);
	   it--;
	   int p=(*it);
	   p++;
	   return lcniz[p];
	}
	struct pstcvor{
	   int vred;
	   int d[2];
	} pst[maxn*(logg+2)+200];
	int sz=0,psroot[maxn];
	int novi(){
	   ++sz;
	   pst[sz].vred=pst[sz].d[0]=pst[sz].d[1]=0;
	   return sz;
	}
	int kopiraj(int x){
	   ++sz;
	   pst[sz]=pst[x];
	   return sz;
	}
	void dodaj(int gde,int x,int lc=0,int dc=(1<<(logg+1))-1){
	   pst[gde].vred++;
	   if(lc==dc)
	      return;
	   int sred=(lc+dc)/2;
	   if(x<=sred)
	      dodaj(pst[gde].d[0]=kopiraj(pst[gde].d[0]),x,lc,sred);
	   else
	      dodaj(pst[gde].d[1]=kopiraj(pst[gde].d[1]),x,sred+1,dc);
	   return;
	}
	int add(int root,int sta){
	   root=kopiraj(root);
	   dodaj(root,sta);
	   return root;
	}
	inline int getsum(const vector<int> &A,const vector<int> &B,bool d0=false){
	   int s=0;
	   for(int x:A){
	      if(d0)
	         s+=pst[pst[x].d[0]].vred;
	      else
	         s+=pst[x].vred;
	   }
	   for(int x:B){
	      if(d0)
	         s-=pst[pst[x].d[0]].vred;
	      else
	         s-=pst[x].vred;
	   }
	   return s;
	}
	int walk(vector<int> &A,vector<int> &S,int k,int poz=0,int val=(1<<logg)){
	   if(val==0)
	      return poz;
	   int s=getsum(A,S,true);
	   if(s>=k){
	      for(int i=0;i<A.size();i++)
	         A[i]=pst[A[i]].d[0];
	      for(int i=0;i<S.size();i++)
	         S[i]=pst[S[i]].d[0];
	      return walk(A,S,k,poz,val>>1);
	   }
	   k-=s;
	   poz+=val;
	   for(int i=0;i<A.size();i++)
	      A[i]=pst[A[i]].d[1];
	   for(int i=0;i<S.size();i++)
	      S[i]=pst[S[i]].d[1];
	   return walk(A,S,k,poz,val>>1);
	}
	void dfs(int gde,int proot){
	   vrem++;
	   in[gde]=out[gde]=vrem;
	   lcniz[vrem]=gde;
	   poz[gde].push_back(vrem);
	   for(int x:koji[gde])
	      proot=add(proot,niz[x]);
	   psroot[gde]=proot;
	   for(int x:stablo[gde]){
	      dfs(x,proot);
	      vrem++;
	      poz[gde].push_back(vrem);
	      lcniz[vrem]=gde;
	      out[gde]=vrem;
	   }
	   return;
	}
	void sveukomp(){
	   for(int i=2;i<=ccount;i++){
	      for(int x:koji[i])
	         vrednosti[i].push_back(niz[x]);
	      vrednosti[i].push_back(niz[croot[i]]);
	      sort(vrednosti[i].begin(),vrednosti[i].end());
	   }
	}
	int medijan(const vector<int> &V){
	   return V[(V.size()-1)/2];
	}
	int upit(int a,int b){
	   if(a==b)
	      return niz[a];
	   if(brc[a]==brc[b] or croot[brc[b]]==a or croot[brc[a]]==b){ /// Ista komponenta
	      int komp=brc[a];
	      if(croot[brc[b]]==a)
	         komp=brc[b];
	      return medijan(vrednosti[komp]);
	   }
	   vector<int> A,S;
	   int ka,kb;
	   ka=brc[a];
	   kb=brc[b];
	   int lc=lca(ka,kb);
	   if(ka==lc){
	      swap(a,b);
	      swap(ka,kb);
	   }
	   sz=PST_SIZE; /// Pravimo update-e, ali nas bas briga sta su menjali prethodni upiti pa to overwrite-ujemo
	   int roota=psroot[ka];
	 
	   if(kb==lc){
	      int sa=kapar(ka,lc);
	      if(croot[sa]==b){
	         roota=add(roota,niz[b]);
	         A.push_back(roota);
	         S.push_back(psroot[lc]);
	      }
	      else{
	         roota=add(roota,niz[croot[lc]]);
	         A.push_back(roota);
	         S.push_back(psroot[bc_par[lc]]);
	      }
	   }
	   else{
	      int sa=kapar(ka,lc);
	      int sb=kapar(kb,lc);
	      if(croot[sb]==croot[sa]){
	         roota=add(roota,niz[croot[sa]]);
	         A.push_back(roota);
	         A.push_back(psroot[kb]);
	         S.push_back(psroot[lc]);
	         S.push_back(psroot[lc]);
	      }
	      else{
	         roota=add(roota,niz[croot[lc]]);
	         A.push_back(roota);
	         A.push_back(psroot[kb]);
	         S.push_back(psroot[lc]);
	         S.push_back(psroot[brc[croot[lc]]]);
	      }
	   }
	   return walk(A,S,(getsum(A,S)+1)/2);
	}
	int main(){
	   ios_base::sync_with_stdio(false);
	   cin.tie(0);
	   cin>>N>>M>>Q>>P;
	   for(int i=1;i<=N;i++)
	      cin>>niz[i];
	   for(int i=1;i<=M;i++){
	      int a,b;
	      cin>>a>>b;
	      graf[a].push_back(b);
	      graf[b].push_back(a);
	   }
	   kompresuj();
	   napravi_stablo();
	   dfs(1,0);
	   buildst();
	   sveukomp();
	 
	   croot[1]=0;
	   psroot[0]=0;
	   PST_SIZE=sz;
	   int ans=0;
	   while(Q--){
	      int a,b;
	      cin>>a>>b;
	      a=(a+ans*P-1)%N+1;
	      b=(b+ans*P-1)%N+1;
	      ans=decode[upit(a,b)];
	      cout<<ans<<"\n";
	   }
	}

	```
