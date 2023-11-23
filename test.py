import time
import requests
import pandas as pd
import numpy as np

# Manipulação da planilha

planilha_cnpj = "teste_cnpj.xlsx"

coluna = 7
dados_planilha = pd.read_excel("teste_cnpj.xlsx", usecols=[coluna], header=None)
valores_coluna = dados_planilha[coluna].tolist()

array_coluna_cnpj = np.array(valores_coluna)

"""=========================================================================================="""

# API
def obter_informacoes_cnpj(cnpj):
    url = f'https://receitaws.com.br/v1/cnpj/{cnpj}'
    
    try:
        response = requests.get(url)
        response.raise_for_status()  
        dados_empresa = response.json()
        
        return dados_empresa

    except requests.exceptions.RequestException as e:
        print(f'Erro na requisição: {e}')

"""=========================================================================================="""   

# Dados do excel (CNPJs)
cnpj_exemplo = array_coluna_cnpj
# API
response = requests.get("https://receitaws.com.br/v1/cnpj/{cnpj}")
"""==========================================================================================""" 

# Inicialização
dados_acumulados = []
x = "iniciar";
cont = 0

async def teste():


# Consulta API e acumula os dados
    for cnpj_exemplo in array_coluna_cnpj:
        cont + 1
        if cont < 3:
        dados_empresa = obter_informacoes_cnpj(cnpj_exemplo)
        
        if x == "parar":
            time.sleep(60)
            x = "iniciar";

        if x == "iniciar":
            index = 0;

            while index < 3:
                #print(dados_empresa)
                if dados_empresa:
                    print(f"CNPJ: {cnpj_exemplo}\n")
                    dados_acumulados.append(dados_empresa)

                print("\nConsultando próximo CNPJ...\n")
                time.sleep(1)
                index += 1

            x = "parar";

# Criar DataFrame pandas com os dados acumulados
df_acumulado = pd.DataFrame(dados_acumulados)

# Salvar DataFrame no Excel
with pd.ExcelWriter('dados_acumulados.xlsx', engine='openpyxl') as writer:
    print(dados_acumulados)
    df_acumulado.to_excel(writer, sheet_name='Sheet1', index=False)
    print("\nPlanilha atualizada!\n")