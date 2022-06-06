# Pré-Requisitos para Execução
## Instalação do Python<br />
Para utilizar a aplicação é necessário que seu ambiente de execução tenha o python instalado. <br />
Para baixar o Python refira-se ao site oficial e siga os passos de instalação. https://www.python.org/downloads/ <br/>
## Instalação das Bibliotecas <br />
Após a instalação do python é necessário instalar as bibliotecas usadas na aplicação. Para isso utilize os seguinte comandos no terminal de sua preferência. <br />
*pip install opencv* <br/>
*pip install numpy* <br/>
*pip install tensorflow* <br/>

# Base de Dados
Certifique-se que os arquivos haarcascade_frontalface_default.xml, model.json e model_weights.h5 estejam no mesmo diretório que o arquivo main.py .

# Execução
Para executar o código insira o seguinte comando no terminal: python main.py <br/>
A aplicação irá exibir uma janela com as imagens capturadas em tempo real a partir de sua camêra e irá realizar a identificação das expressões sendo exibidas.
Para sair da aplicação aperte a tecla q. No final é exibido a expressão predominante capturada.
