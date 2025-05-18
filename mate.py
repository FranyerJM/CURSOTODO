def suma(a, b): #int:
    resultado = a + b
    return resultado

def multiplicar(a, b): #int:
    return a * b 

def diametro(radio):
    return radio * 2 

def perimetro(radio):
    return diametro(radio) * 3.1415926
 
def cuadrado(a):
    return a ** 2 

def raiz_cuadrada(numero):
    return numero ** (1/2) 
    
def raiz(numero, indice):
    return numero ** (1/indice)        

def hipotenusa_manual(a, b):
    return ((a ** 2) + (b ** 2)) ** (1/2) 

def hipotenusa(a, b):
    """Calcula la hipotenusa de un triángulo rectángulo dados los catetos a y b.
    Parameters:
        a (float): Cateto a.
        b (float): Cateto b.
    """
    return raiz((suma((cuadrado(a)), (cuadrado(b)))),2)