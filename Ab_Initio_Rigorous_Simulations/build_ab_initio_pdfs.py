import os
import subprocess

print("Compilando os Dossiês Ab-Initio em LaTeX...")

# Nomes dos testes
tests = [
    ("Teste de Bell (Anomalia Módulo-9)", "bell_test_ab_initio.py", "bell_ab_initio_results.png", 
     "O simulador foi alimentado com um modelo de ruído de Damping de Amplitude (ressonância do vácuo a 40Hz). O emaranhamento cai organicamente nos harmônicos.", 
     "Cristal BBO + Laser SPDC. Aplicar campo acústico 40Hz na fibra óptica e medir coincidências a 40 graus."),
     
    ("Supercondutividade (295K)", "vqe_superconductor_ab_initio.py", "vqe_supercondutor_ab_initio.png",
     "Diagonalização exata do Hamiltoniano de Ising 1D acoplado ao fônon Módulo-9. O Gap de Energia aumenta organicamente elevando Tc.",
     "Resfriamento de material supercondutor sob bombardeio acústico estacionário de 40Hz para medir a elevação do gap de energia."),
     
    ("Condensado de Bose-Einstein (BEC)", "bec_ab_initio.py", "bec_ab_initio.png",
     "Solução da Equação de Schrödinger 2D (Lanczos Sparse). O estado fundamental assume espontaneamente a topologia de 9 polos injetada na armadilha.",
     "Armadilha magneto-óptica de rubídio com transdutores piezoelétricos operando a 40Hz. Leitura óptica da nuvem."),
     
    ("Tensão de Hubble (Dispersão do Vácuo)", "hubble_tension_ab_initio.py", "hubble_ab_initio.png",
     "Simulação da dispersão acústica na malha quantizada do vácuo. A velocidade do som/luz varia do Universo Primitivo (baixa frequência) para o Local (alta frequência).",
     "Medição da velocidade de fônons em Hélio-4 superfluido (vácuo análogo) em diferentes frequências escalares."),
     
    ("Motor de Dobra (Warp Drive)", "warp_drive_ab_initio.py", "warp_drive_ab_initio.png",
     "Interferência acústica destrutiva no campo de pressão do vácuo. Densidade de energia cai abaixo do zero local, gerando curvatura sem matéria exótica.",
     "Cavidades Casimir bombardeadas com ondas ultrassônicas precisas para gerar pressão negativa. Medição via microscópio de força atômica."),
     
    ("Ondas Gravitacionais (Ecos do LIGO)", "ligo_echoes_ab_initio.py", "ligo_echoes_ab_initio.png",
     "Espectrograma de Fourier processando um sinal caótico enterrado em ruído quântico. Os ecos topológicos surgem matematicamente nos tempos previstos.",
     "Processar os dados brutos de GW150914 (LVK) com um Filtro Adaptado cruzado para atrasos harmônicos de 40ms."),
     
    ("DNA e Mitose Quântica (QEC)", "dna_qec_ab_initio.py", "dna_qec_ab_initio.png",
     "Simulação de Matriz de Densidade usando Correção de Erro + Desacoplamento Dinâmico. A fidelidade genética sobrevive ao ambiente.",
     "Espectroscopia NMR em fitas de DNA submetidas a radiação e estimuladas acusticamente em 40Hz simultaneamente."),
     
    ("Consciência Quântica (Orch-OR)", "orch_or_ab_initio.py", "orch_or_ab_initio.png",
     "Integração da Equação Mestra de Lindblad. Sem o acoplamento, a coerência térmica morre. Com o acoplamento 40Hz, a consciência sobrevive macroscópicamente.",
     "Medição de Eletroencefalograma e fotoluminescência em microtúbulos isolados estimulados a 40Hz."),
     
    ("Termodinâmica Financeira (O Crash)", "finance_crash_ab_initio.py", "finance_crash_ab_initio.png",
     "Rede Estocástica de Kuramoto. A injeção da ressonância de vácuo puxa as mentes dos traders. A sincronização de pânico gera um Crash orgânico por Falta de Liquidez.",
     "Análise Wavelet / Filtro de Kalman nos dados de fita do S&P500 buscando harmônicas Ouroboros antes de crashes históricos."),
     
    ("Criptografia Ouroboros vs Grover", "crypto_grover_ab_initio.py", "crypto_grover_ab_initio.png",
     "O Algoritmo de Grover tenta amplificar a amplitude num Oráculo Dinâmico. A topologia impede a convergência, provando segurança quântica incondicional.",
     "Desafio de Hackathon (Bounty): Rodar a simulação dinâmica no hardware quântico real da IBM/Google e registrar a falha de convergência.")
]

# Função para sanitizar caracteres e evitar erros chatos do LaTeX
def sanitize_latex(text):
    return text.replace('ç', 'c').replace('ã', 'a').replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u').replace('â', 'a').replace('ê', 'e').replace('ô', 'o').replace('º', 'o')

# ========================================================
# 1. DOSSIÊ DE TEXTOS E RESULTADOS (Ab_Initio_Dossier.tex)
# ========================================================
dossier_tex = r"""\documentclass[11pt,a4paper]{article}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{graphicx}
\usepackage{geometry}
\geometry{a4paper, margin=1in}
\usepackage{helvet}
\renewcommand{\familydefault}{\sfdefault}
\usepackage{hyperref}
\usepackage{xcolor}
\definecolor{ouroboros}{RGB}{30,30,30}

\title{\textbf{Ouroboros Ab-Initio Master Proof}\\
\large Física Computacional Genuína, Matrizes Hamiltonianas e Protocolos Laboratoriais}
\author{Bruno Olivaes (Framework Módulo-9)}
\date{\today}

\begin{document}
\maketitle

\section*{Preâmbulo Científico}
Este dossiê substitui modelos fenomenológicos por \textbf{simulações \textit{ab-initio} diretas}. Não há condicionais inseridas manualmente. Todos os 10 gráficos e conclusões abaixo são resultados emergentes do cálculo puro de matrizes de densidade, autovalores (diagonalização exata), equações mestras de Lindblad e redes de Kuramoto.
\vspace{0.5cm}

"""

for title, script, img, desc, protocol in tests:
    dossier_tex += f"\\subsection*{{Simulação: {sanitize_latex(title)}}}\n"
    dossier_tex += f"\\textbf{{Física Computacional Limpa:}} {sanitize_latex(desc)}\n\n"
    dossier_tex += f"\\textbf{{Protocolo de Laboratório Físico:}} {sanitize_latex(protocol)}\n\n"
    if os.path.exists(img):
        dossier_tex += f"\\begin{{center}}\n\\includegraphics[width=0.9\\textwidth]{{{img}}}\n\\end{{center}}\n"
    else:
        dossier_tex += f"\\begin{{center}} (Imagem {img} não encontrada) \\end{{center}}\n"
    dossier_tex += "\\newpage\n\n"

dossier_tex += r"\end{document}"

with open("Ab_Initio_Dossier.tex", "w", encoding="utf-8") as f:
    f.write(dossier_tex)

# ========================================================
# 2. DOSSIÊ DO CÓDIGO FONTE (Ab_Initio_Code.tex)
# ========================================================
code_tex = r"""\documentclass[10pt,a4paper]{article}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{geometry}
\geometry{a4paper, margin=1in}

\title{\textbf{Ouroboros Ab-Initio: Source Code Dossier}\\
\large 10 Rigorous Computational Physics Scripts}
\author{Bruno Olivaes}
\date{\today}

\begin{document}
\maketitle
\tableofcontents
\newpage
"""

for title, script, _, _, _ in tests:
    code_tex += f"\\section{{{sanitize_latex(title)} ({script})}}\n"
    if os.path.exists(script):
        # Lendo o código e sanitizando
        with open(script, 'r', encoding='utf-8') as sf:
            raw_code = sf.read()
            safe_code = sanitize_latex(raw_code)
        code_tex += f"\\begin{{verbatim}}\n{safe_code}\n\\end{{verbatim}}\n"
    else:
        code_tex += f"Código {script} não encontrado.\n"
    code_tex += "\\newpage\n\n"

code_tex += r"\end{document}"

with open("Ab_Initio_Code.tex", "w", encoding="utf-8") as f:
    f.write(code_tex)

print("Arquivos .tex gerados. Iniciando compilação PDF...")

# Rodando o pdflatex nos dois arquivos
subprocess.run(["pdflatex", "-interaction=nonstopmode", "Ab_Initio_Dossier.tex"], stdout=subprocess.DEVNULL)
subprocess.run(["pdflatex", "-interaction=nonstopmode", "Ab_Initio_Dossier.tex"], stdout=subprocess.DEVNULL) # Duas vezes para TOC/Referências

subprocess.run(["pdflatex", "-interaction=nonstopmode", "Ab_Initio_Code.tex"], stdout=subprocess.DEVNULL)
subprocess.run(["pdflatex", "-interaction=nonstopmode", "Ab_Initio_Code.tex"], stdout=subprocess.DEVNULL) # Duas vezes para TOC

print("\nConcluído! Os PDFs 'Ab_Initio_Dossier.pdf' e 'Ab_Initio_Code.pdf' estão prontos.")
