print("Pentru exprimarea formulei folositi urmatoarele caractere:\nlitere A-Z\ncifre 0-9 \n'!' - negatia\n'&&' - conjunctia\n'||' - disjunctia\n'->' - implicatia\n'<->' - echivalenta\n'('  ')' - paranteze")
formula = input("Introduceti formula: ")
#my_formula_list = list(set(formula))
#my_symbols_list = []
#ok = 1
count = 0
step = 0
#symbols = ["!", "&", "|", "(", ")", "-", ">", "<"];
#for el in my_formula_list:
#  if el.isalnum() == False:
#    my_symbols_list.append(el)
#for el in my_symbols_list:
#  if el not in symbols:
#    ok = 0
#    break
if formula[0] != "(":
  print("This is not a well formed formula")
else:
  i = 0
  while i < len(formula):
    if formula[i] == "(":
      print(f"Pasul {step}: '{formula[i]}' - urmeaza o propozitie compusa\n - urmeaza fie o negatie, fie o propozitie atomica sau compusa")
      step += 1
      if formula[i+1] == "!" or formula[i+1] == "(" or formula[i+1].isalpha() == 1:
        i += 1
        continue
      else:
        print(f"Pasul {step}: '{formula[i+1]} - arborele este incomplet.\nFormula propozitionala nu este bine formata'")
        break
    elif formula[i] == "!":
      print(f"Pasul {step}: '{formula[i]}' - negatie\n - urmeaza o propozitie atomica sau compusa")
      step += 1
      count += 1
      if formula[i+1] == "(" or formula[i+1].isalpha() == 1:
        i += 1
        continue
      else:
        print(f"Pasul {step}: '{formula[i+1]} - arborele este incomplet.\nFormula propozitionala nu este bine formata'")
        break
    elif formula[i].isalpha() == 1: 
      print(f"Pasul {step}: '{formula[i]}' - propozitie atomica")
      step += 1
      if formula[i+1] == "&" or formula[i+1] == "|" or formula[i+1] == "-" or formula[i+1] == "<" or formula[i+1] == ")" or formula[i+1].isnumeric() == 1:
        i += 1
        continue
      else:
        print(f"Pasul {step}: '{formula[i+1]} - arborele este incomplet.\nFormula propozitionala nu este bine formata'")
        break
    elif formula[i].isnumeric() == 1:
      if formula[i+1] == "&" or formula[i+1] == "|" or formula[i+1] == "-" or formula[i+1] == "<" or formula[i+1] == ")" or formula[i+1].isnumeric() == 1:
        i += 1
        continue
      else:
        print(f"Pasul {step}: '{formula[i+1]} - arborele este incomplet.\nFormula propozitionala nu este bine formata'")
        break
    elif formula[i:i+2] == "&&" or formula[i:i+2] == "||" or formula[i:i+2] == "->":
      print(f"Pasul {step}: '{formula[i:i+2]}' - conector\n - urmeaza o propozitie atomica sau compusa")
      step += 1
      count += 1
      if formula[i+2] == "(" or formula[i+2].isalpha() == 1:
        i += 2
        continue
      else:
        print(f"Pasul {step+1}: '{formula[i+1]} - arborele este incomplet.\nFormula propozitionala nu este bine formata'")
        break
    elif formula[i:i+3] == "<->":
      print(f"Pasul {step}: '{formula[i:i+3]}' - conector\n - urmeaza o propozitie atomica sau compusa")
      step += 1
      count += 1
      if formula[i+3] == "(" or formula[i+3].isalpha() == 1:
        i += 3
        continue
      else:
        print(f"Pasul {step}: '{formula[i+1]} - arborele este incomplet.\nFormula propozitionala nu este bine formata'")
        break
    elif formula[i] == ")" and len(formula)!=i+1:
      print(f"Pasul {step}: '{formula[i]}' - subarborele curent este complet")
      step += 1
      if formula[i+1] == "&" or formula[i+1] == "|" or formula[i+1] == "-" or formula[i+1] == "<" or formula[i+1] == ")":
        i += 1
        continue
      else:
        print(f"Pasul {step}: '{formula[i+1]} - arborele este incomplet.\nFormula propozitionala nu este bine formata'")
        break
    elif len(formula) == i+1 and formula.count("(") != formula.count(")"):
      print("- arborele este complet, dar ramane un simbol necitit in expresie.\nFormula propozitionala nu este bine formata.")
      i += 1
    elif len(formula) == i+1 and formula[i] == ")" and formula.count("(") == count:
      print(f"Pasul {step}: '{formula[i]}' - arborele este complet")
      i += 1
      print("Formula propozitionala este bine formata")
      continue
    else:
      print(f"Pasul {step}: - arborele este incomplet.\nFormula propozitionala nu este bine formata.")
      break

