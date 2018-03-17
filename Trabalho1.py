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
            return ("Stack Empty!") 
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
                posfixa[x] = pilha.pop()
            pilha.pop()
        else:
            while prec(expressao[x],pilha.top()) == "maior":
                posfixa += pilha.pop()
            pilha.push(expressao[x])        
while pilha.size() > 0 :
    posfixa += pilha.pop()



print('posfixa: ', posfixa)
print('pilha: ',pilha.size())















"""



class Stack: #Constructor creates a list 
    def __init__(self):     
        self.stack = list()
         #Adding elements to stack 
    def push(self,data): #Checking to avoid duplicate entries 
        if data not in self.stack: 
            self.stack.append(data) 
            return True 
        return False #Removing last element from the stack 
    def pop(self): 
        if len(self.stack)<=0: 
            return ("Stack Empty!") 
        return self.stack.pop() #Getting the size of the stack 
    def size(self): 
        return len(self.stack) 

myStack = Stack() 
print(myStack.push(5)) #prints True 
print(myStack.push(6)) #prints True 
print(myStack.push(9)) #prints True 
print(myStack.push(5)) #prints False since 5 is there 
print(myStack.push(3)) #prints True 
print(myStack.size()) #prints 4 
print(myStack.pop()) #prints 3 
print(myStack.pop()) #prints 9 
print(myStack.pop()) #prints 6 
print(myStack.pop()) #prints 5 
print(myStack.size()) #prints 0 
print(myStack.pop()) #prints Stack Empty!

#NOTE: We are not worried about the size of the stack since it is represented by a list which can dynamically change its size.



        


"""