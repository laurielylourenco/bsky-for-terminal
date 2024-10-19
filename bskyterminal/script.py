import click
import os
from index import loginClient,sendPost 


@click.command()
@click.option('--post', '-p', prompt=False, help='Post in Bluesky')
@click.option('--config', is_flag=True, help='Make or reset login and password credentials.')
def main(post, config):
    credenciais_arquivo = 'credenciais.txt'

    if config:
        # Se o usuário passou o --config, recriar o arquivo de credenciais
        login = click.prompt('Your login')
        password = click.prompt('Your password', hide_input=True)

        with open(credenciais_arquivo, 'w') as f:
            f.write(f"{login}\n{password}\n")
    else:
        
        if os.path.exists(credenciais_arquivo):
    
            with open(credenciais_arquivo, 'r') as f:
                login = f.readline().strip()
                password = f.readline().strip()

        else:
            click.echo("Error: Credentials file not found. Run the '--config' command to create it.")
            return

        if post:
            client = loginClient(login, password)
            if client: 
                sendPost(client, post)
                click.echo(f"Sended post: {post}")
        else:
            click.echo("Error: No post message was provided. Use the '-p' option to post.")

if __name__ == '__main__':
    main()
