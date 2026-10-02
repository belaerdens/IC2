import random

#Criar cópias p/ cada porcentagem de oxidação
caixa_new_15 = open("caixa_membrana_oxidada_15.pdb", "w")
caixa_new_30 = open("caixa_membrana_oxidada_30.pdb", "w")
caixa_new_45 = open("caixa_membrana_oxidada_45.pdb", "w")

# Funções p/ gerar números aleatórios (lipídios que vou oxidar)
def random_lipids(caixa_new, leaflet1, n, leaflet2, m):

    print("Nova caixa:", caixa_new.name)
    caixa_new.truncate(0)

    caixa_old = open("/home/isabelaerdens/IC2/membrana_POPC/caixa_membrana.pdb", "r")

    numeros1 = random.sample(range(1, 65), n)
    numeros2 = random.sample(range(1, 65), m)

    print(f"{leaflet1}:", sorted(numeros1))
    print(f"{leaflet2}:", sorted(numeros2))


    while True:

        linha = caixa_old.readline()

    
        if not linha.startswith("ATOM" or "HETATM"):
            caixa_new.write(linha)

        if linha.startswith("END"):
            break

        if linha.startswith("ATOM"):
            dados = linha.split()
            if ((dados[3] == leaflet1) and (int(dados[4]) in numeros1)) or ((dados[3] == leaflet2) and (int(dados[4]) in numeros2)):

                if (dados[2] == "H91"):
                    dados[3] = "PAZ E"
                    dados[11] = "O"
                    dados[2] = "O29"

                if (dados[2] == "C210"):
                    dados[3] = "PAZ E"
                    dados[11] = "O"
                    dados[2] = "O210"

                if (dados[2] == "H101"):
                    dados[3] = "PAZ E"
                    dados[2] = "H210"

                if dados[2] == "C211" or dados[2] == "H11R" or dados[2] == "H11S" or dados[2] == "C212" or dados[2] == "H12R" or dados[2] == "H12S" or dados[2] == "C213" or dados[2] == "H13R" or dados[2] == "H13S" or dados[2] == "C214" or dados[2] == "H14R" or dados[2] == "H14S" or dados[2] == "C215" or dados[2] == "H15R" or dados[2] == "H15S" or dados[2] == "C216" or dados[2] == "H16R" or dados[2] == "H16S" or dados[2] == "C217" or dados[2] == "H17R" or dados[2] == "H17S" or dados[2] == "C218" or dados[2] == "H18R" or dados[2] == "H18S" or dados[2] == "H18T":
                    continue

                else:
                    dados[3] = "PAZ E"

                if len(dados[2]) == 1:
                    dados[2] = f" {dados[2]}  "

                if len(dados[2]) == 2:
                    dados[2] = f" {dados[2]} "

                if len(dados[2]) == 3:
                    dados[2] = f" {dados[2]}"

                nova_linha = (
                    f"{dados[0]:<6}"     # 1-6  "ATOM" or "HETATM"
                    f"{dados[1]:>5}"     # 7-11 Atom serial number
                    f" "                 # 12
                    f"{dados[2]:<4}"     # 13-16 Atom name
                    f" "                 # 17 Alternate location indicator
                    f"{dados[3]:>5}"     # 18-22 "{Residue name} {Chain identifier}
                    f"{dados[4]:>4}"     # 23-26 Residue sequence number
                    f"    "              # 27-30
                    f"{dados[5]:>8}"     # 31-38 X
                    f"{dados[6]:>8}"     # 39-46 Y
                    f"{dados[7]:>8}"     # 47-54 Z
                    f"{dados[8]:>6}"     # 55-60 Occupancy
                    f"{dados[9]:>6}"     # 61-66 Temperature factor
                    f"      "            # 67-72
                    f"{dados[10]:<4}"    # 73-76 Segment
                    f"{dados[11]:>2}\n"    # 77-78 Element
                )
                caixa_new.write(nova_linha)
            else:
                caixa_new.write(linha)

    caixa_old.close()
    caixa_new.close()

#Editar caixa_new.pdb para todas as porcentagens de oxidação
random_lipids(caixa_new_15, "POPCC", 9, "POPCD", 10)
random_lipids(caixa_new_30, "POPCC", 19, "POPCD", 19)
random_lipids(caixa_new_45, "POPCC", 29, "POPCD", 29)












