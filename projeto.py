import getpass

senha = "python123"
diario = []

print("Diário Secreto - Suas memórias protegidas")

while True:
    print("\n1. Escrever entrada")
    print("2. Ler diário")
    print("3. Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        entrada = input("Escreva sua entrada hoje: ")
        diario.append(entrada)
        print("Salvo com sucesso!")
    elif opcao == "2":
        if getpass.getpass("Digite a senha: ") == senha:
            print("\n--- SEU DIÁRIO ---")
            for i, entrada in enumerate(diario, 1):
                print(f"{i}. {entrada}")
        else:
            print("Senha incorreta!")
    elif opcao == "3":
        print("Até logo! Seus segredos estão seguros.")
        break
    else:
        print("Opção inválida!")
from flask import Flask, render_template, request, jsonify
import json
import os

app = Flask(__name__)
senha = "python123"
diario = []

# Nome do arquivo para salvar os dados
ARQUIVO_DIARIO = "diario.json"

def carregar_diario():
    if os.path.exists(ARQUIVO_DIARIO):
        with open(ARQUIVO_DIARIO, 'r') as f:
            return json.load(f)
    return []

def salvar_diario(dados):
    with open(ARQUIVO_DIARIO, 'w') as f:
        json.dump(dados, f)

# Carrega as entradas ao iniciar o servidor
diario = carregar_diario()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def add_entrada():
    entrada = request.json.get('entrada')
    if entrada:
        diario.append(entrada)
        salvar_diario(diario)  # Salva no arquivo
        return jsonify({"success": True})
    return jsonify({"success": False})

@app.route('/ler', methods=['POST'])
def ler_diario():
    input_senha = request.json.get('senha')
    if input_senha == senha:
        return jsonify({"success": True, "diario": diario})
    return jsonify({"success": False})

if __name__ == '__main__':
    app.run(debug=True)
