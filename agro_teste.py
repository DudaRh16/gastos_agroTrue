produtos = ["cereja", "morango", "kiwi", "uva", "maçã"]
valor_ganho = [6000, 4]
escolher = input("Escolha uma fruta: ")

if escolher == produtos[0]:
    print(f"Você escolheu o produto {produtos[0]} e gastará um total de R$40 com sementes ou mudas, R$200 com insumos, R$ 1000 com a energia, R$4000 com a mão de obra")

elif escolher == produtos[1]:
    print(f"Você escolheu o produto {produtos[1]} e gastará um total de R$45 com sementes ou mudas, R$300 com insumos, R$ 750 com a energia, R$5000 com a mão de obra")

elif escolher == produtos[2]:
    print(f"Você escolheu o produto {produtos[2]} e gastará um total de R$35 com sementes ou mudas, R$150 com insumos, R$ 900 com a energia, R$3700 com a mão de obra")

elif escolher == produtos[3]:
    print(f"Você escolheu o produto {produtos[3]} e gastará um total de R$50 com sementes ou mudas, R$500 com insumos, R$ 800 com a energia, R$3800 com a mão de obra")

elif escolher == produtos[4]:
    print(f"Você escolheu o produto {produtos[4]} e gastará um total de R$38 com sementes ou mudas, R$250 com insumos, R$ 950 com a energia, R$4200 com a mão de obra")

else:
    print("Fruta não encontrada.")


