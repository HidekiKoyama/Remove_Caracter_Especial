class Dados:
    def __init__(self, dados) -> None:
        self.__dados = dados
        self.__letras_especiais_dict = {
            'á': 'a', 'à': 'a', 'ã': 'a', 'â': 'a', 'ä': 'a',
            'é': 'e', 'è': 'e', 'ê': 'e', 'ë': 'e',
            'í': 'i', 'ì': 'i', 'î': 'i', 'ï': 'i',
            'ó': 'o', 'ò': 'o', 'õ': 'o', 'ô': 'o', 'ö': 'o', 'ø': 'o',
            'ú': 'u', 'ù': 'u', 'û': 'u', 'ü': 'u',
            'ñ': 'n',
            'ç': 'c',
            'ß': 's',
            'æ': 'ae',
            'œ': 'oe',
            'ø': 'o'
        }
        self.__caracteres_especiais = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '{', '}', '[', ']', '|', '\\', ':', ';', '<', '>', ',', '.', '?', '/', '~', '`', "'", '"']
    
    def removeCaracterEspecial(self) -> None:
        for ce in self.__caracteres_especiais:
            self.__dados = self.__dados.replace(ce, "")
        
    def removeLetraEspecial(self)  -> None:
        for especial, letra in self.__letras_especiais_dict.items():
            self.__dados = self.__dados.replace(especial, letra)
        
    def getDados(self) -> str:
        return self.__dados

if __name__ == "__main__":

    dados = Dados("Até amanhã, talvez eu vá para a praia!")
    print(dados.getDados())
    dados.removeLetraEspecial()
    print(dados.getDados())
    dados.removeCaracterEspecial()
    print(dados.getDados())
