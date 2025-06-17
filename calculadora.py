def somar (numero_1, numero_2):
  return numero_1 + numero_2
  
def subtrair (numero_1,numero_2):
  return numero_1 - numero_2
  
if __name__ == "__main__":
  print("Calculadora Simples")
  print("Escolha a operação: ")
  print("1 - Soma")
  print("2 - Subtração")
  operacao = int(input("Digite o número da operação desejada: "))
  
  numero_1 = int(input("Digite o primeiro número: "))
  numero_2 = int(input("Digite o segundo número: "))

  if operacao == 1:
    resultado = somar(numero_1,numero_2)
    print(f"Resultado da soma é: {resultado}")
  elif operacao == 2:
    resultado = subtrair(numero_1,numero_2)
    print(f"Resultado da subtração é: {resultado}")
  else:
    print("Operação inválida!")
