import os
import math
import numpy as np


class Eratostenes:
    def __init__(self, lim):
        self.lim = lim
        self._primos = np.ones(self.lim + 1, dtype=bool)
        self._primos[0] = self._primos[1] = False  # Casos Base 0 e 1 (não-primos)

    def teste_primo(self):
        for p in range(2, int(math.sqrt(self.lim)) + 1):
            if self._primos[p]:
                self._primos[p * p : self.lim + 1 : p] = False
        numeros_primos = np.where(self._primos)[0]
        return numeros_primos


def rodar_programa():
    while True:
        limite_str = input("\nDigite o limite de números | sair[ex]: ")
        if limite_str.lower() == "ex":
            print("Bye!")
            os.system("cls")
            break
        if len(limite_str) > 4:
            print("[ALERT] Segurança extra! Só procure itens com menos de 4 dígitos!")
            continue
        try:
            limite_int = int(limite_str)
            if limite_int < 0:
                print("[ERROR] Digite um valor inteiro POSITIVO, por favor!")
                continue
            objeto = Eratostenes(limite_int)
            print(objeto.teste_primo())
        except ValueError as v:
            print(f"[ERROR] Digite um valor INTEIRO positivo, por favor!: {v}")
            continue


if __name__ == "__main__":
    print("[ALERT] Exemplo de uso:\nSe digita 100, ele gera os primos de 2 até 100.")
    rodar_programa()
