# Crie um código em Python que teste se o site barraw está acessível pelo
# computador usado.
import urllib.request

try:
    site = urllib.request.urlopen("https://www.barraw.com.br")
except urllib.error.URLError:
    print("Erro ao tentar acessar o site")
else:
    print("Site acessado com sucesso")
    


