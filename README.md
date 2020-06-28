# Calculadora CDB
Serviço para calcular o valor de um CDB pós fixado indexado ao CDI em uma data específica e uma página web em que esses dados calculados serão expostos.

Para instalar os requisitos basicos
pip install -r requirements.txt

Para configurar o banco de dados
python manage.py migrate

Para configurar as variaveis de ambiente, crie um cdbcalc/.env encima de cdbcalc/.env.example e faça os ajustes necessários
As variaveis de ambiente utilizadas são:
DEBUG=false
SECRET_KEY=sua-chave-secreta
DATABASE_URL=sgdb://login:senha@host:porta/dbnome

Para gerar uma SECRET_KEY para sua aplicação, utilize o comando abaixo

python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'

Para executar os testes:
python manage.py test calc.tests
python manage.py test importcdi.tests
