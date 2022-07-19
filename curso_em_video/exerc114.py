from urllib.error import URLError
import requests as req

try:
    resp = req.get('http://pudim.com.br')

except URLError:
    print("\033[31mFalha na conexão!\033[m\nConfira se sua internet está funcionando corretamente!")

else:
    print("\033[32mSucesso!\033[m\nAcesso realizado.")