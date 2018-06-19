# reglas de variables
# 1. El primer caracter es una letra o el underscore (_)
# 2. Pueden contener letras, numeros y underscore (_) despues
#   del primer caracter
# 3. No pueden contener signos de caracteres especiales como # , ' " $ % - + * & @ ( ) = ! ~ ` ; : < > , . / ? etc. Solo letras, numeros y underscore

# variables validas son
my_var
_my_var
myvar

LaVariable
Caro123
victor_123


# variables invalidas incluyen
$victor
@#$
!!

# Adicional, variables no pueden ser palabras reservadas por Python,
# como los siguientes
and
not
or
if
else
while
for
def
class
import
from
in
type
# etc