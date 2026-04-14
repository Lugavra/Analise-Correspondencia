# Analise-Correspondencia

Análise de Correspondência: Setor vs. Desfecho (Consultoria Jurídica)
Este repositório contém um script em Python para a realização de uma Análise de Correspondência (CA), aplicada a dados de uma consultoria jurídica. O objetivo é visualizar a associação entre diferentes setores da empresa e os desfechos dos processos ou atendimentos.

📌 Sobre o Projeto
A Análise de Correspondência é uma técnica estatística multivariada que permite visualizar relações entre variáveis categóricas em um mapa bidimensional (Mapa Perceptual).

Neste caso específico, analisamos como os Setores se comportam em relação aos Desfechos, facilitando a identificação de padrões que seriam difíceis de notar apenas observando tabelas de contingência numéricas.

🛠️ Tecnologias Utilizadas
Python 3.x

Pandas: Para manipulação e tratamento dos dados.

Prince: Biblioteca especializada em análise fatorial e de correspondência.

Matplotlib: Para a renderização e personalização do mapa perceptual.

📂 Estrutura do Código
Carregamento de Dados: Importação da base de dados jurídica.

Tabela de Contingência: Criação de uma matriz de frequências cruzando Setor e Desfecho.

Modelagem (CA): Aplicação do algoritmo para reduzir a dimensionalidade em 2 componentes principais.

Visualização: Geração do Mapa Perceptual para interpretação dos resultados.
