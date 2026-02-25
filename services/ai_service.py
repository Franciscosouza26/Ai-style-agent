import time
import google.genai as genai
import os
from dotenv import load_dotenv

load_dotenv()


client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def analisar_codigo(codigo):

    prompt = f"""
    você é um especialista em UI/UX.

    Analise o código abaixo e forneça:

    1. Problemas de UX
    2. Problemas de contraste
    3. Problemas de hierarquia visual
    4. sugestão na prática
    5. Versão melhorada do código

    código:
    {codigo}
    """
    tentativas = 3

    for i in range (tentativas):
        try:
            response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents =prompt
              )
            return response.text
        except Exception as e:
            print(f"Tentativa {i+1} falhou", e)
            time.sleep(2)
    return "Erro no serviço temporariamente indisponível. Tente Novamente mais tarde"
