import pandas as pd
import os

tabela = pd.read_excel('JANEIRO.xls', sheet_name=None)

arr = []

def verifica_despesa():
    total_despesa = 0

    for nome_aba, df in tabela.items():
        for index,linha in df.iterrows():
            if linha.astype(str).str.contains('DESPESA', case=False, na=False).any():
                valor_5 = linha.iloc[5]
                valor_7 = linha.iloc[7]
                valor_9 = linha.iloc[9]      

                if pd.isna(valor_5):
                    if pd.isna(valor_7):
                        total_despesa += valor_9
                        ##print(f"{linha.iloc[1]} - R$ {valor_9}")
                        arr.append({"nome_dado": linha.iloc[1],
                                    "valor_dado": "R$ " + str(valor_9) })

                    else:
                        total_despesa += valor_7
                        arr.append({"nome_dado": linha.iloc[1],
                                    "valor_dado": "R$ " + str(valor_7) })                 
                else:
                    
                    total_despesa += valor_5
                    ##print(f"{linha.iloc[1]} - R$ {valor_5}")
                    arr.append({"nome_dado": linha.iloc[1],
                                    "valor_dado": "R$ " + str(valor_5) })
                          
    total = f"TOTAL = R$ {round(total_despesa,2)}"
    ##print(dados)

    
    return {"total": total,
            "array": arr}


def ajusta_lista(dado):
    map_dados = ''
    for itens in dado:
        map_dados +="\n" + itens["nome_dado"] + itens["valor_dado"]

    return map_dados


verifica_despesa()
