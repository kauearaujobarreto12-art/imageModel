# Projeto de Reconhecimento e Programação

Este repositório reúne dois focos principais:

1. Uma página web com reconhecimento de imagens usando câmera e modelo do Teachable Machine.
2. Scripts Python de apoio que demonstram verificação de número primo e refatoração de código.

---

## Estrutura do projeto

- `index.html`
  - Página de demonstração que usa a webcam para capturar imagens e classificar em tempo real.
  - Utiliza `TensorFlow.js` e `Teachable Machine` para carregar um modelo remoto.

- `test-assistent-programming/`
  - `num_primo.py`: script Python que verifica se um número é primo, valida entradas e executa testes básicos.
  - `refatoracao.py`: exemplo de refatoração onde uma função antiga foi transformada em `summarize_numbers`.
  - `explicacao_num_primo.md`: documentação explicativa do algoritmo de primalidade.
  - `explicacao_refatoracao.md`: descrição das mudanças e benefícios da refatoração.
  - `debug.py`: arquivo vazio atualmente disponível para uso futuro.

---

## `index.html`

A página contém:

- interface escura com botão para iniciar a câmera;
- área de visualização da webcam;
- painel de resultados com classes previstas e barras de probabilidade;
- indicadores de status de carregamento e execução.

### Tecnologias usadas

- HTML/CSS padrão
- Bootstrap 5.3
- TensorFlow.js
- Teachable Machine Image

### Modelo carregado

O modelo remoto é carregado a partir de:

- `https://teachablemachine.withgoogle.com/models/aOY-mKp7c/`

Quando a câmera é iniciada, o script:

1. carrega o modelo e metadata;
2. inicializa a webcam em 280x280 pixels;
3. atualiza o vídeo em tempo real;
4. faz predições contínuas e mostra as probabilidades no painel.

---

## `test-assistent-programming/num_primo.py`

Este script implementa uma verificação de número primo com as seguintes características:

- validação de entrada para inteiros não negativos;
- tratamento de casos base (`0`, `1`, `2`, `3`);
- eliminação imediata de múltiplos de `2` e `3`;
- loop otimizado com passos de `6k ± 1` até a raiz quadrada de `n`.

### Como executar

```bash
python test-assistent-programming/num_primo.py
```

O script pede um número inteiro ao usuário e informa se ele é primo.

---

## `test-assistent-programming/refatoracao.py`

Esse arquivo contém uma versão refatorada de uma função de agregação numérica. A função `summarize_numbers`:

- recebe um iterável de valores numéricos;
- valida se há pelo menos um elemento;
- calcula soma, média, máximo e mínimo;
- retorna esses quatro valores.

### Como executar

```bash
python test-assistent-programming/refatoracao.py
```

Ele imprime um exemplo de saída usando uma lista de números de amostra.

---

## Como abrir o projeto

### Navegador

Para usar a página de reconhecimento, abra `index.html` no navegador. Caso o carregamento de recursos ou da câmera falhe por causa de restrições de arquivo local, execute um servidor HTTP simples:

```bash
cd c:\Users\KAUEAMORIM\Desktop\ProjetoSiteComReconhecimentoJoia
python -m http.server 8000
```

Em seguida, abra `http://localhost:8000`.

### Python

Use a versão do Python já disponível no sistema. Por exemplo:

```bash
python --version
python test-assistent-programming/num_primo.py
python test-assistent-programming/refatoracao.py
```

---

## Possíveis melhorias

- adicionar interface gráfica para o script `num_primo.py`;
- incluir testes automatizados com `unittest` ou `pytest`;
- documentar o comportamento esperado do modelo do Teachable Machine;
- preencher `debug.py` com utilitários de depuração ou testes adicionais;
- adicionar uma página separada `README` para explicar o conjunto de classes do modelo de imagem.

---

## Observações

Este repositório mistura um projeto front-end de reconhecimento de imagens com pequenos exemplos Python de algoritmos e refatoração. Ele parece ser um conjunto de provas de conceito ou exercícios de estudo aplicados pelo autor.
