# GetNinjas Datascience Template - DJANGO based

Estrutura recomendada para projetos de datascience em Python, quando usando Django.

## Estrutura do projeto:

Este projeto usa Docker e tem a estrutura inspirada no PaaS Heroku. Se você não tem um ambiente Docker siga as instruções para seu sistema operacional disponíveis aqui: https://docs.docker.com/engine/installation/.

**TBD: Árvore de arquivos e comentar arquivos importantes**


## Testando via Docker

Você não precisa do ambiente de desenvolvimento para rodar os testes. Com o Docker funcionando, pode rodar os testes via ``docker-compose``:

```
$ docker-compose build test
$ docker-compose run --rm test
```


## Instalação do ambiente de desenvolvimento

Este é um projeto escrito para em Django, para Python 3 e com estrutura fortemente influenciada por [12-Factor App](https://12factor.net/pt_br/) e ~~com coisas que o Rails faz direito e o Django não~~ partes do Rails.

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
$ django-admin migrate
$ django-admin runserver
```


## Testando localmente

Com um ambiente de desenvolvimento funcional, podemos rodar os testes localmente desde que o virtualenv esteja ativado e as dependências instaladas:

```
$ workon meuprojeto
$ pip install -r requirements-test.txt
$ ./runtests.sh
```

Isso também criará um relatório de cobertura em ``.coverage_html/index.html``
