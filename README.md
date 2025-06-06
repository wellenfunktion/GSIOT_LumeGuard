# 🚑 LumeGuard — Protótipo de Reconhecimento de Gestos para Cenários de Desastre

## RM550702 - Enzo Vasconcelos
## RM98323 - Felipe Hideki 
## RM550295 - Guilherme Milheiro

## 🚨 Contexto

Em áreas propensas a **desastres naturais** como enchentes, deslizamentos e tempestades, a capacidade de **comunicação não verbal** pode ser essencial para garantir a segurança das pessoas.

Em ambientes de:

* **Baixa iluminação**
* **Ruídos excessivos**
* **Queda de energia elétrica**

pode ser difícil usar métodos tradicionais (voz, celular, sirene).
**Gestos com as mãos** são uma forma universal e simples para chamar atenção ou solicitar ajuda.

---

## 🌟 Visão do Projeto

**LumeGuard** é um **protótipo experimental** de sistema de reconhecimento de gestos com as mãos, voltado para ambientes de risco.

Atualmente, o sistema é capaz de:

🔢 Analisar **vídeos previamente gravados**
🔢 Detectar dois tipos de gestos:

* ✌️ **Sinal de paz** → Pedido de ajuda
* 👋 **Aceno lateral** → Sinal de emergência

🔢 Gerar:

* Alertas sonoros
* Log de eventos detectados

---

## ⚠️ Estado Atual

📌 Este é um **protótipo de demonstração**.

* O sistema **não funciona em tempo real com câmeras ao vivo** ainda.
* O vídeo de entrada é um arquivo `.mp4` (exemplo: `teste_aceno_escuro.mp4`).
* O objetivo é **explorar a viabilidade da técnica** de reconhecimento de gestos com MediaPipe + OpenCV.

---

## 🚀 Como Usar

### 1️⃣ Pré-requisitos

* Python 3.8+
* Baixar o restante do projeto (Modelos muito grandes para serem hosteados pelo Git) -> https://drive.google.com/file/d/1DBWNRV3a5Q50hqCm89qGjjy_5He1MMRs/view?usp=sharing
* Depois de descompactar o .zip, abrir na sua IME preferida e seguir as instruções
* Instalar dependências:

```bash
pip install opencv-python mediapipe
```

### 2️⃣ Preparar vídeo de teste

* Grave um vídeo simulando gestos em um cenário de pouca iluminação.
* Exemplo de nome: `teste_aceno_escuro.mp4`
* Coloque o vídeo na pasta do projeto.

### 3️⃣ Configurar o código

Abra o arquivo `main.py` e edite a linha:

```python
video_path = "teste_aceno_escuro.mp4"
```

Troque o nome do arquivo se necessário.

### 4️⃣ Executar o sistema

```bash
python main.py
```

### 5️⃣ Resultados

* O sistema abrirá uma janela com o vídeo processado.
* Quando detectar um gesto válido:

  * Um alerta sonoro será emitido.
  * O evento será salvo no arquivo `log_lumeguard.txt`.

### 6️⃣ Encerrar

* Pressione **Q** para encerrar o programa.

---

## 📸 Exemplos Visuais 

### Aceno Lateral Detectado:

![Aceno](https://media.discordapp.net/attachments/675563459383001098/1380592398748614778/3A389A4B-014B-49D4-9AC1-49F670394803.png?ex=6844705e&is=68431ede&hm=cf61578c8c8855cfcea4b18791dea697c945363190a78ec64b6220b8ad0b4eb4&=&format=webp&quality=lossless&width=1585&height=1701)

---

## 🔍 Possível Aplicação Futura

Embora o protótipo atual funcione com vídeos gravados, ele poderia evoluir para:

* Rodar em **mini-PCs com câmeras fixas** instaladas em abrigos temporários
* Ser integrado em **kits portáteis de monitoramento** para equipes de resgate
* Operar com **câmeras infravermelhas** para suportar ambientes de escuridão total

Por enquanto, o objetivo é demonstrar a viabilidade da **detecção de gestos em condições adversas**.
