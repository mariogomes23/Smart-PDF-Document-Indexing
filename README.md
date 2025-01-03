# Indexação Inteligente de Documentos PDF

## Visão Geral
Este repositório implementa uma solução para indexação e classificação inteligente de documentos PDF. A aplicação permite carregar arquivos PDF, extrair texto e identificar automaticamente o tipo de documento (ex.: Contrato, Fatura, Relatório) usando a API da Groq. A interface do usuário é desenvolvida com Streamlit para facilitar a interatividade.

## Funcionalidades
- **Carregamento de PDF:** Upload de documentos PDF diretamente na interface.
- **Extração de Texto:** Processa os PDFs e extrai o conteúdo textual utilizando a biblioteca `PyPDF2`.
- **Identificação do Tipo de Documento:** Utiliza a API Groq para classificar o documento com base no texto extraído.
- **Interface Intuitiva:** Desenvolvida com Streamlit, permitindo uso direto no navegador.

## Tecnologias Utilizadas
- **Linguagem:** Python 3.8+
- **Bibliotecas:**
  - `pandas`
  - `streamlit`
  - `PyPDF2`
  - `python-dotenv`
  - `groq`
- **API:** Groq para análise do texto e classificação.

## Como Usar

### 1. Clonar o Repositório
```bash
git clone https://github.com/mariogomes23/Smart-PDF-Document-Indexing
cd Smart-PDF-Document-Indexing
```

### 2. Configurar o Ambiente
Certifique-se de que as dependências estejam instaladas:
```bash
pip install -r requirements.txt
```

### 3. Configurar Variáveis de Ambiente
Crie um arquivo `.env` no diretório raiz com a chave de API da Groq:
```
GROQ_API_KEY=your_groq_api_key_here
```

### 4. Executar a Aplicação
Inicie a aplicação com o comando:
```bash
streamlit run app.py
```
Acesse a interface em [http://localhost:8501](http://localhost:8501).

## Estrutura do Projeto
```
.
├── app.py                # Arquivo principal da aplicação
├── requirements.txt      # Lista de dependências do projeto
├── .env                  # Arquivo de variáveis de ambiente
└── README.md             # Documentação do repositório
```

## Melhorias Futuras
- **Integração com OCR:** Suporte para leitura de documentos digitalizados utilizando `pytesseract`.
- **Processamento de Outros Formatos:** Permitir upload de imagens e documentos Word.
- **Funcionalidades Avançadas:** Adicionar armazenamento e busca de documentos classificados.

## Contribuições
Contribuições são bem-vindas! Para contribuir:
1. Fork este repositório.
2. Crie uma branch para a sua funcionalidade (`git checkout -b minha-funcionalidade`).
3. Commit suas alterações (`git commit -m 'Adiciona minha funcionalidade'`).
4. Envie o push para a branch (`git push origin minha-funcionalidade`).
5. Abra um Pull Request.

## Licença
Este projeto está licenciado sob a [Licença MIT](LICENSE).

## Contato
Caso tenha dúvidas ou sugestões, entre em contato:
- **Email:** mario.gomes@example.com
- **GitHub:** [Mario Gomes](https://github.com/seu-usuario)

---
Esperamos que este projeto seja útil para você! Se gostou, não esqueça de dar uma estrela no repositório. ⭐

