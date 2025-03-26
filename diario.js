function mostrarForm(tipo) {
    document.getElementById('escrever-form').style.display = 'none';
    document.getElementById('ler-form').style.display = 'none';
    document.getElementById(`${tipo}-form`).style.display = 'block';
}
2
:
0
async function salvarEntrada() {
    const entrada = document.getElementById('entrada-texto').value;
    if (!entrada) return alert("Digite algo!");

    const response = await fetch('/add', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ entrada })
    });

    const data = await response.json();
    if (data.success) {
        alert("Salvo com sucesso!");
        document.getElementById('entrada-texto').value = "";
    } else {
        alert("Erro ao salvar.");
    }
}

async function lerDiario() {
    const senha = document.getElementById('senha-input').value;
    const response = await fetch('/ler', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ senha })
    });

    const data = await response.json();
    const container = document.getElementById('diario-container');
    container.innerHTML = "";

    if (data.success) {
        data.diario.forEach((entrada, index) => {
            const div = document.createElement('div');
            div.innerHTML = `<strong>Entrada ${index + 1}:</strong> ${entrada}`;
            container.appendChild(div);
        });
    } else {
        alert("Senha incorreta!");
    }
