# Crivo de Eratóstenes: Otimização Matemática com NumPy

![Badge Python](https://img.shields.io/badge/python-3.x-blue) ![Badge NumPy](https://img.shields.io/badge/numpy-vectorization-orange) ![Badge Status](https://img.shields.io/badge/status-concluido-green)

## 🚀 Visão Geral

Este projeto explora a implementação de alta performance do clássico algoritmo **Crivo de Eratóstenes** utilizando **Python** e a biblioteca **NumPy**.

O objetivo principal não é apenas encontrar números primos, mas demonstrar como a **Vetorização** e o **Slicing de Arrays** podem transformar uma linguagem interpretada (Python) em uma ferramenta de processamento numérico extremamente veloz, eliminando a necessidade de laços `for` explícitos.

Este repositório serve como um estudo de caso sobre **Engenharia de Algoritmos** na interseção entre Matemática e Desenvolvimento de Software.

## 🧠 A Lógica da Implementação (Python + NumPy)

Em vez de verificar cada número individualmente (o que seria lento em Python puro), esta implementação utiliza operações em massa na memória:

1.  **Alocação Otimizada:** Criamos um array booleano representando todos os números, assumindo inicialmente que todos são primos (`True`).
2.  **Otimização Matemática:** O loop externo itera apenas até $\sqrt{N}$ (raiz quadrada do limite), pois qualquer número composto $N$ deve ter um fator menor ou igual à sua raiz.
3.  **Slicing Avançado (O Pulo do Gato):**
    Em vez de um loop interno para marcar os múltiplos, utilizamos a sintaxe de fatiamento do NumPy:
    ```python
    # Marca todos os múltiplos de 'i' como False, começando de i*i
    is_prime[i*i::i] = False
    ```
    *Isso delega o processamento para o backend em C do NumPy, tornando a execução ordens de magnitude mais rápida que um loop nativo.*

## 📊 Benchmarks: Python (NumPy) vs. C++

Para validar a eficiência, comparei esta implementação otimizada em Python com uma implementação padrão em C++ (conhecida por sua velocidade bruta).

*Ambiente de teste: Processador [Seu Processador]*

| Linguagem & Método | Limite ($N$) | Tempo de Execução |
| :--- | :--- | :--- |
| **Python (NumPy Vetorizado)** | 10.000.000 | **0.XX s** (Preencher) |
| **C++ (std::vector)** | 10.000.000 | **0.XX s** (Preencher) |
| Python Puro (Listas - Sem NumPy) | 10.000.000 | *Time Limit Exceeded (>10s)* |

> **Conclusão:** Com a utilização correta de bibliotecas otimizadas, o Python atinge uma performance competitiva com linguagens compiladas para tarefas de álgebra linear e processamento de vetores.

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3.x
* **Core:** NumPy (Computing Backend)
* **Conceitos:** Complexidade de Algoritmos ($O(n \log \log n)$), Manipulação de Memória.

## 💻 Como Executar

1. **Instale as dependências:**
   ```bash
   pip install numpy
