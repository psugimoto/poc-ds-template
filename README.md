# GetNinjas Datascience Template - FLASK based

Estrutura recomendada para projetos de datascience em Python, quando usando Flask. Há uma versão para Django também, no branch **``django``**.

## Estrutura do projeto:

Este projeto usa Docker e tem a estrutura inspirada no PaaS Heroku. Se você não tem um ambiente Docker siga as instruções para seu sistema operacional disponíveis aqui: https://docs.docker.com/engine/installation/.

**TBD: Árvore de arquivos e comentar arquivos importantes**


## Rodando e testando via Docker

Você não precisa do ambiente de desenvolvimento para rodar o projeto ou seus testes. Para rodar o projeto em Docker, o Dockerfile incluído inicia por padrão o entrypoint ``web`` descrito no Procfile. Há também um ``docker-compose.yml`` com os "alvos" ``web``, ``test`` e ``shell``

```
$ docker-compose build web test shell
$ docker-compose run --rm web     # Por padrão, na porta 8080
$ docker-compose run --rm test    # Instala dependências de teste, testa e sai.
$ docker-compose run --rm shell   # Shell Linux com a porta 8080 mapeada
```

## Instalação do ambiente de desenvolvimento

Este é um projeto escrito com Flask, para Python 3, mantendo compatibilidade com Python 2 se possível.

Ele também utiliza módulos em C que necessitam de dependências do sistema operacional. Se estiver no Ubuntu, instale estes pacotes aqui:

```
sudo apt-get install libffi-dev libpq-dev python-dev python-virtualenv python-pip virtualenvwrapper libpcre3 libpcre3-dev
```

Como boa prática, não instale os pacotes Python do sistema de sua máquina. Utilize um [virtualenv](https://virtualenv.pypa.io/en/stable/installation/). Para facilitar, instale também o [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/#introduction). Com isso pronto, vamos criar um ambiente Python separado do sistema e instalar as dependências do projeto nele:

```
$ mkvirtualenv -p `which python3` meuprojeto
$ workon meuprojeto
$ add2virtualenv .
$ pip install -r requirements.txt
```

Ative algumas variáveis de ambiente necessárias, configure a base de dados local, rode o projeto e abra o browser na página ``http://localhost:8000``:

```
$ export $(cat .env)
$ PORT=8000 ./runserver.sh
```


## Testando localmente

Com um ambiente de desenvolvimento funcional, podemos rodar os testes localmente desde que o virtualenv esteja ativado e as dependências instaladas:

```
$ workon meuprojeto
$ ./runtests.sh
```

Isso também criará um relatório de cobertura em ``.coverage_html/index.html``
