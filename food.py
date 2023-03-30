'''
Modulo para calcular los macronutrientes basado en las calorias a comer
'''

PROTEINAS_POR_KG = 1.6
CALORIAS_POR_PROTEINA = 4

CALORIAS_POR_GRASA = 9

CALORIAS_POR_CARBOHIDRATOS = 4


def calcular_macronutrientes(peso_actual, calorias_a_comer, porcentaje_grasa_a_comer=0.25):
    '''Funcion que calcula los macronutrientes a comer, basado en el peso actual, grasa y calorias
    a comer

    :param peso_actual: Es el peso actual de la persona en Kg
    :type peso_actual: float

    :param porcentaje_grasa_a_comer: Es la proporcion de grasas que quiere comer la persona de
    sus calorias totales
    :type porcentaje_grasa_a_comer: float

    :param calorias_a_comer: Son las calorias que va a comer el usuario. Debe estar en kcal
    :type calorias_a_comer: int o float
    '''

    grs_proteinas = (peso_actual * PROTEINAS_POR_KG)
    kcal_proteinas = grs_proteinas * CALORIAS_POR_PROTEINA

    kcal_grasas = calorias_a_comer * porcentaje_grasa_a_comer
    grs_grasas = kcal_grasas / CALORIAS_POR_GRASA

    kcal_carbohidratos = (calorias_a_comer - (kcal_proteinas + kcal_grasas))

    grs_carbohidratos = kcal_carbohidratos / CALORIAS_POR_CARBOHIDRATOS

    grs_proteinas = round(grs_proteinas, 0)
    grs_grasas = round(grs_grasas, 0)
    grs_carbohidratos = round(grs_carbohidratos, 0)

    return grs_proteinas, grs_grasas, grs_carbohidratos


if __name__ == '__main__':
    print(calcular_macronutrientes(74.7, 2150, 0.25))
