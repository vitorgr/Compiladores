Operador = 0
Operando = 1
NULL = None
 
class Stack: #Constructor creates a list 
    def __init__(self):     
        self.stack = list()
         #Adding elements to stack 
    def push(self,data): #Checking to avoid duplicate entries 
            self.stack.append(data) 
            return True  
    def pop(self): 
        if len(self.stack)<=0: 
            return "" 
        return self.stack.pop() #Getting the size of the stack 
    def size(self): 
        return len(self.stack) 
    def top(self):
        top=self.pop()
        self.push(top)
        return top
        
def prec(x,y):
    if x == '*' and y == '*' or x == '*' and y == '+' or x == '*' and y == '.' :
        return ("maior")
    elif x == '+' and y == '+' or x == '+' and y == '.':
        return ("maior")
    elif x == '.' and y == '.':
        return ("maior")
    elif x == '(' and y == '.' or x == '(' and y == '+' or x == '(' and y == '*' or x == '(' and y == ')':
        return ("maior")
    elif x == ')' and y == '.' or x == ')' and y == '+' or x == ')' and y == '*' or x == ')' and y == '(':
        return ("maior")
    else:
        return ("menor")  

def ehop(simb):
    if simb == '(' or simb == ')' or simb == '*' or simb == '.' or simb == '+':
        return Operador    
    else:
        return Operando

def imp(exp):
    aux =""
    x = 0
    if len(exp)>1:
        
        for x in range(0,len(exp)-1):
        #while (x < (len(exp)-1)) :
            if (exp[x] == '.' and ehop(exp[x+1]) == 1) or (exp[x] == '.' and exp[x+1] == '(') or (ehop(exp[x]) == 1 and exp[x+1] == '.') or (exp[x] == '*' and exp[x+1] == '.') or (exp[x] == '.' and exp[x+1] == '*') or (exp[x] == ')' and exp[x+1] == '.')  :
                return exp    
            if exp[x] == '*' and ehop(exp[x+1]) == 1: # *a
                aux += exp[x] + "." + exp[x+1]
                
            elif exp[x] == '*' and exp[x+1] == '(' : # *(
                aux += exp[x] + "." + exp[x+1]
                
            elif exp[x] == ')' and exp[x+1] == '(' : # )(
                aux += exp[x] + "." + exp[x+1]
                
            elif ehop(exp[x]) == 1 and ehop(exp[x+1]) == 1 : # aa
                aux += exp[x] + "." + exp[x+1]
                
            elif ehop(exp[x]) == 1 and exp[x+1] == '(' : # a(
                aux += exp[x] + "." + exp[x+1]
                
            elif exp[x] == ')' and ehop(exp[x+1]) == 1 : # )a
                aux += exp[x] + "." + exp[x+1]
                
             
            else:
                aux += exp[x]
        return aux
    else:
        return exp


expressao=input('Entre com a expressão\n')
aux = imp(expressao)
print('expressão: ', aux)
posfixa = ""
pilha = Stack()
"""for x in range(0,len(expressao)):
    if ehop(expressao[x]) == 1:
        posfixa += expressao[x]
    else:
        #print('pilha: ', pilha.top())
        if expressao[x] == '(':
            pilha.push(expressao[x])
        elif expressao[x] == ')':
            while (pilha.top() != '(') :
                print('pilha: ', pilha.top())
                posfixa += pilha.pop()
            
            pilha.pop()
        else:
            while expressao[x] == '*' and pilha.top() =='*' or expressao[x] == '+' and pilha.top() =='+' or expressao[x] == '.' and pilha.top() =='.' or expressao[x] == '+' and pilha.top() =='*' or expressao[x] == '.' and pilha.top() =='*' or expressao[x] == '+' and pilha.top() =='.':
               # print('pilha: ', pilha.top())
                posfixa += pilha.pop()
            pilha.push(expressao[x])
    
while pilha.size() != 0 :
    #print('pilha: ', pilha.top())
    posfixa += pilha.pop()
    
p2 =Stack()
for y in range(0, len(posfixa)):
    simbolo = posfixa[y]
    if ehop(simbolo) == 1:
        p2.push(simbolo)
    else:
        if p2.top() != NULL:
            op2 = p2.pop()
            if simbolo == '*':
                valor = "asdasd"
                p2.push(valor)
            else:
                if p2.top() != NULL:
                    op1 = p2.pop()
                    valor = "asdasdasd2"
                    p2.push(valor)
                else:
                    print("deu ruim")
        else:   
            print("deu ruim")            
op1 = p2.pop()
if p2.top() == NULL:
    print('Deu bom')
    
print('posfixa:final ', posfixa)
print('pilha:final ',pilha.size())
"""
