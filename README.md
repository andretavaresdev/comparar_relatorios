# Automação de Comparação de Relatórios Fiscais com Python e Pandas

**Descrição:**

Esse projeto foi desenvolvido para automatizar o processo de comparação entre dois relatórios fiscais, com o objetivo de identificar divergências de documentos fiscais (notas fiscais eletrônicas). O código utiliza a biblioteca **Pandas** do Python para processar, comparar e gerar relatórios de forma rápida, eficiente e confiável.

**Contexto:**

No cenário real, a tarefa de comparar dois relatórios — um da contabilidade e outro de um fornecedor terceirizado — com milhares de registros, seria extremamente demorada e propensa a erros se feita manualmente. A solução foi utilizar o Python para **automatizar esse processo**, garantindo precisão e agilidade.

---

## Funcionalidades

O código realiza as seguintes tarefas:

- **Carregamento seguro de arquivos CSV**: Leitura dos relatórios em formato `.csv` com tratamento adequado de erros.
- **Padronização de dados**: Assegura que as colunas que contêm os identificadores (como a chave de acesso das NFe) estejam uniformizadas, removendo espaços extras.
- **Identificação de divergências**: Compara os documentos dos dois relatórios e identifica os que estão ausentes em cada um.
- **Geração de relatórios automatizados**: Criação de arquivos CSV que indicam as divergências encontradas, prontos para análise.

---

## Como Funciona

### 1. **Carregar os Arquivos**
O código começa carregando dois arquivos `.csv` que representam os relatórios a serem comparados: um da contabilidade e outro de um fornecedor terceirizado.

### 2. **Padronização e Comparação**
As colunas com os identificadores (como as chaves de acesso das NFe) são padronizadas e convertidas para um formato uniforme, para garantir que a comparação seja precisa.

### 3. **Identificação de Divergências**
O código identifica os documentos que estão presentes em um relatório, mas não no outro, e salva os resultados em novos arquivos `.csv`.

### 4. **Geração dos Relatórios**
Por fim, dois novos arquivos são gerados com os documentos faltantes em cada relatório, que podem ser analisados e enviados para os responsáveis.

---

## Como Usar

### Requisitos

- Python 3.x
- Biblioteca Pandas (instalar com `pip install pandas`)

### Passo a Passo

1. Clone o repositório:

   ```bash
   git clone https://github.com/andretavaresdev/comparar_relatorios.git
   cd comparar_relatorios

2. Coloque seus arquivos .csv na mesma pasta do script Python.

3. Execute o script:
   ```bash
   python comparar_relatorios.py

4. O código irá gerar dois novos arquivos .csv com os documentos faltantes:
    contabilidade_sem_terceirizado.csv
    terceirizado_sem_contabilidade.csv

5. Esses arquivos estarão prontos para análise e poderão ser compartilhados conforme necessário.

   [ Post LinkedIn: https://www.linkedin.com/feed/update/urn:li:activity:7339741984309272576/ ]
