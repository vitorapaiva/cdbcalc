# Calculadora CDB
Serviço para calcular o valor de um CDB pós fixado indexado ao CDI em uma data específica e uma página web em que esses dados calculados serão expostos.

Para instalar os requisitos basicos
pip install -r requirements.txt

Para configurar as variaveis de ambiente, crie um cdbcalc/.env encima de cdbcalc/.env.example e faça os ajustes necessários

Para executar os testes:
python manage.py test calc.tests
python manage.py test importcdi.tests
