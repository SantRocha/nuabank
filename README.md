# NUAbank

NUAbank é um banco fictício desenvolvido como parte da disciplina TESI I (Tópicos Especiais em Sistemas de Informação I), com o objetivo de avaliar o domínio dos conceitos de Programação Orientada a Objetos (OOP) e a utilização da biblioteca Tkinter para criação de interfaces gráficas em Python. O nome do projeto é uma paródia do Nubank, uma das principais fintechs do Brasil.
O sistema não utiliza banco de dados, sendo uma aplicação simples focada em gerenciamento de clientes e operações bancárias básicas, como abertura e fechamento de contas, saques e depósitos.

## Funcionalidades
- **Gerenciamento de clientes:** Cadastro e manutenção de informações dos clientes do banco.
- **Abertura e fechamento de contas:** O cliente pode abrir e fechar suas contas bancárias diretamente pelo sistema.
- **Operações bancárias:** Realização de depósitos e saques nas contas dos clientes.
- **Interface gráfica:** A aplicação possui uma interface gráfica desenvolvida com Tkinter, proporcionando uma experiência interativa e amigável ao usuário.

## Tecnologias Utilizadas
- **Python:** Linguagem de programação utilizada para desenvolver o sistema.
- **Tkinter:** Biblioteca gráfica para a criação da interface do usuário.
- **OOP (Programação Orientada a Objetos):** O sistema foi desenvolvido utilizando conceitos de orientação a objetos, com classes e objetos para representar os diferentes componentes do banco (clientes, contas, etc.).

## Estrutura do Projeto
O código está estruturado em módulos que implementam as diferentes funcionalidades do banco. As principais partes do sistema incluem:

1. Classes de Clientes e Contas: Representam os dados e as operações associadas aos clientes e suas respectivas contas bancárias.
2. Interface Gráfica (GUI): Desenvolvida com Tkinter, possibilita a interação do usuário com o sistema, realizando operações como depósitos e saques.
3. Lógica de Negócio: Implementa a validação das operações bancárias e a execução de ações como abertura e fechamento de contas.

## Objetivo do Projeto
O objetivo principal do projeto foi avaliar os conceitos de Programação Orientada a Objetos (OOP) e o uso do Tkinter pelos alunos da graduação. O foco era criar um sistema simples e funcional, sem a necessidade de banco de dados, onde as operações são realizadas apenas na memória, utilizando listas ou dicionários para armazenar as informações temporariamente.

## Como Executar o Projeto
### Pré-requisitos
- **Python** versão 3.x ou superior.
- Biblioteca **Tkinter* (geralmente já incluída com o Python).

### Instruções
1. Clone o repositório para o seu computador:

   ```bash
    git clone https://github.com/SantRocha/nuabank
2. Navegue até o diretório do projeto:

   ```bash
   cd NUAbank
3. Execute o script principal do projeto:

   ```bash
   python main.py
4. A interface gráfica será aberta, permitindo que você interaja com o sistema e realize operações bancárias.
5. A Senha Para acessar o programa é **123**.

## Limitações
- O sistema não utiliza banco de dados, o que significa que os dados são perdidos quando o programa é fechado.
- A aplicação é um protótipo simples, sem implementação de recursos avançados como autenticação de usuário ou controle de saldo negativo.
- O sistema não é preparado para uso em ambientes de produção, sendo apenas uma implementação acadêmica para fins de aprendizado.
