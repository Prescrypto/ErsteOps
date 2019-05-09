/* eslint-disable import/prefer-default-export */
export const TREE_DATA = [
  {
    id: '1-1000000',
    label: '(Adulto) AHOGADOS POR INMERSION',
    children: [
      {
        id: '1-1100000',
        label: ' No esta consciente [Grado : 1]',
      },
      {
        id: '1-1200000',
        label: ' Esta consciente',
        children: [
          {
            id: '1-1210000',
            label: ' Respira bien [Grado : 2]',
          },
          {
            id: '1-1220000',
            label: ' No Respira bien [Grado : 1]',
          },
        ],
      },
    ],
  },
  {
    id: '1-2000000',
    label: '(Adulto) ALTERACION DE LA AUDICION [Grado : 3]',
  },
  {
    id: '1-4000000',
    label: '(Adulto) ACCIDENTE VEHICULAR [Grado : 1]',
  },
  {
    id: '1-5000000',
    label: '(Adulto) ARRITMIAS [Nota : (REALIZAR ECG)]',
    children: [
      {
        id: '1-5100000',
        label: ' No esta consciente [Grado : 1]',
      },
      {
        id: '1-5200000',
        label: ' Esta consciente',
        children: [
          {
            id: '1-5210000',
            label: ' Tiene dolor de pecho [Grado : 1]',
          },
          {
            id: '1-5220000',
            label: ' No tiene dolor de pecho [Grado : 2]',
          },
        ],
      },
    ],
  },
  {
    id: '1-7000000',
    label: '(Adulto) CONSTIPACION [Grado : 3]',
  },
  {
    id: '1-8000000',
    label: '(Adulto) CONVULSIONES',
    children: [
      {
        id: '1-8100000',
        label: ' Esta convulsionando ahora [Grado : 1]',
      },
      {
        id: '1-8200000',
        label: ' No esta convulsionado ahora',
        children: [
          {
            id: '1-8210000',
            label: ' No está conciente [Grado : 1]',
          },
          {
            id: '1-8220000',
            label: ' Está conciente',
            children: [
              {
                id: '1-8221000',
                label: ' Respira Mal [Grado : 2]',
              },
              {
                id: '1-8222000',
                label: ' Respira bien [Grado : 3P]',
              },
            ],
          },
        ],
      },
    ],
  },
  {
    id: '1-9000000',
    label: '(Adulto) TRASTORNOS DE CONDUCTA',
    children: [
      {
        id: '1-9100000',
        label: ' Esta muy violento o agresivo [Grado : 2]',
      },
      {
        id: '1-9200000',
        label: ' No esta violento o agresivo',
        children: [
          {
            id: '1-9210000',
            label: ' Está alcoholizado o consumió drogas [Grado : 2]',
          },
          {
            id: '1-9220000',
            label: ' No está alcoholizado ni consumió drogas',
            children: [
              {
                id: '1-9221000',
                label: ' Tuvo trauma de cráneo [Grado : 2]',
              },
              {
                id: '1-9222000',
                label: ' No tuvo trama de cráneo [Grado : 3]',
              },
            ],
          },
        ],
      },
    ],
  },
  {
    id: '1-10000000',
    label: '(Adulto) CONFUSION-OBNUBILACION',
    children: [
      {
        id: '1-10100000',
        label: ' Respira Mal [Grado : 1]',
      },
      {
        id: '1-10200000',
        label: ' Respira Bien',
        children: [
          {
            id: '1-10210000',
            label: ' Está pálido o sudoroso [Grado : 2]',
          },
          {
            id: '1-10220000',
            label: ' No está pálido ni sudoroso',
            children: [
              {
                id: '1-10221000',
                label: ' Cuanto tiempo hace que está con este cuadro',
                children: [
                  {
                    id: '1-10221100',
                    label: ' Menos de seis horas [Grado : 2]',
                  },
                  {
                    id: '1-10221200',
                    label: ' Entre seis y doce horas [Grado : 3]',
                  },
                  {
                    id: '1-10221300',
                    label: ' Más de doce horas [Grado : 3]',
                  },
                ],
              },
              {
                id: '1-10222000',
                label: ' Se desconoce el tiempo de evolución [Grado : 3]',
              },
            ],
          },
        ],
      },
    ],
  },
  {
    id: '1-11000000',
    label: '(Adulto) CAIDA DE ALTURA [Grado : 1]',
  },
  {
    id: '1-14000000',
    label: '(Adulto) CEFALEA',
    children: [
      {
        id: '1-14100000',
        label: ' Habla con dificultad [Grado : 2]',
      },
      {
        id: '1-14200000',
        label: ' No Habla con dificultad',
        children: [
          {
            id: '1-14210000',
            label: ' Presenta vómitos [Grado : 3]',
          },
          {
            id: '1-14220000',
            label: ' No presenta vómitos [Grado : 3]',
          },
        ],
      },
    ],
  },
  {
    id: '1-15000000',
    label: '(Adulto) DIARREA [Grado : 3]',
  },
  {
    id: '1-16000000',
    label: '(Adulto) DEBILIDAD  DECAIMIENTO - PALIDEZ',
    children: [
      {
        id: '1-16100000',
        label: ' No está conciente [Grado : 1]',
      },
      {
        id: '1-16200000',
        label: ' Está conciente',
        children: [
          {
            id: '1-16210000',
            label: ' Respira mal [Grado : 2]',
          },
          {
            id: '1-16220000',
            label: ' Respira bien',
            children: [
              {
                id: '1-16221000',
                label: ' Hace menos de 60 minutos [Grado : 3]',
              },
              {
                id: '1-16222000',
                label: ' Hace más de 60 minutos',
              },
            ],
          },
        ],
      },
    ],
  },
  {
    id: '1-18000000',
    label: '(Adulto) DISNEA',
  },
  {
    id: '1-19000000',
    label: '(Adulto) DOLOR ABDOMINAL',
    children: [
      {
        id: '1-19100000',
        label: ' El dolor es en la parte superior del abdomen',
        children: [
          {
            id: '1-19110000',
            label: ' Tiene antecedentes de enfermedad cardíaca [Grado : 2]',
          },
          {
            id: '1-19120000',
            label: ' No tiene antecedentes de enfermedad cardíaca [Grado:3]',
          },
        ],
      },
      {
        id: '1-19200000',
        label: ' El dolor no es en la parte superior del abdomen',
        children: [
          {
            id: '1-19210000',
            label: ' Tiene vómitos o diarrea [Grado : 3]',
          },
          {
            id: '1-19220000',
            label: ' No tiene vómitos o diarrea [Grado : 3]',
          },
        ],
      },
    ],
  },
  {
    id: '1-20000000',
    label: '(Adulto) DOLOR DE TORAX [Nota : (REALIZAR ECG)]',
    children: [
      {
        id: '1-20100000',
        label: ' Respira mal',
        children: [
          {
            id: '1-20110000',
            label: ' No está sudoroso ni pálido [Grado : 3P]',
          },
          {
            id: '1-20120000',
            label: ' Está sudoroso o pálido [Grado : 1]',
          },
        ],
      },
      {
        id: '1-20200000',
        label: ' Respira bien',
        children: [
          {
            id: '1-20210000',
            label: ' Esta sudoroso o pálido [Grado : 1]',
          },
          {
            id: '1-20220000',
            label: ' No está sudoroso ni pálido',
            children: [
              {
                id: '1-20221000',
                label: ' Tiene antecedentes cardiacos [Grado : 3P]',
              },
              {
                id: '1-20222000',
                label: ' No tiene antecedentes cardiacos',
                children: [
                  {
                    id: '1-20222100',
                    label: ' Menos de 12 hs de evolución [Grado : 2]',
                    children: [
                      {
                        id: '1-20222210',
                        label: ' Tiene tos [Grado : 3]',
                      },
                      {
                        id: '1-20222220',
                        label: ' No tiene fiebre o tos [Grado : 3]',
                      },
                    ],
                  },
                  {
                    id: '1-20222200',
                    label: ' Más de 12 hs de evolución',
                    children: [
                      {
                        id: '1-20222210',
                        label: ' Tiene tos [Grado : 3]',
                      },
                      {
                        id: '1-20222220',
                        label: ' No tiene fiebre o tos [Grado : 3]',
                      },
                    ],
                  },
                ],
              },
            ],
          },
        ],
      },
    ],
  },
  {
    id: '1-21000000',
    label: '(Adulto) DISARTRIA (Dificultad para hablar)',
    children: [
      {
        id: '1-21100000',
        label: ' Comenzó hace menos de 6 horas o se desconoce [Grado : 2]',
      },
      {
        id: '1-21200000',
        label: ' Hace más de 6 horas que comenzó',
        children: [
          {
            id: '1-21210000',
            label: ' Tiene dificultad para movilizar un miembro [Grado : 2]',
          },
          {
            id: '1-21220000',
            label: ' No tiene dificultad para movilizar un miembro [Grado : 3]',
          },
        ],
      },
    ],
  },
  {
    id: '1-22000000',
    label: '(Adulto) TRANSTORNO EN LA MICCION',
    children: [
      {
        id: '1-22100000',
        label: ' Tiene sonda',
        children: [
          {
            id: '1-22110000',
            label: ' Está obstruida [Grado : 3P]',
          },
          {
            id: '1-22120000',
            label: ' No está obstruida',
            children: [
              {
                id: '1-22121000',
                label: ' Tiene dolor abdominal [Grado : 3]',
              },
              {
                id: '1-22122000',
                label: ' No tiene dolor abdominal',
                children: [
                  {
                    id: '1-22122100',
                    label: ' Tiene ardor uretral [Grado : 3]',
                  },
                  {
                    id: '1-22122200',
                    label: ' No tiene ardor uretral [Grado : 3]',
                  },
                ],
              },
            ],
          },
        ],
      },
      {
        id: '1-22200000',
        label: ' No tiene sonda',
        children: [
          {
            id: '1-22210000',
            label: ' Tiene dolor abdominal [Grado : 3]',
          },
          {
            id: '1-22220000',
            label: ' No tiene dolor abdominal',
          },
        ],
      },
    ],
  },
  {
    id: '1-23000000',
    label: '(Adulto) ERUPCION CUTANEA',
    children: [
      {
        id: '1-23100000',
        label: ' Antecedentes de edema de glotis [Grado : 2]',
      },
      {
        id: '1-23200000',
        label: ' Sin antecedentes de edema de glotis',
        children: [
          {
            id: '1-23210000',
            label: ' Tiene ronchas en la piel [Grado : 3]',
          },
          {
            id: '1-23220000',
            label: ' Sin ronchas pero otras lesiones [Grado : 3]',
          },
        ],
      },
    ],
  },
  {
    id: '1-24000000',
    label: '(Adulto) ELECTROCUCION',
    children: [
      {
        id: '1-24100000',
        label: ' No esta consciente [Grado : 1]',
      },
      {
        id: '1-24200000',
        label: ' Esta consciente',
        children: [
          {
            id: '1-24210000',
            label: ' Respira bien [Grado : 2]',
            children: [
              {
                id: '1-24212000',
                label: ' No Respira bien [Grado : 1]',
              },
            ],
          },
        ],
      },
    ],
  },
  {
    id: '1-25000000',
    label: '(Adulto) FIEBRE [Grado: 3]',
  },
  {
    id: '1-26000000',
    label: '(Adulto) GRIPE [Grado : 3]',
  },
  {
    id: '1-27000000',
    label:
      '(Adulto) HERIDA POR ARMA BLANCA O DE FUEGO [Nota : (EVALUAR APOYO POLICIAL)] [Grado : 1]',
  },
  {
    id: '1-28000000',
    label: '(Adulto) HEMORRAGIAS (EVIDENCIA DE SANGRADO)',
    children: [
      {
        id: '1-28100000',
        label: ' No está consciente [Grado : 1]',
      },
      {
        id: '1-28200000',
        label: ' Esta consciente',
        children: [
          {
            id: '1-28210000',
            label: ' Respira mal [Grado : 2]',
          },
          {
            id: '1-28220000',
            label: ' Respira bien',
            children: [
              {
                id: '1-28221000',
                label: ' Está sudoroso [Grado : 2]',
              },
              {
                id: '1-28222000',
                label: ' No está sudoroso',
                children: [
                  {
                    id: '1-28222100',
                    label: ' Vómitos con sangre [Grado : 2]',
                    children: [
                      {
                        id: '1-28222210',
                        label: ' Abundante [Grado : 2]',
                        children: [
                          {
                            id: '1-28222421',
                            label: ' Primer o segundo trimestre [Grado : 2]',
                          },
                          {
                            id: '1-28222422',
                            label: ' Tercer trimestre [Grado : 1]',
                          },
                        ],
                      },
                      {
                        id: '1-28222220',
                        label: ' Escaso [Grado : 3]',
                        children: [
                          {
                            id: '1-28222421',
                            label: ' Primer o segundo trimestre [Grado : 2]',
                          },
                          {
                            id: '1-28222422',
                            label: ' Tercer trimestre [Grado : 1]',
                          },
                        ],
                      },
                      {
                        id: '1-28222410',
                        label: ' Sin embarazo [Grado : 3]',
                        children: [
                          {
                            id: '1-28222421',
                            label: ' Primer o segundo trimestre [Grado : 2]',
                          },
                          {
                            id: '1-28222422',
                            label: ' Tercer trimestre [Grado : 1]',
                          },
                        ],
                      },
                      {
                        id: '1-28222420',
                        label: ' Con embarazo',
                        children: [
                          {
                            id: '1-28222421',
                            label: ' Primer o segundo trimestre [Grado : 2]',
                          },
                          {
                            id: '1-28222422',
                            label: ' Tercer trimestre [Grado : 1]',
                          },
                        ],
                      },
                      {
                        id: '1-28222510',
                        label: ' Tiene dificultad respiratoria [Grado: 2]',
                        children: [
                          {
                            id: '1-28222421',
                            label: ' Primer o segundo trimestre [Grado : 2]',
                          },
                          {
                            id: '1-28222422',
                            label: ' Tercer trimestre [Grado : 1]',
                          },
                        ],
                      },
                      {
                        id: '1-28222520',
                        label: ' No tiene dificultad respiratoria [Grado: 3]',
                        children: [
                          {
                            id: '1-28222421',
                            label: ' Primer o segundo trimestre [Grado : 2]',
                          },
                          {
                            id: '1-28222422',
                            label: ' Tercer trimestre [Grado : 1]',
                          },
                        ],
                      },
                      {
                        id: '1-28222610',
                        label: ' Tuvo traumatismo [Grado : 2]',
                        children: [
                          {
                            id: '1-28222421',
                            label: ' Primer o segundo trimestre [Grado : 2]',
                          },
                          {
                            id: '1-28222422',
                            label: ' Tercer trimestre [Grado : 1]',
                          },
                        ],
                      },
                    ],
                  },
                  {
                    id: '1-28222200',
                    label: ' Materia fecal con sangre [Grado : 3]',
                    children: [
                      {
                        id: '1-28222210',
                        label: ' Abundante [Grado : 2]',
                        children: [
                          {
                            id: '1-28222421',
                            label: ' Primer o segundo trimestre [Grado : 2]',
                          },
                          {
                            id: '1-28222422',
                            label: ' Tercer trimestre [Grado : 1]',
                          },
                        ],
                      },
                      {
                        id: '1-28222220',
                        label: ' Escaso [Grado : 3]',
                        children: [
                          {
                            id: '1-28222421',
                            label: ' Primer o segundo trimestre [Grado : 2]',
                          },
                          {
                            id: '1-28222422',
                            label: ' Tercer trimestre [Grado : 1]',
                          },
                        ],
                      },
                      {
                        id: '1-28222410',
                        label: ' Sin embarazo [Grado : 3]',
                        children: [
                          {
                            id: '1-28222421',
                            label: ' Primer o segundo trimestre [Grado : 2]',
                          },
                          {
                            id: '1-28222422',
                            label: ' Tercer trimestre [Grado : 1]',
                          },
                        ],
                      },
                      {
                        id: '1-28222420',
                        label: ' Con embarazo',
                        children: [
                          {
                            id: '1-28222421',
                            label: ' Primer o segundo trimestre [Grado : 2]',
                          },
                          {
                            id: '1-28222422',
                            label: ' Tercer trimestre [Grado : 1]',
                          },
                        ],
                      },
                      {
                        id: '1-28222510',
                        label: ' Tiene dificultad respiratoria [Grado: 2]',
                        children: [
                          {
                            id: '1-28222421',
                            label: ' Primer o segundo trimestre [Grado : 2]',
                          },
                          {
                            id: '1-28222422',
                            label: ' Tercer trimestre [Grado : 1]',
                          },
                        ],
                      },
                      {
                        id: '1-28222520',
                        label: ' No tiene dificultad respiratoria [Grado: 3]',
                        children: [
                          {
                            id: '1-28222421',
                            label: ' Primer o segundo trimestre [Grado : 2]',
                          },
                          {
                            id: '1-28222422',
                            label: ' Tercer trimestre [Grado : 1]',
                          },
                        ],
                      },
                      {
                        id: '1-28222610',
                        label: ' Tuvo traumatismo [Grado : 2]',
                        children: [
                          {
                            id: '1-28222421',
                            label: ' Primer o segundo trimestre [Grado : 2]',
                          },
                          {
                            id: '1-28222422',
                            label: ' Tercer trimestre [Grado : 1]',
                          },
                        ],
                      },
                    ],
                  },
                  {
                    id: '1-28222300',
                    label: ' Orina con sangre [Grado : 3]',
                    children: [
                      {
                        id: '1-28222210',
                        label: ' Abundante [Grado : 2]',
                        children: [
                          {
                            id: '1-28222421',
                            label: ' Primer o segundo trimestre [Grado : 2]',
                          },
                          {
                            id: '1-28222422',
                            label: ' Tercer trimestre [Grado : 1]',
                          },
                        ],
                      },
                      {
                        id: '1-28222220',
                        label: ' Escaso [Grado : 3]',
                        children: [
                          {
                            id: '1-28222421',
                            label: ' Primer o segundo trimestre [Grado : 2]',
                          },
                          {
                            id: '1-28222422',
                            label: ' Tercer trimestre [Grado : 1]',
                          },
                        ],
                      },
                      {
                        id: '1-28222410',
                        label: ' Sin embarazo [Grado : 3]',
                        children: [
                          {
                            id: '1-28222421',
                            label: ' Primer o segundo trimestre [Grado : 2]',
                          },
                          {
                            id: '1-28222422',
                            label: ' Tercer trimestre [Grado : 1]',
                          },
                        ],
                      },
                      {
                        id: '1-28222420',
                        label: ' Con embarazo',
                        children: [
                          {
                            id: '1-28222421',
                            label: ' Primer o segundo trimestre [Grado : 2]',
                          },
                          {
                            id: '1-28222422',
                            label: ' Tercer trimestre [Grado : 1]',
                          },
                        ],
                      },
                      {
                        id: '1-28222510',
                        label: ' Tiene dificultad respiratoria [Grado: 2]',
                        children: [
                          {
                            id: '1-28222421',
                            label: ' Primer o segundo trimestre [Grado : 2]',
                          },
                          {
                            id: '1-28222422',
                            label: ' Tercer trimestre [Grado : 1]',
                          },
                        ],
                      },
                      {
                        id: '1-28222520',
                        label: ' No tiene dificultad respiratoria [Grado: 3]',
                        children: [
                          {
                            id: '1-28222421',
                            label: ' Primer o segundo trimestre [Grado : 2]',
                          },
                          {
                            id: '1-28222422',
                            label: ' Tercer trimestre [Grado : 1]',
                          },
                        ],
                      },
                      {
                        id: '1-28222610',
                        label: ' Tuvo traumatismo [Grado : 2]',
                        children: [
                          {
                            id: '1-28222421',
                            label: ' Primer o segundo trimestre [Grado : 2]',
                          },
                          {
                            id: '1-28222422',
                            label: ' Tercer trimestre [Grado : 1]',
                          },
                        ],
                      },
                    ],
                  },
                  {
                    id: '1-28222400',
                    label: ' Sangrado ginecológico',
                    children: [
                      {
                        id: '1-28222210',
                        label: ' Abundante [Grado : 2]',
                        children: [
                          {
                            id: '1-28222421',
                            label: ' Primer o segundo trimestre [Grado : 2]',
                          },
                          {
                            id: '1-28222422',
                            label: ' Tercer trimestre [Grado : 1]',
                          },
                        ],
                      },
                      {
                        id: '1-28222220',
                        label: ' Escaso [Grado : 3]',
                        children: [
                          {
                            id: '1-28222421',
                            label: ' Primer o segundo trimestre [Grado : 2]',
                          },
                          {
                            id: '1-28222422',
                            label: ' Tercer trimestre [Grado : 1]',
                          },
                        ],
                      },
                      {
                        id: '1-28222410',
                        label: ' Sin embarazo [Grado : 3]',
                        children: [
                          {
                            id: '1-28222421',
                            label: ' Primer o segundo trimestre [Grado : 2]',
                          },
                          {
                            id: '1-28222422',
                            label: ' Tercer trimestre [Grado : 1]',
                          },
                        ],
                      },
                      {
                        id: '1-28222420',
                        label: ' Con embarazo',
                        children: [
                          {
                            id: '1-28222421',
                            label: ' Primer o segundo trimestre [Grado : 2]',
                          },
                          {
                            id: '1-28222422',
                            label: ' Tercer trimestre [Grado : 1]',
                          },
                        ],
                      },
                      {
                        id: '1-28222510',
                        label: ' Tiene dificultad respiratoria [Grado: 2]',
                        children: [
                          {
                            id: '1-28222421',
                            label: ' Primer o segundo trimestre [Grado : 2]',
                          },
                          {
                            id: '1-28222422',
                            label: ' Tercer trimestre [Grado : 1]',
                          },
                        ],
                      },
                      {
                        id: '1-28222520',
                        label: ' No tiene dificultad respiratoria [Grado: 3]',
                        children: [
                          {
                            id: '1-28222421',
                            label: ' Primer o segundo trimestre [Grado : 2]',
                          },
                          {
                            id: '1-28222422',
                            label: ' Tercer trimestre [Grado : 1]',
                          },
                        ],
                      },
                      {
                        id: '1-28222610',
                        label: ' Tuvo traumatismo [Grado : 2]',
                        children: [
                          {
                            id: '1-28222421',
                            label: ' Primer o segundo trimestre [Grado : 2]',
                          },
                          {
                            id: '1-28222422',
                            label: ' Tercer trimestre [Grado : 1]',
                          },
                        ],
                      },
                    ],
                  },
                  {
                    id: '1-28222500',
                    label: ' Tos con sangre',
                    children: [
                      {
                        id: '1-28222210',
                        label: ' Abundante [Grado : 2]',
                        children: [
                          {
                            id: '1-28222421',
                            label: ' Primer o segundo trimestre [Grado : 2]',
                          },
                          {
                            id: '1-28222422',
                            label: ' Tercer trimestre [Grado : 1]',
                          },
                        ],
                      },
                      {
                        id: '1-28222220',
                        label: ' Escaso [Grado : 3]',
                        children: [
                          {
                            id: '1-28222421',
                            label: ' Primer o segundo trimestre [Grado : 2]',
                          },
                          {
                            id: '1-28222422',
                            label: ' Tercer trimestre [Grado : 1]',
                          },
                        ],
                      },
                      {
                        id: '1-28222410',
                        label: ' Sin embarazo [Grado : 3]',
                        children: [
                          {
                            id: '1-28222421',
                            label: ' Primer o segundo trimestre [Grado : 2]',
                          },
                          {
                            id: '1-28222422',
                            label: ' Tercer trimestre [Grado : 1]',
                          },
                        ],
                      },
                      {
                        id: '1-28222420',
                        label: ' Con embarazo',
                        children: [
                          {
                            id: '1-28222421',
                            label: ' Primer o segundo trimestre [Grado : 2]',
                          },
                          {
                            id: '1-28222422',
                            label: ' Tercer trimestre [Grado : 1]',
                          },
                        ],
                      },
                      {
                        id: '1-28222510',
                        label: ' Tiene dificultad respiratoria [Grado: 2]',
                        children: [
                          {
                            id: '1-28222421',
                            label: ' Primer o segundo trimestre [Grado : 2]',
                          },
                          {
                            id: '1-28222422',
                            label: ' Tercer trimestre [Grado : 1]',
                          },
                        ],
                      },
                      {
                        id: '1-28222520',
                        label: ' No tiene dificultad respiratoria [Grado: 3]',
                        children: [
                          {
                            id: '1-28222421',
                            label: ' Primer o segundo trimestre [Grado : 2]',
                          },
                          {
                            id: '1-28222422',
                            label: ' Tercer trimestre [Grado : 1]',
                          },
                        ],
                      },
                      {
                        id: '1-28222610',
                        label: ' Tuvo traumatismo [Grado : 2]',
                        children: [
                          {
                            id: '1-28222421',
                            label: ' Primer o segundo trimestre [Grado : 2]',
                          },
                          {
                            id: '1-28222422',
                            label: ' Tercer trimestre [Grado : 1]',
                          },
                        ],
                      },
                    ],
                  },
                  {
                    id: '1-28222600',
                    label: ' Sangra por nariz',
                    children: [
                      {
                        id: '1-28222210',
                        label: ' Abundante [Grado : 2]',
                        children: [
                          {
                            id: '1-28222421',
                            label: ' Primer o segundo trimestre [Grado : 2]',
                          },
                          {
                            id: '1-28222422',
                            label: ' Tercer trimestre [Grado : 1]',
                          },
                        ],
                      },
                      {
                        id: '1-28222220',
                        label: ' Escaso [Grado : 3]',
                        children: [
                          {
                            id: '1-28222421',
                            label: ' Primer o segundo trimestre [Grado : 2]',
                          },
                          {
                            id: '1-28222422',
                            label: ' Tercer trimestre [Grado : 1]',
                          },
                        ],
                      },
                      {
                        id: '1-28222410',
                        label: ' Sin embarazo [Grado : 3]',
                        children: [
                          {
                            id: '1-28222421',
                            label: ' Primer o segundo trimestre [Grado : 2]',
                          },
                          {
                            id: '1-28222422',
                            label: ' Tercer trimestre [Grado : 1]',
                          },
                        ],
                      },
                      {
                        id: '1-28222420',
                        label: ' Con embarazo',
                        children: [
                          {
                            id: '1-28222421',
                            label: ' Primer o segundo trimestre [Grado : 2]',
                          },
                          {
                            id: '1-28222422',
                            label: ' Tercer trimestre [Grado : 1]',
                          },
                        ],
                      },
                      {
                        id: '1-28222510',
                        label: ' Tiene dificultad respiratoria [Grado: 2]',
                        children: [
                          {
                            id: '1-28222421',
                            label: ' Primer o segundo trimestre [Grado : 2]',
                          },
                          {
                            id: '1-28222422',
                            label: ' Tercer trimestre [Grado : 1]',
                          },
                        ],
                      },
                      {
                        id: '1-28222520',
                        label: ' No tiene dificultad respiratoria [Grado: 3]',
                        children: [
                          {
                            id: '1-28222421',
                            label: ' Primer o segundo trimestre [Grado : 2]',
                          },
                          {
                            id: '1-28222422',
                            label: ' Tercer trimestre [Grado : 1]',
                          },
                        ],
                      },
                      {
                        id: '1-28222610',
                        label: ' Tuvo traumatismo [Grado : 2]',
                        children: [
                          {
                            id: '1-28222421',
                            label: ' Primer o segundo trimestre [Grado : 2]',
                          },
                          {
                            id: '1-28222422',
                            label: ' Tercer trimestre [Grado : 1]',
                          },
                        ],
                      },
                    ],
                  },
                  {
                    id: '1-28222700',
                    label: ' Se desconoce por donde sangra [Grado : 2]',
                    children: [
                      {
                        id: '1-28222210',
                        label: ' Abundante [Grado : 2]',
                        children: [
                          {
                            id: '1-28222421',
                            label: ' Primer o segundo trimestre [Grado : 2]',
                          },
                          {
                            id: '1-28222422',
                            label: ' Tercer trimestre [Grado : 1]',
                          },
                        ],
                      },
                      {
                        id: '1-28222220',
                        label: ' Escaso [Grado : 3]',
                        children: [
                          {
                            id: '1-28222421',
                            label: ' Primer o segundo trimestre [Grado : 2]',
                          },
                          {
                            id: '1-28222422',
                            label: ' Tercer trimestre [Grado : 1]',
                          },
                        ],
                      },
                      {
                        id: '1-28222410',
                        label: ' Sin embarazo [Grado : 3]',
                        children: [
                          {
                            id: '1-28222421',
                            label: ' Primer o segundo trimestre [Grado : 2]',
                          },
                          {
                            id: '1-28222422',
                            label: ' Tercer trimestre [Grado : 1]',
                          },
                        ],
                      },
                      {
                        id: '1-28222420',
                        label: ' Con embarazo',
                        children: [
                          {
                            id: '1-28222421',
                            label: ' Primer o segundo trimestre [Grado : 2]',
                          },
                          {
                            id: '1-28222422',
                            label: ' Tercer trimestre [Grado : 1]',
                          },
                        ],
                      },
                      {
                        id: '1-28222510',
                        label: ' Tiene dificultad respiratoria [Grado: 2]',
                        children: [
                          {
                            id: '1-28222421',
                            label: ' Primer o segundo trimestre [Grado : 2]',
                          },
                          {
                            id: '1-28222422',
                            label: ' Tercer trimestre [Grado : 1]',
                          },
                        ],
                      },
                      {
                        id: '1-28222520',
                        label: ' No tiene dificultad respiratoria [Grado: 3]',
                        children: [
                          {
                            id: '1-28222421',
                            label: ' Primer o segundo trimestre [Grado : 2]',
                          },
                          {
                            id: '1-28222422',
                            label: ' Tercer trimestre [Grado : 1]',
                          },
                        ],
                      },
                      {
                        id: '1-28222610',
                        label: ' Tuvo traumatismo [Grado : 2]',
                        children: [
                          {
                            id: '1-28222421',
                            label: ' Primer o segundo trimestre [Grado : 2]',
                          },
                          {
                            id: '1-28222422',
                            label: ' Tercer trimestre [Grado : 1]',
                          },
                        ],
                      },
                    ],
                  },
                ],
              },
            ],
          },
        ],
      },
    ],
  },
  {
    id: '1-29000000',
    label: '(Adulto) HIPERTENSION ARTERIAL',
    children: [
      {
        id: '1-29100000',
        label: ' Dificultad para hablar [Grado : 2]',
      },
      {
        id: '1-29200000',
        label: ' Sin Dificultad para hablar',
        children: [
          {
            id: '1-29210000',
            label: ' Cefalea [Grado : 3]',
          },
          {
            id: '1-29220000',
            label: ' Sin cefaleas ni otros síntomas [Grado : 3]',
          },
        ],
      },
    ],
  },
  {
    id: '1-30000000',
    label: '(Adulto) HIPOTENSION ARTERIAL (TA menor de 90 mmHg)',
    children: [
      {
        id: '1-30100000',
        label: ' Tiene dolor de pecho [Grado : 2]',
      },
      {
        id: '1-30200000',
        label: ' No tiene dolor de pecho',
        children: [
          {
            id: '1-30210000',
            label: ' Esta sudoroso [Grado : 3P]',
          },
          {
            id: '1-30220000',
            label: ' No esta sudoroso',
            children: [
              {
                id: '1-30221000',
                label: ' No tiene síntomas específicos [Grado : 3]',
              },
            ],
          },
        ],
      },
    ],
  },
  {
    id: '1-31000000',
    label:
      '(Adulto) INTENTO DE SUICIDIO [Grado : 1] Evaluar apoyo policial y psiquiátrico',
  },
  {
    id: '1-32000000',
    label: '(Adulto) INCONTINENCIA DE ESFINTERES',
    children: [
      {
        id: '1-32100000',
        label: ' Tuvo convulsiones [Deriva : CONVULSIONES]',
      },
      {
        id: '1-32200000',
        label: ' No tuvo convulsiones [Grado : 3]',
      },
    ],
  },
  {
    id: '1-33000000',
    label:
      '(Adulto) INTOXICACION POR GASES TOXICOS O DROGAS [Nota : (ALERTAR A LA TRIPULACION)]',
    children: [
      {
        id: '1-33100000',
        label: ' No esta consciente [Grado : 1]',
      },
      {
        id: '1-33200000',
        label: ' Esta consciente',
        children: [
          {
            id: '1-33210000',
            label: ' Respira mal [Grado : 1]',
          },
          {
            id: '1-33220000',
            label: ' Respira bien',
            children: [
              {
                id: '1-33221000',
                label: ' Ocurrió recién (menos de 2 horas) [Grado : 2]',
              },
              {
                id: '1-33222000',
                label: ' No ocurrió recién (más de 2 horas)',
                children: [
                  {
                    id: '1-33222100',
                    label: ' Tiene nauseas vómitos o cefalea[Grado : 2]',
                  },
                  {
                    id: '1-33222200',
                    label: ' No tiene nauseas, vómitos ni cefalea[Grado : 3P]',
                  },
                ],
              },
            ],
          },
        ],
      },
    ],
  },
  {
    id: '1-34000000',
    label: '(Adulto) LUMBALGIA',
    children: [
      {
        id: '1-34100000',
        label: ' Antecedentes de cólico renal',
        children: [
          {
            id: '1-34110000',
            label: ' Esta cursando un cólico renal [Grado : 2]',
          },
          {
            id: '1-34120000',
            label: ' No está cursando un cólico renal [Grado : 3]',
          },
        ],
      },
      {
        id: '1-34200000',
        label: ' No tiene ant. cólico renal(único síntoma) [Grado : 3]',
      },
    ],
  },
  {
    id: '1-35000000',
    label: '(Adulto) MAREOS',
    children: [
      {
        id: '1-35100000',
        label: ' Tiene vómitos [Grado : 3]',
      },
      {
        id: '1-35200000',
        label: ' No tiene vómitos',
        children: [
          {
            id: '1-35210000',
            label: ' Tiene Dolor de cabeza [Grado : 3]',
          },
          {
            id: '1-35220000',
            label: ' No tiene Dolor de cabeza',
            children: [
              {
                id: '1-35221000',
                label: ' Tiene zumbidos en los oídos [Grado : 3]',
              },
              {
                id: '1-35222000',
                label: ' No tiene zumbidos en los oídos [Grado : 3]',
              },
            ],
          },
        ],
      },
    ],
  },
  {
    id: '1-36000000',
    label: '(Adulto) MORDEDURA DE...',
    children: [
      {
        id: '1-36100000',
        label: ' Sangra mucho [Grado: 1]',
      },
      {
        id: '1-36200000',
        label: ' No sangra mucho [Grado: 2]',
        children: [
          {
            id: '1-36210000',
            label: ' Lesión múltiples y/o en cara [Grado : 2]',
          },
          {
            id: '1-36220000',
            label: ' Sin Lesión múltiples y/o en cara [Grado : 3]',
          },
        ],
      },
    ],
  },
  {
    id: '1-37000000',
    label: '(Adulto) NAUSEAS-VOMITOS',
    children: [
      {
        id: '1-37100000',
        label: ' Tiene vómitos con sangre [Grado: 2]',
      },
      {
        id: '1-37200000',
        label: ' No tiene vómitos con sangre',
        children: [
          {
            id: '1-37210000',
            label: ' Tuvo traumatismo de cráneo [Grado : 2]',
          },
          {
            id: '1-37220000',
            label: ' No tuvo traumatismo de cráneo',
            children: [
              {
                id: '1-37221000',
                label: ' Tiene dolor abdominal [Grado : 3]',
              },
              {
                id: '1-37222000',
                label: ' No tiene dolor abdominal [Grado : 3]',
              },
            ],
          },
        ],
      },
    ],
  },
  {
    id: '1-38000000',
    label: '(Adulto) POLITRAUMATISMO',
    children: [
      {
        id: '1-38100000',
        label: ' No esta consciente [Grado : 1]',
      },
      {
        id: '1-38200000',
        label: ' Esta consciente',
        children: [
          {
            id: '1-38210000',
            label: ' No respira o respira mal [Grado : 1]',
          },
          {
            id: '1-38220000',
            label: ' Respira bien',
            children: [
              {
                id: '1-38221000',
                label: ' Tiene hemorragia evidente [Grado : 1]',
              },
              {
                id: '1-38222000',
                label: ' No tiene hemorragia evidente',
                children: [
                  {
                    id: '1-38222100',
                    label: ' Esta caído en el suelo [Grado : 1]',
                  },
                  {
                    id: '1-38222200',
                    label: ' No esta caído en el suelo [Grado : 2]',
                  },
                ],
              },
            ],
          },
        ],
      },
    ],
  },
  {
    id: '1-39000000',
    label: '(Adulto) PARESTESIAS (HORMIGUEOS) [Grado : 3]',
    children: [
      {
        id: '1-39100000',
        label: ' Tiene dificultad para mover el miembro [Grado: 3]',
      },
      {
        id: '1-39200000',
        label: ' No tiene dificultad para mover el miembro [Grado: 3]',
      },
    ],
  },
  {
    id: '1-41000000',
    label:
      '(Adulto) PACIENTE VIOLENTO[Nota:(EVALUAR APOYO POLICIAL)][Grado : 2]',
  },
  {
    id: '1-42000000',
    label: '(Adulto) PROBLEMAS VINCULADOS CON LA DBT',
    children: [
      {
        id: '1-42100000',
        label: ' Está hipoglucémico (menor de 70) [Grado: 1]',
      },
      {
        id: '1-42200000',
        label: ' No está hipoglucémico (mayor de 70)',
        children: [
          {
            id: '1-42210000',
            label: ' Está hiperglucémico',
            children: [
              {
                id: '1-42211000',
                label: ' Glucemia mayor a 300 [Grado : 2]',
              },
              {
                id: '1-42212000',
                label: ' Glucemia menor a 300 [Grado : 3P]',
              },
            ],
          },
          {
            id: '1-42220000',
            label: ' No está hiperglucémico [Grado: 3]',
          },
        ],
      },
    ],
  },
  {
    id: '1-43000000',
    label: '(Adulto) PICADURA DE...',
    children: [
      {
        id: '1-43100000',
        label: ' Respira mal [Grado : 1]',
      },
      {
        id: '1-43200000',
        label: ' Respira bien',
        children: [
          {
            id: '1-43210000',
            label: ' Tiene hinchada la cara o lengua [Grado : 2]',
          },
          {
            id: '1-43220000',
            label: ' No tiene hinchada cara o lengua',
            children: [
              {
                id: '1-43221000',
                label: ' Antecedentes de edema de glotis [Grado : 3P]',
              },
              {
                id: '1-43222000',
                label: ' Sin antecedentes de edema de glotis [Grado : 3]',
              },
            ],
          },
        ],
      },
    ],
  },
  {
    id: '1-44000000',
    label: '(Adulto) QUEMADURAS',
    children: [
      {
        id: '1-44100000',
        label: ' No esta consciente [Grado : 1]',
      },
      {
        id: '1-44200000',
        label: ' Esta consciente',
        children: [
          {
            id: '1-44210000',
            label: ' Respira mal [Grado : 1]',
          },
          {
            id: '1-44220000',
            label: ' Respira bien',
            children: [
              {
                id: '1-44221000',
                label: ' En cara-torso-abdomen o todo miembro [Grado : 1]',
              },
              {
                id: '1-44222000',
                label: ' No en cara-torso-abdomen o todo miembro [Grado : 3P]',
              },
            ],
          },
        ],
      },
    ],
  },
  {
    id: '1-45000000',
    label: '(Adulto) SIN DATOS [Grado : 1]',
  },
  {
    id: '1-46000000',
    label: '(Adulto) TOS [Grado : 3]',
  },
  {
    id: '1-50000000',
    label: '(Adulto) TRAUMA DE TORAX',
    children: [
      {
        id: '1-50100000',
        label: ' Respira mal [Grado : 2]',
      },
      {
        id: '1-50200000',
        label: ' Respira bien',
        children: [
          {
            id: '1-50210000',
            label: ' Está sangrando [Grado : 2]',
          },
          {
            id: '1-50220000',
            label: ' No está sangrando',
            children: [
              {
                id: '1-50221000',
                label: ' Tiene dolor en el tórax [Grado : 3P]',
              },
              {
                id: '1-50222000',
                label: ' No tiene dolor en el tórax [Grado : 3]',
              },
            ],
          },
        ],
      },
    ],
  },
  {
    id: '1-51000000',
    label: '(Adulto) TRAUMA DORSO LUMBAR',
    children: [
      {
        id: '1-51100000',
        label: ' Tiene dificultad para respirar [Grado : 2]',
      },
      {
        id: '1-51200000',
        label: ' No tiene dificultad para respirar',
        children: [
          {
            id: '1-51210000',
            label: ' Orinó con sangre [Grado : 2]',
          },
          {
            id: '1-51220000',
            label: ' No orinó con sangre',
            children: [
              {
                id: '1-51221000',
                label: ' No mueve bien las piernas [Grado : 2]',
              },
              {
                id: '1-51222000',
                label: ' Mueve bien las piernas [Grado : 3]',
              },
            ],
          },
        ],
      },
    ],
  },
  {
    id: '1-52000000',
    label: '(Adulto) TRAUMA DE ABDOMEN O PELVIS',
    children: [
      {
        id: '1-52100000',
        label: ' Está inconciente [Grado : 1]',
      },
      {
        id: '1-52200000',
        label: ' Está conciente',
        children: [
          {
            id: '1-52210000',
            label: ' Esta sangrando o sudoroso [Grado : 1]',
          },
        ],
      },
    ],
  },
  {
    id: '1-53000000',
    label: '(Adulto) TRAUMATISMO FACIAL',
    children: [
      {
        id: '1-53100000',
        label: ' No está conciente [Grado : 1]',
      },
      {
        id: '1-53200000',
        label: ' Está conciente',
        children: [
          {
            id: '1-53210000',
            label: ' Respira mal [Grado : 2]',
          },
          {
            id: '1-53220000',
            label: ' Respira bien',
            children: [
              {
                id: '1-53221000',
                label: ' Esta sangrando [Grado : 3P]',
              },
              {
                id: '1-53222000',
                label: ' No esta sangrando [Grado : 3]',
              },
            ],
          },
        ],
      },
    ],
  },
  {
    id: '1-54000000',
    label: '(Adulto) TRAUMATISMO DE MIEMBROS',
    children: [
      {
        id: '1-54100000',
        label:
          ' Evidencia de fractura (deformación miembro-imp. Mo) [Grado : 2]',
      },
      {
        id: '1-54200000',
        label: ' No tiene evidencia de fractura',
        children: [
          {
            id: '1-54210000',
            label: ' Está sangrando [Grado : 2]',
          },
          {
            id: '1-54220000',
            label: ' No está sangrando',
            children: [
              {
                id: '1-54221000',
                label: ' Tiene dolor [Grado : 3P]',
              },
              {
                id: '1-54222000',
                label: ' No tiene dolor [Grado : 3]',
              },
            ],
          },
        ],
      },
    ],
  },
  {
    id: '1-55000000',
    label: '(Adulto) TRAUMATISMO DE CRANEO',
    children: [
      {
        id: '1-55100000',
        label: ' No está consciente [Grado : 1]',
      },
      {
        id: '1-55200000',
        label: ' Esta consciente actualmente',
        children: [
          {
            id: '1-55210000',
            label: ' Cuando se golpeó tuvo pérdida de conocimiento [Grado : 1]',
          },
          {
            id: '1-55220000',
            label: ' Cuando se golpeó no tuvo pérdida de conocimiento',
            children: [
              {
                id: '1-55221000',
                label: ' Tiene dificultad para hablar [Grado : 1]',
              },
              {
                id: '1-55222000',
                label: ' No tiene dificultad para hablar',
                children: [
                  {
                    id: '1-55222100',
                    label: ' Tiene herida que sangra [Grado : 2]',
                  },
                  {
                    id: '1-55222200',
                    label: ' No tiene herida que sangra [Grado : 3]',
                  },
                ],
              },
            ],
          },
        ],
      },
    ],
  },
  {
    id: '1-56000000',
    label: '(Adulto) EMBARAZO A TERMINO',
    children: [
      {
        id: '1-56100000',
        label: ' El niño está saliendo [Grado: 1]',
      },
      {
        id: '1-56200000',
        label: ' No está saliendo',
        children: [
          {
            id: '1-56210000',
            label: ' Perdió sangre [Grado: 1]',
          },
          {
            id: '1-56220000',
            label: ' No perdió sangre',
            children: [
              {
                id: '1-56221000',
                label: ' Tiene contracciones',
                children: [
                  {
                    id: '1-56221100',
                    label: ' Primer embarazo',
                    children: [
                      {
                        id: '1-56221110',
                        label:
                          ' Contracciones cada 2 minutos o menos [Grado : 1]',
                      },
                      {
                        id: '1-56221120',
                        label:
                          ' Contracciones cada más de 2 minutos [Grado : 2]',
                      },
                      {
                        id: '1-56221210',
                        label:
                          ' Contracciones cada 5 minutos o menos [Grado : 1]',
                      },
                      {
                        id: '1-56221220',
                        label:
                          ' Contracciones cada más de 5 minutos [Grado : 2]',
                      },
                    ],
                  },
                  {
                    id: '1-56221200',
                    label: ' Embarazos previos',
                    children: [
                      {
                        id: '1-56221110',
                        label:
                          ' Contracciones cada 2 minutos o menos [Grado : 1]',
                      },
                      {
                        id: '1-56221120',
                        label:
                          ' Contracciones cada más de 2 minutos [Grado : 2]',
                      },
                      {
                        id: '1-56221210',
                        label:
                          ' Contracciones cada 5 minutos o menos [Grado : 1]',
                      },
                      {
                        id: '1-56221220',
                        label:
                          ' Contracciones cada más de 5 minutos [Grado : 2]',
                      },
                    ],
                  },
                ],
              },
              {
                id: '1-56222000',
                label: ' No tiene contracciones',
                children: [
                  {
                    id: '1-56222100',
                    label: ' Perdió líquido o rompió bolsa [Grado : 2]',
                  },
                  {
                    id: '1-56222200',
                    label: ' No Perdió líquido ni rompió bolsa [Grado:3]',
                  },
                ],
              },
            ],
          },
        ],
      },
    ],
  },
  {
    id: '1-57000000',
    label: '(Adulto) TEMBLOR',
    children: [
      {
        id: '1-57100000',
        label: ' No se mantiene parado [Grado : 3]',
      },
      {
        id: '1-57200000',
        label: ' Se mantiene parado',
        children: [
          {
            id: '1-57210000',
            label: ' Tiene Fiebre [Grado : 3]',
          },
          {
            id: '1-57220000',
            label: ' No tiene fiebre [Grado : 3]',
          },
        ],
      },
    ],
  },
  {
    id: '1-58000000',
    label: '(Adulto) VICTIMAS MULTIPLES [Grado : 1]',
  },
  {
    id: '1-59000000',
    label:
      '(Adulto) PALPITACIONES [Nota : (REALIZAR ECG)] Igual que en arritmias',
    children: [
      {
        id: '1-59100000',
        label: ' Tiene alteración de la conciencia [Grado : 2]',
      },
      {
        id: '1-59200000',
        label: ' No tiene alteración de la conciencia',
        children: [
          {
            id: '1-59210000',
            label: ' Respira Mal [Grado : 2]',
          },
          {
            id: '1-59220000',
            label: ' No respira Mal',
            children: [
              {
                id: '1-59221000',
                label: ' Tiene dolor de pecho [Grado : 2]',
              },
              {
                id: '1-59222000',
                label: ' No tiene dolor de pecho [Grado : 3]',
              },
            ],
          },
        ],
      },
    ],
  },
  {
    id: '1-60000000',
    label: '(Adulto) VIA PUBLICA [Grado : 1]',
  },
  {
    id: '1-61000000',
    label: '(Adulto) GALENO EN QTH',
    children: [
      {
        id: '1-61100000',
        label: ' Requiere grado 1 [Grado : 1]',
      },
      {
        id: '1-61200000',
        label: ' Requiere grado 2 [Grado : 2]',
      },
      {
        id: '1-61300000',
        label: ' Requiere grado 3 [Grado : 3]',
      },
    ],
  },
  {
    id: '1-62000000',
    label: '(Adulto) HERIDA CORTANTE',
    children: [
      {
        id: '1-62100000',
        label: ' Con sangrado activo [Grado : 2]',
      },
      {
        id: '1-62200000',
        label: ' Sin sangrado activo [Grado : 3P]',
      },
    ],
  },
  {
    id: '1-97000000',
    label: '(Adulto) PERDIDA DE CONOCIMIENTO [Nota : (REALIZAR ECG)]',
    children: [
      {
        id: '1-97100000',
        label: ' No se recupero [Grado : 1]',
      },
      {
        id: '1-97200000',
        label: ' Se Recupero',
        children: [
          {
            id: '1-97210000',
            label: ' Respira mal [Grado : 2]',
          },
          {
            id: '1-97220000',
            label: ' Respira bien',
            children: [
              {
                id: '1-97221000',
                label: ' Habla con dificultad [Grado : 2]',
              },
              {
                id: '1-97222000',
                label: ' Habla sin dificultad',
                children: [
                  {
                    id: '1-97222100',
                    label: ' Tuvo traumatismo [Grado : 2]',
                  },
                  {
                    id: '1-97222200',
                    label: ' No tuvo traumatismo [Grado : 3P]',
                  },
                ],
              },
            ],
          },
        ],
      },
    ],
  },
  {
    id: '1-100000000',
    label: '(Adulto) CONTROL DE AUSENTISMO [Grado : 3]',
  },
  {
    id: '1-101000000',
    label:
      '(Adulto) PARESIA (DIFICULTAD MOV. DE 1 O MAS MIEMBROS O BOCA [Nota : No confundir c/PARESTESIA]',
    children: [
      {
        id: '1-101100000',
        label: ' Menor de tres horas de evolución [Grado : 2]',
      },
      {
        id: '1-101200000',
        label: ' Mayor de tres horas de evolución',
        children: [
          {
            id: '1-101210000',
            label: ' No moviliza bien resto miembros [Grado: 2]',
          },
          {
            id: '1-101220000',
            label: ' Moviliza bien el resto de los miembros.',
            children: [
              {
                id: '1-101221000',
                label:
                  ' Tiene antecedentes de enfermedad neurológica [Grado : 3]',
              },
              {
                id: '1-101222000',
                label:
                  ' No tiene antecedentes de enfermedad neurológica [Grado:3]',
              },
            ],
          },
        ],
      },
    ],
  },
  {
    id: '1-102000000',
    label: '(Adulto) CUERPO EXTRAÑO EN NARIZ',
    children: [
      {
        id: '1-102100000',
        label: ' Respira mal [Grado : 2]',
      },
      {
        id: '1-102200000',
        label: ' Respira bien',
        children: [
          {
            id: '1-102210000',
            label: ' Está sangrando [Grado : 2]',
          },
          {
            id: '1-102220000',
            label: ' No está sangrando [Grado : 3]',
          },
        ],
      },
    ],
  },
  {
    id: '1-103000000',
    label: '(Adulto) CUERPO EXTRAÑO EN OIDO',
    children: [
      {
        id: '1-103100000',
        label: ' Está sangrando [Grado : 2]',
      },
      {
        id: '1-103200000',
        label: ' No está sangrando [Grado : 3P]',
      },
    ],
  },
  {
    id: '1-104000000',
    label: '(Adulto) CUERPO EXTRAÑO EN OJO',
    children: [
      {
        id: '1-104100000',
        label: ' Está con mucho dolor o irritación [Grado : 3P]',
      },
      {
        id: '1-104200000',
        label: ' Está solamente con molestias leves [Grado : 3]',
      },
    ],
  },
  {
    id: '1-105000000',
    label: '(Adulto) EDEMAS EN MI',
    children: [
      {
        id: '1-105100000',
        label: ' En un solo miembro',
        children: [
          {
            id: '1-105110000',
            label: ' Está azul o blanco [Grado : 2]',
          },
          {
            id: '1-105120000',
            label: ' No está azul ni blanco [Grado : 3]',
          },
        ],
      },
      {
        id: '1-105200000',
        label: ' En ambos miembros',
        children: [
          {
            id: '1-105210000',
            label: ' Respirar mal [Grado : 2]',
          },
          {
            id: '1-105220000',
            label: ' Respira bien [Grado : 3]',
          },
        ],
      },
    ],
  },
  {
    id: '1-106000000',
    label: '(Adulto) IRRITACIÓN OCULAR',
    children: [
      {
        id: '1-106100000',
        label: ' Tuvo un traumatismo [Grado : 2]',
      },
      {
        id: '1-106200000',
        label: ' No tuvo traumatismo',
        children: [
          {
            id: '1-106210000',
            label: ' Le ingreso alguna sustancia irritativa [Grado : 2]',
          },
        ],
      },
    ],
  },
  {
    id: '1-107000000',
    label: '(Adulto) DOLOR DE ESPALDA/DORSAL',
    children: [
      {
        id: '1-107100000',
        label: ' Tiene dolor con el movimiento [Grado : 3]',
      },
      {
        id: '1-107200000',
        label: ' No tiene dolor con el movimiento [Grado : 3]',
      },
    ],
  },
  {
    id: '1-108000000',
    label: '(Adulto) DOLOR DE MIEMBROS',
    children: [
      {
        id: '1-108100000',
        label: ' Presentó traumatismo',
        children: [
          {
            id: '1-108110000',
            label: ' Evidencia de fractura [Grado : 2]',
          },
          {
            id: '1-108120000',
            label: ' No tiene evidencia de fractura',
            children: [
              {
                id: '1-108121000',
                label: ' Está sangrando [Grado : 2]',
              },
              {
                id: '1-108122000',
                label: ' No está sangrando [Grado : 3]',
              },
            ],
          },
        ],
      },
      {
        id: '1-108200000',
        label: ' No presentó traumatismo',
        children: [
          {
            id: '1-108210000',
            label: ' Está el miembro azul o blanco [Grado : 2]',
          },
          {
            id: '1-108220000',
            label: ' No está azul o blanco [Grado : 3]',
          },
        ],
      },
    ],
  },
  {
    id: '1-109000000',
    label: '(Adulto) DOLOR TESTICULAR',
    children: [
      {
        id: '1-109100000',
        label: ' Presentó traumatismo [Grado : 2]',
      },
      {
        id: '1-109200000',
        label: ' No presentó traumatismo [Grado : 2]',
        children: [
          {
            id: '1-109210000',
            label: ' Tiempo de evolución < 12 hs [Grado : 2]',
          },
          {
            id: '1-109220000',
            label: ' Tiempo de evolución > 12 hs [Grado : 3]',
          },
        ],
      },
    ],
  },
  {
    id: '1-110000000',
    label: '(Adulto) DOLOR DE OIDOS [Grado : 3]',
  },
  {
    id: '1-111000000',
    label: '(Adulto) DOLOR DE GARGANTA [Grado : 3]',
  },
  {
    id: '1-112000000',
    label: '(Adulto) DOLOR CORPORAL',
    children: [
      {
        id: '1-112100000',
        label: ' Tiene fiebre [Grado : 3]',
      },
      {
        id: '1-112200000',
        label: ' No tiene fiebre [Grado : 3]',
      },
    ],
  },
  {
    id: '1-113000000',
    label: '(Adulto) EMBARAZO PRIMER TRIMESTRE',
    children: [
      {
        id: '1-113100000',
        label: ' Tiene hemorragia genital o pérdida de líquido [Grado: 2]',
      },
      {
        id: '1-113200000',
        label: ' No tiene hemorragia genital ni pérdida de líquido',
        children: [
          {
            id: '1-113210000',
            label: ' Tiene dolor abdominal [Grado: 2]',
          },
          {
            id: '1-113220000',
            label: ' No tiene dolor abdominal',
          },
        ],
      },
    ],
  },
  {
    id: '1-114000000',
    label: '(Adulto) ATRAGANTAMIENTO',
    children: [
      {
        id: '1-114100000',
        label: ' No puede hablar o toser [Grado : 1]',
      },
      {
        id: '1-114200000',
        label: ' Puede hablar o toser [Grado : 2]',
      },
    ],
  },
  {
    id: '1-115000000',
    label: '(Adulto) CONTROL EVOLUTIVO',
    children: [
      {
        id: '1-115100000',
        label: ' Control de infección respiratoria [Grado: 3]',
      },
      {
        id: '1-115200000',
        label: ' Control de diarrea/gastroenteritis [Grado: 3]',
      },
      {
        id: '1-115300000',
        label: ' Control de Eruptiva [Grado: 3]',
      },
      {
        id: '1-115400000',
        label: ' Control de hipertensión arterial [Grado: 3]',
      },
      {
        id: '1-115500000',
        label: ' Control de síndrome febril [Grado: 3]',
      },
      {
        id: '1-115600000',
        label: ' Control de otras enfermedades [Grado: 3]',
      },
    ],
  },
  {
    id: '2-1000000',
    label: '(Pediatrico) AHOGADOS POR INMERSION',
    children: [
      {
        id: '2-1100000',
        label: ' No está consciente [Grado: 1]',
      },
      {
        id: '2-1200000',
        label: ' Está conciente',
        children: [
          {
            id: '2-1210000',
            label: ' Respira mal [Grado: 1]',
          },
          {
            id: '2-1220000',
            label: ' Respira bien [Grado: 2]',
          },
        ],
      },
    ],
  },
  {
    id: '2-10000000',
    label: '(Pediatrico) CONFUSION-OBNUBILACION',
    children: [
      {
        id: '2-10100000',
        label: ' Respira Mal [Grado: 1]',
      },
      {
        id: '2-10200000',
        label: ' Respira Bien',
        children: [
          {
            id: '2-10210000',
            label: ' Está pálido o sudoroso [Grado: 2]',
          },
          {
            id: '2-10220000',
            label: ' No está pálido ni sudoroso',
            children: [
              {
                id: '2-10221000',
                label: ' Cuanto tiempo hace que está con este cuadro',
                children: [
                  {
                    id: '2-10221100',
                    label: ' Menos de seis horas [Grado: 2]',
                  },
                  {
                    id: '2-10221200',
                    label: ' Entre seis y doce horas [Grado: 3]',
                  },
                  {
                    id: '2-10221300',
                    label: ' Más de doce horas [Grado: 3]',
                  },
                ],
              },
              {
                id: '2-10222000',
                label: ' Se desconoce el tiempo de evolución [Grado: 3]',
              },
            ],
          },
        ],
      },
    ],
  },
  {
    id: '2-101000000',
    label: '(Pediatrico) PARESIA (DIFICULTAD MOV.DE 1 O MAS MIEMBROS O BOCA',
    children: [
      {
        id: '2-101100000',
        label: ' Menor de tres horas de evolución [Grado: 2]',
      },
      {
        id: '2-101200000',
        label: ' Mayor de tres horas de evolución',
        children: [
          {
            id: '2-101210000',
            label: ' No moviliza bien el resto de los miembros. [Grado: 2]',
          },
          {
            id: '2-101220000',
            label: ' Moviliza bien resto miembros',
            children: [
              {
                id: '2-101221000',
                label: ' Habla mal [Grado: 2]',
              },
              {
                id: '2-101222000',
                label: ' Habla bien',
                children: [
                  {
                    id: '2-101222100',
                    label: ' Antecedentes de enfermedad neurológica [Grado: 3]',
                  },
                  {
                    id: '2-101222200',
                    label:
                      ' Sin antecedentes de enfermedad neurológica [Grado: 3]',
                  },
                ],
              },
            ],
          },
        ],
      },
    ],
  },
  {
    id: '2-102000000',
    label: '(Pediatrico) CUERPO EXTRAÑO EN NARIZ',
    children: [
      {
        id: '2-102100000',
        label: ' Respira mal [Grado: 2]',
      },
      {
        id: '2-102200000',
        label: ' Respira bien',
        children: [
          {
            id: '2-102210000',
            label: ' Está sangrando [Grado: 2]',
          },
          {
            id: '2-102220000',
            label: ' No está sangrando [Grado: 3]',
          },
        ],
      },
    ],
  },
  {
    id: '2-103000000',
    label: '(Pediatrico) CUERPO EXTRAÑO EN OIDO',
    children: [
      {
        id: '2-103100000',
        label: ' Está sangrando [Grado: 2]',
      },
      {
        id: '2-103200000',
        label: ' No está sangrando',
      },
    ],
  },
  {
    id: '2-104000000',
    label: '(Pediatrico) CUERPO EXTRAÑO EN OJO',
    children: [
      {
        id: '2-104100000',
        label: ' Está con mucho dolor o irritación',
      },
      {
        id: '2-104200000',
        label: ' Está solamente con molestias leves [Grado: 3]',
      },
    ],
  },
  {
    id: '2-105000000',
    label: '(Pediatrico) EDEMAS EN MIEMBROS INFERIORES',
    children: [
      {
        id: '2-105100000',
        label: ' En un solo miembro',
        children: [
          {
            id: '2-105110000',
            label: ' Está azul o blanco [Grado: 2]',
          },
          {
            id: '2-105120000',
            label: ' No está azul ni blanco [Grado: 3]',
          },
        ],
      },
      {
        id: '2-105200000',
        label: ' En ambos miembros',
        children: [
          {
            id: '2-105210000',
            label: ' Respira mal [Grado: 2]',
          },
          {
            id: '2-105220000',
            label: ' Respira bien [Grado: 3]',
          },
        ],
      },
    ],
  },
  {
    id: '2-106000000',
    label: '(Pediatrico) IRRITACION OCULAR',
    children: [
      {
        id: '2-106100000',
        label: ' Tuvo traumatismo [Grado: 2]',
      },
      {
        id: '2-106200000',
        label: ' No tuvo traumatismo',
        children: [
          {
            id: '2-106210000',
            label: ' Le ingreso alguna sustancia irritativa [Grado: 2]',
          },
          {
            id: '2-106220000',
            label: ' No le ingreso sustancia irritativa [Grado: 3]',
          },
        ],
      },
    ],
  },
  {
    id: '2-107000000',
    label: '(Pediatrico) DOLOR DE ESPALDA/DOLOR DORSAL',
    children: [
      {
        id: '2-107100000',
        label: ' Tiene dolor con el movimiento [Grado: 3]',
      },
      {
        id: '2-107200000',
        label: ' No tiene dolor con el movimiento [Grado: 3]',
      },
    ],
  },
  {
    id: '2-108000000',
    label: '(Pediatrico) DOLOR DE MIEMBROS',
    children: [
      {
        id: '2-108100000',
        label: ' Presentó traumatismo',
        children: [
          {
            id: '2-108110000',
            label: ' Evidencia de fractura [Grado: 2]',
          },
          {
            id: '2-108120000',
            label: ' Sin evidencias de fractura',
            children: [
              {
                id: '2-108121000',
                label: ' Está sangrando [Grado: 2]',
              },
              {
                id: '2-108122000',
                label: ' No está sangrando [Grado: 3]',
              },
            ],
          },
        ],
      },
      {
        id: '2-108200000',
        label: ' No presentó traumatismo',
        children: [
          {
            id: '2-108210000',
            label: ' Está el miembro azul o blanco [Grado: 2]',
          },
          {
            id: '2-108220000',
            label: ' El miembro no está azul o blanco [Grado: 3]',
          },
        ],
      },
    ],
  },
  {
    id: '2-109000000',
    label: '(Pediatrico) DOLOR TESTICULAR',
    children: [
      {
        id: '2-109100000',
        label: ' Presentó traumatismo [Grado: 2]',
      },
      {
        id: '2-109200000',
        label: ' No presentó traumatismo',
        children: [
          {
            id: '2-109210000',
            label: ' Tiempo de evolución menor de 12 horas [Grado: 2]',
          },
          {
            id: '2-109220000',
            label: ' Tiempo de evolución mayor de 12 horas [Grado: 3]',
          },
        ],
      },
    ],
  },
  {
    id: '2-112000000',
    label: '(Pediatrico) DOLOR CORPORAL',
    children: [
      {
        id: '2-112100000',
        label: ' Tiene fiebre [Grado: 3]',
      },
      {
        id: '2-112200000',
        label: ' No tiene fiebre [Grado: 3]',
      },
    ],
  },
  {
    id: '2-113000000',
    label: '(Pediatrico) EMBARAZO PRIMER TRIMESTRE',
    children: [
      {
        id: '2-113100000',
        label: ' Tiene hemorragia genital o perdida de liquido [Grado: 2]',
      },
      {
        id: '2-113200000',
        label: ' No tiene hemorragia genital ni pérdida de líquido',
        children: [
          {
            id: '2-113210000',
            label: ' Tiene dolor abdominal [Grado: 2]',
          },
          {
            id: '2-113220000',
            label: ' No tiene dolor abdominal [Grado: 3]',
          },
        ],
      },
    ],
  },
  {
    id: '2-114000000',
    label: '(Pediatrico) ATRAGANTAMIENTO',
    children: [
      {
        id: '2-114100000',
        label: ' No puede hablar ni toser [Grado: 1]',
      },
      {
        id: '2-114200000',
        label: ' Puede hablar o toser [Grado: 2]',
      },
    ],
  },
  {
    id: '2-115000000',
    label: '(Pediatrico) CONTROL EVOLUTIVO',
    children: [
      {
        id: '2-115100000',
        label: ' CONTROL DE INFECCIÓN RESPIRATORIA [Grado: 3]',
      },
      {
        id: '2-115200000',
        label: ' CONTROL DE DIARREA O GASTROENTERITIS [Grado: 3]',
      },
      {
        id: '2-115300000',
        label: ' CONTROL DE ERUPTIVA [Grado: 3]',
      },
      {
        id: '2-115400000',
        label: ' CONTROL DE HIPERTENSION ARTERIAL [Grado: 3]',
      },
      {
        id: '2-115500000',
        label: ' CONTROL DE SINDROME FEBRIL [Grado: 3]',
      },
      {
        id: '2-115600000',
        label: ' CONTROL DE OTRA ENFERMEDAD [Grado: 3]',
      },
    ],
  },
  {
    id: '2-116000000',
    label: '(Pediatrico) LLANTO EN NIÑO',
    children: [
      {
        id: '2-116100000',
        label: ' Se pone azul y luego se recupera [Grado: 3]',
      },
      {
        id: '2-116200000',
        label: ' No se pone Azul',
        children: [
          {
            id: '2-116210000',
            label: ' Aparece Bruscamente y lo despierta [Grado: 3]',
          },
          {
            id: '2-116220000',
            label: ' NO apareció bruscamente',
            children: [
              {
                id: '2-116221000',
                label: ' Se calma al estar en brazos [Grado: 3]',
              },
              {
                id: '2-116222000',
                label: ' No se calma al estar en brazos [Grado: 3]',
              },
            ],
          },
        ],
      },
    ],
  },
  {
    id: '2-14000000',
    label: '(Pediatrico) CEFALEA',
    children: [
      {
        id: '2-14100000',
        label: ' Tuvo trauma de cráneo [Grado: 2]',
      },
      {
        id: '2-14200000',
        label: ' No tuvo trauma de craneo',
        children: [
          {
            id: '2-14210000',
            label: ' Tiene cambios de conducta o alt conciencia [Grado: 2]',
          },
          {
            id: '2-14220000',
            label: ' Sin cambios de conducta',
            children: [
              {
                id: '2-14221000',
                label: ' Tiene vómitos [Grado: 3]',
              },
              {
                id: '2-14222000',
                label: ' No tiene vómitos [Grado: 3]',
              },
            ],
          },
        ],
      },
    ],
  },
  {
    id: '2-16000000',
    label: '(Pediatrico) DEBILIDAD-DECAIMIENTO-PALIDEZ',
    children: [
      {
        id: '2-16100000',
        label: ' No está conciente [Grado: 1]',
      },
      {
        id: '2-16200000',
        label: ' Está conciente',
        children: [
          {
            id: '2-16210000',
            label: ' Respira mal [Grado: 2]',
          },
          {
            id: '2-16220000',
            label: ' Respira bien',
            children: [
              {
                id: '2-16221000',
                label: ' Hace menos de 60 minutos [Grado: 3]',
              },
              {
                id: '2-16222000',
                label: ' Hace más de 60 minutos',
                children: [
                  {
                    id: '2-16222100',
                    label: ' Tiene fiebre [Grado: 3]',
                  },
                  {
                    id: '2-16222200',
                    label: ' No tiene fiebre [Grado: 3]',
                  },
                ],
              },
            ],
          },
        ],
      },
    ],
  },
  {
    id: '2-18000000',
    label: '(Pediatrico) DISNEA',
    children: [
      {
        id: '2-18100000',
        label: ' Respira mal ahora',
        children: [
          {
            id: '2-18110000',
            label: ' Tiene alt. de la conciencia [Grado: 1]',
          },
          {
            id: '2-18120000',
            label: ' No tiene alt, de la conciencia',
            children: [
              {
                id: '2-18121000',
                label: ' Esta azulado o morado [Grado: 1]',
              },
              {
                id: '2-18122000',
                label: ' No está azul ni morado',
                children: [
                  {
                    id: '2-18122100',
                    label: ' Tiene 2 años o más',
                    children: [
                      {
                        id: '2-18122110',
                        label:
                          ' Tiene dificultad para hablar por la disnea [Grado: 2]',
                      },
                      {
                        id: '2-18122120',
                        label: ' La disnea no le dificulta hablar',
                      },
                      {
                        id: '2-18122210',
                        label:
                          ' Tiene dificultad para dormir o alimentarse [Grado: 2]',
                      },
                      {
                        id: '2-18122220',
                        label: ' No tiene dificultad para dormir o alimentarse',
                      },
                    ],
                  },
                  {
                    id: '2-18122200',
                    label: ' Tiene menos de dos años',
                    children: [
                      {
                        id: '2-18122110',
                        label:
                          ' Tiene dificultad para hablar por la disnea [Grado: 2]',
                      },
                      {
                        id: '2-18122120',
                        label: ' La disnea no le dificulta hablar',
                      },
                      {
                        id: '2-18122210',
                        label:
                          ' Tiene dificultad para dormir o alimentarse [Grado: 2]',
                      },
                      {
                        id: '2-18122220',
                        label: ' No tiene dificultad para dormir o alimentarse',
                      },
                    ],
                  },
                ],
              },
            ],
          },
        ],
      },
      {
        id: '2-18200000',
        label: ' Respira bien ahora',
        children: [
          {
            id: '2-18210000',
            label: ' Tiene tos o fiebre [Grado: 3]',
          },
          {
            id: '2-18220000',
            label: ' No tiene tos ni fiebre [Grado: 3]',
          },
        ],
      },
    ],
  },
  {
    id: '2-19000000',
    label: '(Pediatrico) DOLOR ABDOMINAL',
    children: [
      {
        id: '2-19100000',
        label: ' El dolor es en la parte superior del abdomen',
        children: [
          {
            id: '2-19110000',
            label: ' Tiene antecedentes de enfermedad cardiaca [Grado: 2]',
          },
          {
            id: '2-19120000',
            label: ' No tiene antecedentes de enfermedad cardiaca [Grado: 3]',
          },
        ],
      },
      {
        id: '2-19200000',
        label: ' El dolor no es en la parte superior del abdomen',
        children: [
          {
            id: '2-19210000',
            label: ' Tiene vómitos o diarrea [Grado: 3]',
          },
          {
            id: '2-19220000',
            label: ' No tiene vómitos o diarrea [Grado: 3]',
          },
        ],
      },
    ],
  },
  {
    id: '2-20000000',
    label: '(Pediatrico) DOLOR DE TORAX',
    children: [
      {
        id: '2-20100000',
        label: ' Tiene antecedentes cardiacos [Grado: 1]',
      },
      {
        id: '2-20200000',
        label: ' No tiene antecedentes de enfermedad cardiaca',
        children: [
          {
            id: '2-20210000',
            label: ' Tiene antecedentes de trauma de tórax [Grado: 2]',
          },
          {
            id: '2-20220000',
            label: ' Sin antecedentes de trauma de torax',
            children: [
              {
                id: '2-20221000',
                label: ' Tiene fiebre o tos [Grado: 3]',
              },
              {
                id: '2-20222000',
                label: ' No tiene fiebre ni tos [Grado: 3]',
              },
            ],
          },
        ],
      },
    ],
  },
  {
    id: '2-21000000',
    label: '(Pediatrico) DISARTRIA',
    children: [
      {
        id: '2-21100000',
        label: ' Comenzó hace menos de 6 hs o se desconoce el tiemp [Grado: 2]',
      },
      {
        id: '2-21200000',
        label: ' Hace más de 6 horas que comenzó',
        children: [
          {
            id: '2-21210000',
            label: ' Tiene dificultad para movilizar un miembro [Grado: 2]',
          },
          {
            id: '2-21220000',
            label: ' No tiene dificultad para movilizar un miembro [Grado: 3]',
          },
        ],
      },
    ],
  },
  {
    id: '2-22000000',
    label: '(Pediatrico) TRANSTORNO EN LA MICCION',
    children: [
      {
        id: '2-22100000',
        label: ' Tiene sonda',
        children: [
          {
            id: '2-22110000',
            label: ' Está obstruída',
          },
          {
            id: '2-22120000',
            label: ' No está obstruída',
            children: [
              {
                id: '2-22121000',
                label: ' Tiene dolor abdominal [Grado: 3]',
              },
              {
                id: '2-22122000',
                label: ' No tiene dolor abdominal',
                children: [
                  {
                    id: '2-22122100',
                    label: ' Tiene ardor uretral [Grado: 3]',
                  },
                  {
                    id: '2-22122200',
                    label: ' No tiene ardor uretral [Grado: 3]',
                  },
                ],
              },
            ],
          },
        ],
      },
      {
        id: '2-22200000',
        label: ' No tiene sonda',
        children: [
          {
            id: '2-22210000',
            label: ' Tiene dolor abdominal [Grado: 3]',
          },
          {
            id: '2-22220000',
            label: ' No tiene dolor abdominal [Grado: 3]',
          },
        ],
      },
    ],
  },
  {
    id: '2-23000000',
    label: '(Pediatrico) ERUPCION CUTANEA',
    children: [
      {
        id: '2-23100000',
        label: ' Tiene dificultad para respirar [Grado: 1]',
      },
      {
        id: '2-23200000',
        label: ' Sin dificultad respiratoria',
        children: [
          {
            id: '2-23210000',
            label: ' Tiene hinchada cara o lengua [Grado: 2]',
          },
          {
            id: '2-23220000',
            label: ' NO hinchada cara ni lengua',
            children: [
              {
                id: '2-23221000',
                label: ' Tiene ronchas en la piel [Grado: 3]',
              },
              {
                id: '2-23222000',
                label: ' No tiene ronchas en la piel',
                children: [
                  {
                    id: '2-23222100',
                    label: ' Lo picó algún insecto [Grado: 3]',
                  },
                  {
                    id: '2-23222200',
                    label: ' No lo picó ningún insecto [Grado: 3]',
                  },
                ],
              },
            ],
          },
        ],
      },
    ],
  },
  {
    id: '2-24000000',
    label: '(Pediatrico) ELECTROCUCION',
    children: [
      {
        id: '2-24100000',
        label: ' No está conciente [Grado: 1]',
      },
      {
        id: '2-24200000',
        label: ' Está conciente',
        children: [
          {
            id: '2-24210000',
            label: ' Respira mal [Grado: 1]',
          },
          {
            id: '2-24220000',
            label: ' Respira bien [Grado: 2]',
          },
        ],
      },
    ],
  },
  {
    id: '2-28000000',
    label: '(Pediatrico) HEMORRAGIAS',
    children: [
      {
        id: '2-28100000',
        label: ' No está conciente [Grado: 1]',
      },
      {
        id: '2-28200000',
        label: ' Está conciente',
        children: [
          {
            id: '2-28210000',
            label: ' Respira mal [Grado: 1]',
          },
          {
            id: '2-28220000',
            label: ' Respira bien',
            children: [
              {
                id: '2-28221000',
                label: ' Está sudoroso [Grado: 2]',
              },
              {
                id: '2-28222000',
                label: ' No está sudoroso',
                children: [
                  {
                    id: '2-28222100',
                    label: ' Vómitos con sangre [Grado: 2]',
                    children: [
                      {
                        id: '2-28222210',
                        label: ' Sangrado abundante [Grado: 2]',
                        children: [
                          {
                            id: '2-28222421',
                            label: ' Primer o segundo semestre [Grado: 2]',
                          },
                          {
                            id: '2-28222422',
                            label: ' Tercer trimestre [Grado: 2]',
                          },
                        ],
                      },
                      {
                        id: '2-28222220',
                        label: ' Sangrado escaso [Grado: 3]',
                        children: [
                          {
                            id: '2-28222421',
                            label: ' Primer o segundo semestre [Grado: 2]',
                          },
                          {
                            id: '2-28222422',
                            label: ' Tercer trimestre [Grado: 2]',
                          },
                        ],
                      },
                      {
                        id: '2-28222410',
                        label: ' Sin embarazo [Grado: 3]',
                        children: [
                          {
                            id: '2-28222421',
                            label: ' Primer o segundo semestre [Grado: 2]',
                          },
                          {
                            id: '2-28222422',
                            label: ' Tercer trimestre [Grado: 2]',
                          },
                        ],
                      },
                      {
                        id: '2-28222420',
                        label: ' Con embarazo',
                        children: [
                          {
                            id: '2-28222421',
                            label: ' Primer o segundo semestre [Grado: 2]',
                          },
                          {
                            id: '2-28222422',
                            label: ' Tercer trimestre [Grado: 2]',
                          },
                        ],
                      },
                      {
                        id: '2-28222510',
                        label: ' Tiene dificultad respiratoria [Grado: 2]',
                        children: [
                          {
                            id: '2-28222421',
                            label: ' Primer o segundo semestre [Grado: 2]',
                          },
                          {
                            id: '2-28222422',
                            label: ' Tercer trimestre [Grado: 2]',
                          },
                        ],
                      },
                      {
                        id: '2-28222520',
                        label: ' No tiene dificultad respiratoria [Grado: 3]',
                        children: [
                          {
                            id: '2-28222421',
                            label: ' Primer o segundo semestre [Grado: 2]',
                          },
                          {
                            id: '2-28222422',
                            label: ' Tercer trimestre [Grado: 2]',
                          },
                        ],
                      },
                      {
                        id: '2-28222610',
                        label: ' Tuvo traumatismo [Grado: 2]',
                        children: [
                          {
                            id: '2-28222421',
                            label: ' Primer o segundo semestre [Grado: 2]',
                          },
                          {
                            id: '2-28222422',
                            label: ' Tercer trimestre [Grado: 2]',
                          },
                        ],
                      },
                      {
                        id: '2-28222620',
                        label: ' No tuvo traumatismo [Grado: 3]',
                        children: [
                          {
                            id: '2-28222421',
                            label: ' Primer o segundo semestre [Grado: 2]',
                          },
                          {
                            id: '2-28222422',
                            label: ' Tercer trimestre [Grado: 2]',
                          },
                        ],
                      },
                    ],
                  },
                  {
                    id: '2-28222200',
                    label: ' Materia fecal con sangre',
                    children: [
                      {
                        id: '2-28222210',
                        label: ' Sangrado abundante [Grado: 2]',
                        children: [
                          {
                            id: '2-28222421',
                            label: ' Primer o segundo semestre [Grado: 2]',
                          },
                          {
                            id: '2-28222422',
                            label: ' Tercer trimestre [Grado: 2]',
                          },
                        ],
                      },
                      {
                        id: '2-28222220',
                        label: ' Sangrado escaso [Grado: 3]',
                        children: [
                          {
                            id: '2-28222421',
                            label: ' Primer o segundo semestre [Grado: 2]',
                          },
                          {
                            id: '2-28222422',
                            label: ' Tercer trimestre [Grado: 2]',
                          },
                        ],
                      },
                      {
                        id: '2-28222410',
                        label: ' Sin embarazo [Grado: 3]',
                        children: [
                          {
                            id: '2-28222421',
                            label: ' Primer o segundo semestre [Grado: 2]',
                          },
                          {
                            id: '2-28222422',
                            label: ' Tercer trimestre [Grado: 2]',
                          },
                        ],
                      },
                      {
                        id: '2-28222420',
                        label: ' Con embarazo',
                        children: [
                          {
                            id: '2-28222421',
                            label: ' Primer o segundo semestre [Grado: 2]',
                          },
                          {
                            id: '2-28222422',
                            label: ' Tercer trimestre [Grado: 2]',
                          },
                        ],
                      },
                      {
                        id: '2-28222510',
                        label: ' Tiene dificultad respiratoria [Grado: 2]',
                        children: [
                          {
                            id: '2-28222421',
                            label: ' Primer o segundo semestre [Grado: 2]',
                          },
                          {
                            id: '2-28222422',
                            label: ' Tercer trimestre [Grado: 2]',
                          },
                        ],
                      },
                      {
                        id: '2-28222520',
                        label: ' No tiene dificultad respiratoria [Grado: 3]',
                        children: [
                          {
                            id: '2-28222421',
                            label: ' Primer o segundo semestre [Grado: 2]',
                          },
                          {
                            id: '2-28222422',
                            label: ' Tercer trimestre [Grado: 2]',
                          },
                        ],
                      },
                      {
                        id: '2-28222610',
                        label: ' Tuvo traumatismo [Grado: 2]',
                        children: [
                          {
                            id: '2-28222421',
                            label: ' Primer o segundo semestre [Grado: 2]',
                          },
                          {
                            id: '2-28222422',
                            label: ' Tercer trimestre [Grado: 2]',
                          },
                        ],
                      },
                      {
                        id: '2-28222620',
                        label: ' No tuvo traumatismo [Grado: 3]',
                        children: [
                          {
                            id: '2-28222421',
                            label: ' Primer o segundo semestre [Grado: 2]',
                          },
                          {
                            id: '2-28222422',
                            label: ' Tercer trimestre [Grado: 2]',
                          },
                        ],
                      },
                    ],
                  },
                  {
                    id: '2-28222300',
                    label: ' Orina con sangre [Grado: 3]',
                    children: [
                      {
                        id: '2-28222210',
                        label: ' Sangrado abundante [Grado: 2]',
                        children: [
                          {
                            id: '2-28222421',
                            label: ' Primer o segundo semestre [Grado: 2]',
                          },
                          {
                            id: '2-28222422',
                            label: ' Tercer trimestre [Grado: 2]',
                          },
                        ],
                      },
                      {
                        id: '2-28222220',
                        label: ' Sangrado escaso [Grado: 3]',
                        children: [
                          {
                            id: '2-28222421',
                            label: ' Primer o segundo semestre [Grado: 2]',
                          },
                          {
                            id: '2-28222422',
                            label: ' Tercer trimestre [Grado: 2]',
                          },
                        ],
                      },
                      {
                        id: '2-28222410',
                        label: ' Sin embarazo [Grado: 3]',
                        children: [
                          {
                            id: '2-28222421',
                            label: ' Primer o segundo semestre [Grado: 2]',
                          },
                          {
                            id: '2-28222422',
                            label: ' Tercer trimestre [Grado: 2]',
                          },
                        ],
                      },
                      {
                        id: '2-28222420',
                        label: ' Con embarazo',
                        children: [
                          {
                            id: '2-28222421',
                            label: ' Primer o segundo semestre [Grado: 2]',
                          },
                          {
                            id: '2-28222422',
                            label: ' Tercer trimestre [Grado: 2]',
                          },
                        ],
                      },
                      {
                        id: '2-28222510',
                        label: ' Tiene dificultad respiratoria [Grado: 2]',
                        children: [
                          {
                            id: '2-28222421',
                            label: ' Primer o segundo semestre [Grado: 2]',
                          },
                          {
                            id: '2-28222422',
                            label: ' Tercer trimestre [Grado: 2]',
                          },
                        ],
                      },
                      {
                        id: '2-28222520',
                        label: ' No tiene dificultad respiratoria [Grado: 3]',
                        children: [
                          {
                            id: '2-28222421',
                            label: ' Primer o segundo semestre [Grado: 2]',
                          },
                          {
                            id: '2-28222422',
                            label: ' Tercer trimestre [Grado: 2]',
                          },
                        ],
                      },
                      {
                        id: '2-28222610',
                        label: ' Tuvo traumatismo [Grado: 2]',
                        children: [
                          {
                            id: '2-28222421',
                            label: ' Primer o segundo semestre [Grado: 2]',
                          },
                          {
                            id: '2-28222422',
                            label: ' Tercer trimestre [Grado: 2]',
                          },
                        ],
                      },
                      {
                        id: '2-28222620',
                        label: ' No tuvo traumatismo [Grado: 3]',
                        children: [
                          {
                            id: '2-28222421',
                            label: ' Primer o segundo semestre [Grado: 2]',
                          },
                          {
                            id: '2-28222422',
                            label: ' Tercer trimestre [Grado: 2]',
                          },
                        ],
                      },
                    ],
                  },
                  {
                    id: '2-28222400',
                    label: ' Sangrado ginecológico',
                    children: [
                      {
                        id: '2-28222210',
                        label: ' Sangrado abundante [Grado: 2]',
                        children: [
                          {
                            id: '2-28222421',
                            label: ' Primer o segundo semestre [Grado: 2]',
                          },
                          {
                            id: '2-28222422',
                            label: ' Tercer trimestre [Grado: 2]',
                          },
                        ],
                      },
                      {
                        id: '2-28222220',
                        label: ' Sangrado escaso [Grado: 3]',
                        children: [
                          {
                            id: '2-28222421',
                            label: ' Primer o segundo semestre [Grado: 2]',
                          },
                          {
                            id: '2-28222422',
                            label: ' Tercer trimestre [Grado: 2]',
                          },
                        ],
                      },
                      {
                        id: '2-28222410',
                        label: ' Sin embarazo [Grado: 3]',
                        children: [
                          {
                            id: '2-28222421',
                            label: ' Primer o segundo semestre [Grado: 2]',
                          },
                          {
                            id: '2-28222422',
                            label: ' Tercer trimestre [Grado: 2]',
                          },
                        ],
                      },
                      {
                        id: '2-28222420',
                        label: ' Con embarazo',
                        children: [
                          {
                            id: '2-28222421',
                            label: ' Primer o segundo semestre [Grado: 2]',
                          },
                          {
                            id: '2-28222422',
                            label: ' Tercer trimestre [Grado: 2]',
                          },
                        ],
                      },
                      {
                        id: '2-28222510',
                        label: ' Tiene dificultad respiratoria [Grado: 2]',
                        children: [
                          {
                            id: '2-28222421',
                            label: ' Primer o segundo semestre [Grado: 2]',
                          },
                          {
                            id: '2-28222422',
                            label: ' Tercer trimestre [Grado: 2]',
                          },
                        ],
                      },
                      {
                        id: '2-28222520',
                        label: ' No tiene dificultad respiratoria [Grado: 3]',
                        children: [
                          {
                            id: '2-28222421',
                            label: ' Primer o segundo semestre [Grado: 2]',
                          },
                          {
                            id: '2-28222422',
                            label: ' Tercer trimestre [Grado: 2]',
                          },
                        ],
                      },
                      {
                        id: '2-28222610',
                        label: ' Tuvo traumatismo [Grado: 2]',
                        children: [
                          {
                            id: '2-28222421',
                            label: ' Primer o segundo semestre [Grado: 2]',
                          },
                          {
                            id: '2-28222422',
                            label: ' Tercer trimestre [Grado: 2]',
                          },
                        ],
                      },
                      {
                        id: '2-28222620',
                        label: ' No tuvo traumatismo [Grado: 3]',
                        children: [
                          {
                            id: '2-28222421',
                            label: ' Primer o segundo semestre [Grado: 2]',
                          },
                          {
                            id: '2-28222422',
                            label: ' Tercer trimestre [Grado: 2]',
                          },
                        ],
                      },
                    ],
                  },
                  {
                    id: '2-28222500',
                    label: ' Tos con sangre',
                    children: [
                      {
                        id: '2-28222210',
                        label: ' Sangrado abundante [Grado: 2]',
                        children: [
                          {
                            id: '2-28222421',
                            label: ' Primer o segundo semestre [Grado: 2]',
                          },
                          {
                            id: '2-28222422',
                            label: ' Tercer trimestre [Grado: 2]',
                          },
                        ],
                      },
                      {
                        id: '2-28222220',
                        label: ' Sangrado escaso [Grado: 3]',
                        children: [
                          {
                            id: '2-28222421',
                            label: ' Primer o segundo semestre [Grado: 2]',
                          },
                          {
                            id: '2-28222422',
                            label: ' Tercer trimestre [Grado: 2]',
                          },
                        ],
                      },
                      {
                        id: '2-28222410',
                        label: ' Sin embarazo [Grado: 3]',
                        children: [
                          {
                            id: '2-28222421',
                            label: ' Primer o segundo semestre [Grado: 2]',
                          },
                          {
                            id: '2-28222422',
                            label: ' Tercer trimestre [Grado: 2]',
                          },
                        ],
                      },
                      {
                        id: '2-28222420',
                        label: ' Con embarazo',
                        children: [
                          {
                            id: '2-28222421',
                            label: ' Primer o segundo semestre [Grado: 2]',
                          },
                          {
                            id: '2-28222422',
                            label: ' Tercer trimestre [Grado: 2]',
                          },
                        ],
                      },
                      {
                        id: '2-28222510',
                        label: ' Tiene dificultad respiratoria [Grado: 2]',
                        children: [
                          {
                            id: '2-28222421',
                            label: ' Primer o segundo semestre [Grado: 2]',
                          },
                          {
                            id: '2-28222422',
                            label: ' Tercer trimestre [Grado: 2]',
                          },
                        ],
                      },
                      {
                        id: '2-28222520',
                        label: ' No tiene dificultad respiratoria [Grado: 3]',
                        children: [
                          {
                            id: '2-28222421',
                            label: ' Primer o segundo semestre [Grado: 2]',
                          },
                          {
                            id: '2-28222422',
                            label: ' Tercer trimestre [Grado: 2]',
                          },
                        ],
                      },
                      {
                        id: '2-28222610',
                        label: ' Tuvo traumatismo [Grado: 2]',
                        children: [
                          {
                            id: '2-28222421',
                            label: ' Primer o segundo semestre [Grado: 2]',
                          },
                          {
                            id: '2-28222422',
                            label: ' Tercer trimestre [Grado: 2]',
                          },
                        ],
                      },
                      {
                        id: '2-28222620',
                        label: ' No tuvo traumatismo [Grado: 3]',
                        children: [
                          {
                            id: '2-28222421',
                            label: ' Primer o segundo semestre [Grado: 2]',
                          },
                          {
                            id: '2-28222422',
                            label: ' Tercer trimestre [Grado: 2]',
                          },
                        ],
                      },
                    ],
                  },
                  {
                    id: '2-28222600',
                    label: ' Sangra por nariz',
                    children: [
                      {
                        id: '2-28222210',
                        label: ' Sangrado abundante [Grado: 2]',
                        children: [
                          {
                            id: '2-28222421',
                            label: ' Primer o segundo semestre [Grado: 2]',
                          },
                          {
                            id: '2-28222422',
                            label: ' Tercer trimestre [Grado: 2]',
                          },
                        ],
                      },
                      {
                        id: '2-28222220',
                        label: ' Sangrado escaso [Grado: 3]',
                        children: [
                          {
                            id: '2-28222421',
                            label: ' Primer o segundo semestre [Grado: 2]',
                          },
                          {
                            id: '2-28222422',
                            label: ' Tercer trimestre [Grado: 2]',
                          },
                        ],
                      },
                      {
                        id: '2-28222410',
                        label: ' Sin embarazo [Grado: 3]',
                        children: [
                          {
                            id: '2-28222421',
                            label: ' Primer o segundo semestre [Grado: 2]',
                          },
                          {
                            id: '2-28222422',
                            label: ' Tercer trimestre [Grado: 2]',
                          },
                        ],
                      },
                      {
                        id: '2-28222420',
                        label: ' Con embarazo',
                        children: [
                          {
                            id: '2-28222421',
                            label: ' Primer o segundo semestre [Grado: 2]',
                          },
                          {
                            id: '2-28222422',
                            label: ' Tercer trimestre [Grado: 2]',
                          },
                        ],
                      },
                      {
                        id: '2-28222510',
                        label: ' Tiene dificultad respiratoria [Grado: 2]',
                        children: [
                          {
                            id: '2-28222421',
                            label: ' Primer o segundo semestre [Grado: 2]',
                          },
                          {
                            id: '2-28222422',
                            label: ' Tercer trimestre [Grado: 2]',
                          },
                        ],
                      },
                      {
                        id: '2-28222520',
                        label: ' No tiene dificultad respiratoria [Grado: 3]',
                        children: [
                          {
                            id: '2-28222421',
                            label: ' Primer o segundo semestre [Grado: 2]',
                          },
                          {
                            id: '2-28222422',
                            label: ' Tercer trimestre [Grado: 2]',
                          },
                        ],
                      },
                      {
                        id: '2-28222610',
                        label: ' Tuvo traumatismo [Grado: 2]',
                        children: [
                          {
                            id: '2-28222421',
                            label: ' Primer o segundo semestre [Grado: 2]',
                          },
                          {
                            id: '2-28222422',
                            label: ' Tercer trimestre [Grado: 2]',
                          },
                        ],
                      },
                      {
                        id: '2-28222620',
                        label: ' No tuvo traumatismo [Grado: 3]',
                        children: [
                          {
                            id: '2-28222421',
                            label: ' Primer o segundo semestre [Grado: 2]',
                          },
                          {
                            id: '2-28222422',
                            label: ' Tercer trimestre [Grado: 2]',
                          },
                        ],
                      },
                    ],
                  },
                  {
                    id: '2-28222700',
                    label: ' Se desconoce por donde sangra [Grado: 2]',
                    children: [
                      {
                        id: '2-28222210',
                        label: ' Sangrado abundante [Grado: 2]',
                        children: [
                          {
                            id: '2-28222421',
                            label: ' Primer o segundo semestre [Grado: 2]',
                          },
                          {
                            id: '2-28222422',
                            label: ' Tercer trimestre [Grado: 2]',
                          },
                        ],
                      },
                      {
                        id: '2-28222220',
                        label: ' Sangrado escaso [Grado: 3]',
                        children: [
                          {
                            id: '2-28222421',
                            label: ' Primer o segundo semestre [Grado: 2]',
                          },
                          {
                            id: '2-28222422',
                            label: ' Tercer trimestre [Grado: 2]',
                          },
                        ],
                      },
                      {
                        id: '2-28222410',
                        label: ' Sin embarazo [Grado: 3]',
                        children: [
                          {
                            id: '2-28222421',
                            label: ' Primer o segundo semestre [Grado: 2]',
                          },
                          {
                            id: '2-28222422',
                            label: ' Tercer trimestre [Grado: 2]',
                          },
                        ],
                      },
                      {
                        id: '2-28222420',
                        label: ' Con embarazo',
                        children: [
                          {
                            id: '2-28222421',
                            label: ' Primer o segundo semestre [Grado: 2]',
                          },
                          {
                            id: '2-28222422',
                            label: ' Tercer trimestre [Grado: 2]',
                          },
                        ],
                      },
                      {
                        id: '2-28222510',
                        label: ' Tiene dificultad respiratoria [Grado: 2]',
                        children: [
                          {
                            id: '2-28222421',
                            label: ' Primer o segundo semestre [Grado: 2]',
                          },
                          {
                            id: '2-28222422',
                            label: ' Tercer trimestre [Grado: 2]',
                          },
                        ],
                      },
                      {
                        id: '2-28222520',
                        label: ' No tiene dificultad respiratoria [Grado: 3]',
                        children: [
                          {
                            id: '2-28222421',
                            label: ' Primer o segundo semestre [Grado: 2]',
                          },
                          {
                            id: '2-28222422',
                            label: ' Tercer trimestre [Grado: 2]',
                          },
                        ],
                      },
                      {
                        id: '2-28222610',
                        label: ' Tuvo traumatismo [Grado: 2]',
                        children: [
                          {
                            id: '2-28222421',
                            label: ' Primer o segundo semestre [Grado: 2]',
                          },
                          {
                            id: '2-28222422',
                            label: ' Tercer trimestre [Grado: 2]',
                          },
                        ],
                      },
                      {
                        id: '2-28222620',
                        label: ' No tuvo traumatismo [Grado: 3]',
                        children: [
                          {
                            id: '2-28222421',
                            label: ' Primer o segundo semestre [Grado: 2]',
                          },
                          {
                            id: '2-28222422',
                            label: ' Tercer trimestre [Grado: 2]',
                          },
                        ],
                      },
                    ],
                  },
                ],
              },
            ],
          },
        ],
      },
    ],
  },
  {
    id: '2-29000000',
    label: '(Pediatrico) HIPERTENSION ARTERIAL',
    children: [
      {
        id: '2-29100000',
        label: ' Dificultad para hablar [Grado: 2]',
      },
      {
        id: '2-29200000',
        label: ' Sin dificultad para hablar',
        children: [
          {
            id: '2-29210000',
            label: ' Cefalea [Grado: 3]',
          },
          {
            id: '2-29220000',
            label: ' Sin cefalea ni otros síntomas [Grado: 3]',
          },
        ],
      },
    ],
  },
  {
    id: '2-30000000',
    label: '(Pediatrico) HIPOTENSION ARTERIAL (TA menor 90 mmHg)',
    children: [
      {
        id: '2-30100000',
        label: ' Tiene dolor de pecho [Grado: 2]',
      },
      {
        id: '2-30200000',
        label: ' No tiene dolor de pecho',
        children: [
          {
            id: '2-30210000',
            label: ' Esta sudoroso',
          },
          {
            id: '2-30220000',
            label: ' NO está sudoroso',
            children: [
              {
                id: '2-30221000',
                label: ' No tiene síntomas específicos [Grado: 3]',
              },
            ],
          },
        ],
      },
    ],
  },
  {
    id: '2-32000000',
    label: '(Pediatrico) INCONTINENCIA DE ESFINTERES',
    children: [
      {
        id: '2-32100000',
        label: ' Tuvo convulsiones [Grado: 2]',
      },
      {
        id: '2-32200000',
        label: ' No tuvo convulsiones [Grado: 3]',
      },
    ],
  },
  {
    id: '2-33000000',
    label: '(Pediatrico) INTOXICACION POR GASES TOXICOS O DROGAS',
    children: [
      {
        id: '2-33100000',
        label: ' No está consciente [Grado: 1]',
      },
      {
        id: '2-33200000',
        label: ' Está consciente',
        children: [
          {
            id: '2-33210000',
            label: ' Respira mal [Grado: 1]',
          },
          {
            id: '2-33220000',
            label: ' Respira bien',
            children: [
              {
                id: '2-33221000',
                label: ' Ocurrió recién (menos de 2 horas) [Grado: 2]',
              },
              {
                id: '2-33222000',
                label: ' No ocurrió recién (más de 2 horas)',
                children: [
                  {
                    id: '2-33222100',
                    label: ' Tiene náuseas, vómitos o cefalea [Grado: 2]',
                  },
                  {
                    id: '2-33222200',
                    label: ' No tiene náuseas, vómitos ni cefalea',
                  },
                ],
              },
            ],
          },
        ],
      },
    ],
  },
  {
    id: '2-34000000',
    label: '(Pediatrico) LUMBALGIA',
    children: [
      {
        id: '2-34100000',
        label: ' Antecedentes de cólico renal',
        children: [
          {
            id: '2-34110000',
            label: ' Está cursando un cólico renal [Grado: 2]',
          },
          {
            id: '2-34120000',
            label: ' No está cursando un cólico renal [Grado: 3]',
          },
        ],
      },
      {
        id: '2-34200000',
        label: ' No tiene antecedentes de cólico renal [Grado: 3]',
      },
    ],
  },
  {
    id: '2-35000000',
    label: '(Pediatrico) MAREOS',
    children: [
      {
        id: '2-35100000',
        label: ' Estuvo mucho tiempo parado [Grado: 3]',
      },
      {
        id: '2-35200000',
        label: ' No estuvo mucho tiempo parado',
        children: [
          {
            id: '2-35210000',
            label: ' Está en ayunas [Grado: 3]',
          },
          {
            id: '2-35220000',
            label: ' No está en ayunas [Grado: 3]',
          },
        ],
      },
    ],
  },
  {
    id: '2-36000000',
    label: '(Pediatrico) MORDEDURA DE...',
    children: [
      {
        id: '2-36100000',
        label: ' Sangra mucho [Grado: 1]',
      },
      {
        id: '2-36200000',
        label: ' No sangra mucho',
        children: [
          {
            id: '2-36210000',
            label: ' Lesiones múltiples y/o en cara [Grado: 2]',
          },
          {
            id: '2-36220000',
            label: ' Sin lesiones múltiples o cara [Grado: 3]',
          },
        ],
      },
    ],
  },
  {
    id: '2-37000000',
    label: '(Pediatrico) NAUSEAS-VOMITOS',
    children: [
      {
        id: '2-37100000',
        label: ' Tiene vómitos con sangre [Grado: 2]',
      },
      {
        id: '2-37200000',
        label: ' No tiene vómitos con sangre',
        children: [
          {
            id: '2-37210000',
            label: ' Tuvo traumatismo de cráneo [Grado: 2]',
          },
          {
            id: '2-37220000',
            label: ' No tuvo traumatismo de cráneo',
            children: [
              {
                id: '2-37221000',
                label: ' Tiene dolor abdominal [Grado: 3]',
              },
              {
                id: '2-37222000',
                label: ' No tiene dolor abdominal [Grado: 3]',
              },
            ],
          },
        ],
      },
    ],
  },
  {
    id: '2-38000000',
    label: '(Pediatrico) POLITRAUMATISMO',
    children: [
      {
        id: '2-38100000',
        label: ' No está consciente [Grado: 1]',
      },
      {
        id: '2-38200000',
        label: ' Está consciente',
        children: [
          {
            id: '2-38210000',
            label: ' No respira o respira mal [Grado: 1]',
          },
          {
            id: '2-38220000',
            label: ' Respira bien',
            children: [
              {
                id: '2-38221000',
                label: ' Tiene hemorragia evidente [Grado: 1]',
              },
              {
                id: '2-38222000',
                label: ' No tiene hemorragia evidente',
                children: [
                  {
                    id: '2-38222100',
                    label: ' Está caído en el suelo [Grado: 1]',
                  },
                  {
                    id: '2-38222200',
                    label: ' No está caído en el suelo [Grado: 2]',
                  },
                ],
              },
            ],
          },
        ],
      },
    ],
  },
  {
    id: '2-39000000',
    label: '(Pediatrico) PARESTESIAS (HORMIGUEOS)',
    children: [
      {
        id: '2-39100000',
        label: ' Tiene dificultad para mover el miembro [Grado: 3]',
      },
      {
        id: '2-39200000',
        label: ' No tiene dificultad para mover el miembro [Grado: 3]',
      },
    ],
  },
  {
    id: '2-42000000',
    label: '(Pediatrico) PROBLEMAS VINCULADOS CON LA DBT',
    children: [
      {
        id: '2-42100000',
        label: ' Tiene alteracion de la conciencia [Grado: 2]',
      },
      {
        id: '2-42200000',
        label: ' No tiene alteración de la conciencia',
        children: [
          {
            id: '2-42210000',
            label: ' Esta sudoroso o pálido [Grado: 2]',
          },
          {
            id: '2-42220000',
            label: ' No esta sudoroso ni pálido',
            children: [
              {
                id: '2-42221000',
                label: ' No se aplica insulina [Grado: 3]',
              },
              {
                id: '2-42222000',
                label: ' Se aplica insulina',
                children: [
                  {
                    id: '2-42222100',
                    label: ' Está hipoglucémico (menor a 70) [Grado: 1]',
                    children: [
                      {
                        id: '2-42222210',
                        label: ' Está hiperglucémico',
                        children: [
                          {
                            id: '2-42222211',
                            label: ' Mayor a 300 [Grado: 2]',
                          },
                          {
                            id: '2-42222212',
                            label: ' Menor a 300',
                          },
                        ],
                      },
                      {
                        id: '2-42222220',
                        label: ' No está hiperglucémico [Grado: 3]',
                        children: [
                          {
                            id: '2-42222211',
                            label: ' Mayor a 300 [Grado: 2]',
                          },
                          {
                            id: '2-42222212',
                            label: ' Menor a 300',
                          },
                        ],
                      },
                    ],
                  },
                  {
                    id: '2-42222200',
                    label: ' No está hipoglucémico',
                    children: [
                      {
                        id: '2-42222210',
                        label: ' Está hiperglucémico',
                        children: [
                          {
                            id: '2-42222211',
                            label: ' Mayor a 300 [Grado: 2]',
                          },
                          {
                            id: '2-42222212',
                            label: ' Menor a 300',
                          },
                        ],
                      },
                      {
                        id: '2-42222220',
                        label: ' No está hiperglucémico [Grado: 3]',
                        children: [
                          {
                            id: '2-42222211',
                            label: ' Mayor a 300 [Grado: 2]',
                          },
                          {
                            id: '2-42222212',
                            label: ' Menor a 300',
                          },
                        ],
                      },
                    ],
                  },
                ],
              },
            ],
          },
        ],
      },
    ],
  },
  {
    id: '2-43000000',
    label: '(Pediatrico) PICADURA DE...',
    children: [
      {
        id: '2-43100000',
        label: ' Respira mal [Grado: 1]',
      },
      {
        id: '2-43200000',
        label: ' Respira bien',
        children: [
          {
            id: '2-43210000',
            label: ' Tiene hinchada la cara o lengua [Grado: 2]',
          },
          {
            id: '2-43220000',
            label: ' No tiene hinchada cara ni lengua',
            children: [
              {
                id: '2-43221000',
                label: ' Antecedentes de edema de glotis',
              },
              {
                id: '2-43222000',
                label: ' Sin antecedentes de edema de glotis [Grado: 3]',
              },
            ],
          },
        ],
      },
    ],
  },
  {
    id: '2-44000000',
    label: '(Pediatrico) QUEMADURAS',
    children: [
      {
        id: '2-44100000',
        label: ' No está consciente [Grado: 1]',
      },
      {
        id: '2-44200000',
        label: ' Está consciente',
        children: [
          {
            id: '2-44210000',
            label: ' Respira mal [Grado: 1]',
          },
          {
            id: '2-44220000',
            label: ' Respira bien',
            children: [
              {
                id: '2-44221000',
                label: ' En cara-torso-abdomen o todo miembro [Grado: 1]',
              },
              {
                id: '2-44222000',
                label: ' No cara-torso-abdomen o todo miembro',
              },
            ],
          },
        ],
      },
    ],
  },
  {
    id: '2-5000000',
    label: '(Pediatrico) ARRITMIAS',
    children: [
      {
        id: '2-5100000',
        label: ' No está conciente [Grado: 1]',
      },
      {
        id: '2-5200000',
        label: ' Está conciente',
        children: [
          {
            id: '2-5210000',
            label: ' Tiene dolor de pecho [Grado: 1]',
          },
          {
            id: '2-5220000',
            label: ' No tiene dolor de pecho [Grado: 2]',
          },
        ],
      },
    ],
  },
  {
    id: '2-50000000',
    label: '(Pediatrico) TRAUMA DE TORAX',
    children: [
      {
        id: '2-50100000',
        label: ' Respira mal [Grado: 2]',
      },
      {
        id: '2-50200000',
        label: ' Respira bien',
        children: [
          {
            id: '2-50210000',
            label: ' Está sangrando [Grado: 2]',
          },
          {
            id: '2-50220000',
            label: ' No está sangrando',
            children: [
              {
                id: '2-50221000',
                label: ' Tiene dolor en tórax',
              },
              {
                id: '2-50222000',
                label: ' No tiene dolor en tórax [Grado: 3]',
              },
            ],
          },
        ],
      },
    ],
  },
  {
    id: '2-51000000',
    label: '(Pediatrico) TRAUMA DORSO LUMBAR',
    children: [
      {
        id: '2-51100000',
        label: ' Respira mal [Grado: 2]',
      },
      {
        id: '2-51200000',
        label: ' Respira bien',
        children: [
          {
            id: '2-51210000',
            label: ' Orinó con sangre [Grado: 2]',
          },
          {
            id: '2-51220000',
            label: ' No orinó con sangre',
            children: [
              {
                id: '2-51221000',
                label: ' No mueve bien las piernas [Grado: 2]',
              },
              {
                id: '2-51222000',
                label: ' Mueve bien las piernas [Grado: 3]',
              },
            ],
          },
        ],
      },
    ],
  },
  {
    id: '2-52000000',
    label: '(Pediatrico) TRAUMA DE ABDOMEN O PELVIS',
    children: [
      {
        id: '2-52100000',
        label: ' Está inconsciente [Grado: 1]',
      },
      {
        id: '2-52200000',
        label: ' Está consciente',
        children: [
          {
            id: '2-52210000',
            label: ' Está sangrando o sudoroso [Grado: 1]',
          },
          {
            id: '2-52220000',
            label: ' No está sangrando ni sudoroso',
            children: [
              {
                id: '2-52221000',
                label: ' No se moviliza [Grado: 2]',
              },
              {
                id: '2-52222000',
                label: ' Se moviliza',
                children: [
                  {
                    id: '2-52222100',
                    label: ' Tiene dolor abdominal',
                  },
                  {
                    id: '2-52222200',
                    label: ' No tiene dolor abdominal [Grado: 3]',
                  },
                ],
              },
            ],
          },
        ],
      },
    ],
  },
  {
    id: '2-53000000',
    label: '(Pediatrico) TRAUMATISMO FACIAL',
    children: [
      {
        id: '2-53100000',
        label: ' No está consciente [Grado: 1]',
      },
      {
        id: '2-53200000',
        label: ' Está consciente',
        children: [
          {
            id: '2-53210000',
            label: ' Respira mal [Grado: 2]',
          },
          {
            id: '2-53220000',
            label: ' Respira bien',
            children: [
              {
                id: '2-53221000',
                label: ' Está sangrando',
              },
              {
                id: '2-53222000',
                label: ' No está sangrando [Grado: 3]',
              },
            ],
          },
        ],
      },
    ],
  },
  {
    id: '2-54000000',
    label: '(Pediatrico) TRAUMATISMO DE MIEMBROS',
    children: [
      {
        id: '2-54100000',
        label: ' Tiene el miembro deformado o imposibilidad de move [Grado: 2]',
      },
      {
        id: '2-54200000',
        label: ' No tiene el miembro deformado y puede moverlo',
        children: [
          {
            id: '2-54210000',
            label: ' Está sangrando [Grado: 2]',
          },
          {
            id: '2-54220000',
            label: ' No está sangrando',
            children: [
              {
                id: '2-54221000',
                label: ' Tiene dolor',
              },
              {
                id: '2-54222000',
                label: ' No tiene dolor [Grado: 3]',
              },
            ],
          },
        ],
      },
    ],
  },
  {
    id: '2-55000000',
    label: '(Pediatrico) TRAUMATISMO DE CRANEO',
    children: [
      {
        id: '2-55100000',
        label: ' No esta consciente [Grado: 1]',
      },
      {
        id: '2-55200000',
        label: ' Esta consciente actualmente',
        children: [
          {
            id: '2-55210000',
            label: ' Cuando se golpeó tuvo pérdida conocimiento [Grado: 2]',
          },
          {
            id: '2-55220000',
            label: ' Cuando se golpeó no tuvo pérdida conocimiento',
            children: [
              {
                id: '2-55221000',
                label: ' Está sangrando [Grado: 2]',
              },
              {
                id: '2-55222000',
                label: ' No está sangrando',
                children: [
                  {
                    id: '2-55222100',
                    label: ' Tiene tendencia al sueño [Grado: 2]',
                    children: [
                      {
                        id: '2-55222210',
                        label: ' Tiene vómitos [Grado: 2]',
                        children: [
                          {
                            id: '2-55222221',
                            label: ' Tiene cambios de conducta [Grado: 2]',
                          },
                          {
                            id: '2-55222222',
                            label: ' No tiene cambios de conducta [Grado: 3]',
                          },
                        ],
                      },
                      {
                        id: '2-55222220',
                        label: ' NO tiene vómitos',
                        children: [
                          {
                            id: '2-55222221',
                            label: ' Tiene cambios de conducta [Grado: 2]',
                          },
                          {
                            id: '2-55222222',
                            label: ' No tiene cambios de conducta [Grado: 3]',
                          },
                        ],
                      },
                    ],
                  },
                  {
                    id: '2-55222200',
                    label: ' No tiene tendencia al sueño',
                    children: [
                      {
                        id: '2-55222210',
                        label: ' Tiene vómitos [Grado: 2]',
                        children: [
                          {
                            id: '2-55222221',
                            label: ' Tiene cambios de conducta [Grado: 2]',
                          },
                          {
                            id: '2-55222222',
                            label: ' No tiene cambios de conducta [Grado: 3]',
                          },
                        ],
                      },
                      {
                        id: '2-55222220',
                        label: ' NO tiene vómitos',
                        children: [
                          {
                            id: '2-55222221',
                            label: ' Tiene cambios de conducta [Grado: 2]',
                          },
                          {
                            id: '2-55222222',
                            label: ' No tiene cambios de conducta [Grado: 3]',
                          },
                        ],
                      },
                    ],
                  },
                ],
              },
            ],
          },
        ],
      },
    ],
  },
  {
    id: '2-56000000',
    label: '(Pediatrico) EMBARAZO A TERMINO',
    children: [
      {
        id: '2-56100000',
        label: ' El nino esta saliendo [Grado: 1]',
      },
      {
        id: '2-56200000',
        label: ' No esta saliendo',
        children: [
          {
            id: '2-56210000',
            label: ' Perdió sangre [Grado: 1]',
          },
          {
            id: '2-56220000',
            label: ' No perdió sangre',
            children: [
              {
                id: '2-56221000',
                label: ' Tiene contracciones',
                children: [
                  {
                    id: '2-56221100',
                    label: ' Primer embrazo',
                    children: [
                      {
                        id: '2-56221110',
                        label:
                          ' Contracciones cada 2 minutos o menos [Grado: 1]',
                      },
                      {
                        id: '2-56221120',
                        label:
                          ' Contracciones cada más de dos minutos [Grado: 2]',
                      },
                      {
                        id: '2-56221210',
                        label:
                          ' Contracciones cada 5 minutos o menos [Grado: 1]',
                      },
                      {
                        id: '2-56221220',
                        label:
                          ' Contracciones cada más de 5 minutos [Grado: 2]',
                      },
                    ],
                  },
                  {
                    id: '2-56221200',
                    label: ' Embarazos previos',
                    children: [
                      {
                        id: '2-56221110',
                        label:
                          ' Contracciones cada 2 minutos o menos [Grado: 1]',
                      },
                      {
                        id: '2-56221120',
                        label:
                          ' Contracciones cada más de dos minutos [Grado: 2]',
                      },
                      {
                        id: '2-56221210',
                        label:
                          ' Contracciones cada 5 minutos o menos [Grado: 1]',
                      },
                      {
                        id: '2-56221220',
                        label:
                          ' Contracciones cada más de 5 minutos [Grado: 2]',
                      },
                    ],
                  },
                ],
              },
              {
                id: '2-56222000',
                label: ' No tiene contracciones',
                children: [
                  {
                    id: '2-56222100',
                    label: ' Perdió líquido o rompió bolsa [Grado: 2]',
                  },
                  {
                    id: '2-56222200',
                    label: ' No perdió líquido ni rompió bolsa [Grado: 3]',
                  },
                ],
              },
            ],
          },
        ],
      },
    ],
  },
  {
    id: '2-57000000',
    label: '(Pediatrico) TEMBLOR',
    children: [
      {
        id: '2-57100000',
        label: ' No está lúcido [Grado: 1]',
      },
      {
        id: '2-57200000',
        label: ' Está lúcido',
        children: [
          {
            id: '2-57210000',
            label: ' Tiene fiebre [Grado: 3]',
          },
          {
            id: '2-57220000',
            label: ' No tiene fiebre',
            children: [
              {
                id: '2-57221000',
                label:
                  ' Tiene antecedentes de enfermedad de tiroides [Grado: 3]',
              },
              {
                id: '2-57222000',
                label:
                  ' No tiene antecedentes de enfermedad de tiroides [Grado: 3]',
              },
            ],
          },
        ],
      },
    ],
  },
  {
    id: '2-59000000',
    label: '(Pediatrico) PALPITACIONES',
    children: [
      {
        id: '2-59100000',
        label: ' Tiene fiebre [Grado: 3]',
      },
      {
        id: '2-59200000',
        label: ' No tiene fiebre',
        children: [
          {
            id: '2-59210000',
            label: ' Antecedentes de problemas en tiroides [Grado: 3]',
          },
          {
            id: '2-59220000',
            label: ' Sin antecedentes de problemas en tiroides',
            children: [
              {
                id: '2-59221000',
                label: ' Antecedentes de enfermedad cardiaca [Grado: 3]',
              },
              {
                id: '2-59222000',
                label: ' Sin antecedentes de enfermedad cardiaca [Grado: 3]',
              },
            ],
          },
        ],
      },
    ],
  },
  {
    id: '2-61000000',
    label: '(Pediatrico) GALENO EN QTH',
    children: [
      {
        id: '2-61100000',
        label: ' Requiere grado 1 [Grado: 1]',
      },
      {
        id: '2-61200000',
        label: ' Requiere grado 2 [Grado: 2]',
      },
      {
        id: '2-61300000',
        label: ' Requiere grado 3 [Grado: 3]',
      },
    ],
  },
  {
    id: '2-62000000',
    label: '(Pediatrico) HERIDA CORTANTE',
    children: [
      {
        id: '2-62100000',
        label: ' Con sangrado activo [Grado: 2]',
      },
      {
        id: '2-62200000',
        label: ' Sin sangrado activo',
      },
    ],
  },
  {
    id: '2-8000000',
    label: '(Pediatrico) CONVULSIONES',
    children: [
      {
        id: '2-8100000',
        label: ' Esta convulsionando ahora [Grado: 1]',
      },
      {
        id: '2-8200000',
        label: ' No esta convulsionado ahora',
        children: [
          {
            id: '2-8210000',
            label: ' No está conciente [Grado: 1]',
          },
          {
            id: '2-8220000',
            label: ' Está conciente',
            children: [
              {
                id: '2-8221000',
                label: ' Respira mal [Grado: 2]',
              },
              {
                id: '2-8222000',
                label: ' Respira bien',
              },
            ],
          },
        ],
      },
    ],
  },
  {
    id: '2-9000000',
    label: '(Pediatrico) TRASTORNOS DE CONDUCTA',
    children: [
      {
        id: '2-9100000',
        label: ' Está muy violento o agresivo [Grado: 2]',
      },
      {
        id: '2-9200000',
        label: ' No está violento o agresivo',
        children: [
          {
            id: '2-9210000',
            label: ' Está alcoholizado o consumió drogas [Grado: 2]',
          },
          {
            id: '2-9220000',
            label: ' No está alcoholizado ni consumió drogas',
            children: [
              {
                id: '2-9221000',
                label: ' Tuvo trauma de cráneo [Grado: 2]',
              },
              {
                id: '2-9222000',
                label: ' No tuvo trauma de cráneo [Grado: 3]',
              },
            ],
          },
        ],
      },
    ],
  },
  {
    id: '2-97000000',
    label: '(Pediatrico) PERDIDA DE CONOCIMIENTO',
    children: [
      {
        id: '2-97100000',
        label: ' No se recuperó [Grado: 1]',
      },
      {
        id: '2-97200000',
        label: ' Se recuperó',
        children: [
          {
            id: '2-97210000',
            label: ' Respira mal [Grado: 2]',
          },
          {
            id: '2-97220000',
            label: ' Respira bien',
            children: [
              {
                id: '2-97221000',
                label: ' Habla con dificultad [Grado: 2]',
              },
              {
                id: '2-97222000',
                label: ' Habla sin dificultad',
                children: [
                  {
                    id: '2-97222100',
                    label: ' Tuvo traumatismo [Grado: 1]',
                  },
                  {
                    id: '2-97222200',
                    label: ' No tuvo traumatismo',
                  },
                ],
              },
            ],
          },
        ],
      },
    ],
  },
]; // ,
