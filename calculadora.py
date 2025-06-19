def somar (numero_1, numero_2):
  return numero_1 + numero_2
  
def subtrair (numero_1,numero_2):
  return numero_1 - numero_2

def menu():
  while True:
      print("\nEscolha uma opção:")
      print("1. Somar")
      print("2. Subtrair")
      print("3. Sair")
      opcao = int(input("Digite o número da opção: "))

      if opcao == 1:
          numero_1 = int(input("Digite o primeiro número: "))
          numero_2 = int(input("Digite o segundo número: "))
          print(f"Resultado da soma é: {somar(numero_1, numero_2)}")
      elif opcao== 2:
          numero_1 = int(input("Digite o primeiro número: "))
          numero_2 = int(input("Digite o segundo número: "))
          print(f"Resultado da soma é: {subtrair(numero_1, numero_2)}")
      elif opcao == 3:  
          print("Saindo do programa.")
          break
      else:
          print("Operação inválida!")

if __name__ == "__main__":
   menu()
