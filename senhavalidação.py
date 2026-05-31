# No Python o "None" serve para ausência de valor, um valor nulo ou um estado padrão
# No Python declaramos variáveis apenas com um nome, que fica do seu gosto
senha = None
# Começa com zero tentativas
tentativas = 0
# Aqui defini o limite
maxtentativas = 3
# Aqui criamos uma variável, com o valor da senha correta, para não ficar repetindo ela no código, aí quando precisamos dela, chamamos apenas a variável "senha_correta"
# Aqui definimos a senha com string, pois o teclado reconhece apenas letras, assim ele vai a comparação, de quando o usuário digita letra ou números.
senha_correta = '12345'

# No Python o while não usa () e {}, apenas DOIS PONTOS = :
# Em While a lógica diz, "se senha for diferente de senha_correta e o número de tentativas for menor que o maxtentativas" esse código será executado.
while senha != senha_correta and tentativas < maxtentativas:
	# No Python os valores que vão ficar dentro do while, sempre fica "mais para dentro" do código.
    senha = input("Digite sua senha: ")
    # Verifica se o usuário digitou letras ou qualquer outro coisa que não seja um número.
    # o if not = Se não for, se a senha não for número, essa código será executado.
    if not senha.isdigit():
    # Se ele digitou letras, essa mensagem irá aparecer para ele.
        print("Alerta: A senha precisa conter apenas números!")
    # Se ele digitar números, o sistema vai para outra etapa, que é validar a senha.
        continue
    # Aqui é o incremento das tentativas, quando o usuário digita na senha números e estiver errado, o Python vai somar mais uma tentativa, ou seja as tentativas começam em 0, então 0+1=1
    tentativas += 1
    # Aqui se a senha número for diferente, da "senha_correta", ele vai exibir a mensagem em "print" e acrescentar mais uma tentativa, assim retornando o loop, lá para "senha = input"
    if senha != senha_correta:
        print("Senha Incorreta!")
# Bem já é alto explicativo, se a senha for igual a definida em "senha_correta" o acesso é liberado.
if senha == senha_correta:
    print("Acesso permitido!")
# Se o usuário alcansar o limite de tentativas, definido em "maxtentativas" o seu acesso será bloqueado.
else:
    print("Acesso bloqueado! Você excedeu as tentativas")