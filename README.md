# Codigos
Projeto Integrador I - Univesp

O projeto consiste em um sistema capaz de, a partir da descrição de uma receita (tributária ou não), obter o código da operação e o código da receita para o preenchimento da guia de depósito judicial.
Com o uso desta ferramenta, evita-se problemas tais como: incorreta destinação do recurso recolhido na conta judicial e divergência quanto ao critério de atualização monetária.
A escolha do tema foi feita em virtude da percepção da dificuldade que as partes envolvidas em processos judiciais tinham para obter os dados corretos (Operação e códigos) necessários para efetivação de depósito  em garantia a uma ação em andamento.
Em vários casos, observou-se que é necessário o deslocamento do interessado até o fórum para obtenção dos dados corretos para a operação bancária.
O objetivo foi  permitir agilidade na obtenção dos dados corretos em função do tipo de dívida ou controvérsia judicial.

O arquivo p_0.service é o arquivo que permite que a aplicação python rode como um serviço no servidor de aplicação.
É utilizado como parâmetro para o comando no systemctl no linux.
Comando para ativar: systemctl start p_0.service
Comando para verificar: systemctl status p_0.service
Comando para parar o serviço (Utilizado quando foi feita alguma modificação no arquivo .py): systemctl stop p_0.service

Os arquivos 2025-05-10_15h10m04s.json e 2025-05-23_13h01m52s.json são exemplos do arquivo do tipo json gerado com o processamento dos dados iniciais, por outro lado o arquivo resultado.txt é formado para possibilitar o retorno ao front-end, viabilizando o uso dos dados de resultado.

O arquivo resultado.txt também é gerado pelo programa python e possibilita a visualização dos resultados no front-end

