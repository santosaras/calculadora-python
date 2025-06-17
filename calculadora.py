def somar (a, b):
  return a + b
  
def subtrair (a,b):
  return a - b
  
if __name__ == "__main__":
  print("Calculadora Simples")
  print("Escolha a operação:")
  print("1 - Soma")
  print("2 - Subtração")
  operacao = int(input("Digite o número da operação desejada: "))
  
  x = int(input("Digite o primeiro número:"))
  y = int(input("Digite o segundo número:"))

  if operacao == 1:
    resultado = somar(x,y)
    print(f"Resultado da soma é: {resultado}")
  elif operacao == 2:
    resultado = subtrair(x,y)
    print(f"Resultado da subtração é: {resultado}")
  else:
    print("Operação inválida!")
