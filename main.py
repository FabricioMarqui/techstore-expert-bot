# 1. Instalação
!pip install -q -U google-genai

import os
import time
from google import genai
from google.genai import types
from google.colab import userdata

# 2. Configuração do Cliente (Extração de String)
try:
    raw_key = userdata.get('GEMINI_API_KEY')
    API_KEY = raw_key.get('value', raw_key) if isinstance(raw_key, dict) else str(raw_key)
except:
    from getpass import getpass
    API_KEY = getpass("Cole sua API Key: ")

client = genai.Client(api_key=API_KEY)

# 3. Contexto (Base de Conhecimento TechStore)
context = """
Você é o Atendente Virtual da TechStore. Seu conhecimento é restrito:
1. ENTREGA: 3-5 dias (Capitais); até 10 dias (Interior). Frete grátis acima de R$ 500.
2. TROCA: Arrependimento (7 dias); Defeito (30 dias). Requer Nota Fiscal.
3. GARANTIA: Eletrônicos (12 meses); Acessórios (6 meses). Não cobre mau uso.
4. PAGAMENTO: PIX (5% desc); Cartão (até 10x sem juros, parcela mín R$ 50).
TAREFA: Responda exatamente 3 perguntas. Na 3ª resposta, faça um resumo e encerre o chat.
"""

# 4. Configuração (GenerateContentConfig + role="model")
config_especialista = types.GenerateContentConfig(
    system_instruction="Você é um assistente especialista que nunca alucina.",
    temperature=0.1
)

instrucoes_history = [
    types.Content(
        role="user", 
        parts=[types.Part(text="Como você deve atuar?")]
    ),
    types.Content(
        role="model", 
        parts=[types.Part(text=f"Sou o Assistente TechStore. Seguirei este contexto: {context}")]
    )
]

# 5. Execução do Chatbot
def executar_bot_techstore():
    # REMOVIDO O 'models/' DA FRENTE PARA EVITAR ERRO 404 NA SDK NOVA
    try:
        chat = client.chats.create(
            model="gemini-2.5-flash", 
            config=config_especialista,
            history=instrucoes_history
        )
        
        print("--- 📱 TechStore: Atendimento Especializado ---\n")

        for i in range(1, 4):
            pergunta = input(f"Pergunta {i}/3: ")
            
            if i == 3:
                pergunta += " (Responda, faça um resumo final dos atendimentos e encerre)."
                
            try:
                response = chat.send_message(pergunta)
                print(f"\nAssistente: {response.text}\n" + "-"*30)
                # Pequena pausa para não estourar a cota (429)
                time.sleep(1) 
            except Exception as e:
                print(f"\nErro no envio: {e}")
                break

        print("\n[SESSÃO FINALIZADA]")
    
    except Exception as e:
        print(f"\nErro ao iniciar chat: {e}")

# Iniciar o bot
executar_bot_techstore()