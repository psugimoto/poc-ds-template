# GetNinjas Datascience Template - DJANGO based

Estrutura recomendada para projetos de datascience em Python, quando usando Django.

## Instalação no Heroku PaaS:

Este projeto usa Docker quando no Heroku. Se você não tem um ambiente Docker siga as instruções para seu sistema operacional disponíveis aqui: https://docs.docker.com/engine/installation/.


```
$ heroku run -- django-admin migrate --noinput
```
Um mapa de São Paulo deve aparecer no centro da página. Hora de coletar Tweets! Vamos coletar 1000 tweets e guarda-los na base de dados:

* Obs: Este ``-v2`` é a verbosidade dos logs. Retire para nenhum log ou aumente para ver mais

```
$ heroku run -- django-admin tweets_fetch --stop-count 1000 -v2
```

Ao fim, atualize a página em seu browser. Já deve existir um belo heatmap te esperando.


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
$ pip install -r requirements.txt
$ ./runtests.sh
```

Isso também criará um relatório de cobertura em ``.coverage_html/index.html``
