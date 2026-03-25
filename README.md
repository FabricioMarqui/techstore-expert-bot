#  TechStore Expert Bot - IA Especialista

Este repositório contém um **Chatbot Especialista** desenvolvido em Python, utilizando a API do **Google Gemini 2.5 Flash**. O bot foi projetado para atuar como um atendente virtual da loja **TechStore**, fornecendo informações precisas sobre políticas de entrega, trocas e garantias.

##  Objetivo
Demonstrar a implementação de um modelo de IA com **restrição de domínio**, garantindo que as respostas sejam baseadas exclusivamente em um contexto pré-definido, evitando "alucinações" e mantendo a persona da marca.

##  Requisitos Técnicos Atendidos
- **Persona:** Atendente técnico e prestativa.
- **Contexto Privado:** Base de conhecimento sobre Entrega, Troca, Garantia e Pagamento.
- **Configuração Avançada:** Uso de `GenerateContentConfig` para definir as instruções de sistema.
- **Controle de Fluxo:** Gerenciamento de turnos (3 perguntas) com encerramento e resumo automático.

##  Como Rodar o Projeto

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/SEU_USUARIO/techstore-expert-bot.git](https://github.com/SEU_USUARIO/techstore-expert-bot.git)
    ```
2.  **Instale a biblioteca necessária:**
    ```bash
    pip install -q -U google-generativeai
    ```
3.  **Configuração da API Key:**
    - Obtenha sua chave no [Google AI Studio](https://aistudio.google.com/).
    - Se estiver no Colab, adicione aos Secrets como `GEMINI_API_KEY`.

##  Lógica de Implementação
O bot utiliza o `role="model"` no histórico inicial para "treinar" o comportamento do assistente antes da interação com o usuário, garantindo que ele siga as diretrizes da **TechStore** à risca.

```python
# Exemplo da lógica de histórico (History)
history=[
    {"role": "user", "parts": ["Olá, como você deve atuar?"]},
    {"role": "model", "parts": ["Olá! Sou o Assistente da TechStore..."]}
]
