#Anotação
#The error “TypeError: 'module' object is not callable” occurs when the python compiler gets confused between function
#name and module name and try to run a module name as a function.
import re
from collections import Counter

def Verificar_Digitos(valor):
    '''
    Recebe uma string e verifica se ela contem apenas numeros;
    Retorna verdadeiro caso apenas exista numeros e falso caso exista pelo menos uma letra;
    '''
    return bool(re.match("^[0-9.]*$", valor))

def Verificar_Espaco(valor):
    '''
    Recebe uma string e verifica se ela não contem espaços em branco;
    Retorna verdadeiro caso não exista nenhum espaço em branco e falso caso exista pelo menos um;
    '''
    string = valor
    for i in string:
        if (i.isspace()):
            return False
    return   True

def Verificar_Caractes_Especiais(valor):
    '''
    Recebe uma string e verifica se ela contem caracteres especiais;
    Retorna verdadeiro caso não exista nenhum caractere especial;
    '''
    return(bool(re.match("^[A-Za-z0-9.,]*$", valor)))

def Verifica_Apenas_Um_Ponto(valor):
    '''
    Recebe uma string e verifica se ela contem mais de um ponto {.}
    Retorna Falso se encontrar mais de dois pontos verdadeiro em caso contrario
    '''
    res = Counter(valor)
    contador_De_Dots = res['.']
    if(contador_De_Dots > 1):
        return  False
    else:
        return True