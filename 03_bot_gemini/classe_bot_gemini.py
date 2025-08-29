import google.generativeai as genai

class Boot_gemini:
    """Cria um robo especialista em fazer brownie"""

    def __init__(self):
       genai.configure(api_ky="AIzaSyAwxjTXssSQ9gLXB-Q9QlATJYTk78bpE0g") 
    
    

     

    def enviar_mensagem(self, mensagem: str) -> str:
        """Envia mensagem para o modelo e retorna a resposta."""
        response = self.chat.send_message(mensagem)
        return response.text


    def responder (self,pergunta:str) -> str:
        """Funçao para responder as perguntas enviadas como parametro"""

        response = self.chat.send_message(pergunta)
        return response.text