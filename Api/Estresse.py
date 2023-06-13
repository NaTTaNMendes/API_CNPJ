import requests
import time

def fazer_teste_de_estresse(url, num_requests):
    tempos = []
    contador = 1
    for _ in range(num_requests):
        start_time = time.time()
        response = requests.get(url)
        end_time = time.time()

        contador = contador + 1
        
        tempo_requisicao = end_time - start_time
        tempos.append(tempo_requisicao)

       
        print(contador)
        if response.status_code != 200:
            print("Erro na requisição")

    return tempos

# Exemplo de uso
url = "link"
num_requests = 10000  # Número total de requisições a serem feitas

tempos_requisicoes = fazer_teste_de_estresse(url, num_requests)

# Exibir estatísticas dos tempos
print("Tempo médio de resposta:", sum(tempos_requisicoes) / len(tempos_requisicoes))
print("Tempo mínimo de resposta:", min(tempos_requisicoes))
print("Tempo máximo de resposta:", max(tempos_requisicoes))