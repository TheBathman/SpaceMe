#Osnovne informacije:
* Igra se na kvadratni n x n mreži (n>4).
* Cilj je zasesti čim večjo površino.
* Igra se konča, ko prvemu igralcu zmanka potez.
* Igro začne X

#Potek:
  * Igralca začneta v nasprotnih vogalih mreže vsak s svojim pobarvanim kvadratkom
    * Na voljo imata dva tipa potez:
      * Dupliciranje: igralec zasede eno od sosednjih polj (pobarva s svojo barvo)
      * Skok: igralec premakne eno od obsotoječih polj za točno 2 polji stran (rob 5x5 kvadrata s središčem v izbranem polju)
  * Če igralec zasede polje, ki meji na nasprotnikova, postanejo tudi ta njegova
  * Igra poteka izmenično, igralec na vrsti opravi eno potezo
  
##Primer prvih nekaj potez:
###Začetna postavitev:
    +---+---+---+---+---+---+---+
    | X |   |   |   |   |   |   |
    +---+---+---+---+---+---+---+
    |   |   |   |   |   |   |   |
    +---+---+---+---+---+---+---+
    |   |   |   |   |   |   |   |
    +---+---+---+---+---+---+---+
    |   |   |   |   |   |   |   |
    +---+---+---+---+---+---+---+
    |   |   |   |   |   |   | O |
    +---+---+---+---+---+---+---+

###Prva poteza:
    +---+---+---+---+---+---+---+
    | X | X |   |   |   |   |   |
    +---+---+---+---+---+---+---+
    |   |   |   |   |   |   |   |
    +---+---+---+---+---+---+---+
    |   |   |   |   |   |   |   |
    +---+---+---+---+---+---+---+
    |   |   |   |   |   |   |   |
    +---+---+---+---+---+---+---+
    |   |   |   |   |   |   | O |
    +---+---+---+---+---+---+---+
X se duplicira na sosednje polje.

###Druga poteza:
    +---+---+---+---+---+---+---+
    | X | X |   |   |   |   |   |
    +---+---+---+---+---+---+---+
    |   |   |   |   |   |   |   |
    +---+---+---+---+---+---+---+
    |   |   |   |   | 0 |   |   |
    +---+---+---+---+---+---+---+
    |   |   |   |   |   |   |   |
    +---+---+---+---+---+---+---+
    |   |   |   |   |   |   |   |
    +---+---+---+---+---+---+---+
Krogec skoči (nujno se more premakniti za 2 polji).

###Tretja poteza:
    +---+---+---+---+---+---+---+
    | X | X | X |   |   |   |   |
    +---+---+---+---+---+---+---+
    |   |   |   |   |   |   |   |
    +---+---+---+---+---+---+---+
    |   |   |   |   | 0 |   |   |
    +---+---+---+---+---+---+---+
    |   |   |   |   |   |   |   |
    +---+---+---+---+---+---+---+
    |   |   |   |   |   |   |   |
    +---+---+---+---+---+---+---+
X se še enkrat duplicira.

###Četrta poteza:
    +---+---+---+---+---+---+---+
    | X | 0 | 0 |   |   |   |   |
    +---+---+---+---+---+---+---+
    |   |   | 0 |   |   |   |   |
    +---+---+---+---+---+---+---+
    |   |   |   |   |   |   |   |
    +---+---+---+---+---+---+---+
    |   |   |   |   |   |   |   |
    +---+---+---+---+---+---+---+
    |   |   |   |   |   |   |   |
    +---+---+---+---+---+---+---+
Krogec skoči in zavzame sosednja polja.

###Peta poteza:
    +---+---+---+---+---+---+---+
    | X | X | X |   |   |   |   |
    +---+---+---+---+---+---+---+
    |   | X | X |   |   |   |   |
    +---+---+---+---+---+---+---+
    |   |   |   |   |   |   |   |
    +---+---+---+---+---+---+---+
    |   |   |   |   |   |   |   |
    +---+---+---+---+---+---+---+
    |   |   |   |   |   |   |   |
    +---+---+---+---+---+---+---+
X se duplicira, zavzame vsa polja krogca in zmaga.
