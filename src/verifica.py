import pandas as pd
import getpass

def verifica_despesa(nome_tabela,ano,valor_pesquisa):
        user_windows = getpass.getuser()

        caminho = f"C:\\Users\\{user_windows}\\Desktop\\TABELAS\\{ano}\\{nome_tabela}.xls"
        tabela = pd.read_excel(caminho, sheet_name=None)

        total_despesa = 0
        
        arr = []

        for nome_aba, df in tabela.items():
            for index,linha in df.iterrows():
                if linha.astype(str).str.contains(f'{valor_pesquisa}', case=False, na=False).any():
                    
                    
                    deposito = "DEPÓSITO"
                    rendimento = "RENDIMENTO"
                    caixa = "CX"

                    if deposito in valor_pesquisa or rendimento in valor_pesquisa or caixa in valor_pesquisa:
                        valor_2 = linha.iloc[2]
                        valor_5 = linha.iloc[4]
                        valor_7 = linha.iloc[6]
                        valor_9 = linha.iloc[8]
                        valor_10 = linha.iloc[10]

                    else:
                        valor_2 = linha.iloc[3]
                        valor_5 = linha.iloc[5]
                        valor_7 = linha.iloc[7]
                        valor_9 = linha.iloc[9]
                        valor_10 = linha.iloc[11]      
    
                    if pd.isna(valor_2):
                        if pd.isna(valor_5):
                            if pd.isna(valor_7):
                                if pd.isna(valor_9):
                                    total_despesa += valor_10
                                    #print(f"{linha.iloc[1]} - R$ {valor_10}")
                                    arr.append({"nome_dado": linha.iloc[1],
                                                "valor_dado": f"R$ {valor_10:,.2f}".replace(',', 'TEMP').replace('.', ',').replace('TEMP', '.')})
                                else:
                                    total_despesa += valor_9
                                    #print(f"{linha.iloc[1]} - R$ {valor_9}")
                                    arr.append({"nome_dado": linha.iloc[1],
                                                "valor_dado": f"R$ {valor_9:,.2f}".replace(',', 'TEMP').replace('.', ',').replace('TEMP', '.')})

                            else:
                                total_despesa += valor_7
                                #print(f"{linha.iloc[1]} - R$ {valor_7}")
                                arr.append({"nome_dado": linha.iloc[1],
                                            "valor_dado": f"R$ {valor_7:,.2f}".replace(',', 'TEMP').replace('.', ',').replace('TEMP', '.')})                 
                        else:    
                            total_despesa += valor_5
                            #print(f"{linha.iloc[1]} - R$ {valor_5}")
                            arr.append({"nome_dado": linha.iloc[1],
                                            "valor_dado": f"R$ {valor_5:,.2f}".replace(',', 'TEMP').replace('.', ',').replace('TEMP', '.')}) 
                    else:
                        total_despesa += valor_2
                        #print(f"{linha.iloc[1]} - R$ {valor_2}")
                        arr.append({"nome_dado": linha.iloc[1],
                                    "valor_dado":f"R$ {valor_2:,.2f}".replace(',', 'TEMP').replace('.', ',').replace('TEMP', '.')})
                   
                                     
        total = f"{total_despesa:,.2f}"
        total = str(total).replace('.',',',1)
        total = str(total).replace(',','.',1)
        
        return {"total": total,
                "array": arr}     


def ajusta_lista(dado):
    map_dados = ''
    for itens in dado:
        map_dados +="\n" + itens["nome_dado"] + " - " + itens["valor_dado"]

    return map_dados