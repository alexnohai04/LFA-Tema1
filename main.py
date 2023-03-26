f=open("input.txt","r")
NrTranzitii=int(f.readline())
print(NrTranzitii)
StInitiala=f.readline().strip()
Tranzitii=[]
StFin=[]
for i in range(NrTranzitii):
    line=f.readline()
    line=line.strip().split()
    Tranzitii.append([line[0],line[1],line[2]])
print(Tranzitii)
line2=f.readline()
StFin=line2.strip().split()
print(StFin)

#Am citit automatul din fisier
cuv = input("Cuvantul = ")
StCurenta = StInitiala
Drum = [StCurenta]  # drumul va contine starile prin care trece automatul
ok=True
# parcurgem cuvantul si verificam daca exista o tranzitie pentru fiecare litera
for x in cuv:
    tranzitie_gasita = False
    for t in Tranzitii:
        if t[0] == StCurenta and t[1] == x:
            # am gasit o tranzitie pentru litera curenta
            StCurenta = t[2]  # schimbam starea curenta
            Drum.append(StCurenta)  # adaugam starea curenta la drum
            tranzitie_gasita = True
            break
    if tranzitie_gasita==False:
        print("Neacceptat")
        ok=False
        break

# verificam daca starea curenta este una finala
if StCurenta in StFin:
    print("Acceptat")
    print("Drum:", "->".join(Drum))
elif ok==True:
    print("Neacceptat")

f.close()