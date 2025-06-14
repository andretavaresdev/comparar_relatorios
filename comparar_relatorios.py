import pandas as pd

# Nomes dos arquivos dos relatórios
arquivo_contabilidade = 'relatorio_contabilidade.csv'
arquivo_terceirizado = 'relatorio_terceirizado.csv'

# Nome das colunas a serem verificadas (dados fictícios)
coluna_doc_contabilidade = 'ID_DOCUMENTO_CONTABILIDADE'
coluna_doc_terceirizado = 'ID_DOCUMENTO_TERCEIRIZADO'

# Carregar os Relatórios
try:
 # Leitura arquivos .csv com separadores ";" entre colunas 
 df_contabilidade = pd.read_csv(arquivo_contabilidade, sep=';')
 df_terceirizado = pd.read_csv(arquivo_terceirizado, sep=';')

 print("Contabilidade (cabeçalho):")
 print(df_contabilidade.head())
 print("\nColunas da Contabilidade:", df_contabilidade.columns.tolist())

 print("\nTerceirizado (cabeçalho):")
 print(df_terceirizado.head())
 print("\nColunas do Terceirizado:", df_terceirizado.columns.tolist())

# Verificação de erros
except FileNotFoundError:
 print("Um dos arquivos não foi encontrado. Verifique os nomes e o local.")
 exit()
except KeyError as e:
 print(f"Erro: A coluna '{e}' não foi encontrada. Verifique se os nomes das colunas estão corretos.")
 exit()
except pd.errors.ParserError as e:
 print(f"Erro ao ler o arquivo: {e}. Pode ser um problema de formatação no CSV.")
 exit()
except Exception as e:
 print(f"Aconteceu um erro inesperado ao carregar os arquivos: {e}")
 exit()

# Pega todos os IDs únicos de cada relatório e transforma em texto
ids_contabilidade = df_contabilidade[coluna_doc_contabilidade].astype(str).str.strip().unique()
ids_terceirizado = df_terceirizado[coluna_doc_terceirizado].astype(str).str.strip().unique()

print(f"\nTotal de documentos únicos na Contabilidade: {len(ids_contabilidade)}")
print(f"Total de documentos únicos no Terceirizado: {len(ids_terceirizado)}")

# Conjunto dos IDs do terceirizado
set_ids_terceirizado = set(ids_terceirizado)

# Filtra os IDs da contabilidade que não aparecem no conjunto terceirizado
docs_contabilidade_faltando_terceirizado = [
  doc_id for doc_id in ids_contabilidade if doc_id not in set_ids_terceirizado
]

print("\nDocumentos da Contabilidade que não constam no terceirizado")
if docs_contabilidade_faltando_terceirizado:
  # Caso haja documentos faltando, mostrará os detalhes
  df_detalhes_faltando = df_contabilidade[
      df_contabilidade[coluna_doc_contabilidade].isin(docs_contabilidade_faltando_terceirizado)
  ].drop_duplicates(subset=[coluna_doc_contabilidade]) # Remove linhas duplicadas do mesmo documento

  print(f"Encontrei {len(docs_contabilidade_faltando_terceirizado)} documento(s) faltando:")
  print(df_detalhes_faltando)

  # Salva o resultado em um arquivo CSV
  df_detalhes_faltando.to_csv('contabilidade_sem_terceirizado.csv', index=False)
  print("\nDetalhes salvos em 'contabilidade_sem_terceirizado.csv'")
else:
  print("Todos os documentos da contabilidade foram encontrados no terceirizado.")

# Conjunto dos IDs da contabilidade
set_ids_contabilidade = set(ids_contabilidade)

docs_terceirizado_faltando_contabilidade = [
  doc_id for doc_id in ids_terceirizado if doc_id not in set_ids_contabilidade
]

print("\nDocumentos do terceirizado que não constam na contabilidade")
if docs_terceirizado_faltando_contabilidade:
  df_detalhes_faltando_contabilidade = df_terceirizado[
      df_terceirizado[coluna_doc_terceirizado].isin(docs_terceirizado_faltando_contabilidade)
  ].drop_duplicates(subset=[coluna_doc_terceirizado])

  print(f"Encontrei {len(docs_terceirizado_faltando_contabilidade)} documento(s) faltando:")
  print(df_detalhes_faltando_contabilidade)

  # Salva o resultado em outro arquivo CSV
  df_detalhes_faltando_contabilidade.to_csv('terceirizado_sem_contabilidade.csv', index=False)
  print("\nDetalhes salvos em 'terceirizado_sem_contabilidade.csv'")
else:
  print("Todos os documentos do terceirizado foram encontrados na contabilidade.")

print("\nProcesso de comparação finalizado.")