import datetime
import os
from flask import Flask, request, jsonify
from flask_cors import CORS
import json

lisCodigo = ['0092','0107','0115','0123','0131','0141','0157','0165','0173','0181','0199','0204','0212','0220','0238','0246','0254','0301','0319','0327','0335','0343','0351','0369','0377','0385','0393','0409','0416','0424','0432','0440','0458','0466','0474','0482','0490','0505','0513','0521','0539','0547','0555','1602','1604','2080','4396','5155','5246','5252','5269','5275','5281','5298','5308','5314','5337','5343','5350','5366','5372','5405','5428','5680','6086','7118','0163','0216','0868','1947','1994','2226','2300','2420','2450','2466','2472','2489','2505','2528','2534','2557','2563','2570','2586','2592','2602','3300','5470','7363','7389','7391','7416','7429','7431','7444','7457','7460','7485','7498','7525','7961','8047','8811']

lisDCurta = ['CRÉDITO COBRANÇA NA PROCURADORIA – DEBCAD','CRÉDITO COBRANÇA NA PROCURADORIA – CNPJ','CRÉDITO COBRANÇA NA PROCURADORIA – CEI','CRÉDITO COBRANÇA NA PROCURADORIA – NIT/PIS/PASEP','CRÉDITO COBRANÇA NA PROCURADORIA – CPF','CRÉDITO COBRANÇA ADMINISTRATIVA – DEBCAD','CRÉDITO REFERENTE A PATRIMÔNIO – CNPJ','CRÉDITO REFERENTE A PATRIMÔNIO – CPF','CONTRIBUIÇÕES REF. A CONTRIBUINTE INDIVIDUAL – NIT/PIS/PASEP','CONTRIBUIÇÃO DA EMPRESA PARA O INSS E OUTRAS ENTIDADES – CNPJ','CONTRIBUIÇÃO DA EMPRESA PARA O INSS E OUTRAS ENTIDADES – CEI','CONTRIBUIÇÃO DA EMPRESA SOMENTE PARA INSS – CNPJ','CONTRIBUIÇÃO DA EMPRESA SOMENTE PARA INSS – CEI','CONTRIBUIÇÃO DA EMPRESA SOMENTE PARA OUTRAS ENTIDADES – CNPJ','CONTRIBUIÇÃO DA EMPRESA SOMENTE PARA OUTRAS ENTIDADES –CEI','ARRECADAÇÃO BLOQUEADA – CNPJ (CEF)','ARRECADAÇÃO BLOQUEADA – CNPJ (OUTROS BANCOS)','CONTRIBUIÇÃO DA EMPRESA SOMENTE PARA SALÁRIO EDUCAÇÃO (FNDE) - CNPJ','CONTRIBUIÇÃO DA EMPRESA SOMENTE PARA SALÁRIO EDUCAÇÃO (FNDE) – CEI','CONTRIBUIÇÃO DA EMPRESA SOMENTE PARA INCRA – CNPJ','CONTRIBUIÇÃO DA EMPRESA SOMENTE PARA INCRA – CEI','CONTRIBUIÇÃO DA EMPRESA SOMENTE PARA SENAI – CNPJ','CONTRIBUIÇÃO DA EMPRESA SOMENTE PARA SENAI – CEI','CONTRIBUIÇÃO DA EMPRESA SOMENTE PARA SESI – CNPJ','CONTRIBUIÇÃO DA EMPRESA SOMENTE PARA SESI – CEI','CONTRIBUIÇÃO DA EMPRESA SOMENTE PARA SENAC – CNPJ','CONTRIBUIÇÃO DA EMPRESA SOMENTE PARA SENAC – CEI','CONTRIBUIÇÃO DA EMPRESA SOMENTE PARA SESC – CNPJ','CONTRIBUIÇÃO DA EMPRESA SOMENTE PARA SESC - CEI','CONTRIBUIÇÃO DA EMPRESA SOMENTE PARA SEBRAE – CNPJ','CONTRIBUIÇÃO DA EMPRESA SOMENTE PARA SEBRAE – CEI','CONTRIBUIÇÃO DA EMPRESA SOMENTE PARA DPC – CNPJ','CONTRIBUIÇÃO DA EMPRESA SOMENTE PARA DPC – CEI','CONTRIBUIÇÃO DA EMPRESA SOMENTE PARA FUNDO AEROVIÁRIO – CNPJ','CONTRIBUIÇÃO DA EMPRESA SOMENTE PARA FUNDO AEROVIÁRIO – CEI','CONTRIBUIÇÃO DA EMPRESA SOMENTE PARA SENAR – CNPJ','CONTRIBUIÇÃO DA EMPRESA SOMENTE PARA SENAR – CEI','CONTRIBUIÇÃO DA EMPRESA SOMENTE PARA SESCOOP – CNPJ','CONTRIBUIÇÃO DA EMPRESA SOMENTE PARA SESCOOP – CEI','CONTRIBUIÇÃO DA EMPRESA SOMENTE PARA SEST – CNPJ','CONTRIBUIÇÃO DA EMPRESA SOMENTE PARA SEST – CEI','CONTRIBUIÇÃO DA EMPRESA SOMENTE PARA SENAT – CNPJ','CONTRIBUIÇÃO DA EMPRESA SOMENTE PARA SENAT - CEI','AÇÃO PENAL, INQUÉRITO POLICIAL OU INCIDENTE PROCESSUAL PENAL - MJSP','AÇÃO PENAL, INQUÉRITO POLICIAL OU INCIDENTE PROCESSUAL PENAL - MPF','JUDICIAIS [PGF-AG]','ARREMATAÇÃO - 1ª PARC','ROYALTIES','ROYALTIES 5% (E-M) (L 7990 ART. 7 I A III)','ROYALTIES - ATÉ 5% - PRÉ-SAL','ROYALTIES 5% (E-M) (L 7990 ART. 7 P 4)','INDENIZAÇÃO PELA EXTRAÇÃO DE PETRÓLEO, XISTO E GÁS','ROYALTIES ATÉ 5% - ART. 2º DA LEI Nº 12.858/2013','ROYALTIES EXCEDENTES A 5% (E/M) LEI Nº 9.478/1997, ART. 49, I','ROYALTIES EXCEDENTES A 5% (MCT) LEI Nº 9.478/1997, ART. 49, I','ROYALTIES EXCEDENTES 5% - LAVRA NA ÁREA PRÉ-SAL','ROYALTIES EXCEDENTES A 5% (E-M) - LEI Nº 9.478/1997, ART. 49, II','ROYALTIES EXCEDENTES A 5% (MM/MCT) - LEI Nº 9.478/1997, ART. 49, II','ROYALTIES EXCEDENTES A 5% - ART. 2º DA LEI Nº 12.858/2013','PARTICIPAÇÃO ESPECIAL (E-M) - LEI Nº 9.478/1997, ART. 50','PARTICIPAÇÃO ESPECIAL (MME/MMA) - LEI Nº 9.478/1997, ART. 50','PARTICIPAÇÃO ESPECIAL - ART. 2º DA LEI Nº 12.858/2013','ROYALTIES - REG. PART. PRODUÇÃO - ALÍQ. 15% - ART. 42 -LEI 12351/2010 - PRÉ-SAL E ÁREAS ESTRATÉGICAS','FUNDO NACIONAL ANTIDROGAS','PERDIMENTO BENS, DIREITOS E VALORES DECLARADOS PELA JUST. FEDERAL - CRIMES LEI Nº 9.613, DE 1998','MULTA ADMINISTRATIVA - INFRAÇÃO TRABALHISTA','ANTIDUMPING','ADUANEIROS','PASEP','PIS IMPORTAÇÃO','COFINS IMPORTAÇÃO','CONTRIB. PREVID. SEGURADO','CONTRIB. PREVID. EMPREGADOR','MULTA PREVIDENCIÁRIA','SALÁRIO-EDUCAÇÃO','SENAR','INCRA','FUNDO AEROVIÁRIO','FUNDO MARÍTIMO','SENAT','SEST','SENAI','SESI','SENAC','SESC','CIDE','SESCOOP','CONTRIB. PREVID. PÚBLICA','PERDIMENTO','IMPOSTO IMPORTAÇÃO','IPI','IPI IMPORTAÇÃO','IRPF','IRPJ','IRRF','IOF','ITR','PIS','CSLL','COFINS','DÍVIDA ATIVA - J. FEDERAL','DÍVIDA ATIVA - J. ESTADUAL','OUTROS','REFIS']

lisD_Orig = ['Crédito em Cobrança na Procuradoria – DEBCAD','Crédito em Cobrança na Procuradoria – CNPJ','Crédito em Cobrança na Procuradoria – CEI','Crédito em Cobrança na Procuradoria – NIT/PIS/PASEP','Crédito em Cobrança na Procuradoria – CPF','Crédito em Cobrança Administrativa – DEBCAD','Crédito Referente a Patrimônio – CNPJ','Crédito Referente a Patrimônio – CPF','Contribuições Ref. a Contribuinte Individual – NIT/PIS/PASEP','Contribuição da Empresa para o INSS e Outras Entidades – CNPJ','Contribuição da Empresa para o INSS e Outras Entidades – CEI','Contribuição da Empresa Somente para INSS – CNPJ','Contribuição da Empresa Somente para INSS – CEI','Contribuição da Empresa Somente para Outras Entidades – CNPJ','Contribuição da Empresa Somente para Outras Entidades –CEI','Arrecadação Bloqueada – CNPJ (CEF)','Arrecadação Bloqueada – CNPJ (Outros Bancos)','Contribuição da Empresa Somente para Salário Educação (FNDE) - CNPJ','Contribuição da Empresa Somente para Salário Educação (FNDE) – CEI','Contribuição da Empresa Somente para INCRA – CNPJ','Contribuição da Empresa Somente para INCRA – CEI','Contribuição da Empresa Somente para SENAI – CNPJ','Contribuição da Empresa Somente para SENAI – CEI','Contribuição da Empresa Somente para SESI – CNPJ','Contribuição da Empresa Somente para SESI – CEI','Contribuição da Empresa Somente para SENAC – CNPJ','Contribuição da Empresa Somente para SENAC – CEI','Contribuição da Empresa Somente para SESC – CNPJ','Contribuição da Empresa Somente para SESC - CEI','Contribuição da Empresa Somente para SEBRAE – CNPJ','Contribuição da Empresa Somente para SEBRAE – CEI','Contribuição da Empresa Somente para DPC – CNPJ','Contribuição da Empresa Somente para DPC – CEI','Contribuição da Empresa Somente para Fundo Aeroviário – CNPJ','Contribuição da Empresa Somente para Fundo Aeroviário – CEI','Contribuição da Empresa Somente para SENAR – CNPJ','Contribuição da Empresa Somente para SENAR – CEI','Contribuição da Empresa Somente para SESCOOP – CNPJ','Contribuição da Empresa Somente para SESCOOP – CEI','Contribuição da Empresa Somente para SEST – CNPJ','Contribuição da empresa somente para SEST – CEI','Contribuição da Empresa Somente para SENAT – CNPJ','Contribuição da Empresa Somente para SENAT - CEI','Ação Penal, Inquérito Policial ou Incidente Processual Penal - MJSP','Ação Penal, Inquérito Policial ou Incidente Processual Penal - MPF','Depósitos Judiciais e Extrajudiciais Administrados pela PGF-AG','Parcelamento de Arrematação - Primeira Parcela','Depósitos Judiciais - Royalties e/ou Participação Especial','Royalties 5% (E/M) L 7990 art. 7 I A III','Royalties até 5% - Lavra na Área Pré-Sal - Em Plataforma','Royalties 5% (E-M) (L 7990 art. 7 P 4)','Cota Parte Indenização pela Extração de Petróleo, Xisto e Gás (MM)','Royalties até 5% - Art. 2º da Lei nº 12.858/2013','Royalties Excedentes a 5% (E/M) Lei nº 9.478/1997, art. 49, I','Royalties Excedentes a 5% (MCT) Lei nº 9.478/1997, art. 49, I','Royalties Excedentes 5% - Lavra na Área Pré-Sal - Em Plataforma','Royalties Excedentes a 5% (E-M) - Lei nº 9.478/1997, art. 49, II','Royalties Excedentes a 5% (MM/MCT) - Lei nº 9.478/1997, art. 49, II','Royalties Excedentes a 5% - Art. 2º da Lei nº 12.858/2013','Participação Especial (E-M) - Lei nº 9.478/1997, art. 50','Participação Especial (MME/MMA) - Lei nº 9.478/1997, art. 50','Participação Especial - Art. 2º da Lei nº 12.858/2013','Royalties - Regime de Partilha de Produção - Alíquota de 15% - Art. 42 da Leinº 12.351/2010 - Pré-Sal e Áreas Estratégicas','Fundo Nacional Antidrogas','Perdimento de Bens, Direitos e Valores Declarados pela Justiça Federal nosCrimes Previstos na Lei nº 9.613, de 1998','Multa Administrativa por Infração Trabalhista','Receita dos Direitos Antidumping e Compensatórios','Outros - Aduaneiros','Pasep','PIS - Importação','Cofins - Importação','Contribuição Segurado','Contribuição Empresa/Empregador','Multa Isolada Previdenciária','Contribuição Devida a Outras Entidades e Fundos - Salário Educação','Contribuição Devida a Outras Entidades e Fundos - Serviço Nacional de Aprendizagem Rural - Senar','Contribuição Devida a Outras Entidades e Fundos - Instituto Nacional de Colonização e Reforma Agrária - Incra','Contribuição Devida a Outras Entidades e Fundos - Fundo Aeroviário','Contribuição Devida a Outras Entidades e Fundos - Fundo de Desenvolvimento do Ensino Profissional Marítimo - FDEPM','Contribuição Devida a Outras Entidades e Fundos - Serviço Nacional de Aprendizagem do Transporte - Senat','Contribuição Devida a Outras Entidades e Fundos - Serviço Social de Transporte - Sest','Contribuição Devida a Outras Entidades e Fundos - Serviço Nacional de Aprendizagem Industrial - Senai','Contribuição Devida a Outras Entidades e Fundos - Serviço Social da Indústria - Sesi','Contribuição Devida a Outras Entidades e Fundos - Serviço Nacional de Aprendizagem Comercial - Senac','Contribuição Devida a Outras Entidades e Fundos - Serviço Social do Comércio - Sesc','Cide - Sebrae/Apex/ABDI','Contribuição Devida a Outras Entidades e Fundos - Serviço Nacional de Aprendizagem do Cooperativismo - Sescoop','CPSS - Contribuição para o Plano de Seguridade Social do Servidor Público – Não Patronal','Perdimento de Bens Apreendidos','Imposto de Importação','IPI - Outros','IPI Vinculado à Importação','IRPF','IRPJ','IRRF','IOF','ITR','PIS','CSLL','Cofins','Receita Dívida Ativa - Justiça Federal','Receita Dívida Ativa - Justiça Estadual','Depósito Judicial - Outros','Refis']

app = Flask(__name__)

os.system("clear")

print('Iniciando ....')

CORS(app)  # This will enable CORS for all routes

@app.route('/submit', methods=['POST'])

def submit():
    if request.method == 'POST':
        data = request.get_json()  # Assuming data is sent as JSON
        d_curta = data['tipo']
        nome_user = data['nome']
        num_cpf = data['cpf']
        nome_benef = data['beneficiario']
        num_cnpj = data['cnpj']
        operacao = data['operacao']
        print("Received JSON data:", data)  # Print JSON data to console
        if d_curta in lisDCurta:
            pos = lisDCurta.index(d_curta)
            print(f'A descrição "{d_curta} está no índice {pos}, ou seja, na {pos+1}ª posição.')
            codigo = lisCodigo[pos]
            descr_longa = lisD_Orig[pos] 
            data['codigo'] = codigo
        else:
            print(f'A descrição {d_curta} não está existe.')

        #prepara nome de arquivo
        now=datetime.datetime.now()
        string_i_want=('%04d-%02d-%02d'%(now.year,now.month,now.day) + '_' + '%02d'%(now.hour) + 'h' + '%02d'%(now.minute) + 'm' + '%02d'%(now.second) + 's')
        nomearquivo = '/var/www/p_1/html/outputs/' + string_i_want + '.json'
        
        arq_results = '/var/www/p_1/html/resultado.txt'

        print(nomearquivo)
        print(arq_results)

        # Gravando arquivo com os resultados
        file = open(arq_results,'w+') #criando o arquivo (Se o arquivo existir, vai sobreescrever)
        print('Iniciando a inserção de linhas para formação do arquivo de resultados')
        file.write('Depositante: ' + nome_user + '\n')        # inserindo 1a linha
        file.write('CPF do depositante: ' + num_cpf + '\n')        # inserindo 1a linha
        file.write('Beneficiário: ' + nome_benef + '\n')        # inserindo 2a linha
        file.write('CNPJ do beneficiário: ' + num_cnpj + '\n')        # inserindo 2a linha
        file.write('Código da Operação: ' + operacao + '\n') # inserindo 3a linha
        file.write('Código da Receita: ' + codigo + '\n') # inserindo 4a linha
        file.write('Descrição Completa: ' + descr_longa + '\n') # inserindo 5a linha
        file.close()

        # Gravando arquivo com os resultados
        # Write data to the JSON file
        with open(nomearquivo, 'w') as json_file:
            json.dump(data, json_file, indent=4)

        print("Data has been written to ", nomearquivo)
        return jsonify({'message': 'Data processed successfully'})
    else:
        return jsonify({'error': 'Method not allowed'}), 405


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
