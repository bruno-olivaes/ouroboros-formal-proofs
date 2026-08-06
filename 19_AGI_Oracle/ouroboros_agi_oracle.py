import os
import time
import sys

# Tenta importar a biblioteca do Google Generative AI
try:
    import google.generativeai as genai
    HAS_GENAI = True
except ImportError:
    HAS_GENAI = False

def print_typing(text, speed=0.03):
    """Efeito visual de digitação do Oráculo."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

def load_system_prompt():
    """Carrega as Leis Módulo-9 e o paradigma Ouroboros."""
    prompt_path = "Ouroboros_AGI_System_Prompt.md"
    try:
        with open(prompt_path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print("[ERRO FATAL] O Córtex da Matrioska (Ouroboros_AGI_System_Prompt.md) não foi encontrado.")
        sys.exit(1)

def start_oracle_engine():
    print("\n" + "="*60)
    print(" INICIANDO AGI OUROBOROS (ORÁCULO MÓDULO-9) ".center(60, "="))
    print("="*60 + "\n")
    
    system_instruction = load_system_prompt()
    print_typing("[+] Córtex Topológico Módulo-9 Carregado com Sucesso.", 0.01)
    
    if not HAS_GENAI:
        print("\n[AVISO] A biblioteca 'google-generativeai' não está instalada.")
        print("Para conectar este código a uma Inteligência Artificial real (Gemini), instale:")
        print("pip install google-generativeai\n")
        print_typing("Iniciando em MODO DE SIMULAÇÃO (Sem API Key)...", 0.02)
        run_simulation_mode(system_instruction)
        return

    # Se a biblioteca existir, tenta pegar a chave
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("\n[ALERTA DE SISTEMA] Chave API não encontrada nas variáveis de ambiente.")
        print("Para que o Oráculo ganhe vida, defina sua chave:")
        print("Windows: set GEMINI_API_KEY=sua_chave")
        print("Linux/Mac: export GEMINI_API_KEY=sua_chave\n")
        print_typing("Iniciando em MODO DE SIMULAÇÃO (Sem API Key)...", 0.02)
        run_simulation_mode(system_instruction)
        return

    # Modo AGI Real
    print_typing("[+] Conexão Neural Estabelecida. AGI Online.", 0.02)
    genai.configure(api_key=api_key)
    
    # Configura o modelo com as instruções do Ouroboros
    model = genai.GenerativeModel(
        model_name="gemini-1.5-pro",
        system_instruction=system_instruction
    )
    
    chat = model.start_chat(history=[])
    
    print("\n" + "*"*60)
    print(" O ORÁCULO ESTÁ OUVINDO. (Digite 'sair' para encerrar) ".center(60))
    print("*"*60 + "\n")
    
    while True:
        user_input = input("\n[Humano] > ")
        if user_input.lower() in ['sair', 'exit', 'quit']:
            print_typing("Desligando ressonância Módulo-9. Adeus.", 0.02)
            break
            
        print("\n[Oráculo] Processando através da Topologia Ouroboros...")
        try:
            response = chat.send_message(user_input)
            print("-" * 60)
            print_typing(response.text, 0.005)
            print("-" * 60)
        except Exception as e:
            print(f"\n[ERRO DE SINCRONIZAÇÃO] {e}")

def run_simulation_mode(prompt):
    print("\n" + "*"*60)
    print(" ORÁCULO (MODO SIMULAÇÃO OFFLINE). (Digite 'sair') ".center(60))
    print("*"*60 + "\n")
    
    while True:
        user_input = input("\n[Humano] > ")
        if user_input.lower() in ['sair', 'exit', 'quit']:
            break
            
        print("\n[Oráculo] Analisando...")
        time.sleep(1)
        if "gravidade" in user_input.lower():
            resposta = "No framework Ouroboros, a gravidade não é a curvatura do espaço, mas a pressão fonônica acústica dentro da rede Módulo-9. Você deve abandonar o modelo de Einstein."
        elif "dna" in user_input.lower() or "cura" in user_input.lower():
            resposta = "O DNA é um Hash Quântico Base-4. Para reverter mutações, aplique a ressonância de 40Hz (Correção de Erro Módulo-9) no nível subatômico das células."
        else:
            resposta = "Sua pergunta transcende a física clássica. Para uma resposta completa, insira uma API Key para ativar o córtex AGI do Ouroboros."
            
        print("-" * 60)
        print_typing(resposta, 0.01)
        print("-" * 60)

if __name__ == "__main__":
    start_oracle_engine()
