import requests
import streamlit as st

BASE_URL = 'https://api.github.com'

def selecionar_usuario(username):
   url = f'{BASE_URL}/users/{username}' 
   response = requests.get(url)
   if response.status_code == 200:
      return response.json()
   else:
      None

def ui():
    st.markdown('<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD" crossorigin="anonymous">', unsafe_allow_html=True)     

    st.title('Consulta Github')
    username = st.text_input('Insira o username de usuário do github')

    if st.button('Buscar'):
       info_usuario = selecionar_usuario(username)
       if info_usuario is not None:
          st.markdown(f'''
            <div class="card" style="width: 18rem;">
               <img src="{info_usuario['avatar_url']}" class="card-img-top" alt="...">
               <div class="card-body">
                  <h5 class="card-title">{info_usuario['login']}</h5>
                  <p class="card-text">{info_usuario['bio']}</p>
                  <a href="{info_usuario['html_url']}" style="color: white; text-decoration: none;" class="btn btn-primary">Ver perfil</a>
               </div>
            </div>          
                      
                      ''', unsafe_allow_html=True)

ui()    