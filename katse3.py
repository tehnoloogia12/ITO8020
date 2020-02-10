import sys
def loenimed(failinimi):
    sisend=open(failinimi)
    lines=sisend.readlines()
    i=0
    while i<len(lines):
        nimi=lines[i].strip()
        lines[i]=nimi
        i=i+1
    sisend.close()
    return lines



naistenimed=loenimed("tydrukunimed.txt")
meestenimed=loenimed("poistenimed.txt")


sisend=open("palgad.csv")
lines=sisend.readlines()
sisend.close()
# print(lines)
reanr=0
palgasumma=0
meestepalgasumma=0
naistepalgasumma=0
meestearv=0
naistearv=0
# tspkkel
while reanr<len(lines):
    rida=lines[reanr]
    # print(rida)
    tykid=rida.split(";")
    if tykid[1]=="m" or tykid[1]=="M":
        # print("mees")
        meestepalgasumma=meestepalgasumma+int(tykid[2])
        meestearv=meestearv+1
    if tykid[1]=="N" or tykid[1]=="n":
        # print("naine")
        naistepalgasumma=naistepalgasumma+int(tykid[2])
        naistearv=naistearv+1
    if not (tykid[1] in ["m","M","n","N"]):
        if tykid[0] in meestenimed:
            # print(tykid[0],"mees")
            meestepalgasumma=meestepalgasumma+int(tykid[2])
            meestearv=meestearv+1
        elif tykid[0] in naistenimed:
            # print(tykid[0],"naine")
            naistepalgasumma=naistepalgasumma+int(tykid[2])
            naistearv=naistearv+1


    palgasumma=palgasumma+int(tykid[2])
    reanr=reanr+1
print("palgasumma", palgasumma)
print("keskmine palk", palgasumma/len(lines))
print("kesmine meeste palk:",meestepalgasumma/meestearv)
print("kesmine naiste palk:",naistepalgasumma/naistearv)
