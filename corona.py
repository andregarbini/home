
print("HCV - Hospital Corona Virus")

nome = input("Nome do paciente: ").upper
idade = str(input("Idade do paciente: "))
idade = int(idade)
temperatura = str(input("Temperatura do paciente: "))
risco = input("É grupo de risco? (SIM ou NAO)").upper

if risco != "SIM" or "NAO":
    risco = input("É grupo de risco? (SIM ou NAO)").upper



temperatura = int(temperatura)

if idade < 15 or idade > 60:
    print(" -- PRIORIDADE MÁXIMA -- ")
else:
    print(" Continue na fila ")


if (temperatura >= 39) and idade < 15 or idade > 60:
    print(" -- O PACIENTE ESTÁ CONTAMINADO -- ")
else:
    print(" --      Continue na fila      --")






