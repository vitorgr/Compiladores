Operador = 0
Operando = 1
def ehop(simb):
    if simb == '(' or simb == ')' or simb == '*' or simb == '.' or simb == '+':
        return Operador
    else:
        return Operando


expressao=input('Entre com a expressão\n')
posfixa = ""
for x in range(0,len(expressao)):
    if ehop(expressao[x]) == 1:
        posfixa += expressao[x]

print('posfixa: ', posfixa)

        