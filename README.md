# Removedor de Metadados

Um projeto buscando aprender mais sobre manipulação de imagens e sobre metadados. Este projeto possui scripts para verificar todos os metadados e exibi-los, removê-los, e fornecer a localização em formato DMS.

## Descrição

Este projeto tem como objetivo fornecer ferramentas para manipulação de metadados de imagens. Ele permite:

- Verificar metadados de imagens.
- Remover metadados de imagens.
- Obter a localização das imagens em formato DMS (Degrees, Minutes, Seconds).

## Requisitos

- Python 3.10 (PyPy 3.10 recomendado)
- PIL (Pillow)
- piexif
- tkinter

## Instalação

1. Clone o repositório:

    ```sh
    git clone https://github.com/seuusuario/removedor-de-metadados.git
    cd removedor-de-metadados
    ```

2. Crie um ambiente virtual (opcional, mas recomendado):

    ```sh
    python -m venv venv
    source venv/bin/activate  # No Windows: venv\Scripts\activate
    ```

3. Instale as dependências:

    ```sh
    pip install Pillow piexif
    ```

## Uso

Execute o script principal:

```sh
python main.py
```

O script irá solicitar que você escolha uma das seguintes opções:

- `1`: Verificar metadados.
- `2`: Remover metadados.
- `3`: Obter a localização das imagens em formato DMS.

### Exemplo de Uso

```python
import subprocess

def main():
    match_case = int(input("Write 1 to verify, 2 to remove the exif data and 3 to get location: "))

    match match_case:
        case 1:
            print("Verifying!")
            subprocess.run(["python", "scripts/verificador_metadados.py"])
        case 2:
            print("Removing!")
            subprocess.run(["python", "scripts/removedor_metadados.py"])
        case 3:
            print("Locating!")
            subprocess.run(["python", "scripts/localizador.py"])
        case _:
            print("Invalid option!")

if __name__ == '__main__':
    main()
```

## Estrutura do Projeto

```
removedor-de-metadados/
├── main.py
├── scripts/
│   └── verificador_metadados.py
│   └── removedor_metadados.py
│   └── localizador.py
│   └── get_image.py
│   └── save_image.py
└── README.md
```

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

---

Você gostaria de adicionar ou modificar alguma parte dessa documentação?