import google.generativeai as genai

class Gemini_Bot:
    """Classe responsável por gerenciar o modelo do Gemini."""
    
    def __init__(self):
        genai.configure(api_key="AIzaSyDBoTTE06H5ADrvPqwDbqLH_piX3jt0NoQ")
        
        instrucao_sistema = """
            Você é um especialista em confeitaria, principalmemte em brownie com 15 anos de experiência.
            Seu nome é Dona Rosa. Você deve responder a todas as perguntas de forma 
            profissional, detalhada e focada exclusivamente no mundo em brwnie. 
            Se o usuário perguntar sobre outro assunto, gentilmente redirecione a conversa 
            de volta para brownie, afirmando que seu conhecimento é especializado.
            """
        
        self.model = genai.GenerativeModel(
            model_name='gemini-1.5-flash',
            system_instruction=instrucao_sistema
        )
        self.chat = self.model.start_chat()

    def enviar_mensagem(self, mensagem: str) -> str:
        """Envia mensagem para o modelo e retorna a resposta."""
        response = self.chat.send_message(mensagem)
        return response.text
    

    #este is so sera execultado se eu rodar o arquivo diretamente 
    #caso eu importe essa parte não será execultada
    #podemos utilizar isso para testes 

if __name__ =="__main__":
    robo = Gemini_Bot()
    resposta = robo.enviar_mensagem("Qual é a flor mais cheirosa do mundo?")
    print(resposta)