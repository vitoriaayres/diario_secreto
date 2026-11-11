<div align="center">

# Diário Secreto / Secret Diary

**A password-protected virtual diary — HTML/CSS/JS front-end with a Python back-end.**

*English* · [Português](#-português)

</div>

> 🇧🇷 **Português:** aplicação de diário virtual onde cada entrada fica protegida por senha. Permite criar mensagens privadas com título, data e conteúdo; listar as entradas sem revelar o conteúdo; e ler, editar ou excluir apenas após autenticação.

## About / Sobre

O **Diário Secreto** simula um diário virtual onde os usuários armazenam mensagens, pensamentos ou segredos protegidos por senha.

**The Secret Diary** is a programming project that simulates a virtual journal where users store private messages, thoughts or secrets protected by passwords.

It started as a practice ground for **JavaScript** (front-end), **Python** (back-end / cryptography), **SQL** (storage) and **HTML/CSS** (interface).

## Features / Funcionalidades

- Create a new entry: title + message + password
- List saved entries without revealing content until unlocked
- Authenticate to read, edit or delete
- Single master password **or** per-entry passwords
- Responsive layout for mobile and desktop

- Criar nova entrada (título + mensagem + senha)
- Listar mensagens salvas sem mostrar o conteúdo até autenticar
- Autenticação por senha para ler, editar ou apagar
- Senha única (mestra) ou senhas individuais por entrada
- Responsivo, funciona em celular e computador

## Repository structure

| File | Role |
|---|---|
| `diario.html` | page structure (forms, buttons, display area) |
| `diario.css` | modern responsive styling, soft colours, open animation |
| `diario.js` | password validation, in-browser encryption, show/hide logic |
| `projeto.py` | Python back-end: routes to save entries and authenticate |
| `CNN.ipynb` | related CNN study notebook |

## Implementation notes

**Front-end** — `HTML` for structure, `CSS` for a responsive design, `JavaScript` for password validation and simple in-browser encryption (Web Crypto API / `btoa` + `atob`), showing or hiding messages according to the authentication state.

**Back-end (optional, advanced version)** — `Flask`/`Django` routes persist entries in `SQLite`/`MySQL` through a `Mensagens` table (`id`, `titulo`, `conteudo`, `senha`, `data`), releasing content only when the password matches.

**Simplified alternative** — a front-end-only variant stores entries in `localStorage` using Base64 encoding.

## 🇧🇷 Português

- **O que é:** diário virtual protegido por senha, feito como projeto de prática full-stack.
- **Funcionalidades:** criar entrada privada, listar sem revelar conteúdo, autenticar para ler/editar/excluir, senha mestra ou senhas individuais, layout responsivo.
- **Estrutura:** `diario.html` (estrutura), `diario.css` (estilo), `diario.js` (validação e criptografia), `projeto.py` (back-end Python).
- **Versões possíveis:** apenas front-end com `localStorage`, ou front-end + back-end com banco `SQLite`/`MySQL`.

## Author

[Vitoria AYRES](https://github.com/vitoriaayres)
