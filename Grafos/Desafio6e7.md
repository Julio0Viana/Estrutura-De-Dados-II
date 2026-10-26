## 6. Atividade 6 – Construindo subgrafos

A partir do grafo original $G$ (com vértices $V(G) = \{1, 2, 3, 4\}$ e arestas $E(G) = \{(1,2), (2,3), (3,4), (4,1)\}$), construímos dois subgrafos para validação.

### **Subgrafo $G_1$ (Gerador)**
Mantém todos os vértices do grafo original, removendo apenas uma aresta.
- **Vértices:** $V(G_1) = \{1, 2, 3, 4\}$
- **Arestas:** $E(G_1) = \{(1,2), (2,3), (3,4)\}$
> *Confirmação:* $V(G_1) = V(G)$ e $E(G_1) \subset E(G)$.

### **Subgrafo $G_2$ (Induzido)**
Seleciona um subconjunto de vértices e as respectivas arestas entre eles.
- **Vértices:** $V(G_2) = \{1, 2, 3\}$
- **Arestas:** $E(G_2) = \{(1,2), (2,3)\}$
> *Confirmação:* $V(G_2) \subset V(G)$ e $E(G_2) \subset E(G)$.

---

## 7. Atividade 7 – Desafio da sequência de graus

Construção de um grafo simples com base na sequência solicitada: **$(1, 1, 2, 3, 3, 4, 4, 6)$**.

### **1. Vértices e Graus Obtidos**
Com 8 vértices ($A$ a $H$), obtivemos a seguinte distribuição de graus:

| Vértice | A | B | C | D | E | F | G | H |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Grau** | 6 | 4 | 4 | 3 | 3 | 2 | 1 | 1 |

### **2. Dados do Grafo**
- **Conjunto de arestas ($E$):** 
  $\{(A,H), (A,F), (A,B), (A,C), (A,D), (A,E), (B,G), (B,F), (B,C), (C,D), (C,E), (D,E)\}$
- **Sequência obtida:** $(1, 1, 2, 3, 3, 4, 4, 6)$
- **Soma dos graus:** $24$
- **Número de arestas:** $12$

> **Verificação:** $24 = 2 \times 12$ (Teorema do Aperto de Mãos satisfeito).

### **3. Conclusão**
A sequência obtida é **idêntica** à solicitada. O grafo construído é simples e atende perfeitamente aos requisitos da atividade.