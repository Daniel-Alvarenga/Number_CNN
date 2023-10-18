# Number_CNN

Esse projeto é um sistema de reconhecimento de dígitos manuscritos utilizando uma Convolutional Neural Network (CNN). O sistema permite treinar um modelo CNN para reconhecer dígitos manuscritos de 0 a 9, armazenar o modelo treinado e testá-lo em novas entradas de dígitos desenhados no momento de execução.

<p align="center">
	<img src="https://github.com/Daniel-Alvarenga/Number_CNN/assets/128755697/8bf78f52-ba7e-4528-98cd-4ddbd0c6e245">
</p>

## Estrutura de Diretórios

```
Number_CNN/
├── data/
│   ├── n0/
│   │   ├── n0_1.png
│   │   ├── ...
│   │   └── n0_200.png
│   ├── ...
│   └── n9/
│       ├── n9_1.png
│       ├── ...
│       └── n9_200.png
├── models/
│   ├── modelo0.keras
│   ├── modelo1.keras
│   ├── modelo2.keras
├── src/
│   ├── main.py
│   ├── load.py
│   └── digits.py
├── test/
│   └── image.py
```

- `data/`: Contém imagens de 64 * 64 pixels dos dígitos manuscritos organizados em subpastas de 0 a 9.
- `models/`: O local onde o modelos CNNs treinados são salvos.
- `src/`: Contém os scripts Python para treinamento, carregamento de modelo e captura de novos dígitos manuscritos.
- `test/`: Usado para armazenar a imagem de dígito manuscrito para teste de rede.

## Scripts

### main.py

O script `main.py` é responsável pelo treinamento de um CNN, após o carregando das imagens de dígitos, adequação dos valores, e criando do modelo.

### load.py

O script `load.py` permite carregar um modelo previamente treinado e utilizá-lo para reconhecer dígitos em novas imagens desenhadas através da interface gerada com pygame.

### digits.py

O script `digits.py` permite desenhar dígitos na tela e salvá-los como imagens para fins de treinamento do modelo, ele foi inicialmente usado para a criação do dataset.

## Utilização

Para utilizar este projeto, siga os passos abaixo:

1. **Clone o Repositório:** Para começar, clone o repositório do projeto para o seu sistema local. Use o seguinte comando no terminal:
```bash    
git clone https://github.com/Daniel-Alvarenga/Number_CNN.git
```

    
2. **Navegue para a Pasta do Projeto:** Navegue para a pasta do projeto usando o comando `cd`. Por exemplo:
```bash
cd Number_CNN
 ```
    
3. **Crie um Ambiente Virtual (Opcional):** Recomenda-se criar um ambiente virtual para isolar as dependências deste projeto. Use `venv` (Python 3) ou `virtualenv`:
 ```bash
python -m venv venv
 ```

Ative o ambiente virtual:
    

 - No Windows:
```bash
venv\Scripts\activate
``` 
    
 - No macOS e Linux: 
```bash       
source venv/bin/activate
```

1. **Instale as Dependências:** Certifique-se de que as dependências necessárias estejam instaladas. Você pode usar o `requirements.txt` fornecido para instalar todas as dependências de uma vez:
 ```bash
 pip install -r requirements.txt
  ```
2. **Execute o `load.py`:** Após configurar o ambiente e instalar as dependências, você pode executar o `load.py` para carregar o modelo treinado e reconhecer dígitos em novas imagens. Use o seguinte comando: 
   ```bash   
    python src/load.py
    ```
3. **Selecione a tela** após o carregar da mesma e desenhe um dígito de 0 a 9 e tecle 's', a previsão irá ser exibida no terminal.
