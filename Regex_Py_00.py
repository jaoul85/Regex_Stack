import re
"""
Script per modificare una striga utilizzando una regex
prendendo esempio la stringa '(var1 * 1.3e4 + abc)/log(blabla+2E3)*1.2E+23'
ogni parola deve essere sostituito con 1, simboli, parentesi, operazioni non devono essere sostituite

1)re.escape vedere https://docs.python.org/2/library/re.html
1.1) questa funzione risulta utile per inserire il back slash davanti ai caratteri che non sono ascii
1.2) r"[+-]?\d*\.?\d+(?:e[+-]?\d+)?" :
		[+-]			->	seleziona solo i caratteri + e -
		[+-]?\d*		->	selezionare caratteri [+-] e precedentemente seguiti da una cifra 
		[+-]?\d*\.?\d+	-> come sopra ma aggiungiamo il . e un numero (in questo modo prendiamo cifre decimali) notare che la prima usiamo \d* e dopo \d+
		(?:e[+-]?\d+)?	-> gruppo passivo trova tutte le sequenze dei, la ? indica che possiamo avere zero o 1 ripetizioni di questa
		
	usati:
	[+-] , \d , * , + , ? , \. , (?:)
"""

exceptions = [
	re.escape("log"),
	re.escape("sin"),
	re.escape("cos"),
	r"[+-]?\d*\.?\d+(?:e[+-]?\d+)?"
	]

"""
dalla lista di exceptions usando .jon nella stringa unimo le varie ecezioni con pipe | il quale corrisponde alle alternative log|sin|cos|[+-]?\d*\.?\d+(?:e[+-]?\d+)?

nella espressione troveremo:
		\b 			->	indentifica il punto tra due caratteri che siano \w a sinistra e non \w a destra
		(?!pattern) ->	asserzione lookahead negativa, cioe' valida l' espressione precedente solo se la condizione patternnon e' verificata.
		regex completa in esempio:
		\b(?!(?:[+-]?\d*\.?\d+(?:e[+-]?\d+)?|log|sin|cos)\b)\w+\b
	
	alla fine tutte le parole trovare in questo caso var1,abc,blabla con "1"
"""

s = "(var1 * 1.3e4 + abc)/log(blabla+2E3)*1.2E+23"

print "stringa" , s

r = r"\b(?!(?:" + "|".join(exceptions) + r")\b)\w+\b"

print "regex" , r
 
print "re.sub" , re.sub(r, "1", s, 0, re.I)
