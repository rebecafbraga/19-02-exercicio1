import datetime
dia_hoje = datetime.date.today()#(year=2020, month=2, day=20)

ano = int (input('Digite o ano de seu nascimento:'))
mes = int (input('Digite o mes de seu nascimento:'))
dia = int (input('Digite o dia de seu nascimento:'))
dia_nascimento = datetime.date (year= ano, month= mes,day = dia)

def dias_vida (dia_hoje, dia_nascimento):
    resultado = dia_hoje - dia_nascimento
    print(resultado)
    return resultado

dias_vida (dia_hoje, dia_nascimento)