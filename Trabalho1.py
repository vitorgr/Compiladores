Operador = 0
Operando = 1
maior = None;
menor = None;
def prec(x,y):
    if x == '*' and y == '*' or x == '*' and y == '+' or x == '*' and y == '.':
        return maior
    elif x == '+' and y == '+' or x == '+' and y == '.':
        return maior
    elif x == '.' and y == '.':
        return maior
    else:
        return menor   
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


def ehop(simb):
    if simb == '(' or simb == ')' or simb == '*' or simb == '.' or simb == '+':
        return Operador
    else:
        return Operando


expressao=input('Entre com a expressão\n')

posfixa = ""
pilha = Stack()
for x in range(0,len(expressao)):
    if ehop(expressao[x]) == 1:
        posfixa += expressao[x]
    else:
        if expressao[x] == '(':
            pilha.push(expressao[x])
        elif expressao[x] == ')':
            while (pilha.top() != '(') :
                posfixa += pilha.pop()
            pilha.pop()
        else:
            while prec(expressao[x],pilha.top()) == "maior":
                posfixa += pilha.pop()
            pilha.push(expressao[x])        
while pilha.size() > 0 :
    posfixa += pilha.pop()



    
print('posfixa: ', posfixa)
print('pilha: ',pilha.size())















