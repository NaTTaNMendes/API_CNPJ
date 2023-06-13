import requests
import time

def fazer_teste_de_estresse(url, duracao):
    start_time = time.time()
    end_time = start_time + duracao
    num_requests = 0

    while time.time() < end_time:
        response = requests.get(url)

        if response.status_code == 200:
            num_requests += 1
        else:
            print("Erro na requisição")
    
    return num_requests

# Exemplo de uso
url = "link"
duracao = 60  # Duração do teste em segundos (1 minuto)

num_requests = fazer_teste_de_estresse(url, duracao)

# Exibir quantidade de requisições realizadas
print("Quantidade de requisições realizadas:", num_requests)
