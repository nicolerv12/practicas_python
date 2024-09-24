
from abc import ABC, abstractmethod
class MetodoPago(ABC):
    @abstractmethod
    def procesar_pago(self, cantidad):
        pass

class Pago_Tarjeta_Credito(MetodoPago):
    def procesar_pago(self, cantidad):
        print(f"Procesando pago con tarjeta de crédito, cantidad: {cantidad}")
        
class Pago_Paypal(MetodoPago):
    def procesar_pago(self, cantidad):
        print(f"Procesando pago con PayPal, cantidad: {cantidad}")       
        
    class PagoCriptomoneda(MetodoPago):
    def procesar_pago(self, cantidad):
        print(f"Procesando pago con criptomoneda, cantidad: {cantidad}")      
        
def realizar_pago(metodo_pago, cantidad):
    metodo_pago.procesar_pago(cantidad)    
        
        
#main
pago1=Pago_Tarjeta_Credito()  
pago2=Pago_Paypal()
pago3=PagoCriptomoneda()

realizar_pago(pago1,100)
realizar_pago(pago2,500)
        