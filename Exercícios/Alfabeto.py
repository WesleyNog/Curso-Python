lista2 = 'α β γ δ ε δ η θ ι k λ μ ν ξ ο π ρ σ τ υ φ χ ψ ω'
alfabeto_grego = lista2.split(' ')

lista1 = 'a b c d e f g h i j l m n o p q r s t u v x w y'
alfabeto_portugues = lista1.split(' ')

# alfabeto = [
# ['a','α'],['b','β'],['c','γ'],['d','δ'],['e','ε'],['f','δ'],
# ['g','η'],['h','θ'],['i','ι'],['j','k'],['l','λ'],['m','μ'],
# ['n','ν'],['o','ξ'],['p','ο'],['q','π'],['r','ρ'],['s','σ'],
# ['t','τ'],['u','υ'],['v','φ'],['x','χ'],['w','ω'],['y','ψ']]

# com metodo
def traduzir(texto)
  traduzido = ''
  for letra in texto
    indice = alfabeto_portugues.index(letra)
    if indice
      traduzido += alfabeto_grego[indice]
    else
      traduzido += letra
  traduzido  

# ---
def traduzir(texto)
  traduzido = ''
  for letra in texto
    indice = 0
    for letra_pt in alfabeto_portugues
      if letra == letra_pt
        traduzido += alfabeto_grego[indice]
        break
      indice += 1

alfabeto_traduzido = traduzir('wesley')
# fim com metodo

# sem metodo
texto = 'wesley
traduzido = ''
for letra in texto
  indice = alfabeto_portugues.index(letra)
  if indice
    traduzido += alfabeto_grego[indice]
  else
    traduzido += letra

alfabeto_traduzido = traduzido  
# sem metodo
