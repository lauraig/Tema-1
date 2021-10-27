# Tema-1
Formule propozitionale bine formate

Este un program care stabileste daca o expresie luata ca argument este o formula propozitionala bine formata sau nu.
Programul parcurge expresia element cu element, descriind fiecare pas parcurs si stabilind daca formula este sau nu bine formata.
O expresie este considerata o formula propozitionala bine formata, daca expresia a fost parcursa in intregime si arborele este complet, fara a mai ramane elemente necitite.


Ex.1: 
Pentru exprimarea formulei folositi urmatoarele caractere:
litere A-Z
cifre 0-9 
'!' - negatia
'&&' - conjunctia
'||' - disjunctia
'->' - implicatia
'<->' - echivalenta
'('  ')' - paranteze
Introduceti formula: (((P->Q)||S)<->T)
Pasul 0: '(' - urmeaza o propozitie compusa
 - urmeaza fie o negatie, fie o propozitie atomica sau compusa
Pasul 1: '(' - urmeaza o propozitie compusa
 - urmeaza fie o negatie, fie o propozitie atomica sau compusa
Pasul 2: '(' - urmeaza o propozitie compusa
 - urmeaza fie o negatie, fie o propozitie atomica sau compusa
Pasul 3: 'P' - propozitie atomica
Pasul 4: '->' - conector
 - urmeaza o propozitie atomica sau compusa
Pasul 5: 'Q' - propozitie atomica
Pasul 6: ')' - subarborele curent este complet
Pasul 7: '||' - conector
 - urmeaza o propozitie atomica sau compusa
Pasul 8: 'S' - propozitie atomica
Pasul 9: ')' - subarborele curent este complet
Pasul 10: '<->' - conector
 - urmeaza o propozitie atomica sau compusa
Pasul 11: 'T' - propozitie atomica
Pasul 12: ')' - arborele este complet
Formula propozitionala este bine formata

Ex.2:
Pentru exprimarea formulei folositi urmatoarele caractere:
litere A-Z
cifre 0-9 
'!' - negatia
'&&' - conjunctia
'||' - disjunctia
'->' - implicatia
'<->' - echivalenta
'('  ')' - paranteze
Introduceti formula: ((P->(Q&&(S->T))))
Pasul 0: '(' - urmeaza o propozitie compusa
 - urmeaza fie o negatie, fie o propozitie atomica sau compusa
Pasul 1: '(' - urmeaza o propozitie compusa
 - urmeaza fie o negatie, fie o propozitie atomica sau compusa
Pasul 2: 'P' - propozitie atomica
Pasul 3: '->' - conector
 - urmeaza o propozitie atomica sau compusa
Pasul 4: '(' - urmeaza o propozitie compusa
 - urmeaza fie o negatie, fie o propozitie atomica sau compusa
Pasul 5: 'Q' - propozitie atomica
Pasul 6: '&&' - conector
 - urmeaza o propozitie atomica sau compusa
Pasul 7: '(' - urmeaza o propozitie compusa
 - urmeaza fie o negatie, fie o propozitie atomica sau compusa
Pasul 8: 'S' - propozitie atomica
Pasul 9: '->' - conector
 - urmeaza o propozitie atomica sau compusa
Pasul 10: 'T' - propozitie atomica
Pasul 11: ')' - subarborele curent este complet
Pasul 12: ')' - subarborele curent este complet
Pasul 13: ')' - subarborele curent este complet
Pasul 14: - arborele este incomplet.
Formula propozitionala nu este bine formata.

Ex.3:
Pentru exprimarea formulei folositi urmatoarele caractere:
litere A-Z
cifre 0-9 
'!' - negatia
'&&' - conjunctia
'||' - disjunctia
'->' - implicatia
'<->' - echivalenta
'('  ')' - paranteze
Introduceti formula: (!(B(!Q))&&R)
Pasul 0: '(' - urmeaza o propozitie compusa
 - urmeaza fie o negatie, fie o propozitie atomica sau compusa
Pasul 1: '!' - negatie
 - urmeaza o propozitie atomica sau compusa
Pasul 2: '(' - urmeaza o propozitie compusa
 - urmeaza fie o negatie, fie o propozitie atomica sau compusa
Pasul 3: 'B' - propozitie atomica
Pasul 4: '( - arborele este incomplet.
Formula propozitionala nu este bine formata'
