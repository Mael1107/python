vale_transporte = 9
valor_da_bolsa_por_hora = 5.083
horas_por_dia = 4
dias_estagiados = int(input("Quantos dias você estagiou? "))

total_horas_estagiadas = horas_por_dia * dias_estagiados


bolsa_estagio = (vale_transporte * dias_estagiados) + (valor_da_bolsa_por_hora * total_horas_estagiadas)

print(f"Nesse mês, você estagiou {dias_estagiados} dias (exatamente {total_horas_estagiadas} horas) e receberá aproximadamente \033[1;32mR${bolsa_estagio:.2f}\033[m.")
