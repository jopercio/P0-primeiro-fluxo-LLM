from google import genai
from dotenv import load_dotenv

# lê a chave API do arquivo .env
load_dotenv()

# importa o template do prompt
with open('prompt.md') as prompt_file:
    prompt = prompt_file.read()

# inicializa o cliente
client = genai.Client()

# dados de entrada (exemplo)
input_usuario="Faz duas semanas que pedi minhas férias e ainda não tive retorno. Preciso me organizar porque quero viajar no próximo mês."

mensagem = f"{prompt}{input_usuario}"

# chamar o LLM
response = client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents=mensagem,
)

# exibir resposta
print(response.text)