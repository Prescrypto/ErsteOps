# -*- coding: utf-8 -*-
''' Utils functions to Unit model '''

UNIT_TYPE_LIST = (
    ('undefined', 'Indefinido'),
    ('terapia_intensiva' , 'Ambulancia de terapia intensiva económico'),
    ('urgencias_avanzadas' , 'Ambulancia de urgencias avanzadas económico'),
    ('urgencias_basicas' , 'Ambulancia de urgencias básicas económico'),
    ('vehiculo_consulta_medica_domicilio' , 'Vehículos de consulta médica a domicilio, Económico'),
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
