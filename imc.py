def imc(peso, altura):
  altura_quadrada = altura ** 2
  meu_imc = peso/altura_quadrada
  return meu_imc

meu_imc = imc(115, 1.82)
print(f'Seu índice de massa corporal é {meu_imc:.2f}'.format(imc))  


  