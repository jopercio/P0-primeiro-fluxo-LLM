from google import genai
from dotenv import load_dotenv

# lê a chave API do arquivo .env
load_dotenv()

# importa o template do prompt
with open('prompt.md') as prompt_file:
    prompt = prompt_file.read()

# inicializa o cliente
client = genai.Client()

# dados de entrada
usuario=input("Digite sua solicitação: ").strip()

if not usuario:
    print("Solicitação inválida. Tente novamente.")
else:
    mensagem = f"""
    {prompt}

    Solicitação do usuário:
    {usuario}
    """

    # chamar o LLM
    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=mensagem,
    )

    # exibir resposta
    print(response.text)