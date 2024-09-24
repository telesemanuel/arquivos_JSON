# importa a biblioteca
import json

# classe ArquivoJson
class Manipulador:
    def criar_arquivo(self, nome_arquivo):
        try:
            usuarios = [
                {
                    'codigo': 0,
                    'nome': 'Admin',
                    'cpf':'000.000.00-00',
                    'email': 'admin@admin.com',
                    'profissao': 'Administrador'
                }
            ]
            
            # serializando objeto python com json
            json_dados = json.dumps(usuarios)
            with open(f'{nome_arquivo}.json','w', encoding='utf-8') as f:
              f.write(json_dados)
            return f'{nome_arquivo}.json criado com sucesso'
                
        except Exception as e:
            return f'Não foi possível criar o arquivo. {e}'
    
    def abrir_arquivo(self, nome_arquivo):
        # desserializarndo objeto json em python
        with open(f'{nome_arquivo}.json', 'r', encoding='utf-8') as f:
            dados = json.load(f)
        return dados
    
    def salvar_dados(self, usuarios, nome_arquivo):
        try:
            with open(f"{nome_arquivo}.json", "w", encoding="utf-8") as f:
                json.dump(usuarios, f)
            return f"Dados gravados com sucesso."
        except Exception as e:
            return f"Não foi possível salvar os dados. {e}."
    
    # destrutor
    def __del__(self):
        return f'Manipulador destruído'
    
    