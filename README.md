# High-Performance Prime Sieve (NumPy Optimized)

![Badge License](https://img.shields.io/badge/license-MIT-green) ![Badge Python](https://img.shields.io/badge/python-3.x-blue) ![Badge NumPy](https://img.shields.io/badge/numpy-vectorization-orange)

## 🚀 Visão Geral

Uma implementação de alta performance do clássico algoritmo **Crivo de Eratóstenes**, otimizada para processamento de grandes volumes de dados numéricos.

Ao contrário de implementações ingênuas que utilizam loops aninhados em Python puro (que são custosos computacionalmente), este projeto alavanca a **Vetorização do NumPy** e **Broadcasting** para realizar operações em nível de C, reduzindo drasticamente o tempo de execução para inputs grandes.

Este projeto representa a **interseção entre Matemática e Engenharia de Software**, demonstrando como o conhecimento profundo de um algoritmo ($O(n \log \log n)$) combinado com a ferramenta certa pode gerar software eficiente.

## ⚙️ Otimizações Matemáticas & Técnicas

* **Vetorização vs. Iteração:** Substituição de laços `for` lentos por operações vetorizadas de array e *slicing* avançado (`arr[start::step]`).
* **Redução do Espaço de Busca:**
  * O algoritmo itera apenas até $\sqrt{n}$ (raiz quadrada do limite), pois qualquer número composto n deve ter um fator menor ou igual à sua raiz.
  * O "risco" dos múltiplos começa em $p^2$ (e não em $2p$), evitando remarcar números já processados.
* **Eficiência de Memória:** Utilização de arrays booleanos para representar o estado dos números, minimizando o *overhead* de memória em comparação com listas de inteiros.

## 📊 Benchmarks (Comparativo)

*Testes realizados em processador [Seu Processador, ex: i5/Ryzen 5]*

| Input (Limite $N$) | Python Puro (Listas) | Minha Implementação (NumPy) | Ganho de Performance |
| :--- | :--- | :--- | :--- |
| 1.000.000 ($10^6$) | ~0.XX s | **0.0X s** | **10x mais rápido** |
| 10.000.000 ($10^7$) | ~X.XX s | **0.XX s** | **--x mais rápido** |

> **Nota:** A abordagem vetorizada escala significativamente melhor à medida que $N$ cresce.

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3
* **Computação Numérica:** NumPy
* **Conceitos:** Análise Assintótica, Álgebra, Manipulação de Memória.

## 💻 Como Executar

1. **Instale as dependências:**
   ```bash
   pip install numpy
