produtos = ["cereja", "morango", "kiwi", "uva", "maçã"]
valor_vendas = [9000, 10000, 9000, 9500, 7000]
valor_gasto = [4500, 3095, 4785, 5150, 4280]
escolher = input("Escolha uma fruta:")

if escolher == produtos[0]:
    print(f"Você escolheu o protudo {produtos[0]} e gastará um total de R$40 com sementes ou mudas, R$200 com insumos, R$ 300 com a energia, R$4000 com a mão de obra")
    hectares = int(input(f'Digite a quantidade de hectares que você deseja para a(o) {produtos[0]}:'))

elif  escolher == produtos[1]:
    print(f"Você escolheu o protudo {produtos[1]} e gastará um total de R$45 com sementes ou mudas, R$300 com insumos, R$ 750 com a energia, R$2000 com a mão de obra")
    hectares = int(input(f'Digite a quantidade de hectares que você deseja para a(o) {produtos[1]}:'))
    

elif escolher == produtos[2]:
    print(f"Você escolheu o protudo {produtos[2]} e gastará um total de R$35 com sementes ou mudas, R$150 com insumos, R$ 900 com a energia, R$3700 com a mão de obra")
    hectares = int(input(f'Digite a quantidade de hectares que você deseja para a(o) {produtos[2]}:'))
    

elif escolher == produtos[3]:
    print(f"Você escolheu o protudo {produtos[3]} e gastará um total de R$50 com sementes ou mudas, R$500 com insumos, R$ 800 com a energia, R$3800 com a mão de obra")
    hectares = int(input(f'Digite a quantidade de hectares que você deseja para a(o) {produtos[3]}:'))
    

elif escolher == produtos[4]:
    print(f"Você escolheu o produto {produtos[4]} e gastará um total de R$20 com sementes ou mudas, R$160 com insumos, R$ 700 com a energia, R$3400 com a mão de obra")
    hectares = int(input(f'Digite a quantidade de hectares que você deseja para a(o) {produtos[4]}:'))
    

else: 
    print("A fruta não foi encontrada")


escolha_lucro = input("Escolha uma fruta para saber o lucro dela: ")
if escolha_lucro == produtos[0]:
    print(f"O lucro do(a) {produtos[0]} é equivalente a {valor_vendas[0] - valor_gasto[0]}")

elif escolha_lucro == produtos[1]:
    print(f"O lucro do(a) {produtos[1]} é equivalente a {valor_vendas[1] - valor_gasto[1]}")

elif escolha_lucro == produtos[2]:
    print(f" O lucro do(a) {produtos[2]} é equivalente a {valor_vendas[2] - valor_gasto[2]}")

elif escolha_lucro == produtos[3]:
    print(f" O lucro do(a) {produtos[3]} é equivalente a {valor_vendas[3] - valor_gasto[3]}")

elif escolha_lucro == produtos[4]:
    print(f" O lucro do(a) {produtos[4]} é equivalente a {valor_vendas[4] - valor_gasto[4]}")

else: 
    print("Lucro não encontrado!") 