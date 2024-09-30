def contar_as(string):


  string_minusc = string.lower()

  contagem = string_minusc.count('a')
  return contagem


string = input("Digite uma string: ")


resultado = contar_as(string)
print("A letra 'a' aparece", resultado, "vezes na string.")