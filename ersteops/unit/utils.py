''' Utils functions to Unit model '''

UNIT_TYPE_LIST = (
    ('terapia_intensiva' , 'Ambulancia de terapia intensiva'),
    ('urgencias_avanzadas' , 'Ambulancia de urgencias avanzadas'),
    ('urgencias_basicas' , 'Ambulancia de urgencias básicas'),
    ('vehiculo_consulta_medica_domicilio' , 'Vehiculo consulta medica a domicilio'),
)

UNIT_LIST_FIELD = [
    "id",
    "identifier",
    "unit_type",
    "is_active",
    "is_assigned",
    "is_alliance",
    "location",
    "operator",
    "phone",
    "description"
]