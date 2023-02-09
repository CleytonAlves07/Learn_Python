import requests
# import time

# Depois da décima chamada vai aparecer status 429 - Too many requests.
# Por isso a importância do time.sleep
# for _ in range(15):
#     response = requests.get("https://www.cloudflare.com/rate-limit-test/")
#     print(response.status_code)
#     time.sleep(6)


# Timeout

# Delay de 10 segundos
# Simulando um timeout de 2 segundos para a requisição falhar
# Colocando um try/except para tratar o erro de timeout
try:
    response = requests.get("https://httpbin.org/delay/10", timeout=3)
except requests.Timeout:
    response = requests.get("https://httpbin.org/delay/1", timeout=3)
finally:
    print(response.status_code)
