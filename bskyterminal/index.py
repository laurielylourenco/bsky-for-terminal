from atproto import Client

def loginClient(login,password):
   try:
        client = Client()
        client.login(login, password)
        return client
   except Exception as e:
        print(f'Error logging in. Recreate your login again using command --config, your email or password may be wrong')
             
def sendPost(user,post):
    user.send_post(post)