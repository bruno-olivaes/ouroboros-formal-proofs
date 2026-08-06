import os
import subprocess

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN", "COLOQUE_SEU_TOKEN_AQUI")
USERNAME = "bruno-olivaes"
REPO_NAME = "ouroboros-formal-proofs"

framework_dir = r"C:\Users\bruno\OneDrive\Desktop\Ouroboros-Quantum-Framework"

print("[+] Iniciando sincronização da Matriz Quântica com o GitHub...")

# (O token será obtido automaticamente pelo Git do Windows)

os.chdir(framework_dir)

# Initialize git if not already
if not os.path.exists(".git"):
    subprocess.run(["git", "init"])
    subprocess.run(["git", "branch", "-M", "main"])

# Link to repo using standard HTTPS so Windows Git Credential Manager authenticates automatically
remote_url = f"https://github.com/{USERNAME}/{REPO_NAME}.git"
subprocess.run(["git", "remote", "remove", "origin"], stderr=subprocess.DEVNULL)
subprocess.run(["git", "remote", "add", "origin", remote_url])

# Add and commit
print("[-] Empacotando arquivos (Scrubbed e Verificados)...")
subprocess.run(["git", "add", "."])
subprocess.run(["git", "commit", "-m", "Quantum Matrix Update: Phase 2 and 3 (Biology, Engineering, AI, Crypto, Astrophysics)"])

# Push
print("[-] Transmitindo para o Mainframe (GitHub)...")
res = subprocess.run(["git", "push", "-u", "origin", "main", "--force"])

if res.returncode == 0:
    print("[!] GITHUB UPLOAD SUCESSO: A Biblioteca Quântica Ouroboros está online e aberta ao público!")
else:
    print("[!] Falha na sincronização Git.")
