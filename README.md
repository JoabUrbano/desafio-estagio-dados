# Desafio em Análise de Dados da SeuBoné!

Links importantes:
- [Informações sobre layout de dados](https://www.gov.br/produtividade-e-comercio-exterior/pt-br/assuntos/comercio-exterior/estatisticas/base-de-dados-bruta
)
  - OBS: Utilizar "Base de dados detalhada por NCM"

**Quais os quesitos de avaliação?** <br>

- Clareza da implementação e boas práticas de código;
- Documentação;
- Solução apresentada.

<h1 id="usage" > 💻 Descrição </h1>

Projeto feito em python para o desafio de análise de dados da SeuBoné.

O desafio é dividido em duas partes:

1. Carregamento e armazenamento dos dados
2. Construção de visualizações a partir dos dados carregados.

- Utilizando a ferramenta de sua preferência crie um dashboard capaz de mostrar as seguintes informações:
  - Qual os top 3 produtos mais exportados por estado nos anos de 2020 e 2021;
  - Qual os top 3 produtos mais importados por estado nos anos de 2020 e 2021;
  - Quais os top 3 produtos exportados em cada mês de 2021 por estado;

<h1 id="usage" > 📚 Bibliotecas </h1>
- Numpy<br>
- Pandas<br>
- PyMySQL<br>
- python-dotenv<br>
- Tkinter<br>

<h2>👨‍💻 Como rodar o projeto</h2>

1. É necessario ter o <a href="https://www.python.org/">python 3</a> instalado e o pip.

2. Com o pip instalado é necessario instalar as bibliotecas.
```sh
    pip install numpy
```
```sh
    pip install pandas
```
```sh
    pip install PyMySQL
```
```sh
    pip install python-dotenv
```

3. Crie um arquivo ```.env``` na raiz do projeto e defina as variaveis de ambiente no arquivo como está no ```.env.example```.

4. O arquivo ```gui.py```  é a interfacie gráfica do projeto, baasta executana na pasta raiz do projeco com:
```sh
    python gui.py
```
e poderá utilizar o programa.

5. Alternativamente, se quiser gerar um executavel basta rodar na raiz:
```sh
    pip install pyinstaller
    pyinstaller --onefile --windowed --add-data "assets/frame0;assets/frame0" gui.py
```
que irá gerar o executável dentro de uma pasta ```dist```. Basta arrastar o executavel para a raiz do projeto e pode apagar a pasta ```dist```, a ```build``` e o arquivo ```gui.spec```. Há também a possibilidade de criar um atalho do arquivo e movelo para onde você desejar.

<h3>Autor</h3>
<a href="https://github.com/JoabUrbano">Joab Urbano</a><br>
