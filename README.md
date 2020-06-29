# Calculadora CDB
Serviço para calcular o valor de um CDB pós fixado indexado ao CDI em uma data específica e uma página web em que esses dados calculados serão expostos.

## Para instalar os requisitos basicos
* pip install -r requirements.txt

## Para criar as tabelas do banco de dados
* python manage.py migrate

## Para configurar as variaveis de ambiente
* Crie um cdbcalc/.env encima de cdbcalc/.env.example
* Faça os ajustes necessários

### As variaveis de ambiente utilizadas são:
* DEBUG=false
* SECRET_KEY=sua-chave-secreta
* DATABASE_URL=sgdb://login:senha@host:porta/dbnome

### Para gerar uma SECRET_KEY para sua aplicação, utilize o comando abaixo
* python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'

## Para executar os testes:
### Testes de importação de base CDI
* python manage.py test importcdi.tests
### Testes de calculo de CDB
* python manage.py test calc.tests

## Documentações da API no Postman:
* Collection: https://www.getpostman.com/collections/bb1847988fc473d5c8ba
* Web: https://web.postman.co/collections/1874212-dea34fab-aa6b-4377-8a72-e0a14ca6b68b

# Veja em funcionamento no Heroku
https://calc-cdb.herokuapp.com/

#Futuras Melhorias
* Criação de Docker
* Ajustes no template
* Criação de front end para a importação