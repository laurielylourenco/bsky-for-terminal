# Bluesky for Terminal

Este projeto é uma ferramenta de linha de comando que permite fazer posts na plataforma Bluesky diretamente pelo terminal. Ele utiliza a biblioteca `atproto` para interagir com a API de Bluesky e o `Click` para a interface de linha de comando.

## Pré-requisitos

- Python 3.7 ou superior
- As bibliotecas Python necessárias estão listadas no arquivo `requirements.txt`. Use o comando abaixo para instalá-las:

```bash
pip install -r requirements.txt
```

### Bibliotecas usadas:

- [Click](https://click.palletsprojects.com/) - para criar a interface de linha de comando.
- [atproto](https://pypi.org/project/atproto/) - para a interação com a API do Bluesky.

## Instalação

1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/bsky-for-terminal.git
   ```

2. Entre no diretório do projeto:
   ```bash
   cd bsky-for-terminal
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Instale o projeto:
   ```bash
   pip install .

   ```
5. Desistalar o projeto:
   ```bash
   pip uninstall bsky-for-terminal

   ```

## Uso

### Configuração

Antes de fazer um post, é necessário configurar suas credenciais de login no Bluesky. Você pode fazer isso usando o comando `--config`:

```bash
bsky --config
```

Este comando solicitará seu login e senha, que serão salvos em um arquivo `credenciais.txt` para uso futuro.

### Postar no Bluesky

Depois de configurar as credenciais, você pode enviar um post no Bluesky diretamente do terminal:

```bash
bsky -p "Meu post no Bluesky"
```

### Sobrescrever credenciais

Se você precisar mudar suas credenciais, pode reconfigurá-las a qualquer momento executando novamente o comando `--config`:

```bash
bsky --config
```

## Contribuições

Sinta-se à vontade para abrir issues ou enviar pull requests para melhorias e correções.
