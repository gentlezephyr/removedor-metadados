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
    git clone https://github.com/gentlezephyr/removedor-metadados.git
    cd removedor-metadados
    ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
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

## Estrutura do Projeto

```
removedor-de-metadados/
├── main.py
├── scripts/
│   └── verificador_metadados.py
│   └── removedor_metadados.py
│   └── localizador.py
│   └── utils.py
└── README.md
```

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.
