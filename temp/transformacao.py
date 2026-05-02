import json

dados = [
  {
    "id_erp": 10001,
    "nome": "PÉ FRENTE CAD BAMBOLÊ",
    "equipamentos": [
      3
    ],
    "tempo": 20,
    "setup": 3540,
    "codigo_barra": 10001
  },
  {
    "id_erp": 10002,
    "nome": "PÉ TRASEIRO CAD BAMBOLÊ",
    "equipamentos": [
      3
    ],
    "tempo": 20,
    "setup": 3540,
    "codigo_barra": 10002
  },
  {
    "id_erp": 10003,
    "nome": "TRAVESSA LAT.CAD BAMBOLÊ",
    "equipamentos": [
      2
    ],
    "tempo": 90,
    "setup": 3540,
    "codigo_barra": 10003
  },
  {
    "id_erp": 10004,
    "nome": "TRAVESSA TRASEIRA CAD. BAMBOLÊ",
    "equipamentos": [
      2
    ],
    "tempo": 120,
    "setup": 2100,
    "codigo_barra": 10004
  },
  {
    "id_erp": 10005,
    "nome": "TRAVESSA FRENTE CAD.BAMBOLÊ",
    "equipamentos": [
      2
    ],
    "tempo": 120,
    "setup": 2100,
    "codigo_barra": 10005
  },
  {
    "id_erp": 10006,
    "nome": "PÉ FRENTE CAD TRAPO",
    "equipamentos": [
      3
    ],
    "tempo": 23,
    "setup": 3540,
    "codigo_barra": 10006
  },
  {
    "id_erp": 10007,
    "nome": "PÉ TRASEIRO CAD TRAPO",
    "equipamentos": [
      3
    ],
    "tempo": 23,
    "setup": 3540,
    "codigo_barra": 10007
  },
  {
    "id_erp": 10008,
    "nome": "TRAVESSA LAT. CAD TRAPO",
    "equipamentos": [
      2
    ],
    "tempo": 25,
    "setup": 2100,
    "codigo_barra": 10008
  },
  {
    "id_erp": 10009,
    "nome": "TRAVESSA TRASEIRA CAD .TRAPO",
    "equipamentos": [
      2
    ],
    "tempo": 50,
    "setup": 2100,
    "codigo_barra": 10009
  },
  {
    "id_erp": 10010,
    "nome": "TRAVESSA FRENTE CAD TRAPO",
    "equipamentos": [
      2
    ],
    "tempo": 50,
    "setup": 2100,
    "codigo_barra": 10010
  },
  {
    "id_erp": 10704,
    "nome": "PE MAD DIANTEIRO P0014 430 X 50 X 32MM ESQUERDO - CADEIRA BARI/LINA",
    "equipamentos": [
      3
    ],
    "tempo": 15,
    "setup": 2100,
    "codigo_barra": 10704
  },
  {
    "id_erp": 11000,
    "nome": "TEMPO NA DJET - TESTE",
    "equipamentos": [
      3
    ],
    "tempo": 151,
    "setup": 6300,
    "codigo_barra": 11000
  },
  {
    "id_erp": 12000,
    "nome": "TEMPO NA JET - TESTE",
    "equipamentos": [
      2
    ],
    "tempo": 151,
    "setup": 2700,
    "codigo_barra": 12000
  },
  {
    "id_erp": 12291,
    "nome": "PE MAD TRASEIRO P0065 920 X 54 X 32MM ESQUERDO - CADEIRA LORENZA",
    "equipamentos": [
      2
    ],
    "tempo": 15,
    "setup": 2100,
    "codigo_barra": 12291
  },
  {
    "id_erp": 12292,
    "nome": "PE MAD DIANTEIRO P0006 430 X 45 X 45MM - CADEIRA LORENZA",
    "equipamentos": [
      2
    ],
    "tempo": 15,
    "setup": 2100,
    "codigo_barra": 12292
  },
  {
    "id_erp": 12295,
    "nome": "TRAVESSA MAD TRASEIRA T0037 410 X 45 X 26MM - CADEIRA LORENZA",
    "equipamentos": [
      2
    ],
    "tempo": 13,
    "setup": 2100,
    "codigo_barra": 12295
  },
  {
    "id_erp": 12296,
    "nome": "FRONTAL MAD  F0008 435 X 33 X 24MM - CADEIRA LORENZA",
    "equipamentos": [
      2
    ],
    "tempo": 28,
    "setup": 2100,
    "codigo_barra": 12296
  },
  {
    "id_erp": 12297,
    "nome": "TRAVESSA MAD T0139 410 X 33 X 24MM - CADEIRA LORENZA",
    "equipamentos": [
      2
    ],
    "tempo": 29,
    "setup": 2100,
    "codigo_barra": 12297
  },
  {
    "id_erp": 13000,
    "nome": "PROTÓTIPO DJET",
    "equipamentos": [
      3
    ],
    "tempo": 151,
    "setup": 14340,
    "codigo_barra": 13000
  },
  {
    "id_erp": 14000,
    "nome": "PROTÓTIPO JET",
    "equipamentos": [
      2
    ],
    "tempo": 60,
    "setup": 7140,
    "codigo_barra": 14000
  },
  {
    "id_erp": 14372,
    "nome": "FRONTAL MAD  F0006 430 X 50 X 28MM - CADEIRA PANTHEON",
    "equipamentos": [
      2
    ],
    "tempo": 13,
    "setup": 2100,
    "codigo_barra": 14372
  },
  {
    "id_erp": 14372,
    "nome": "FRONTAL MAD  F0006 430 X 50 X 28MM - CADEIRA PANTHEON",
    "equipamentos": [
      3
    ],
    "tempo": 9,
    "setup": 2100,
    "codigo_barra": 14372
  },
  {
    "id_erp": 14374,
    "nome": "ASA MAD A0005 435 X 50 X 28MM - CADEIRA PANTHEON/GOYA",
    "equipamentos": [
      3
    ],
    "tempo": 11,
    "setup": 2100,
    "codigo_barra": 14374
  },
  {
    "id_erp": 14430,
    "nome": "TRAVESSA MAD T0141 415 X 45 X 32MM ESQUERDA - CADEIRA LORENZA",
    "equipamentos": [
      2
    ],
    "tempo": 9,
    "setup": 2100,
    "codigo_barra": 14430
  },
  {
    "id_erp": 16960,
    "nome": "ASA MAD A0007 475 X 55 X 24MM ESQUERDA - CADEIRA CASSINA/LISBOA/ATENAS/LIANE/LONDRES/ORNATA/BIA/MARI",
    "equipamentos": [
      3
    ],
    "tempo": 11,
    "setup": 2100,
    "codigo_barra": 16960
  },
  {
    "id_erp": 16961,
    "nome": "PE MAD DIANTEIRO P0016 440 X 50 X 32MM ESQUERDO - CADEIRA CASSINA/ATENAS/LISBOA/LIANE/LONDRES/ORNATA/BIA/MARI",
    "equipamentos": [
      2
    ],
    "tempo": 12,
    "setup": 2100,
    "codigo_barra": 16961
  },
  {
    "id_erp": 18467,
    "nome": "FRONTAL MAD  F0003 450 X 45 X 50MM - CADEIRA CASSINA/ATENAS",
    "equipamentos": [
      2
    ],
    "tempo": 29,
    "setup": 2100,
    "codigo_barra": 18467
  },
  {
    "id_erp": 19152,
    "nome": "PE MAD TRASEIRO P0074 485 X 53 X 32MM ESQUERDO - CADEIRA PANTHEON/GOYA",
    "equipamentos": [
      3
    ],
    "tempo": 11,
    "setup": 2100,
    "codigo_barra": 19152
  },
  {
    "id_erp": 20264,
    "nome": "PE MAD TRASEIRO P0072 490 X 55 X 32MM ESQUERDO - CADEIRA NICE/IRIS/GALLA/AMBER/AMBER C/BRACO/NICE NOVA/IRIS NOVA",
    "equipamentos": [
      3
    ],
    "tempo": 11,
    "setup": 2100,
    "codigo_barra": 20264
  },
  {
    "id_erp": 20265,
    "nome": "PE MAD DIANTEIRO P0043 440 X 45 X 45MM - NICE/IRIS/GALLA/AMBER/AMBER C/BRACO/NICE NOVA/IRIS NOVA",
    "equipamentos": [
      2
    ],
    "tempo": 11,
    "setup": 2100,
    "codigo_barra": 20265
  },
  {
    "id_erp": 20265,
    "nome": "PE MAD DIANTEIRO P0043 440 X 45 X 45MM - NICE/IRIS/GALLA/AMBER/AMBER C/BRACO/NICE NOVA/IRIS NOVA",
    "equipamentos": [
      3
    ],
    "tempo": 12,
    "setup": 2100,
    "codigo_barra": 20265
  },
  {
    "id_erp": 20266,
    "nome": "PEGA MAD P0002 396 X 34 X 28MM - CADEIRA NICE/OLIVA/IRIS/ALBANI/LISBOA",
    "equipamentos": [
      2
    ],
    "tempo": 19,
    "setup": 2100,
    "codigo_barra": 20266
  },
  {
    "id_erp": 20266,
    "nome": "PEGA MAD P0002 396 X 34 X 28MM - CADEIRA NICE/OLIVA/IRIS/ALBANI/LISBOA",
    "equipamentos": [
      3
    ],
    "tempo": 13,
    "setup": 2100,
    "codigo_barra": 20266
  },
  {
    "id_erp": 20267,
    "nome": "ASA MAD A0009 535 X 52 X 24MM ESQUERDA - CADEIRA NICE/IRIS/NICE NOVA/IRIS NOVA/GALLA/AMBER",
    "equipamentos": [
      3
    ],
    "tempo": 11,
    "setup": 2100,
    "codigo_barra": 20267
  },
  {
    "id_erp": 21000,
    "nome": "PROTÓTIPO (NELSINHO)",
    "equipamentos": [
      2
    ],
    "tempo": 59,
    "setup": 7200,
    "codigo_barra": 21000
  },
  {
    "id_erp": 21539,
    "nome": "PE MAD TRASEIRO P0057 490 X 55 X 32MM ESQUERDO - CADEIRA CASSINA/ATENAS/LISBOA/LIANE/LONDRES/ORNATA/BIA/MARI",
    "equipamentos": [
      3
    ],
    "tempo": 14,
    "setup": 2100,
    "codigo_barra": 21539
  },
  {
    "id_erp": 22000,
    "nome": "PROTÓTIPO (NELSINHO)",
    "equipamentos": [
      3
    ],
    "tempo": 59,
    "setup": 5400,
    "codigo_barra": 22000
  },
  {
    "id_erp": 23304,
    "nome": "PE MAD DIANTEIRO P0004 430 X 45 X 45MM - CADEIRA ENNA",
    "equipamentos": [
      2
    ],
    "tempo": 11,
    "setup": 2100,
    "codigo_barra": 23304
  },
  {
    "id_erp": 23304,
    "nome": "PE MAD DIANTEIRO P0004 430 X 45 X 45MM - CADEIRA ENNA",
    "equipamentos": [
      3
    ],
    "tempo": 17,
    "setup": 2100,
    "codigo_barra": 23304
  },
  {
    "id_erp": 25751,
    "nome": "TRAVESSA MAD T0560 1405 X 70 X 32MM - MESA PRADES/TOLEDO",
    "equipamentos": [
      2
    ],
    "tempo": 62,
    "setup": 2100,
    "codigo_barra": 25751
  },
  {
    "id_erp": 25889,
    "nome": "PE MAD P0109 400 X  90 X  32MM - BANCO AZZURE",
    "equipamentos": [
      2
    ],
    "tempo": 16,
    "setup": 2100,
    "codigo_barra": 25889
  },
  {
    "id_erp": 25890,
    "nome": "TRAVESSA MAD T0137 1440 X 110 X 32MM - BANCO AZZURE",
    "equipamentos": [
      2
    ],
    "tempo": 22,
    "setup": 2100,
    "codigo_barra": 25890
  },
  {
    "id_erp": 25918,
    "nome": "PE MAD DIANTEIRO P0045 430 X 50 X 32MM ESQUERDO - CADEIRA AZZURE/CANNES",
    "equipamentos": [
      2
    ],
    "tempo": 11,
    "setup": 2100,
    "codigo_barra": 25918
  },
  {
    "id_erp": 25918,
    "nome": "PE MAD DIANTEIRO P0045 430 X 50 X 32MM ESQUERDO - CADEIRA AZZURE/CANNES",
    "equipamentos": [
      3
    ],
    "tempo": 14,
    "setup": 2100,
    "codigo_barra": 25918
  },
  {
    "id_erp": 25919,
    "nome": "PE MAD TRASEIRO P0049 435 X 50 X 32MM - CADEIRA AZZURE/CANNES",
    "equipamentos": [
      3
    ],
    "tempo": 9,
    "setup": 2100,
    "codigo_barra": 25919
  },
  {
    "id_erp": 25922,
    "nome": "TRAVESSA MAD LATERAL T0086 398 X 57 X 34MM - CADEIRA AZZURE/CANNES",
    "equipamentos": [
      2
    ],
    "tempo": 18,
    "setup": 2100,
    "codigo_barra": 25922
  },
  {
    "id_erp": 25923,
    "nome": "TRAVESSA MAD TRASEIRA T0047 345 X 57 X 36MM - CADEIRA AZZURE/CANNES",
    "equipamentos": [
      2
    ],
    "tempo": 24,
    "setup": 2100,
    "codigo_barra": 25923
  },
  {
    "id_erp": 25923,
    "nome": "TRAVESSA MAD TRASEIRA T0047 345 X 57 X 36MM - CADEIRA AZZURE/CANNES",
    "equipamentos": [
      3
    ],
    "tempo": 13,
    "setup": 2100,
    "codigo_barra": 25923
  },
  {
    "id_erp": 25926,
    "nome": "TRAVESSA MAD LATERAL T0118 330 X 34 X 25MM ESQUERD - CADEIRA AZZURE",
    "equipamentos": [
      2
    ],
    "tempo": 16,
    "setup": 2100,
    "codigo_barra": 25926
  },
  {
    "id_erp": 25926,
    "nome": "TRAVESSA MAD LATERAL T0118 330 X 34 X 25MM ESQUERD - CADEIRA AZZURE",
    "equipamentos": [
      3
    ],
    "tempo": 12,
    "setup": 2100,
    "codigo_barra": 25926
  },
  {
    "id_erp": 25969,
    "nome": "TRAVESSA MAD T0123 380 X 100 X 32MM - BANCO AZZURE",
    "equipamentos": [
      2
    ],
    "tempo": 30,
    "setup": 2100,
    "codigo_barra": 25969
  },
  {
    "id_erp": 27389,
    "nome": "ASA MAD A0003 548 X 50 X 24MM - CADEIRA GALLA/AMBER/AMBER C/BRACO",
    "equipamentos": [
      3
    ],
    "tempo": 10,
    "setup": 2100,
    "codigo_barra": 27389
  },
  {
    "id_erp": 27391,
    "nome": "TRAVESSA MAD TRASEIRA T0052 356 X 58 X 35MM - CADEIRA GALLA/AMBER/AMBER C/BRACO - LX",
    "equipamentos": [
      2
    ],
    "tempo": 13,
    "setup": 2100,
    "codigo_barra": 27391
  },
  {
    "id_erp": 27391,
    "nome": "TRAVESSA MAD TRASEIRA T0052 356 X 58 X 35MM - CADEIRA GALLA/AMBER/AMBER C/BRACO - LX",
    "equipamentos": [
      3
    ],
    "tempo": 11,
    "setup": 2100,
    "codigo_barra": 27391
  },
  {
    "id_erp": 27426,
    "nome": "PEGA MAD P0003 400 X 34 X 28MM - CADEIRA ELLEN/MEG/LAIS/NAOMI/VIVI",
    "equipamentos": [
      2
    ],
    "tempo": 19,
    "setup": 2100,
    "codigo_barra": 27426
  },
  {
    "id_erp": 27426,
    "nome": "PEGA MAD P0003 400 X 34 X 28MM - CADEIRA ELLEN/MEG/LAIS/NAOMI/VIVI",
    "equipamentos": [
      3
    ],
    "tempo": 13,
    "setup": 2100,
    "codigo_barra": 27426
  },
  {
    "id_erp": 28786,
    "nome": "PE MAD TRASEIRO P0051 500 X 44 X 32MM ESQUERDO - CADEIRA VITORIA",
    "equipamentos": [
      3
    ],
    "tempo": 11,
    "setup": 2100,
    "codigo_barra": 28786
  },
  {
    "id_erp": 28787,
    "nome": "PE MAD DIANTEIRO P0002 440 X 45 X 45MM - CADEIRA ALBANI",
    "equipamentos": [
      2
    ],
    "tempo": 11,
    "setup": 2100,
    "codigo_barra": 28787
  },
  {
    "id_erp": 28787,
    "nome": "PE MAD DIANTEIRO P0002 440 X 45 X 45MM - CADEIRA ALBANI",
    "equipamentos": [
      3
    ],
    "tempo": 12,
    "setup": 2100,
    "codigo_barra": 28787
  },
  {
    "id_erp": 28791,
    "nome": "ASA MAD A0001 490 X 45 X 24MM - CADEIRA ALBANI/VITORIA",
    "equipamentos": [
      3
    ],
    "tempo": 11,
    "setup": 2100,
    "codigo_barra": 28791
  },
  {
    "id_erp": 28807,
    "nome": "TRAVESSA MAD T0124 393 X 66 X 25MM - CADEIRA ALBANI",
    "equipamentos": [
      2
    ],
    "tempo": 13,
    "setup": 2100,
    "codigo_barra": 28807
  },
  {
    "id_erp": 28808,
    "nome": "TRAVESSA MAD T0125 298 X 66 X 25MM - CADEIRA ALBANI",
    "equipamentos": [
      2
    ],
    "tempo": 10,
    "setup": 2100,
    "codigo_barra": 28808
  },
  {
    "id_erp": 28815,
    "nome": "PE MAD TRASEIRO P0078 685 X 65 X 30MM ESQUERDO - POLTRONA CLEO",
    "equipamentos": [
      2
    ],
    "tempo": 23,
    "setup": 2100,
    "codigo_barra": 28815
  },
  {
    "id_erp": 28815,
    "nome": "PE MAD TRASEIRO P0078 685 X 65 X 30MM ESQUERDO - POLTRONA CLEO",
    "equipamentos": [
      3
    ],
    "tempo": 14,
    "setup": 2100,
    "codigo_barra": 28815
  },
  {
    "id_erp": 28816,
    "nome": "PE MAD DIANTEIRO P0025 645 X 55 X 30MM ESQUERDO - POLTRONA CLEO",
    "equipamentos": [
      2
    ],
    "tempo": 23,
    "setup": 2100,
    "codigo_barra": 28816
  },
  {
    "id_erp": 28816,
    "nome": "PE MAD DIANTEIRO P0025 645 X 55 X 30MM ESQUERDO - POLTRONA CLEO",
    "equipamentos": [
      3
    ],
    "tempo": 12,
    "setup": 2100,
    "codigo_barra": 28816
  },
  {
    "id_erp": 28817,
    "nome": "TRAVESSA MAD T0142 495 X 65 X 30MM ESQUERDA - POLTRONA CLEO",
    "equipamentos": [
      2
    ],
    "tempo": 11,
    "setup": 2100,
    "codigo_barra": 28817
  },
  {
    "id_erp": 28817,
    "nome": "TRAVESSA MAD T0142 495 X 65 X 30MM ESQUERDA - POLTRONA CLEO",
    "equipamentos": [
      3
    ],
    "tempo": 30,
    "setup": 2100,
    "codigo_barra": 28817
  },
  {
    "id_erp": 28818,
    "nome": "TRAVESSA MAD T0134 482 X 54 X 30MM - POLTRONA CLEO",
    "equipamentos": [
      2
    ],
    "tempo": 25,
    "setup": 2100,
    "codigo_barra": 28818
  },
  {
    "id_erp": 28818,
    "nome": "TRAVESSA MAD T0134 482 X 54 X 30MM - POLTRONA CLEO",
    "equipamentos": [
      3
    ],
    "tempo": 30,
    "setup": 2100,
    "codigo_barra": 28818
  },
  {
    "id_erp": 28819,
    "nome": "TRAVESSA MAD LATERAL T0120 460 X 60 X 24MM - POLTRONA CLEO/CLEO RATAN",
    "equipamentos": [
      2
    ],
    "tempo": 29,
    "setup": 2100,
    "codigo_barra": 28819
  },
  {
    "id_erp": 28820,
    "nome": "ASA MAD A0013 542 X 60 X 25MM - CADEIRA CLEO/CLEO RATAN",
    "equipamentos": [
      2
    ],
    "tempo": 15,
    "setup": 2100,
    "codigo_barra": 28820
  },
  {
    "id_erp": 30000,
    "nome": "MESA CENTRO MORANA (NELSINHO)",
    "equipamentos": [
      3
    ],
    "tempo": 2.131,
    "setup": 6900,
    "codigo_barra": 30000
  },
  {
    "id_erp": 30794,
    "nome": "PE MAD TRASEIRO P0064 970 X 52 X 32MM ESQUERDO - CADEIRA LINA",
    "equipamentos": [
      3
    ],
    "tempo": 15,
    "setup": 2100,
    "codigo_barra": 30794
  },
  {
    "id_erp": 31353,
    "nome": "FRONTAL MAD  F0007 450 X 45 X 32MM - CADEIRA ARENA/LIANE",
    "equipamentos": [
      2
    ],
    "tempo": 23,
    "setup": 2100,
    "codigo_barra": 31353
  },
  {
    "id_erp": 31536,
    "nome": "PE MAD TRASEIRO P0071 865 X 42 X 32MM ESQUERDO - CADEIRA MONTANA",
    "equipamentos": [
      3
    ],
    "tempo": 14,
    "setup": 2100,
    "codigo_barra": 31536
  },
  {
    "id_erp": 31537,
    "nome": "PE MAD EMB FREN DIR CAD MONTANA/DONNA 450 X 40 X 3 -",
    "equipamentos": [
      2
    ],
    "tempo": 11,
    "setup": 2100,
    "codigo_barra": 31537
  },
  {
    "id_erp": 31537,
    "nome": "PE MAD EMB FREN DIR CAD MONTANA/DONNA 450 X 40 X 3 -",
    "equipamentos": [
      3
    ],
    "tempo": 13,
    "setup": 2100,
    "codigo_barra": 31537
  },
  {
    "id_erp": 31543,
    "nome": "TRAVESSA MAD T0213 420 X 35 X 25MM - CADEIRA MONTANA",
    "equipamentos": [
      2
    ],
    "tempo": 16,
    "setup": 2100,
    "codigo_barra": 31543
  },
  {
    "id_erp": 31610,
    "nome": "PE MAD TRASEIRO P0054 920 X 50 X 32MM ESQUERDO - CADEIRA ATLANTA",
    "equipamentos": [
      3
    ],
    "tempo": 13,
    "setup": 2100,
    "codigo_barra": 31610
  },
  {
    "id_erp": 31611,
    "nome": "PE MAD DIANTEIRO P0013 430 X 50 X 32MM ESQUERDO - CADEIRA ATLANTA",
    "equipamentos": [
      2
    ],
    "tempo": 11,
    "setup": 2100,
    "codigo_barra": 31611
  },
  {
    "id_erp": 31611,
    "nome": "PE MAD DIANTEIRO P0013 430 X 50 X 32MM ESQUERDO - CADEIRA ATLANTA",
    "equipamentos": [
      3
    ],
    "tempo": 15,
    "setup": 2100,
    "codigo_barra": 31611
  },
  {
    "id_erp": 31689,
    "nome": "TRAV MAD EMB HOME THEATER LUTERO 2,2 1690 X 55 X 3 - HOME LUTERO",
    "equipamentos": [
      2
    ],
    "tempo": 29,
    "setup": 2100,
    "codigo_barra": 31689
  },
  {
    "id_erp": 31690,
    "nome": "TRAV MAD EMB HOME THEATER LUTERO 2,2 420 X 55 X 30 - HOME LUTERO",
    "equipamentos": [
      2
    ],
    "tempo": 32,
    "setup": 2100,
    "codigo_barra": 31690
  },
  {
    "id_erp": 31979,
    "nome": "PE MAD TRASEIRO P0108 685 X 65 X 30MM - POLTRONA CLEO RATAN",
    "equipamentos": [
      2
    ],
    "tempo": 15,
    "setup": 2100,
    "codigo_barra": 31979
  },
  {
    "id_erp": 31980,
    "nome": "PE MAD DIANTEIRO P0042 645 X 55 X 30MM - POLTRONA CLEO RATAN",
    "equipamentos": [
      2
    ],
    "tempo": 15,
    "setup": 2100,
    "codigo_barra": 31980
  },
  {
    "id_erp": 31981,
    "nome": "TRAVESSA MAD T0144 495 X 65 X 30MM - POLTRONA CLEO RATAN",
    "equipamentos": [
      2
    ],
    "tempo": 18,
    "setup": 2100,
    "codigo_barra": 31981
  },
  {
    "id_erp": 31982,
    "nome": "TRAVESSA MAD T0129 482 X 55 X 30MM - POLTRONA CLEO RATAN",
    "equipamentos": [
      2
    ],
    "tempo": 18,
    "setup": 2100,
    "codigo_barra": 31982
  },
  {
    "id_erp": 32990,
    "nome": "PE MAD P0027 730 X 110 X 45MM - MESA ALANIS",
    "equipamentos": [
      2
    ],
    "tempo": 23,
    "setup": 2100,
    "codigo_barra": 32990
  },
  {
    "id_erp": 32991,
    "nome": "TRAVESSA MAD T0552 640 X 90 X 45MM - MESA ALANIS",
    "equipamentos": [
      2
    ],
    "tempo": 27,
    "setup": 2100,
    "codigo_barra": 32991
  },
  {
    "id_erp": 33280,
    "nome": "PE MAD TRASEIRO P0062 497 X 63 X 32MM ESQUERDO - CADEIRA ESPANHA",
    "equipamentos": [
      3
    ],
    "tempo": 17,
    "setup": 2100,
    "codigo_barra": 33280
  },
  {
    "id_erp": 33281,
    "nome": "PE MAD DIANTEIRO P0018 430 X 50 X 32MM ESQUERDO - CADEIRA ESPANHA/PANTHEON/VITORIA",
    "equipamentos": [
      2
    ],
    "tempo": 11,
    "setup": 2100,
    "codigo_barra": 33281
  },
  {
    "id_erp": 33281,
    "nome": "PE MAD DIANTEIRO P0018 430 X 50 X 32MM ESQUERDO - CADEIRA ESPANHA/PANTHEON/VITORIA",
    "equipamentos": [
      3
    ],
    "tempo": 11,
    "setup": 2100,
    "codigo_barra": 33281
  },
  {
    "id_erp": 33282,
    "nome": "ASA MAD A0002 535 X 52 X 24MM - CADEIRA ESPANHA",
    "equipamentos": [
      3
    ],
    "tempo": 17,
    "setup": 2100,
    "codigo_barra": 33282
  },
  {
    "id_erp": 33283,
    "nome": "TRAVESSA MAD LATERAL T0100 459 X 60 X 24MM ESQUERD - CADEIRA ESPANHA",
    "equipamentos": [
      2
    ],
    "tempo": 30,
    "setup": 2100,
    "codigo_barra": 33283
  },
  {
    "id_erp": 33319,
    "nome": "PE MAD TRASEIRO P0050 915 X 50 X 32MM ESQUERDO - CADEIRA ALANIS",
    "equipamentos": [
      3
    ],
    "tempo": 21,
    "setup": 2100,
    "codigo_barra": 33319
  },
  {
    "id_erp": 33320,
    "nome": "PE MAD P0011 430 X  50 X  32MM  ESQUERDO - CADEIRA ALANIS",
    "equipamentos": [
      2
    ],
    "tempo": 14,
    "setup": 2100,
    "codigo_barra": 33320
  },
  {
    "id_erp": 33320,
    "nome": "PE MAD P0011 430 X  50 X  32MM  ESQUERDO - CADEIRA ALANIS",
    "equipamentos": [
      3
    ],
    "tempo": 14,
    "setup": 2100,
    "codigo_barra": 33320
  },
  {
    "id_erp": 33410,
    "nome": "TRAVESSA MAD T0513 1600 X 60 X 30MM - BUFFET NANTES",
    "equipamentos": [
      2
    ],
    "tempo": 35,
    "setup": 2100,
    "codigo_barra": 33410
  },
  {
    "id_erp": 33411,
    "nome": "TRAVESSA MAD T0514 330 X 60 X 30MM - BUFFET NANTES",
    "equipamentos": [
      2
    ],
    "tempo": 30,
    "setup": 2100,
    "codigo_barra": 33411
  },
  {
    "id_erp": 33412,
    "nome": "PE MAD P0023 290 X 80 X 30MM - BUFFET NANTES",
    "equipamentos": [
      2
    ],
    "tempo": 13,
    "setup": 2100,
    "codigo_barra": 33412
  },
  {
    "id_erp": 33445,
    "nome": "PE MAD DIANTEIRO P0007 679 X 52 X 32MM - CADEIRA PALOMA",
    "equipamentos": [
      3
    ],
    "tempo": 12,
    "setup": 2100,
    "codigo_barra": 33445
  },
  {
    "id_erp": 33450,
    "nome": "TRAVESSA MAD T0186 505 X 60 X 22MM - CADEIRA PALOMA",
    "equipamentos": [
      2
    ],
    "tempo": 14,
    "setup": 2100,
    "codigo_barra": 33450
  },
  {
    "id_erp": 33451,
    "nome": "TRAVESSA MAD T0228 460 X 40 X 22MM - CADEIRA PALOMA",
    "equipamentos": [
      2
    ],
    "tempo": 14,
    "setup": 2100,
    "codigo_barra": 33451
  },
  {
    "id_erp": 33452,
    "nome": "ASA MAD A0004 515 X 75 X 24MM - CADEIRA PALOMA",
    "equipamentos": [
      2
    ],
    "tempo": 15,
    "setup": 2100,
    "codigo_barra": 33452
  },
  {
    "id_erp": 33453,
    "nome": "TRAVESSA MAD LATERAL T0094 460 X 60 X 24MM - CADEIRA PALOMA",
    "equipamentos": [
      2
    ],
    "tempo": 15,
    "setup": 2100,
    "codigo_barra": 33453
  },
  {
    "id_erp": 34127,
    "nome": "PE MAD TRASEIRO P0060 555 X 50 X 32MM ESQUERDO - CADEIRA ELLEN/LANA/MALU/BELA/ALBA/MEG/LAIS/NAOMI/VIVI",
    "equipamentos": [
      2
    ],
    "tempo": 39,
    "setup": 2100,
    "codigo_barra": 34127
  },
  {
    "id_erp": 34127,
    "nome": "PE MAD TRASEIRO P0060 555 X 50 X 32MM ESQUERDO - CADEIRA ELLEN/LANA/MALU/BELA/ALBA/MEG/LAIS/NAOMI/VIVI",
    "equipamentos": [
      3
    ],
    "tempo": 15,
    "setup": 2100,
    "codigo_barra": 34127
  },
  {
    "id_erp": 34128,
    "nome": "PE MAD DIANTEIRO P0017 450 X 40 X 32MM ESQUERDO - CADEIRA ELLEN/LANA/MALU/BELA/MONTANA/DONNA/ALBA/MEG/LAIS/NAOMI/VIVI",
    "equipamentos": [
      2
    ],
    "tempo": 11,
    "setup": 2100,
    "codigo_barra": 34128
  },
  {
    "id_erp": 34128,
    "nome": "PE MAD DIANTEIRO P0017 450 X 40 X 32MM ESQUERDO - CADEIRA ELLEN/LANA/MALU/BELA/MONTANA/DONNA/ALBA/MEG/LAIS/NAOMI/VIVI",
    "equipamentos": [
      3
    ],
    "tempo": 14,
    "setup": 2100,
    "codigo_barra": 34128
  },
  {
    "id_erp": 34129,
    "nome": "ASA MAD A0008 475 X 43 X 23MM ESQUERDA - CADEIRA ELLEN/BRUNNA/CITY/ELEGANCE/LANA/MALU/BELA/ALBA/MEG/LAIS/NAOMI/VIVI/LIVIA",
    "equipamentos": [
      3
    ],
    "tempo": 12,
    "setup": 2100,
    "codigo_barra": 34129
  },
  {
    "id_erp": 34132,
    "nome": "PE MAD TRASEIRO P0056 555 X 53 X 32MM ESQUERDO - CADEIRA BRUNNA/CITY/LIVIA",
    "equipamentos": [
      2
    ],
    "tempo": 42,
    "setup": 900,
    "codigo_barra": 34132
  },
  {
    "id_erp": 34132,
    "nome": "PE MAD TRASEIRO P0056 555 X 53 X 32MM ESQUERDO - CADEIRA BRUNNA/CITY/LIVIA",
    "equipamentos": [
      3
    ],
    "tempo": 15,
    "setup": 900,
    "codigo_barra": 34132
  },
  {
    "id_erp": 34133,
    "nome": "PE MAD DIANTEIRO P0015 450 X 40 X 32MM ESQUERDO - CADEIRA BRUNNA/CITY/LIVIA/TARSILA",
    "equipamentos": [
      2
    ],
    "tempo": 11,
    "setup": 2100,
    "codigo_barra": 34133
  },
  {
    "id_erp": 34177,
    "nome": "TRAVESSA MAD T0557 500 X 60 X 32MM - MESA/COLUNA LINEA",
    "equipamentos": [
      2
    ],
    "tempo": 27,
    "setup": 0,
    "codigo_barra": 34177
  },
  {
    "id_erp": 34221,
    "nome": "PE MAD TRASEIRO P0059 550 X 50 X 32MM ESQUERDO - CADEIRA ELEGANCE/AGATA",
    "equipamentos": [
      3
    ],
    "tempo": 16,
    "setup": 2100,
    "codigo_barra": 34221
  },
  {
    "id_erp": 34222,
    "nome": "PE MAD DIANTEIRO P0003 450 X 45 X 45MM - CADEIRA ELEGANCE/AGATA",
    "equipamentos": [
      2
    ],
    "tempo": 25,
    "setup": 2100,
    "codigo_barra": 34222
  },
  {
    "id_erp": 34466,
    "nome": "PE MAD TRASEIRO P0073 679 X 52 X 32MM ESQUERDO - CADEIRA PALOMA",
    "equipamentos": [
      3
    ],
    "tempo": 12,
    "setup": 2100,
    "codigo_barra": 34466
  },
  {
    "id_erp": 34504,
    "nome": "TRAVESSA MAD T0556 720 X 40 X 32MM - MESA JANTAR MENFIS",
    "equipamentos": [
      2
    ],
    "tempo": 23,
    "setup": 2100,
    "codigo_barra": 34504
  },
  {
    "id_erp": 34565,
    "nome": "PE MAD TRASEIRO P0068 570 X 60 X 32MM ESQUERDO - CADEIRA LUNNA/ELISA/LUNNA TK",
    "equipamentos": [
      3
    ],
    "tempo": 13,
    "setup": 2100,
    "codigo_barra": 34565
  },
  {
    "id_erp": 34566,
    "nome": "PE MAD DIANTEIRO P0022 400 X 42 X 42MM ESQUERDO - CADEIRA LUNNA/ELISA/LUNNA TK",
    "equipamentos": [
      3
    ],
    "tempo": 13,
    "setup": 2100,
    "codigo_barra": 34566
  },
  {
    "id_erp": 34568,
    "nome": "TRAVESSA MAD LATERAL T0067 443 X 75 X 22MM ESQUERD - CADEIRA LUNNA/ELISA",
    "equipamentos": [
      2
    ],
    "tempo": 34,
    "setup": 2100,
    "codigo_barra": 34568
  },
  {
    "id_erp": 34568,
    "nome": "TRAVESSA MAD LATERAL T0067 443 X 75 X 22MM ESQUERD - CADEIRA LUNNA/ELISA",
    "equipamentos": [
      3
    ],
    "tempo": 25,
    "setup": 2100,
    "codigo_barra": 34568
  },
  {
    "id_erp": 34689,
    "nome": "PE MAD DIANTEIRO P0021 435 X 35 X 35MM ESQUERDO - CADEIRA LUCI/DUDA",
    "equipamentos": [
      3
    ],
    "tempo": 12,
    "setup": 2100,
    "codigo_barra": 34689
  },
  {
    "id_erp": 34690,
    "nome": "PE MAD TRASEIRO P0067 640 X 42 X 32MM ESQUERDO - CADEIRA LUCI",
    "equipamentos": [
      3
    ],
    "tempo": 12,
    "setup": 0,
    "codigo_barra": 34690
  },
  {
    "id_erp": 34692,
    "nome": "TRAVESSA MAD T0146 400 X 27 X 32MM - CADEIRA LUCI/DUDA",
    "equipamentos": [
      2
    ],
    "tempo": 42,
    "setup": 3000,
    "codigo_barra": 34692
  },
  {
    "id_erp": 34693,
    "nome": "TRAVESSA MAD LATERAL T0066 430 X 55 X 21MM ESQUERD - CADEIRA LUCI/DUDA",
    "equipamentos": [
      2
    ],
    "tempo": 29,
    "setup": 2100,
    "codigo_barra": 34693
  },
  {
    "id_erp": 34693,
    "nome": "TRAVESSA MAD LATERAL T0066 430 X 55 X 21MM ESQUERD - CADEIRA LUCI/DUDA",
    "equipamentos": [
      1
    ],
    "tempo": 29,
    "setup": 2100,
    "codigo_barra": 34693
  },
  {
    "id_erp": 34702,
    "nome": "TRAVESSA MAD LATERAL T0108 408 X 33 X 34MM DIREITA - CADEIRA LUCI",
    "equipamentos": [
      2
    ],
    "tempo": 29,
    "setup": 0,
    "codigo_barra": 34702
  },
  {
    "id_erp": 34703,
    "nome": "TRAVESSA MAD LATERAL T0083 440 X 30 X 30MM DIREITA - CADEIRA LUCI",
    "equipamentos": [
      2
    ],
    "tempo": 20,
    "setup": 3300,
    "codigo_barra": 34703
  },
  {
    "id_erp": 34703,
    "nome": "TRAVESSA MAD LATERAL T0083 440 X 30 X 30MM DIREITA - CADEIRA LUCI",
    "equipamentos": [
      1
    ],
    "tempo": 20,
    "setup": 3300,
    "codigo_barra": 34703
  },
  {
    "id_erp": 34709,
    "nome": "TRAVESSA MAD T0220 430 X 18 X 25MM - CADEIRA LUCI",
    "equipamentos": [
      2
    ],
    "tempo": 26,
    "setup": 2100,
    "codigo_barra": 34709
  },
  {
    "id_erp": 35045,
    "nome": "PE MAD TRASEIRO P0080 500 X 44 X 32MM DIREITO - CADEIRA ALBANI",
    "equipamentos": [
      3
    ],
    "tempo": 11,
    "setup": 2100,
    "codigo_barra": 35045
  },
  {
    "id_erp": 35046,
    "nome": "PE MAD DIANTEIRO P0028 430 X 50 X 32MM DIREITO - CADEIRA ATLANTA",
    "equipamentos": [
      3
    ],
    "tempo": 13,
    "setup": 2100,
    "codigo_barra": 35046
  },
  {
    "id_erp": 35047,
    "nome": "PE MAD TRASEIRO P0083 920 X 50 X 32MM DIREITO - CADEIRA ATLANTA",
    "equipamentos": [
      3
    ],
    "tempo": 13,
    "setup": 2100,
    "codigo_barra": 35047
  },
  {
    "id_erp": 35050,
    "nome": "TRAVESSA MAD LATERAL T0119 330 X 34 X 25MM DIREITA - CADEIRA AZZURE",
    "equipamentos": [
      2
    ],
    "tempo": 16,
    "setup": 2100,
    "codigo_barra": 35050
  },
  {
    "id_erp": 35050,
    "nome": "TRAVESSA MAD LATERAL T0119 330 X 34 X 25MM DIREITA - CADEIRA AZZURE",
    "equipamentos": [
      3
    ],
    "tempo": 16,
    "setup": 2100,
    "codigo_barra": 35050
  },
  {
    "id_erp": 35051,
    "nome": "PE MAD DIANTEIRO P0029 430 X 50 X 32MM DIREITO - CADEIRA AZZURE/CANNES",
    "equipamentos": [
      2
    ],
    "tempo": 11,
    "setup": 2100,
    "codigo_barra": 35051
  },
  {
    "id_erp": 35051,
    "nome": "PE MAD DIANTEIRO P0029 430 X 50 X 32MM DIREITO - CADEIRA AZZURE/CANNES",
    "equipamentos": [
      3
    ],
    "tempo": 11,
    "setup": 2100,
    "codigo_barra": 35051
  },
  {
    "id_erp": 35053,
    "nome": "PE MAD DIANTEIRO P0030 430 X 50 X 32MM DIREITO - CADEIRA BARI/LINA",
    "equipamentos": [
      3
    ],
    "tempo": 15,
    "setup": 2100,
    "codigo_barra": 35053
  },
  {
    "id_erp": 35055,
    "nome": "PE MAD DIANTEIRO P0032 440 X 50 X 32MM DIREITO - CADEIRA CASSINA/ATENAS/LISBOA/LONDRES/ORNATA/BIA/MARI",
    "equipamentos": [
      2
    ],
    "tempo": 12,
    "setup": 2100,
    "codigo_barra": 35055
  },
  {
    "id_erp": 35056,
    "nome": "PE MAD DIANTEIRO P0026 430 X 50 X 32MM DIREITO - CADEIRA ALANIS",
    "equipamentos": [
      2
    ],
    "tempo": 14,
    "setup": 2100,
    "codigo_barra": 35056
  },
  {
    "id_erp": 35056,
    "nome": "PE MAD DIANTEIRO P0026 430 X 50 X 32MM DIREITO - CADEIRA ALANIS",
    "equipamentos": [
      3
    ],
    "tempo": 14,
    "setup": 2100,
    "codigo_barra": 35056
  },
  {
    "id_erp": 35057,
    "nome": "PE MAD TRASEIRO P0086 490 X 55 X 32MM DIREITO - CADEIRA CASSINA/ATENAS/LISBOA/LIANE/LONDRES/ORNATA/BIA/MARI",
    "equipamentos": [
      3
    ],
    "tempo": 14,
    "setup": 2100,
    "codigo_barra": 35057
  },
  {
    "id_erp": 35059,
    "nome": "PE MAD DIANTEIRO P0031 450 X 40 X 32MM DIREITO - CADEIRA BRUNNA/CITY/LIVIA/TARSILA",
    "equipamentos": [
      2
    ],
    "tempo": 11,
    "setup": 2100,
    "codigo_barra": 35059
  },
  {
    "id_erp": 35063,
    "nome": "PE MAD TRASEIRO P0088 550 X 50 X 32MM DIREITO - CADEIRA ELEGANCE/AGATA",
    "equipamentos": [
      3
    ],
    "tempo": 16,
    "setup": 2100,
    "codigo_barra": 35063
  },
  {
    "id_erp": 35064,
    "nome": "ASA MAD A0010 475 X 55 X 24MM DIREITA - CADEIRA CASSINA/LISBOA/ATENAS/LIANE/LONDRES/ORNATA/BIA/MARI",
    "equipamentos": [
      3
    ],
    "tempo": 11,
    "setup": 2100,
    "codigo_barra": 35064
  },
  {
    "id_erp": 35066,
    "nome": "PE MAD TRASEIRO P0093 970 X 52 X 32MM DIREITO - CADEIRA LINA",
    "equipamentos": [
      3
    ],
    "tempo": 15,
    "setup": 2100,
    "codigo_barra": 35066
  },
  {
    "id_erp": 35072,
    "nome": "PE MAD EMB FREN ESQ CAD MONTANA/DONNA 450 X 40 X 3 -",
    "equipamentos": [
      2
    ],
    "tempo": 11,
    "setup": 2100,
    "codigo_barra": 35072
  },
  {
    "id_erp": 35072,
    "nome": "PE MAD EMB FREN ESQ CAD MONTANA/DONNA 450 X 40 X 3 -",
    "equipamentos": [
      3
    ],
    "tempo": 11,
    "setup": 2100,
    "codigo_barra": 35072
  },
  {
    "id_erp": 35075,
    "nome": "PE MAD TRASEIRO P0101 490 X 55 X 32MM DIREITO - CADEIRA NICE/IRIS/GALLA/AMBER/AMBER C/BRACO/NICE NOVA/IRIS NOVA",
    "equipamentos": [
      3
    ],
    "tempo": 11,
    "setup": 2100,
    "codigo_barra": 35075
  },
  {
    "id_erp": 35076,
    "nome": "PE MAD TRASEIRO P0103 485 X 53 X 32MM DIREITO - CADEIRA PANTHEON/GOYA",
    "equipamentos": [
      3
    ],
    "tempo": 11,
    "setup": 2100,
    "codigo_barra": 35076
  },
  {
    "id_erp": 35078,
    "nome": "PE MAD DIANTEIRO P0033 450 X 40 X 32MM DIREITO - CADEIRA ELLEN/LANA/MALU/BELA/MONT/DONNA/ALBA/MEG/LAIS/NAOMI/VIVI",
    "equipamentos": [
      2
    ],
    "tempo": 11,
    "setup": 2100,
    "codigo_barra": 35078
  },
  {
    "id_erp": 35078,
    "nome": "PE MAD DIANTEIRO P0033 450 X 40 X 32MM DIREITO - CADEIRA ELLEN/LANA/MALU/BELA/MONT/DONNA/ALBA/MEG/LAIS/NAOMI/VIVI",
    "equipamentos": [
      3
    ],
    "tempo": 11,
    "setup": 2100,
    "codigo_barra": 35078
  },
  {
    "id_erp": 35079,
    "nome": "PE MAD DIANTEIRO P0034 430 X 50 X 32MM DIREITO - CADEIRA ESPANHA/PANTHEON/VITORIA",
    "equipamentos": [
      2
    ],
    "tempo": 11,
    "setup": 2100,
    "codigo_barra": 35079
  },
  {
    "id_erp": 35079,
    "nome": "PE MAD DIANTEIRO P0034 430 X 50 X 32MM DIREITO - CADEIRA ESPANHA/PANTHEON/VITORIA",
    "equipamentos": [
      3
    ],
    "tempo": 11,
    "setup": 2100,
    "codigo_barra": 35079
  },
  {
    "id_erp": 35080,
    "nome": "PE MAD TRASEIRO P0100 865 X 42 X 32MM DIREITO - CADEIRA MONTANA",
    "equipamentos": [
      3
    ],
    "tempo": 14,
    "setup": 2100,
    "codigo_barra": 35080
  },
  {
    "id_erp": 35081,
    "nome": "PE MAD TRASEIRO P0096 640 X 42 X 32MM DIREITO - CADEIRA LUCI",
    "equipamentos": [
      3
    ],
    "tempo": 12,
    "setup": 0,
    "codigo_barra": 35081
  },
  {
    "id_erp": 35082,
    "nome": "PE MAD TRASEIRO P0102 679 X 52 X 32MM DIREITO - CADEIRA PALOMA",
    "equipamentos": [
      3
    ],
    "tempo": 12,
    "setup": 2100,
    "codigo_barra": 35082
  },
  {
    "id_erp": 35083,
    "nome": "PE MAD TRASEIRO P0089 555 X 50 X 32MM DIREITO - CADEIRA ELLEN/LANA/MALU/BELA/ALBA/MEG/LAIS/NAOMI/VIVI",
    "equipamentos": [
      2
    ],
    "tempo": 39,
    "setup": 2100,
    "codigo_barra": 35083
  },
  {
    "id_erp": 35083,
    "nome": "PE MAD TRASEIRO P0089 555 X 50 X 32MM DIREITO - CADEIRA ELLEN/LANA/MALU/BELA/ALBA/MEG/LAIS/NAOMI/VIVI",
    "equipamentos": [
      3
    ],
    "tempo": 39,
    "setup": 2100,
    "codigo_barra": 35083
  },
  {
    "id_erp": 35084,
    "nome": "PE MAD TRASEIRO P0091 497 X 63 X 32MM DIREITO - CADEIRA ESPANHA",
    "equipamentos": [
      3
    ],
    "tempo": 17,
    "setup": 2100,
    "codigo_barra": 35084
  },
  {
    "id_erp": 35085,
    "nome": "PE MAD TRASEIRO P0094 920 X 54 X 32MM DIREITO - CADEIRA LORENZA",
    "equipamentos": [
      2
    ],
    "tempo": 15,
    "setup": 2100,
    "codigo_barra": 35085
  },
  {
    "id_erp": 35086,
    "nome": "PE MAD TRASEIRO P0097 570 X 60 X 32MM DIREITO - CADEIRA LUNNA/ELISA/LUNNA TK",
    "equipamentos": [
      3
    ],
    "tempo": 13,
    "setup": 2100,
    "codigo_barra": 35086
  },
  {
    "id_erp": 35088,
    "nome": "PE MAD DIANTEIRO P0038 400 X 42 X 42MM DIREITO - CADEIRA LUNNA/ELISA/LUNNA TK",
    "equipamentos": [
      3
    ],
    "tempo": 13,
    "setup": 2100,
    "codigo_barra": 35088
  },
  {
    "id_erp": 35089,
    "nome": "PE MAD DIANTEIRO P0037 435 X 35 X 35MM DIREITO - CADEIRA LUCI/DUDA",
    "equipamentos": [
      3
    ],
    "tempo": 12,
    "setup": 2100,
    "codigo_barra": 35089
  },
  {
    "id_erp": 35090,
    "nome": "TRAVESSA MAD LATERAL T0074 430 X 55 X 21MM DIREITA - CADEIRA LUCI/DUDA",
    "equipamentos": [
      2
    ],
    "tempo": 29,
    "setup": 0,
    "codigo_barra": 35090
  },
  {
    "id_erp": 35090,
    "nome": "TRAVESSA MAD LATERAL T0074 430 X 55 X 21MM DIREITA - CADEIRA LUCI/DUDA",
    "equipamentos": [
      1
    ],
    "tempo": 29,
    "setup": 0,
    "codigo_barra": 35090
  },
  {
    "id_erp": 35091,
    "nome": "TRAVESSA MAD LATERAL T0106 408 X 33 X 34MM ESQUERD - CADEIRA LUCI",
    "equipamentos": [
      2
    ],
    "tempo": 29,
    "setup": 3600,
    "codigo_barra": 35091
  },
  {
    "id_erp": 35092,
    "nome": "TRAVESSA MAD LATERAL T0082 440 X 30 X 30MM ESQUERD - CADEIRA LUCI",
    "equipamentos": [
      2
    ],
    "tempo": 20,
    "setup": 0,
    "codigo_barra": 35092
  },
  {
    "id_erp": 35092,
    "nome": "TRAVESSA MAD LATERAL T0082 440 X 30 X 30MM ESQUERD - CADEIRA LUCI",
    "equipamentos": [
      1
    ],
    "tempo": 20,
    "setup": 0,
    "codigo_barra": 35092
  },
  {
    "id_erp": 35094,
    "nome": "ASA MAD A0012 535 X 52 X 24MM DIREITA - CADEIRA NICE/IRIS/NICE NOVA/IRIS NOVA/GALLA/AMBER",
    "equipamentos": [
      3
    ],
    "tempo": 11,
    "setup": 0,
    "codigo_barra": 35094
  },
  {
    "id_erp": 35096,
    "nome": "TRAVESSA MAD LATERAL T0112 459 X 60 X 24MM DIREITA - CADEIRA ESPANHA",
    "equipamentos": [
      2
    ],
    "tempo": 30,
    "setup": 2100,
    "codigo_barra": 35096
  },
  {
    "id_erp": 35097,
    "nome": "ASA MAD A0011 475 X 43 X 23MM DIREITA - CADEIRA ELLEN/BRUNNA/CITY/ELEGANCE/LANA/MALU/BELA/ALBA/MEG/LAIS/NAOMI/VIVI/LIVIA",
    "equipamentos": [
      3
    ],
    "tempo": 12,
    "setup": 2100,
    "codigo_barra": 35097
  },
  {
    "id_erp": 35098,
    "nome": "PE MAD TRASEIRO P0085 555 X 53 X 32MM DIREITO - CADEIRA BRUNNA/CITY/LIVIA",
    "equipamentos": [
      2
    ],
    "tempo": 42,
    "setup": 2100,
    "codigo_barra": 35098
  },
  {
    "id_erp": 35098,
    "nome": "PE MAD TRASEIRO P0085 555 X 53 X 32MM DIREITO - CADEIRA BRUNNA/CITY/LIVIA",
    "equipamentos": [
      3
    ],
    "tempo": 42,
    "setup": 2100,
    "codigo_barra": 35098
  },
  {
    "id_erp": 35099,
    "nome": "PE MAD TRASEIRO P0079 915 X 50 X 32MM DIREITO - CADEIRA ALANIS",
    "equipamentos": [
      3
    ],
    "tempo": 21,
    "setup": 2100,
    "codigo_barra": 35099
  },
  {
    "id_erp": 35102,
    "nome": "PE MAD TRASEIRO P0107 685 X 65 X 30MM DIREITO - POLTRONA CLEO",
    "equipamentos": [
      2
    ],
    "tempo": 23,
    "setup": 2100,
    "codigo_barra": 35102
  },
  {
    "id_erp": 35102,
    "nome": "PE MAD TRASEIRO P0107 685 X 65 X 30MM DIREITO - POLTRONA CLEO",
    "equipamentos": [
      3
    ],
    "tempo": 23,
    "setup": 2100,
    "codigo_barra": 35102
  },
  {
    "id_erp": 35103,
    "nome": "PE MAD DIANTEIRO P0041 645 X 55 X 30MM DIREITO - POLTRONA CLEO",
    "equipamentos": [
      2
    ],
    "tempo": 23,
    "setup": 2100,
    "codigo_barra": 35103
  },
  {
    "id_erp": 35103,
    "nome": "PE MAD DIANTEIRO P0041 645 X 55 X 30MM DIREITO - POLTRONA CLEO",
    "equipamentos": [
      3
    ],
    "tempo": 23,
    "setup": 2100,
    "codigo_barra": 35103
  },
  {
    "id_erp": 35104,
    "nome": "TRAVESSA MAD T0143 495 X 65 X 30MM DIREITA - POLTRONA CLEO",
    "equipamentos": [
      2
    ],
    "tempo": 11,
    "setup": 2100,
    "codigo_barra": 35104
  },
  {
    "id_erp": 35104,
    "nome": "TRAVESSA MAD T0143 495 X 65 X 30MM DIREITA - POLTRONA CLEO",
    "equipamentos": [
      3
    ],
    "tempo": 11,
    "setup": 2100,
    "codigo_barra": 35104
  },
  {
    "id_erp": 35105,
    "nome": "TRAVESSA MAD T0136 482 X 54 X 30MM - POLTRONA CLEO",
    "equipamentos": [
      2
    ],
    "tempo": 25,
    "setup": 2100,
    "codigo_barra": 35105
  },
  {
    "id_erp": 35105,
    "nome": "TRAVESSA MAD T0136 482 X 54 X 30MM - POLTRONA CLEO",
    "equipamentos": [
      3
    ],
    "tempo": 25,
    "setup": 2100,
    "codigo_barra": 35105
  },
  {
    "id_erp": 35173,
    "nome": "TRAVESSA MAD LATERAL T0075 443 X 75 X 22MM DIREITA - CADEIRA LUNNA/ELISA",
    "equipamentos": [
      2
    ],
    "tempo": 34,
    "setup": 0,
    "codigo_barra": 35173
  },
  {
    "id_erp": 35173,
    "nome": "TRAVESSA MAD LATERAL T0075 443 X 75 X 22MM DIREITA - CADEIRA LUNNA/ELISA",
    "equipamentos": [
      3
    ],
    "tempo": 34,
    "setup": 0,
    "codigo_barra": 35173
  },
  {
    "id_erp": 35197,
    "nome": "FRONTAL MAD  F0004 450 X 45 X 32MM - CADEIRA LONDRES",
    "equipamentos": [
      2
    ],
    "tempo": 23,
    "setup": 2100,
    "codigo_barra": 35197
  },
  {
    "id_erp": 35318,
    "nome": "PE MAD P0044 810 X 100 X 45MM - MESA JANTAR ELLEN",
    "equipamentos": [
      3
    ],
    "tempo": 30,
    "setup": 2100,
    "codigo_barra": 35318
  },
  {
    "id_erp": 35319,
    "nome": "TRAVESSA MAD T0568 860 X 85 X 45MM - MESA JANTAR ELLEN",
    "equipamentos": [
      2
    ],
    "tempo": 53,
    "setup": 2100,
    "codigo_barra": 35319
  },
  {
    "id_erp": 35326,
    "nome": "PE MAD DIANTEIRO P0010 440 X 35 X 35MM - CADEIRA UNA",
    "equipamentos": [
      3
    ],
    "tempo": 12,
    "setup": 2100,
    "codigo_barra": 35326
  },
  {
    "id_erp": 35327,
    "nome": "PE MAD TRASEIRO P0076 440 X 35 X 35MM ESQUERDO - CADEIRA UNA",
    "equipamentos": [
      3
    ],
    "tempo": 12,
    "setup": 2100,
    "codigo_barra": 35327
  },
  {
    "id_erp": 35328,
    "nome": "PE MAD TRASEIRO P0105 440 X 35 X 35MM DIREITO - CADEIRA UNA",
    "equipamentos": [
      3
    ],
    "tempo": 12,
    "setup": 2100,
    "codigo_barra": 35328
  },
  {
    "id_erp": 35664,
    "nome": "PE MAD TRASEIRO P0077 430 X 55 X 32MM ESQUERDO - CADEIRA VIC/SARA",
    "equipamentos": [
      3
    ],
    "tempo": 12,
    "setup": 2100,
    "codigo_barra": 35664
  },
  {
    "id_erp": 35665,
    "nome": "PE MAD TRASEIRO P0106 430 X 55 X 32MM DIREITO - CADEIRA VIC/SARA",
    "equipamentos": [
      3
    ],
    "tempo": 12,
    "setup": 2100,
    "codigo_barra": 35665
  },
  {
    "id_erp": 35666,
    "nome": "TRAVESSA MAD TRASEIRA T0040 465 X 60 X 22MM - CADEIRA VIC/SARA",
    "equipamentos": [
      2
    ],
    "tempo": 28,
    "setup": 2100,
    "codigo_barra": 35666
  },
  {
    "id_erp": 35667,
    "nome": "TRAVESSA MAD DIANTEIRA T0010 450 X 60 X 22MM - CADEIRA VIC/SARA",
    "equipamentos": [
      2
    ],
    "tempo": 28,
    "setup": 2100,
    "codigo_barra": 35667
  },
  {
    "id_erp": 35668,
    "nome": "TRAVESSA MAD LATERAL T0061 440 X 60 X 22MM - CADEIRA VIC/SARA",
    "equipamentos": [
      2
    ],
    "tempo": 30,
    "setup": 2100,
    "codigo_barra": 35668
  },
  {
    "id_erp": 35674,
    "nome": "TRAVESSA MAD LATERAL T0107 530 X 50 X 32MM ESQUERD - CADEIRA VIC/SARA",
    "equipamentos": [
      3
    ],
    "tempo": 12,
    "setup": 2100,
    "codigo_barra": 35674
  },
  {
    "id_erp": 35675,
    "nome": "TRAVESSA MAD LATERAL T0109 530 X 50 X 32MM DIREITA - CADEIRA VIC/SARA",
    "equipamentos": [
      3
    ],
    "tempo": 12,
    "setup": 2100,
    "codigo_barra": 35675
  },
  {
    "id_erp": 35685,
    "nome": "PE MAD DIANTEIRO P0044 410 X 45 X 45MM - CADEIRA VIC/SARA",
    "equipamentos": [
      2
    ],
    "tempo": 12,
    "setup": 2100,
    "codigo_barra": 35685
  },
  {
    "id_erp": 35809,
    "nome": "PE MAD TRASEIRO P0070 900 X 54 X 32MM ESQUERDO - CADEIRA MILE",
    "equipamentos": [
      3
    ],
    "tempo": 14,
    "setup": 0,
    "codigo_barra": 35809
  },
  {
    "id_erp": 35810,
    "nome": "PE MAD DIANTEIRO P0024 430 X 45 X 32MM ESQUERDO - CADEIRA MILE",
    "equipamentos": [
      3
    ],
    "tempo": 14,
    "setup": 3600,
    "codigo_barra": 35810
  },
  {
    "id_erp": 35813,
    "nome": "TRAVESSA MAD TRASEIRA T0039 410 X 45 X 26MM - CADEIRA MILE",
    "equipamentos": [
      2
    ],
    "tempo": 41,
    "setup": 3060,
    "codigo_barra": 35813
  },
  {
    "id_erp": 35814,
    "nome": "FRONTAL MAD  F0005 435 X 33 X 24MM - CADEIRA MILE",
    "equipamentos": [
      2
    ],
    "tempo": 33,
    "setup": 4800,
    "codigo_barra": 35814
  },
  {
    "id_erp": 35815,
    "nome": "TRAVESSA MAD T0133 410 X 33 X 24MM - CADEIRA MILE",
    "equipamentos": [
      2
    ],
    "tempo": 41,
    "setup": 3600,
    "codigo_barra": 35815
  },
  {
    "id_erp": 35831,
    "nome": "PE MAD TRASEIRO P0099 900 X 54 X 32MM DIREITO - CADEIRA MILE",
    "equipamentos": [
      3
    ],
    "tempo": 14,
    "setup": 3600,
    "codigo_barra": 35831
  },
  {
    "id_erp": 35832,
    "nome": "PE MAD DIANTEIRO P0040 430 X 45 X 32MM DIREITO - CADEIRA MILE",
    "equipamentos": [
      3
    ],
    "tempo": 14,
    "setup": 0,
    "codigo_barra": 35832
  },
  {
    "id_erp": 35966,
    "nome": "PE MAD TRASEIRO P0053 925 X 65 X 32MM ESQUERDO - CADEIRA ANNE/MATELASSE",
    "equipamentos": [
      3
    ],
    "tempo": 13,
    "setup": 0,
    "codigo_barra": 35966
  },
  {
    "id_erp": 35967,
    "nome": "PE MAD TRASEIRO P0082 925 X 65 X 32MM DIREITO - CADEIRA ANNE/MATELASSE",
    "equipamentos": [
      3
    ],
    "tempo": 13,
    "setup": 0,
    "codigo_barra": 35967
  },
  {
    "id_erp": 35970,
    "nome": "FRONTAL MAD  F0002 450 X 45 X 25MM - CADEIRA ANNE/MATELASSE",
    "equipamentos": [
      2
    ],
    "tempo": 40,
    "setup": 2880,
    "codigo_barra": 35970
  },
  {
    "id_erp": 35970,
    "nome": "FRONTAL MAD  F0002 450 X 45 X 25MM - CADEIRA ANNE/MATELASSE",
    "equipamentos": [
      3
    ],
    "tempo": 40,
    "setup": 2880,
    "codigo_barra": 35970
  },
  {
    "id_erp": 35972,
    "nome": "TRAVESSA MAD LATERAL T0063 460 X 60 X 22MM ESQUERD - CADEIRA ANNE/MATELASSE",
    "equipamentos": [
      2
    ],
    "tempo": 28,
    "setup": 2100,
    "codigo_barra": 35972
  },
  {
    "id_erp": 35973,
    "nome": "TRAVESSA MAD LATERAL T0071 460 X 60 X 22MM DIREITA - CADEIRA ANNE/MATELASSE",
    "equipamentos": [
      2
    ],
    "tempo": 28,
    "setup": 2100,
    "codigo_barra": 35973
  },
  {
    "id_erp": 36000,
    "nome": "PE MAD TRASEIRO P0052 925 X 65 X 30MM ESQUERDO - CADEIRA ANNE RATAN",
    "equipamentos": [
      3
    ],
    "tempo": 13,
    "setup": 0,
    "codigo_barra": 36000
  },
  {
    "id_erp": 36001,
    "nome": "PE MAD TRASEIRO P0081 925 X 65 X 30MM DIREITO - CADEIRA ANNE RATAN",
    "equipamentos": [
      3
    ],
    "tempo": 13,
    "setup": 0,
    "codigo_barra": 36001
  },
  {
    "id_erp": 36002,
    "nome": "PE MAD DIANTEIRO P0012 433 X 52 X 30MM ESQUERDO - CADEIRA ANNE (RATAN/MATELASSE)/ELIZE (RATAN/C/ BRACO)",
    "equipamentos": [
      3
    ],
    "tempo": 15,
    "setup": 3600,
    "codigo_barra": 36002
  },
  {
    "id_erp": 36003,
    "nome": "PE MAD DIANTEIRO P0027 433 X 52 X 30MM DIREITO - CADEIRA ANNE (RATAN/MATELASSE)/ELIZE (RATAN/C/ BRACO)",
    "equipamentos": [
      3
    ],
    "tempo": 15,
    "setup": 3600,
    "codigo_barra": 36003
  },
  {
    "id_erp": 36004,
    "nome": "FRONTAL MAD  F0001 450 X 45 X 25MM - CADEIRA ANNE RATAN",
    "equipamentos": [
      2
    ],
    "tempo": 44,
    "setup": 2100,
    "codigo_barra": 36004
  },
  {
    "id_erp": 36004,
    "nome": "FRONTAL MAD  F0001 450 X 45 X 25MM - CADEIRA ANNE RATAN",
    "equipamentos": [
      3
    ],
    "tempo": 44,
    "setup": 2100,
    "codigo_barra": 36004
  },
  {
    "id_erp": 36005,
    "nome": "TRAVESSA MAD TRASEIRA T0034 466 X 42 X 25MM - CADEIRA ANNE RATAN",
    "equipamentos": [
      2
    ],
    "tempo": 27,
    "setup": 2100,
    "codigo_barra": 36005
  },
  {
    "id_erp": 36006,
    "nome": "TRAVESSA MAD T0130 460 X 43 X 26MM - CADEIRA ANNE RATAN",
    "equipamentos": [
      2
    ],
    "tempo": 39,
    "setup": 2100,
    "codigo_barra": 36006
  },
  {
    "id_erp": 36006,
    "nome": "TRAVESSA MAD T0130 460 X 43 X 26MM - CADEIRA ANNE RATAN",
    "equipamentos": [
      3
    ],
    "tempo": 39,
    "setup": 2100,
    "codigo_barra": 36006
  },
  {
    "id_erp": 36007,
    "nome": "TRAVESSA MAD DIANTEIRA T0002 480 X 60 X 22MM - CADEIRA ANNE/ANNE MATELASSE",
    "equipamentos": [
      2
    ],
    "tempo": 25,
    "setup": 2100,
    "codigo_barra": 36007
  },
  {
    "id_erp": 36031,
    "nome": "TRAVESSA MAD T0565 830 X 65 X 32MM - BAR ORION",
    "equipamentos": [
      2
    ],
    "tempo": 46,
    "setup": 2100,
    "codigo_barra": 36031
  },
  {
    "id_erp": 36032,
    "nome": "PE MAD P0021 300 X 100 X 32MM - BAR/BUFFET ORION",
    "equipamentos": [
      3
    ],
    "tempo": 40,
    "setup": 4800,
    "codigo_barra": 36032
  },
  {
    "id_erp": 36033,
    "nome": "TRAVESSA MAD T0523 380 X 50 X 32MM - BUFFET ORION",
    "equipamentos": [
      2
    ],
    "tempo": 27,
    "setup": 2100,
    "codigo_barra": 36033
  },
  {
    "id_erp": 36217,
    "nome": "TRAVESSA MAD T0563 1130 X 65 X 32MM - APARADOR ORION",
    "equipamentos": [
      2
    ],
    "tempo": 49,
    "setup": 2100,
    "codigo_barra": 36217
  },
  {
    "id_erp": 36218,
    "nome": "PE MAD P0020 640 X 90 X 32MM - APARADOR ORION",
    "equipamentos": [
      3
    ],
    "tempo": 23,
    "setup": 2100,
    "codigo_barra": 36218
  },
  {
    "id_erp": 36359,
    "nome": "TRAVESSA MAD T0605 1568 X 65 X 32MM - BUFFET ORION",
    "equipamentos": [
      2
    ],
    "tempo": 57,
    "setup": 2100,
    "codigo_barra": 36359
  },
  {
    "id_erp": 36521,
    "nome": "PE MAD P0026 325 X 120 X 32MM - MESA CENTRO MARA 1,10",
    "equipamentos": [
      3
    ],
    "tempo": 30,
    "setup": 4200,
    "codigo_barra": 36521
  },
  {
    "id_erp": 36523,
    "nome": "PE MAD P0025 260 X 105 X 38MM - MESA CENTRO MARA 1,00",
    "equipamentos": [
      3
    ],
    "tempo": 30,
    "setup": 4200,
    "codigo_barra": 36523
  },
  {
    "id_erp": 36526,
    "nome": "TRAVESSA MAD T0529 765 X 52 X 32MM - MESA CENTRO MARA 1,00",
    "equipamentos": [
      3
    ],
    "tempo": 20,
    "setup": 5700,
    "codigo_barra": 36526
  },
  {
    "id_erp": 36722,
    "nome": "TRAVESSA MAD T0538 660 X 52 X 32MM - MESA CENTRO MARA 1,00",
    "equipamentos": [
      3
    ],
    "tempo": 20,
    "setup": 0,
    "codigo_barra": 36722
  },
  {
    "id_erp": 36723,
    "nome": "TRAVESSA MAD T0539 660 X 52 X 32MM - MESA CENTRO MARA 1,10",
    "equipamentos": [
      3
    ],
    "tempo": 20,
    "setup": 0,
    "codigo_barra": 36723
  },
  {
    "id_erp": 36904,
    "nome": "TRAVESSA MAD T0522 388 X 50 X 32MM - APARADOR ORION",
    "equipamentos": [
      2
    ],
    "tempo": 27,
    "setup": 2100,
    "codigo_barra": 36904
  },
  {
    "id_erp": 36910,
    "nome": "TRAVESSA MAD T0530 765 X 52 X 32MM - MESA CENTRO MARA 1,10",
    "equipamentos": [
      3
    ],
    "tempo": 20,
    "setup": 5700,
    "codigo_barra": 36910
  },
  {
    "id_erp": 36999,
    "nome": "TRAVESSA MAD T0524 1480 X 45 X 32MM - APARADOR LYON/DENVER",
    "equipamentos": [
      2
    ],
    "tempo": 70,
    "setup": 2100,
    "codigo_barra": 36999
  },
  {
    "id_erp": 37063,
    "nome": "TRAVESSA MAD T0527 1780 X 45 X 32MM - BUFFET LYON/DENVER 1,80",
    "equipamentos": [
      2
    ],
    "tempo": 70,
    "setup": 2100,
    "codigo_barra": 37063
  },
  {
    "id_erp": 37194,
    "nome": "TRAVESSA MAD T0526 1480 X 45 X 32MM - BUFFET LYON/DENVER 1,50",
    "equipamentos": [
      2
    ],
    "tempo": 70,
    "setup": 2100,
    "codigo_barra": 37194
  },
  {
    "id_erp": 37303,
    "nome": "PE MAD TRASEIRO P0063 873 X 43 X 31MM ESQUERDO - CADEIRA ISA/ISA MATELASSE/DORA/EVA",
    "equipamentos": [
      3
    ],
    "tempo": 12,
    "setup": 2100,
    "codigo_barra": 37303
  },
  {
    "id_erp": 37304,
    "nome": "PE MAD TRASEIRO P0092 873 X 43 X 31MM DIREITO - CADEIRA ISA/ISA MATELASSE/DORA/EVA",
    "equipamentos": [
      3
    ],
    "tempo": 12,
    "setup": 2100,
    "codigo_barra": 37304
  },
  {
    "id_erp": 37305,
    "nome": "PE MAD DIANTEIRO P0019 430 X 43 X 43MM - CADEIRA ISA/ISA MATELASSE/DORA/EVA",
    "equipamentos": [
      3
    ],
    "tempo": 11,
    "setup": 2100,
    "codigo_barra": 37305
  },
  {
    "id_erp": 37410,
    "nome": "PE MAD TRASEIRO P0069 890 X 46 X 32MM ESQUERDO - CADEIRA MAIA",
    "equipamentos": [
      3
    ],
    "tempo": 13,
    "setup": 0,
    "codigo_barra": 37410
  },
  {
    "id_erp": 37411,
    "nome": "PE MAD TRASEIRO P0098 890 X 46 X 32MM DIREITO - CADEIRA MAIA",
    "equipamentos": [
      3
    ],
    "tempo": 13,
    "setup": 2100,
    "codigo_barra": 37411
  },
  {
    "id_erp": 37413,
    "nome": "PE MAD DIANTEIRO P0023 432 X 44 X 32MM ESQUERDO - CADEIRA MAIA/MAIA RATAN/LAURA",
    "equipamentos": [
      3
    ],
    "tempo": 13,
    "setup": 0,
    "codigo_barra": 37413
  },
  {
    "id_erp": 37414,
    "nome": "PE MAD DIANTEIRO P0039 432 X 44 X 32MM DIREITO - CADEIRA MAIA/MAIA RATAN/LAURA",
    "equipamentos": [
      3
    ],
    "tempo": 13,
    "setup": 2100,
    "codigo_barra": 37414
  },
  {
    "id_erp": 38007,
    "nome": "TRAVESSA MAD LATERAL T0062 418 X 60 X 22MM - CADEIRA ANNE RATAN",
    "equipamentos": [
      2
    ],
    "tempo": 28,
    "setup": 2100,
    "codigo_barra": 38007
  },
  {
    "id_erp": 38008,
    "nome": "TRAVESSA MAD LATERAL T0070 418 X 60 X 22MM DIREITA - CADEIRA ANNE RATAN",
    "equipamentos": [
      2
    ],
    "tempo": 28,
    "setup": 2100,
    "codigo_barra": 38008
  },
  {
    "id_erp": 38132,
    "nome": "PE MAD P0028 810 X 100 X 45MM - MESA CAPRI",
    "equipamentos": [
      3
    ],
    "tempo": 13,
    "setup": 2100,
    "codigo_barra": 38132
  },
  {
    "id_erp": 38133,
    "nome": "TRAVESSA MAD T0553 870 X 40 X 32MM - MESA CAPRI",
    "equipamentos": [
      2
    ],
    "tempo": 43,
    "setup": 2100,
    "codigo_barra": 38133
  },
  {
    "id_erp": 38204,
    "nome": "TRAVESSA MAD  T0100 500 X 60 X 22MM -  (SOFA ITAMBE)",
    "equipamentos": [
      3
    ],
    "tempo": "-",
    "setup": 0,
    "codigo_barra": 38204
  },
  {
    "id_erp": 38311,
    "nome": "TRAVESSA MAD LATERAL T0235 632 X 80 X 18MM ESQUERD - POLTRONA JADE",
    "equipamentos": [
      2
    ],
    "tempo": 23,
    "setup": 2100,
    "codigo_barra": 38311
  },
  {
    "id_erp": 38326,
    "nome": "TRAVESSA MAD T0237 508 X 42 X 22MM - POLTRONA JADE",
    "equipamentos": [
      2
    ],
    "tempo": 55,
    "setup": 2100,
    "codigo_barra": 38326
  },
  {
    "id_erp": 38327,
    "nome": "TRAVESSA MAD T0238 520 X 42 X 35MM - POLTRONA JADE",
    "equipamentos": [
      2
    ],
    "tempo": 69,
    "setup": 2100,
    "codigo_barra": 38327
  },
  {
    "id_erp": 38341,
    "nome": "PE MAD TRASEIRO P0110 824 X 66 X 30MM ESQUERDO - CADEIRA ALICE/ALICE C/BRACO",
    "equipamentos": [
      3
    ],
    "tempo": 14,
    "setup": 2100,
    "codigo_barra": 38341
  },
  {
    "id_erp": 38342,
    "nome": "PE MAD DIANTEIRO P0111 430 X 50 X 30MM ESQUERDO - CADEIRA ALICE/ALICE C/BRACO",
    "equipamentos": [
      3
    ],
    "tempo": 14,
    "setup": 2100,
    "codigo_barra": 38342
  },
  {
    "id_erp": 38344,
    "nome": "PE MAD TRASEIRO P0112 824 X 66 X 30MM DIREITO - CADEIRA ALICE/ALICE C/BRACO",
    "equipamentos": [
      3
    ],
    "tempo": 14,
    "setup": 2100,
    "codigo_barra": 38344
  },
  {
    "id_erp": 38345,
    "nome": "PE MAD DIANTEIRO P0113 430 X 50 X 30MM DIREITO - CADEIRA ALICE/ALICE C/BRACO",
    "equipamentos": [
      3
    ],
    "tempo": 14,
    "setup": 2100,
    "codigo_barra": 38345
  },
  {
    "id_erp": 38347,
    "nome": "TRAVESSA MAD TRASEIRA T0242 428 X 43 X 24MM - CADEIRA ALICE/ALICE C/BRACO",
    "equipamentos": [
      2
    ],
    "tempo": 34,
    "setup": 2100,
    "codigo_barra": 38347
  },
  {
    "id_erp": 38348,
    "nome": "TRAVESSA MAD T0243 428 X 32 X 25MM - CADEIRA ALICE/ALICE C/BRACO",
    "equipamentos": [
      2
    ],
    "tempo": 38,
    "setup": 2100,
    "codigo_barra": 38348
  },
  {
    "id_erp": 38690,
    "nome": "TRAVESSA MAD T0624 570 X 103 X 42MM - MESA JANTAR PRISMA",
    "equipamentos": [
      3
    ],
    "tempo": 20,
    "setup": 0,
    "codigo_barra": 38690
  },
  {
    "id_erp": 38691,
    "nome": "PE MAD P0101 565 X 100 X 42MM - MESA JANTAR PRISMA",
    "equipamentos": [
      3
    ],
    "tempo": 60,
    "setup": 2100,
    "codigo_barra": 38691
  },
  {
    "id_erp": 38692,
    "nome": "TRAVESSA MAD T0564 250 X 120 X 42MM - MESA JANTAR PRISMA",
    "equipamentos": [
      2
    ],
    "tempo": 67,
    "setup": 2100,
    "codigo_barra": 38692
  },
  {
    "id_erp": 38695,
    "nome": "TRAVESSA MAD T0565 390 X 80 X 30MM - MESA JANTAR PRISMA",
    "equipamentos": [
      2
    ],
    "tempo": 47,
    "setup": 2100,
    "codigo_barra": 38695
  },
  {
    "id_erp": 38731,
    "nome": "PE MAD DIANTEIRO P0114 400 X 44 X 44MM ESQUERDO - CADEIRA SOFIA",
    "equipamentos": [
      3
    ],
    "tempo": 12,
    "setup": 2100,
    "codigo_barra": 38731
  },
  {
    "id_erp": 38735,
    "nome": "PE MAD DIANTEIRO P0115 400 X 44 X 44MM DIREITO - CADEIRA SOFIA",
    "equipamentos": [
      3
    ],
    "tempo": 12,
    "setup": 2100,
    "codigo_barra": 38735
  },
  {
    "id_erp": 38737,
    "nome": "PE MAD TRASEIRO P0116 400 X 44 X 44MM ESQUERDO - CADEIRA SOFIA",
    "equipamentos": [
      3
    ],
    "tempo": 12,
    "setup": 2100,
    "codigo_barra": 38737
  },
  {
    "id_erp": 38738,
    "nome": "PE MAD TRASEIRO P0117 400 X 44 X 44MM DIREITO - CADEIRA SOFIA",
    "equipamentos": [
      3
    ],
    "tempo": 12,
    "setup": 2100,
    "codigo_barra": 38738
  },
  {
    "id_erp": 38839,
    "nome": "PE MAD TRASEIRO P0118 615 X 145 X 32MM DIREITO - CADEIRA MARROCOS/MARROCOS LAMINADA/IBIZA",
    "equipamentos": [
      3
    ],
    "tempo": 50,
    "setup": 2100,
    "codigo_barra": 38839
  },
  {
    "id_erp": 38840,
    "nome": "PE MAD DIANTEIRO P0119 435 X 70 X 32MM DIRETO - CADEIRA MARROCOS/MARROCOS LAMINADA/IBIZA",
    "equipamentos": [
      3
    ],
    "tempo": 26,
    "setup": 2100,
    "codigo_barra": 38840
  },
  {
    "id_erp": 38841,
    "nome": "TRAVESSA MAD DIANTEIRA T0254 360 X 55 X 22MM - CADEIRA MARROCOS/MARROCOS LAMINADA/IBIZA",
    "equipamentos": [
      2
    ],
    "tempo": 29,
    "setup": 2100,
    "codigo_barra": 38841
  },
  {
    "id_erp": 38842,
    "nome": "TRAVESSA MAD LATERAL T0255 415 X 63 X 32MM DIRETO - CADEIRA MARROCOS/MARROCOS LAMINADA/IBIZA",
    "equipamentos": [
      2
    ],
    "tempo": 30,
    "setup": 0,
    "codigo_barra": 38842
  },
  {
    "id_erp": 38843,
    "nome": "TRAVESSA MAD TRASEIRA T0256 355 X 80 X 22MM - CADEIRA MARROCOS/MARROCOS LAMINADA/IBIZA",
    "equipamentos": [
      2
    ],
    "tempo": 29,
    "setup": 0,
    "codigo_barra": 38843
  },
  {
    "id_erp": 38844,
    "nome": "PE MAD TRASEIRO P0120 615 X 145 X 32MM ESQUERDO - CADEIRA MARROCOS/MARROCOS LAMINADA/IBIZA",
    "equipamentos": [
      3
    ],
    "tempo": 50,
    "setup": 2100,
    "codigo_barra": 38844
  },
  {
    "id_erp": 38845,
    "nome": "PE MAD DIANTEIRO P0121 435 X 70 X 32MM ESQUERDO - CADEIRA MARROCOS/MARROCOS LAMINADA/IBIZA",
    "equipamentos": [
      3
    ],
    "tempo": 26,
    "setup": 2100,
    "codigo_barra": 38845
  },
  {
    "id_erp": 38846,
    "nome": "TRAVESSA MAD LATERAL T0257 415 X 63 X 32MM ESQUERD - CADEIRA MARROCOS/MARROCOS LAMINADA/IBIZA",
    "equipamentos": [
      2
    ],
    "tempo": 30,
    "setup": 3000,
    "codigo_barra": 38846
  },
  {
    "id_erp": 38892,
    "nome": "PE MAD P0122 430 X 90 X 32MM - CADEIRA EMILY/MANU GIRATORIA/NANDA GIRATORIA",
    "equipamentos": [
      3
    ],
    "tempo": 27,
    "setup": 5400,
    "codigo_barra": 38892
  },
  {
    "id_erp": 38930,
    "nome": "PE MAD P0123 300 X 80 X 32MM - PUFF CAROL/POLTRONA CAROL",
    "equipamentos": [
      2
    ],
    "tempo": 17,
    "setup": 2100,
    "codigo_barra": 38930
  },
  {
    "id_erp": 39932,
    "nome": "TRAVESSA MAD T0262 265 X 55 X 32MM ESQUERDO - CADEIRA ALICE C/ BRACO",
    "equipamentos": [
      2
    ],
    "tempo": 19,
    "setup": 2100,
    "codigo_barra": 39932
  },
  {
    "id_erp": 39933,
    "nome": "TRAVESSA MAD T0263 405 X 60 X 32MM ESQUERDO - CADEIRA ALICE C/ BRACO",
    "equipamentos": [
      2
    ],
    "tempo": 19,
    "setup": 2100,
    "codigo_barra": 39933
  },
  {
    "id_erp": 39937,
    "nome": "TRAVESSA MAD T0264 265 X 55 X 32MM DIREITO - CADEIRA ALICE C/ BRACO",
    "equipamentos": [
      2
    ],
    "tempo": 19,
    "setup": 2100,
    "codigo_barra": 39937
  },
  {
    "id_erp": 39938,
    "nome": "TRAVESSA MAD T0265 405 X 60 X 32MM DIREITO - CADEIRA ALICE C/ BRACO",
    "equipamentos": [
      2
    ],
    "tempo": 18,
    "setup": 2100,
    "codigo_barra": 39938
  },
  {
    "id_erp": 40000,
    "nome": "MESA CENTRO MORANA (NELSINHO)",
    "equipamentos": [
      2
    ],
    "tempo": 2.131,
    "setup": 5100,
    "codigo_barra": 40000
  },
  {
    "id_erp": 40119,
    "nome": "TRAVESSA MAD T0597 1080 X 45 X 32MM - BAR DENVER/LYON",
    "equipamentos": [
      3
    ],
    "tempo": 46,
    "setup": 2100,
    "codigo_barra": 40119
  },
  {
    "id_erp": 40250,
    "nome": "TRAVESSA MAD T0593 880 X 45 X 32MM - ARMARIO DENVER/LYON",
    "equipamentos": [
      2
    ],
    "tempo": 46,
    "setup": 2100,
    "codigo_barra": 40250
  },
  {
    "id_erp": 40252,
    "nome": "TRAVESSA MAD T0594 325 X 50 X 32MM - ARMARIO DENVER/LYON",
    "equipamentos": [
      2
    ],
    "tempo": 27,
    "setup": 2100,
    "codigo_barra": 40252
  },
  {
    "id_erp": 40425,
    "nome": "PE MAD DIANTEIRO P0124 510 X 50 X 40MM DIREITO - POLTRONA JADE",
    "equipamentos": [
      3
    ],
    "tempo": 15,
    "setup": 2100,
    "codigo_barra": 40425
  },
  {
    "id_erp": 40426,
    "nome": "PE MAD DIANTEIRO P0125 510 X 50 X 40MM ESQUERDO - POLTRONA JADE",
    "equipamentos": [
      3
    ],
    "tempo": 15,
    "setup": 2100,
    "codigo_barra": 40426
  },
  {
    "id_erp": 40427,
    "nome": "PE MAD TRASEIRO P0126 760 X 125 X 40MM DIREITO - POLTRONA JADE",
    "equipamentos": [
      3
    ],
    "tempo": 25,
    "setup": 2100,
    "codigo_barra": 40427
  },
  {
    "id_erp": 40428,
    "nome": "PE MAD TRASEIRO P0127 760 X 125 X 40MM ESQUERDO - POLTRONA JADE",
    "equipamentos": [
      3
    ],
    "tempo": 25,
    "setup": 2100,
    "codigo_barra": 40428
  },
  {
    "id_erp": 40505,
    "nome": "TRAVESSA MAD LATERAL T0268 550 X 50 X 40MM - POLTRONA JADE",
    "equipamentos": [
      2
    ],
    "tempo": 44,
    "setup": 2100,
    "codigo_barra": 40505
  },
  {
    "id_erp": 40595,
    "nome": "PE MAD P0003 335 X 80 X 31MM CANTO (SOFÁ SAUÍPE)",
    "equipamentos": [
      2
    ],
    "tempo": 76,
    "setup": 2100,
    "codigo_barra": 40595
  },
  {
    "id_erp": 40595,
    "nome": "PE MAD P0003 335 X 80 X 31MM CANTO (SOFÁ SAUÍPE)",
    "equipamentos": [
      1
    ],
    "tempo": 76,
    "setup": 2100,
    "codigo_barra": 40595
  },
  {
    "id_erp": 40664,
    "nome": "PE MAD TRASEIRO P0128 640 X 42 X 32MM ESQUERDO - CADEIRA DUDA",
    "equipamentos": [
      3
    ],
    "tempo": 12,
    "setup": 900,
    "codigo_barra": 40664
  },
  {
    "id_erp": 40668,
    "nome": "PE MAD TRASEIRO P0129 640 X 42 X 32MM DIREITO - CADEIRA DUDA",
    "equipamentos": [
      3
    ],
    "tempo": 12,
    "setup": 2100,
    "codigo_barra": 40668
  },
  {
    "id_erp": 41839,
    "nome": "PE MAD TRASEIRO P0130 824 X 66 X 30MM DIREITO - CADEIRA ALICE C/BRACO",
    "equipamentos": [
      3
    ],
    "tempo": 14,
    "setup": 2100,
    "codigo_barra": 41839
  },
  {
    "id_erp": 41840,
    "nome": "PE MAD TRASEIRO P0131 824 X 66 X 30MM ESQUERDA - CADEIRA ALICE C/BRACO",
    "equipamentos": [
      3
    ],
    "tempo": 14,
    "setup": 2100,
    "codigo_barra": 41840
  },
  {
    "id_erp": 41881,
    "nome": "PE MAD TRASEIRO P0132 765 X 80 X 32MM DIREITO - CADEIRA LIA",
    "equipamentos": [
      3
    ],
    "tempo": 25,
    "setup": 3600,
    "codigo_barra": 41881
  },
  {
    "id_erp": 41881,
    "nome": "PE MAD TRASEIRO P0132 765 X 80 X 32MM DIREITO - CADEIRA LIA",
    "equipamentos": [
      1
    ],
    "tempo": 25,
    "setup": 3600,
    "codigo_barra": 41881
  },
  {
    "id_erp": 41882,
    "nome": "PE MAD TRASEIRO P0133 765 X 80 X 32MM ESQUERDO - CADEIRA LIA",
    "equipamentos": [
      3
    ],
    "tempo": 25,
    "setup": 0,
    "codigo_barra": 41882
  },
  {
    "id_erp": 41882,
    "nome": "PE MAD TRASEIRO P0133 765 X 80 X 32MM ESQUERDO - CADEIRA LIA",
    "equipamentos": [
      1
    ],
    "tempo": 25,
    "setup": 0,
    "codigo_barra": 41882
  },
  {
    "id_erp": 41883,
    "nome": "PE MAD DIANTEIRO P0134 435 X 80 X 32MM DIREITO - CADEIRA LIA/LIA LX",
    "equipamentos": [
      3
    ],
    "tempo": 11,
    "setup": 3600,
    "codigo_barra": 41883
  },
  {
    "id_erp": 41883,
    "nome": "PE MAD DIANTEIRO P0134 435 X 80 X 32MM DIREITO - CADEIRA LIA/LIA LX",
    "equipamentos": [
      1
    ],
    "tempo": 16,
    "setup": 3600,
    "codigo_barra": 41883
  },
  {
    "id_erp": 41884,
    "nome": "PE MAD DIANTEIRO P0135 435 X 80 X 32MM ESQUERDO - CADEIRA LIA/LIA LX",
    "equipamentos": [
      3
    ],
    "tempo": 11,
    "setup": 0,
    "codigo_barra": 41884
  },
  {
    "id_erp": 41884,
    "nome": "PE MAD DIANTEIRO P0135 435 X 80 X 32MM ESQUERDO - CADEIRA LIA/LIA LX",
    "equipamentos": [
      1
    ],
    "tempo": 16,
    "setup": 0,
    "codigo_barra": 41884
  },
  {
    "id_erp": 41885,
    "nome": "TRAVESSA MAD TRASEIRA T0274 485 X 95 X 32MM - CADEIRA LIA",
    "equipamentos": [
      2
    ],
    "tempo": 28,
    "setup": 2100,
    "codigo_barra": 41885
  },
  {
    "id_erp": 41885,
    "nome": "TRAVESSA MAD TRASEIRA T0274 485 X 95 X 32MM - CADEIRA LIA",
    "equipamentos": [
      1
    ],
    "tempo": 28,
    "setup": 2100,
    "codigo_barra": 41885
  },
  {
    "id_erp": 41886,
    "nome": "TRAVESSA MAD DIANTEIRA T0275 450 X 60 X 23MM - CADEIRA LIA",
    "equipamentos": [
      2
    ],
    "tempo": 28,
    "setup": 2100,
    "codigo_barra": 41886
  },
  {
    "id_erp": 41886,
    "nome": "TRAVESSA MAD DIANTEIRA T0275 450 X 60 X 23MM - CADEIRA LIA",
    "equipamentos": [
      1
    ],
    "tempo": 28,
    "setup": 2100,
    "codigo_barra": 41886
  },
  {
    "id_erp": 41887,
    "nome": "TRAVESSA MAD LATERAL T0276 425 X 65 X 22MM ESQUERD - CADEIRA LIA",
    "equipamentos": [
      2
    ],
    "tempo": 20,
    "setup": 2100,
    "codigo_barra": 41887
  },
  {
    "id_erp": 41888,
    "nome": "TRAVESSA MAD LATERAL T0277 425 X 65 X 22MM DIREITA - CADEIRA LIA",
    "equipamentos": [
      2
    ],
    "tempo": 20,
    "setup": 2100,
    "codigo_barra": 41888
  },
  {
    "id_erp": 41919,
    "nome": "TRAVESSA MAD LATERAL T0281 632 X 80 X 18MM DIREITO - POLTRONA JADE MAD",
    "equipamentos": [
      2
    ],
    "tempo": 23,
    "setup": 2100,
    "codigo_barra": 41919
  },
  {
    "id_erp": 42193,
    "nome": "PE MAD TRASEIRO P0136 865 X 100 X 32MM DIREITO - CADEIRA CLAU/CLAU LAMINADA",
    "equipamentos": [
      3
    ],
    "tempo": 13,
    "setup": 2100,
    "codigo_barra": 42193
  },
  {
    "id_erp": 42193,
    "nome": "PE MAD TRASEIRO P0136 865 X 100 X 32MM DIREITO - CADEIRA CLAU/CLAU LAMINADA",
    "equipamentos": [
      1
    ],
    "tempo": 13,
    "setup": 2100,
    "codigo_barra": 42193
  },
  {
    "id_erp": 42194,
    "nome": "PE MAD TRASEIRO P0137 865 X 100 X 32MM ESQUERDO - CADEIRA CLAU",
    "equipamentos": [
      3
    ],
    "tempo": 12,
    "setup": 0,
    "codigo_barra": 42194
  },
  {
    "id_erp": 42194,
    "nome": "PE MAD TRASEIRO P0137 865 X 100 X 32MM ESQUERDO - CADEIRA CLAU",
    "equipamentos": [
      1
    ],
    "tempo": 12,
    "setup": 0,
    "codigo_barra": 42194
  },
  {
    "id_erp": 42195,
    "nome": "PE MAD DIANTEIRO P0138 465 X 77 X 32MM DIREITO - CADEIRA CLAU",
    "equipamentos": [
      3
    ],
    "tempo": 13,
    "setup": 0,
    "codigo_barra": 42195
  },
  {
    "id_erp": 42195,
    "nome": "PE MAD DIANTEIRO P0138 465 X 77 X 32MM DIREITO - CADEIRA CLAU",
    "equipamentos": [
      1
    ],
    "tempo": 13,
    "setup": 0,
    "codigo_barra": 42195
  },
  {
    "id_erp": 42196,
    "nome": "PE MAD DIANTEIRO P0139 465 X 77 X 32MM ESQUESDO - CADEIRA CLAU",
    "equipamentos": [
      3
    ],
    "tempo": 12,
    "setup": 2100,
    "codigo_barra": 42196
  },
  {
    "id_erp": 42196,
    "nome": "PE MAD DIANTEIRO P0139 465 X 77 X 32MM ESQUESDO - CADEIRA CLAU",
    "equipamentos": [
      1
    ],
    "tempo": 12,
    "setup": 2100,
    "codigo_barra": 42196
  },
  {
    "id_erp": 42197,
    "nome": "TRAVESSA MAD T0312 380 X 30 X 32MM - CADEIRA CLAU",
    "equipamentos": [
      2
    ],
    "tempo": 41,
    "setup": 2100,
    "codigo_barra": 42197
  },
  {
    "id_erp": 42198,
    "nome": "TRAVESSA MAD T0313 420 X 50 X 22MM - CADEIRA CLAU",
    "equipamentos": [
      2
    ],
    "tempo": 23,
    "setup": 2100,
    "codigo_barra": 42198
  },
  {
    "id_erp": 42198,
    "nome": "TRAVESSA MAD T0313 420 X 50 X 22MM - CADEIRA CLAU",
    "equipamentos": [
      1
    ],
    "tempo": 23,
    "setup": 2100,
    "codigo_barra": 42198
  },
  {
    "id_erp": 42199,
    "nome": "TRAVESSA MAD DIANTEIRA T0314 400 X 60 X 22MM - CADEIRA CLAU",
    "equipamentos": [
      2
    ],
    "tempo": 22,
    "setup": 0,
    "codigo_barra": 42199
  },
  {
    "id_erp": 42199,
    "nome": "TRAVESSA MAD DIANTEIRA T0314 400 X 60 X 22MM - CADEIRA CLAU",
    "equipamentos": [
      1
    ],
    "tempo": 22,
    "setup": 0,
    "codigo_barra": 42199
  },
  {
    "id_erp": 42200,
    "nome": "TRAVESSA MAD LATERAL T0315 527 X 65 X 22MM DIREITA - CADEIRA CLAU",
    "equipamentos": [
      3
    ],
    "tempo": 13,
    "setup": 2100,
    "codigo_barra": 42200
  },
  {
    "id_erp": 42200,
    "nome": "TRAVESSA MAD LATERAL T0315 527 X 65 X 22MM DIREITA - CADEIRA CLAU",
    "equipamentos": [
      1
    ],
    "tempo": 13,
    "setup": 2100,
    "codigo_barra": 42200
  },
  {
    "id_erp": 42201,
    "nome": "TRAVESSA MAD LATERAL T0316 527 X 65 X 22MM ESQUERD - CADEIRA CLAU",
    "equipamentos": [
      3
    ],
    "tempo": 12,
    "setup": 0,
    "codigo_barra": 42201
  },
  {
    "id_erp": 42201,
    "nome": "TRAVESSA MAD LATERAL T0316 527 X 65 X 22MM ESQUERD - CADEIRA CLAU",
    "equipamentos": [
      1
    ],
    "tempo": 12,
    "setup": 0,
    "codigo_barra": 42201
  },
  {
    "id_erp": 42675,
    "nome": "PE MAD TRASEIRO P0140 915 X 42 X 32MM DIREITO - CADEIRA OMEGA",
    "equipamentos": [
      3
    ],
    "tempo": 16,
    "setup": 2100,
    "codigo_barra": 42675
  },
  {
    "id_erp": 42676,
    "nome": "PE MAD TRASEIRO P0141 915 X 42 X 32MM ESQUERDO - CADEIRA OMEGA",
    "equipamentos": [
      3
    ],
    "tempo": 16,
    "setup": 2100,
    "codigo_barra": 42676
  },
  {
    "id_erp": 42679,
    "nome": "TRAVESSA MAD DIANTEIRA T0317 450 X 55 X 22MM - CADEIRA PROVENCE/CELINE/OMEGA/BETTY/LAINE",
    "equipamentos": [
      2
    ],
    "tempo": 13,
    "setup": 2100,
    "codigo_barra": 42679
  },
  {
    "id_erp": 42680,
    "nome": "TRAVESSA MAD T0318 380 X 25 X 32MM INF ENC - CADEIRA PROVENCE/CELINE/OMEGA/BETTY/LAINE",
    "equipamentos": [
      2
    ],
    "tempo": 14,
    "setup": 2100,
    "codigo_barra": 42680
  },
  {
    "id_erp": 42681,
    "nome": "TRAVESSA MAD T0319 445 X 25 X 32MM - CADEIRA PROVENCE/CELINE/OMEGA",
    "equipamentos": [
      2
    ],
    "tempo": 13,
    "setup": 2100,
    "codigo_barra": 42681
  },
  {
    "id_erp": 42682,
    "nome": "TRAVESSA MAD TRASEIRA T0320 385 X 28 X 55MM - CADEIRA PROVENCE/CELINE/OMEGA/BETTY/LAINE",
    "equipamentos": [
      2
    ],
    "tempo": 12,
    "setup": 2100,
    "codigo_barra": 42682
  },
  {
    "id_erp": 42683,
    "nome": "TRAVESSA MAD LATERAL T0321 425 X 43 X 55MM DIREITA - CADEIRA PROVENCE/CELINE/OMEGA/BETTY/LAINE",
    "equipamentos": [
      2
    ],
    "tempo": 14,
    "setup": 2100,
    "codigo_barra": 42683
  },
  {
    "id_erp": 42683,
    "nome": "TRAVESSA MAD LATERAL T0321 425 X 43 X 55MM DIREITA - CADEIRA PROVENCE/CELINE/OMEGA/BETTY/LAINE",
    "equipamentos": [
      3
    ],
    "tempo": 14,
    "setup": 2100,
    "codigo_barra": 42683
  },
  {
    "id_erp": 42684,
    "nome": "TRAVESSA MAD LATERAL T0322 425 X 43 X 55MM ESQUERD - CADEIRA PROVENCE/CELINE/OMEGA/BETTY/LAINE",
    "equipamentos": [
      2
    ],
    "tempo": 14,
    "setup": 2100,
    "codigo_barra": 42684
  },
  {
    "id_erp": 42684,
    "nome": "TRAVESSA MAD LATERAL T0322 425 X 43 X 55MM ESQUERD - CADEIRA PROVENCE/CELINE/OMEGA/BETTY/LAINE",
    "equipamentos": [
      3
    ],
    "tempo": 14,
    "setup": 2100,
    "codigo_barra": 42684
  },
  {
    "id_erp": 42696,
    "nome": "PE MAD TRASEIRO P0144 915 X 110 X 32MM DIREITO - CADEIRA PROVENCE/CELINE",
    "equipamentos": [
      3
    ],
    "tempo": 16,
    "setup": 2100,
    "codigo_barra": 42696
  },
  {
    "id_erp": 42697,
    "nome": "PE MAD TRASEIRO P0145 915 X 110 X 32MM ESQUERDO - CADEIRA PROVENCE/CELINE",
    "equipamentos": [
      3
    ],
    "tempo": 16,
    "setup": 2100,
    "codigo_barra": 42697
  },
  {
    "id_erp": 43078,
    "nome": "TRAVESSA MAD T0633 500 X 60 X 32MM - MESA LINEA",
    "equipamentos": [
      2
    ],
    "tempo": 27,
    "setup": 5700,
    "codigo_barra": 43078
  },
  {
    "id_erp": 43079,
    "nome": "TRAVESSA MAD T0634 720 X 40 X 32MM - MESA MENFIS",
    "equipamentos": [
      2
    ],
    "tempo": 23,
    "setup": 2100,
    "codigo_barra": 43079
  },
  {
    "id_erp": 43162,
    "nome": "TRAVESSA MAD T0636 1698 X 60 X 32MM MAIOR - HOME/BUFFET VEDRA",
    "equipamentos": [
      2
    ],
    "tempo": 35,
    "setup": 2100,
    "codigo_barra": 43162
  },
  {
    "id_erp": 43281,
    "nome": "TRAVESSA MAD T0641 868 X 60 X 32MM MAIOR - ARMARIO VEDRA",
    "equipamentos": [
      2
    ],
    "tempo": 35,
    "setup": 2100,
    "codigo_barra": 43281
  },
  {
    "id_erp": 43364,
    "nome": "PE MAD TRASEIRO P0150 890 X 46 X 32MM DIREITO - CADEIRA MAIA RATAN",
    "equipamentos": [
      3
    ],
    "tempo": 14,
    "setup": 2100,
    "codigo_barra": 43364
  },
  {
    "id_erp": 43365,
    "nome": "PE MAD TRASEIRO P0151 890 X 46 X 32MM ESQUERDO - CADEIRA MAIA RATAN",
    "equipamentos": [
      3
    ],
    "tempo": 14,
    "setup": 2100,
    "codigo_barra": 43365
  },
  {
    "id_erp": 43368,
    "nome": "TRAVESSA MAD TRASEIRA T0327 428 X 80 X 32MM - CADEIRA MAIA RATAN",
    "equipamentos": [
      2
    ],
    "tempo": 27,
    "setup": 2100,
    "codigo_barra": 43368
  },
  {
    "id_erp": 43514,
    "nome": "PE MAD TRASEIRO P0152 415 X 65 X 45MM ESQUERDO - POLTRONA TINA/CLARA",
    "equipamentos": [
      3
    ],
    "tempo": 18,
    "setup": 1200,
    "codigo_barra": 43514
  },
  {
    "id_erp": 43515,
    "nome": "PE MAD TRASEIRO P0153 415 X 65 X 45MM DIREITO - POLTRONA TINA/CLARA",
    "equipamentos": [
      3
    ],
    "tempo": 18,
    "setup": 1200,
    "codigo_barra": 43515
  },
  {
    "id_erp": 43516,
    "nome": "PE MAD DIANTEIRO P0154 403 X 65 X 45MM ESQUERDO - POLTRONA TINA/CLARA",
    "equipamentos": [
      3
    ],
    "tempo": 18,
    "setup": 1500,
    "codigo_barra": 43516
  },
  {
    "id_erp": 43517,
    "nome": "PE MAD DIANTEIRO P0155 403 X 65 X 45MM DIREITO - POLTRONA TINA/CLARA",
    "equipamentos": [
      3
    ],
    "tempo": 18,
    "setup": 1500,
    "codigo_barra": 43517
  },
  {
    "id_erp": 43518,
    "nome": "TRAVESSA MAD LATERAL T0333 515 X 63 X 32MM DIREITA - POLTRONA TINA/CLARA",
    "equipamentos": [
      2
    ],
    "tempo": 45,
    "setup": 2100,
    "codigo_barra": 43518
  },
  {
    "id_erp": 43869,
    "nome": "PE MAD P0156 750 X 96 X 32MM - BANQUETA MANARI",
    "equipamentos": [
      3
    ],
    "tempo": 18,
    "setup": 2100,
    "codigo_barra": 43869
  },
  {
    "id_erp": 44265,
    "nome": "PE MAD P0007 900 X 80 X 45MM (SOFA ENZO)",
    "equipamentos": [
      2
    ],
    "tempo": 94,
    "setup": 2100,
    "codigo_barra": 44265
  },
  {
    "id_erp": 44339,
    "nome": "PE MAD TRASEIRO P0157 970 X 110 X 32MM DIREITO - BANQUETA LIA 1030",
    "equipamentos": [
      3
    ],
    "tempo": 20,
    "setup": 2400,
    "codigo_barra": 44339
  },
  {
    "id_erp": 44340,
    "nome": "PE MAD TRASEIRO P0158 970 X 110 X 32MM ESQUERDO - BANQUETA LIA 1030",
    "equipamentos": [
      3
    ],
    "tempo": 20,
    "setup": 0,
    "codigo_barra": 44340
  },
  {
    "id_erp": 44341,
    "nome": "PE MAD DIANTEIRO P0159 1070 X 80 X 32MM DIREITO - BANQUETA LIA 1030",
    "equipamentos": [
      3
    ],
    "tempo": 20,
    "setup": 600,
    "codigo_barra": 44341
  },
  {
    "id_erp": 44342,
    "nome": "PE MAD DIANTEIRO P0160 1070 X 80 X 32MM ESQUERDO - BANQUETA LIA 1030",
    "equipamentos": [
      3
    ],
    "tempo": 20,
    "setup": 0,
    "codigo_barra": 44342
  },
  {
    "id_erp": 44444,
    "nome": "TRAV. MAIOR ESQ. SOFA KAUÊ",
    "equipamentos": [
      2
    ],
    "tempo": 72,
    "setup": 2100,
    "codigo_barra": 44444
  },
  {
    "id_erp": 44445,
    "nome": "TRAV. MAIOR DIR. SOFA KAUÊ",
    "equipamentos": [
      2
    ],
    "tempo": 72,
    "setup": 2100,
    "codigo_barra": 44445
  },
  {
    "id_erp": 44446,
    "nome": "PÉS SOFA KAUÊ",
    "equipamentos": [
      2
    ],
    "tempo": 62,
    "setup": 2100,
    "codigo_barra": 44446
  },
  {
    "id_erp": 44522,
    "nome": "PE MAD P0006 110 X 60 X 45MM (SOFA ITAMBE)",
    "equipamentos": [
      3
    ],
    "tempo": 17,
    "setup": 2100,
    "codigo_barra": 44522
  },
  {
    "id_erp": 44525,
    "nome": "TRAV. MAD T0457 1560 X 60 X 32MM (SOFA ITAMBE)",
    "equipamentos": [
      3
    ],
    "tempo": 41,
    "setup": 2100,
    "codigo_barra": 44525
  },
  {
    "id_erp": 44547,
    "nome": "TRAV. MAD T0459 860 X 60 X 32MM (SOFA ITAMBE)",
    "equipamentos": [
      3
    ],
    "tempo": 39,
    "setup": 2100,
    "codigo_barra": 44547
  },
  {
    "id_erp": 45087,
    "nome": "PE MAD TRASEIRO P0163 890 X 47 X 32MM DIREITO - CADEIRA LAURA",
    "equipamentos": [
      3
    ],
    "tempo": 13,
    "setup": 2100,
    "codigo_barra": 45087
  },
  {
    "id_erp": 45088,
    "nome": "PE MAD TRASEIRO P0167 890 X 47 X 32MM ESQUERDO - CADEIRA LAURA",
    "equipamentos": [
      3
    ],
    "tempo": 13,
    "setup": 2100,
    "codigo_barra": 45088
  },
  {
    "id_erp": 45089,
    "nome": "FRONTAL MAD  F0016 420 X 28 X 28MM - CADEIRA LAURA (FRON. INF.)",
    "equipamentos": [
      2
    ],
    "tempo": 17,
    "setup": 2100,
    "codigo_barra": 45089
  },
  {
    "id_erp": 45093,
    "nome": "FRONTAL MAD  F0017 420 X 28 X 28MM - CADEIRA LAURA (FRON. SUP.)",
    "equipamentos": [
      2
    ],
    "tempo": 17,
    "setup": 0,
    "codigo_barra": 45093
  },
  {
    "id_erp": 45167,
    "nome": "PE MAD TRASEIRO P0168 690 X 50 X 45MM DIREITA - POLTRONA BOTANIC",
    "equipamentos": [
      3
    ],
    "tempo": 33,
    "setup": 2100,
    "codigo_barra": 45167
  },
  {
    "id_erp": 45168,
    "nome": "PE MAD TRASEIRO P0169 690 X 50 X 45MM ESQUERDO - POLTRONA BOTANIC",
    "equipamentos": [
      3
    ],
    "tempo": 33,
    "setup": 2100,
    "codigo_barra": 45168
  },
  {
    "id_erp": 45169,
    "nome": "PE MAD DIANTEIRO P0170 690 X 45 X 45MM DIREITO - POLTRONA BOTANIC",
    "equipamentos": [
      3
    ],
    "tempo": 25,
    "setup": 600,
    "codigo_barra": 45169
  },
  {
    "id_erp": 45171,
    "nome": "TRAVESSA MAD T0370 350 X 47 X 47MM DIREITA - POLTRONA BOTANIC (TRAV. BRACO)",
    "equipamentos": [
      2
    ],
    "tempo": 53,
    "setup": 2100,
    "codigo_barra": 45171
  },
  {
    "id_erp": 45172,
    "nome": "TRAVESSA MAD T0371 350 X 47 X 47MM ESQUERDA - POLTRONA BOTANIC (TRAV. BRACO)",
    "equipamentos": [
      2
    ],
    "tempo": 53,
    "setup": 2100,
    "codigo_barra": 45172
  },
  {
    "id_erp": 45173,
    "nome": "TRAVESSA MAD DIANTEIRA T0372 538 X 80 X 22MM - POLTRONA BOTANIC",
    "equipamentos": [
      2
    ],
    "tempo": 64,
    "setup": 6300,
    "codigo_barra": 45173
  },
  {
    "id_erp": 45174,
    "nome": "PE MAD DIANTEIRO P0472 690 X 45 X 45MM ESQUERDO - POLTRONA BOTANIC",
    "equipamentos": [
      3
    ],
    "tempo": 25,
    "setup": 600,
    "codigo_barra": 45174
  },
  {
    "id_erp": 45175,
    "nome": "TRAVESSA MAD TRASEIRA T0373 538 X 80 X 22MM - POLTRONA BOTANIC",
    "equipamentos": [
      2
    ],
    "tempo": 67,
    "setup": 4920,
    "codigo_barra": 45175
  },
  {
    "id_erp": 45176,
    "nome": "TRAVESSA MAD LATERAL T0374 405 X 40 X 22MM DIREITA - POLTRONA BOTANIC",
    "equipamentos": [
      2
    ],
    "tempo": 28,
    "setup": 3420,
    "codigo_barra": 45176
  },
  {
    "id_erp": 45177,
    "nome": "TRAVESSA MAD LATERAL T0375 405 X 40 X 22MM ESQUERD - POLTRONA BOTANIC",
    "equipamentos": [
      2
    ],
    "tempo": 28,
    "setup": 0,
    "codigo_barra": 45177
  },
  {
    "id_erp": 45233,
    "nome": "TRAV. PINTADA T004 715 X 100 X 40MM (FRENTE) - POLTRONA ITAUNA",
    "equipamentos": [
      2
    ],
    "tempo": 58,
    "setup": 2100,
    "codigo_barra": 45233
  },
  {
    "id_erp": 45234,
    "nome": "TRAV. PINTADA T005 675 X 115 X 40MM (TRASEIRA) - POLTRONA ITAUNA",
    "equipamentos": [
      2
    ],
    "tempo": 56,
    "setup": 2100,
    "codigo_barra": 45234
  },
  {
    "id_erp": 45235,
    "nome": "TRAV. PINTADA T006 625 X 100 X 40MM (LATERAL) - POLTRONA ITAUNA",
    "equipamentos": [
      2
    ],
    "tempo": 67,
    "setup": 2100,
    "codigo_barra": 45235
  },
  {
    "id_erp": 45236,
    "nome": "PE PINTADO MAD P0364 210 X 48 X 35MM - POLT/SOFA ITAUNA",
    "equipamentos": [
      2
    ],
    "tempo": 21,
    "setup": 2100,
    "codigo_barra": 45236
  },
  {
    "id_erp": 45237,
    "nome": "PE PINTADO MAD T0365 210 X 48 X 35MM - POLT/SOFA ITAUNA",
    "equipamentos": [
      2
    ],
    "tempo": 21,
    "setup": 2100,
    "codigo_barra": 45237
  },
  {
    "id_erp": 45238,
    "nome": "PE PINTADO MAD T0366 216 X 48 X 35MM - POLT/SOFA ITAUNA",
    "equipamentos": [
      2
    ],
    "tempo": 21,
    "setup": 2100,
    "codigo_barra": 45238
  },
  {
    "id_erp": 45239,
    "nome": "PE PINTADO MAD T0367 216 X 48 X 35MM - POLT/SOFA ITAUNA",
    "equipamentos": [
      2
    ],
    "tempo": 21,
    "setup": 2100,
    "codigo_barra": 45239
  },
  {
    "id_erp": 45254,
    "nome": "JOGO DE PES P/ ESTOFADO ITAUNA",
    "equipamentos": [
      2
    ],
    "tempo": 80,
    "setup": 2100,
    "codigo_barra": 45254
  },
  {
    "id_erp": 45477,
    "nome": "PE MAD TRASEIRO P0473 630 X 50 X 32MM DIREITO - CADEIRA MANU",
    "equipamentos": [
      3
    ],
    "tempo": 11,
    "setup": 2100,
    "codigo_barra": 45477
  },
  {
    "id_erp": 45478,
    "nome": "PE MAD TRASEIRO P0474 630 X 50 X 32MM ESQUERDO - CADEIRA MANU",
    "equipamentos": [
      3
    ],
    "tempo": 11,
    "setup": 2100,
    "codigo_barra": 45478
  },
  {
    "id_erp": 45479,
    "nome": "PE MAD DIANTEIRO P0475 430 X 45 X 32MM DIREITO - CADEIRA MANU",
    "equipamentos": [
      3
    ],
    "tempo": 11,
    "setup": 1800,
    "codigo_barra": 45479
  },
  {
    "id_erp": 45480,
    "nome": "PE MAD DIANTEIRO P0476 430 X 45 X 32MM ESQUERDO - CADEIRA MANU",
    "equipamentos": [
      3
    ],
    "tempo": 11,
    "setup": 1800,
    "codigo_barra": 45480
  },
  {
    "id_erp": 45481,
    "nome": "TRAVESSA MAD LATERAL T0376 440 X 90 X 32MM DIREITA - CADEIRA MANU",
    "equipamentos": [
      2
    ],
    "tempo": 50,
    "setup": 4980,
    "codigo_barra": 45481
  },
  {
    "id_erp": 45482,
    "nome": "TRAVESSA MAD LATERAL T0377 440 X 90 X 32MM ESQERDA - CADEIRA MANU",
    "equipamentos": [
      2
    ],
    "tempo": 50,
    "setup": 0,
    "codigo_barra": 45482
  },
  {
    "id_erp": 45483,
    "nome": "TRAVESSA MAD DIANTEIRA T0378 410 X 50 X 22MM - CADEIRA MANU",
    "equipamentos": [
      2
    ],
    "tempo": 20,
    "setup": 2100,
    "codigo_barra": 45483
  },
  {
    "id_erp": 45535,
    "nome": "TRAV. PINTADA T0007 1507 X 75 X 40MM (FRENTE) - SOFA ITAUNA 1650",
    "equipamentos": [
      2
    ],
    "tempo": 89,
    "setup": 2100,
    "codigo_barra": 45535
  },
  {
    "id_erp": 45536,
    "nome": "TRAV. PINTADA T0008 1465 X 115 X 40MM (TRASEIRA) - SOFA ITAUNA 1650",
    "equipamentos": [
      2
    ],
    "tempo": 91,
    "setup": 2100,
    "codigo_barra": 45536
  },
  {
    "id_erp": 45537,
    "nome": "TRAV. PINTADA T0009 606 X 93 X 40MM (LATERAL) - SOFA ITAUNA 1650",
    "equipamentos": [
      2
    ],
    "tempo": 67,
    "setup": 2100,
    "codigo_barra": 45537
  },
  {
    "id_erp": 45653,
    "nome": "PE MAD TRASEIRO P0477 575 X 40 X 40MM DIREITA - CADEIRA DALIA",
    "equipamentos": [
      3
    ],
    "tempo": 13,
    "setup": 4500,
    "codigo_barra": 45653
  },
  {
    "id_erp": 45654,
    "nome": "PE MAD TRASEIRO P0478 575 X 40 X 40MM ESQUERDO - CADEIRA DALIA",
    "equipamentos": [
      3
    ],
    "tempo": 12,
    "setup": 0,
    "codigo_barra": 45654
  },
  {
    "id_erp": 45655,
    "nome": "PE MAD DIANTEIRO P0479 418 X 40 X 40MM - CADEIRA DALIA",
    "equipamentos": [
      3
    ],
    "tempo": 10,
    "setup": 3600,
    "codigo_barra": 45655
  },
  {
    "id_erp": 45656,
    "nome": "PE MAD DIANTEIRO P0480 418 X 40 X 40MM ESQUERDO - CADEIRA DALIA",
    "equipamentos": [
      3
    ],
    "tempo": 10,
    "setup": 0,
    "codigo_barra": 45656
  },
  {
    "id_erp": 45657,
    "nome": "TRAVESSA MAD DIANTEIRA T0380 450 X 50 X 22MM - CADEIRA DALIA",
    "equipamentos": [
      2
    ],
    "tempo": 35,
    "setup": 2100,
    "codigo_barra": 45657
  },
  {
    "id_erp": 45658,
    "nome": "TRAVESSA MAD LATERAL T0381 390 X 55 X 32MM DIREITA - CADEIRA DALIA",
    "equipamentos": [
      2
    ],
    "tempo": 34,
    "setup": 2100,
    "codigo_barra": 45658
  },
  {
    "id_erp": 45659,
    "nome": "TRAVESSA MAD LATERAL T0382 390 X 55 X 32MM ESQUERD - CADEIRA DALIA",
    "equipamentos": [
      2
    ],
    "tempo": 34,
    "setup": 0,
    "codigo_barra": 45659
  },
  {
    "id_erp": 45660,
    "nome": "TRAVESSA MAD TRASEIRA T0383 470 X 45 X 22MM - CADEIRA DALIA",
    "equipamentos": [
      2
    ],
    "tempo": 35,
    "setup": 0,
    "codigo_barra": 45660
  },
  {
    "id_erp": 45787,
    "nome": "TRAV. PINTADA T0054 1480 X 75 X 40MM(COMPLEMENTO BASE ITAUNA 1590 ESQ)",
    "equipamentos": [
      2
    ],
    "tempo": 90,
    "setup": 2100,
    "codigo_barra": 45787
  },
  {
    "id_erp": 45815,
    "nome": "TRAV. PINTADA T0057 840 X 85 X 40MM (FRENTE)",
    "equipamentos": [
      2
    ],
    "tempo": 70,
    "setup": 2100,
    "codigo_barra": 45815
  },
  {
    "id_erp": 45878,
    "nome": "TRAVESSA MAD T0690 700 X 50 X 32MM MAIOR - MESA JANTAR UOMINI",
    "equipamentos": [
      3
    ],
    "tempo": 50,
    "setup": 5400,
    "codigo_barra": 45878
  },
  {
    "id_erp": 46083,
    "nome": "PE MAD P0481 415 X 60 X 28MM - BANCO YAGO 1,60/1,80 (PE)",
    "equipamentos": [
      3
    ],
    "tempo": 40,
    "setup": 5400,
    "codigo_barra": 46083
  },
  {
    "id_erp": 46084,
    "nome": "TRAVESSA MAD T0385 415 X 60 X 28MM - BANCO YAGO 1,60/1,80 (PE)",
    "equipamentos": [
      3
    ],
    "tempo": 40,
    "setup": 0,
    "codigo_barra": 46084
  },
  {
    "id_erp": 46085,
    "nome": "TRAVESSA MAD T0386 480 X 75 X 45MM MENOR - BANCO YAGO 1,60/1,80",
    "equipamentos": [
      2
    ],
    "tempo": 34,
    "setup": 4500,
    "codigo_barra": 46085
  },
  {
    "id_erp": 46085,
    "nome": "TRAVESSA MAD T0386 480 X 75 X 45MM MENOR - BANCO YAGO 1,60/1,80",
    "equipamentos": [
      1
    ],
    "tempo": 34,
    "setup": 4500,
    "codigo_barra": 46085
  },
  {
    "id_erp": 46086,
    "nome": "TRAVESSA MAD T0387 1785 X 75 X 45MM MAIOR - BANCO YAGO 1,80",
    "equipamentos": [
      2
    ],
    "tempo": 26,
    "setup": 2100,
    "codigo_barra": 46086
  },
  {
    "id_erp": 46136,
    "nome": "PE MAD DIANTEIRO P0482 470 X 42 X 42MM - CADEIRA NANDA",
    "equipamentos": [
      3
    ],
    "tempo": 13,
    "setup": 2100,
    "codigo_barra": 46136
  },
  {
    "id_erp": 46137,
    "nome": "PE MAD TRASEIRO P0483 470 X 42 X 42MM DIREITO - CADEIRA NANDA",
    "equipamentos": [
      3
    ],
    "tempo": 13,
    "setup": 2100,
    "codigo_barra": 46137
  },
  {
    "id_erp": 46138,
    "nome": "TRAVESSA MAD T0388 480 X 60 X 32MM - CADEIRA NANDA (EM X)",
    "equipamentos": [
      2
    ],
    "tempo": 42,
    "setup": 2100,
    "codigo_barra": 46138
  },
  {
    "id_erp": 46158,
    "nome": "PE MAD DIANTEIRO P0008 252 X 52 X 40MM ESQUERDA - POLTRONA CAIENA",
    "equipamentos": [
      3
    ],
    "tempo": 4,
    "setup": 2100,
    "codigo_barra": 46158
  },
  {
    "id_erp": 46159,
    "nome": "PE MAD TRASEIRO P0009 265 X 52 X 40MM - POLTRONA CAIENA",
    "equipamentos": [
      3
    ],
    "tempo": 8,
    "setup": 2100,
    "codigo_barra": 46159
  },
  {
    "id_erp": 46160,
    "nome": "TRAVESSA MAD  T0628 685 X 35 X 32MM - POLTRONA CAIENA DIREITA",
    "equipamentos": [
      2
    ],
    "tempo": 17,
    "setup": 2100,
    "codigo_barra": 46160
  },
  {
    "id_erp": 46161,
    "nome": "TRAVESSA MAD  T0629 685 X 35 X 32MM - POLTRONA CAIENA ESQUERDA",
    "equipamentos": [
      2
    ],
    "tempo": 17,
    "setup": 2100,
    "codigo_barra": 46161
  },
  {
    "id_erp": 46252,
    "nome": "TRAVESSA MAD T0695 470 X 110 X 45MM MENOR - BUFFET/BAR TAMBORE",
    "equipamentos": [
      2
    ],
    "tempo": 90,
    "setup": 2100,
    "codigo_barra": 46252
  },
  {
    "id_erp": 46252,
    "nome": "TRAVESSA MAD T0695 470 X 110 X 45MM MENOR - BUFFET/BAR TAMBORE",
    "equipamentos": [
      3
    ],
    "tempo": 90,
    "setup": 2100,
    "codigo_barra": 46252
  },
  {
    "id_erp": 46536,
    "nome": "PE MAD DIANTEIRO P0484 465 X 45 X 35MM DIR - POLTRONA RUBIA",
    "equipamentos": [
      3
    ],
    "tempo": 17,
    "setup": 2100,
    "codigo_barra": 46536
  },
  {
    "id_erp": 46537,
    "nome": "PE MAD DIANTEIRO P0485 465 X 45 X 35MM ESQ - POLTRONA RUBIA",
    "equipamentos": [
      3
    ],
    "tempo": 16,
    "setup": 2100,
    "codigo_barra": 46537
  },
  {
    "id_erp": 46538,
    "nome": "PE MAD TRASEIRO P0486 465 X 45 X 35MM DIR - POLTRONA RUBIA",
    "equipamentos": [
      3
    ],
    "tempo": 17,
    "setup": 2100,
    "codigo_barra": 46538
  },
  {
    "id_erp": 46539,
    "nome": "PE MAD TRASEIRO P0487 465 X 45 X 35MM ESQ - POLTRONA RUBIA",
    "equipamentos": [
      3
    ],
    "tempo": 16,
    "setup": 2100,
    "codigo_barra": 46539
  },
  {
    "id_erp": 46548,
    "nome": "TRAVESSA MAD LATERAL T0392 656 X 48 X 32MM ESQ - POLTRONA RUBIA",
    "equipamentos": [
      3
    ],
    "tempo": 19,
    "setup": 2100,
    "codigo_barra": 46548
  },
  {
    "id_erp": 46549,
    "nome": "TRAVESSA MAD TRASEIRA T0393 833 X 50 X 32MM - POLTRONA RUBIA",
    "equipamentos": [
      3
    ],
    "tempo": 18,
    "setup": 2100,
    "codigo_barra": 46549
  },
  {
    "id_erp": 46550,
    "nome": "TRAVESSA MAD T0416 1067 X 40 X 32MM ASS - POLTRONA RUBIA",
    "equipamentos": [
      2
    ],
    "tempo": 54,
    "setup": 2100,
    "codigo_barra": 46550
  },
  {
    "id_erp": 46551,
    "nome": "TRAVESSA MAD LATERAL T0394 656 X 48 X 32MM DIR - POLTRONA RUBIA",
    "equipamentos": [
      3
    ],
    "tempo": 19,
    "setup": 2100,
    "codigo_barra": 46551
  },
  {
    "id_erp": 46552,
    "nome": "TRAVESSA MAD T0395 1067 X 40 X 32MM ASS - POLTRONA RUBIA",
    "equipamentos": [
      2
    ],
    "tempo": 54,
    "setup": 2100,
    "codigo_barra": 46552
  },
  {
    "id_erp": 46876,
    "nome": "TRAVESSA MAD T0398 1585 X 75 X 45MM MAIOR - BANCO YAGO 1,60",
    "equipamentos": [
      2
    ],
    "tempo": 50,
    "setup": 4800,
    "codigo_barra": 46876
  },
  {
    "id_erp": 47014,
    "nome": "PE MAD TRASEIRO P0488 470 X 42 X 42MM ESQUEDO - CADEIRA NANDA",
    "equipamentos": [
      3
    ],
    "tempo": 12,
    "setup": 2100,
    "codigo_barra": 47014
  },
  {
    "id_erp": 47015,
    "nome": "PE MAD DIANTEIRO P0489 470 X 42 X 42MM ESQUERDO - CADEIRA NANDA",
    "equipamentos": [
      3
    ],
    "tempo": 12,
    "setup": 2100,
    "codigo_barra": 47015
  },
  {
    "id_erp": 47025,
    "nome": "TRAVESSA MAD T0399 480 X 60 X 32MM - CADEIRA NANDA (EM X)",
    "equipamentos": [
      2
    ],
    "tempo": 43,
    "setup": 2100,
    "codigo_barra": 47025
  },
  {
    "id_erp": 47039,
    "nome": "PE MAD P0010 145 X 50 X 40MM (SOFA LUNE) (4)",
    "equipamentos": [
      3
    ],
    "tempo": 14,
    "setup": 2100,
    "codigo_barra": 47039
  },
  {
    "id_erp": 47040,
    "nome": "TRAVESSA MAD  T0029 790 X 60 X 40MM - SOFA LUNE - DEIXAR NA MEDIDA 790 X 63 X 40 PARA DOUBLE JET",
    "equipamentos": [
      3
    ],
    "tempo": 14,
    "setup": 2100,
    "codigo_barra": 47040
  },
  {
    "id_erp": 47465,
    "nome": "PE MAD DIANTEIRO P0011 252 X 52 X 40MM DIREITA - POLTRONA CAIENA",
    "equipamentos": [
      3
    ],
    "tempo": 4,
    "setup": 2100,
    "codigo_barra": 47465
  },
  {
    "id_erp": 47703,
    "nome": "PE MAD DIANTEIRO P0490 425 X 45 X 32MM ESQ - CADEIRA JADE",
    "equipamentos": [
      3
    ],
    "tempo": 8,
    "setup": 2100,
    "codigo_barra": 47703
  },
  {
    "id_erp": 47704,
    "nome": "PE MAD DIANTEIRO P0491 425 X 45 X 32MM DIR - CADEIRA JADE/ARIEL/ESTER",
    "equipamentos": [
      3
    ],
    "tempo": 7,
    "setup": 2100,
    "codigo_barra": 47704
  },
  {
    "id_erp": 47705,
    "nome": "PE MAD TRASEIRO P0492 560 X 54 X 32MM ESQ - CADEIRA JADE/ARIEL/ESTER",
    "equipamentos": [
      3
    ],
    "tempo": 7,
    "setup": 2100,
    "codigo_barra": 47705
  },
  {
    "id_erp": 47706,
    "nome": "PE MAD TRASEIRO P0493 560 X 54 X 32MM DIR - CADEIRA JADE/ARIEL/ESTER",
    "equipamentos": [
      3
    ],
    "tempo": 7,
    "setup": 2100,
    "codigo_barra": 47706
  },
  {
    "id_erp": 47707,
    "nome": "TRAVESSA MAD LATERAL T0401 440 X 45 X 22MM ESQ - CADEIRA JADE/ARIEL/ESTER",
    "equipamentos": [
      2
    ],
    "tempo": 22,
    "setup": 2100,
    "codigo_barra": 47707
  },
  {
    "id_erp": 47708,
    "nome": "TRAVESSA MAD LATERAL P0402 440 X 45 X 22MM DIR - CADEIRA JADE/ARIEL/ESTER",
    "equipamentos": [
      2
    ],
    "tempo": 23,
    "setup": 2100,
    "codigo_barra": 47708
  },
  {
    "id_erp": 47768,
    "nome": "PE MAD DIANTEIRO P0494 435 X 40 X 35MM DIR - CADEIRA HARRY (IKEA)",
    "equipamentos": [
      2
    ],
    "tempo": 22,
    "setup": 2100,
    "codigo_barra": 47768
  },
  {
    "id_erp": 47768,
    "nome": "PE MAD DIANTEIRO P0494 435 X 40 X 35MM DIR - CADEIRA HARRY (IKEA)",
    "equipamentos": [
      3
    ],
    "tempo": 22,
    "setup": 2100,
    "codigo_barra": 47768
  },
  {
    "id_erp": 47769,
    "nome": "PE MAD DIANTEIRO P0495 435 X 40 X 35MM ESQ - CADEIRA HARRY (IKEA)",
    "equipamentos": [
      2
    ],
    "tempo": 23,
    "setup": 2100,
    "codigo_barra": 47769
  },
  {
    "id_erp": 47769,
    "nome": "PE MAD DIANTEIRO P0495 435 X 40 X 35MM ESQ - CADEIRA HARRY (IKEA)",
    "equipamentos": [
      3
    ],
    "tempo": 23,
    "setup": 2100,
    "codigo_barra": 47769
  },
  {
    "id_erp": 47770,
    "nome": "PE MAD TRASEIRO P0496 953 X 40 X 32MM DIR - CADEIRA HARRY (IKEA)",
    "equipamentos": [
      2
    ],
    "tempo": 34,
    "setup": 2100,
    "codigo_barra": 47770
  },
  {
    "id_erp": 47770,
    "nome": "PE MAD TRASEIRO P0496 953 X 40 X 32MM DIR - CADEIRA HARRY (IKEA)",
    "equipamentos": [
      3
    ],
    "tempo": 34,
    "setup": 2100,
    "codigo_barra": 47770
  },
  {
    "id_erp": 47771,
    "nome": "PE MAD TRASEIRO P0497 953 X 40 X 32MM ESQ - CADEIRA HARRY (IKEA)",
    "equipamentos": [
      2
    ],
    "tempo": 34,
    "setup": 2100,
    "codigo_barra": 47771
  },
  {
    "id_erp": 47771,
    "nome": "PE MAD TRASEIRO P0497 953 X 40 X 32MM ESQ - CADEIRA HARRY (IKEA)",
    "equipamentos": [
      3
    ],
    "tempo": 34,
    "setup": 2100,
    "codigo_barra": 47771
  },
  {
    "id_erp": 47774,
    "nome": "TRAVESSA MAD LATERAL T0404 370 X 65 X 25MM DIR - CADEIRA HARRY (IKEA)",
    "equipamentos": [
      2
    ],
    "tempo": 32,
    "setup": 2100,
    "codigo_barra": 47774
  },
  {
    "id_erp": 47774,
    "nome": "TRAVESSA MAD LATERAL T0404 370 X 65 X 25MM DIR - CADEIRA HARRY (IKEA)",
    "equipamentos": [
      3
    ],
    "tempo": 32,
    "setup": 2100,
    "codigo_barra": 47774
  },
  {
    "id_erp": 47775,
    "nome": "TRAVESSA MAD LATERAL T0405 370 X 65 X 25MM ESQ - CADEIRA HARRY (IKEA)",
    "equipamentos": [
      2
    ],
    "tempo": 31,
    "setup": 2100,
    "codigo_barra": 47775
  },
  {
    "id_erp": 47775,
    "nome": "TRAVESSA MAD LATERAL T0405 370 X 65 X 25MM ESQ - CADEIRA HARRY (IKEA)",
    "equipamentos": [
      3
    ],
    "tempo": 31,
    "setup": 2100,
    "codigo_barra": 47775
  },
  {
    "id_erp": 47974,
    "nome": "PE MAD DIANTEIRO P0498 425 X 45 X 45MM - CADEIRA STELA/STELA LX",
    "equipamentos": [
      3
    ],
    "tempo": 5,
    "setup": 2100,
    "codigo_barra": 47974
  },
  {
    "id_erp": 47975,
    "nome": "PE MAD DIANTEIRO P0499 425 X 45 X 45MM ESQ - CADEIRA STELA",
    "equipamentos": [
      3
    ],
    "tempo": 6,
    "setup": 600,
    "codigo_barra": 47975
  },
  {
    "id_erp": 47976,
    "nome": "PE MAD TRASEIRO P0500 490 X 45 X 35MM DIR - CADEIRA STELA",
    "equipamentos": [
      3
    ],
    "tempo": 5,
    "setup": 2100,
    "codigo_barra": 47976
  },
  {
    "id_erp": 47977,
    "nome": "PE MAD TRASEIRO P0501 490 X 45 X 35MM ESQ - CADEIRA STELA",
    "equipamentos": [
      3
    ],
    "tempo": 6,
    "setup": 600,
    "codigo_barra": 47977
  },
  {
    "id_erp": 47978,
    "nome": "TRAVESSA MAD LATERAL T0408 430 X 45 X 30MM DIR - CADEIRA STELA/STELA LX",
    "equipamentos": [
      2
    ],
    "tempo": 37,
    "setup": 0,
    "codigo_barra": 47978
  },
  {
    "id_erp": 47979,
    "nome": "TRAVESSA MAD LATERAL T0409 430 X 45 X 30MM ESQ - CADEIRA STELA/STELA LX",
    "equipamentos": [
      2
    ],
    "tempo": 37,
    "setup": 4800,
    "codigo_barra": 47979
  },
  {
    "id_erp": 47980,
    "nome": "TRAVESSA MAD DIANTEIRA T0410 440 X 45 X 30MM - CADEIRA STELA/STELA LX",
    "equipamentos": [
      2
    ],
    "tempo": 22,
    "setup": 3900,
    "codigo_barra": 47980
  },
  {
    "id_erp": 47981,
    "nome": "TRAVESSA MAD TRASEIRA T0411 335 X 45 X 30MM - CADEIRA STELA/STELA LX",
    "equipamentos": [
      2
    ],
    "tempo": 23,
    "setup": 0,
    "codigo_barra": 47981
  },
  {
    "id_erp": 48024,
    "nome": "TRAVESSA MAD LATERAL T0417 1490 X 40 X 30MM MAIOR SUP - MESA CENTRO MORANA",
    "equipamentos": [
      3
    ],
    "tempo": 51,
    "setup": 2100,
    "codigo_barra": 48024
  },
  {
    "id_erp": 48026,
    "nome": "TRAVESSA MAD LATERAL T0418 590 X 40 X 30MM MENOR SUP - MESA CENTRO MORANA",
    "equipamentos": [
      3
    ],
    "tempo": 51,
    "setup": 600,
    "codigo_barra": 48026
  },
  {
    "id_erp": 48027,
    "nome": "TRAVESSA MAD T0419 255 X 75 X 30MM LAT - MESA CENTRO MORANA",
    "equipamentos": [
      2
    ],
    "tempo": 45,
    "setup": 4500,
    "codigo_barra": 48027
  },
  {
    "id_erp": 48028,
    "nome": "TRAVESSA MAD T0420 250 X 70 X 30MM - MESA CENTRO MORANA",
    "equipamentos": [
      2
    ],
    "tempo": 45,
    "setup": 4500,
    "codigo_barra": 48028
  },
  {
    "id_erp": 48048,
    "nome": "FRONTAL MAD  F0018 430 X 50 X 30MM - CADEIRA LAIS/NAOMI/VIVI",
    "equipamentos": [
      2
    ],
    "tempo": 13,
    "setup": 2100,
    "codigo_barra": 48048
  },
  {
    "id_erp": 48048,
    "nome": "FRONTAL MAD  F0018 430 X 50 X 30MM - CADEIRA LAIS/NAOMI/VIVI",
    "equipamentos": [
      1
    ],
    "tempo": 13,
    "setup": 2100,
    "codigo_barra": 48048
  },
  {
    "id_erp": 48100,
    "nome": "TRAVESSA MAD LATERAL T0428 1490 X 40 X 30MM MAIOR INF - MESA CENTRO MORANA",
    "equipamentos": [
      3
    ],
    "tempo": 71,
    "setup": 2100,
    "codigo_barra": 48100
  },
  {
    "id_erp": 48101,
    "nome": "TRAVESSA MAD LATERAL T0429 590 X 40 X 30MM MENOR INF - MESA CENTRO MORANA",
    "equipamentos": [
      3
    ],
    "tempo": 71,
    "setup": 600,
    "codigo_barra": 48101
  },
  {
    "id_erp": 48168,
    "nome": "TRAV. PINTADA T0064 840 X 100 X 40MM (TRAS.BASE DIR)",
    "equipamentos": [
      2
    ],
    "tempo": 74,
    "setup": 2100,
    "codigo_barra": 48168
  },
  {
    "id_erp": 48169,
    "nome": "TRAV. PINTADA T0061 1455 X 85 X 40MM (LAT ESQ. DA BASE)",
    "equipamentos": [
      2
    ],
    "tempo": 91,
    "setup": 2100,
    "codigo_barra": 48169
  },
  {
    "id_erp": 48170,
    "nome": "TRAV. PINTADA T0010 1535 X 85 X 40MM (LAT DIR DA BASE)",
    "equipamentos": [
      2
    ],
    "tempo": 91,
    "setup": 2100,
    "codigo_barra": 48170
  },
  {
    "id_erp": 48173,
    "nome": "TRAV. PINTADA T0070 1495 X 97 X 40MM (COMPLEMENTO BASE ITAUNA 1590 ESQ)",
    "equipamentos": [
      2
    ],
    "tempo": 85,
    "setup": 1200,
    "codigo_barra": 48173
  },
  {
    "id_erp": 48174,
    "nome": "TRAV. PINTADA T0071 605 X 95 X 40MM (COMPLEMENTO BASE ITAUNA 1590 ESQ)",
    "equipamentos": [
      2
    ],
    "tempo": 65,
    "setup": 2100,
    "codigo_barra": 48174
  },
  {
    "id_erp": 48175,
    "nome": "TRAV. PINTADA T0072 715 X 85 X 40MM (COMPLEMENTO BASE ITAUNA 1590 ESQ)",
    "equipamentos": [
      2
    ],
    "tempo": 65,
    "setup": 2100,
    "codigo_barra": 48175
  },
  {
    "id_erp": 48207,
    "nome": "PE MAD DIANTEIRO P0510 430 X 45 X 32MM ESQ - CADEIRA JULIA",
    "equipamentos": [
      3
    ],
    "tempo": 18,
    "setup": 1800,
    "codigo_barra": 48207
  },
  {
    "id_erp": 48208,
    "nome": "PE MAD DIANTEIRO P0511 430 X 45 X 32MM DIR - CADEIRA JULIA",
    "equipamentos": [
      3
    ],
    "tempo": 18,
    "setup": 1800,
    "codigo_barra": 48208
  },
  {
    "id_erp": 48209,
    "nome": "PE MAD TRASEIRO P0512 870 X 175 X 32MM ESQ - CADEIRA JULIA (1ª ETAPA)",
    "equipamentos": [
      2
    ],
    "tempo": 30,
    "setup": 2100,
    "codigo_barra": 48209
  },
  {
    "id_erp": 48210,
    "nome": "PE MAD TRASEIRO P0513 870 X 175 X 32MM DIR - CADEIRA JULIA  (1ª ETAPA)",
    "equipamentos": [
      2
    ],
    "tempo": 30,
    "setup": 2100,
    "codigo_barra": 48210
  },
  {
    "id_erp": 48211,
    "nome": "TRAVESSA MAD T0423 382 X 40 X 26MM SUP ENC - CADEIRA JULIA (PAINEL 1 395X1030X50 - 15PCS / PAINEL 2 395X1030X62 - 23PCS)",
    "equipamentos": [
      2
    ],
    "tempo": 43,
    "setup": 7200,
    "codigo_barra": 48211
  },
  {
    "id_erp": 48212,
    "nome": "TRAVESSA MAD TRASEIRA T0424 430 X 45 X 26MM - CADEIRA JULIA (PAINEL 1 435X1030X50 - 15PCS / PAINEL 2 435X1030X62 - 23PCS)",
    "equipamentos": [
      2
    ],
    "tempo": 43,
    "setup": 0,
    "codigo_barra": 48212
  },
  {
    "id_erp": 48213,
    "nome": "TRAVESSA MAD DIANTEIRA T0425 440 X 45 X 22MM - CADEIRA JULIA",
    "equipamentos": [
      2
    ],
    "tempo": 21,
    "setup": 2100,
    "codigo_barra": 48213
  },
  {
    "id_erp": 48346,
    "nome": "TRAVESSA MAD T0745 1520 X 50 X 40MM MAIOR - MESA CENTRO CALIANDRA",
    "equipamentos": [
      3
    ],
    "tempo": 8,
    "setup": 0,
    "codigo_barra": 48346
  },
  {
    "id_erp": 48347,
    "nome": "TRAVESSA MAD T0746 620 X 50 X 40MM MENOR - MESA CENTRO CALIANDRA",
    "equipamentos": [
      3
    ],
    "tempo": 9,
    "setup": 2100,
    "codigo_barra": 48347
  },
  {
    "id_erp": 48349,
    "nome": "PE MAD P0654 320 X 60 X 32MM - MESA CENTRO CALIANDRA",
    "equipamentos": [
      3
    ],
    "tempo": 11,
    "setup": 4200,
    "codigo_barra": 48349
  },
  {
    "id_erp": 48409,
    "nome": "PE MAD P0014 360 X 45 X 45MM (SOFA ALTAMIRA)",
    "equipamentos": [
      3
    ],
    "tempo": 40,
    "setup": 2100,
    "codigo_barra": 48409
  },
  {
    "id_erp": 48446,
    "nome": "PE MAD DIANTEIRO P0514 642 X 123 X 32MM DIR - POLTRONA MALBEC",
    "equipamentos": [
      2
    ],
    "tempo": 10,
    "setup": 2100,
    "codigo_barra": 48446
  },
  {
    "id_erp": 48446,
    "nome": "PE MAD DIANTEIRO P0514 642 X 123 X 32MM DIR - POLTRONA MALBEC",
    "equipamentos": [
      1
    ],
    "tempo": 10,
    "setup": 2100,
    "codigo_barra": 48446
  },
  {
    "id_erp": 48447,
    "nome": "PE MAD DIANTEIRO P0515 642 X 123 X 32MM ESQ - POLTRONA MALBEC",
    "equipamentos": [
      2
    ],
    "tempo": 10,
    "setup": 2100,
    "codigo_barra": 48447
  },
  {
    "id_erp": 48447,
    "nome": "PE MAD DIANTEIRO P0515 642 X 123 X 32MM ESQ - POLTRONA MALBEC",
    "equipamentos": [
      1
    ],
    "tempo": 10,
    "setup": 2100,
    "codigo_barra": 48447
  },
  {
    "id_erp": 48448,
    "nome": "PE MAD TRASEIRO P0516 630 X 102 X 32MM DIR - POLTRONA MALBEC",
    "equipamentos": [
      2
    ],
    "tempo": 10,
    "setup": 2100,
    "codigo_barra": 48448
  },
  {
    "id_erp": 48448,
    "nome": "PE MAD TRASEIRO P0516 630 X 102 X 32MM DIR - POLTRONA MALBEC",
    "equipamentos": [
      1
    ],
    "tempo": 10,
    "setup": 2100,
    "codigo_barra": 48448
  },
  {
    "id_erp": 48449,
    "nome": "PE MAD TRASEIRO P0517 630 X 102 X 32MM ESQ - POLTRONA MALBEC",
    "equipamentos": [
      2
    ],
    "tempo": 10,
    "setup": 2100,
    "codigo_barra": 48449
  },
  {
    "id_erp": 48449,
    "nome": "PE MAD TRASEIRO P0517 630 X 102 X 32MM ESQ - POLTRONA MALBEC",
    "equipamentos": [
      1
    ],
    "tempo": 10,
    "setup": 2100,
    "codigo_barra": 48449
  },
  {
    "id_erp": 48450,
    "nome": "TRAVESSA MAD T0430 495 X 85 X 32MM TOPO DIR - POLTRONA MALBEC",
    "equipamentos": [
      2
    ],
    "tempo": 10,
    "setup": 2100,
    "codigo_barra": 48450
  },
  {
    "id_erp": 48450,
    "nome": "TRAVESSA MAD T0430 495 X 85 X 32MM TOPO DIR - POLTRONA MALBEC",
    "equipamentos": [
      1
    ],
    "tempo": 10,
    "setup": 2100,
    "codigo_barra": 48450
  },
  {
    "id_erp": 48451,
    "nome": "TRAVESSA MAD T0431 495 X 85 X 32MM TOPO ESQ - POLTRONA MALBEC",
    "equipamentos": [
      2
    ],
    "tempo": 10,
    "setup": 2100,
    "codigo_barra": 48451
  },
  {
    "id_erp": 48451,
    "nome": "TRAVESSA MAD T0431 495 X 85 X 32MM TOPO ESQ - POLTRONA MALBEC",
    "equipamentos": [
      1
    ],
    "tempo": 10,
    "setup": 2100,
    "codigo_barra": 48451
  },
  {
    "id_erp": 48452,
    "nome": "TRAVESSA MAD DIANTEIRA T0432 640 X 65 X 22MM - POLTRONA MALBEC",
    "equipamentos": [
      2
    ],
    "tempo": 50,
    "setup": 3600,
    "codigo_barra": 48452
  },
  {
    "id_erp": 48453,
    "nome": "TRAVESSA MAD TRASEIRA T0434 640 X 65 X 22MM - POLTRONA MALBEC",
    "equipamentos": [
      2
    ],
    "tempo": 50,
    "setup": 3600,
    "codigo_barra": 48453
  },
  {
    "id_erp": 48483,
    "nome": "PE MAD TRASEIRO P0518 935 X 42 X 32MM DIR - CADEIRA BETTY/LAINE",
    "equipamentos": [
      3
    ],
    "tempo": 16,
    "setup": 2100,
    "codigo_barra": 48483
  },
  {
    "id_erp": 48484,
    "nome": "PE MAD TRASEIRO P0519 935 X 42 X 32MM ESQ - CADEIRA BETTY/LAINE",
    "equipamentos": [
      3
    ],
    "tempo": 16,
    "setup": 2100,
    "codigo_barra": 48484
  },
  {
    "id_erp": 48486,
    "nome": "PE MAD P0656 555 X 45 X 40MM - MESA ITACARE RETANGULAR/REDONDA",
    "equipamentos": [
      3
    ],
    "tempo": 35,
    "setup": 2100,
    "codigo_barra": 48486
  },
  {
    "id_erp": 48487,
    "nome": "PE MAD P0655 555 X 45 X 40MM - MESA ITACARE RETANGULAR/REDONDA",
    "equipamentos": [
      3
    ],
    "tempo": 35,
    "setup": 2100,
    "codigo_barra": 48487
  },
  {
    "id_erp": 48492,
    "nome": "TRAVESSA MAD T0748 612 X 40 X 32MM LAT - MESA ITACARE RETANGULAR",
    "equipamentos": [
      2
    ],
    "tempo": 32,
    "setup": 2100,
    "codigo_barra": 48492
  },
  {
    "id_erp": 48493,
    "nome": "TRAVESSA MAD T0749 380 X 40 X 32MM MAIOR - MESA ITACARE RETANGULAR",
    "equipamentos": [
      2
    ],
    "tempo": 16,
    "setup": 2100,
    "codigo_barra": 48493
  },
  {
    "id_erp": 48494,
    "nome": "TRAVESSA MAD T0750 300 X 40 X 32MM MENOR - MESA ITACARE RETANGULAR",
    "equipamentos": [
      2
    ],
    "tempo": 17,
    "setup": 2100,
    "codigo_barra": 48494
  },
  {
    "id_erp": 48612,
    "nome": "TRAVESSA MAD T0751 425 X 40 X 32MM BORDA - MESA ITACARE REDONDA",
    "equipamentos": [
      2
    ],
    "tempo": 33,
    "setup": 4800,
    "codigo_barra": 48612
  },
  {
    "id_erp": 48621,
    "nome": "PE MAD P0657 780 X 82 X 45MM - MESA ITACARE QUADRADA",
    "equipamentos": [
      3
    ],
    "tempo": 41,
    "setup": 2100,
    "codigo_barra": 48621
  },
  {
    "id_erp": 48622,
    "nome": "PE MAD P0658 780 X 82 X 45MM - MESA ITACARE QUADRADA",
    "equipamentos": [
      3
    ],
    "tempo": 41,
    "setup": 2100,
    "codigo_barra": 48622
  },
  {
    "id_erp": 48631,
    "nome": "TRAVESSA MAD T0752 772 X 43 X 32MM BORDA - MESA ITACARE QUADRADA",
    "equipamentos": [
      2
    ],
    "tempo": 33,
    "setup": 2100,
    "codigo_barra": 48631
  },
  {
    "id_erp": 48860,
    "nome": "PE MAD P0671 520 X 85 X 45MM - APARADOR CONRADO",
    "equipamentos": [
      2
    ],
    "tempo": 35,
    "setup": 2100,
    "codigo_barra": 48860
  },
  {
    "id_erp": 48862,
    "nome": "TRAVESSA MAD T0754 1100 X 120 X 45MM - APARADOR CONRADO",
    "equipamentos": [
      2
    ],
    "tempo": 75,
    "setup": 2100,
    "codigo_barra": 48862
  },
  {
    "id_erp": 49548,
    "nome": "PE MAD P0015 110 X 45 X 40MM (SOFA KAUE)",
    "equipamentos": [
      2
    ],
    "tempo": 46,
    "setup": 4800,
    "codigo_barra": 49548
  },
  {
    "id_erp": 49552,
    "nome": "TRAVESSA MAD  T0866 495 X 50 X 45MM - ESTOFADO KAUE PE DIR",
    "equipamentos": [
      2
    ],
    "tempo": 38,
    "setup": 2100,
    "codigo_barra": 49552
  },
  {
    "id_erp": 49562,
    "nome": "TRAVESSA MAD  T0865 395 X 50 X 45MM - ESTOFADO KAUE CANTO PE ESQ",
    "equipamentos": [
      2
    ],
    "tempo": 71,
    "setup": 5100,
    "codigo_barra": 49562
  },
  {
    "id_erp": 50519,
    "nome": "PECA BRUTA MAD P0451 600 X 70 X 32MM - CADEIRA JULIA - PECA P/ MONTAGEM INFERIOR",
    "equipamentos": [
      2
    ],
    "tempo": 15,
    "setup": 2100,
    "codigo_barra": 50519
  },
  {
    "id_erp": 50520,
    "nome": "PECA BRUTA MAD P0452 400 X 70 X 32MM - CADEIRA JULIA - PECA P/ MONTAGEM SUPERIOR",
    "equipamentos": [
      2
    ],
    "tempo": 15,
    "setup": 2100,
    "codigo_barra": 50520
  },
  {
    "id_erp": 50535,
    "nome": "PE MAD TRASEIRO P0524 890 X 70 X 32MM DIREITO - CADEIRA ELIZE/ELIZE C/ BRACO",
    "equipamentos": [
      3
    ],
    "tempo": 15,
    "setup": 0,
    "codigo_barra": 50535
  },
  {
    "id_erp": 50536,
    "nome": "PE MAD TRASEIRO P0525 890 X 70 X 32MM ESQUERDO - CADEIRA ELIZE/ELIZE C/ BRACO",
    "equipamentos": [
      3
    ],
    "tempo": 15,
    "setup": 0,
    "codigo_barra": 50536
  },
  {
    "id_erp": 50537,
    "nome": "FRONTAL MAD  F0019 430 X 45 X 28MM - CADEIRA ELIZE/ELIZE C/ BRACO",
    "equipamentos": [
      2
    ],
    "tempo": 40,
    "setup": 2400,
    "codigo_barra": 50537
  },
  {
    "id_erp": 50537,
    "nome": "FRONTAL MAD  F0019 430 X 45 X 28MM - CADEIRA ELIZE/ELIZE C/ BRACO",
    "equipamentos": [
      3
    ],
    "tempo": 40,
    "setup": 2400,
    "codigo_barra": 50537
  },
  {
    "id_erp": 50538,
    "nome": "TRAVESSA MAD TRASEIRA T0464 430 X 45 X 28MM - CADEIRA ELIZE/ELIZE C/ BRACO (COM FURO)",
    "equipamentos": [
      2
    ],
    "tempo": 32,
    "setup": 3480,
    "codigo_barra": 50538
  },
  {
    "id_erp": 50539,
    "nome": "TRAVESSA MAD LATERAL T0465 425 X 55 X 22MM ESQUERD - CADEIRA ELIZE",
    "equipamentos": [
      2
    ],
    "tempo": 34,
    "setup": 3300,
    "codigo_barra": 50539
  },
  {
    "id_erp": 50540,
    "nome": "TRAVESSA MAD LATERAL T0466 425 X 55 X 22MM DIREITA - CADEIRA ELIZE",
    "equipamentos": [
      2
    ],
    "tempo": 33,
    "setup": 0,
    "codigo_barra": 50540
  },
  {
    "id_erp": 50541,
    "nome": "TRAVESSA MAD DIANTEIRA T0467 440 X 55 X 22MM - CADEIRA ELIZE/ELIZE C/BRACO/ELIZE RATAN/ELIZE RATAN BRACO",
    "equipamentos": [
      2
    ],
    "tempo": 23,
    "setup": 2100,
    "codigo_barra": 50541
  },
  {
    "id_erp": 50566,
    "nome": "TRAVESSA MAD LATERAL T0472 510 X 75 X 22MM LAT ENC - POLTRONA ELDORA 600-720/TOLEDO 600-720/NAMORADEIRA TOLEDO 1300",
    "equipamentos": [
      2
    ],
    "tempo": 26,
    "setup": 3780,
    "codigo_barra": 50566
  },
  {
    "id_erp": 50569,
    "nome": "TRAVESSA MAD LATERAL T0475 460 X 65 X 22MM ASS - POLTRONA ELDORA 600-720/TOLEDO 600-720/NAMORADEIRA TOLEDO 1300",
    "equipamentos": [
      2
    ],
    "tempo": 26,
    "setup": 0,
    "codigo_barra": 50569
  },
  {
    "id_erp": 50578,
    "nome": "PE MAD DIANTEIRO P0526 679 X 52 X 32MM - POLTRONA ELDORA 600-720/TOLEDO 600-720/NAMORADEIRA TOLEDO 1300",
    "equipamentos": [
      3
    ],
    "tempo": 12,
    "setup": 2100,
    "codigo_barra": 50578
  },
  {
    "id_erp": 50579,
    "nome": "PE MAD TRASEIRO P0527 679 X 52 X 32MM ESQ - POLTRONA ELDORA 600-720/TOLEDO 600-720/NAMORADEIRA TOLEDO 1300",
    "equipamentos": [
      3
    ],
    "tempo": 12,
    "setup": 2100,
    "codigo_barra": 50579
  },
  {
    "id_erp": 50580,
    "nome": "TRAVESSA MAD T0479 510 X 60 X 18MM INF BRACO - POLTRONA ELDORA 600-720/TOLEDO 600-720/NAMORADEIRA TOLEDO 1300",
    "equipamentos": [
      2
    ],
    "tempo": 14,
    "setup": 2100,
    "codigo_barra": 50580
  },
  {
    "id_erp": 50705,
    "nome": "PE MAD TRASEIRO P0530 190 X 45 X 45MM DIR - POLTRONA BARBARA",
    "equipamentos": [
      3
    ],
    "tempo": 8,
    "setup": 2100,
    "codigo_barra": 50705
  },
  {
    "id_erp": 50706,
    "nome": "PE MAD TRASEIRO P0531 190 X 45 X 45MM ESQ - POLTRONA BARBARA",
    "equipamentos": [
      3
    ],
    "tempo": 7,
    "setup": 2100,
    "codigo_barra": 50706
  },
  {
    "id_erp": 50707,
    "nome": "TRAVESSA MAD DIANTEIRA T0480 750 X 45 X 25MM - POLTRONA BARBARA",
    "equipamentos": [
      2
    ],
    "tempo": 37,
    "setup": 2100,
    "codigo_barra": 50707
  },
  {
    "id_erp": 50708,
    "nome": "TRAVESSA MAD TRASEIRA T0481 630 X 77 X 30MM - POLTRONA BARBARA (620 X 77 X 25MM)",
    "equipamentos": [
      2
    ],
    "tempo": 30,
    "setup": 2100,
    "codigo_barra": 50708
  },
  {
    "id_erp": 50712,
    "nome": "TRAVESSA MAD LATERAL T0484 655 X 40 X 30MM DIR BRA - POLTRONA BARBARA",
    "equipamentos": [
      2
    ],
    "tempo": 20,
    "setup": 2100,
    "codigo_barra": 50712
  },
  {
    "id_erp": 50713,
    "nome": "TRAVESSA MAD LATERAL T0485 655 X 40 X 30MM ESQ BRA - POLTRONA BARBARA",
    "equipamentos": [
      2
    ],
    "tempo": 20,
    "setup": 2100,
    "codigo_barra": 50713
  },
  {
    "id_erp": 50860,
    "nome": "TRAVESSA MAD T0488 460 X 40 X 18MM SUP BRACO - POLTRONA ELDORA 600-720/TOLEDO 600-720/NAMORADEIRA TOLEDO 1300",
    "equipamentos": [
      2
    ],
    "tempo": 14,
    "setup": 0,
    "codigo_barra": 50860
  },
  {
    "id_erp": 50862,
    "nome": "PE MAD TRASEIRO P0532 679 X 52 X 32MM DIR - POLTRONA ELDORA 600-720/TOLEDO 600-720/NAMORADEIRA TOLEDO 1300",
    "equipamentos": [
      3
    ],
    "tempo": 12,
    "setup": 2100,
    "codigo_barra": 50862
  },
  {
    "id_erp": 50961,
    "nome": "PE MAD DIANTEIRO P0533 438 X 56 X 32MM DIR - CADEIRA PAOLA",
    "equipamentos": [
      3
    ],
    "tempo": 22,
    "setup": 5400,
    "codigo_barra": 50961
  },
  {
    "id_erp": 50962,
    "nome": "PE MAD DIANTEIRO P0534 438 X 56 X 32MM ESQ - CADEIRA PAOLA",
    "equipamentos": [
      3
    ],
    "tempo": 22,
    "setup": 0,
    "codigo_barra": 50962
  },
  {
    "id_erp": 50963,
    "nome": "PE MAD TRASEIRO P0535 580 X 68 X 32MM DIR - CADEIRA PAOLA",
    "equipamentos": [
      3
    ],
    "tempo": 22,
    "setup": 5400,
    "codigo_barra": 50963
  },
  {
    "id_erp": 50964,
    "nome": "PE MAD TRASEIRO P0536 580 X 68 X 32MM ESQ - CADEIRA PAOLA",
    "equipamentos": [
      3
    ],
    "tempo": 22,
    "setup": 0,
    "codigo_barra": 50964
  },
  {
    "id_erp": 50965,
    "nome": "TRAVESSA MAD LATERAL T0493 425 X 96 X 32MM DIR - CADEIRA PAOLA",
    "equipamentos": [
      2
    ],
    "tempo": 73,
    "setup": 3600,
    "codigo_barra": 50965
  },
  {
    "id_erp": 50965,
    "nome": "TRAVESSA MAD LATERAL T0493 425 X 96 X 32MM DIR - CADEIRA PAOLA",
    "equipamentos": [
      1
    ],
    "tempo": 73,
    "setup": 3600,
    "codigo_barra": 50965
  },
  {
    "id_erp": 50966,
    "nome": "TRAVESSA MAD LATERAL T0494 425 X 96 X 32MM ESQ - CADEIRA PAOLA",
    "equipamentos": [
      2
    ],
    "tempo": 73,
    "setup": 0,
    "codigo_barra": 50966
  },
  {
    "id_erp": 50966,
    "nome": "TRAVESSA MAD LATERAL T0494 425 X 96 X 32MM ESQ - CADEIRA PAOLA",
    "equipamentos": [
      1
    ],
    "tempo": 73,
    "setup": 0,
    "codigo_barra": 50966
  },
  {
    "id_erp": 50967,
    "nome": "TRAVESSA MAD DIANTEIRA T0495 485 X 46 X 22MM - CADEIRA PAOLA",
    "equipamentos": [
      2
    ],
    "tempo": 29,
    "setup": 2400,
    "codigo_barra": 50967
  },
  {
    "id_erp": 50967,
    "nome": "TRAVESSA MAD DIANTEIRA T0495 485 X 46 X 22MM - CADEIRA PAOLA",
    "equipamentos": [
      1
    ],
    "tempo": 29,
    "setup": 2400,
    "codigo_barra": 50967
  },
  {
    "id_erp": 50968,
    "nome": "TRAVESSA MAD TRASEIRA T0496 455 X 51 X 22MM - CADEIRA PAOLA",
    "equipamentos": [
      2
    ],
    "tempo": 29,
    "setup": 2400,
    "codigo_barra": 50968
  },
  {
    "id_erp": 50968,
    "nome": "TRAVESSA MAD TRASEIRA T0496 455 X 51 X 22MM - CADEIRA PAOLA",
    "equipamentos": [
      1
    ],
    "tempo": 29,
    "setup": 2400,
    "codigo_barra": 50968
  },
  {
    "id_erp": 51000,
    "nome": "MESA CENTRO CALIANDRA (NELSINHO)",
    "equipamentos": [
      3
    ],
    "tempo": 2.431,
    "setup": 6600,
    "codigo_barra": 51000
  },
  {
    "id_erp": 51104,
    "nome": "TRAVESSA MAD  T0053 495 X 50 X 45MM - ESTOFADO KAUE PE ESQ",
    "equipamentos": [
      2
    ],
    "tempo": 69,
    "setup": 5100,
    "codigo_barra": 51104
  },
  {
    "id_erp": 51673,
    "nome": "PE MAD P0018 200 X 70 X 32 MM (ESFADO SUMARE)",
    "equipamentos": [
      2
    ],
    "tempo": 25,
    "setup": 2100,
    "codigo_barra": 51673
  },
  {
    "id_erp": 51674,
    "nome": "TRAV. MAD  T1050 380 X 50 X 32MM (ESFADO SUMARE)",
    "equipamentos": [
      2
    ],
    "tempo": 20,
    "setup": 2100,
    "codigo_barra": 51674
  },
  {
    "id_erp": 51783,
    "nome": "TRAVESSA MAD BRACO T0660 265 X 55 X 32MM ESQ - CADEIRA ELIZE C/ BRACO",
    "equipamentos": [
      2
    ],
    "tempo": 19,
    "setup": 0,
    "codigo_barra": 51783
  },
  {
    "id_erp": 51784,
    "nome": "TRAVESSA MAD BRACO T0661 405 X 60 X 32MM ESQ - CADEIRA ELIZE C/ BRACO",
    "equipamentos": [
      2
    ],
    "tempo": 19,
    "setup": 2100,
    "codigo_barra": 51784
  },
  {
    "id_erp": 51785,
    "nome": "TRAVESSA MAD BRACO T0662 265 X 55 X 32MM DIR - CADEIRA ELIZE C/ BRACO",
    "equipamentos": [
      2
    ],
    "tempo": 19,
    "setup": 2100,
    "codigo_barra": 51785
  },
  {
    "id_erp": 51786,
    "nome": "TRAVESSA MAD BRACO T0663 405 X 60 X 32MM DIR - CADEIRA ELIZE C/ BRACO",
    "equipamentos": [
      2
    ],
    "tempo": 18,
    "setup": 0,
    "codigo_barra": 51786
  },
  {
    "id_erp": 51789,
    "nome": "PE MAD TRASEIRO P0537 890 X 70 X 32MM DIREITO - CADEIRA ELIZE/ELIZE C/ BRACO",
    "equipamentos": [
      3
    ],
    "tempo": 15,
    "setup": 0,
    "codigo_barra": 51789
  },
  {
    "id_erp": 51790,
    "nome": "PE MAD TRASEIRO P0538 890 X 70 X 32MM ESQUERDO - CADEIRA ELIZE/ELIZE C/ BRACO",
    "equipamentos": [
      3
    ],
    "tempo": 15,
    "setup": 0,
    "codigo_barra": 51790
  },
  {
    "id_erp": 51816,
    "nome": "TRAVESSA MAD T0664 1365 X 50 X 32MM - BANCO BARBARA",
    "equipamentos": [
      2
    ],
    "tempo": 35,
    "setup": 2100,
    "codigo_barra": 51816
  },
  {
    "id_erp": 51817,
    "nome": "TRAVESSA MAD LATERAL T0665 525 X 50 X 30MM - BANCO BARBARA",
    "equipamentos": [
      2
    ],
    "tempo": 35,
    "setup": 2100,
    "codigo_barra": 51817
  },
  {
    "id_erp": 51838,
    "nome": "TRAVESSA MAD LATERAL T0667 700 X 40 X 30MM - PUFF BARBARA",
    "equipamentos": [
      2
    ],
    "tempo": 45,
    "setup": 4200,
    "codigo_barra": 51838
  },
  {
    "id_erp": 51962,
    "nome": "PE MAD DIANTEIRO P0543 700 X 115 X 32MM ESQ - BANQUETA PAOLA 1010MM",
    "equipamentos": [
      3
    ],
    "tempo": 27,
    "setup": 2100,
    "codigo_barra": 51962
  },
  {
    "id_erp": 51963,
    "nome": "PE MAD DIANTEIRO P0544 700 X 115 X 32MM DIR - BANQUETA PAOLA 1010MM",
    "equipamentos": [
      3
    ],
    "tempo": 27,
    "setup": 2100,
    "codigo_barra": 51963
  },
  {
    "id_erp": 51965,
    "nome": "PE MAD TRASEIRO P0545 816 X 145 X 32MM ESQ - BANQUETA PAOLA 1010MM",
    "equipamentos": [
      3
    ],
    "tempo": 30,
    "setup": 3300,
    "codigo_barra": 51965
  },
  {
    "id_erp": 51966,
    "nome": "PE MAD TRASEIRO P0546 816 X 145 X 32MM DIR - BANQUETA PAOLA 1010MM",
    "equipamentos": [
      3
    ],
    "tempo": 30,
    "setup": 3300,
    "codigo_barra": 51966
  },
  {
    "id_erp": 51969,
    "nome": "TRAVESSA MAD DIANTEIRA T0669 485 X 46 X 22MM SUP - BANQUETA PAOLA",
    "equipamentos": [
      2
    ],
    "tempo": 29,
    "setup": 0,
    "codigo_barra": 51969
  },
  {
    "id_erp": 51971,
    "nome": "TRAVESSA MAD TRASEIRA T0670 455 X 51 X 22MM SUP - BANQUETA PAOLA",
    "equipamentos": [
      2
    ],
    "tempo": 29,
    "setup": 4500,
    "codigo_barra": 51971
  },
  {
    "id_erp": 51973,
    "nome": "TRAVESSA MAD LATERAL T0671 340 X 96 X 32MM SUP - BANQUETA PAOLA 910/1010MM",
    "equipamentos": [
      2
    ],
    "tempo": 63,
    "setup": 4500,
    "codigo_barra": 51973
  },
  {
    "id_erp": 51975,
    "nome": "TRAVESSA MAD LATERAL T0672 360 X 96 X 32MM DIR SUP - BANQUETA PAOLA",
    "equipamentos": [
      2
    ],
    "tempo": 63,
    "setup": 2100,
    "codigo_barra": 51975
  },
  {
    "id_erp": 52043,
    "nome": "PE MAD TRASEIRO P0547 890 X 70 X 32MM DIREITO - CADEIRA ELIZE RATAN/ELIZE RATAN C/ BRACO (FAZ JUNTO 36002,36003)",
    "equipamentos": [
      3
    ],
    "tempo": 15,
    "setup": 0,
    "codigo_barra": 52043
  },
  {
    "id_erp": 52044,
    "nome": "PE MAD TRASEIRO P0548 890 X 70 X 32MM ESQUERDO - CADEIRA ELIZE RATAN/ELIZE RATAN C/ BRACO (FAZ JUNTO 36002,36003)",
    "equipamentos": [
      3
    ],
    "tempo": 15,
    "setup": 0,
    "codigo_barra": 52044
  },
  {
    "id_erp": 52045,
    "nome": "TRAVESSA MAD T0677 430 X 45 X 28MM SUP ENC - CADEIRA ELIZE RATAN/ELIZE RATAN C/ BRACO",
    "equipamentos": [
      2
    ],
    "tempo": 48,
    "setup": 3420,
    "codigo_barra": 52045
  },
  {
    "id_erp": 52046,
    "nome": "TRAVESSA MAD T0678 390 X 45 X 28MM INF ENC - CADEIRA ELIZE RATAN/ELIZE RATAN C/ BRACO",
    "equipamentos": [
      2
    ],
    "tempo": 40,
    "setup": 3566,
    "codigo_barra": 52046
  },
  {
    "id_erp": 52049,
    "nome": "PE MAD TRASEIRO P0549 890 X 70 X 32MM DIR - CADEIRA ELIZE RATAN C/ BRACO",
    "equipamentos": [
      3
    ],
    "tempo": 15,
    "setup": 2100,
    "codigo_barra": 52049
  },
  {
    "id_erp": 52050,
    "nome": "PE MAD TRASEIRO P0550 890 X 70 X 32MM ESQ - CADEIRA ELIZE RATAN C/ BRACO",
    "equipamentos": [
      3
    ],
    "tempo": 15,
    "setup": 2100,
    "codigo_barra": 52050
  },
  {
    "id_erp": 52367,
    "nome": "PE MAD TRASEIRO P0555 765 X 80 X 32MM DIREITO - CADEIRA THAIS",
    "equipamentos": [
      3
    ],
    "tempo": 20,
    "setup": 2100,
    "codigo_barra": 52367
  },
  {
    "id_erp": 52368,
    "nome": "PE MAD TRASEIRO P0556 765 X 80 X 32MM ESQUERDO - CADEIRA THAIS",
    "equipamentos": [
      3
    ],
    "tempo": 20,
    "setup": 2100,
    "codigo_barra": 52368
  },
  {
    "id_erp": 52369,
    "nome": "PE MAD DIANTEIRO P0557 415 X 45 X 45MM DIREITO - CADEIRA THAIS",
    "equipamentos": [
      3
    ],
    "tempo": 20,
    "setup": 2100,
    "codigo_barra": 52369
  },
  {
    "id_erp": 52370,
    "nome": "PE MAD DIANTEIRO P0558 415 X 45 X 45MM ESQUERDO - CADEIRA THAIS",
    "equipamentos": [
      3
    ],
    "tempo": 20,
    "setup": 2100,
    "codigo_barra": 52370
  },
  {
    "id_erp": 52371,
    "nome": "TRAVESSA MAD TRASEIRA T0681 485 X 95 X 32MM - CADEIRA THAIS",
    "equipamentos": [
      2
    ],
    "tempo": 26,
    "setup": 2100,
    "codigo_barra": 52371
  },
  {
    "id_erp": 52371,
    "nome": "TRAVESSA MAD TRASEIRA T0681 485 X 95 X 32MM - CADEIRA THAIS",
    "equipamentos": [
      2
    ],
    "tempo": 27,
    "setup": 2100,
    "codigo_barra": 52371
  },
  {
    "id_erp": 52372,
    "nome": "TRAVESSA MAD DIANTEIRA T0682 450 X 60 X 23MM - CADEIRA THAIS",
    "equipamentos": [
      2
    ],
    "tempo": 25,
    "setup": 2100,
    "codigo_barra": 52372
  },
  {
    "id_erp": 52373,
    "nome": "TRAVESSA MAD LATERAL T0683 425 X 65 X 22MM DIREITA - CADEIRA LIA LX C/ BRACO/ THAIS C/ BRACO",
    "equipamentos": [
      2
    ],
    "tempo": 20,
    "setup": 2100,
    "codigo_barra": 52373
  },
  {
    "id_erp": 52374,
    "nome": "TRAVESSA MAD LATERAL T0684 425 X 65 X 22MM ESQUERD - CADEIRA LIA LX C/ BRACO/ THAIS C/ BRACO",
    "equipamentos": [
      2
    ],
    "tempo": 20,
    "setup": 2100,
    "codigo_barra": 52374
  },
  {
    "id_erp": 52402,
    "nome": "PE MAD TRASEIRO P0559 765 X 80 X 32MM DIREITO - CADEIRA LIA LX C/ BRACO",
    "equipamentos": [
      3
    ],
    "tempo": 23,
    "setup": 5400,
    "codigo_barra": 52402
  },
  {
    "id_erp": 52403,
    "nome": "PE MAD TRASEIRO P0560 765 X 80 X 32MM ESQUERDO - CADEIRA LIA LX C/ BRACO",
    "equipamentos": [
      3
    ],
    "tempo": 23,
    "setup": 0,
    "codigo_barra": 52403
  },
  {
    "id_erp": 52404,
    "nome": "PE MAD DIANTEIRO P0561 587 X 55 X 32MM DIREITO - CADEIRA LIA LX C/ BRACO",
    "equipamentos": [
      3
    ],
    "tempo": 20,
    "setup": 2100,
    "codigo_barra": 52404
  },
  {
    "id_erp": 52405,
    "nome": "PE MAD DIANTEIRO P0562 587 X 55 X 32MM ESQUERDO - CADEIRA LIA LX C/ BRACO",
    "equipamentos": [
      3
    ],
    "tempo": 20,
    "setup": 2100,
    "codigo_barra": 52405
  },
  {
    "id_erp": 52406,
    "nome": "TRAVESSA MAD LATERAL T0685 380 X 105 X 32MM BRACO DIREITO - CADEIRA LIA LX C/ BRACO",
    "equipamentos": [
      2
    ],
    "tempo": 52,
    "setup": 5400,
    "codigo_barra": 52406
  },
  {
    "id_erp": 52407,
    "nome": "TRAVESSA MAD LATERAL T0686 380 X 105 X 32MM BRACO ESQUERDO - CADEIRA LIA LX C/ BRACO",
    "equipamentos": [
      2
    ],
    "tempo": 52,
    "setup": 0,
    "codigo_barra": 52407
  },
  {
    "id_erp": 52450,
    "nome": "TRAVESSA MAD DIANTEIRA T0693 530 X 75 X 22MM - CADEIRA LIA LX C/ BRACO",
    "equipamentos": [
      2
    ],
    "tempo": 30,
    "setup": 0,
    "codigo_barra": 52450
  },
  {
    "id_erp": 52450,
    "nome": "TRAVESSA MAD DIANTEIRA T0693 530 X 75 X 22MM - CADEIRA LIA LX C/ BRACO",
    "equipamentos": [
      1
    ],
    "tempo": 30,
    "setup": 0,
    "codigo_barra": 52450
  },
  {
    "id_erp": 53543,
    "nome": "TRAVESSA MAD TRASEIRA T0695 485 X 95 X 32MM - CADEIRA LIA LX C/ BRACO",
    "equipamentos": [
      2
    ],
    "tempo": 30,
    "setup": 4200,
    "codigo_barra": 53543
  },
  {
    "id_erp": 53543,
    "nome": "TRAVESSA MAD TRASEIRA T0695 485 X 95 X 32MM - CADEIRA LIA LX C/ BRACO",
    "equipamentos": [
      1
    ],
    "tempo": 30,
    "setup": 4200,
    "codigo_barra": 53543
  },
  {
    "id_erp": 53702,
    "nome": "CURVA MAD C0007 187 X 55 X 45MM - MESA JANTAR MITRE (420 X 87 X 46MM)",
    "equipamentos": [
      2
    ],
    "tempo": 19,
    "setup": 2100,
    "codigo_barra": 53702
  },
  {
    "id_erp": 53703,
    "nome": "TRAVESSA MAD T0846 866 X 55 X 45MM MENOR - MESA JANTAR MITRE",
    "equipamentos": [
      2
    ],
    "tempo": 19,
    "setup": 0,
    "codigo_barra": 53703
  },
  {
    "id_erp": 53867,
    "nome": "TRAVESSA MAD LATERAL T0697 480 X 70 X 22MM ESQ - CADEIRA MONACO (480 X 140 X 22MM)",
    "equipamentos": [
      2
    ],
    "tempo": 55,
    "setup": 0,
    "codigo_barra": 53867
  },
  {
    "id_erp": 53868,
    "nome": "TRAVESSA MAD LATERAL T0698 480 X 70 X 22MM DIR - CADEIRA MONACO (480 X 140 X 22MM)",
    "equipamentos": [
      2
    ],
    "tempo": 55,
    "setup": 2100,
    "codigo_barra": 53868
  },
  {
    "id_erp": 53869,
    "nome": "TRAVESSA MAD DIANTEIRA T0699 410 X 60 X 22MM - CADEIRA MONACO",
    "equipamentos": [
      2
    ],
    "tempo": 25,
    "setup": 0,
    "codigo_barra": 53869
  },
  {
    "id_erp": 53870,
    "nome": "TRAVESSA MAD TRASEIRA T0700 390 X 50 X 22MM - CADEIRA MONACO",
    "equipamentos": [
      2
    ],
    "tempo": 25,
    "setup": 3300,
    "codigo_barra": 53870
  },
  {
    "id_erp": 54150,
    "nome": "PE MAD TRASEIRO P0585 716 X 160 X 32MM ESQ - BANQUETA PAOLA 910MM",
    "equipamentos": [
      3
    ],
    "tempo": 30,
    "setup": 3300,
    "codigo_barra": 54150
  },
  {
    "id_erp": 54151,
    "nome": "PE MAD TRASEIRO P0586 716 X 160 X 32MM DIR - BANQUETA PAOLA 910MM",
    "equipamentos": [
      3
    ],
    "tempo": 30,
    "setup": 3300,
    "codigo_barra": 54151
  },
  {
    "id_erp": 54152,
    "nome": "PE MAD DIANTEIRO P0587 600 X 115 X 32MM ESQ - BANQUETA PAOLA 910MM",
    "equipamentos": [
      3
    ],
    "tempo": 27,
    "setup": 2100,
    "codigo_barra": 54152
  },
  {
    "id_erp": 54153,
    "nome": "PE MAD DIANTEIRO P0589 600 X 115 X 32MM DIR - BANQUETA PAOLA 910MM",
    "equipamentos": [
      3
    ],
    "tempo": 27,
    "setup": 2100,
    "codigo_barra": 54153
  },
  {
    "id_erp": 54159,
    "nome": "PE MAD TRASEIRO P0590 418 X 45 X 35MM ESQ - CADEIRA STELA LX",
    "equipamentos": [
      3
    ],
    "tempo": 5,
    "setup": 2100,
    "codigo_barra": 54159
  },
  {
    "id_erp": 54160,
    "nome": "PE MAD TRASEIRO P0591 418 X 45 X 35MM DIR - CADEIRA STELA LX",
    "equipamentos": [
      3
    ],
    "tempo": 6,
    "setup": 600,
    "codigo_barra": 54160
  },
  {
    "id_erp": 54247,
    "nome": "PE MAD TRASEIRO P0592 870 X 110 X 32MM DIR - BANQUETA LIA 930",
    "equipamentos": [
      3
    ],
    "tempo": 20,
    "setup": 600,
    "codigo_barra": 54247
  },
  {
    "id_erp": 54248,
    "nome": "PE MAD TRASEIRO P0593 870 X 110 X 32MM ESQ - BANQUETA LIA 930",
    "equipamentos": [
      3
    ],
    "tempo": 20,
    "setup": 600,
    "codigo_barra": 54248
  },
  {
    "id_erp": 54249,
    "nome": "PE MAD DIANTEIRO P0594 970 X 80 X 32MM DIR - BANQUETA LIA 930",
    "equipamentos": [
      3
    ],
    "tempo": 20,
    "setup": 2100,
    "codigo_barra": 54249
  },
  {
    "id_erp": 54250,
    "nome": "PE MAD DIANTEIRO P0595 970 X 80 X 32MM ESQ - BANQUETA LIA 930",
    "equipamentos": [
      3
    ],
    "tempo": 20,
    "setup": 2100,
    "codigo_barra": 54250
  },
  {
    "id_erp": 54270,
    "nome": "TRAVESSA MAD LATERAL T0708 550 X 80 X 22MM ESQ - CADEIRA MONACO C/ BRACO (560 X 155 X 22MM)",
    "equipamentos": [
      2
    ],
    "tempo": 55,
    "setup": 2100,
    "codigo_barra": 54270
  },
  {
    "id_erp": 54271,
    "nome": "TRAVESSA MAD LATERAL T0709 550 X 80 X 22MM DIR - CADEIRA MONACO C/ BRACO ( 560 X 155 X 22MM)",
    "equipamentos": [
      2
    ],
    "tempo": 55,
    "setup": 0,
    "codigo_barra": 54271
  },
  {
    "id_erp": 54272,
    "nome": "TRAVESSA MAD TRASEIRA T0710 375 X 50 X 22MM - CADEIRA MONACO C/ BRACO",
    "equipamentos": [
      2
    ],
    "tempo": 25,
    "setup": 3300,
    "codigo_barra": 54272
  },
  {
    "id_erp": 54273,
    "nome": "TRAVESSA MAD DIANTEIRA T0711 550 X 60 X 22MM - CADEIRA MONACO C/ BRACO",
    "equipamentos": [
      2
    ],
    "tempo": 25,
    "setup": 0,
    "codigo_barra": 54273
  },
  {
    "id_erp": 54277,
    "nome": "TRAVESSA MAD TRASEIRA T0712 430 X 45 X 28MM - CADEIRA ELIZE RATAN/ELIZE RATAN C/ BRACO (SEM FURO)",
    "equipamentos": [
      2
    ],
    "tempo": 27,
    "setup": 2820,
    "codigo_barra": 54277
  },
  {
    "id_erp": 54337,
    "nome": "TRAVESSA MAD LATERAL T0719 435 X 80 X 20MM ESQ - CADEIRA CAPINCHO",
    "equipamentos": [
      2
    ],
    "tempo": 23,
    "setup": 2100,
    "codigo_barra": 54337
  },
  {
    "id_erp": 54338,
    "nome": "TRAVESSA MAD LATERAL T0720 435 X 80 X 20MM DIR - CADEIRA CAPINCHO",
    "equipamentos": [
      2
    ],
    "tempo": 23,
    "setup": 0,
    "codigo_barra": 54338
  },
  {
    "id_erp": 54339,
    "nome": "TRAVESSA MAD TRASEIRA T0721 450 X 80 X 20MM - CADEIRA CAPINCHO",
    "equipamentos": [
      2
    ],
    "tempo": 40,
    "setup": 2100,
    "codigo_barra": 54339
  },
  {
    "id_erp": 54340,
    "nome": "TRAVESSA MAD DIANTEIRA T0722 510 X 80 X 20MM - CADEIRA CAPINCHO",
    "equipamentos": [
      2
    ],
    "tempo": 42,
    "setup": 2100,
    "codigo_barra": 54340
  },
  {
    "id_erp": 54346,
    "nome": "PE MAD DIANTEIRO P0604 555 X 40 X 40MM ESQ - CADEIRA BAMBOLE",
    "equipamentos": [
      3
    ],
    "tempo": 27,
    "setup": 0,
    "codigo_barra": 54346
  },
  {
    "id_erp": 54347,
    "nome": "PE MAD DIANTEIRO P0605 555 X 40 X 40MM DIR - CADEIRA BAMBOLE",
    "equipamentos": [
      3
    ],
    "tempo": 27,
    "setup": 0,
    "codigo_barra": 54347
  },
  {
    "id_erp": 54348,
    "nome": "PE MAD TRASEIRO P0606 530 X 40 X 40MM ESQ - CADEIRA BAMBOLE",
    "equipamentos": [
      3
    ],
    "tempo": 27,
    "setup": 2100,
    "codigo_barra": 54348
  },
  {
    "id_erp": 54349,
    "nome": "PE MAD TRASEIRO P0607 530 X 40 X 40MM DIR - CADEIRA BAMBOLE",
    "equipamentos": [
      3
    ],
    "tempo": 27,
    "setup": 600,
    "codigo_barra": 54349
  },
  {
    "id_erp": 54350,
    "nome": "TRAVESSA MAD LATERAL T0723 440 X 80 X 20MM ESQ - CADEIRA BAMBOLE",
    "equipamentos": [
      2
    ],
    "tempo": 80,
    "setup": 2100,
    "codigo_barra": 54350
  },
  {
    "id_erp": 54351,
    "nome": "TRAVESSA MAD LATERAL T0724 440 X 80 X 20MM DIR - CADEIRA BAMBOLE",
    "equipamentos": [
      2
    ],
    "tempo": 80,
    "setup": 0,
    "codigo_barra": 54351
  },
  {
    "id_erp": 54352,
    "nome": "TRAVESSA MAD TRASEIRA T0725 420 X 80 X 20MM - CADEIRA BAMBOLE",
    "equipamentos": [
      2
    ],
    "tempo": 94,
    "setup": 2100,
    "codigo_barra": 54352
  },
  {
    "id_erp": 54353,
    "nome": "TRAVESSA MAD DIANTEIRA T0726 510 X 80 X 20MM - CADEIRA BAMBOLE",
    "equipamentos": [
      2
    ],
    "tempo": 94,
    "setup": 2100,
    "codigo_barra": 54353
  },
  {
    "id_erp": 54774,
    "nome": "PE MAD DIANTEIRO P0610 230 X 40 X 40MM DIR - POLTRONA DALVA",
    "equipamentos": [
      2
    ],
    "tempo": 34,
    "setup": 5400,
    "codigo_barra": 54774
  },
  {
    "id_erp": 54775,
    "nome": "PE MAD DIANTEIRO P0611 230 X 40 X 40MM ESQ - POLTRONA DALVA",
    "equipamentos": [
      2
    ],
    "tempo": 34,
    "setup": 3000,
    "codigo_barra": 54775
  },
  {
    "id_erp": 54776,
    "nome": "PE MAD TRASEIRO P0612 390 X 40 X 40MM DIR - POLTRONA DALVA",
    "equipamentos": [
      2
    ],
    "tempo": 34,
    "setup": 0,
    "codigo_barra": 54776
  },
  {
    "id_erp": 54777,
    "nome": "PE MAD TRASEIRO P0613 390 X 40 X 40MM ESQ - POLTRONA DALVA",
    "equipamentos": [
      2
    ],
    "tempo": 34,
    "setup": 0,
    "codigo_barra": 54777
  },
  {
    "id_erp": 54778,
    "nome": "TRAVESSA MAD DIANTEIRA T0727 290 X 65 X 25MM DIR - POLTRONA DALVA (610 X 68 X 26MM)",
    "equipamentos": [
      2
    ],
    "tempo": 26,
    "setup": 4200,
    "codigo_barra": 54778
  },
  {
    "id_erp": 54779,
    "nome": "TRAVESSA MAD TRASEIRA T0728 310 X 65 X 25MM DIR - POLTRONA DALVA (610 X 68 X 26MM)",
    "equipamentos": [
      2
    ],
    "tempo": 26,
    "setup": 0,
    "codigo_barra": 54779
  },
  {
    "id_erp": 54810,
    "nome": "PE MAD TRASEIRO P0614 590 X 61 X 32MM DIR - CADEIRA TALITA",
    "equipamentos": [
      3
    ],
    "tempo": 12,
    "setup": 0,
    "codigo_barra": 54810
  },
  {
    "id_erp": 54811,
    "nome": "PE MAD TRASEIRO P0615 590 X 61 X 32MM ESQ - CADEIRA TALITA",
    "equipamentos": [
      3
    ],
    "tempo": 12,
    "setup": 0,
    "codigo_barra": 54811
  },
  {
    "id_erp": 54812,
    "nome": "PE MAD DIANTEIRO P0616 438 X 45 X 32MM DIR - CADEIRA TALITA",
    "equipamentos": [
      3
    ],
    "tempo": 13,
    "setup": 2100,
    "codigo_barra": 54812
  },
  {
    "id_erp": 54813,
    "nome": "PE MAD DIANTEIRO P0617 438 X 45 X 32MM ESQ - CADEIRA TALITA",
    "equipamentos": [
      3
    ],
    "tempo": 13,
    "setup": 2100,
    "codigo_barra": 54813
  },
  {
    "id_erp": 54814,
    "nome": "TRAVESSA MAD LATERAL T0739 455 X 60 X 22MM DIR - CADEIRA TALITA",
    "equipamentos": [
      2
    ],
    "tempo": 25,
    "setup": 2100,
    "codigo_barra": 54814
  },
  {
    "id_erp": 54815,
    "nome": "TRAVESSA MAD LATERAL T0740 455 X 60 X 22MM ESQ - CADEIRA TALITA",
    "equipamentos": [
      2
    ],
    "tempo": 25,
    "setup": 0,
    "codigo_barra": 54815
  },
  {
    "id_erp": 54857,
    "nome": "PE MAD TRASEIRO P0618 670 X 45 X 32MM ESQ - CADEIRA LUISE",
    "equipamentos": [
      3
    ],
    "tempo": 12,
    "setup": 0,
    "codigo_barra": 54857
  },
  {
    "id_erp": 54858,
    "nome": "PE MAD TRASEIRO P0619 670 X 45 X 32MM DIR - CADEIRA LUISE",
    "equipamentos": [
      3
    ],
    "tempo": 13,
    "setup": 0,
    "codigo_barra": 54858
  },
  {
    "id_erp": 54859,
    "nome": "PE MAD DIANTEIRO P0620 460 X 45 X 32MM ESQ - CADEIRA LUISE",
    "equipamentos": [
      3
    ],
    "tempo": 12,
    "setup": 3000,
    "codigo_barra": 54859
  },
  {
    "id_erp": 54860,
    "nome": "PE MAD DIANTEIRO P0621 460 X 45 X 32MM DIR - CADEIRA LUISE",
    "equipamentos": [
      3
    ],
    "tempo": 13,
    "setup": 3000,
    "codigo_barra": 54860
  },
  {
    "id_erp": 54861,
    "nome": "TRAVESSA MAD DIANTEIRA T0743 405 X 66 X 32MM - CADEIRA LUISE",
    "equipamentos": [
      2
    ],
    "tempo": 22,
    "setup": 3900,
    "codigo_barra": 54861
  },
  {
    "id_erp": 54862,
    "nome": "TRAVESSA MAD TRASEIRA T0744 310 X 43 X 23MM - CADEIRA LUISE",
    "equipamentos": [
      2
    ],
    "tempo": 22,
    "setup": 0,
    "codigo_barra": 54862
  },
  {
    "id_erp": 54863,
    "nome": "TRAVESSA MAD LATERAL T0745 465 X 47 X 23MM ESQ - CADEIRA LUISE",
    "equipamentos": [
      2
    ],
    "tempo": 26,
    "setup": 0,
    "codigo_barra": 54863
  },
  {
    "id_erp": 54864,
    "nome": "TRAVESSA MAD LATERAL T0746 465 X 47 X 23MM DIR - CADEIRA LUISE",
    "equipamentos": [
      2
    ],
    "tempo": 26,
    "setup": 4800,
    "codigo_barra": 54864
  },
  {
    "id_erp": 54865,
    "nome": "FRONTAL MAD  F0020 305 X 32 X 20MM - CADEIRA LUISE",
    "equipamentos": [
      2
    ],
    "tempo": 35,
    "setup": 3600,
    "codigo_barra": 54865
  },
  {
    "id_erp": 55049,
    "nome": "PE MAD TRASEIRO P0622 720 X 45 X 32MM - CADEIRA ANDRIA",
    "equipamentos": [
      3
    ],
    "tempo": 10,
    "setup": 4800,
    "codigo_barra": 55049
  },
  {
    "id_erp": 55050,
    "nome": "PE MAD TRASEIRO P0623 720 X 45 X 32MM DIR - CADEIRA ANDRIA",
    "equipamentos": [
      3
    ],
    "tempo": 10,
    "setup": 1800,
    "codigo_barra": 55050
  },
  {
    "id_erp": 55051,
    "nome": "PE MAD DIANTEIRO P0624 460 X 45 X 32MM ESQ - CADEIRA ANDRIA (480 X 75 X 32MM)",
    "equipamentos": [
      3
    ],
    "tempo": 10,
    "setup": 1800,
    "codigo_barra": 55051
  },
  {
    "id_erp": 55052,
    "nome": "PE MAD DIANTEIRO P0625 460 X 45 X 32MM DIR - CADEIRA ANDRIA (480 X 75 X 32MM)",
    "equipamentos": [
      3
    ],
    "tempo": 10,
    "setup": 0,
    "codigo_barra": 55052
  },
  {
    "id_erp": 55053,
    "nome": "TRAVESSA MAD DIANTEIRA T0747 405 X 66 X 32MM - CADEIRA ANDRIA",
    "equipamentos": [
      2
    ],
    "tempo": 25,
    "setup": 2700,
    "codigo_barra": 55053
  },
  {
    "id_erp": 55054,
    "nome": "TRAVESSA MAD LATERAL T0748 425 X 60 X 23MM ESQ - CADEIRA ANDRIA",
    "equipamentos": [
      2
    ],
    "tempo": 27,
    "setup": 2820,
    "codigo_barra": 55054
  },
  {
    "id_erp": 55055,
    "nome": "TRAVESSA MAD LATERAL T0749 425 X 60 X 23MM DIR - CADEIRA ANDRIA",
    "equipamentos": [
      2
    ],
    "tempo": 27,
    "setup": 0,
    "codigo_barra": 55055
  },
  {
    "id_erp": 55056,
    "nome": "TRAVESSA MAD TRASEIRA T0750 255 X 50 X 23MM - CADEIRA ANDRIA",
    "equipamentos": [
      2
    ],
    "tempo": 25,
    "setup": 0,
    "codigo_barra": 55056
  },
  {
    "id_erp": 55403,
    "nome": "PE MAD P0672 800 X 180 X 45MM ESQ - MESA JANTAR NEPAL",
    "equipamentos": [
      3
    ],
    "tempo": 30,
    "setup": 5400,
    "codigo_barra": 55403
  },
  {
    "id_erp": 55404,
    "nome": "PE MAD P0673 800 X 180 X 45MM DIR - MESA JANTAR NEPAL",
    "equipamentos": [
      3
    ],
    "tempo": 30,
    "setup": 0,
    "codigo_barra": 55404
  },
  {
    "id_erp": 55405,
    "nome": "TRAVESSA MAD T0891 490 X 75 X 32MM INF - MESA JANTAR NEPAL",
    "equipamentos": [
      2
    ],
    "tempo": 23,
    "setup": 2100,
    "codigo_barra": 55405
  },
  {
    "id_erp": 55406,
    "nome": "TRAVESSA MAD T0892 405 X 100 X 32MM SUP - MESA JANTAR NEPAL",
    "equipamentos": [
      2
    ],
    "tempo": 22,
    "setup": 2100,
    "codigo_barra": 55406
  },
  {
    "id_erp": 56062,
    "nome": "PE MAD TRASEIRO P0626 765 X 80 X 32MM ESQ - CADEIRA LIA LX",
    "equipamentos": [
      3
    ],
    "tempo": 25,
    "setup": 2100,
    "codigo_barra": 56062
  },
  {
    "id_erp": 56063,
    "nome": "PE MAD TRASEIRO P0627 765 X 80 X 32MM DIR - CADEIRA LIA LX",
    "equipamentos": [
      3
    ],
    "tempo": 25,
    "setup": 2100,
    "codigo_barra": 56063
  },
  {
    "id_erp": 56149,
    "nome": "TRAVESSA MAD T0757 430 X 60 X 32MM SUP - CADEIRA SELA (SEM FURO)",
    "equipamentos": [
      2
    ],
    "tempo": 36,
    "setup": 2100,
    "codigo_barra": 56149
  },
  {
    "id_erp": 56150,
    "nome": "TRAVESSA MAD T0758 430 X 60 X 32MM INF - CADEIRA SELA (COM FURO)",
    "equipamentos": [
      2
    ],
    "tempo": 36,
    "setup": 0,
    "codigo_barra": 56150
  },
  {
    "id_erp": 56180,
    "nome": "TRAVESSA MAD TRASEIRA T0759 485 X 95 X 32MM - CADEIRA LIA LX/LAMINADA/TAPECADA",
    "equipamentos": [
      2
    ],
    "tempo": 35,
    "setup": 5700,
    "codigo_barra": 56180
  },
  {
    "id_erp": 56180,
    "nome": "TRAVESSA MAD TRASEIRA T0759 485 X 95 X 32MM - CADEIRA LIA LX/LAMINADA/TAPECADA",
    "equipamentos": [
      1
    ],
    "tempo": 35,
    "setup": 5700,
    "codigo_barra": 56180
  },
  {
    "id_erp": 56181,
    "nome": "TRAVESSA MAD DIANTEIRA T0760 450 X 60 X 23MM - CADEIRA LIA LX/LAMINADA/TAPECADA",
    "equipamentos": [
      2
    ],
    "tempo": 35,
    "setup": 0,
    "codigo_barra": 56181
  },
  {
    "id_erp": 56181,
    "nome": "TRAVESSA MAD DIANTEIRA T0760 450 X 60 X 23MM - CADEIRA LIA LX/LAMINADA/TAPECADA",
    "equipamentos": [
      1
    ],
    "tempo": 35,
    "setup": 0,
    "codigo_barra": 56181
  },
  {
    "id_erp": 56182,
    "nome": "TRAVESSA MAD LATERAL T0761 425 X 65 X 22MM DIREITA - CADEIRA LIA LX/ LIA LX C/BRACO",
    "equipamentos": [
      2
    ],
    "tempo": 25,
    "setup": 5400,
    "codigo_barra": 56182
  },
  {
    "id_erp": 56182,
    "nome": "TRAVESSA MAD LATERAL T0761 425 X 65 X 22MM DIREITA - CADEIRA LIA LX/ LIA LX C/BRACO",
    "equipamentos": [
      3
    ],
    "tempo": 25,
    "setup": 5400,
    "codigo_barra": 56182
  },
  {
    "id_erp": 56183,
    "nome": "TRAVESSA MAD LATERAL T0762 425 X 65 X 22MM ESQUERDA - CADEIRA LIA LX/ LIA LX C/BRACO",
    "equipamentos": [
      2
    ],
    "tempo": 25,
    "setup": 0,
    "codigo_barra": 56183
  },
  {
    "id_erp": 56183,
    "nome": "TRAVESSA MAD LATERAL T0762 425 X 65 X 22MM ESQUERDA - CADEIRA LIA LX/ LIA LX C/BRACO",
    "equipamentos": [
      3
    ],
    "tempo": 25,
    "setup": 0,
    "codigo_barra": 56183
  },
  {
    "id_erp": 56275,
    "nome": "MONTADO LATERAL M0011 ESQUERDA (CADEIRA LIA LX C/ BRACO) - 2º ETAPA",
    "equipamentos": [
      1
    ],
    "tempo": 30,
    "setup": 3000,
    "codigo_barra": 56275
  },
  {
    "id_erp": 56276,
    "nome": "MONTADO LATERAL M0012 DIREITA (CADEIRA LIA LX C/ BRACO) - 2º ETAPA",
    "equipamentos": [
      1
    ],
    "tempo": 30,
    "setup": 3000,
    "codigo_barra": 56276
  },
  {
    "id_erp": 56320,
    "nome": "LATERAL MONTADA DIREITA (POLTRONA MALBEC) - 2º ETAPA",
    "equipamentos": [
      1
    ],
    "tempo": 65,
    "setup": 3600,
    "codigo_barra": 56320
  },
  {
    "id_erp": 56321,
    "nome": "LATERAL MONTADA  ESQUERDA (POLTRONA MALBEC) - 2º ETAPA",
    "equipamentos": [
      1
    ],
    "tempo": 65,
    "setup": 0,
    "codigo_barra": 56321
  },
  {
    "id_erp": 56741,
    "nome": "PE MAD DIANTEIRO P0632 435 X 71 X 45MM DIR - CADEIRA AGATA",
    "equipamentos": [
      3
    ],
    "tempo": 15,
    "setup": 2100,
    "codigo_barra": 56741
  },
  {
    "id_erp": 56742,
    "nome": "PE MAD DIANTEIRO P0633 435 X 71 X 45MM ESQ - CADEIRA AGATA",
    "equipamentos": [
      3
    ],
    "tempo": 15,
    "setup": 600,
    "codigo_barra": 56742
  },
  {
    "id_erp": 56743,
    "nome": "PE MAD TRASEIRO P0634 445 X 65 X 45MM DIR - CADEIRA AGATA",
    "equipamentos": [
      3
    ],
    "tempo": 15,
    "setup": 2100,
    "codigo_barra": 56743
  },
  {
    "id_erp": 56744,
    "nome": "PE MAD TRASEIRO P0635 445 X 65 X 45MM ESQ - CADEIRA AGATA",
    "equipamentos": [
      3
    ],
    "tempo": 15,
    "setup": 600,
    "codigo_barra": 56744
  },
  {
    "id_erp": 56745,
    "nome": "TRAVESSA MAD LATERAL T0767 345 X 60 X 45MM DIR - CADEIRA AGATA",
    "equipamentos": [
      2
    ],
    "tempo": 35,
    "setup": 0,
    "codigo_barra": 56745
  },
  {
    "id_erp": 56746,
    "nome": "TRAVESSA MAD LATERAL T0768 345 X 60 X 45MM ESQ - CADEIRA AGATA",
    "equipamentos": [
      2
    ],
    "tempo": 35,
    "setup": 4200,
    "codigo_barra": 56746
  },
  {
    "id_erp": 56747,
    "nome": "TRAVESSA MAD T0769 345 X 60 X 32MM DIANT/TRAS - CADEIRA AGATA",
    "equipamentos": [
      2
    ],
    "tempo": 87,
    "setup": 3000,
    "codigo_barra": 56747
  },
  {
    "id_erp": 57481,
    "nome": "TRAVESSA MAD LATERAL T0774 470 X 70 X 22MM DIREITA - CADEIRA DELTA",
    "equipamentos": [
      2
    ],
    "tempo": 44,
    "setup": 4200,
    "codigo_barra": 57481
  },
  {
    "id_erp": 57482,
    "nome": "TRAVESSA MAD LATERAL T0775 470 X 70 X 22MM ESQUERD - CADEIRA DELTA",
    "equipamentos": [
      2
    ],
    "tempo": 44,
    "setup": 0,
    "codigo_barra": 57482
  },
  {
    "id_erp": 57483,
    "nome": "TRAVESSA MAD DIANTEIRA T0776 325 X 67 X 22MM - CADEIRA DELTA",
    "equipamentos": [
      2
    ],
    "tempo": 39,
    "setup": 5400,
    "codigo_barra": 57483
  },
  {
    "id_erp": 57484,
    "nome": "TRAVESSA MAD TRASEIRA T0777 345 X 67 X 22MM - CADEIRA DELTA",
    "equipamentos": [
      2
    ],
    "tempo": 39,
    "setup": 0,
    "codigo_barra": 57484
  },
  {
    "id_erp": 57485,
    "nome": "ENCOSTO MONTADO MAD E0341 - CADEIRA DELTA - 2º ETAPA",
    "equipamentos": [
      1
    ],
    "tempo": 270,
    "setup": 2100,
    "codigo_barra": 57485
  },
  {
    "id_erp": 57487,
    "nome": "TRAVESSA MAD T0778 418 X 50 X 45MM SUPERIOR - CADEIRA DELTA/CADEIRA DELTA TAP",
    "equipamentos": [
      1
    ],
    "tempo": 20,
    "setup": 2700,
    "codigo_barra": 57487
  },
  {
    "id_erp": 57488,
    "nome": "TRAVESSA MAD T0779 446 X 46 X 46MM INFERIOR - CADEIRA DELTA/CADEIRA DELTA TAP",
    "equipamentos": [
      1
    ],
    "tempo": 20,
    "setup": 0,
    "codigo_barra": 57488
  },
  {
    "id_erp": 57489,
    "nome": "TRAVESSA MAD T0780 210 X 90 X 45MM DIREITA - CADEIRA DELTA/CADEIRA DELTA TAP",
    "equipamentos": [
      1
    ],
    "tempo": 20,
    "setup": 0,
    "codigo_barra": 57489
  },
  {
    "id_erp": 57490,
    "nome": "TRAVESSA MAD T0781 210 X 90 X 45MM ESQUERDA - CADEIRA DELTA/CADEIRA DELTA TAP",
    "equipamentos": [
      1
    ],
    "tempo": 20,
    "setup": 0,
    "codigo_barra": 57490
  },
  {
    "id_erp": 57505,
    "nome": "CURVA MAD C0008 140 X 50 X 31MM ALCA - APARADOR URBI (250 X 50 X 31MM)",
    "equipamentos": [
      2
    ],
    "tempo": 38,
    "setup": 3240,
    "codigo_barra": 57505
  },
  {
    "id_erp": 57506,
    "nome": "PE MAD P0679 693 X 70 X 30MM FRENTE DIREITO - APARADOR URBI (710 X 110 X 31MM)",
    "equipamentos": [
      3
    ],
    "tempo": 30,
    "setup": 6000,
    "codigo_barra": 57506
  },
  {
    "id_erp": 57507,
    "nome": "PE MAD P0680 755 X 45 X 30MM TRASEIRO - APARADOR URBI (770 X 82 X 31MM)",
    "equipamentos": [
      3
    ],
    "tempo": 16,
    "setup": 0,
    "codigo_barra": 57507
  },
  {
    "id_erp": 57508,
    "nome": "TRAVESSA MAD T0924 398 X 35 X 31MM ALCA - APARADOR URBI",
    "equipamentos": [
      2
    ],
    "tempo": 38,
    "setup": 0,
    "codigo_barra": 57508
  },
  {
    "id_erp": 57510,
    "nome": "TRAVESSA MAD T0925 1374 X 45 X 30MM EXTERNA TAMPO - APARADOR URBI 1,50 (1380 X 85 X 31MM)",
    "equipamentos": [
      3
    ],
    "tempo": 16,
    "setup": 3000,
    "codigo_barra": 57510
  },
  {
    "id_erp": 57513,
    "nome": "TRAVESSA MAD T0926 700 X 50 X 32MM VERTICAL - MESA JANTAR UOMINI LX",
    "equipamentos": [
      3
    ],
    "tempo": 50,
    "setup": 5400,
    "codigo_barra": 57513
  },
  {
    "id_erp": 58570,
    "nome": "TRAVESSA MAD T0977 770 X 45 X 30MM EXTERNA TAMPO - APARADOR URBI 0,90 (770 X 82 X 32MM)",
    "equipamentos": [
      3
    ],
    "tempo": 16,
    "setup": 3000,
    "codigo_barra": 58570
  },
  {
    "id_erp": 58619,
    "nome": "TRAVESSA MAD T0979 510 X 60 X 32MM LIGACAO - MESA CENTRO TANGARA 1,20/1,60/1,80 - 515 X 63 X 33MM",
    "equipamentos": [
      2
    ],
    "tempo": 58,
    "setup": 4500,
    "codigo_barra": 58619
  },
  {
    "id_erp": 58623,
    "nome": "TRAVESSA MAD T0980 805 X 60 X 32MM - MESA CENTRO TANGARA 0,90 - 810 X 63 X 33",
    "equipamentos": [
      2
    ],
    "tempo": 55,
    "setup": 2100,
    "codigo_barra": 58623
  },
  {
    "id_erp": 58781,
    "nome": "PE MAD DIANTEIRO P0645 430 X 45 X 32MM DIREITO - CADEIRA LINA",
    "equipamentos": [
      3
    ],
    "tempo": 11,
    "setup": 2100,
    "codigo_barra": 58781
  },
  {
    "id_erp": 58782,
    "nome": "PE MAD DIANTEIRO P0646 430 X 45 X 32MM ESQUERDO - CADEIRA LINA",
    "equipamentos": [
      3
    ],
    "tempo": 11,
    "setup": 600,
    "codigo_barra": 58782
  },
  {
    "id_erp": 58783,
    "nome": "PE MAD TRASEIRO P0647 613 X 45 X 32MM DIREITO - CADEIRA LINA",
    "equipamentos": [
      3
    ],
    "tempo": 11,
    "setup": 0,
    "codigo_barra": 58783
  },
  {
    "id_erp": 58784,
    "nome": "PE MAD TRASEIRO P0648 613 X 45 X 32MM ESQUERDO - CADEIRA LINA",
    "equipamentos": [
      3
    ],
    "tempo": 11,
    "setup": 0,
    "codigo_barra": 58784
  },
  {
    "id_erp": 58785,
    "nome": "TRAVESSA MAD LATERAL T0793 435 X 50 X 22MM DIREITA - CADEIRA LINA",
    "equipamentos": [
      2
    ],
    "tempo": 25,
    "setup": 2100,
    "codigo_barra": 58785
  },
  {
    "id_erp": 58786,
    "nome": "TRAVESSA MAD LATERAL T0794 435 X 50 X 22MM ESQUERD - CADEIRA LINA",
    "equipamentos": [
      2
    ],
    "tempo": 25,
    "setup": 0,
    "codigo_barra": 58786
  },
  {
    "id_erp": 58787,
    "nome": "TRAVESSA MAD TRASEIRA T0795 392 X 50 X 22MM - CADEIRA LINA",
    "equipamentos": [
      2
    ],
    "tempo": 15,
    "setup": 2100,
    "codigo_barra": 58787
  },
  {
    "id_erp": 58788,
    "nome": "TRAVESSA MAD DIANTEIRA T0796 392 X 50 X 22MM - CADEIRA LINA",
    "equipamentos": [
      2
    ],
    "tempo": 15,
    "setup": 0,
    "codigo_barra": 58788
  },
  {
    "id_erp": 58789,
    "nome": "TRAVESSA MAD T0797 355 X 32 X 25MM ENCOSTO - CADEIRA LINA",
    "equipamentos": [
      2
    ],
    "tempo": 17,
    "setup": 2100,
    "codigo_barra": 58789
  },
  {
    "id_erp": 58810,
    "nome": "PE MAD TRASEIRO P0649 920 X 52 X 32MM DIREITO - BANQUETA LIA LX 990",
    "equipamentos": [
      3
    ],
    "tempo": 19,
    "setup": 4800,
    "codigo_barra": 58810
  },
  {
    "id_erp": 58811,
    "nome": "PE MAD TRASEIRO P0650 920 X 52 X 32MM ESQUERDO - BANQUETA LIA LX 990",
    "equipamentos": [
      3
    ],
    "tempo": 19,
    "setup": 0,
    "codigo_barra": 58811
  },
  {
    "id_erp": 58812,
    "nome": "PE MAD DIANTEIRO P0651 715 X 50 X 32MM DIREITO - BANQUETA LIA LX 990",
    "equipamentos": [
      3
    ],
    "tempo": 11,
    "setup": 0,
    "codigo_barra": 58812
  },
  {
    "id_erp": 58813,
    "nome": "PE MAD DIANTEIRO P0652 715 X 50 X 32MM ESQUERDO - BANQUETA LIA LX 990",
    "equipamentos": [
      3
    ],
    "tempo": 11,
    "setup": 3600,
    "codigo_barra": 58813
  },
  {
    "id_erp": 58814,
    "nome": "TRAVESSA MAD DIANTEIRA T0798 437 X 59 X 22MM - BANQUETA LIA LX",
    "equipamentos": [
      2
    ],
    "tempo": 35,
    "setup": 4800,
    "codigo_barra": 58814
  },
  {
    "id_erp": 58815,
    "nome": "TRAVESSA MAD TRASEIRA T0799 461 X 92 X 32MM - BANQUETA LIA LX",
    "equipamentos": [
      2
    ],
    "tempo": 35,
    "setup": 0,
    "codigo_barra": 58815
  },
  {
    "id_erp": 58816,
    "nome": "TRAVESSA MAD LATERAL T0800 303 X 77 X 22MM DIREITA - BANQUETA LIA LX",
    "equipamentos": [
      2
    ],
    "tempo": 27,
    "setup": 0,
    "codigo_barra": 58816
  },
  {
    "id_erp": 58817,
    "nome": "TRAVESSA MAD LATERAL T0801 303 X 77 X 22MM ESQUERD - BANQUETA LIA LX",
    "equipamentos": [
      2
    ],
    "tempo": 27,
    "setup": 3000,
    "codigo_barra": 58817
  },
  {
    "id_erp": 59084,
    "nome": "PE MAD TRASEIRO P0653 820 X 52 X 32MM DIR - BANQUETA LIA LX 890",
    "equipamentos": [
      3
    ],
    "tempo": 19,
    "setup": 4800,
    "codigo_barra": 59084
  },
  {
    "id_erp": 59085,
    "nome": "PE MAD TRASEIRO P0654 820 X 52 X 32MM ESQ - BANQUETA LIA LX 890",
    "equipamentos": [
      3
    ],
    "tempo": 19,
    "setup": 0,
    "codigo_barra": 59085
  },
  {
    "id_erp": 59086,
    "nome": "PE MAD DIANTEIRO P0655 615 X 50 X 32MM DIR - BANQUETA LIA LX 890",
    "equipamentos": [
      3
    ],
    "tempo": 11,
    "setup": 0,
    "codigo_barra": 59086
  },
  {
    "id_erp": 59087,
    "nome": "PE MAD DIANTEIRO P0656 615 X 50 X 32MM ESQ - BANQUETA LIA LX 890",
    "equipamentos": [
      3
    ],
    "tempo": 11,
    "setup": 3600,
    "codigo_barra": 59087
  },
  {
    "id_erp": 59139,
    "nome": "TRAVESSA MAD LATERAL T805 1230 X 100 X 32MM - BANCO LAOS 1,60 (1240X105X33)",
    "equipamentos": [
      2
    ],
    "tempo": 56,
    "setup": 3000,
    "codigo_barra": 59139
  },
  {
    "id_erp": 59213,
    "nome": "PE MAD P0684 693 X 70 X 30MM FRENTE ESQUERDO - APARADOR URBI (710 X 110 X 31MM)",
    "equipamentos": [
      3
    ],
    "tempo": 30,
    "setup": 0,
    "codigo_barra": 59213
  },
  {
    "id_erp": 60000,
    "nome": "PÉ TRASEIRO DIR CADEIRA BORJE",
    "equipamentos": [
      3
    ],
    "tempo": 14,
    "setup": 2100,
    "codigo_barra": 60000
  },
  {
    "id_erp": 60001,
    "nome": "PÉ TRASEIRO ESQ CADEIRA BORJE",
    "equipamentos": [
      3
    ],
    "tempo": 13,
    "setup": 2100,
    "codigo_barra": 60001
  },
  {
    "id_erp": 60002,
    "nome": "PÉ FRENTE DIR CADEIRA BORJE",
    "equipamentos": [
      3
    ],
    "tempo": 14,
    "setup": 2100,
    "codigo_barra": 60002
  },
  {
    "id_erp": 60003,
    "nome": "PÉ FRENTE ESQ CADEIRA BORJE",
    "equipamentos": [
      3
    ],
    "tempo": 13,
    "setup": 2100,
    "codigo_barra": 60003
  },
  {
    "id_erp": 60004,
    "nome": "TRAV. CURVA ENCOSTO CADEIRA BORJE LAD DIR",
    "equipamentos": [
      2
    ],
    "tempo": 15,
    "setup": 2100,
    "codigo_barra": 60004
  },
  {
    "id_erp": 60005,
    "nome": "TRAV. FRENTE CADEIRA BORJE",
    "equipamentos": [
      2
    ],
    "tempo": 19,
    "setup": 600,
    "codigo_barra": 60005
  },
  {
    "id_erp": 60006,
    "nome": "TRAV. TRASEIRA CADEIRA BORJE",
    "equipamentos": [
      2
    ],
    "tempo": 18,
    "setup": 600,
    "codigo_barra": 60006
  },
  {
    "id_erp": 60007,
    "nome": "TRAV. LATERAL CADEIRA BORJE LAD DIR",
    "equipamentos": [
      2
    ],
    "tempo": 53,
    "setup": 600,
    "codigo_barra": 60007
  },
  {
    "id_erp": 60008,
    "nome": "TRAV. CURVA ENCOSTO CADEIRA BORJE LAD ESQ",
    "equipamentos": [
      2
    ],
    "tempo": 15,
    "setup": 2100,
    "codigo_barra": 60008
  },
  {
    "id_erp": 60009,
    "nome": "TRAV. LATERAL CADEIRA BORJE LAD ESQ",
    "equipamentos": [
      2
    ],
    "tempo": 53,
    "setup": 600,
    "codigo_barra": 60009
  },
  {
    "id_erp": 60010,
    "nome": "PROTÓTIPO CADEIRA LIA",
    "equipamentos": [
      2
    ],
    "tempo": 3,
    "setup": 1200,
    "codigo_barra": 60010
  },
  {
    "id_erp": 60020,
    "nome": "PROTÓTIPO CADEIRA LIA",
    "equipamentos": [
      3
    ],
    "tempo": 3,
    "setup": 1200,
    "codigo_barra": 60020
  },
  {
    "id_erp": 60128,
    "nome": "PE MAD DIANTEIRO P0658 541 X 68 X 43MM DIREITO - POLTRONA COPAN",
    "equipamentos": [
      3
    ],
    "tempo": 13,
    "setup": 5100,
    "codigo_barra": 60128
  },
  {
    "id_erp": 60129,
    "nome": "PE MAD DIANTEIRO P0659 541 X 68 X 43MM ESQUERDO - POLTRONA COPAN",
    "equipamentos": [
      3
    ],
    "tempo": 13,
    "setup": 0,
    "codigo_barra": 60129
  },
  {
    "id_erp": 60803,
    "nome": "PE MAD P0660 330 X 100 X 32MM - BANCO LAOS",
    "equipamentos": [
      2
    ],
    "tempo": 50,
    "setup": 4620,
    "codigo_barra": 60803
  },
  {
    "id_erp": 60804,
    "nome": "TRAVESSA MAD LATERAL T0814 1430 X 100 X 32MM - BANCO LAOS 1,80 (1440 X 105 X 33)",
    "equipamentos": [
      2
    ],
    "tempo": 56,
    "setup": 2400,
    "codigo_barra": 60804
  },
  {
    "id_erp": 61137,
    "nome": "LATERAL MAD L0710 340 X 82 X 32MM - PUFF JOLIE",
    "equipamentos": [
      1
    ],
    "tempo": 17,
    "setup": 3600,
    "codigo_barra": 61137
  },
  {
    "id_erp": 61138,
    "nome": "TRAVESSA MAD T1022 560 X 85 X 32MM FRENTE/TRAS - PUFF JOLIE",
    "equipamentos": [
      1
    ],
    "tempo": 17,
    "setup": 0,
    "codigo_barra": 61138
  },
  {
    "id_erp": 61170,
    "nome": "TRAVESSA MAD DIANTEIRA T0816 700 X 90 X 32MM - POLTRONA JOLIE",
    "equipamentos": [
      1
    ],
    "tempo": 17,
    "setup": 3600,
    "codigo_barra": 61170
  },
  {
    "id_erp": 61171,
    "nome": "TRAVESSA MAD LATERAL T0817 560 X 82 X 32MM - POLTRONA JOLIE",
    "equipamentos": [
      1
    ],
    "tempo": 17,
    "setup": 0,
    "codigo_barra": 61171
  },
  {
    "id_erp": 61186,
    "nome": "TRAVESSA MAD TRASEIRA T0818 512 X 90 X 32MM - POLTRONA JOLIE",
    "equipamentos": [
      1
    ],
    "tempo": 17,
    "setup": 0,
    "codigo_barra": 61186
  },
  {
    "id_erp": 61191,
    "nome": "PE MAD TRASEIRO P0661 541 X 68 X 43MM DIREITO - POLTRONA COPAN",
    "equipamentos": [
      3
    ],
    "tempo": 18,
    "setup": 5100,
    "codigo_barra": 61191
  },
  {
    "id_erp": 61192,
    "nome": "PE MAD TRASEIRO P0662 541 X 68 X 43MM ESQUERDO - POLTRONA COPAN",
    "equipamentos": [
      3
    ],
    "tempo": 20,
    "setup": 0,
    "codigo_barra": 61192
  },
  {
    "id_erp": 61198,
    "nome": "TRAVESSA MAD LATERAL T0819 675 X 91 X 43MM INFERIOR - POLTRONA COPAN",
    "equipamentos": [
      3
    ],
    "tempo": 20,
    "setup": 0,
    "codigo_barra": 61198
  },
  {
    "id_erp": 61199,
    "nome": "TRAVESSA MAD LATERAL T0820 790 X 85 X 43MM SUPERIOR - POLTRONA COPAN",
    "equipamentos": [
      3
    ],
    "tempo": 13,
    "setup": 0,
    "codigo_barra": 61199
  },
  {
    "id_erp": 61488,
    "nome": "TRAVESSA MAD DIANTEIRA T0824 290 X 65 X 25MM ESQ - POLTRONA DALVA (610 X 68 X 26MM)",
    "equipamentos": [
      2
    ],
    "tempo": 26,
    "setup": 0,
    "codigo_barra": 61488
  },
  {
    "id_erp": 61489,
    "nome": "TRAVESSA MAD TRASEIRA T0825 310 X 65 X 25MM ESQ - POLTRONA DALVA (610 X 68 X 26MM)",
    "equipamentos": [
      2
    ],
    "tempo": 26,
    "setup": 0,
    "codigo_barra": 61489
  },
  {
    "id_erp": 62415,
    "nome": "PE MAD TRASEIRO P0663 475 X 40 X 40MM DIREITO - POLTRONA BALEIA",
    "equipamentos": [
      3
    ],
    "tempo": 34,
    "setup": 2100,
    "codigo_barra": 62415
  },
  {
    "id_erp": 62906,
    "nome": "LATERAL MONTADA MAD L0005 DIREITO - CADEIRA VILAR RATAN - 2º ETAPA",
    "equipamentos": [
      1
    ],
    "tempo": 160,
    "setup": 0,
    "codigo_barra": 62906
  },
  {
    "id_erp": 62907,
    "nome": "LATERAL MONTADA MAD L0006 ESQUERDO - CADEIRA VILAR RATAN - 2º ETAPA",
    "equipamentos": [
      1
    ],
    "tempo": 160,
    "setup": 3600,
    "codigo_barra": 62907
  },
  {
    "id_erp": 62908,
    "nome": "PE MAD TRASEIRO P0664 805 X 60 X 32MM DIREITO - CADEIRA VILAR RATAN/TAPECADA",
    "equipamentos": [
      3
    ],
    "tempo": 49,
    "setup": 2100,
    "codigo_barra": 62908
  },
  {
    "id_erp": 62909,
    "nome": "TRAVESSA MAD LATERAL T0806 440 X 55 X 32MM DIREITO - CADEIRA VILAR RATAN/TAPECADA",
    "equipamentos": [
      2
    ],
    "tempo": 19,
    "setup": 3540,
    "codigo_barra": 62909
  },
  {
    "id_erp": 62910,
    "nome": "PE MAD DIANTEIRO P0665 410 X 45 X 32MM DIREITO - CADEIRA VILAR RATAN/TAPECADA",
    "equipamentos": [
      3
    ],
    "tempo": 49,
    "setup": 0,
    "codigo_barra": 62910
  },
  {
    "id_erp": 62911,
    "nome": "PE MAD TRASEIRO P0666 805 X 60 X 32MM ESQUERDO - CADEIRA VILAR RATAN/TAPECADA",
    "equipamentos": [
      3
    ],
    "tempo": 49,
    "setup": 2100,
    "codigo_barra": 62911
  },
  {
    "id_erp": 62912,
    "nome": "PE MAD DIANTEIRO P0667 410 X 45 X 32MM ESQUERDO - CADEIRA VILAR RATAN/TAPECADA",
    "equipamentos": [
      3
    ],
    "tempo": 49,
    "setup": 0,
    "codigo_barra": 62912
  },
  {
    "id_erp": 62913,
    "nome": "TRAVESSA MAD LATERAL T0806 440 X 55 X 32MM ESQUERDO - CADEIRA VILAR RATAN/TAPECADA",
    "equipamentos": [
      2
    ],
    "tempo": 19,
    "setup": 0,
    "codigo_barra": 62913
  },
  {
    "id_erp": 62914,
    "nome": "TRAVESSA MAD DIANTEIRA T0807 455 X 80 X 22MM BASE - CADEIRA VILAR RATAN/TAPECADA",
    "equipamentos": [
      2
    ],
    "tempo": 50,
    "setup": 5400,
    "codigo_barra": 62914
  },
  {
    "id_erp": 62915,
    "nome": "TRAVESSA MAD TRASEIRA T0808 440 X 72 X 22MM BASE - CADEIRA VILAR RATAN/TAPECADA",
    "equipamentos": [
      2
    ],
    "tempo": 50,
    "setup": 0,
    "codigo_barra": 62915
  },
  {
    "id_erp": 62916,
    "nome": "TRAVESSA MAD T0809 421 X 33 X 26MM SUP ENC - CADEIRA VILAR RATAN",
    "equipamentos": [
      3
    ],
    "tempo": 30,
    "setup": 3900,
    "codigo_barra": 62916
  },
  {
    "id_erp": 62917,
    "nome": "TRAVESSA MAD T0810 421 X 33 X 26MM INF ENC - CADEIRA VILAR RATAN",
    "equipamentos": [
      2
    ],
    "tempo": 70,
    "setup": 4800,
    "codigo_barra": 62917
  },
  {
    "id_erp": 62918,
    "nome": "TRAVESSA MAD TRASEIRA T0811 475 X 72 X 25MM ASSENTO MONT - CADEIRA VILAR RATAN",
    "equipamentos": [
      1
    ],
    "tempo": 23,
    "setup": 2100,
    "codigo_barra": 62918
  },
  {
    "id_erp": 62919,
    "nome": "TRAVESSA MAD DIANTEIRA T0812 490 X 70 X 25MM ASSENTO - CADEIRA VILAR RATAN",
    "equipamentos": [
      1
    ],
    "tempo": 22,
    "setup": 0,
    "codigo_barra": 62919
  },
  {
    "id_erp": 62928,
    "nome": "LATERAL MONTADA MAD L0007 DIREITO - CADEIRA VILAR TAPECADA - 2º ETAPA",
    "equipamentos": [
      1
    ],
    "tempo": 140,
    "setup": 3600,
    "codigo_barra": 62928
  },
  {
    "id_erp": 62929,
    "nome": "LATERAL MONTADA MAD L0008 ESQUERDO - CADEIRA VILAR TAPECADA - 2º ETAPA",
    "equipamentos": [
      1
    ],
    "tempo": 140,
    "setup": 0,
    "codigo_barra": 62929
  },
  {
    "id_erp": 62930,
    "nome": "ASSENTO MONTADO MAD A0524 - CADEIRA VILAR RATAN - 2º ETAPA",
    "equipamentos": [
      1
    ],
    "tempo": 221,
    "setup": 2100,
    "codigo_barra": 62930
  },
  {
    "id_erp": 62941,
    "nome": "PE MAD TRASEIRO P0670 590 X 50 X 32MM DIREITO - CADEIRA TALITA LX",
    "equipamentos": [
      3
    ],
    "tempo": 14,
    "setup": 4800,
    "codigo_barra": 62941
  },
  {
    "id_erp": 62943,
    "nome": "PE MAD DIANTEIRO P0672 438 X 45 X 32MM DIREITO - CADEIRA TALITA LX",
    "equipamentos": [
      3
    ],
    "tempo": 13,
    "setup": 0,
    "codigo_barra": 62943
  },
  {
    "id_erp": 62945,
    "nome": "TRAVESSA MAD T0811 421 X 33 X 26MM SUP ENC - CADEIRA VILAR TAPECADA",
    "equipamentos": [
      2
    ],
    "tempo": 30,
    "setup": 3900,
    "codigo_barra": 62945
  },
  {
    "id_erp": 62945,
    "nome": "TRAVESSA MAD T0811 421 X 33 X 26MM SUP ENC - CADEIRA VILAR TAPECADA",
    "equipamentos": [
      3
    ],
    "tempo": 30,
    "setup": 3900,
    "codigo_barra": 62945
  },
  {
    "id_erp": 62946,
    "nome": "TRAVESSA MAD T0812 421 X 33 X 26MM INF ENC - CADEIRA VILAR TAPECADA",
    "equipamentos": [
      2
    ],
    "tempo": 30,
    "setup": 4800,
    "codigo_barra": 62946
  },
  {
    "id_erp": 62947,
    "nome": "TRAVESSA MAD LATERAL T0813 452 X 65 X 22MM DIREITA - CADEIRA TALITA LX",
    "equipamentos": [
      2
    ],
    "tempo": 30,
    "setup": 4800,
    "codigo_barra": 62947
  },
  {
    "id_erp": 62948,
    "nome": "TRAVESSA MAD LATERAL T0814 452 X 65 X 22MM ESQUERDA - CADEIRA TALITA LX",
    "equipamentos": [
      2
    ],
    "tempo": 30,
    "setup": 0,
    "codigo_barra": 62948
  },
  {
    "id_erp": 62952,
    "nome": "TRAVESSA MAD T0817 450 X 22 X 22MM ENCOSTO - CADEIRA TALITA LX",
    "equipamentos": [
      2
    ],
    "tempo": 45,
    "setup": 3480,
    "codigo_barra": 62952
  },
  {
    "id_erp": 62965,
    "nome": "TRAVESSA MAD DIANTEIRA T0821 457 X 139 X 45MM - CADEIRA JOLIE",
    "equipamentos": [
      1
    ],
    "tempo": 38,
    "setup": 2100,
    "codigo_barra": 62965
  },
  {
    "id_erp": 62966,
    "nome": "TRAVESSA MAD TRASEIRA T0822 371 X 124 X 45MM - CADEIRA JOLIE",
    "equipamentos": [
      1
    ],
    "tempo": 38,
    "setup": 0,
    "codigo_barra": 62966
  },
  {
    "id_erp": 62967,
    "nome": "TRAVESSA MAD LATERAL T0823 316 X 119 X 45MM - CADEIRA JOLIE",
    "equipamentos": [
      1
    ],
    "tempo": 38,
    "setup": 0,
    "codigo_barra": 62967
  },
  {
    "id_erp": 62995,
    "nome": "TRAVESSA MAD DIANTEIRA T0826 465 X 146 X 32MM ASSENTO - CADEIRA JOLIE GIRATORIA",
    "equipamentos": [
      1
    ],
    "tempo": 28,
    "setup": 0,
    "codigo_barra": 62995
  },
  {
    "id_erp": 62996,
    "nome": "TRAVESSA MAD TRASEIRA T0827 357 X 120 X 32MM ASSENTO - CADEIRA JOLIE GIRATORIA",
    "equipamentos": [
      1
    ],
    "tempo": 28,
    "setup": 3600,
    "codigo_barra": 62996
  },
  {
    "id_erp": 62997,
    "nome": "TRAVESSA MAD LATERAL T0828 322 X 126 X 32MM ASSENTO - CADEIRA JOLIE GIRATORIA",
    "equipamentos": [
      1
    ],
    "tempo": 28,
    "setup": 0,
    "codigo_barra": 62997
  },
  {
    "id_erp": 63027,
    "nome": "TRAVESSA MAD T0840 420 X 50 X 38MM SUPERIOR - BANQUETA DELTA/ BANQUETA DELTA TAP",
    "equipamentos": [
      1
    ],
    "tempo": 13,
    "setup": 2100,
    "codigo_barra": 63027
  },
  {
    "id_erp": 63028,
    "nome": "TRAVESSA MAD T0841 400 X 45 X 45MM INFERIOR - BANQUETA DELTA/BANQUETA DELTA TAP",
    "equipamentos": [
      1
    ],
    "tempo": 13,
    "setup": 0,
    "codigo_barra": 63028
  },
  {
    "id_erp": 63031,
    "nome": "TRAVESSA MAD LATERAL T0836 432 X 60 X 22MM DIREITO - BANQUETA DELTA",
    "equipamentos": [
      2
    ],
    "tempo": 30,
    "setup": 3600,
    "codigo_barra": 63031
  },
  {
    "id_erp": 63036,
    "nome": "TRAVESSA MAD LATERAL T0837 432 X 60 X 22MM ESQUERDO - BANQUETA DELTA",
    "equipamentos": [
      2
    ],
    "tempo": 30,
    "setup": 0,
    "codigo_barra": 63036
  },
  {
    "id_erp": 63037,
    "nome": "TRAVESSA MAD DIANTEIRA T0837 302 X 50 X 22MM - BANQUETA DELTA",
    "equipamentos": [
      2
    ],
    "tempo": 42,
    "setup": 3780,
    "codigo_barra": 63037
  },
  {
    "id_erp": 63038,
    "nome": "TRAVESSA MAD TRASEIRA T0838 301 X 50 X 22MM - BANQUETA DELTA",
    "equipamentos": [
      2
    ],
    "tempo": 42,
    "setup": 0,
    "codigo_barra": 63038
  },
  {
    "id_erp": 63039,
    "nome": "ENCOSTO MONTADO MAD E0356 - BANQUETA DELTA - 2º ETAPA",
    "equipamentos": [
      1
    ],
    "tempo": 360,
    "setup": 3600,
    "codigo_barra": 63039
  },
  {
    "id_erp": 63040,
    "nome": "TRAVESSA MAD LATERAL T0842 150 X 31 X 25MM ENCOSTO - BANQUETA DELTA/BANQUETA DELTA TAP",
    "equipamentos": [
      1
    ],
    "tempo": 13,
    "setup": 0,
    "codigo_barra": 63040
  },
  {
    "id_erp": 63049,
    "nome": "PE MAD TRASEIRO P0683 297 X 45 X 32MM - PUFF PAOLA",
    "equipamentos": [
      3
    ],
    "tempo": 12,
    "setup": 0,
    "codigo_barra": 63049
  },
  {
    "id_erp": 63051,
    "nome": "PE MAD DIANTEIRO E0685 235 X 55 X 32MM - PUFF PAOLA",
    "equipamentos": [
      3
    ],
    "tempo": 12,
    "setup": 6000,
    "codigo_barra": 63051
  },
  {
    "id_erp": 63052,
    "nome": "TRAVESSA MAD LATERAL T0845 385 X 65 X 32MM ESQUERDA - PUFF PAOLA",
    "equipamentos": [
      2
    ],
    "tempo": 54,
    "setup": 4500,
    "codigo_barra": 63052
  },
  {
    "id_erp": 63053,
    "nome": "TRAVESSA MAD LATERAL T0846 385 X 65 X 32MM DIREITA - PUFF PAOLA",
    "equipamentos": [
      2
    ],
    "tempo": 54,
    "setup": 0,
    "codigo_barra": 63053
  },
  {
    "id_erp": 63118,
    "nome": "PE MAD TRASEIRO P0685 465 X 73 X 32MM - POLTRONA PAOLA",
    "equipamentos": [
      3
    ],
    "tempo": 18,
    "setup": 2100,
    "codigo_barra": 63118
  },
  {
    "id_erp": 63120,
    "nome": "TRAVESSA MAD LATERAL T0852 527 X 100 X 32MM DIREITA - POLTRONA PAOLA",
    "equipamentos": [
      1
    ],
    "tempo": 55,
    "setup": 2100,
    "codigo_barra": 63120
  },
  {
    "id_erp": 63121,
    "nome": "TRAVESSA MAD LATERAL T0853 527 X 100 X 32MM ESQUERDA - POLTRONA PAOLA",
    "equipamentos": [
      1
    ],
    "tempo": 55,
    "setup": 0,
    "codigo_barra": 63121
  },
  {
    "id_erp": 63122,
    "nome": "PE MAD DIANTEIRO P0687 286 X 65 X 32MM - POLTRONA PAOLA",
    "equipamentos": [
      3
    ],
    "tempo": 17,
    "setup": 2100,
    "codigo_barra": 63122
  },
  {
    "id_erp": 63124,
    "nome": "TRAVESSA MAD DIANTEIRA T0854 711 X 64 X 22MM - POLTRONA PAOLA",
    "equipamentos": [
      1
    ],
    "tempo": 45,
    "setup": 2100,
    "codigo_barra": 63124
  },
  {
    "id_erp": 63125,
    "nome": "TRAVESSA MAD TRASEIRA T0855 641 X 71 X 22MM - POLTRONA PAOLA",
    "equipamentos": [
      1
    ],
    "tempo": 45,
    "setup": 2100,
    "codigo_barra": 63125
  },
  {
    "id_erp": 63127,
    "nome": "ENCOSTO PRENSADO TAP E0357 420 X 600 X 20MM - MEIO - POLTRONA PAOLA",
    "equipamentos": [
      1
    ],
    "tempo": 60,
    "setup": 2100,
    "codigo_barra": 63127
  },
  {
    "id_erp": 63128,
    "nome": "ENCOSTO PRENSADO TAP E0358 500 X 100 X 20MM - UNIAO ESQUERDA - POLTRONA PAOLA",
    "equipamentos": [
      1
    ],
    "tempo": 60,
    "setup": 2100,
    "codigo_barra": 63128
  },
  {
    "id_erp": 63129,
    "nome": "ENCOSTO PRENSADO TAP E0359 500 X 100 X 20MM - UNIAO DIREITA - POLTRONA PAOLA",
    "equipamentos": [
      1
    ],
    "tempo": 130,
    "setup": 2100,
    "codigo_barra": 63129
  },
  {
    "id_erp": 63163,
    "nome": "PE MAD TRASEIRO P0689 420 X 42 X 42MM ESQUERDO - CADEIRA SOFIA LX",
    "equipamentos": [
      3
    ],
    "tempo": 12,
    "setup": 2100,
    "codigo_barra": 63163
  },
  {
    "id_erp": 63164,
    "nome": "PE MAD DIANTEIRO P0690 400 X 42 X 42MM ESQUERDO - CADEIRA SOFIA LX",
    "equipamentos": [
      3
    ],
    "tempo": 12,
    "setup": 2100,
    "codigo_barra": 63164
  },
  {
    "id_erp": 63165,
    "nome": "PE MAD TRASEIRO P0691 420 X 42 X 42MM DIREITO - CADEIRA SOFIA LX",
    "equipamentos": [
      3
    ],
    "tempo": 12,
    "setup": 2100,
    "codigo_barra": 63165
  },
  {
    "id_erp": 63166,
    "nome": "PE MAD DIANTEIRO P0692 400 X 42 X 42MM DIREITO - CADEIRA SOFIA LX",
    "equipamentos": [
      3
    ],
    "tempo": 12,
    "setup": 2100,
    "codigo_barra": 63166
  },
  {
    "id_erp": 63182,
    "nome": "TRAVESSA MAD LATERAL T0806 515 X 63 X 32MM ESQUERDA - POLTRONA CLARA/TINA",
    "equipamentos": [
      2
    ],
    "tempo": 45,
    "setup": 2100,
    "codigo_barra": 63182
  },
  {
    "id_erp": 63411,
    "nome": "PE MAD TRASEIRO P0693 430 X 100 X 45MM ESQUERDO - CADEIRA TINA",
    "equipamentos": [
      3
    ],
    "tempo": 18,
    "setup": 1200,
    "codigo_barra": 63411
  },
  {
    "id_erp": 63412,
    "nome": "PE MAD TRASEIRO P0694 430 X 100 X 45MM DIREITO - CADEIRA TINA",
    "equipamentos": [
      3
    ],
    "tempo": 18,
    "setup": 1200,
    "codigo_barra": 63412
  },
  {
    "id_erp": 63413,
    "nome": "PE MAD DIANTEIRO P0695 430 X 100 X 45MM ESQUERDO - CADEIRA TINA",
    "equipamentos": [
      3
    ],
    "tempo": 18,
    "setup": 1500,
    "codigo_barra": 63413
  },
  {
    "id_erp": 63414,
    "nome": "PE MAD DIANTEIRO P0696 430 X 100 X 45MM DIREITO - CADEIRA TINA",
    "equipamentos": [
      3
    ],
    "tempo": 18,
    "setup": 1500,
    "codigo_barra": 63414
  },
  {
    "id_erp": 63427,
    "nome": "TRAVESSA MAD LATERAL T0875 490 X 63 X 32MM ESQUERDA - CADEIRA TINA",
    "equipamentos": [
      2
    ],
    "tempo": 45,
    "setup": 2100,
    "codigo_barra": 63427
  },
  {
    "id_erp": 63428,
    "nome": "TRAVESSA MAD LATERAL T0876 490 X 63 X 32MM DIREITA - CADEIRA TINA",
    "equipamentos": [
      2
    ],
    "tempo": 45,
    "setup": 2100,
    "codigo_barra": 63428
  },
  {
    "id_erp": 63447,
    "nome": "PE MAD DIANTEIRO P0697 525 X 40 X 40MM DIREITO - POLTRONA BALEIA",
    "equipamentos": [
      3
    ],
    "tempo": 34,
    "setup": 0,
    "codigo_barra": 63447
  },
  {
    "id_erp": 63452,
    "nome": "TRAVESSA MAD LATERAL T0880 740 X 55 X 32MM - POLTRONA BALEIA",
    "equipamentos": [
      2
    ],
    "tempo": 26,
    "setup": 2100,
    "codigo_barra": 63452
  },
  {
    "id_erp": 63472,
    "nome": "TRAVESSA MAD BRACO T0886 833 X 90 X 24MM - POLTRONA BALEIA",
    "equipamentos": [
      1
    ],
    "tempo": 240,
    "setup": 2100,
    "codigo_barra": 63472
  },
  {
    "id_erp": 65035,
    "nome": "PE MAD TRASEIRO P0670 590 X 50 X 32MM ESQEURDO - CADEIRA TALITA LX",
    "equipamentos": [
      3
    ],
    "tempo": 14,
    "setup": 0,
    "codigo_barra": 65035
  },
  {
    "id_erp": 65036,
    "nome": "PE MAD DIANTEIRO P0672 438 X 45 X 32MM ESQUERDO - CADEIRA TALITA LX",
    "equipamentos": [
      3
    ],
    "tempo": 13,
    "setup": 2100,
    "codigo_barra": 65036
  },
  {
    "id_erp": 65232,
    "nome": "PE MAD TRASEIRO P0663 475 X 40 X 40MM ESQUERDO - POLTRONA BALEIA",
    "equipamentos": [
      3
    ],
    "tempo": 34,
    "setup": 2100,
    "codigo_barra": 65232
  },
  {
    "id_erp": 65233,
    "nome": "PE MAD DIANTEIRO P0697 525 X 40 X 40MM ESQUERDO - POLTRONA BALEIA",
    "equipamentos": [
      3
    ],
    "tempo": 34,
    "setup": 0,
    "codigo_barra": 65233
  },
  {
    "id_erp": 65330,
    "nome": "ASSENTO MDF A0550 395 X 430 X 30MM RETO - CADEIRA KRAFT EUCALIPTO",
    "equipamentos": [
      1
    ],
    "tempo": 242,
    "setup": 2100,
    "codigo_barra": 65330
  },
  {
    "id_erp": 65967,
    "nome": "TRAVESSA MAD LATERAL T0806 450 X 73 X 22MM DIR - CADEIRA BAIA",
    "equipamentos": [
      2
    ],
    "tempo": 34,
    "setup": 4080,
    "codigo_barra": 65967
  },
  {
    "id_erp": 65970,
    "nome": "TRAVESSA MAD LATERAL T0807 450 X 73 X 22MM ESQ - CADEIRA BAIA",
    "equipamentos": [
      2
    ],
    "tempo": 34,
    "setup": 0,
    "codigo_barra": 65970
  },
  {
    "id_erp": 65975,
    "nome": "TRAVESSA MAD DIANTEIRA T0806 365 X 60 X 32MM - CADEIRA/BANQUETA BAIA",
    "equipamentos": [
      2
    ],
    "tempo": 30,
    "setup": 3600,
    "codigo_barra": 65975
  },
  {
    "id_erp": 66303,
    "nome": "TRAVESSA MAD BRACO T0806 340 X 74 X 32MM FRENTE DIREITO - CADEIRA MIRO (1º ETAPA)",
    "equipamentos": [
      1
    ],
    "tempo": 25,
    "setup": 0,
    "codigo_barra": 66303
  },
  {
    "id_erp": 66304,
    "nome": "TRAVESSA MAD BRACO T0808 340 X 74 X 32MM FRENTE ESQUERDO - CADEIRA MIRO (1º ETAPA)",
    "equipamentos": [
      1
    ],
    "tempo": 25,
    "setup": 0,
    "codigo_barra": 66304
  },
  {
    "id_erp": 66312,
    "nome": "TRAVESSA MAD BRACO T0812 160 X 42 X 32MM TRASEIRO DIREITO - CADEIRA MIRO (1º ETAPA)",
    "equipamentos": [
      1
    ],
    "tempo": 25,
    "setup": 2700,
    "codigo_barra": 66312
  },
  {
    "id_erp": 66313,
    "nome": "TRAVESSA MAD BRACO T0813 160 X 42 X 32MM TRASEIRO ESQUERDO - CADEIRA MIRO (1º ETAPA)",
    "equipamentos": [
      1
    ],
    "tempo": 25,
    "setup": 0,
    "codigo_barra": 66313
  },
  {
    "id_erp": 66641,
    "nome": "TRAVESSA MAD DIANTEIRA T0807 834 X 42 X 22MM BASE - POLTRONA MONET",
    "equipamentos": [
      2
    ],
    "tempo": 41,
    "setup": 3120,
    "codigo_barra": 66641
  },
  {
    "id_erp": 66643,
    "nome": "TRAVESSA MAD TRASEIRA T0809 527 X 32 X 42MM INFERIOR - POLTRONA MONET",
    "equipamentos": [
      1
    ],
    "tempo": 23,
    "setup": 0,
    "codigo_barra": 66643
  },
  {
    "id_erp": 66644,
    "nome": "TRAVESSA MAD TRASEIRA T0810 515 X 22 X 42MM SUPERIOR - POLTRONA MONET",
    "equipamentos": [
      1
    ],
    "tempo": 23,
    "setup": 0,
    "codigo_barra": 66644
  },
  {
    "id_erp": 66645,
    "nome": "TRAVESSA MAD LATERAL T0811 538 X 32 X 42MM INFERIOR ESQUERDA - POLTRONA MONET",
    "equipamentos": [
      1
    ],
    "tempo": 23,
    "setup": 3600,
    "codigo_barra": 66645
  },
  {
    "id_erp": 66646,
    "nome": "TRAVESSA MAD LATERAL T0812 541 X 22 X 42MM SUPERIOR - POLTRONA MONET",
    "equipamentos": [
      2
    ],
    "tempo": 27,
    "setup": 3000,
    "codigo_barra": 66646
  },
  {
    "id_erp": 67464,
    "nome": "PE MAD P0685 340 X 70 X 32MM (MESA APOIO KALA)",
    "equipamentos": [
      2
    ],
    "tempo": 28,
    "setup": 2100,
    "codigo_barra": 67464
  },
  {
    "id_erp": 68125,
    "nome": "TRAVESSA MAD LATERAL T0811 538 X 32 X 42MM INFERIOR DIREITA - POLTRONA MONET",
    "equipamentos": [
      1
    ],
    "tempo": 23,
    "setup": 0,
    "codigo_barra": 68125
  },
  {
    "id_erp": 68143,
    "nome": "BRAÇO MONTADO - CADEIRA MIRO (2º ETAPA)",
    "equipamentos": [
      1
    ],
    "tempo": 522,
    "setup": 2100,
    "codigo_barra": 68143
  },
  {
    "id_erp": 68714,
    "nome": "PE MAD TRASEIRO P0726 691 X 86 X 32MM DIREITO - CADEIRA ADHARA",
    "equipamentos": [
      3
    ],
    "tempo": 31,
    "setup": 5100,
    "codigo_barra": 68714
  },
  {
    "id_erp": 68715,
    "nome": "PE MAD TRASEIRO P0727 691 X 86 X 32MM ESQUERDO - CADEIRA ADHARA",
    "equipamentos": [
      3
    ],
    "tempo": 31,
    "setup": 0,
    "codigo_barra": 68715
  },
  {
    "id_erp": 68718,
    "nome": "TRAVESSA MAD LATERAL T0806 366 X 67 X 22MM DIREITA - CADEIRA ADHARA",
    "equipamentos": [
      1
    ],
    "tempo": 40,
    "setup": 0,
    "codigo_barra": 68718
  },
  {
    "id_erp": 68719,
    "nome": "TRAVESSA MAD LATERAL T0609 366 X 67 X 22MM ESQUERDA - CADEIRA ADHARA",
    "equipamentos": [
      1
    ],
    "tempo": 40,
    "setup": 5400,
    "codigo_barra": 68719
  },
  {
    "id_erp": 68720,
    "nome": "TRAVESSA MAD DIANTEIRA T0806 440 X 60 X 32MM BASE - CADEIRA ADHARA",
    "equipamentos": [
      2
    ],
    "tempo": 70,
    "setup": 4260,
    "codigo_barra": 68720
  },
  {
    "id_erp": 68721,
    "nome": "TRAVESSA MAD TRASEIRA T0807 454 X 55 X 22MM BASE - CADEIRA ADHARA",
    "equipamentos": [
      1
    ],
    "tempo": 32,
    "setup": 3600,
    "codigo_barra": 68721
  },
  {
    "id_erp": 69148,
    "nome": "TRAVESSA MAD LATERAL T0806 575 X 77 X 22MM DIREITA - POLTRONA DELTA",
    "equipamentos": [
      1
    ],
    "tempo": "-",
    "setup": 3600,
    "codigo_barra": 69148
  },
  {
    "id_erp": 69149,
    "nome": "TRAVESSA MAD LATERAL T0807 575 X 77 X 22MM ESQUERDA - POLTRONA DELTA",
    "equipamentos": [
      1
    ],
    "tempo": "-",
    "setup": 3600,
    "codigo_barra": 69149
  },
  {
    "id_erp": 69150,
    "nome": "TRAVESSA MAD DIANTEIRA T0806 692 X 105 X 22MM - POLTRONA DELTA",
    "equipamentos": [
      1
    ],
    "tempo": "-",
    "setup": 3600,
    "codigo_barra": 69150
  },
  {
    "id_erp": 69155,
    "nome": "ENCOSTO MONTADO MAD E0377 - POLTRONA DELTA - 2º ETAPA",
    "equipamentos": [
      1
    ],
    "tempo": 200,
    "setup": 2100,
    "codigo_barra": 69155
  },
  {
    "id_erp": 69156,
    "nome": "TRAVESSA MAD BRACO T0806 135 X 32 X 45MM DIREITO MENOR (UNIÃO) - POLTRONA DELTA",
    "equipamentos": [
      1
    ],
    "tempo": 43,
    "setup": 3600,
    "codigo_barra": 69156
  },
  {
    "id_erp": 69157,
    "nome": "TRAVESSA MAD BRACO T0807 450 X 50 X 32MM DIREITO MAIOR - POLTRONA DELTA",
    "equipamentos": [
      1
    ],
    "tempo": 45,
    "setup": 3600,
    "codigo_barra": 69157
  },
  {
    "id_erp": 69158,
    "nome": "TRAVESSA MAD BRACO T0808 135 X 32 X 45MM ESQUERDO MENOR (UNIÃO) - POLTRONA DELTA",
    "equipamentos": [
      1
    ],
    "tempo": 43,
    "setup": 0,
    "codigo_barra": 69158
  },
  {
    "id_erp": 69159,
    "nome": "TRAVESSA MAD BRACO T0809 450 X 50 X 32MM ESQUERDO MAIOR - POLTRONA DELTA",
    "equipamentos": [
      1
    ],
    "tempo": 45,
    "setup": 0,
    "codigo_barra": 69159
  },
  {
    "id_erp": 69160,
    "nome": "TRAVESSA MAD T0806 470 X 32 X 32MM SUPERIOR - POLTRONA DELTA / POLTRONA DELTA TAP",
    "equipamentos": [
      1
    ],
    "tempo": 14,
    "setup": 0,
    "codigo_barra": 69160
  },
  {
    "id_erp": 69161,
    "nome": "TRAVESSA MAD T0809 480 X 32 X 32MM INFERIOR - POLTRONA DELTA / POLTRONA DELTA TAP",
    "equipamentos": [
      1
    ],
    "tempo": 14,
    "setup": 0,
    "codigo_barra": 69161
  },
  {
    "id_erp": 69186,
    "nome": "TRAVESSA MAD T0806 420 X 100 X 22MM INFERIOR - BANQUETA GIRATORIA PIER 940/1040",
    "equipamentos": [
      2
    ],
    "tempo": 52,
    "setup": 3600,
    "codigo_barra": 69186
  },
  {
    "id_erp": 69187,
    "nome": "TRAVESSA MAD T0812 420 X 100 X 22MM SUPERIOR - BANQUETA GIRATORIA PIER 940/1040",
    "equipamentos": [
      2
    ],
    "tempo": 52,
    "setup": 0,
    "codigo_barra": 69187
  },
  {
    "id_erp": 69595,
    "nome": "TRAVESSA MAD LATERAL T0806 505 X 60 X 22MM DIREITO - CADEIRA DUCHAMP",
    "equipamentos": [
      2
    ],
    "tempo": 24,
    "setup": 3600,
    "codigo_barra": 69595
  },
  {
    "id_erp": 69596,
    "nome": "TRAVESSA MAD LATERAL T0807 505 X 60 X 22MM ESQUERDO - CADEIRA DUCHAMP",
    "equipamentos": [
      2
    ],
    "tempo": 24,
    "setup": 0,
    "codigo_barra": 69596
  },
  {
    "id_erp": 69599,
    "nome": "ASSENTO MAD A0547 470 X 45 X 32MM MONTADO - CADEIRA DUCHAMP - 2º ETAPA",
    "equipamentos": [
      1
    ],
    "tempo": 113,
    "setup": 3600,
    "codigo_barra": 69599
  },
  {
    "id_erp": 69606,
    "nome": "TRAVESSA MAD T0806 332 X 45 X 32MM ASSENTO - CADEIRA DUCHAMP",
    "equipamentos": [
      1
    ],
    "tempo": 11,
    "setup": 3600,
    "codigo_barra": 69606
  },
  {
    "id_erp": 69650,
    "nome": "ENCOSTO PRENSADO LAM E0381 470 X 140 X 4,2MM - CADEIRA ADHARA",
    "equipamentos": [
      1
    ],
    "tempo": 78,
    "setup": 2100,
    "codigo_barra": 69650
  },
  {
    "id_erp": 69695,
    "nome": "ENCOSTO PRENSADO TAPECADO - CADEIRA ADHARA",
    "equipamentos": [
      1
    ],
    "tempo": 105,
    "setup": 2100,
    "codigo_barra": 69695
  },
  {
    "id_erp": 69788,
    "nome": "BRACO MONTADO MAD T0198 - CADEIRA DUCHAMP - 2º ETAPA",
    "equipamentos": [
      1
    ],
    "tempo": 90,
    "setup": 3600,
    "codigo_barra": 69788
  },
  {
    "id_erp": 69791,
    "nome": "TRAVESSA MAD T0806 205 X 28 X 28MM INFERIOR - CADEIRA DUCHAMP",
    "equipamentos": [
      1
    ],
    "tempo": 68,
    "setup": 3600,
    "codigo_barra": 69791
  },
  {
    "id_erp": 70203,
    "nome": "TRAVESSA MAD LATERAL T088 195 X 32 X 32MM ENCOSTO DIREITO - POLTRONA DELTA / POLTRONA DELTA TAP",
    "equipamentos": [
      1
    ],
    "tempo": 14,
    "setup": 0,
    "codigo_barra": 70203
  },
  {
    "id_erp": 70205,
    "nome": "TRAVESSA MAD LATERAL T0089 195 X 32 X 32MM ENCOSTO ESQ - POLTRONA DELTA / POLTRONA DELTA TAP",
    "equipamentos": [
      1
    ],
    "tempo": 14,
    "setup": 3000,
    "codigo_barra": 70205
  },
  {
    "id_erp": 70446,
    "nome": "TRAVESSA MDF T0811 475 X 50 X 40MM ENCOSTO (FRONTAL) - CADEIRA KRAFT EUCALIPTO",
    "equipamentos": [
      1
    ],
    "tempo": 40,
    "setup": 2100,
    "codigo_barra": 70446
  },
  {
    "id_erp": 71074,
    "nome": "ENCOSTO PRENSADO TAP E0385 450 X 120 X 16MM - CADEIRA/BANQUETA  PANTALONA",
    "equipamentos": [
      1
    ],
    "tempo": 60,
    "setup": 2100,
    "codigo_barra": 71074
  },
  {
    "id_erp": 71081,
    "nome": "TRAVESSA MAD LATERAL T0806 382 X 65 X 22MM DIREITA - CADEIRA PANTALONA / BANQUETA PANTALONA",
    "equipamentos": [
      1
    ],
    "tempo": 19,
    "setup": 2100,
    "codigo_barra": 71081
  },
  {
    "id_erp": 71083,
    "nome": "TRAVESSA MAD LATERAL T0807 382 X 65 X 22MM ESQUERDA - CADEIRA PANTALONA / BANQUETA PANTALONA",
    "equipamentos": [
      1
    ],
    "tempo": 19,
    "setup": 0,
    "codigo_barra": 71083
  },
  {
    "id_erp": 71085,
    "nome": "TRAVESSA MAD T0808 303 X 65 X 22MM FRENTE - CADEIRA PANTALONA / BANQUETA PANTALONA",
    "equipamentos": [
      1
    ],
    "tempo": 19,
    "setup": 0,
    "codigo_barra": 71085
  },
  {
    "id_erp": 71087,
    "nome": "TRAVESSA MAD LATERAL T0809 176 X 65 X 22MM DIREITA - CADEIRA PANTALONA / BANQUETA PANTALONA",
    "equipamentos": [
      1
    ],
    "tempo": 19,
    "setup": 0,
    "codigo_barra": 71087
  },
  {
    "id_erp": 71323,
    "nome": "ASSENTO PRENSADO TAP A0551 470 X 470 X 49MM - CADEIRA PANTALONA - 2º ETAPA (USINAR MONTADO)",
    "equipamentos": [
      1
    ],
    "tempo": 87,
    "setup": 2100,
    "codigo_barra": 71323
  },
  {
    "id_erp": 71324,
    "nome": "TRAVESSA MDF T0119 340 X 45 X 40MM ASSENTO - CADEIRA PANTALONA - 1º ETAPA (USINAR TRAV. ASSENTO)",
    "equipamentos": [
      1
    ],
    "tempo": 13,
    "setup": 2100,
    "codigo_barra": 71324
  },
  {
    "id_erp": 71383,
    "nome": "TRAVESSA MAD T0812 475 X 50 X 40MM ENCOSTO (FRONTAL) - CADEIRA KRAFT TAUARI",
    "equipamentos": [
      1
    ],
    "tempo": 40,
    "setup": 2100,
    "codigo_barra": 71383
  },
  {
    "id_erp": 71387,
    "nome": "ASSENTO MAD T0820 395 X 430 X 30MM - CADEIRA KRAFT TAUARI",
    "equipamentos": [
      1
    ],
    "tempo": 242,
    "setup": 2100,
    "codigo_barra": 71387
  },
  {
    "id_erp": 71465,
    "nome": "PE MAD TRASEIRO P0655 820 X 50 X 32MM DIREITO - BANQUETA STEIN 827",
    "equipamentos": [
      3
    ],
    "tempo": 19,
    "setup": 4800,
    "codigo_barra": 71465
  },
  {
    "id_erp": 71466,
    "nome": "PE MAD TRASEIRO P0657 820 X 50 X 32MM ESQUERDO - BANQUETA STEIN 827",
    "equipamentos": [
      3
    ],
    "tempo": 19,
    "setup": 0,
    "codigo_barra": 71466
  },
  {
    "id_erp": 71477,
    "nome": "ENCOSTO MAD T0922 445 X 140 X 55MM MAIOR - BANQUETA STEIN",
    "equipamentos": [
      1
    ],
    "tempo": 132,
    "setup": 3600,
    "codigo_barra": 71477
  },
  {
    "id_erp": 71478,
    "nome": "ENCOSTO MAD T0923 123 X 140 X 55MM MENOR - BANQUETA STEIN",
    "equipamentos": [
      1
    ],
    "tempo": 270,
    "setup": 3600,
    "codigo_barra": 71478
  },
  {
    "id_erp": 71574,
    "nome": "PE MAD TRASEIRO P0658 720 X 50 X 32MM DIREITO - BANQUETA STEIN 727",
    "equipamentos": [
      3
    ],
    "tempo": 19,
    "setup": 4800,
    "codigo_barra": 71574
  },
  {
    "id_erp": 71576,
    "nome": "PE MAD TRASEIRO P0659 720 X 50 X 32MM ESQUERDO - BANQUETA STEIN 727",
    "equipamentos": [
      3
    ],
    "tempo": 19,
    "setup": 0,
    "codigo_barra": 71576
  },
  {
    "id_erp": 71662,
    "nome": "TRAVESSA MAD T0926 1055 X 45 X 30MM EXTERNA TAMPO - APARADOR URBI 1,20 (1055 X 45 X 30MM)",
    "equipamentos": [
      3
    ],
    "tempo": 16,
    "setup": 3000,
    "codigo_barra": 71662
  },
  {
    "id_erp": 71734,
    "nome": "TRAVESSA MAD LATERAL T0807 404 X 73 X 22MM DIR - BANQUETA BAIA",
    "equipamentos": [
      1
    ],
    "tempo": 24,
    "setup": 2100,
    "codigo_barra": 71734
  },
  {
    "id_erp": 71736,
    "nome": "TRAVESSA MAD LATERAL T0808 404 X 73 X 22MM ESQ - BANQUETA BAIA",
    "equipamentos": [
      1
    ],
    "tempo": 24,
    "setup": 0,
    "codigo_barra": 71736
  },
  {
    "id_erp": 71785,
    "nome": "TRAVESSA MAD LATERAL T0809 176 X 65 X 22MM ESQUERDA - CADEIRA PANTALONA / BANQUETA PANTALONA",
    "equipamentos": [
      1
    ],
    "tempo": 19,
    "setup": 0,
    "codigo_barra": 71785
  },
  {
    "id_erp": 71932,
    "nome": "PE MAD TRASEIRO T0745 741 X 41 X 32MM DIREITO - CADEIRA ANGA",
    "equipamentos": [
      3
    ],
    "tempo": 43,
    "setup": 4200,
    "codigo_barra": 71932
  },
  {
    "id_erp": 71934,
    "nome": "PE MAD TRASEIRO T0746 741 X 41 X 32MM ESQUERDO - CADEIRA ANGA",
    "equipamentos": [
      3
    ],
    "tempo": 43,
    "setup": 0,
    "codigo_barra": 71934
  },
  {
    "id_erp": 71935,
    "nome": "PE MAD DIANTEIRO T0747 445 X 51 X 32MM DIREITO - CADEIRA ANGA",
    "equipamentos": [
      1
    ],
    "tempo": 14,
    "setup": 2100,
    "codigo_barra": 71935
  },
  {
    "id_erp": 71937,
    "nome": "PE MAD DIANTEIRO T4148 445 X 51 X 32MM ESQUERDO - CADEIRA ANGA",
    "equipamentos": [
      1
    ],
    "tempo": 14,
    "setup": 0,
    "codigo_barra": 71937
  },
  {
    "id_erp": 71938,
    "nome": "TRAVESSA MAD LATERAL T0749 426 X 80 X 32MM DIREITO - CADEIRA ANGA",
    "equipamentos": [
      1
    ],
    "tempo": 50,
    "setup": 5400,
    "codigo_barra": 71938
  },
  {
    "id_erp": 71940,
    "nome": "TRAVESSA MAD LATERAL T0750 426 X 80 X 32MM ESQUERDO - CADEIRA ANGA",
    "equipamentos": [
      1
    ],
    "tempo": 50,
    "setup": 0,
    "codigo_barra": 71940
  },
  {
    "id_erp": 71941,
    "nome": "TRAVESSA MAD DIANTEIRA T0751 380 X 70 X 32MM FRENTE - CADEIRA ANGA",
    "equipamentos": [
      1
    ],
    "tempo": 47,
    "setup": 4800,
    "codigo_barra": 71941
  },
  {
    "id_erp": 72445,
    "nome": "PE MAD XA67187 123 X 75 X 45MM SUPORTE - BANCO CURUPIRA",
    "equipamentos": [
      1
    ],
    "tempo": 30,
    "setup": 2100,
    "codigo_barra": 72445
  },
  {
    "id_erp": 72472,
    "nome": "TRAVESSA MAD 6U91S85 440 X 75 X 45MM MENOR ASSENTO - BANCO BARU",
    "equipamentos": [
      2
    ],
    "tempo": 27,
    "setup": 2100,
    "codigo_barra": 72472
  },
  {
    "id_erp": 72474,
    "nome": "TRAVESSA MAD 6787NG7 1570 X 75 X 45MM MAIOR ASSENTO - BANCO BARU 1,60",
    "equipamentos": [
      2
    ],
    "tempo": 25,
    "setup": 2100,
    "codigo_barra": 72474
  },
  {
    "id_erp": 72489,
    "nome": "TRAVESSA MAD TW41774 1770 X 75 X 45MM MAIOR ASSENTO - BANCO BARU 1,80",
    "equipamentos": [
      2
    ],
    "tempo": 25,
    "setup": 2100,
    "codigo_barra": 72489
  },
  {
    "id_erp": 72509,
    "nome": "TRAVESSA MAD K8Y9121 1970 X 75 X 45MM MAIOR ASSENTO - BANCO BARU 2,00",
    "equipamentos": [
      2
    ],
    "tempo": 25,
    "setup": 2100,
    "codigo_barra": 72509
  },
  {
    "id_erp": 72677,
    "nome": "LATERAL MONTADA MAD 8MT7123 DIREITO - BANQUETA VILAR TAPECADA 990 - 2º ETAPA",
    "equipamentos": [
      1
    ],
    "tempo": 81,
    "setup": 3600,
    "codigo_barra": 72677
  },
  {
    "id_erp": 72678,
    "nome": "LATERAL MONTADA MAD FB71687 ESQUERDO - BANQUETA VILAR TAPECADA 990 - 2º ETAPA",
    "equipamentos": [
      1
    ],
    "tempo": 81,
    "setup": 0,
    "codigo_barra": 72678
  },
  {
    "id_erp": 72679,
    "nome": "PE MAD TRASEIRO TO64534 980 X 35 X 32MM DIREITO - BANQUETA VILAR 990",
    "equipamentos": [
      1
    ],
    "tempo": 70,
    "setup": 3600,
    "codigo_barra": 72679
  },
  {
    "id_erp": 72781,
    "nome": "PE MAD DIANTEIRO 9246DQ6 680 X 35 X 32MM DIREITO - BANQUETA VILAR 990",
    "equipamentos": [
      1
    ],
    "tempo": 20,
    "setup": 4200,
    "codigo_barra": 72781
  },
  {
    "id_erp": 72785,
    "nome": "TRAVESSA MAD LATERAL 955O897 409 X 60 X 32MM DIREITO - BANQUETA VILAR",
    "equipamentos": [
      1
    ],
    "tempo": 37,
    "setup": 2100,
    "codigo_barra": 72785
  },
  {
    "id_erp": 72787,
    "nome": "PE MAD TRASEIRO X46A593 980 X 35 X 32MM ESQUERDO - BANQUETA VILAR 990",
    "equipamentos": [
      1
    ],
    "tempo": 79,
    "setup": 3600,
    "codigo_barra": 72787
  },
  {
    "id_erp": 72788,
    "nome": "PE MAD DIANTEIRO 3D1E724 680 X 35 X 32MM ESQUERDO - BANQUETA VILAR 990",
    "equipamentos": [
      1
    ],
    "tempo": 20,
    "setup": 2100,
    "codigo_barra": 72788
  },
  {
    "id_erp": 72789,
    "nome": "TRAVESSA MAD LATERAL H29A912 409 X 60 X 32MM ESQUERDO - BANQUETA VILAR",
    "equipamentos": [
      1
    ],
    "tempo": 37,
    "setup": 2100,
    "codigo_barra": 72789
  },
  {
    "id_erp": 72790,
    "nome": "TRAVESSA MAD DIANTEIRA RP64248 425 X 68 X 22MM - BANQUETA VILAR",
    "equipamentos": [
      1
    ],
    "tempo": 31,
    "setup": 3600,
    "codigo_barra": 72790
  },
  {
    "id_erp": 72792,
    "nome": "TRAVESSA MAD TRASEIRA BN45231 425 X 60 X 22MM - BANQUETA VILAR",
    "equipamentos": [
      1
    ],
    "tempo": 31,
    "setup": 0,
    "codigo_barra": 72792
  },
  {
    "id_erp": 72821,
    "nome": "TRAVESSA MAD 353TJ78 425 X 72 X 25MM TRASEIRA ASSENTO - BANQUETA VILAR RATAN",
    "equipamentos": [
      1
    ],
    "tempo": 16,
    "setup": 0,
    "codigo_barra": 72821
  },
  {
    "id_erp": 72825,
    "nome": "TRAVESSA MAD LATERAL W15H554 465 X 80 X 32MM INFERIOR - BANQUETA VILAR",
    "equipamentos": [
      1
    ],
    "tempo": 40,
    "setup": 3600,
    "codigo_barra": 72825
  },
  {
    "id_erp": 72832,
    "nome": "TRAVESSA MAD DIANTEIRA K1M8617 440 X 70 X 25MM ASSENTO - BANQUETA VILAR RATAN",
    "equipamentos": [
      1
    ],
    "tempo": 16,
    "setup": 2100,
    "codigo_barra": 72832
  },
  {
    "id_erp": 72833,
    "nome": "ASSENTO MONTADO MAD 6JU2696 - BANQUETA VILAR RATAN",
    "equipamentos": [
      1
    ],
    "tempo": 270,
    "setup": 2100,
    "codigo_barra": 72833
  },
  {
    "id_erp": 73482,
    "nome": "LATERAL MONTADA MAD 1K9R411 DIREITO - BANQUETA VILAR 890 - 2º ETAPA",
    "equipamentos": [
      1
    ],
    "tempo": 81,
    "setup": 3600,
    "codigo_barra": 73482
  },
  {
    "id_erp": 73483,
    "nome": "LATERAL MONTADA MAD 15Q7G72 ESQUERDO - BANQUETA VILAR 890  - 2º ETAPA",
    "equipamentos": [
      1
    ],
    "tempo": 81,
    "setup": 0,
    "codigo_barra": 73483
  },
  {
    "id_erp": 73484,
    "nome": "PE MAD TRASEIRO TO64534 880 X 35 X 32MM DIREITO - BANQUETA VILAR 890",
    "equipamentos": [
      1
    ],
    "tempo": 120,
    "setup": 3000,
    "codigo_barra": 73484
  },
  {
    "id_erp": 73486,
    "nome": "PE MAD DIANTEIRO 9246DQ6 580 X 35 X 32MM DIREITO - BANQUETA VILAR 890",
    "equipamentos": [
      1
    ],
    "tempo": 20,
    "setup": 0,
    "codigo_barra": 73486
  },
  {
    "id_erp": 73488,
    "nome": "PE MAD TRASEIRO X46A593 880 X 35 X 32MM ESQUERDO - BANQUETA VILAR 890",
    "equipamentos": [
      1
    ],
    "tempo": 135,
    "setup": 3000,
    "codigo_barra": 73488
  },
  {
    "id_erp": 73489,
    "nome": "PE MAD DIANTEIRO 3D1E724 580 X 35 X 32MM ESQUERDO - BANQUETA VILAR 890",
    "equipamentos": [
      1
    ],
    "tempo": 20,
    "setup": 4200,
    "codigo_barra": 73489
  },
  {
    "id_erp": 73519,
    "nome": "TRAVESSA MAD 6CV9438 1370 X 85 X 45MM MAIOR ASSENTO - BANCO BARU 1,40",
    "equipamentos": [
      2
    ],
    "tempo": 25,
    "setup": 2100,
    "codigo_barra": 73519
  },
  {
    "id_erp": 73710,
    "nome": "PE MAD OK97917 660 X 50 X 45MM - ESTOFADO NIMBUS/ZAFIR - PE MENOR",
    "equipamentos": [
      2
    ],
    "tempo": 111,
    "setup": 4500,
    "codigo_barra": 73710
  },
  {
    "id_erp": 73711,
    "nome": "PE MAD O4L6988 1050 X 50 X 45MM - ESTOFADO NIMBUS/ZAFIR - PE MAIOR",
    "equipamentos": [
      2
    ],
    "tempo": 137,
    "setup": 4500,
    "codigo_barra": 73711
  },
  {
    "id_erp": 73874,
    "nome": "TRAVESSA MAD 1871BB6 572 X 45 X 32MM BORDA - MESA CENTRO GOYA 600 QUADRADA",
    "equipamentos": [
      2
    ],
    "tempo": 15,
    "setup": 2100,
    "codigo_barra": 73874
  },
  {
    "id_erp": 73876,
    "nome": "TRAVESSA MAD 817299S 612 X 40 X 32MM LATERAL - MESA LATERAL GOYA 700 X 400 ORGANICA",
    "equipamentos": [
      2
    ],
    "tempo": 15,
    "setup": 2100,
    "codigo_barra": 73876
  },
  {
    "id_erp": 73877,
    "nome": "TRAVESSA MAD QQ31688 380 X 40 X 32MM CURVA MAIOR - MESA LATERAL GOYA  700 X 400 ORGANICA",
    "equipamentos": [
      2
    ],
    "tempo": 15,
    "setup": 2100,
    "codigo_barra": 73877
  },
  {
    "id_erp": 73878,
    "nome": "TRAVESSA MAD 6828R38 300 X 40 X 32MM CURVA MENOR - MESA LATERAL GOYA 700 X 400 ORGANICA",
    "equipamentos": [
      2
    ],
    "tempo": 15,
    "setup": 2100,
    "codigo_barra": 73878
  },
  {
    "id_erp": 73880,
    "nome": "TRAVESSA MAD 97158T2 772 X 50 X 32MM BORDA - MESA CENTRO GOYA 800 QUADRADA",
    "equipamentos": [
      2
    ],
    "tempo": 15,
    "setup": 2100,
    "codigo_barra": 73880
  },
  {
    "id_erp": 73885,
    "nome": "TRAVESSA MAD 7448ZI5 1372 X 50 X 32MM MAIOR BORDA - MESA CENTRO GOYA 1400 X 800",
    "equipamentos": [
      2
    ],
    "tempo": 15,
    "setup": 2100,
    "codigo_barra": 73885
  },
  {
    "id_erp": 74913,
    "nome": "TRAVESSA MAD DI83972 411 X 33 X 26MM INF ENC - BANQUETA VILAR TAPECADA",
    "equipamentos": [
      2
    ],
    "tempo": 30,
    "setup": 4800,
    "codigo_barra": 74913
  },
  {
    "id_erp": 74914,
    "nome": "TRAVESSA MAD 5TG8179 411 X 33 X 26MM INF ENC - BANQUETA VILAR RATAN",
    "equipamentos": [
      2
    ],
    "tempo": 70,
    "setup": 4800,
    "codigo_barra": 74914
  },
  {
    "id_erp": 76297,
    "nome": "PE MAD TRASEIRO 5217R8S 780 X 86 X 32MM DIREITO - BANQUETA ADHARA 970",
    "equipamentos": [
      3
    ],
    "tempo": 28,
    "setup": 2100,
    "codigo_barra": 76297
  },
  {
    "id_erp": 76299,
    "nome": "PE MAD TRASEIRO OK45459 780 X 86 X 32MM ESQUERDO - BANQUETA ADHARA 970",
    "equipamentos": [
      3
    ],
    "tempo": 28,
    "setup": 0,
    "codigo_barra": 76299
  },
  {
    "id_erp": 76303,
    "nome": "TRAVESSA MAD LATERAL 2M18V81 310 X 68 X 22MM DIREITO - BANQUETA ADHARA 870 / BANQUETA ADHARA 970",
    "equipamentos": [
      1
    ],
    "tempo": 27,
    "setup": 2100,
    "codigo_barra": 76303
  },
  {
    "id_erp": 76305,
    "nome": "TRAVESSA MAD LATERAL 25JY213 310 X 68 X 22MM ESQUERDO - BANQUETA ADHARA 870 / BANQUETA ADHARA 970",
    "equipamentos": [
      1
    ],
    "tempo": 27,
    "setup": 0,
    "codigo_barra": 76305
  },
  {
    "id_erp": 76306,
    "nome": "TRAVESSA MAD D8L2116 460 X 80 X 32MM FRENTE BASE - BANQUETA ADHARA 870 / BANQUETA ADHARA 970",
    "equipamentos": [
      2
    ],
    "tempo": 82,
    "setup": 4800,
    "codigo_barra": 76306
  },
  {
    "id_erp": 76325,
    "nome": "PE MAD TRASEIRO 667NY17 680 X 86 X 32MM DIREITO - BANQUETA ADHARA 870",
    "equipamentos": [
      3
    ],
    "tempo": 28,
    "setup": 5100,
    "codigo_barra": 76325
  },
  {
    "id_erp": 76327,
    "nome": "PE MAD TRASEIRO IK77859 680 X 86 X 32MM ESQUERDO - BANQUETA ADHARA 870",
    "equipamentos": [
      3
    ],
    "tempo": 28,
    "setup": 0,
    "codigo_barra": 76327
  },
  {
    "id_erp": 77013,
    "nome": "TRAVESSA MAD LATERAL 7ZM7773 460 X 100 X 22MM DIREITA - POLTRONA PANTALONA",
    "equipamentos": [
      1
    ],
    "tempo": 32,
    "setup": 900,
    "codigo_barra": 77013
  },
  {
    "id_erp": 77016,
    "nome": "TRAVESSA MAD LATERAL V3C9772 460 X 100 X 22MM ESQUERDA - POLTRONA PANTALONA",
    "equipamentos": [
      1
    ],
    "tempo": 32,
    "setup": 900,
    "codigo_barra": 77016
  },
  {
    "id_erp": 77017,
    "nome": "TRAVESSA MAD DIANTEIRA 3MA3231 445 X 100 X 22MM - POLTRONA PANTALONA",
    "equipamentos": [
      1
    ],
    "tempo": 32,
    "setup": 900,
    "codigo_barra": 77017
  },
  {
    "id_erp": 77022,
    "nome": "TRAVESSA MAD LATERAL 9R7397V 232 X 100 X 22MM FRENTE - POLTRONA PANTALONA",
    "equipamentos": [
      1
    ],
    "tempo": 32,
    "setup": 900,
    "codigo_barra": 77022
  },
  {
    "id_erp": 77028,
    "nome": "TRAVESSA MAD TRASEIRA 999AL21 397 X 100 X 22MM - POLTRONA PANTALONA",
    "equipamentos": [
      1
    ],
    "tempo": 32,
    "setup": 900,
    "codigo_barra": 77028
  },
  {
    "id_erp": 77030,
    "nome": "ENCOSTO PRENSADO TAP 113CL57 632 X 200 X 16MM - POLTRONA PANTALONA",
    "equipamentos": [
      1
    ],
    "tempo": 54,
    "setup": 2100,
    "codigo_barra": 77030
  },
  {
    "id_erp": 77033,
    "nome": "ASSENTO PRENSADO TAP J37466B 590 X 590 X 69MM - POLTRONA PANTALONA",
    "equipamentos": [
      1
    ],
    "tempo": 300,
    "setup": 2400,
    "codigo_barra": 77033
  },
  {
    "id_erp": 77803,
    "nome": "TRAVESSA MAD OX95146 677 X 65 X 22MM SUPERIOR - MESA CENTRO PANTALONA 600",
    "equipamentos": [
      2
    ],
    "tempo": 64,
    "setup": 4200,
    "codigo_barra": 77803
  },
  {
    "id_erp": 77810,
    "nome": "TRAVESSA MAD 5I33191 877 X 65 X 22MM SUPERIOR- MESA CENTRO PANTALONA 800",
    "equipamentos": [
      2
    ],
    "tempo": 64,
    "setup": 4200,
    "codigo_barra": 77810
  },
  {
    "id_erp": 78651,
    "nome": "TRAVESSA MAD 9V8H572 525 X 65 X 22MM SUPERIOR - BANCO PANTALONA",
    "equipamentos": [
      2
    ],
    "tempo": 41,
    "setup": 0,
    "codigo_barra": 78651
  },
  {
    "id_erp": 78653,
    "nome": "TRAVESSA MAD 6IC1985 525 X 65 X 22MM INFERIOR - BANCO PANTALONA",
    "equipamentos": [
      2
    ],
    "tempo": 41,
    "setup": 4800,
    "codigo_barra": 78653
  },
  {
    "id_erp": 78654,
    "nome": "ASSENTO PRENSADO TAP OC79941 450 X 450 X 49MM - BANCO PANTALONA - 2º ETAPA (USINAR MONTADO)",
    "equipamentos": [
      1
    ],
    "tempo": 180,
    "setup": 2100,
    "codigo_barra": 78654
  },
  {
    "id_erp": 78657,
    "nome": "TRAVESSA MDF 68QL145 340 X 45 X 40MM - BANCO PANTALONA - 1º ETAPA (USINAR TRAV. ASSENTO)",
    "equipamentos": [
      1
    ],
    "tempo": 48,
    "setup": 3600,
    "codigo_barra": 78657
  },
  {
    "id_erp": 79206,
    "nome": "PE MAD TRASEIRO 99M7T77 760 X 40 X 32MM DIREITO - CADEIRA PINDORAMA",
    "equipamentos": [
      3
    ],
    "tempo": 17,
    "setup": 5400,
    "codigo_barra": 79206
  },
  {
    "id_erp": 79208,
    "nome": "PE MAD TRASEIRO D368I75 760 X 40 X 32MM ESQUERDO - CADEIRA PINDORAMA",
    "equipamentos": [
      3
    ],
    "tempo": 17,
    "setup": 0,
    "codigo_barra": 79208
  },
  {
    "id_erp": 79209,
    "nome": "PE MAD DIANTEIRO A943W55 435 X 40 X 32MM DIREITO - CADEIRA PINDORAMA",
    "equipamentos": [
      3
    ],
    "tempo": 12,
    "setup": 3600,
    "codigo_barra": 79209
  },
  {
    "id_erp": 79211,
    "nome": "PE MAD DIANTEIRO 775P26B 435 X 40 X 32MM ESQUERDO - CADEIRA PINDORAMA",
    "equipamentos": [
      3
    ],
    "tempo": 12,
    "setup": 0,
    "codigo_barra": 79211
  },
  {
    "id_erp": 79218,
    "nome": "TRAVESSA MAD DIANTEIRA 5P9S893 385 X 55 X 22MM - CADEIRA PINDORAMA",
    "equipamentos": [
      2
    ],
    "tempo": "-",
    "setup": 0,
    "codigo_barra": 79218
  },
  {
    "id_erp": 79218,
    "nome": "TRAVESSA MAD DIANTEIRA 5P9S893 385 X 55 X 22MM - CADEIRA PINDORAMA",
    "equipamentos": [
      1
    ],
    "tempo": "-",
    "setup": 0,
    "codigo_barra": 79218
  },
  {
    "id_erp": 79220,
    "nome": "TRAVESSA MAD TRASEIRA 286KI55 435 X 80 X 32MM - CADEIRA PINDORAMA",
    "equipamentos": [
      2
    ],
    "tempo": 40,
    "setup": 3600,
    "codigo_barra": 79220
  },
  {
    "id_erp": 79220,
    "nome": "TRAVESSA MAD TRASEIRA 286KI55 435 X 80 X 32MM - CADEIRA PINDORAMA",
    "equipamentos": [
      1
    ],
    "tempo": 40,
    "setup": 3600,
    "codigo_barra": 79220
  },
  {
    "id_erp": 79440,
    "nome": "PE MAD TRASEIRO 4N5G992 450 X 65 X 42MM - CADEIRA CORA",
    "equipamentos": [
      3
    ],
    "tempo": 34,
    "setup": 4800,
    "codigo_barra": 79440
  },
  {
    "id_erp": 79441,
    "nome": "TRAVESSA MAD S2757S6 155 X 45 X 42MM COMPL PE TRASEIRO - CADEIRA CORA",
    "equipamentos": [
      1
    ],
    "tempo": 53,
    "setup": 3600,
    "codigo_barra": 79441
  },
  {
    "id_erp": 79447,
    "nome": "ENCOSTO PRENSSADO TAP 3WW4111 550 X 400 X 16MM - CADEIRA CORA",
    "equipamentos": [
      1
    ],
    "tempo": 76,
    "setup": 5400,
    "codigo_barra": 79447
  },
  {
    "id_erp": 79593,
    "nome": "PE MAD DIANTEIRO 132237P 628 X 50 X 23MM DIREITO - CADEIRA ANGA C/ BRACO",
    "equipamentos": [
      3
    ],
    "tempo": 40,
    "setup": 0,
    "codigo_barra": 79593
  },
  {
    "id_erp": 79595,
    "nome": "PE MAD DIANTEIRO 056L837 628 X 50 X 32MM ESQUERDO - CADEIRA ANGA C/ BRACO",
    "equipamentos": [
      3
    ],
    "tempo": 40,
    "setup": 5400,
    "codigo_barra": 79595
  },
  {
    "id_erp": 79596,
    "nome": "PE MAD TRASEIRO HN63793 741 X 41 X 32MM DIREITO - CADEIRA ANGA C/ BRACO",
    "equipamentos": [
      3
    ],
    "tempo": 40,
    "setup": 0,
    "codigo_barra": 79596
  },
  {
    "id_erp": 79598,
    "nome": "PE MAD TRASEIRO 72392EN 741 X 41 X 32MM ESQUERDO - CADEIRA ANGA C/ BRACO",
    "equipamentos": [
      3
    ],
    "tempo": 40,
    "setup": 6000,
    "codigo_barra": 79598
  },
  {
    "id_erp": 79599,
    "nome": "TRAVESSA MAD DIANTEIRA O3U3147 527 X 87 X 32MM - CADEIRA ANGA C/ BRACO",
    "equipamentos": [
      2
    ],
    "tempo": 54,
    "setup": 4200,
    "codigo_barra": 79599
  },
  {
    "id_erp": 79603,
    "nome": "TRAVESSA MAD BRACO JJ65556 178 X 45 X 32MM APOIO DIREITO - CADEIRA ANGA C/ BRACO",
    "equipamentos": [
      1
    ],
    "tempo": 85,
    "setup": 0,
    "codigo_barra": 79603
  },
  {
    "id_erp": 79605,
    "nome": "TRAVESSA MAD BRACO I652587 178 X 45 X 32MM APOIO ESQUERDO - CADEIRA ANGA C/ BRACO",
    "equipamentos": [
      1
    ],
    "tempo": 85,
    "setup": 2100,
    "codigo_barra": 79605
  },
  {
    "id_erp": 79606,
    "nome": "TRAVESSA MAD LATERAL ZO18996 457 X 80 X 32MM DIREITO - CADEIRA ANGA C/ BRACO",
    "equipamentos": [
      1
    ],
    "tempo": 58,
    "setup": 4800,
    "codigo_barra": 79606
  },
  {
    "id_erp": 79608,
    "nome": "TRAVESSA MAD LATERAL 331ZU94 457 X 80 X 32MM ESQUERDO - CADEIRA ANGA C/ BRACO",
    "equipamentos": [
      1
    ],
    "tempo": 58,
    "setup": 0,
    "codigo_barra": 79608
  },
  {
    "id_erp": 79661,
    "nome": "TRAVESSA MAD LATERAL 7NQ9853 232 X 100 X 22MM FRENTE ESQ - POLTRONA PANTALONA",
    "equipamentos": [
      1
    ],
    "tempo": 32,
    "setup": 900,
    "codigo_barra": 79661
  },
  {
    "id_erp": 79854,
    "nome": "MONTADO LATERAL 5B18V26 DIREITO -  POLTRONA MALBEC 2.0 2º ETAPA",
    "equipamentos": [
      1
    ],
    "tempo": 82,
    "setup": 2700,
    "codigo_barra": 79854
  },
  {
    "id_erp": 79941,
    "nome": "MONTADO LATERAL 62UY429 ESQUERDO -  POLTRONA MALBEC 2.0 2º ETAPA",
    "equipamentos": [
      1
    ],
    "tempo": 82,
    "setup": 0,
    "codigo_barra": 79941
  },
  {
    "id_erp": 80038,
    "nome": "TRAVESSA MAD SUPERIOR 79Q87M8 340 X 102 X 55MM BRACO DIREITO - POLTRONA ICARO",
    "equipamentos": [
      1
    ],
    "tempo": 2.948,
    "setup": 5700,
    "codigo_barra": 80038
  },
  {
    "id_erp": 80045,
    "nome": "TRAVESSA MAD INFERIOR H54F791 131 X 55 X 75MM BRACO DIREITO - POLTRONA ICARO",
    "equipamentos": [
      1
    ],
    "tempo": "-",
    "setup": 0,
    "codigo_barra": 80045
  },
  {
    "id_erp": 80057,
    "nome": "TRAVESSA MAD LATERAL OU91651 280 X 170 X 22MM DIREITO - POLTRONA ICARO",
    "equipamentos": [
      1
    ],
    "tempo": 84,
    "setup": 2400,
    "codigo_barra": 80057
  },
  {
    "id_erp": 80060,
    "nome": "TRAVESSA MAD LATERAL 9HI2172 280 X 170 X 22MM ESQUERDO - POLTRONA ICARO",
    "equipamentos": [
      1
    ],
    "tempo": "-",
    "setup": 0,
    "codigo_barra": 80060
  },
  {
    "id_erp": 80118,
    "nome": "ENCOSTO PRENSADO V5X1993 475 X 160 X 20MM - BAIA ENCOSTO MADEIRA",
    "equipamentos": [
      1
    ],
    "tempo": 157,
    "setup": 3000,
    "codigo_barra": 80118
  },
  {
    "id_erp": 80320,
    "nome": "ENCOSTO PRENSADO 655VV83 475 X 160 X 20MM - PANTALONA ENCOSTO MADEIRA CADEIRA/BANQUETA",
    "equipamentos": [
      1
    ],
    "tempo": 39,
    "setup": 2100,
    "codigo_barra": 80320
  },
  {
    "id_erp": 80350,
    "nome": "ASSENTO MAD 06138W5 450 X 42 X 32MM FRENTE - CADEIRA RIO RATAN",
    "equipamentos": [
      2
    ],
    "tempo": 30,
    "setup": 3600,
    "codigo_barra": 80350
  },
  {
    "id_erp": 80355,
    "nome": "LATERAL MAD 75EP756 226 X 42 X 32 MM ASSENTO - CADEIRA RIO RATAN",
    "equipamentos": [
      2
    ],
    "tempo": 35,
    "setup": 3600,
    "codigo_barra": 80355
  },
  {
    "id_erp": 80357,
    "nome": "CURVA MAD SN35857 315 X 96 X 32MM ASSENTO - CADEIRA RIO RATAN",
    "equipamentos": [
      1
    ],
    "tempo": 62,
    "setup": 2400,
    "codigo_barra": 80357
  },
  {
    "id_erp": 80398,
    "nome": "TRAVESSA MAD SUPERIOR X78E373 340 X 102 X 55M BRACO ESQUERDO - POLTRONA ICARO",
    "equipamentos": [
      1
    ],
    "tempo": "-",
    "setup": 0,
    "codigo_barra": 80398
  },
  {
    "id_erp": 80399,
    "nome": "TRAVESSA MAD INFERIOR 53W94B8 131 X 55 X 75MM BRACO ESQUERDO - POLTRONA ICARO",
    "equipamentos": [
      1
    ],
    "tempo": "-",
    "setup": 0,
    "codigo_barra": 80399
  },
  {
    "id_erp": 80602,
    "nome": "DETALHE MADEIRA FA41849 355 X 90 X 32MM PE - POLTRONA MALBEC 2.0",
    "equipamentos": [
      2
    ],
    "tempo": 33,
    "setup": 3600,
    "codigo_barra": 80602
  },
  {
    "id_erp": 80604,
    "nome": "TRAVESSA MAD BRACO T8Z7747 440 X 80 X 54MM DIREITO -  POLTRONA/CADEIRA MALBEC 2.0",
    "equipamentos": [
      1
    ],
    "tempo": 155,
    "setup": 0,
    "codigo_barra": 80604
  },
  {
    "id_erp": 80606,
    "nome": "TRAVESSA MAD BRACO 1MP8557 440 X 80 X 54MM ESQUERDO - POLTRONA/CADEIRA MALBEC 2.0",
    "equipamentos": [
      1
    ],
    "tempo": 155,
    "setup": 2700,
    "codigo_barra": 80606
  },
  {
    "id_erp": 80607,
    "nome": "TRAVESSA MAD DIANTEIRA 5GK5379 700 X 75 X 32MM -  POLTRONA MALBEC 2.0",
    "equipamentos": [
      1
    ],
    "tempo": 49,
    "setup": 0,
    "codigo_barra": 80607
  },
  {
    "id_erp": 80609,
    "nome": "TRAVESSA MAD TRASEIRA QV36793 700 X 75 X 32MM -  POLTRONA MALBEC 2.0",
    "equipamentos": [
      1
    ],
    "tempo": 49,
    "setup": 2700,
    "codigo_barra": 80609
  },
  {
    "id_erp": 80634,
    "nome": "PE MAD DIANTEIRO H5I8651 610 X 65 X 32MM DIREITO - CADEIRA MALBEC 2.0",
    "equipamentos": [
      1
    ],
    "tempo": 65,
    "setup": 3600,
    "codigo_barra": 80634
  },
  {
    "id_erp": 80636,
    "nome": "PE MAD DIANTEIRO 6NW9613 610 X 65 X 32MM ESQUERDO - CADEIRA MALBEC 2.0",
    "equipamentos": [
      1
    ],
    "tempo": 65,
    "setup": 0,
    "codigo_barra": 80636
  },
  {
    "id_erp": 80637,
    "nome": "PE MAD TRASEIRO 2L8R649 668 X 75 X 32MM DIREITO - CADEIRA MALBEC 2.0",
    "equipamentos": [
      1
    ],
    "tempo": 65,
    "setup": 0,
    "codigo_barra": 80637
  },
  {
    "id_erp": 80639,
    "nome": "PE MAD TRASEIRO 2TJ5277 668 X 75 X 32MM ESQUERDO - CADEIRA MALBEC 2.0",
    "equipamentos": [
      1
    ],
    "tempo": 65,
    "setup": 3600,
    "codigo_barra": 80639
  },
  {
    "id_erp": 80640,
    "nome": "TRAVESSA MAD DIANTEIRA SC34881 615 X 75 X 32MM - CADEIRA MALBEC 2.0",
    "equipamentos": [
      1
    ],
    "tempo": 105,
    "setup": 2700,
    "codigo_barra": 80640
  },
  {
    "id_erp": 80642,
    "nome": "TRAVESSA MAD TRASEIRA 6NU2759 615 X 75 X 32MM - CADEIRA MALBEC 2.0",
    "equipamentos": [
      1
    ],
    "tempo": 105,
    "setup": 0,
    "codigo_barra": 80642
  },
  {
    "id_erp": 80754,
    "nome": "MONTADO LATERAL B89Q526 DIREITO - CADEIRA MALBEC 2.0 2º ETAPA",
    "equipamentos": [
      1
    ],
    "tempo": 84,
    "setup": 0,
    "codigo_barra": 80754
  },
  {
    "id_erp": 80755,
    "nome": "MONTADO LATERAL 49R6F93 ESQUERDO - CADEIRA MALBEC 2.0 2º ETAPA",
    "equipamentos": [
      1
    ],
    "tempo": 84,
    "setup": 2700,
    "codigo_barra": 80755
  },
  {
    "id_erp": 81217,
    "nome": "ENCOSTO MONTADO 71EI348 - CADEIRA DELTA TAPECADA 2ª ETAPA",
    "equipamentos": [
      1
    ],
    "tempo": 100,
    "setup": 3600,
    "codigo_barra": 81217
  },
  {
    "id_erp": 81220,
    "nome": "ENCOSTO MONTADO 4763IN4 - BANQUETA DELTA TAPECADA",
    "equipamentos": [
      1
    ],
    "tempo": 300,
    "setup": 3600,
    "codigo_barra": 81220
  },
  {
    "id_erp": 81223,
    "nome": "ENCOSTO MONTADO G5174E8 - POLTRONA DELTA TAPECADA",
    "equipamentos": [
      1
    ],
    "tempo": 211,
    "setup": 3600,
    "codigo_barra": 81223
  },
  {
    "id_erp": 82287,
    "nome": "TRAVESSA MAD ML79327 677 X 65 X 22MM INFERIOR - MESA CENTRO PANTALONA 600",
    "equipamentos": [
      2
    ],
    "tempo": 64,
    "setup": 4200,
    "codigo_barra": 82287
  },
  {
    "id_erp": 82288,
    "nome": "TRAVESSA MAD U325427 877 X 65 X 22MM INFERIOR - MESA CENTRO PANTALONA 800",
    "equipamentos": [
      2
    ],
    "tempo": 64,
    "setup": 4200,
    "codigo_barra": 82288
  },
  {
    "id_erp": 82966,
    "nome": "DETALHE MADEIRA L6W3699 355 X 90 X 32MM PE ESQUERDO - CADEIRA/POLTRONA MALBEC 2.0",
    "equipamentos": [
      2
    ],
    "tempo": 33,
    "setup": 0,
    "codigo_barra": 82966
  },
  {
    "id_erp": 82979,
    "nome": "TRAVESSA MAD SUPERIOR 5K1J939 1600 X 50 X 32MM - BANCO EROS 1,60",
    "equipamentos": [
      2
    ],
    "tempo": "-",
    "setup": 0,
    "codigo_barra": 82979
  },
  {
    "id_erp": 82980,
    "nome": "TRAVESSA MAD LATERAL ZJ66177 1600 X 130 X 32MM - BANCO EROS 1,60",
    "equipamentos": [
      2
    ],
    "tempo": "-",
    "setup": 0,
    "codigo_barra": 82980
  },
  {
    "id_erp": 82982,
    "nome": "TRAVESSA MAD SUPERIOR G24845P 1800 X 50 X 32MM - BANCO EROS 1,80",
    "equipamentos": [
      2
    ],
    "tempo": 38,
    "setup": 3600,
    "codigo_barra": 82982
  },
  {
    "id_erp": 82983,
    "nome": "TRAVESSA MAD LATERAL 9TO3397 1800 X 130 X 32MM - BANCO EROS 1,80",
    "equipamentos": [
      2
    ],
    "tempo": 42,
    "setup": 3600,
    "codigo_barra": 82983
  },
  {
    "id_erp": 82985,
    "nome": "TRAVESSA MAD SUPERIOR 7A6D252 2000 X 50 X 32MM - BANCO EROS 2,00",
    "equipamentos": [
      2
    ],
    "tempo": "-",
    "setup": 0,
    "codigo_barra": 82985
  },
  {
    "id_erp": 82986,
    "nome": "TRAVESSA MAD LATERAL 356CV95 2000 X 130 X 32MM - BANCO EROS 2,00",
    "equipamentos": [
      2
    ],
    "tempo": "-",
    "setup": 0,
    "codigo_barra": 82986
  },
  {
    "id_erp": 82988,
    "nome": "TRAVESSA MAD SUPERIOR 9P7O577 2200 X 50 X 32MM - BANCO EROS 2,20",
    "equipamentos": [
      2
    ],
    "tempo": 38,
    "setup": 3600,
    "codigo_barra": 82988
  },
  {
    "id_erp": 82989,
    "nome": "TRAVESSA MAD LATERAL 3Z95472 2200 X 130 X 32MM - BANCO EROS 2,20",
    "equipamentos": [
      2
    ],
    "tempo": 42,
    "setup": 3600,
    "codigo_barra": 82989
  },
  {
    "id_erp": 84431,
    "nome": "TRAVESSA MAD 84G1K25 160 X 75 X 22MM DIREITO - POLTRONA ICARO",
    "equipamentos": [
      1
    ],
    "tempo": "-",
    "setup": 0,
    "codigo_barra": 84431
  },
  {
    "id_erp": 84433,
    "nome": "TRAVESSA MAD 84G1K25 160 X 75 X 22MM DIREITO - POLTRONA ICARO",
    "equipamentos": [
      1
    ],
    "tempo": "-",
    "setup": 0,
    "codigo_barra": 84433
  },
  {
    "id_erp": 432639,
    "nome": "PE MAD P0117 305 X 45 X 45MM (MESA ZARA 0,80) APENAS PARA TEMPO NA JET - 2ª ETAPA",
    "equipamentos": [
      2
    ],
    "tempo": 49,
    "setup": 2100,
    "codigo_barra": 432639
  },
  {
    "id_erp": 432679,
    "nome": "TRAV. MAD T0645 315 X 20 X 20MM INF (MESA ZARA 0,80) - 2ª ETAPA",
    "equipamentos": [
      2
    ],
    "tempo": 49,
    "setup": 2100,
    "codigo_barra": 432679
  },
  {
    "id_erp": 433419,
    "nome": "PE MAD P0117 355 X 45 X 45MM (MESA ZARA 1,00) APENAS PARA TEMPO NA JET - 2ª ETAPA",
    "equipamentos": [
      2
    ],
    "tempo": 49,
    "setup": 2100,
    "codigo_barra": 433419
  },
  {
    "id_erp": 433439,
    "nome": "TRAV. MAD T0645 410 X 20 X 20MM INF (MESA ZARA 1,00) - 2ª ETAPA",
    "equipamentos": [
      2
    ],
    "tempo": 46,
    "setup": 2100,
    "codigo_barra": 433439
  },
  {
    "id_erp": 445250,
    "nome": "TRAV. MEDIA ESPECIAL  - TESTE 1450 X 60 X 32",
    "equipamentos": [
      2
    ],
    "tempo": 41,
    "setup": 2100,
    "codigo_barra": 445250
  },
  {
    "id_erp": 482099,
    "nome": "PE MAD TRASEIRO P0512 870 X 175 X 32MM ESQ - CADEIRA JULIA (2ª ETAPA)",
    "equipamentos": [
      3
    ],
    "tempo": 18,
    "setup": 1800,
    "codigo_barra": 482099
  },
  {
    "id_erp": 482109,
    "nome": "PE MAD TRASEIRO P0513 870 X 175 X 32MM DIR - CADEIRA JULIA (2ª ETAPA)",
    "equipamentos": [
      3
    ],
    "tempo": 18,
    "setup": 1800,
    "codigo_barra": 482109
  },
  {
    "id_erp": 484889,
    "nome": "SUPORTE MAD S0033 460 X 45 X 45MM - MESA ITACARE RETANGULAR (TORNO) 2ª ETAPA",
    "equipamentos": [
      2
    ],
    "tempo": 30,
    "setup": 2100,
    "codigo_barra": 484889
  },
  {
    "id_erp": 486109,
    "nome": "SUPORTE MAD S0034 340 X 45 X 45MM - MESA ITACARE REDONDA (TORNO) 2ª ETAPA",
    "equipamentos": [
      2
    ],
    "tempo": 30,
    "setup": 2100,
    "codigo_barra": 486109
  },
  {
    "id_erp": 486239,
    "nome": "SUPORTE MAD S0035 200 X 90 X 90MM - MESA ITACARE QUADRADA (TORNO) 2ª ETAPA",
    "equipamentos": [
      2
    ],
    "tempo": 60,
    "setup": 2100,
    "codigo_barra": 486239
  },
  {
    "id_erp": 507039,
    "nome": "PE MAD DIANTEIRO P0528 575 X 40 X 40MM DIR - POLTRONA BARBARA (TORNO) 2ª ETAPA",
    "equipamentos": [
      3
    ],
    "tempo": 11,
    "setup": 2100,
    "codigo_barra": 507039
  },
  {
    "id_erp": 507049,
    "nome": "PE MAD DIANTEIRO P0529 575 X 40 X 40MM ESQ - POLTRONA BARBARA (TORNO) 2ª ETAPA",
    "equipamentos": [
      3
    ],
    "tempo": 11,
    "setup": 2100,
    "codigo_barra": 507049
  },
  {
    "id_erp": 518149,
    "nome": "PE MAD P0539 275 X 40 X 40MM ESQ - BANCO BARBARA (TORNO) 2ª ETAPA",
    "equipamentos": [
      2
    ],
    "tempo": 19,
    "setup": 2100,
    "codigo_barra": 518149
  },
  {
    "id_erp": 518159,
    "nome": "PE MAD P0540 275 X 40 X 40MM DIR - BANCO BARBARA (TORNO) 2ª ETAPA",
    "equipamentos": [
      2
    ],
    "tempo": 19,
    "setup": 0,
    "codigo_barra": 518159
  },
  {
    "id_erp": 518369,
    "nome": "PE MAD P0541 245 X 40 X 40MM DIR - PUFF BARBARA (TORNO) 2ª ETAPA",
    "equipamentos": [
      2
    ],
    "tempo": 19,
    "setup": 2100,
    "codigo_barra": 518369
  },
  {
    "id_erp": 538659,
    "nome": "PE MAD DIANTEIRO P0563 550 X 40 X 40MM - CADEIRA MONACO C/ BRACO (TORNO) 2ª ETAPA",
    "equipamentos": [
      3
    ],
    "tempo": 14,
    "setup": 2100,
    "codigo_barra": 538659
  },
  {
    "id_erp": 538669,
    "nome": "PE MAD TRASEIRO P0564 655 X 40 X 40MM - CADEIRA MONACO C/ BRACO (TORNO) 2ª ETAPA",
    "equipamentos": [
      3
    ],
    "tempo": 14,
    "setup": 0,
    "codigo_barra": 538669
  },
  {
    "id_erp": 538769,
    "nome": "PE MAD DIANTEIRO P0565 450 X 40 X 40MM - CADEIRA MONACO (TORNO) 2ª ETAPA",
    "equipamentos": [
      3
    ],
    "tempo": 13,
    "setup": 4800,
    "codigo_barra": 538769
  },
  {
    "id_erp": 538789,
    "nome": "PE MAD TRASEIRO P0567 500 X 40 X 40MM - CADEIRA MONACO (TORNO) 2ª ETAPA",
    "equipamentos": [
      3
    ],
    "tempo": 13,
    "setup": 0,
    "codigo_barra": 538789
  },
  {
    "id_erp": 543339,
    "nome": "PE MAD DIANTEIRO P0600 620 X 40 X 40MM ESQ - CADEIRA CAPINCHO - 2ª ETAPA",
    "equipamentos": [
      3
    ],
    "tempo": 20,
    "setup": 2100,
    "codigo_barra": 543339
  },
  {
    "id_erp": 543349,
    "nome": "PE MAD DIANTEIRO P0601 620 X 40 X 40MM DIR - CADEIRA CAPINCHO - 2ª ETAPA",
    "equipamentos": [
      3
    ],
    "tempo": 20,
    "setup": 2100,
    "codigo_barra": 543349
  },
  {
    "id_erp": 543359,
    "nome": "PE MAD TRASEIRO P0602 780 X 40 X 40MM ESQ - CADEIRA CAPINCHO - 2ª ETAPA",
    "equipamentos": [
      3
    ],
    "tempo": 20,
    "setup": 2100,
    "codigo_barra": 543359
  },
  {
    "id_erp": 543369,
    "nome": "PE MAD TRASEIRO P0603 780 X 40 X 40MM DIR - CADEIRA CAPINCHO - 2ª ETAPA",
    "equipamentos": [
      3
    ],
    "tempo": 20,
    "setup": 600,
    "codigo_barra": 543369
  },
  {
    "id_erp": 569219,
    "nome": "PE MAD P0640 245 X 40 X 40MM ESQ - PUFF BARBARA (TORNO) 2ª ETAPA",
    "equipamentos": [
      2
    ],
    "tempo": 19,
    "setup": 2100,
    "codigo_barra": 569219
  },
  {
    "id_erp": 574779,
    "nome": "PE MAD DIANTEIRO P0641 415 X 44 X 44MM DIREITO - CADEIRA DELTA (TORNO) 2ª ETAPA",
    "equipamentos": [
      3
    ],
    "tempo": 25,
    "setup": 3600,
    "codigo_barra": 574779
  },
  {
    "id_erp": 574789,
    "nome": "PE MAD DIANTEIRO P0642 415 X 44 X 44MM ESQUERDO - CADEIRA DELTA (TORNO) 2ª ETAPA",
    "equipamentos": [
      3
    ],
    "tempo": 25,
    "setup": 3600,
    "codigo_barra": 574789
  },
  {
    "id_erp": 574799,
    "nome": "PE MAD TRASEIRO P0643 800 X 40 X 40MM DIREITO - CADEIRA DELTA (TORNO) 2ª ETAPA",
    "equipamentos": [
      3
    ],
    "tempo": 25,
    "setup": 0,
    "codigo_barra": 574799
  },
  {
    "id_erp": 574809,
    "nome": "PE MAD TRASEIRO P0644 800 X 40 X 40MM ESQUERDO - CADEIRA DELTA (TORNO) 2ª ETAPA",
    "equipamentos": [
      3
    ],
    "tempo": 25,
    "setup": 0,
    "codigo_barra": 574809
  },
  {
    "id_erp": 588979,
    "nome": "CURVA MONTADA C0010 (APARADOR URBI) - 2º ETAPA",
    "equipamentos": [
      1
    ],
    "tempo": 30,
    "setup": 2100,
    "codigo_barra": 588979
  },
  {
    "id_erp": 629599,
    "nome": "PE MAD DIANTEIRO P0674 410 X 46 X 46MM DIREITO- CADEIRA JOLIE (TORNO) - 2º ETAPA",
    "equipamentos": [
      3
    ],
    "tempo": 21,
    "setup": 0,
    "codigo_barra": 629599
  },
  {
    "id_erp": 629619,
    "nome": "PE MAD TRASEIRO P0676 416 X 46 X 46MM - CADEIRA JOLIE (TORNO) - 2º ETAPA",
    "equipamentos": [
      3
    ],
    "tempo": 21,
    "setup": 0,
    "codigo_barra": 629619
  },
  {
    "id_erp": 630309,
    "nome": "PE MAD TRASEIRO P0679 950 X 40 X 40MM DIREITO - BANQUETA DELTA 980 (TORNO) 2ª ETAPA",
    "equipamentos": [
      3
    ],
    "tempo": 13,
    "setup": 0,
    "codigo_barra": 630309
  },
  {
    "id_erp": 630339,
    "nome": "PE MAD DIANTEIRO P0680 695 X 45 X 45MM DIREITO - BANQUETA DELTA 980 (TORNO) 2ª ETAPA",
    "equipamentos": [
      3
    ],
    "tempo": 13,
    "setup": 3900,
    "codigo_barra": 630339
  },
  {
    "id_erp": 630349,
    "nome": "PE MAD TRASEIRO P0681 950 X 40 X 40MM ESQUERDO - BANQUETA DELTA 980 (TORNO) 2ª ETAPA",
    "equipamentos": [
      3
    ],
    "tempo": 13,
    "setup": 0,
    "codigo_barra": 630349
  },
  {
    "id_erp": 630359,
    "nome": "PE MAD DIANTEIRO P0681 695 X 45 X 45MM ESQUERDO - BANQUETA DELTA 980 (TORNO) 2ª ETAPA",
    "equipamentos": [
      3
    ],
    "tempo": 13,
    "setup": 3900,
    "codigo_barra": 630359
  },
  {
    "id_erp": 642479,
    "nome": "PE MAD DIANTEIRO P0700 760 X 35 X 35MM DIREITO - BANQUETA ETOS 795 (2ª ETAPA)",
    "equipamentos": [
      3
    ],
    "tempo": 11,
    "setup": 1800,
    "codigo_barra": 642479
  },
  {
    "id_erp": 642489,
    "nome": "PE MAD TRASEIRO P0701 760 X 35 X 35MM DIREITO -  - BANQUETA ETOS 795 (2ª ETAPA)",
    "equipamentos": [
      3
    ],
    "tempo": 11,
    "setup": 1800,
    "codigo_barra": 642489
  },
  {
    "id_erp": 642499,
    "nome": "ASSENTO PRENSADO MAD A0530 403 X 367 X 128MM  - BANQUETA ETOS 695/795 (2º ETAPA)",
    "equipamentos": [
      1
    ],
    "tempo": 1.5,
    "setup": 2100,
    "codigo_barra": 642499
  },
  {
    "id_erp": 642559,
    "nome": "PE MAD DIANTEIRO P0702 660 X 35 X 35MM DIREITA - BANQUETA ETOS 695 (2ª ETAPA)",
    "equipamentos": [
      3
    ],
    "tempo": 11,
    "setup": 2100,
    "codigo_barra": 642559
  },
  {
    "id_erp": 642569,
    "nome": "PE MAD TRASEIRO P0703 660 X 35 X 35MM DIREITA - BANQUETA ETOS 695 (2ª ETAPA)",
    "equipamentos": [
      3
    ],
    "tempo": 11,
    "setup": 0,
    "codigo_barra": 642569
  },
  {
    "id_erp": 646079,
    "nome": "PE MAD TRASEIRO P0704 850 X 40 X 40MM DIREITO - BANQUETA DELTA 880 (TORNO) 2ª ETAPA",
    "equipamentos": [
      3
    ],
    "tempo": 13,
    "setup": 0,
    "codigo_barra": 646079
  },
  {
    "id_erp": 646089,
    "nome": "PE MAD TRASEIRO P0705 850 X 40 X 40MM ESQUERDO - BANQUETA DELTA 880 (TORNO) 2ª ETAPA",
    "equipamentos": [
      3
    ],
    "tempo": 13,
    "setup": 0,
    "codigo_barra": 646089
  },
  {
    "id_erp": 646099,
    "nome": "PE MAD DIANTEIRO P0706 595 X 45 X 45MM DIREITO - BANQUETA DELTA 880 (TORNO) 2ª ETAPA",
    "equipamentos": [
      3
    ],
    "tempo": 13,
    "setup": 3900,
    "codigo_barra": 646099
  },
  {
    "id_erp": 646109,
    "nome": "PE MAD DIANTEIRO P0707 595 X 45 X 45MM ESQUERDO - BANQUETA DELTA 880 (TORNO) 2ª ETAPA",
    "equipamentos": [
      3
    ],
    "tempo": 13,
    "setup": 3900,
    "codigo_barra": 646109
  },
  {
    "id_erp": 650709,
    "nome": "BASE PRENSADA B0482 465 X 250 X 250MM - MESA APOIO ESCHER (2º ETAPA)",
    "equipamentos": [
      1
    ],
    "tempo": 41,
    "setup": 2100,
    "codigo_barra": 650709
  },
  {
    "id_erp": 652359,
    "nome": "PE MAD DIANTEIRO P0674 410 X 46 X 46MM ESQUERDO- CADEIRA JOLIE (TORNO) - 2º ETAPA",
    "equipamentos": [
      3
    ],
    "tempo": 21,
    "setup": 3600,
    "codigo_barra": 652359
  },
  {
    "id_erp": 654379,
    "nome": "PE MAD DIANTEIRO P0700 760 X 35 X 35MM ESQUERDO - BANQUETA ETOS 795 (2ª ETAPA)",
    "equipamentos": [
      3
    ],
    "tempo": 11,
    "setup": 1800,
    "codigo_barra": 654379
  },
  {
    "id_erp": 654389,
    "nome": "PE MAD TRASEIRO P0701 760 X 35 X 35MM ESQUERDO - BANQUETA ETOS 795 (2ª ETAPA)",
    "equipamentos": [
      3
    ],
    "tempo": 11,
    "setup": 1800,
    "codigo_barra": 654389
  },
  {
    "id_erp": 654399,
    "nome": "PE MAD DIANTEIRO P0702 660 X 35 X 35MM ESQUERDA - BANQUETA ETOS 695 (2ª ETAPA)",
    "equipamentos": [
      3
    ],
    "tempo": 11,
    "setup": 2100,
    "codigo_barra": 654399
  },
  {
    "id_erp": 654409,
    "nome": "PE MAD TRASEIRO P0703 660 X 35 X 35MM ESQUERDA - BANQUETA ETOS 695 (2ª ETAPA)",
    "equipamentos": [
      3
    ],
    "tempo": 11,
    "setup": 0,
    "codigo_barra": 654409
  },
  {
    "id_erp": 656569,
    "nome": "PE MAD TRASEIRO P0724 160 X 42 X 42MM SUP ESQ - CADEIRA/BANQUETA BAIA - 2ª ETAPA",
    "equipamentos": [
      3
    ],
    "tempo": 19,
    "setup": 0,
    "codigo_barra": 656569
  },
  {
    "id_erp": 659519,
    "nome": "PE MAD TRASEIRO P0718 160 X 42 X 42MM SUP DIR - CADEIRA/BANQUETA BAIA - 2ª ETAPA",
    "equipamentos": [
      3
    ],
    "tempo": 19,
    "setup": 5400,
    "codigo_barra": 659519
  },
  {
    "id_erp": 659529,
    "nome": "PE MAD TRASEIRO P0719 700 X 42 X 42MM INF DIR - CADEIRA BAIA - 2ª ETAPA",
    "equipamentos": [
      3
    ],
    "tempo": 15,
    "setup": 0,
    "codigo_barra": 659529
  },
  {
    "id_erp": 659569,
    "nome": "PE MAD DIANTEIRO P0720 445 X 45 X 45MM DIR - CADEIRA BAIA - 2ª ETAPA",
    "equipamentos": [
      3
    ],
    "tempo": 15,
    "setup": 3600,
    "codigo_barra": 659569
  },
  {
    "id_erp": 659619,
    "nome": "PE MAD DIANTEIRO P0721 445 X 45 X 45MM ESQ - CADEIRA BAIA - 2ª ETAPA",
    "equipamentos": [
      3
    ],
    "tempo": 15,
    "setup": 3600,
    "codigo_barra": 659619
  },
  {
    "id_erp": 666369,
    "nome": "PE MAD TRASEIRO P0722 520 X 45 X 45MM ESQUERDO - POLTRONA MONET (2ª ETAPA)",
    "equipamentos": [
      3
    ],
    "tempo": 28,
    "setup": 6000,
    "codigo_barra": 666369
  },
  {
    "id_erp": 666379,
    "nome": "PE MAD DIANTEIRO P0723 558 X 45 X 45MM ESQUERDO - POLTRONA MONET (2ª ETAPA)",
    "equipamentos": [
      3
    ],
    "tempo": 21,
    "setup": 6000,
    "codigo_barra": 666379
  },
  {
    "id_erp": 670759,
    "nome": "PE MAD TRASEIRO P0725 700 X 42 X 42MM INF ESQ - CADEIRA BAIA - 2ª ETAPA",
    "equipamentos": [
      3
    ],
    "tempo": 15,
    "setup": 0,
    "codigo_barra": 670759
  },
  {
    "id_erp": 681229,
    "nome": "PE MAD TRASEIRO P0722 520 X 45 X 45MM DIREITO - POLTRONA MONET (2ª ETAPA)",
    "equipamentos": [
      3
    ],
    "tempo": 28,
    "setup": 0,
    "codigo_barra": 681229
  },
  {
    "id_erp": 681239,
    "nome": "PE MAD DIANTEIRO P0723 558 X 45 X 45MM DIREITO - POLTRONA MONET (2ª ETAPA)",
    "equipamentos": [
      3
    ],
    "tempo": 21,
    "setup": 0,
    "codigo_barra": 681239
  },
  {
    "id_erp": 687169,
    "nome": "PE MAD DIANTEIRO T0728 430 X 45 X 45MM DIREITO - CADEIRA ADHARA (2º ETAPA)",
    "equipamentos": [
      3
    ],
    "tempo": 15,
    "setup": 5400,
    "codigo_barra": 687169
  },
  {
    "id_erp": 687179,
    "nome": "PE MAD DIANTEIRO T0729 430 X 45 X 45MM ESQUERDO - CADEIRA ADHARA (2º ETAPA)",
    "equipamentos": [
      3
    ],
    "tempo": 15,
    "setup": 0,
    "codigo_barra": 687179
  },
  {
    "id_erp": 691449,
    "nome": "PE MAD DIANTEIRO T0730 485 X 32 X 32MM DIREITO - POLTRONA DELTA - 2º ETAPA",
    "equipamentos": [
      3
    ],
    "tempo": 11,
    "setup": 3600,
    "codigo_barra": 691449
  },
  {
    "id_erp": 691459,
    "nome": "PE MAD DIANTEIRO T0731 485 X 32 X 32MM ESQUERDO - POLTRONA DELTA - 2º ETAPA",
    "equipamentos": [
      3
    ],
    "tempo": 11,
    "setup": 0,
    "codigo_barra": 691459
  },
  {
    "id_erp": 691469,
    "nome": "PE MAD TRASEIRO T0732 730 X 42 X 42MM DIREITO - POLTRONA DELTA - 2º ETAPA",
    "equipamentos": [
      3
    ],
    "tempo": 16,
    "setup": 5400,
    "codigo_barra": 691469
  },
  {
    "id_erp": 691479,
    "nome": "PE MAD TRASEIRO T0733 730 X 42 X 42MM ESQUERDO - POLTRONA DELTA - 2º ETAPA",
    "equipamentos": [
      3
    ],
    "tempo": 16,
    "setup": 0,
    "codigo_barra": 691479
  },
  {
    "id_erp": 691849,
    "nome": "PE MAD T0734 590 X 32 X 32MM - BANQUETA GIRATORIA PIER 940 (2º ETAPA)",
    "equipamentos": [
      3
    ],
    "tempo": 15,
    "setup": 3600,
    "codigo_barra": 691849
  },
  {
    "id_erp": 692039,
    "nome": "PE MAD T0735 690 X 32 X 32MM - BANQUETA GIRATORIA PIER 1040 (2º ETAPA)",
    "equipamentos": [
      3
    ],
    "tempo": 15,
    "setup": 3600,
    "codigo_barra": 692039
  },
  {
    "id_erp": 695919,
    "nome": "PE MAD DIANTEIRO T0736 410 X 32 X 32MM DIREITO - CADEIRA DUCHAMP (2º ETAPA)",
    "equipamentos": [
      3
    ],
    "tempo": 15,
    "setup": 3600,
    "codigo_barra": 695919
  },
  {
    "id_erp": 695929,
    "nome": "PE MAD DIANTEIRO T0737 695 X 32 X 32MM ESQUERDO - CADEIRA DUCHAMP (2º ETAPA)",
    "equipamentos": [
      3
    ],
    "tempo": 15,
    "setup": 0,
    "codigo_barra": 695929
  },
  {
    "id_erp": 695939,
    "nome": "PE MAD TRASEIRO T0738 660 X 32 X 32MM DIREITO - CADEIRA DUCHAMP (2º ETAPA)",
    "equipamentos": [
      3
    ],
    "tempo": 13,
    "setup": 3600,
    "codigo_barra": 695939
  },
  {
    "id_erp": 695949,
    "nome": "PE MAD TRASEIRO T0739 678 X 32 X 32MM ESQUERDO - CADEIRA DUCHAMP (2º ETAPA)",
    "equipamentos": [
      3
    ],
    "tempo": 13,
    "setup": 0,
    "codigo_barra": 695949
  },
  {
    "id_erp": 696501,
    "nome": "CAPA ENCOSTO PRENSADO LAMINA CARVALHO - CADEIRA ADHARA",
    "equipamentos": [
      1
    ],
    "tempo": 43,
    "setup": 2100,
    "codigo_barra": 696501
  },
  {
    "id_erp": 696502,
    "nome": "CAPA ENCOSTO PRENSADO LAMINA JEQUITIBA - CADEIRA ADHARA",
    "equipamentos": [
      1
    ],
    "tempo": 43,
    "setup": 2100,
    "codigo_barra": 696502
  },
  {
    "id_erp": 696503,
    "nome": "CAPA ENCOSTO PRENSADO LAMINA CINAMOMO - CADEIRA ADHARA",
    "equipamentos": [
      1
    ],
    "tempo": 43,
    "setup": 2100,
    "codigo_barra": 696503
  },
  {
    "id_erp": 696504,
    "nome": "CAPA ENCOSTO PRENSADO LAMINA FREIJO - CADEIRA ADHARA",
    "equipamentos": [
      1
    ],
    "tempo": 43,
    "setup": 2100,
    "codigo_barra": 696504
  },
  {
    "id_erp": 696505,
    "nome": "CAPA ENCOSTO PRENSADO LAMINA NOGUEIRA - CADEIRA ADHARA",
    "equipamentos": [
      1
    ],
    "tempo": 43,
    "setup": 2100,
    "codigo_barra": 696505
  },
  {
    "id_erp": 696506,
    "nome": "CAPA ENCOSTO PRENSADO LAMINA LOURO - CADEIRA ADHARA",
    "equipamentos": [
      1
    ],
    "tempo": 43,
    "setup": 2100,
    "codigo_barra": 696506
  },
  {
    "id_erp": 704339,
    "nome": "PE MAD TRASEIRO T0740 431 X 40 X 40MM DIREITO - CADEIRA KRAFT EUCALIPTO (2º ETAPA)",
    "equipamentos": [
      3
    ],
    "tempo": 8,
    "setup": 2100,
    "codigo_barra": 704339
  },
  {
    "id_erp": 704359,
    "nome": "PE MAD DIANTEIRO T0741 442 X 40 X 40MM DIREITO - CADEIRA KRAFT EUCALIPTO (2º ETAPA)",
    "equipamentos": [
      3
    ],
    "tempo": 8,
    "setup": 2100,
    "codigo_barra": 704359
  },
  {
    "id_erp": 710779,
    "nome": "PE MAD TRASEIRO T0742 720 X 45 X 45MM DIREITO - CADEIRA PANTALONA - 2º ETAPA",
    "equipamentos": [
      3
    ],
    "tempo": 16,
    "setup": 2400,
    "codigo_barra": 710779
  },
  {
    "id_erp": 710799,
    "nome": "PE MAD DIANTEIRO T0743 445 X 45 X 45MM - CADEIRA PANTALONA - 2º ETAPA",
    "equipamentos": [
      3
    ],
    "tempo": 16,
    "setup": 2400,
    "codigo_barra": 710799
  },
  {
    "id_erp": 713759,
    "nome": "PE MAD TRASEIRO T0741 431 X 40 X 40MM DIREITO - CADEIRA KRAFT TAUARI (2º ETAPA)",
    "equipamentos": [
      3
    ],
    "tempo": 8,
    "setup": 2100,
    "codigo_barra": 713759
  },
  {
    "id_erp": 713779,
    "nome": "PE MAD DIANTEIRO T0742 442 X 40 X 40MM DIREITO - CADEIRA KRAFT TAUARI (2º ETAPA)",
    "equipamentos": [
      3
    ],
    "tempo": 8,
    "setup": 2100,
    "codigo_barra": 713779
  },
  {
    "id_erp": 716369,
    "nome": "PE MAD TRASEIRO P0720 837 X 42 X 42MM INF DIR - BANQUETA BAIA 985 - 2º ETAPA",
    "equipamentos": [
      3
    ],
    "tempo": 14,
    "setup": 0,
    "codigo_barra": 716369
  },
  {
    "id_erp": 716399,
    "nome": "PE MAD TRASEIRO P0729 837 X 42 X 42MM INF ESQ - BANQUETA BAIA 985 - 2º ETAPA",
    "equipamentos": [
      3
    ],
    "tempo": 14,
    "setup": 0,
    "codigo_barra": 716399
  },
  {
    "id_erp": 716409,
    "nome": "PE MAD DIANTEIRO P0720 703 X 42 X 42MM DIR - BANQUETA BAIA 985 - 2ª ETAPA",
    "equipamentos": [
      3
    ],
    "tempo": 14,
    "setup": 2100,
    "codigo_barra": 716409
  },
  {
    "id_erp": 716429,
    "nome": "PE MAD DIANTEIRO P0722 703 X 42 X 42MM ESQ - BANQUETA BAIA 985 - 2ª ETAPA",
    "equipamentos": [
      3
    ],
    "tempo": 14,
    "setup": 2100,
    "codigo_barra": 716429
  },
  {
    "id_erp": 716479,
    "nome": "PE MAD TRASEIRO P0726 737 X 42 X 42MM INF ESQ - BANQUETA BAIA 885 - 2º ETAPA",
    "equipamentos": [
      3
    ],
    "tempo": 14,
    "setup": 0,
    "codigo_barra": 716479
  },
  {
    "id_erp": 716509,
    "nome": "PE MAD TRASEIRO P0732 737 X 42 X 42MM INF DIR - BANQUETA BAIA 885 - 2º ETAPA",
    "equipamentos": [
      3
    ],
    "tempo": 14,
    "setup": 0,
    "codigo_barra": 716509
  },
  {
    "id_erp": 716529,
    "nome": "PE MAD DIANTEIRO P0722 603 X 42 X 42MM DIR - BANQUETA BAIA 885 - 2º ETAPA",
    "equipamentos": [
      3
    ],
    "tempo": 14,
    "setup": 2100,
    "codigo_barra": 716529
  },
  {
    "id_erp": 716549,
    "nome": "PE MAD DIANTEIRO P0723 603 X 42 X 42MM ESQ - BANQUETA BAIA 885 - 2º ETAPA",
    "equipamentos": [
      3
    ],
    "tempo": 14,
    "setup": 2100,
    "codigo_barra": 716549
  },
  {
    "id_erp": 724439,
    "nome": "PE MAD 5CN4724 400 X 95 X 120MM - BANCO CURUPIRA (2º ETAPA)",
    "equipamentos": [
      1
    ],
    "tempo": 305,
    "setup": 2100,
    "codigo_barra": 724439
  },
  {
    "id_erp": 735109,
    "nome": "PE MAD TRASEIRO 2I1S275 720 X 45 X 45MM ESQUERDO - CADEIRA PANTALONA - 2º ETAPA",
    "equipamentos": [
      3
    ],
    "tempo": 16,
    "setup": 2400,
    "codigo_barra": 735109
  },
  {
    "id_erp": 747689,
    "nome": "PE MAD TRASEIRO T0740 431 X 40 X 40MM ESQUERDO - CADEIRA KRAFT EUCALIPTO (2º ETAPA)",
    "equipamentos": [
      3
    ],
    "tempo": 8,
    "setup": 2100,
    "codigo_barra": 747689
  },
  {
    "id_erp": 747699,
    "nome": "PE MAD DIANTEIRO T0741 442 X 40 X 40MM ESQUERDO - CADEIRA KRAFT EUCALIPTO (2º ETAPA)",
    "equipamentos": [
      3
    ],
    "tempo": 8,
    "setup": 2100,
    "codigo_barra": 747699
  },
  {
    "id_erp": 747709,
    "nome": "PE MAD TRASEIRO T0741 431 X 40 X 40MM ESQUERDO - CADEIRA KRAFT TAUARI (2º ETAPA)",
    "equipamentos": [
      3
    ],
    "tempo": 8,
    "setup": 2100,
    "codigo_barra": 747709
  },
  {
    "id_erp": 747719,
    "nome": "PE MAD DIANTEIRO T0742 442 X 40 X 40MM ESQUERDO - CADEIRA KRAFT TAUARI (2º ETAPA)",
    "equipamentos": [
      3
    ],
    "tempo": 8,
    "setup": 2100,
    "codigo_barra": 747719
  },
  {
    "id_erp": 752789,
    "nome": "PE MAD TRASEIRO Z123J17 890 X 45 X 45MM DIREITO - BANQUETA PANTALONA 960 - 2º ETAPA",
    "equipamentos": [
      3
    ],
    "tempo": 48,
    "setup": 6000,
    "codigo_barra": 752789
  },
  {
    "id_erp": 752799,
    "nome": "PE MAD TRASEIRO 8NE3445 890 X 45 X 45MM ESQUERDO - BANQUETA PANTALONA 960 - 2º ETAPA",
    "equipamentos": [
      3
    ],
    "tempo": 15,
    "setup": 0,
    "codigo_barra": 752799
  },
  {
    "id_erp": 752819,
    "nome": "PE MAD DIANTEIRO NG79999 690 X 45 X 45MM - BANQUETA PANTALONA 960 - 2º ETAPA",
    "equipamentos": [
      3
    ],
    "tempo": 48,
    "setup": 6000,
    "codigo_barra": 752819
  },
  {
    "id_erp": 762549,
    "nome": "PE MAD TRASEIRO 8Z12U69 765 X 45 X 45MM DIREITO - BANQUETA PANTALONA 860 - 2º ETAPA",
    "equipamentos": [
      3
    ],
    "tempo": 48,
    "setup": 6000,
    "codigo_barra": 762549
  },
  {
    "id_erp": 762569,
    "nome": "PE MAD TRASEIRO 1SX2773 765 X 45 X 45MM ESQUERDO - BANQUETA PANTALONA 860 - 2º ETAPA",
    "equipamentos": [
      3
    ],
    "tempo": 48,
    "setup": 6000,
    "codigo_barra": 762569
  },
  {
    "id_erp": 762579,
    "nome": "PE MAD DIANTEIRO BP59617 550 X 45 X 45MM - BANQUETA PANTALONA 860 - 2º ETAPA",
    "equipamentos": [
      3
    ],
    "tempo": 48,
    "setup": 6000,
    "codigo_barra": 762579
  },
  {
    "id_erp": 763009,
    "nome": "PE MAD DIANTEIRO YG75477 670 X 45 X 45MM DIREITO - BANQUETA ADHARA 970 (2º ETAPA)",
    "equipamentos": [
      3
    ],
    "tempo": 16,
    "setup": 2100,
    "codigo_barra": 763009
  },
  {
    "id_erp": 763029,
    "nome": "PE MAD DIANTEIRO 4OI6923 670 X 45 X 45MM ESQUERDO - BANQUETA ADHARA 970 (2º ETAPA)",
    "equipamentos": [
      3
    ],
    "tempo": 16,
    "setup": 0,
    "codigo_barra": 763029
  },
  {
    "id_erp": 763289,
    "nome": "PE MAD DIANTEIRO NJ64581 570 X 45 X 45MM DIREITO - BANQUETA ADHARA 870 (2º ETAPA)",
    "equipamentos": [
      3
    ],
    "tempo": 16,
    "setup": 2100,
    "codigo_barra": 763289
  },
  {
    "id_erp": 763309,
    "nome": "PE MAD DIANTEIRO 9983JC9 570 X 45 X 45MM ESQUERDO - BANQUETA ADHARA 870 (2º ETAPA)",
    "equipamentos": [
      3
    ],
    "tempo": 16,
    "setup": 0,
    "codigo_barra": 763309
  },
  {
    "id_erp": 770089,
    "nome": "PE MAD TRASEIRO C9W2589 650 X 55 X 55MM DIREITO - POLTRONA PANTALONA - 2º ETAPA",
    "equipamentos": [
      3
    ],
    "tempo": 15,
    "setup": 2400,
    "codigo_barra": 770089
  },
  {
    "id_erp": 770109,
    "nome": "PE MAD TRASEIRO PX11733 650 X 55 X 55MM ESQUERDO - POLTRONA PANTALONA - 2º ETAPA",
    "equipamentos": [
      3
    ],
    "tempo": 15,
    "setup": 2400,
    "codigo_barra": 770109
  },
  {
    "id_erp": 770119,
    "nome": "PE MAD DIANTEIRO 36Q9K35 365 X 55 X 55MM - POLTRONA PANTALONA - 2º ETAPA",
    "equipamentos": [
      3
    ],
    "tempo": 15,
    "setup": 2400,
    "codigo_barra": 770119
  },
  {
    "id_erp": 777979,
    "nome": "PE MAD 185CN46 250 X 50 X 50MM - MESA CENTRO PANTALONA 600 - PE PRENSADO 270 X 65 X 76 MM -  2ª ETAPA",
    "equipamentos": [
      3
    ],
    "tempo": 22,
    "setup": 4800,
    "codigo_barra": 777979
  },
  {
    "id_erp": 778089,
    "nome": "PE MAD JS33345 330 X 50 X 50MM - MESA CENTRO PANTALONA 800 - PE PRENSADO 350 X 65 X 76 MM -  2ª ETAPA",
    "equipamentos": [
      3
    ],
    "tempo": 22,
    "setup": 4800,
    "codigo_barra": 778089
  },
  {
    "id_erp": 786499,
    "nome": "PE MAD ER17316 330 X 330 X 50MM - BANCO PANTALONA - 2º ETAPA",
    "equipamentos": [
      3
    ],
    "tempo": "-",
    "setup": 2100,
    "codigo_barra": 786499
  },
  {
    "id_erp": 794439,
    "nome": "PE MAD DIANTEIRO T6M8816 410 X 50 X 50MM DIREITO - CADEIRA CORA (2ª ETAPA)",
    "equipamentos": [
      3
    ],
    "tempo": 9,
    "setup": 3600,
    "codigo_barra": 794439
  },
  {
    "id_erp": 794459,
    "nome": "PE MAD DIANTEIRO 6814O58 410 X 50 X 50MM ESQUERDO - CADEIRA CORA (2ª ETAPA)",
    "equipamentos": [
      3
    ],
    "tempo": 9,
    "setup": 0,
    "codigo_barra": 794459
  },
  {
    "id_erp": 824569,
    "nome": "PE MAD TRASEIRO 28Y9748 720 X 45 X 45MM DIREITO - CADEIRA PANTALONA ENCOSTO MADEIRA  2ª ETAPA",
    "equipamentos": [
      3
    ],
    "tempo": "-",
    "setup": 0,
    "codigo_barra": 824569
  },
  {
    "id_erp": 824579,
    "nome": "PE MAD TRASEIRO S8L9747 720 X 45 X 45MM ESQUERDO - CADEIRA PANTALONA ENCOSTO MADEIRA   2ª ETAPA",
    "equipamentos": [
      3
    ],
    "tempo": "-",
    "setup": 0,
    "codigo_barra": 824579
  },
  {
    "id_erp": 34128,
    "nome": "PE MAD DIANTEIRO P0017 450 X 40 X 32MM ESQUERDO - CADEIRA ELLEN/LANA/MALU/BELA/MONTANA/DONNA/ALBA/MEG/LAIS/NAOMI/VIVI",
    "equipamentos": [
      1
    ],
    "tempo": 12,
    "setup": 0,
    "codigo_barra": 34128
  },
  {
    "id_erp": 34568,
    "nome": "TRAVESSA MAD LATERAL T0067 443 X 75 X 22MM ESQUERD - CADEIRA LUNNA/ELISA",
    "equipamentos": [
      1
    ],
    "tempo": 42,
    "setup": 2100,
    "codigo_barra": 34568
  },
  {
    "id_erp": 35078,
    "nome": "PE MAD DIANTEIRO P0033 450 X 40 X 32MM DIREITO - CADEIRA ELLEN/LANA/MALU/BELA/MONT/DONNA/ALBA/MEG/LAIS/NAOMI/VIVI",
    "equipamentos": [
      1
    ],
    "tempo": 12,
    "setup": 2100,
    "codigo_barra": 35078
  },
  {
    "id_erp": 35173,
    "nome": "TRAVESSA MAD LATERAL T0075 443 X 75 X 22MM DIREITA - CADEIRA LUNNA/ELISA",
    "equipamentos": [
      1
    ],
    "tempo": 42,
    "setup": 0,
    "codigo_barra": 35173
  },
  {
    "id_erp": 46252,
    "nome": "TRAVESSA MAD T0695 470 X 110 X 45MM MENOR - BUFFET/BAR TAMBORE",
    "equipamentos": [
      1
    ],
    "tempo": 90,
    "setup": 2100,
    "codigo_barra": 46252
  },
  {
    "id_erp": 56182,
    "nome": "TRAVESSA MAD LATERAL T0761 425 X 65 X 22MM DIREITA - CADEIRA LIA LX/ LIA LX C/BRACO",
    "equipamentos": [
      1
    ],
    "tempo": 26,
    "setup": 5400,
    "codigo_barra": 56182
  },
  {
    "id_erp": 56183,
    "nome": "TRAVESSA MAD LATERAL T0762 425 X 65 X 22MM ESQUERDA - CADEIRA LIA LX/ LIA LX C/BRACO",
    "equipamentos": [
      1
    ],
    "tempo": 26,
    "setup": 0,
    "codigo_barra": 56183
  },
  {
    "id_erp": 27304,
    "nome": "APARADOR CARMIM 1,80",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 17,
    "setup": 900,
    "codigo_barra": 27304
  },
  {
    "id_erp": 48482,
    "nome": "APARADOR CONRADO",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 465,
    "setup": 900,
    "codigo_barra": 48482
  },
  {
    "id_erp": 61562,
    "nome": "APARADOR LUGO 1,20",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 310,
    "setup": 900,
    "codigo_barra": 61562
  },
  {
    "id_erp": 42703,
    "nome": "APARADOR LUGO 1,40",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 340,
    "setup": 900,
    "codigo_barra": 42703
  },
  {
    "id_erp": 42702,
    "nome": "APARADOR LUGO 1,50",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 340,
    "setup": 900,
    "codigo_barra": 42702
  },
  {
    "id_erp": 38808,
    "nome": "APARADOR LUGO 1,60",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 340,
    "setup": 900,
    "codigo_barra": 38808
  },
  {
    "id_erp": 24203,
    "nome": "APARADOR LUGO 1,80",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 340,
    "setup": 900,
    "codigo_barra": 24203
  },
  {
    "id_erp": 56315,
    "nome": "APARADOR LUGO 2,20",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 340,
    "setup": 900,
    "codigo_barra": 56315
  },
  {
    "id_erp": 57335,
    "nome": "APARADOR LUGO 2,40",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 340,
    "setup": 900,
    "codigo_barra": 57335
  },
  {
    "id_erp": 63713,
    "nome": "APARADOR LUGO SLIM 1,20",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 340,
    "setup": 900,
    "codigo_barra": 63713
  },
  {
    "id_erp": 70903,
    "nome": "APARADOR LUGO SLIM 1,30 - MEDIDA ESPECIAL (CHAMAR SERGIO PARA ACOMPANHAR)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.2,
    "setup": 900,
    "codigo_barra": 70903
  },
  {
    "id_erp": 63714,
    "nome": "APARADOR LUGO SLIM 1,40",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 340,
    "setup": 900,
    "codigo_barra": 63714
  },
  {
    "id_erp": 63715,
    "nome": "APARADOR LUGO SLIM 1,50",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 340,
    "setup": 900,
    "codigo_barra": 63715
  },
  {
    "id_erp": 63716,
    "nome": "APARADOR LUGO SLIM 1,60",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 340,
    "setup": 900,
    "codigo_barra": 63716
  },
  {
    "id_erp": 63717,
    "nome": "APARADOR LUGO SLIM 1,80",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 340,
    "setup": 900,
    "codigo_barra": 63717
  },
  {
    "id_erp": 63718,
    "nome": "APARADOR LUGO SLIM 2,20",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 340,
    "setup": 900,
    "codigo_barra": 63718
  },
  {
    "id_erp": 63719,
    "nome": "APARADOR LUGO SLIM 2,40",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 240,
    "setup": 900,
    "codigo_barra": 63719
  },
  {
    "id_erp": 65918,
    "nome": "APARADOR OBLONGO 1,80",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.243,
    "setup": 900,
    "codigo_barra": 65918
  },
  {
    "id_erp": 65919,
    "nome": "APARADOR OBLONGO 2,00",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.479,
    "setup": 900,
    "codigo_barra": 65919
  },
  {
    "id_erp": 65920,
    "nome": "APARADOR OBLONGO 2,20",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.494,
    "setup": 900,
    "codigo_barra": 65920
  },
  {
    "id_erp": 53565,
    "nome": "APARADOR ORION 1,20",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 195,
    "setup": 900,
    "codigo_barra": 53565
  },
  {
    "id_erp": 36213,
    "nome": "APARADOR ORION 1,50",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 195,
    "setup": 900,
    "codigo_barra": 36213
  },
  {
    "id_erp": 36934,
    "nome": "APARADOR SENA C/ VIDRO",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 360,
    "setup": 900,
    "codigo_barra": 36934
  },
  {
    "id_erp": 58565,
    "nome": "APARADOR URBI 0,90",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 208,
    "setup": 900,
    "codigo_barra": 58565
  },
  {
    "id_erp": 71658,
    "nome": "APARADOR URBI 1,20 - CHAMAR ZÉ DESENVOLVIMENTO P/ ACOMPANHAR (ESPECIAL)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.08,
    "setup": 900,
    "codigo_barra": 71658
  },
  {
    "id_erp": 57499,
    "nome": "APARADOR URBI 1,50",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 229,
    "setup": 900,
    "codigo_barra": 57499
  },
  {
    "id_erp": 43720,
    "nome": "ARMARIO KLINT",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 115,
    "setup": 900,
    "codigo_barra": 43720
  },
  {
    "id_erp": 43275,
    "nome": "ARMARIO VEDRA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 212,
    "setup": 900,
    "codigo_barra": 43275
  },
  {
    "id_erp": 38894,
    "nome": "ASSENTO LAM (CONCHA) P0026 470 X 450 X 12MM - (CAD. EMILY LAMINADA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 60,
    "setup": 900,
    "codigo_barra": 38894
  },
  {
    "id_erp": 68722,
    "nome": "ASSENTO LAMINA PINUS A0542 480 X 470 X 9MM - CADEIRA ADHARA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 26,
    "setup": 900,
    "codigo_barra": 68722
  },
  {
    "id_erp": 79450,
    "nome": "ASSENTO MDF 485 X 435 X 20MM (CADEIRA CORA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 226,
    "setup": 900,
    "codigo_barra": 79450
  },
  {
    "id_erp": 37433,
    "nome": "ASSENTO MDF A0012 490 X 456 X 2,8MM (3 PÇS) - (CAD. MAIA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 30,
    "setup": 900,
    "codigo_barra": 37433
  },
  {
    "id_erp": 38829,
    "nome": "ASSENTO MDF A0023 490 X 490 X 12MM (3 PÇS)- MASTER (CAD. SOFIA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 30,
    "setup": 900,
    "codigo_barra": 38829
  },
  {
    "id_erp": 42245,
    "nome": "ASSENTO MDF A0039 920 X 500 X 2,8MM - (CAD. CLAU)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 60,
    "setup": 900,
    "codigo_barra": 42245
  },
  {
    "id_erp": 61644,
    "nome": "ASSENTO MDF A0519 655 X 45 X 2,8MM - POLTRONA COPAN",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 660,
    "setup": 900,
    "codigo_barra": 61644
  },
  {
    "id_erp": 46291,
    "nome": "ASSENTO MDF CAD ANNE 510 X 510 X 2,8 MM (3 PÇS) - (CAD. ANNE)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 30,
    "setup": 900,
    "codigo_barra": 46291
  },
  {
    "id_erp": 73518,
    "nome": "ASSENTO MONTADO MAD - BANCO BARU 1,40",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 180,
    "setup": 900,
    "codigo_barra": 73518
  },
  {
    "id_erp": 72464,
    "nome": "ASSENTO MONTADO MAD - BANCO BARU 1,60",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 180,
    "setup": 900,
    "codigo_barra": 72464
  },
  {
    "id_erp": 72488,
    "nome": "ASSENTO MONTADO MAD - BANCO BARU 1,80",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 180,
    "setup": 900,
    "codigo_barra": 72488
  },
  {
    "id_erp": 72508,
    "nome": "ASSENTO MONTADO MAD - BANCO BARU 2,00",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 180,
    "setup": 900,
    "codigo_barra": 72508
  },
  {
    "id_erp": 45179,
    "nome": "ASSENTO PRENSADO - (POLTRONA BOTANIC)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 30,
    "setup": 900,
    "codigo_barra": 45179
  },
  {
    "id_erp": 45100,
    "nome": "ASSENTO PRENSADO A0050 500 X 500 X 8,4MM (CAD. LAURA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 60,
    "setup": 900,
    "codigo_barra": 45100
  },
  {
    "id_erp": 48216,
    "nome": "ASSENTO PRENSADO A0067 455 X 465 X 10MM (CADEIRA JULIA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 22,
    "setup": 900,
    "codigo_barra": 48216
  },
  {
    "id_erp": 50970,
    "nome": "ASSENTO PRENSADO A0080 490 X 430 X 10MM (BANQUETA e CADEIRA PAOLA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 40,
    "setup": 900,
    "codigo_barra": 50970
  },
  {
    "id_erp": 54387,
    "nome": "ASSENTO PRENSADO A0099 470 X 430 X 10MM BANQUETA PAOLA 910/1010MM",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 40,
    "setup": 900,
    "codigo_barra": 54387
  },
  {
    "id_erp": 54818,
    "nome": "ASSENTO PRENSADO A0102 470 X 455 X 10MM (CADEIRA TALITA (LAMINA CRUZADA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 60,
    "setup": 900,
    "codigo_barra": 54818
  },
  {
    "id_erp": 54875,
    "nome": "ASSENTO PRENSADO A0103 470 X 495 X 10MM (CADEIRA LUISE TAPECADA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 60,
    "setup": 900,
    "codigo_barra": 54875
  },
  {
    "id_erp": 55395,
    "nome": "ASSENTO PRENSADO A0104 440 X 520 X 10MM CADEIRA ANDRIA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 60,
    "setup": 900,
    "codigo_barra": 55395
  },
  {
    "id_erp": 64601,
    "nome": "ASSENTO PRENSADO A0531 450 X 450 X 10MM (BANQUETA DELTA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 43,
    "setup": 900,
    "codigo_barra": 64601
  },
  {
    "id_erp": 69180,
    "nome": "ASSENTO PRENSADO A0545 450 X 475 X 18MM (BANQUETA GIRATORIA PIER)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 92,
    "setup": 900,
    "codigo_barra": 69180
  },
  {
    "id_erp": 61908,
    "nome": "ASSENTO PRENSADO LAM A0025 470 X 450 X 12,6MM (CAD. EMILY MODELO NOVO)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 60,
    "setup": 900,
    "codigo_barra": 61908
  },
  {
    "id_erp": 48455,
    "nome": "ASSENTO PRENSADO LAM A0069 570 X 480 X 15,7MM (POLTRONA MALBEC)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 186,
    "setup": 900,
    "codigo_barra": 48455
  },
  {
    "id_erp": 57019,
    "nome": "ASSENTO PRENSADO LAM A0511 470 X 450 X 12,6MM (CADEIRA ÁGATA LAMINADA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 60,
    "setup": 900,
    "codigo_barra": 57019
  },
  {
    "id_erp": 71467,
    "nome": "ASSENTO PRENSADO LAM A0515 482 X 430 X 17,4MM - BANQUETA STEIN",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 600,
    "setup": 900,
    "codigo_barra": 71467
  },
  {
    "id_erp": 65942,
    "nome": "ASSENTO PRENSADO LAM A0534 475 X 475 X 21,5MM (CADEIRA BAIA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 63,
    "setup": 900,
    "codigo_barra": 65942
  },
  {
    "id_erp": 43868,
    "nome": "ASSENTO PRENSADO LAMINADO A0007 420 X 300 X 28MM - (BANQUETA MANARI)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 100,
    "setup": 1200,
    "codigo_barra": 43868
  },
  {
    "id_erp": 64249,
    "nome": "ASSENTO PRENSADO MAD A0530 403 X 367 X 128MM - BANQUETA ETOS",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.414,
    "setup": 900,
    "codigo_barra": 64249
  },
  {
    "id_erp": 68137,
    "nome": "ASSENTO PRENSADO MADEIRA 475 X 475 X 32MM (CADEIRA BAIA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 180,
    "setup": 900,
    "codigo_barra": 68137
  },
  {
    "id_erp": 58791,
    "nome": "ASSENTO PRENSADO TAP - CADEIRA LINA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 29,
    "setup": 900,
    "codigo_barra": 58791
  },
  {
    "id_erp": 79602,
    "nome": "ASSENTO PRENSADO TAP 452 X 485 X 14MM (CADEIRA ANGA C/ BR)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 72,
    "setup": 900,
    "codigo_barra": 79602
  },
  {
    "id_erp": 58821,
    "nome": "ASSENTO PRENSADO TAP 482 X 430 X 10MM (BANQUETA LIA LX) NOVO",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 30,
    "setup": 900,
    "codigo_barra": 58821
  },
  {
    "id_erp": 57486,
    "nome": "ASSENTO PRENSADO TAP 490 X 490 X 14MM (CADEIRA DELTA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 25,
    "setup": 1500,
    "codigo_barra": 57486
  },
  {
    "id_erp": 79223,
    "nome": "ASSENTO PRENSADO TAP 4D3639Y 461 X 472 X 8,4MM (CADEIRA PINDORAMA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 60,
    "setup": 900,
    "codigo_barra": 79223
  },
  {
    "id_erp": 80610,
    "nome": "ASSENTO PRENSADO TAP 510 X 550 X 8,4MM (CADEIRA MALBEC 2.0)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 186,
    "setup": 900,
    "codigo_barra": 80610
  },
  {
    "id_erp": 83797,
    "nome": "ASSENTO PRENSADO TAP 550 X 483 X 8,4MM (POLTRONA MALBEC 2.0)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 186,
    "setup": 900,
    "codigo_barra": 83797
  },
  {
    "id_erp": 61910,
    "nome": "ASSENTO PRENSADO TAP A0026 470 X 450 X 3,9MM (CAD. EMILY MODELO NOVO)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 60,
    "setup": 900,
    "codigo_barra": 61910
  },
  {
    "id_erp": 41890,
    "nome": "ASSENTO PRENSADO TAP A0037 495 X 485 X 8,4MM - (CAD. LIA/LIA LX)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 60,
    "setup": 900,
    "codigo_barra": 41890
  },
  {
    "id_erp": 56753,
    "nome": "ASSENTO PRENSADO TAP A0509 470 X 450 X 12,4MM (CADEIRA ÁGATA TAP)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 60,
    "setup": 900,
    "codigo_barra": 56753
  },
  {
    "id_erp": 61813,
    "nome": "ASSENTO PRENSADO TAP A0510 470 X 450 X 3,9MM (CAPA CADEIRA ÁGATA TAP/LAM)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 60,
    "setup": 900,
    "codigo_barra": 61813
  },
  {
    "id_erp": 61912,
    "nome": "ASSENTO PRENSADO TAP A0523 470 X 450 X 12,4MM (CAD. EMILY MODELO NOVO)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 60,
    "setup": 900,
    "codigo_barra": 61912
  },
  {
    "id_erp": 62934,
    "nome": "ASSENTO PRENSADO TAP A0525 496 X 452 X 14MM (CADEIRA VILAR TAPECADA/ RATAN TAPECADA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 90,
    "setup": 900,
    "codigo_barra": 62934
  },
  {
    "id_erp": 63056,
    "nome": "ASSENTO PRENSADO TAP A0529 545 X 400 X 15MM - PUFF PAOLA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 72,
    "setup": 900,
    "codigo_barra": 63056
  },
  {
    "id_erp": 64697,
    "nome": "ASSENTO PRENSADO TAP A0532 450 X 430 X 10MM (CADEIRA TALITA LX)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 37,
    "setup": 900,
    "codigo_barra": 64697
  },
  {
    "id_erp": 65941,
    "nome": "ASSENTO PRENSADO TAP A0533 470 X 470 X 10MM (CADEIRA BAIA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 29,
    "setup": 900,
    "codigo_barra": 65941
  },
  {
    "id_erp": 66451,
    "nome": "ASSENTO PRENSADO TAP A0536 465 X 475 X 8,4MM",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 30,
    "setup": 900,
    "codigo_barra": 66451
  },
  {
    "id_erp": 71928,
    "nome": "ASSENTO PRENSADO TAP P0047 461 X 472 X 14MM (CADEIRA ANGA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 72,
    "setup": 900,
    "codigo_barra": 71928
  },
  {
    "id_erp": 39370,
    "nome": "ASSENTO TAP (CONCHA) P0026 470 X 450 X 12MM - (CAD. EMILY E IBIZA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 60,
    "setup": 900,
    "codigo_barra": 39370
  },
  {
    "id_erp": 38898,
    "nome": "ASSENTO TAP (INTERNO) MDF P0027 440 X 350 X 2,8MM - (CAD. ELIMY E IBIZA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 60,
    "setup": 900,
    "codigo_barra": 38898
  },
  {
    "id_erp": 38865,
    "nome": "ASSENTO TAP P0025 470 X 440 X 8 MM - (CAD. MARROCOS)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 60,
    "setup": 1500,
    "codigo_barra": 38865
  },
  {
    "id_erp": 76310,
    "nome": "ASSENTP PRENSADO TAP FB38384 450X480X9MM - BANQUETA ADHARA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 128,
    "setup": 900,
    "codigo_barra": 76310
  },
  {
    "id_erp": 74760,
    "nome": "ASSENTRO PRENSADO TAP 9D76481 390 X 440 X 14MM BANQUETA VILAR TAPECADA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 300,
    "setup": 900,
    "codigo_barra": 74760
  },
  {
    "id_erp": 53740,
    "nome": "BANCO TANGO MAIOR",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 330,
    "setup": 1500,
    "codigo_barra": 53740
  },
  {
    "id_erp": 53741,
    "nome": "BANCO TANGO MENOR",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 310,
    "setup": 1500,
    "codigo_barra": 53741
  },
  {
    "id_erp": 4444,
    "nome": "BANDEJA - SOFA ITAMBE",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 60,
    "setup": 600,
    "codigo_barra": 4444
  },
  {
    "id_erp": 65664,
    "nome": "BANDEJA CAMA NUVEM",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 480,
    "setup": 900,
    "codigo_barra": 65664
  },
  {
    "id_erp": 72470,
    "nome": "BANDEJA LAMINADA 400 X 470 X 15MM (BANCO BARU)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 600,
    "setup": 900,
    "codigo_barra": 72470
  },
  {
    "id_erp": 70004,
    "nome": "BANDEJA SOFA CAMA GAVEA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 600,
    "setup": 900,
    "codigo_barra": 70004
  },
  {
    "id_erp": 59098,
    "nome": "BANDEJA SOFÁ LEGACY",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 150,
    "setup": 1500,
    "codigo_barra": 59098
  },
  {
    "id_erp": 53739,
    "nome": "BANQUETA TANGO",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 335,
    "setup": 1500,
    "codigo_barra": 53739
  },
  {
    "id_erp": 31717,
    "nome": "BAR  ARGOS",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 260,
    "setup": 900,
    "codigo_barra": 31717
  },
  {
    "id_erp": 36029,
    "nome": "BAR  ORION",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 225,
    "setup": 900,
    "codigo_barra": 36029
  },
  {
    "id_erp": 54903,
    "nome": "BAR TAMBORE",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 460,
    "setup": 900,
    "codigo_barra": 54903
  },
  {
    "id_erp": 84272,
    "nome": "BAR TAMBORE 1300 - MEDIDA ESPECIAL",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 460,
    "setup": 900,
    "codigo_barra": 84272
  },
  {
    "id_erp": 83350,
    "nome": "BAR TAMBORE 1350 - MEDIDA ESPECIAL",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 460,
    "setup": 900,
    "codigo_barra": 83350
  },
  {
    "id_erp": 61136,
    "nome": "BASE MDF 620 X 510 X 15MM - PUFF JOLIE",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 50,
    "setup": 900,
    "codigo_barra": 61136
  },
  {
    "id_erp": 62964,
    "nome": "BASE MONTADA - CADEIRA JOLIE",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 780,
    "setup": 900,
    "codigo_barra": 62964
  },
  {
    "id_erp": 62994,
    "nome": "BASE MONTADA - CADEIRA JOLIE GIRATORIA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 780,
    "setup": 900,
    "codigo_barra": 62994
  },
  {
    "id_erp": 61167,
    "nome": "BASE MONTADA - POLTRONA JOLIE",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 780,
    "setup": 900,
    "codigo_barra": 61167
  },
  {
    "id_erp": 61135,
    "nome": "BASE MONTADA - PUFF JOLIE",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 780,
    "setup": 900,
    "codigo_barra": 61135
  },
  {
    "id_erp": 74430,
    "nome": "BASE MONTADA PINTADA P/ ESTOFADO CERRADO 2800 MESA 400 (C/ MESA APOIO)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 900,
    "setup": 900,
    "codigo_barra": 74430
  },
  {
    "id_erp": 81499,
    "nome": "BASE MONTADA PINTADA P/ESTOFADO ARENA 1600 X 1000 C/ BANDEJA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 180,
    "setup": 900,
    "codigo_barra": 81499
  },
  {
    "id_erp": 81498,
    "nome": "BASE MONTADA PINTADA P/ESTOFADO ARENA 2000 X 1000 C/ BANDEJA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 180,
    "setup": 900,
    "codigo_barra": 81498
  },
  {
    "id_erp": 74809,
    "nome": "BASE MONTADA PINTADA P/ESTOFADO ARENA 2000 X 800",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 600,
    "setup": 900,
    "codigo_barra": 74809
  },
  {
    "id_erp": 70675,
    "nome": "BASE MONTADA PINTADA P/ESTOFADO ARENA 2300 X 1000",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 300,
    "setup": 900,
    "codigo_barra": 70675
  },
  {
    "id_erp": 81438,
    "nome": "BASE MONTADA PINTADA P/ESTOFADO ARENA 2300 X 1000 C/ BANDEJA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 180,
    "setup": 900,
    "codigo_barra": 81438
  },
  {
    "id_erp": 70648,
    "nome": "BASE MONTADA PINTADA P/ESTOFADO ARENA 2300 X 1300",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 300,
    "setup": 900,
    "codigo_barra": 70648
  },
  {
    "id_erp": 70676,
    "nome": "BASE MONTADA PINTADA P/ESTOFADO ARENA 2300 X 800",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 300,
    "setup": 900,
    "codigo_barra": 70676
  },
  {
    "id_erp": 60704,
    "nome": "BASE MONTADA PINTADA P/ESTOFADO ARENA 2500 X 1000",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 600,
    "setup": 900,
    "codigo_barra": 60704
  },
  {
    "id_erp": 74805,
    "nome": "BASE MONTADA PINTADA P/ESTOFADO ARENA 2600 X 1000",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 600,
    "setup": 900,
    "codigo_barra": 74805
  },
  {
    "id_erp": 79646,
    "nome": "BASE MONTADA PINTADA P/ESTOFADO ARENA 800 X 800",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 183,
    "setup": 900,
    "codigo_barra": 79646
  },
  {
    "id_erp": 74601,
    "nome": "BASE MONTADA PINTADA P/ESTOFADO ARENA 900 X 900 C/ GIR",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 600,
    "setup": 900,
    "codigo_barra": 74601
  },
  {
    "id_erp": 74461,
    "nome": "BASE MONTADA PINTADA P/ESTOFADO CERRADO 1200",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 600,
    "setup": 900,
    "codigo_barra": 74461
  },
  {
    "id_erp": 74416,
    "nome": "BASE MONTADA PINTADA P/ESTOFADO CERRADO 1400",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 600,
    "setup": 900,
    "codigo_barra": 74416
  },
  {
    "id_erp": 74417,
    "nome": "BASE MONTADA PINTADA P/ESTOFADO CERRADO 1400 MESA 400",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 600,
    "setup": 900,
    "codigo_barra": 74417
  },
  {
    "id_erp": 74419,
    "nome": "BASE MONTADA PINTADA P/ESTOFADO CERRADO 1600 MESA 400",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 600,
    "setup": 900,
    "codigo_barra": 74419
  },
  {
    "id_erp": 74420,
    "nome": "BASE MONTADA PINTADA P/ESTOFADO CERRADO 2000",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 600,
    "setup": 900,
    "codigo_barra": 74420
  },
  {
    "id_erp": 74421,
    "nome": "BASE MONTADA PINTADA P/ESTOFADO CERRADO 2000 MESA 1000",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 600,
    "setup": 900,
    "codigo_barra": 74421
  },
  {
    "id_erp": 74512,
    "nome": "BASE MONTADA PINTADA P/ESTOFADO CERRADO 2000 MESA 400",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 600,
    "setup": 900,
    "codigo_barra": 74512
  },
  {
    "id_erp": 74422,
    "nome": "BASE MONTADA PINTADA P/ESTOFADO CERRADO 2200",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 600,
    "setup": 900,
    "codigo_barra": 74422
  },
  {
    "id_erp": 74423,
    "nome": "BASE MONTADA PINTADA P/ESTOFADO CERRADO 2200 MESA 400",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 600,
    "setup": 900,
    "codigo_barra": 74423
  },
  {
    "id_erp": 74424,
    "nome": "BASE MONTADA PINTADA P/ESTOFADO CERRADO 2200 X 1000 MESA 1000",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 300,
    "setup": 900,
    "codigo_barra": 74424
  },
  {
    "id_erp": 74425,
    "nome": "BASE MONTADA PINTADA P/ESTOFADO CERRADO 2400",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 600,
    "setup": 900,
    "codigo_barra": 74425
  },
  {
    "id_erp": 74426,
    "nome": "BASE MONTADA PINTADA P/ESTOFADO CERRADO 2400 MESA 400",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 600,
    "setup": 900,
    "codigo_barra": 74426
  },
  {
    "id_erp": 74427,
    "nome": "BASE MONTADA PINTADA P/ESTOFADO CERRADO 2600",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 600,
    "setup": 900,
    "codigo_barra": 74427
  },
  {
    "id_erp": 74428,
    "nome": "BASE MONTADA PINTADA P/ESTOFADO CERRADO 2600 MESA 400",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 600,
    "setup": 900,
    "codigo_barra": 74428
  },
  {
    "id_erp": 74429,
    "nome": "BASE MONTADA PINTADA P/ESTOFADO CERRADO 2800",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 600,
    "setup": 900,
    "codigo_barra": 74429
  },
  {
    "id_erp": 75476,
    "nome": "BASE MONTADA PINTADA P/ESTOFADO CHAISE CERRADO 1400",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 600,
    "setup": 900,
    "codigo_barra": 75476
  },
  {
    "id_erp": 74433,
    "nome": "BASE MONTADA PINTADA P/ESTOFADO CHAISE CERRADO 1400 MESA 400",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 600,
    "setup": 900,
    "codigo_barra": 74433
  },
  {
    "id_erp": 45566,
    "nome": "BASE MONTADA PINTADA P/ESTOFADO ITAMBE 1200",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 100,
    "setup": 600,
    "codigo_barra": 45566
  },
  {
    "id_erp": 45111,
    "nome": "BASE MONTADA PINTADA P/ESTOFADO ITAMBE 1400",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 50,
    "setup": 600,
    "codigo_barra": 45111
  },
  {
    "id_erp": 45693,
    "nome": "BASE MONTADA PINTADA P/ESTOFADO ITAMBE 1770",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 50,
    "setup": 600,
    "codigo_barra": 45693
  },
  {
    "id_erp": 45107,
    "nome": "BASE MONTADA PINTADA P/ESTOFADO ITAMBE 2170",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 50,
    "setup": 600,
    "codigo_barra": 45107
  },
  {
    "id_erp": 45109,
    "nome": "BASE MONTADA PINTADA P/ESTOFADO ITAMBE 2200",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 50,
    "setup": 600,
    "codigo_barra": 45109
  },
  {
    "id_erp": 45110,
    "nome": "BASE MONTADA PINTADA P/ESTOFADO ITAMBE 2400",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 100,
    "setup": 600,
    "codigo_barra": 45110
  },
  {
    "id_erp": 57612,
    "nome": "BASE MONTADA PINTADA P/ESTOFADO ITAMBE CHAISE 1120 E/D",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 50,
    "setup": 600,
    "codigo_barra": 57612
  },
  {
    "id_erp": 74359,
    "nome": "BASE MONTADA PINTADA P/ESTOFADO PUFF ROCHE 800",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 600,
    "setup": 900,
    "codigo_barra": 74359
  },
  {
    "id_erp": 74432,
    "nome": "BASE MONTADA PINTADA P/PUFF CERRADO 1000",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 600,
    "setup": 900,
    "codigo_barra": 74432
  },
  {
    "id_erp": 58131,
    "nome": "BASE MONTADA POLTRONA DALVA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 155,
    "setup": 900,
    "codigo_barra": 58131
  },
  {
    "id_erp": 58132,
    "nome": "BASE MONTADA POLTRONA DALVA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 155,
    "setup": 900,
    "codigo_barra": 58132
  },
  {
    "id_erp": 79893,
    "nome": "BASE MONTADA SELADA - MESA CENTRO GRAVITA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.5,
    "setup": 900,
    "codigo_barra": 79893
  },
  {
    "id_erp": 65752,
    "nome": "BIOMBO MACAU",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.02,
    "setup": 900,
    "codigo_barra": 65752
  },
  {
    "id_erp": 30422,
    "nome": "BOMBE VERSALHES C/ GAVETA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 540,
    "setup": 1200,
    "codigo_barra": 30422
  },
  {
    "id_erp": 30421,
    "nome": "BOMBE VERSALHES C/ PORTA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 540,
    "setup": 1200,
    "codigo_barra": 30421
  },
  {
    "id_erp": 3333,
    "nome": "BRAÇOS - SOFA ITAMBE",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 50,
    "setup": 600,
    "codigo_barra": 3333
  },
  {
    "id_erp": 23680,
    "nome": "BUFFET ARBO 1,80",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 505,
    "setup": 1500,
    "codigo_barra": 23680
  },
  {
    "id_erp": 236809,
    "nome": "BUFFET ARBO 1,80",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 550,
    "setup": 1800,
    "codigo_barra": 236809
  },
  {
    "id_erp": 36607,
    "nome": "BUFFET BERLIM 1,80",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 335,
    "setup": 900,
    "codigo_barra": 36607
  },
  {
    "id_erp": 36394,
    "nome": "BUFFET BERLIM 2,00",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 335,
    "setup": 900,
    "codigo_barra": 36394
  },
  {
    "id_erp": 43401,
    "nome": "BUFFET KLINT 2,20",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 490,
    "setup": 900,
    "codigo_barra": 43401
  },
  {
    "id_erp": 14759,
    "nome": "BUFFET LUANDA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 130,
    "setup": 900,
    "codigo_barra": 14759
  },
  {
    "id_erp": 36608,
    "nome": "BUFFET NAPOLES 1,80",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 175,
    "setup": 900,
    "codigo_barra": 36608
  },
  {
    "id_erp": 36395,
    "nome": "BUFFET NAPOLES 2,00",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 175,
    "setup": 900,
    "codigo_barra": 36395
  },
  {
    "id_erp": 62247,
    "nome": "BUFFET NAPOLES 2,40",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 175,
    "setup": 900,
    "codigo_barra": 62247
  },
  {
    "id_erp": 36413,
    "nome": "BUFFET ORION 1,80",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 225,
    "setup": 900,
    "codigo_barra": 36413
  },
  {
    "id_erp": 36328,
    "nome": "BUFFET ORION 2,20",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 225,
    "setup": 900,
    "codigo_barra": 36328
  },
  {
    "id_erp": 37765,
    "nome": "BUFFET PIETRA 2,00",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 30,
    "setup": 900,
    "codigo_barra": 37765
  },
  {
    "id_erp": 37621,
    "nome": "BUFFET PIETRA 2,40",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 30,
    "setup": 900,
    "codigo_barra": 37621
  },
  {
    "id_erp": 46233,
    "nome": "BUFFET TAMBORE 1,85",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 990,
    "setup": 900,
    "codigo_barra": 46233
  },
  {
    "id_erp": 46238,
    "nome": "BUFFET TAMBORE 2,10",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 900,
    "setup": 900,
    "codigo_barra": 46238
  },
  {
    "id_erp": 46237,
    "nome": "BUFFET TAMBORE 2,40",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 900,
    "setup": 900,
    "codigo_barra": 46237
  },
  {
    "id_erp": 43155,
    "nome": "BUFFET VEDRA 2,20",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 195,
    "setup": 1500,
    "codigo_barra": 43155
  },
  {
    "id_erp": 61522,
    "nome": "BUFFET VEDRA LX 1,80",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 195,
    "setup": 1500,
    "codigo_barra": 61522
  },
  {
    "id_erp": 61524,
    "nome": "BUFFET VEDRA LX 2,20",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 195,
    "setup": 1500,
    "codigo_barra": 61524
  },
  {
    "id_erp": 35688,
    "nome": "COLUNA CECI",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 930,
    "setup": 900,
    "codigo_barra": 35688
  },
  {
    "id_erp": 38711,
    "nome": "COLUNA DUNA PLUS",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 460,
    "setup": 900,
    "codigo_barra": 38711
  },
  {
    "id_erp": 36268,
    "nome": "COLUNA ELIS",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 180,
    "setup": 900,
    "codigo_barra": 36268
  },
  {
    "id_erp": 18192,
    "nome": "COLUNA GENOVA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 330,
    "setup": 900,
    "codigo_barra": 18192
  },
  {
    "id_erp": 35876,
    "nome": "COLUNA NINA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 445,
    "setup": 900,
    "codigo_barra": 35876
  },
  {
    "id_erp": 28735,
    "nome": "COLUNA OLIVA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 640,
    "setup": 900,
    "codigo_barra": 28735
  },
  {
    "id_erp": 35256,
    "nome": "COLUNA ORNATA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 210,
    "setup": 900,
    "codigo_barra": 35256
  },
  {
    "id_erp": 11461,
    "nome": "COLUNA PANTHEON",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 315,
    "setup": 1500,
    "codigo_barra": 11461
  },
  {
    "id_erp": 14097,
    "nome": "COLUNA PANTHEON PLUS",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 410,
    "setup": 1500,
    "codigo_barra": 14097
  },
  {
    "id_erp": 25,
    "nome": "COLUNA PIAZA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 175,
    "setup": 900,
    "codigo_barra": 25
  },
  {
    "id_erp": 48332,
    "nome": "COLUNA TANGO",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 980,
    "setup": 900,
    "codigo_barra": 48332
  },
  {
    "id_erp": 27665,
    "nome": "COLUNA TREVI ESPELHADA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 315,
    "setup": 900,
    "codigo_barra": 27665
  },
  {
    "id_erp": 31976,
    "nome": "COLUNA VICENZA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 400,
    "setup": 900,
    "codigo_barra": 31976
  },
  {
    "id_erp": 32923,
    "nome": "COLUNA VICENZA 1,20",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 400,
    "setup": 900,
    "codigo_barra": 32923
  },
  {
    "id_erp": 62023,
    "nome": "CONCHA MONTADA LAMINADA 950 X 470 X 18,4MM (CADEIRA AGATA LAMINADA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 120,
    "setup": 900,
    "codigo_barra": 62023
  },
  {
    "id_erp": 62025,
    "nome": "CONCHA MONTADA LAMINADA C0004 950 X 470 X 18,4MM (CAD. EMILY LAMINADA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 120,
    "setup": 900,
    "codigo_barra": 62025
  },
  {
    "id_erp": 62022,
    "nome": "CONCHA MONTADA TAPECADA 950 X 470 X 18MM (CAD. AGATA TAPEÇADA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 120,
    "setup": 900,
    "codigo_barra": 62022
  },
  {
    "id_erp": 62024,
    "nome": "CONCHA MONTADA TAPECADA C0003 950 X 470 X 18MM (CAD. EMILY TAPEÇADA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 120,
    "setup": 900,
    "codigo_barra": 62024
  },
  {
    "id_erp": 63498,
    "nome": "CONCHA PRENSADA TAP 810 X 470 X 11,7MM (CADEIRA MANU GIRATORIA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 100,
    "setup": 900,
    "codigo_barra": 63498
  },
  {
    "id_erp": 57515,
    "nome": "CURVA MAD C0009 212 X 75 X 45MM - MESA JANTAR UOMINI LX (470 X 72 X 50MM)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 68,
    "setup": 900,
    "codigo_barra": 57515
  },
  {
    "id_erp": 23317,
    "nome": "ENCOSTO COMP FLEX OVO CAD ENNA 360 X 320 X 3 MM - (CAD. ENNA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 72,
    "setup": 900,
    "codigo_barra": 23317
  },
  {
    "id_erp": 233801,
    "nome": "ENCOSTO LACA CAD ENNA E0049 500 X 460 X 20 MM - (CAD. ENNA RATAN)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 75,
    "setup": 1500,
    "codigo_barra": 233801
  },
  {
    "id_erp": 23380,
    "nome": "ENCOSTO LACA CAD ENNA E0049 500 X 460 X 20 MM - (CAD. ENNA TAPEÇADA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 135,
    "setup": 1500,
    "codigo_barra": 23380
  },
  {
    "id_erp": 38895,
    "nome": "ENCOSTO LAM (CONCHA) P0213 500 X 470 X 12MM - (CAD. EMILY LAMINADA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 60,
    "setup": 900,
    "codigo_barra": 38895
  },
  {
    "id_erp": 39267,
    "nome": "ENCOSTO LAM P0219 467 X 454 X 9 MM - (CAD. MARROCOS LAM)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 60,
    "setup": 1500,
    "codigo_barra": 39267
  },
  {
    "id_erp": 233121,
    "nome": "ENCOSTO LAMINADO CAD ENNA E0049 500 X 460 X 20 MM - (CAD. ENNA RATAN)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 75,
    "setup": 1500,
    "codigo_barra": 233121
  },
  {
    "id_erp": 23312,
    "nome": "ENCOSTO LAMINADO CAD ENNA E0049 500 X 460 X 20 MM - (CAD. ENNA TAPEÇADA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 135,
    "setup": 1500,
    "codigo_barra": 23312
  },
  {
    "id_erp": 45117,
    "nome": "ENCOSTO LAMINADO E0001 700 X 700 X 15MM - (BANQUETA LIA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 60,
    "setup": 900,
    "codigo_barra": 45117
  },
  {
    "id_erp": 42800,
    "nome": "ENCOSTO LAMINADO E0001 700 X 700 X 15MM - (CAD. LIA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 60,
    "setup": 900,
    "codigo_barra": 42800
  },
  {
    "id_erp": 42798,
    "nome": "ENCOSTO LAMINADO E0226 500 X 500 X 16MM (CAD. CLAU LAM) - MASTER",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 60,
    "setup": 900,
    "codigo_barra": 42798
  },
  {
    "id_erp": 42799,
    "nome": "ENCOSTO LAMINADO E0234 500 X 500 X 10MM (CAD. CLAU TAP.)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 60,
    "setup": 900,
    "codigo_barra": 42799
  },
  {
    "id_erp": 33328,
    "nome": "ENCOSTO LAMINADO SELADO E0045 204 X 255 X 2,8MM",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 65,
    "setup": 1500,
    "codigo_barra": 33328
  },
  {
    "id_erp": 38827,
    "nome": "ENCOSTO MAIOR PRENSADO P0210 520 X 440 X 12MM - MASTER (CAD. SOFIA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 30,
    "setup": 900,
    "codigo_barra": 38827
  },
  {
    "id_erp": 61180,
    "nome": "ENCOSTO MDF 480 X 516 X 15MM - POLTRONA JOLIE",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.2,
    "setup": 900,
    "codigo_barra": 61180
  },
  {
    "id_erp": 35339,
    "nome": "ENCOSTO MDF CAD UNA 630 X 440 X 2,8 MM (4 PEÇAS) - (CAD. UNA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 40,
    "setup": 1500,
    "codigo_barra": 35339
  },
  {
    "id_erp": 61645,
    "nome": "ENCOSTO MDF E0347 600 X 410 X 2,8MM - POLTRONA COPAN",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 600,
    "setup": 0,
    "codigo_barra": 61645
  },
  {
    "id_erp": 63130,
    "nome": "ENCOSTO MDF E0360 435 X 359 X 20MM (POLTRONA PAOLA - ROUTER)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.38,
    "setup": 0,
    "codigo_barra": 63130
  },
  {
    "id_erp": 38764,
    "nome": "ENCOSTO MENOR PRENSADO P0209 490 X 415 X 12MM - MASTER (CAD. SOFIA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 30,
    "setup": 900,
    "codigo_barra": 38764
  },
  {
    "id_erp": 57485,
    "nome": "ENCOSTO MONTADO - CADEIRA DELTA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 600,
    "setup": 1500,
    "codigo_barra": 57485
  },
  {
    "id_erp": 45101,
    "nome": "ENCOSTO PRENSADO E0245 500 X 300 X 10MM (CAD. LAURA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 60,
    "setup": 900,
    "codigo_barra": 45101
  },
  {
    "id_erp": 45487,
    "nome": "ENCOSTO PRENSADO E0250 810 X 470 X 11,7MM (CAD. MANU/MANU GIRATORIA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 100,
    "setup": 900,
    "codigo_barra": 45487
  },
  {
    "id_erp": 45661,
    "nome": "ENCOSTO PRENSADO E0253 440 X 460 X 18MM (CADEIRA DALIA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 30,
    "setup": 900,
    "codigo_barra": 45661
  },
  {
    "id_erp": 46869,
    "nome": "ENCOSTO PRENSADO E0273 875 X 480 X 11,7MM (CAD. NANDA/NANDA GIRATORIA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 100,
    "setup": 900,
    "codigo_barra": 46869
  },
  {
    "id_erp": 47711,
    "nome": "ENCOSTO PRENSADO E0283 565 X 440 X 12MM (CAD. JADE/ARIEL/ESTER)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 60,
    "setup": 900,
    "codigo_barra": 47711
  },
  {
    "id_erp": 50914,
    "nome": "ENCOSTO PRENSADO E0304 430 X 600 X 15MM POLTRONA BARBARA (EXTERNO)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 40,
    "setup": 900,
    "codigo_barra": 50914
  },
  {
    "id_erp": 50915,
    "nome": "ENCOSTO PRENSADO E0305 830 X 580 X 10MM POLTRONA BARBARA (INTERNO)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 40,
    "setup": 900,
    "codigo_barra": 50915
  },
  {
    "id_erp": 50971,
    "nome": "ENCOSTO PRENSADO E0306 455 X 210 X 20MM (CADEIRA PAOLA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 40,
    "setup": 900,
    "codigo_barra": 50971
  },
  {
    "id_erp": 51988,
    "nome": "ENCOSTO PRENSADO E0313 455 X 210 X 20MM BANQUETA PAOLA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 40,
    "setup": 900,
    "codigo_barra": 51988
  },
  {
    "id_erp": 54254,
    "nome": "ENCOSTO PRENSADO E0320 875 X 480 X 11,7MM (CAD. MONACO / MONACO C/ BRACO)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 40,
    "setup": 900,
    "codigo_barra": 54254
  },
  {
    "id_erp": 54819,
    "nome": "ENCOSTO PRENSADO E0322 480 X 470 X 10MM CADEIRA TALITA (LAMINA CRUZADA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 60,
    "setup": 900,
    "codigo_barra": 54819
  },
  {
    "id_erp": 55058,
    "nome": "ENCOSTO PRENSADO E0325 400 X 500 X 14MM  CADEIRA ANDRIA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 60,
    "setup": 900,
    "codigo_barra": 55058
  },
  {
    "id_erp": 55366,
    "nome": "ENCOSTO PRENSADO E0330 700 X 700 X 15MM (CAD. LIA LX C/ BRACO)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 60,
    "setup": 900,
    "codigo_barra": 55366
  },
  {
    "id_erp": 55366,
    "nome": "ENCOSTO PRENSADO E0330 700 X 700 X 15MM (CAD. LIA LX C/ BRACO)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 60,
    "setup": 900,
    "codigo_barra": 55366
  },
  {
    "id_erp": 55366,
    "nome": "ENCOSTO PRENSADO E0330 700 X 700 X 15MM (CAD. LIA LX C/ BRACO)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 60,
    "setup": 900,
    "codigo_barra": 55366
  },
  {
    "id_erp": 61909,
    "nome": "ENCOSTO PRENSADO LAM E0222 500 X 470 X 12,4MM (CAD. EMILY MODELO NOVO)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 60,
    "setup": 900,
    "codigo_barra": 61909
  },
  {
    "id_erp": 48454,
    "nome": "ENCOSTO PRENSADO LAM E0288 570 X 280 X 15,7MM (POLTRONA MALBEC)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 186,
    "setup": 900,
    "codigo_barra": 48454
  },
  {
    "id_erp": 48475,
    "nome": "ENCOSTO PRENSADO LAM E0290 490 X 700 X 17,1MM (CADEIRA STELA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 60,
    "setup": 900,
    "codigo_barra": 48475
  },
  {
    "id_erp": 49206,
    "nome": "ENCOSTO PRENSADO LAM E0291 490 X 700 X 17,1MM (CADEIRA STELA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 60,
    "setup": 900,
    "codigo_barra": 49206
  },
  {
    "id_erp": 48719,
    "nome": "ENCOSTO PRENSADO LAM E0294 490 X 700 X 17,1MM (CADEIRA STELA TAPEÇADA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 60,
    "setup": 900,
    "codigo_barra": 48719
  },
  {
    "id_erp": 52378,
    "nome": "ENCOSTO PRENSADO LAM E0314 700 X 700 X 14,6MM CADEIRA LIA LX LAMINADA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 60,
    "setup": 900,
    "codigo_barra": 52378
  },
  {
    "id_erp": 54157,
    "nome": "ENCOSTO PRENSADO LAM E0317 490 X 700 X 17,1MM CADEIRA STELA LX LAMINADA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 60,
    "setup": 900,
    "codigo_barra": 54157
  },
  {
    "id_erp": 54163,
    "nome": "ENCOSTO PRENSADO LAM E0319 490 X 700 X 17,1MM CADEIRA STELA LX TAPECADA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 60,
    "setup": 900,
    "codigo_barra": 54163
  },
  {
    "id_erp": 54879,
    "nome": "ENCOSTO PRENSADO LAM E0324 400 X 470 X 12,4MM (CADEIRA LUISE LAMINADO)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 40,
    "setup": 900,
    "codigo_barra": 54879
  },
  {
    "id_erp": 55124,
    "nome": "ENCOSTO PRENSADO LAM E0326 700 X 700 X 15MM CADEIRA LIA LX TAPECADA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 60,
    "setup": 900,
    "codigo_barra": 55124
  },
  {
    "id_erp": 55196,
    "nome": "ENCOSTO PRENSADO LAM E0327 700 X 700 X 15MM CADEIRA LIA LX",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 60,
    "setup": 900,
    "codigo_barra": 55196
  },
  {
    "id_erp": 55363,
    "nome": "ENCOSTO PRENSADO LAM E0328 700 X 700 X 17,3MM (CAD. LIA LX LAMINADA C/ BRACO)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 60,
    "setup": 900,
    "codigo_barra": 55363
  },
  {
    "id_erp": 57020,
    "nome": "ENCOSTO PRENSADO LAM E0340 500 X 470 X 12,4MM (CADEIRA ÁGATA LAMINADA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 60,
    "setup": 900,
    "codigo_barra": 57020
  },
  {
    "id_erp": 39180,
    "nome": "ENCOSTO PRENSADO P0217 470 X 435 X 8MM - (CAD. DUDA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 30,
    "setup": 900,
    "codigo_barra": 39180
  },
  {
    "id_erp": 58790,
    "nome": "ENCOSTO PRENSADO TAP - CADEIRA LINA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 29,
    "setup": 1500,
    "codigo_barra": 58790
  },
  {
    "id_erp": 62963,
    "nome": "ENCOSTO PRENSADO TAP 1030 X 490 X 15MM (CADEIRA JOLIE)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 226,
    "setup": 900,
    "codigo_barra": 62963
  },
  {
    "id_erp": 79235,
    "nome": "ENCOSTO PRENSADO TAP 5MO3437 490 X 180 X 8,4MM (CADEIRA PINDORAMA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 60,
    "setup": 900,
    "codigo_barra": 79235
  },
  {
    "id_erp": 80644,
    "nome": "ENCOSTO PRENSADO TAP 633 X 266 X 15MM (CADEIRA MALBEC 2.0)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 186,
    "setup": 900,
    "codigo_barra": 80644
  },
  {
    "id_erp": 80612,
    "nome": "ENCOSTO PRENSADO TAP 633 X 310 X 15MM (POLTRONA MALBEC 2.0)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 186,
    "setup": 900,
    "codigo_barra": 80612
  },
  {
    "id_erp": 61178,
    "nome": "ENCOSTO PRENSADO TAP 650 X 400 X 15MM - POLTRONA JOLIE",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 120,
    "setup": 900,
    "codigo_barra": 61178
  },
  {
    "id_erp": 61911,
    "nome": "ENCOSTO PRENSADO TAP E0214 500 X 470 X 3,9MM (CAD. EMILY MODELO NOVO)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 60,
    "setup": 900,
    "codigo_barra": 61911
  },
  {
    "id_erp": 49209,
    "nome": "ENCOSTO PRENSADO TAP E0292 570 X 280 X 15,1MM (POLTRONA MALBEC)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 186,
    "setup": 900,
    "codigo_barra": 49209
  },
  {
    "id_erp": 52936,
    "nome": "ENCOSTO PRENSADO TAP E0315 700 X 700 X 15,6MM CADEIRA LIA LX TAP. C/ BRAÇO",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 60,
    "setup": 900,
    "codigo_barra": 52936
  },
  {
    "id_erp": 54265,
    "nome": "ENCOSTO PRENSADO TAP E0321 500 X 500 X 8MM (CADEIRA CLAU LX)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 60,
    "setup": 900,
    "codigo_barra": 54265
  },
  {
    "id_erp": 54876,
    "nome": "ENCOSTO PRENSADO TAP E0323 400 X 470 X 12MM (CADEIRA LUISE TAPECADA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 40,
    "setup": 900,
    "codigo_barra": 54876
  },
  {
    "id_erp": 55365,
    "nome": "ENCOSTO PRENSADO TAP E0329 700 X 700 X 15MM (CAD. LIA LX TAPECADA C/ BRACO)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 60,
    "setup": 900,
    "codigo_barra": 55365
  },
  {
    "id_erp": 56755,
    "nome": "ENCOSTO PRENSADO TAP E0338 500 X 470 X 12,4MM (CADEIRA ÁGATA TAP)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 60,
    "setup": 900,
    "codigo_barra": 56755
  },
  {
    "id_erp": 61814,
    "nome": "ENCOSTO PRENSADO TAP E0339 500 X 470 X 3,9MM (CAPA CADEIRA ÁGATA TAP/LAM)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 60,
    "setup": 900,
    "codigo_barra": 61814
  },
  {
    "id_erp": 61216,
    "nome": "ENCOSTO PRENSADO TAP E0346 570 X 570 X 15MM - POLT CLARITAS",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 140,
    "setup": 900,
    "codigo_barra": 61216
  },
  {
    "id_erp": 61913,
    "nome": "ENCOSTO PRENSADO TAP E0351 500 X 470 X 12,4MM (CAD. EMILY MODELO NOVO)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 60,
    "setup": 900,
    "codigo_barra": 61913
  },
  {
    "id_erp": 62362,
    "nome": "ENCOSTO PRENSADO TAP E0352 467 X 454 X 11MM - CADEIRA MARROCOS TAPECADA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 162,
    "setup": 900,
    "codigo_barra": 62362
  },
  {
    "id_erp": 63127,
    "nome": "ENCOSTO PRENSADO TAP E0357 420 X 600 X 20MM - POLTRONA PAOLA (GABARITO POLT BARBARA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 240,
    "setup": 900,
    "codigo_barra": 63127
  },
  {
    "id_erp": 63128,
    "nome": "ENCOSTO PRENSADO TAP E0358 500 X 100 X 20MM - POLTRONA PAOLA (UNIAO ESQUERDA - GABARITO VEDRA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 240,
    "setup": 900,
    "codigo_barra": 63128
  },
  {
    "id_erp": 63129,
    "nome": "ENCOSTO PRENSADO TAP E0359 500 X 100 X 20MM - POLTRONA PAOLA (UNIAO DIREITA - GABARITO VEDRA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 240,
    "setup": 900,
    "codigo_barra": 63129
  },
  {
    "id_erp": 64699,
    "nome": "ENCOSTO PRENSADO TAP E0364 450 X 430 X 10MM (CADEIRA TALITA LX)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 180,
    "setup": 900,
    "codigo_barra": 64699
  },
  {
    "id_erp": 65940,
    "nome": "ENCOSTO PRENSADO TAP E0365 445 X 165 X 9MM (CADEIRA BAIA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 40,
    "setup": 900,
    "codigo_barra": 65940
  },
  {
    "id_erp": 71789,
    "nome": "ENCOSTO PRENSADO TAP E0387 490 X 156 X 16MM (CADEIRA ANGA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 65,
    "setup": 900,
    "codigo_barra": 71789
  },
  {
    "id_erp": 45178,
    "nome": "ENCOSTO PRESNSADO - (POLTRONA BOTANIC)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 100,
    "setup": 900,
    "codigo_barra": 45178
  },
  {
    "id_erp": 39371,
    "nome": "ENCOSTO TAP (CONCHA) P0213 500 X 470 X 12MM - (CAD. EMILY E IBIZA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 60,
    "setup": 900,
    "codigo_barra": 39371
  },
  {
    "id_erp": 38899,
    "nome": "ENCOSTO TAP (INTERNO) MDF P0214 415 X 320 X 2,8MM - (CAD. EMILY E IBIZA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 60,
    "setup": 900,
    "codigo_barra": 38899
  },
  {
    "id_erp": 38861,
    "nome": "ENCOSTO TAP P0211 467 X 454 8 MM - (CAD. MARROCOS)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 60,
    "setup": 1500,
    "codigo_barra": 38861
  },
  {
    "id_erp": 44429,
    "nome": "ENCOSTO TAPECADO E0002 700 X 650 X 0,045MM - (BANQUETA LIA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 60,
    "setup": 900,
    "codigo_barra": 44429
  },
  {
    "id_erp": 41892,
    "nome": "ENCOSTO TAPECADO E0002 700 X 650 X 0,045MM (CAD. LIA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 60,
    "setup": 900,
    "codigo_barra": 41892
  },
  {
    "id_erp": 42226,
    "nome": "ENCOSTO TAPECADO E0227 500 X 500 X 8MM - (CAD. CLAU TAP)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 60,
    "setup": 900,
    "codigo_barra": 42226
  },
  {
    "id_erp": 53742,
    "nome": "ESCRIVANINHA TANGO",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 465,
    "setup": 1500,
    "codigo_barra": 53742
  },
  {
    "id_erp": 25895,
    "nome": "FUNDO MDF F0006 1500 X 410 X 9MM",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 30,
    "setup": 600,
    "codigo_barra": 25895
  },
  {
    "id_erp": 43926,
    "nome": "HOME THEATER VEDRA 2,20",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 300,
    "setup": 1500,
    "codigo_barra": 43926
  },
  {
    "id_erp": 61526,
    "nome": "HOME VEDRA LX 1,80",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 195,
    "setup": 1500,
    "codigo_barra": 61526
  },
  {
    "id_erp": 61528,
    "nome": "HOME VEDRA LX 2,20",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 195,
    "setup": 1500,
    "codigo_barra": 61528
  },
  {
    "id_erp": 45113,
    "nome": "JOGO DE PES P/ ESTOFADO CHAISE ITAMBE 1000/1100/1280",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 600,
    "setup": 900,
    "codigo_barra": 45113
  },
  {
    "id_erp": 69778,
    "nome": "JOGO DE PES P/ ESTOFADO GAMBOA BIP",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 300,
    "setup": 900,
    "codigo_barra": 69778
  },
  {
    "id_erp": 70684,
    "nome": "JOGO DE PES P/ ESTOFADO GAMBOA MODULO",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 300,
    "setup": 900,
    "codigo_barra": 70684
  },
  {
    "id_erp": 66730,
    "nome": "JOGO DE PES P/ ESTOFADO LAGOA CHAISE",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 300,
    "setup": 900,
    "codigo_barra": 66730
  },
  {
    "id_erp": 67460,
    "nome": "JOGO DE PES P/ ESTOFADO LAGOA CURVO",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 300,
    "setup": 900,
    "codigo_barra": 67460
  },
  {
    "id_erp": 66726,
    "nome": "JOGO DE PES P/ ESTOFADO LAGOA S/ PE CENTRAL",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 300,
    "setup": 900,
    "codigo_barra": 66726
  },
  {
    "id_erp": 73789,
    "nome": "JOGO DE PES P/ ESTOFADO MELIM LIVING BIP",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.2,
    "setup": 900,
    "codigo_barra": 73789
  },
  {
    "id_erp": 68438,
    "nome": "JOGO DE PES P/ ESTOFADO SOFA CAMA GAVEA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 300,
    "setup": 900,
    "codigo_barra": 68438
  },
  {
    "id_erp": 73866,
    "nome": "JOGO DE PES P/ ESTOFADO SOFA CORCOVADO 2500",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 600,
    "setup": 900,
    "codigo_barra": 73866
  },
  {
    "id_erp": 45130,
    "nome": "JOGO DE PES P/ ESTOFADO VALENCIA 2200/2530/2830",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 200,
    "setup": 600,
    "codigo_barra": 45130
  },
  {
    "id_erp": 45129,
    "nome": "JOGO DE PES P/ POLTRONA VALENCIA 1000",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 200,
    "setup": 600,
    "codigo_barra": 45129
  },
  {
    "id_erp": 61578,
    "nome": "KIT LEGACY 2260/2600 - BANDEJA - FERRAGEM - PE CENTRAL",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 150,
    "setup": 1500,
    "codigo_barra": 61578
  },
  {
    "id_erp": 61581,
    "nome": "KIT LEGACY 2900/3200/3600 - BANDEJA - FERRAGEM - PE CENTRAL",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 150,
    "setup": 1500,
    "codigo_barra": 61581
  },
  {
    "id_erp": 61584,
    "nome": "KIT LEGACY 4120 - BANDEJA - FERRAGEM - PE CENTRAL",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 150,
    "setup": 1500,
    "codigo_barra": 61584
  },
  {
    "id_erp": 38828,
    "nome": "LAT COMPENS PINUS DIREITA 460 X 370 X 12 MM (CAD.SOFIA C/BRAÇO)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 40,
    "setup": 900,
    "codigo_barra": 38828
  },
  {
    "id_erp": 57893,
    "nome": "LAT COMPENS PINUS ESQUERDA 460 X 370 X 12 MM (CAD.SOFIA C/BRAÇO)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 40,
    "setup": 900,
    "codigo_barra": 57893
  },
  {
    "id_erp": 56321,
    "nome": "LATERAL MONTADA  ESQUERDA (POLTRONA MALBEC)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 170,
    "setup": 900,
    "codigo_barra": 56321
  },
  {
    "id_erp": 60059,
    "nome": "LATERAL MONTADA DIREITA (POLTRONA COPAN)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 135,
    "setup": 900,
    "codigo_barra": 60059
  },
  {
    "id_erp": 56320,
    "nome": "LATERAL MONTADA DIREITA (POLTRONA MALBEC)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 170,
    "setup": 900,
    "codigo_barra": 56320
  },
  {
    "id_erp": 60058,
    "nome": "LATERAL MONTADA ESQUERDA (POLTRONA COPAN)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 135,
    "setup": 900,
    "codigo_barra": 60058
  },
  {
    "id_erp": 666,
    "nome": "LATERAL POLTRONA CLEO RATAN",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 60,
    "setup": 900,
    "codigo_barra": 666
  },
  {
    "id_erp": 70172,
    "nome": "LATERAL PRENSADA 500 X 720 X 12,6MM GAMBOA TAP",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 127,
    "setup": 900,
    "codigo_barra": 70172
  },
  {
    "id_erp": 46721,
    "nome": "LATERAL PRENSADA LAM L0578 420 X 998 X 12,6MM  (SOFA YARA LAT BRACO)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 50,
    "setup": 900,
    "codigo_barra": 46721
  },
  {
    "id_erp": 73546,
    "nome": "LATERAL PRENSADA LAMINADA B9815K1 420 X 998 X 12,6MM YARA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 80,
    "setup": 900,
    "codigo_barra": 73546
  },
  {
    "id_erp": 70171,
    "nome": "LATERAL PRENSADA LAMINADA L0740 500 X 720 X 12,6MM GAMBOA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 127,
    "setup": 900,
    "codigo_barra": 70171
  },
  {
    "id_erp": 70637,
    "nome": "MESA APOIO ALPI 500 X 550 ALT. T. LACA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 180,
    "setup": 900,
    "codigo_barra": 70637
  },
  {
    "id_erp": 71532,
    "nome": "MESA APOIO ALPI 500 X 550 ALT. T. MAD.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 180,
    "setup": 900,
    "codigo_barra": 71532
  },
  {
    "id_erp": 72957,
    "nome": "MESA APOIO ALPI 700 X 550 ALT. T. LACA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 300,
    "setup": 900,
    "codigo_barra": 72957
  },
  {
    "id_erp": 72954,
    "nome": "MESA APOIO ALPI 700 X 550 ALT. T. MAD.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 300,
    "setup": 900,
    "codigo_barra": 72954
  },
  {
    "id_erp": 83460,
    "nome": "MESA APOIO ALPI 900 X 420 ALT. T.MAD. - MEDIDA ESPECIAL",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 420,
    "setup": 900,
    "codigo_barra": 83460
  },
  {
    "id_erp": 54880,
    "nome": "MESA APOIO ALPI T. LACA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 191,
    "setup": 1800,
    "codigo_barra": 54880
  },
  {
    "id_erp": 38004,
    "nome": "MESA APOIO ALPI T. MAD.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 191,
    "setup": 1800,
    "codigo_barra": 38004
  },
  {
    "id_erp": 64968,
    "nome": "MESA APOIO ALPI T. RECOURO",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 191,
    "setup": 1800,
    "codigo_barra": 64968
  },
  {
    "id_erp": 37518,
    "nome": "MESA APOIO ALPI T. V.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 191,
    "setup": 1800,
    "codigo_barra": 37518
  },
  {
    "id_erp": 63766,
    "nome": "MESA APOIO ARENA 1000 X 1000",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 183,
    "setup": 900,
    "codigo_barra": 63766
  },
  {
    "id_erp": 63765,
    "nome": "MESA APOIO ARENA 1000 X 600",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 183,
    "setup": 900,
    "codigo_barra": 63765
  },
  {
    "id_erp": 53735,
    "nome": "MESA APOIO BALI",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 30,
    "setup": 900,
    "codigo_barra": 53735
  },
  {
    "id_erp": 70812,
    "nome": "MESA APOIO EQUILIBRIO 650 X 500 T. MAD",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.02,
    "setup": 900,
    "codigo_barra": 70812
  },
  {
    "id_erp": 62899,
    "nome": "MESA APOIO ESCHER",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 165,
    "setup": 900,
    "codigo_barra": 62899
  },
  {
    "id_erp": 69801,
    "nome": "MESA APOIO ESCHER T. PEDRA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 165,
    "setup": 900,
    "codigo_barra": 69801
  },
  {
    "id_erp": 53736,
    "nome": "MESA APOIO JAVA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 30,
    "setup": 900,
    "codigo_barra": 53736
  },
  {
    "id_erp": 65929,
    "nome": "MESA APOIO KALA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 237,
    "setup": 900,
    "codigo_barra": 65929
  },
  {
    "id_erp": 72004,
    "nome": "MESA APOIO LIRA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 180,
    "setup": 900,
    "codigo_barra": 72004
  },
  {
    "id_erp": 72004,
    "nome": "MESA APOIO LIRA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 300,
    "setup": 900,
    "codigo_barra": 72004
  },
  {
    "id_erp": 72040,
    "nome": "MESA APOIO LIRA T. PEDRA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 300,
    "setup": 900,
    "codigo_barra": 72040
  },
  {
    "id_erp": 72040,
    "nome": "MESA APOIO LIRA T. PEDRA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 300,
    "setup": 900,
    "codigo_barra": 72040
  },
  {
    "id_erp": 54905,
    "nome": "MESA APOIO LUGO",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 191,
    "setup": 1800,
    "codigo_barra": 54905
  },
  {
    "id_erp": 73501,
    "nome": "MESA APOIO MONTADA P/ESTOFADO CERRADO",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 300,
    "setup": 900,
    "codigo_barra": 73501
  },
  {
    "id_erp": 71978,
    "nome": "MESA APOIO TAIGA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 600,
    "setup": 900,
    "codigo_barra": 71978
  },
  {
    "id_erp": 81978,
    "nome": "MESA APOIO TAIGA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 600,
    "setup": 900,
    "codigo_barra": 81978
  },
  {
    "id_erp": 72263,
    "nome": "MESA APOIO TERESA 530",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 600,
    "setup": 900,
    "codigo_barra": 72263
  },
  {
    "id_erp": 72264,
    "nome": "MESA APOIO TERESA 640",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 600,
    "setup": 900,
    "codigo_barra": 72264
  },
  {
    "id_erp": 77990,
    "nome": "MESA BISTRO BERE",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 420,
    "setup": 900,
    "codigo_barra": 77990
  },
  {
    "id_erp": 83147,
    "nome": "MESA BISTRO BERE 0,80 - MEDIDA ESPECIAL",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 420,
    "setup": 900,
    "codigo_barra": 83147
  },
  {
    "id_erp": 64211,
    "nome": "MESA BISTRO LECCI 1030",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 80,
    "setup": 900,
    "codigo_barra": 64211
  },
  {
    "id_erp": 84394,
    "nome": "MESA BISTRO LECCI 600 - MEDIDA ESPECIAL",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 80,
    "setup": 900,
    "codigo_barra": 84394
  },
  {
    "id_erp": 70910,
    "nome": "MESA BISTRO LECCI 800 - MEDIDA ESPECIAL",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 80,
    "setup": 900,
    "codigo_barra": 70910
  },
  {
    "id_erp": 71052,
    "nome": "MESA CABECEIRA TAMBORE 600",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 600,
    "setup": 900,
    "codigo_barra": 71052
  },
  {
    "id_erp": 71741,
    "nome": "MESA CABECEIRA TAMBORE 800",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 600,
    "setup": 900,
    "codigo_barra": 71741
  },
  {
    "id_erp": 76318,
    "nome": "MESA CABECEIRA VOLPI 550 X 600",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 600,
    "setup": 900,
    "codigo_barra": 76318
  },
  {
    "id_erp": 76319,
    "nome": "MESA CABECEIRA VOLPI 750 X 600",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 600,
    "setup": 900,
    "codigo_barra": 76319
  },
  {
    "id_erp": 27123,
    "nome": "MESA CENTRO AGRES",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 230,
    "setup": 1200,
    "codigo_barra": 27123
  },
  {
    "id_erp": 71302,
    "nome": "MESA CENTRO AGRES - MEDIDA ESPECIAL (CHAMAR SERGIO PARA ACOMPANHAR)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 780,
    "setup": 900,
    "codigo_barra": 71302
  },
  {
    "id_erp": 45316,
    "nome": "MESA CENTRO AGRES T. LAM.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 230,
    "setup": 1200,
    "codigo_barra": 45316
  },
  {
    "id_erp": 67286,
    "nome": "MESA CENTRO ALPI 1,00 T. LACA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 151,
    "setup": 900,
    "codigo_barra": 67286
  },
  {
    "id_erp": 65677,
    "nome": "MESA CENTRO ALPI 1,00 T. MAD.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 151,
    "setup": 900,
    "codigo_barra": 65677
  },
  {
    "id_erp": 54883,
    "nome": "MESA CENTRO ALPI T. LACA 1,20",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 151,
    "setup": 900,
    "codigo_barra": 54883
  },
  {
    "id_erp": 38001,
    "nome": "MESA CENTRO ALPI T. MAD. 1,20",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 151,
    "setup": 900,
    "codigo_barra": 38001
  },
  {
    "id_erp": 37436,
    "nome": "MESA CENTRO ALPI T. V. 1,20",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 151,
    "setup": 900,
    "codigo_barra": 37436
  },
  {
    "id_erp": 54884,
    "nome": "MESA CENTRO ASTI T. LACA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 135,
    "setup": 900,
    "codigo_barra": 54884
  },
  {
    "id_erp": 34492,
    "nome": "MESA CENTRO ASTI T. MAD.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 135,
    "setup": 900,
    "codigo_barra": 34492
  },
  {
    "id_erp": 34491,
    "nome": "MESA CENTRO ASTI T. V.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 135,
    "setup": 900,
    "codigo_barra": 34491
  },
  {
    "id_erp": 36399,
    "nome": "MESA CENTRO BENIM 1,20 LX",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 330,
    "setup": 900,
    "codigo_barra": 36399
  },
  {
    "id_erp": 36396,
    "nome": "MESA CENTRO BENIM 1,40 LX",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 330,
    "setup": 900,
    "codigo_barra": 36396
  },
  {
    "id_erp": 68812,
    "nome": "MESA CENTRO BOCO 1,20",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 791,
    "setup": 900,
    "codigo_barra": 68812
  },
  {
    "id_erp": 68799,
    "nome": "MESA CENTRO BOCO 1,40",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 791,
    "setup": 900,
    "codigo_barra": 68799
  },
  {
    "id_erp": 56165,
    "nome": "MESA CENTRO CAIXA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.66,
    "setup": 3000,
    "codigo_barra": 56165
  },
  {
    "id_erp": 561659,
    "nome": "MESA CENTRO CAIXA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 2.64,
    "setup": 1800,
    "codigo_barra": 561659
  },
  {
    "id_erp": 59048,
    "nome": "MESA CENTRO CAIXA 1,60",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.66,
    "setup": 3000,
    "codigo_barra": 59048
  },
  {
    "id_erp": 45182,
    "nome": "MESA CENTRO CALIANDRA 1,50",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 220,
    "setup": 900,
    "codigo_barra": 45182
  },
  {
    "id_erp": 31823,
    "nome": "MESA CENTRO DENVER",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 180,
    "setup": 1200,
    "codigo_barra": 31823
  },
  {
    "id_erp": 56507,
    "nome": "MESA CENTRO DENVER S/ FRISO",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 180,
    "setup": 1200,
    "codigo_barra": 56507
  },
  {
    "id_erp": 70802,
    "nome": "MESA CENTRO DROP 1000",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 600,
    "setup": 900,
    "codigo_barra": 70802
  },
  {
    "id_erp": 70802,
    "nome": "MESA CENTRO DROP 1000 - MEDIDA ESPECIAL (CHAMAR SERGIO NA MASTER)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 780,
    "setup": 900,
    "codigo_barra": 70802
  },
  {
    "id_erp": 72255,
    "nome": "MESA CENTRO DROP 1000 T. MAD",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 300,
    "setup": 900,
    "codigo_barra": 72255
  },
  {
    "id_erp": 54901,
    "nome": "MESA CENTRO DROP 1200",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 960,
    "setup": 900,
    "codigo_barra": 54901
  },
  {
    "id_erp": 72256,
    "nome": "MESA CENTRO DROP 1200 T. MAD.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 600,
    "setup": 900,
    "codigo_barra": 72256
  },
  {
    "id_erp": 54902,
    "nome": "MESA CENTRO DROP 1400",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 960,
    "setup": 900,
    "codigo_barra": 54902
  },
  {
    "id_erp": 72257,
    "nome": "MESA CENTRO DROP 1400 T.MAD.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 600,
    "setup": 900,
    "codigo_barra": 72257
  },
  {
    "id_erp": 72217,
    "nome": "MESA CENTRO GOYA 1400 X 800",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 600,
    "setup": 900,
    "codigo_barra": 72217
  },
  {
    "id_erp": 72135,
    "nome": "MESA CENTRO GOYA 600 QUADRADA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 600,
    "setup": 900,
    "codigo_barra": 72135
  },
  {
    "id_erp": 72120,
    "nome": "MESA CENTRO GOYA 600 REDONDA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 600,
    "setup": 900,
    "codigo_barra": 72120
  },
  {
    "id_erp": 72163,
    "nome": "MESA CENTRO GOYA 800 QUADRADA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 600,
    "setup": 900,
    "codigo_barra": 72163
  },
  {
    "id_erp": 72254,
    "nome": "MESA CENTRO GOYA 800 X 600",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 600,
    "setup": 900,
    "codigo_barra": 72254
  },
  {
    "id_erp": 79798,
    "nome": "MESA CENTRO GRAVITA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.5,
    "setup": 900,
    "codigo_barra": 79798
  },
  {
    "id_erp": 48480,
    "nome": "MESA CENTRO ITACARE QUADRADA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 315,
    "setup": 900,
    "codigo_barra": 48480
  },
  {
    "id_erp": 48479,
    "nome": "MESA CENTRO ITACARE REDONDA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 200,
    "setup": 900,
    "codigo_barra": 48479
  },
  {
    "id_erp": 18203,
    "nome": "MESA CENTRO LARA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 160,
    "setup": 900,
    "codigo_barra": 18203
  },
  {
    "id_erp": 57522,
    "nome": "MESA CENTRO LEON",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 240,
    "setup": 1500,
    "codigo_barra": 57522
  },
  {
    "id_erp": 54881,
    "nome": "MESA CENTRO MARA 1,00 T. LACA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 95,
    "setup": 900,
    "codigo_barra": 54881
  },
  {
    "id_erp": 54944,
    "nome": "MESA CENTRO MARA 1,00 T. MAD.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 95,
    "setup": 900,
    "codigo_barra": 54944
  },
  {
    "id_erp": 36530,
    "nome": "MESA CENTRO MARA 1,00 T. V.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 95,
    "setup": 900,
    "codigo_barra": 36530
  },
  {
    "id_erp": 54882,
    "nome": "MESA CENTRO MARA 1,10 T. LACA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 110,
    "setup": 900,
    "codigo_barra": 54882
  },
  {
    "id_erp": 54945,
    "nome": "MESA CENTRO MARA 1,10 T. MAD.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 110,
    "setup": 900,
    "codigo_barra": 54945
  },
  {
    "id_erp": 36397,
    "nome": "MESA CENTRO MARA 1,10 T. V.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 110,
    "setup": 900,
    "codigo_barra": 36397
  },
  {
    "id_erp": 53625,
    "nome": "MESA CENTRO MORANA C/ VIDRO LX",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 45,
    "setup": 900,
    "codigo_barra": 53625
  },
  {
    "id_erp": 31824,
    "nome": "MESA CENTRO ORLEAN",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 60,
    "setup": 600,
    "codigo_barra": 31824
  },
  {
    "id_erp": 77789,
    "nome": "MESA CENTRO PANTALONA 600 T. MAD.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 300,
    "setup": 900,
    "codigo_barra": 77789
  },
  {
    "id_erp": 77790,
    "nome": "MESA CENTRO PANTALONA 800 T. MAD.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 360,
    "setup": 900,
    "codigo_barra": 77790
  },
  {
    "id_erp": 79676,
    "nome": "MESA CENTRO SHELL 1300",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 480,
    "setup": 900,
    "codigo_barra": 79676
  },
  {
    "id_erp": 79677,
    "nome": "MESA CENTRO SHELL 1600",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 540,
    "setup": 900,
    "codigo_barra": 79677
  },
  {
    "id_erp": 62884,
    "nome": "MESA CENTRO TANGUETO 200",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 76,
    "setup": 900,
    "codigo_barra": 62884
  },
  {
    "id_erp": 63660,
    "nome": "MESA CENTRO TANGUETO 270",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 76,
    "setup": 900,
    "codigo_barra": 63660
  },
  {
    "id_erp": 59528,
    "nome": "MESA CENTRO TUNEL 1200 REDONDA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 450,
    "setup": 900,
    "codigo_barra": 59528
  },
  {
    "id_erp": 59529,
    "nome": "MESA CENTRO TUNEL 1600 OVAL",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 390,
    "setup": 900,
    "codigo_barra": 59529
  },
  {
    "id_erp": 59530,
    "nome": "MESA CENTRO TUNEL 1800 OVAL",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 390,
    "setup": 900,
    "codigo_barra": 59530
  },
  {
    "id_erp": 59527,
    "nome": "MESA CENTRO TUNEL 900 REDONDA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 475,
    "setup": 900,
    "codigo_barra": 59527
  },
  {
    "id_erp": 43256,
    "nome": "MESA CENTRO VEGAS",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 225,
    "setup": 900,
    "codigo_barra": 43256
  },
  {
    "id_erp": 68916,
    "nome": "MESA CENTRO VEGAS LX - LANÇAMENTO (CHAMAR SERGIO DESENVOLVIMENTO)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 180,
    "setup": 900,
    "codigo_barra": 68916
  },
  {
    "id_erp": 68796,
    "nome": "MESA CENTRO VIRA VOLTA 0,70",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 2.52,
    "setup": 900,
    "codigo_barra": 68796
  },
  {
    "id_erp": 68795,
    "nome": "MESA CENTRO VIRA VOLTA 1,00",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 2.52,
    "setup": 900,
    "codigo_barra": 68795
  },
  {
    "id_erp": 63079,
    "nome": "MESA CENTRO YUMA 200",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 170,
    "setup": 900,
    "codigo_barra": 63079
  },
  {
    "id_erp": 63041,
    "nome": "MESA CENTRO YUMA 300",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 175,
    "setup": 900,
    "codigo_barra": 63041
  },
  {
    "id_erp": 43271,
    "nome": "MESA CENTRO ZARA 1000",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 160,
    "setup": 900,
    "codigo_barra": 43271
  },
  {
    "id_erp": 43272,
    "nome": "MESA CENTRO ZARA 1000 T. MAD.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 160,
    "setup": 900,
    "codigo_barra": 43272
  },
  {
    "id_erp": 43273,
    "nome": "MESA CENTRO ZARA 800",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 150,
    "setup": 900,
    "codigo_barra": 43273
  },
  {
    "id_erp": 43274,
    "nome": "MESA CENTRO ZARA 800 T. MAD.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 150,
    "setup": 900,
    "codigo_barra": 43274
  },
  {
    "id_erp": 25670,
    "nome": "MESA LATERAL ADRA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 275,
    "setup": 2100,
    "codigo_barra": 25670
  },
  {
    "id_erp": 54885,
    "nome": "MESA LATERAL ASTI T. LACA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 105,
    "setup": 900,
    "codigo_barra": 54885
  },
  {
    "id_erp": 34494,
    "nome": "MESA LATERAL ASTI T. MAD.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 105,
    "setup": 900,
    "codigo_barra": 34494
  },
  {
    "id_erp": 34493,
    "nome": "MESA LATERAL ASTI T. V.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 105,
    "setup": 900,
    "codigo_barra": 34493
  },
  {
    "id_erp": 52178,
    "nome": "MESA LATERAL BEND 510 T. ESP.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.02,
    "setup": 900,
    "codigo_barra": 52178
  },
  {
    "id_erp": 55116,
    "nome": "MESA LATERAL BEND 510 T. LACA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.02,
    "setup": 900,
    "codigo_barra": 55116
  },
  {
    "id_erp": 43236,
    "nome": "MESA LATERAL BEND 510 T. MAD.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.02,
    "setup": 900,
    "codigo_barra": 43236
  },
  {
    "id_erp": 43235,
    "nome": "MESA LATERAL BEND 510 T. V.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.02,
    "setup": 900,
    "codigo_barra": 43235
  },
  {
    "id_erp": 52179,
    "nome": "MESA LATERAL BEND 580 T. ESP.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.02,
    "setup": 900,
    "codigo_barra": 52179
  },
  {
    "id_erp": 55117,
    "nome": "MESA LATERAL BEND 580 T. LACA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.02,
    "setup": 900,
    "codigo_barra": 55117
  },
  {
    "id_erp": 43234,
    "nome": "MESA LATERAL BEND 580 T. MAD.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.02,
    "setup": 900,
    "codigo_barra": 43234
  },
  {
    "id_erp": 43199,
    "nome": "MESA LATERAL BEND 580 T. V.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.02,
    "setup": 900,
    "codigo_barra": 43199
  },
  {
    "id_erp": 55587,
    "nome": "MESA LATERAL CALIANDRA T. LACA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 520,
    "setup": 900,
    "codigo_barra": 55587
  },
  {
    "id_erp": 43703,
    "nome": "MESA LATERAL CALIANDRA T. MAD.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 520,
    "setup": 900,
    "codigo_barra": 43703
  },
  {
    "id_erp": 44112,
    "nome": "MESA LATERAL CALIANDRA T. V.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 520,
    "setup": 900,
    "codigo_barra": 44112
  },
  {
    "id_erp": 72835,
    "nome": "MESA LATERAL CERRADO 1000",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 300,
    "setup": 900,
    "codigo_barra": 72835
  },
  {
    "id_erp": 56760,
    "nome": "MESA LATERAL CUBO",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 250,
    "setup": 900,
    "codigo_barra": 56760
  },
  {
    "id_erp": 68611,
    "nome": "MESA LATERAL DAHLIA (ROUTER)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 660,
    "setup": 900,
    "codigo_barra": 68611
  },
  {
    "id_erp": 59537,
    "nome": "MESA LATERAL DAHLIA 440 T. LACA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 60,
    "setup": 600,
    "codigo_barra": 59537
  },
  {
    "id_erp": 57947,
    "nome": "MESA LATERAL DAHLIA 440 T. MAD.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 60,
    "setup": 600,
    "codigo_barra": 57947
  },
  {
    "id_erp": 59538,
    "nome": "MESA LATERAL DAHLIA 560 T. LACA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 60,
    "setup": 600,
    "codigo_barra": 59538
  },
  {
    "id_erp": 57946,
    "nome": "MESA LATERAL DAHLIA 560 T. MAD.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 60,
    "setup": 600,
    "codigo_barra": 57946
  },
  {
    "id_erp": 54940,
    "nome": "MESA LATERAL ELO T. LACA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 30,
    "setup": 900,
    "codigo_barra": 54940
  },
  {
    "id_erp": 36356,
    "nome": "MESA LATERAL ELO T. MAD.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 30,
    "setup": 900,
    "codigo_barra": 36356
  },
  {
    "id_erp": 36355,
    "nome": "MESA LATERAL ELO T. V.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 30,
    "setup": 900,
    "codigo_barra": 36355
  },
  {
    "id_erp": 71006,
    "nome": "MESA LATERAL EQUILIBRIO 520 X 400 T. MAD.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.02,
    "setup": 900,
    "codigo_barra": 71006
  },
  {
    "id_erp": 56758,
    "nome": "MESA LATERAL FACE",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 30,
    "setup": 900,
    "codigo_barra": 56758
  },
  {
    "id_erp": 56761,
    "nome": "MESA LATERAL FRAME",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 250,
    "setup": 900,
    "codigo_barra": 56761
  },
  {
    "id_erp": 72179,
    "nome": "MESA LATERAL GOYA 700 X 400 ORGANICA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 480,
    "setup": 900,
    "codigo_barra": 72179
  },
  {
    "id_erp": 63659,
    "nome": "MESA LATERAL GREY 500",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 327,
    "setup": 900,
    "codigo_barra": 63659
  },
  {
    "id_erp": 69528,
    "nome": "MESA LATERAL GREY 500 RED.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 355,
    "setup": 900,
    "codigo_barra": 69528
  },
  {
    "id_erp": 69794,
    "nome": "MESA LATERAL GREY 500 RED. T. PEDRA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 355,
    "setup": 900,
    "codigo_barra": 69794
  },
  {
    "id_erp": 63658,
    "nome": "MESA LATERAL GREY 550",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 327,
    "setup": 900,
    "codigo_barra": 63658
  },
  {
    "id_erp": 69529,
    "nome": "MESA LATERAL GREY 550 RED.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 355,
    "setup": 900,
    "codigo_barra": 69529
  },
  {
    "id_erp": 69795,
    "nome": "MESA LATERAL GREY 550 RED. T. PEDRA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 355,
    "setup": 900,
    "codigo_barra": 69795
  },
  {
    "id_erp": 62898,
    "nome": "MESA LATERAL GREY 600",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 327,
    "setup": 900,
    "codigo_barra": 62898
  },
  {
    "id_erp": 69530,
    "nome": "MESA LATERAL GREY 600 RED.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 355,
    "setup": 900,
    "codigo_barra": 69530
  },
  {
    "id_erp": 69796,
    "nome": "MESA LATERAL GREY 600 RED. T. PEDRA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 355,
    "setup": 900,
    "codigo_barra": 69796
  },
  {
    "id_erp": 48481,
    "nome": "MESA LATERAL ITACARE",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 215,
    "setup": 900,
    "codigo_barra": 48481
  },
  {
    "id_erp": 18204,
    "nome": "MESA LATERAL LARA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 160,
    "setup": 900,
    "codigo_barra": 18204
  },
  {
    "id_erp": 65667,
    "nome": "MESA LATERAL LUGO SLIM 1000 X 500",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 360,
    "setup": 1800,
    "codigo_barra": 65667
  },
  {
    "id_erp": 65465,
    "nome": "MESA LATERAL LUGO SLIM 500",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 360,
    "setup": 1800,
    "codigo_barra": 65465
  },
  {
    "id_erp": 65464,
    "nome": "MESA LATERAL LUGO SLIM 600",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 360,
    "setup": 1800,
    "codigo_barra": 65464
  },
  {
    "id_erp": 31622,
    "nome": "MESA LATERAL PAOLA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 205,
    "setup": 900,
    "codigo_barra": 31622
  },
  {
    "id_erp": 56757,
    "nome": "MESA LATERAL SOMA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 180,
    "setup": 900,
    "codigo_barra": 56757
  },
  {
    "id_erp": 59526,
    "nome": "MESA LATERAL TUNEL 700 REDONDA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 495,
    "setup": 1500,
    "codigo_barra": 59526
  },
  {
    "id_erp": 50725,
    "nome": "MESA LATERAL VEGAS",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 180,
    "setup": 900,
    "codigo_barra": 50725
  },
  {
    "id_erp": 68774,
    "nome": "MESA LATERAL VEGAS LX - FEIRA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 370,
    "setup": 900,
    "codigo_barra": 68774
  },
  {
    "id_erp": 30423,
    "nome": "MINI BOMBE  VERSALHES",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 340,
    "setup": 1800,
    "codigo_barra": 30423
  },
  {
    "id_erp": 39810,
    "nome": "PAINEL ALAMO",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 60,
    "setup": 600,
    "codigo_barra": 39810
  },
  {
    "id_erp": 76609,
    "nome": "PAINEL AMBAR 1,40 X 1,00",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 600,
    "setup": 900,
    "codigo_barra": 76609
  },
  {
    "id_erp": 76610,
    "nome": "PAINEL AMBAR 1,60 X 1,20",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.2,
    "setup": 900,
    "codigo_barra": 76610
  },
  {
    "id_erp": 27349,
    "nome": "PAINEL CERRATO 1,80",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 60,
    "setup": 600,
    "codigo_barra": 27349
  },
  {
    "id_erp": 50924,
    "nome": "PAINEL CERRATO 2,00",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 60,
    "setup": 600,
    "codigo_barra": 50924
  },
  {
    "id_erp": 28713,
    "nome": "PAINEL CERRATO 2,20",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 60,
    "setup": 600,
    "codigo_barra": 28713
  },
  {
    "id_erp": 44322,
    "nome": "PAINEL DIVANO",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 450,
    "setup": 900,
    "codigo_barra": 44322
  },
  {
    "id_erp": 63522,
    "nome": "PAINEL DIVANO",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 450,
    "setup": 900,
    "codigo_barra": 63522
  },
  {
    "id_erp": 68830,
    "nome": "PAINEL INDIGO 1440",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 900,
    "setup": 900,
    "codigo_barra": 68830
  },
  {
    "id_erp": 688309,
    "nome": "PAINEL INDIGO 1440",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 900,
    "setup": 900,
    "codigo_barra": 688309
  },
  {
    "id_erp": 68775,
    "nome": "PAINEL INDIGO 1640 - FEIRA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 350,
    "setup": 900,
    "codigo_barra": 68775
  },
  {
    "id_erp": 687759,
    "nome": "PAINEL INDIGO 1640 - FEIRA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 350,
    "setup": 900,
    "codigo_barra": 687759
  },
  {
    "id_erp": 68831,
    "nome": "PAINEL INDIGO 1840",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 350,
    "setup": 900,
    "codigo_barra": 68831
  },
  {
    "id_erp": 688319,
    "nome": "PAINEL INDIGO 1840",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 350,
    "setup": 900,
    "codigo_barra": 688319
  },
  {
    "id_erp": 39813,
    "nome": "PAINEL MANDI",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 370,
    "setup": 900,
    "codigo_barra": 39813
  },
  {
    "id_erp": 27350,
    "nome": "PAINEL TOLEDO",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 60,
    "setup": 900,
    "codigo_barra": 27350
  },
  {
    "id_erp": 71849,
    "nome": "PECA BRUTA MDF T1385 920 X 920 X 2,8MM",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 600,
    "setup": 900,
    "codigo_barra": 71849
  },
  {
    "id_erp": 37421,
    "nome": "PEGA MAD 378 X 89 X 26 MM - (CAD. MAIA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 90,
    "setup": 1200,
    "codigo_barra": 37421
  },
  {
    "id_erp": 43366,
    "nome": "PEGA RATAN MAD 378 X 89 X 26 MM - (CAD. MAIA RATAN)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 100,
    "setup": 1200,
    "codigo_barra": 43366
  },
  {
    "id_erp": 43380,
    "nome": "PES - SOFA VALENCIA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 50,
    "setup": 900,
    "codigo_barra": 43380
  },
  {
    "id_erp": 50729,
    "nome": "PUFF VEGAS 0,45",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 180,
    "setup": 900,
    "codigo_barra": 50729
  },
  {
    "id_erp": 50730,
    "nome": "PUFF VEGAS 0,80",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 225,
    "setup": 900,
    "codigo_barra": 50730
  },
  {
    "id_erp": 69280,
    "nome": "PUFF VEGAS LX 0,45",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 310,
    "setup": 900,
    "codigo_barra": 69280
  },
  {
    "id_erp": 69281,
    "nome": "PUFF VEGAS LX 0,80",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 720,
    "setup": 900,
    "codigo_barra": 69281
  },
  {
    "id_erp": 28888,
    "nome": "QUADRO ESPELHO ALAMO",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 60,
    "setup": 900,
    "codigo_barra": 28888
  },
  {
    "id_erp": 36023,
    "nome": "QUADRO ESPELHO BRISTOL",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 450,
    "setup": 900,
    "codigo_barra": 36023
  },
  {
    "id_erp": 69355,
    "nome": "TAMPO GIRATORIO MOVEL ARCOS 0,90 LAM.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 331,
    "setup": 900,
    "codigo_barra": 69355
  },
  {
    "id_erp": 69356,
    "nome": "TAMPO GIRATORIO MOVEL ARCOS 0,90 VIDRO",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 331,
    "setup": 900,
    "codigo_barra": 69356
  },
  {
    "id_erp": 69354,
    "nome": "TAMPO GIRATORIO MOVEL ARCOS 090 LACA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 331,
    "setup": 900,
    "codigo_barra": 69354
  },
  {
    "id_erp": 79475,
    "nome": "TAMPO MDF J9P5712 613 X 613 X 6MM P/ PEDRA ATMOS",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 600,
    "setup": 900,
    "codigo_barra": 79475
  },
  {
    "id_erp": 68759,
    "nome": "TAMPO MDF T0741 742 X 742 X 2,8MM - MESA JANTAR INDIGO 1,44 T. RECOURO",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 185,
    "setup": 900,
    "codigo_barra": 68759
  },
  {
    "id_erp": 68760,
    "nome": "TAMPO MDF T0742 1106 X 410 X 2,8MM - MESA JANTAR INDIGO 1,44 T. RECOURO",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 185,
    "setup": 900,
    "codigo_barra": 68760
  },
  {
    "id_erp": 68791,
    "nome": "TAMPO MDF T0745 841 X 841 X 2,8MM - MESA JANTAR INDIGO 1,64 T. RECOURO",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 185,
    "setup": 900,
    "codigo_barra": 68791
  },
  {
    "id_erp": 68792,
    "nome": "TAMPO MDF T0746 1247 X 460 X 2,8MM - MESA JANTAR INDIGO 1,64 T. RECOURO",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 185,
    "setup": 900,
    "codigo_barra": 68792
  },
  {
    "id_erp": 68793,
    "nome": "TAMPO MDF T0747 922 X 922 X 2,8MM - MESA JANTAR INDIGO 1,84 T. RECOURO",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 185,
    "setup": 900,
    "codigo_barra": 68793
  },
  {
    "id_erp": 68794,
    "nome": "TAMPO MDF T0748 1359 X 541 X 2,8MM - MESA JANTAR INDIGO 1,84 T. RECOURO",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 185,
    "setup": 900,
    "codigo_barra": 68794
  },
  {
    "id_erp": 35889,
    "nome": "TAMPO VIDRO CANTO REDONDO 1800 X 1000 X 35MM",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 200,
    "setup": 900,
    "codigo_barra": 35889
  },
  {
    "id_erp": 35892,
    "nome": "TAMPO VIDRO CANTO REDONDO 2000 X 1000 X 35MM",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 200,
    "setup": 900,
    "codigo_barra": 35892
  },
  {
    "id_erp": 35894,
    "nome": "TAMPO VIDRO CANTO REDONDO 2200 X 1100 X 35MM",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 200,
    "setup": 900,
    "codigo_barra": 35894
  },
  {
    "id_erp": 37225,
    "nome": "TAMPO VIDRO CANTO RETO 1400 X 1400 X 25MM",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 102,
    "setup": 900,
    "codigo_barra": 37225
  },
  {
    "id_erp": 35265,
    "nome": "TAMPO VIDRO CANTO RETO 1400 X 1400 X 35MM",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 133,
    "setup": 900,
    "codigo_barra": 35265
  },
  {
    "id_erp": 37228,
    "nome": "TAMPO VIDRO CANTO RETO 1500 X 1500 X 25MM",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 102,
    "setup": 900,
    "codigo_barra": 37228
  },
  {
    "id_erp": 34858,
    "nome": "TAMPO VIDRO CANTO RETO 1500 X 1500 X 35MM",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 133,
    "setup": 900,
    "codigo_barra": 34858
  },
  {
    "id_erp": 37219,
    "nome": "TAMPO VIDRO CANTO RETO 1800 X 1000 X 25MM",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 102,
    "setup": 900,
    "codigo_barra": 37219
  },
  {
    "id_erp": 37345,
    "nome": "TAMPO VIDRO CANTO RETO 1800 X 1000 X 25MM B. MAD.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 102,
    "setup": 900,
    "codigo_barra": 37345
  },
  {
    "id_erp": 35437,
    "nome": "TAMPO VIDRO CANTO RETO 1800 X 1000 X 35MM",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 133,
    "setup": 900,
    "codigo_barra": 35437
  },
  {
    "id_erp": 44115,
    "nome": "TAMPO VIDRO CANTO RETO 1800 X 1000 X 35MM B. LAM.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 133,
    "setup": 900,
    "codigo_barra": 44115
  },
  {
    "id_erp": 37222,
    "nome": "TAMPO VIDRO CANTO RETO 2000 X 1000 X 25MM",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 102,
    "setup": 900,
    "codigo_barra": 37222
  },
  {
    "id_erp": 37347,
    "nome": "TAMPO VIDRO CANTO RETO 2000 X 1000 X 25MM B. MAD.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 102,
    "setup": 900,
    "codigo_barra": 37347
  },
  {
    "id_erp": 35436,
    "nome": "TAMPO VIDRO CANTO RETO 2000 X 1000 X 35MM",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 133,
    "setup": 900,
    "codigo_barra": 35436
  },
  {
    "id_erp": 44116,
    "nome": "TAMPO VIDRO CANTO RETO 2000 X 1000 X 35MM B. LAM.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 133,
    "setup": 900,
    "codigo_barra": 44116
  },
  {
    "id_erp": 35435,
    "nome": "TAMPO VIDRO CANTO RETO 2200 X 1100 X 35MM",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 133,
    "setup": 900,
    "codigo_barra": 35435
  },
  {
    "id_erp": 43665,
    "nome": "TAMPO VIDRO CANTO RETO 2200 X 1100 X 35MM B. LAM.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 133,
    "setup": 900,
    "codigo_barra": 43665
  },
  {
    "id_erp": 44117,
    "nome": "TAMPO VIDRO CANTO RETO 2400 X 1200 X 35MM B. LAM.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 133,
    "setup": 900,
    "codigo_barra": 44117
  },
  {
    "id_erp": 44515,
    "nome": "TRAVESSA LAMINADA ITAMBE T6 1570 X 275 X 35MM BANDEJA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 60,
    "setup": 600,
    "codigo_barra": 44515
  },
  {
    "id_erp": 45722,
    "nome": "TRAVESSA LAMINADA ITAMBE T9 860 X 275 X 35MM BANDEJA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 60,
    "setup": 600,
    "codigo_barra": 45722
  },
  {
    "id_erp": 55393,
    "nome": "TRAVESSA MAD BRACO 270 X 60 X 30MM DIR (CAD. MONACO C/ BRAÇO)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 35,
    "setup": 900,
    "codigo_barra": 55393
  },
  {
    "id_erp": 54939,
    "nome": "TRAVESSA MAD BRACO 270 X 60 X 30MM ESQ (CAD. MONACO C/ BRAÇO)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 35,
    "setup": 900,
    "codigo_barra": 54939
  },
  {
    "id_erp": 69156,
    "nome": "TRAVESSA MAD BRACO T0806 135 X 32 X 45MM DIREITO MENOR - POLTRONA DELTA - LOTE PILOTO (ZÉ ALEX)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.02,
    "setup": 900,
    "codigo_barra": 69156
  },
  {
    "id_erp": 69158,
    "nome": "TRAVESSA MAD BRACO T0808 135 X 32 X 45MM ESQUERDO MENOR - POLTRONA DELTA - LOTE PILOTO (ZÉ ALEX)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.02,
    "setup": 900,
    "codigo_barra": 69158
  },
  {
    "id_erp": 57487,
    "nome": "TRAVESSA MAD T0778 418 X 50 X 45MM SUPERIOR - CADEIRA DELTA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 20,
    "setup": 1500,
    "codigo_barra": 57487
  },
  {
    "id_erp": 57488,
    "nome": "TRAVESSA MAD T0779 446 X 46 X 46MM INFERIOR - CADEIRA DELTA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 20,
    "setup": 0,
    "codigo_barra": 57488
  },
  {
    "id_erp": 57489,
    "nome": "TRAVESSA MAD T0780 210 X 90 X 45MM DIREITA - CADEIRA DELTA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 20,
    "setup": 0,
    "codigo_barra": 57489
  },
  {
    "id_erp": 57490,
    "nome": "TRAVESSA MAD T0781 210 X 90 X 45MM ESQUERDA - CADEIRA DELTA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 20,
    "setup": 0,
    "codigo_barra": 57490
  },
  {
    "id_erp": 61201,
    "nome": "TRAVESSA MAD T0822 663 X 81 X 30MM ENCOSTO - POLTRONA COPAN",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 40,
    "setup": 900,
    "codigo_barra": 61201
  },
  {
    "id_erp": 61748,
    "nome": "TRAVESSA PINT LACA T0036 650 X 80 X 9MM GAVEA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 300,
    "setup": 900,
    "codigo_barra": 61748
  },
  {
    "id_erp": 48145,
    "nome": "UNIAO LAMINA PINUS U0034 750 X 180 X 15MM (POLTRONA RUBIA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 60,
    "setup": 900,
    "codigo_barra": 48145
  },
  {
    "id_erp": 50920,
    "nome": "UNIAO LAMINA PINUS U0037 430 X 90 X 15MM POLTRONA BARBARA (EXTERNA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 40,
    "setup": 900,
    "codigo_barra": 50920
  },
  {
    "id_erp": 50922,
    "nome": "UNIAO LAMINA PINUS U0038 790 X 90 X 9MM POLTRONA BARBARA (INTERNA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 40,
    "setup": 900,
    "codigo_barra": 50922
  },
  {
    "id_erp": 53692,
    "nome": "UNIAO MAD U0039 110 X 102 X 60MM (MESA MITRE)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 90,
    "setup": 900,
    "codigo_barra": 53692
  },
  {
    "id_erp": 60530,
    "nome": "UNIAO MAD U0042 140 X 60 X 51MM - BUFFET/HOME/ARMARIO VEDRA LX",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 90,
    "setup": 900,
    "codigo_barra": 60530
  },
  {
    "id_erp": 39995,
    "nome": "VOL 1/2 ARMARIO DUBLIN",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 130,
    "setup": 900,
    "codigo_barra": 39995
  },
  {
    "id_erp": 44293,
    "nome": "VOL 1/2 ARMARIO DUBLIN C/ ESPELHO",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 115,
    "setup": 900,
    "codigo_barra": 44293
  },
  {
    "id_erp": 81227,
    "nome": "VOL 1/2 BASE AMBAR CORPORATIVA 1,40/1,60",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 600,
    "setup": 900,
    "codigo_barra": 81227
  },
  {
    "id_erp": 44020,
    "nome": "VOL 1/2 BASE BISTRO CALIANDRA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 320,
    "setup": 900,
    "codigo_barra": 44020
  },
  {
    "id_erp": 81916,
    "nome": "VOL 1/2 BASE MESA AMBAR 1,40",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 600,
    "setup": 900,
    "codigo_barra": 81916
  },
  {
    "id_erp": 68462,
    "nome": "VOL 1/2 BASE MESA AMBAR 1,40/1,60",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 600,
    "setup": 900,
    "codigo_barra": 68462
  },
  {
    "id_erp": 81915,
    "nome": "VOL 1/2 BASE MESA AMBAR 1,60",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 600,
    "setup": 900,
    "codigo_barra": 81915
  },
  {
    "id_erp": 81922,
    "nome": "VOL 1/2 BASE MESA AMBAR/SIENA 1,40 ALT. 670",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 600,
    "setup": 900,
    "codigo_barra": 81922
  },
  {
    "id_erp": 43637,
    "nome": "VOL 1/2 BASE MESA CARDEAL",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 300,
    "setup": 900,
    "codigo_barra": 43637
  },
  {
    "id_erp": 50319,
    "nome": "VOL 1/2 BASE MESA CARTAGO",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 330,
    "setup": 900,
    "codigo_barra": 50319
  },
  {
    "id_erp": 36184,
    "nome": "VOL 1/2 BASE MESA CECI",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 900,
    "setup": 900,
    "codigo_barra": 36184
  },
  {
    "id_erp": 37604,
    "nome": "VOL 1/2 BASE MESA CENTRO MARAU",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 430,
    "setup": 900,
    "codigo_barra": 37604
  },
  {
    "id_erp": 60018,
    "nome": "VOL 1/2 BASE MESA CENTRO TANGARA 0,90",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 90,
    "setup": 900,
    "codigo_barra": 60018
  },
  {
    "id_erp": 60020,
    "nome": "VOL 1/2 BASE MESA CENTRO TANGARA 1,20",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 83,
    "setup": 900,
    "codigo_barra": 60020
  },
  {
    "id_erp": 60022,
    "nome": "VOL 1/2 BASE MESA CENTRO TANGARA 1,60",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 98,
    "setup": 900,
    "codigo_barra": 60022
  },
  {
    "id_erp": 60024,
    "nome": "VOL 1/2 BASE MESA CENTRO TANGARA 1,80",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 150,
    "setup": 900,
    "codigo_barra": 60024
  },
  {
    "id_erp": 38629,
    "nome": "VOL 1/2 BASE MESA DUNA PLUS 1,20/1,30",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 390,
    "setup": 900,
    "codigo_barra": 38629
  },
  {
    "id_erp": 38669,
    "nome": "VOL 1/2 BASE MESA DUNA PLUS 1,40/1,50/1,60",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 460,
    "setup": 900,
    "codigo_barra": 38669
  },
  {
    "id_erp": 55057,
    "nome": "VOL 1/2 BASE MESA DUNA PLUS LX 1,40/1,50/1,60",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 460,
    "setup": 900,
    "codigo_barra": 55057
  },
  {
    "id_erp": 42433,
    "nome": "VOL 1/2 BASE MESA DUNA RET. 1,60/1,80",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 455,
    "setup": 900,
    "codigo_barra": 42433
  },
  {
    "id_erp": 41809,
    "nome": "VOL 1/2 BASE MESA DUNA RET. 2,00/2,20/2,40",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 530,
    "setup": 900,
    "codigo_barra": 41809
  },
  {
    "id_erp": 36349,
    "nome": "VOL 1/2 BASE MESA ELIS",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 360,
    "setup": 900,
    "codigo_barra": 36349
  },
  {
    "id_erp": 45301,
    "nome": "VOL 1/2 BASE MESA ELOA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 350,
    "setup": 900,
    "codigo_barra": 45301
  },
  {
    "id_erp": 64319,
    "nome": "VOL 1/2 BASE MESA FUNGI 2,40/3,40",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 270,
    "setup": 900,
    "codigo_barra": 64319
  },
  {
    "id_erp": 76615,
    "nome": "VOL 1/2 BASE MESA FUNGI 2,50 X 1,10",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 270,
    "setup": 900,
    "codigo_barra": 76615
  },
  {
    "id_erp": 70194,
    "nome": "VOL 1/2 BASE MESA FUNGI MENOR",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 270,
    "setup": 900,
    "codigo_barra": 70194
  },
  {
    "id_erp": 70659,
    "nome": "VOL 1/2 BASE MESA FUNGI ORGANICA 1,60/1,80",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 600,
    "setup": 900,
    "codigo_barra": 70659
  },
  {
    "id_erp": 37454,
    "nome": "VOL 1/2 BASE MESA GENEBRA 1,40/1,50 QUAD.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 160,
    "setup": 900,
    "codigo_barra": 37454
  },
  {
    "id_erp": 38375,
    "nome": "VOL 1/2 BASE MESA GENEBRA 1,80/2,00/2,20",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 160,
    "setup": 900,
    "codigo_barra": 38375
  },
  {
    "id_erp": 38395,
    "nome": "VOL 1/2 BASE MESA GENEBRA RET. 1,40/1,60",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 160,
    "setup": 900,
    "codigo_barra": 38395
  },
  {
    "id_erp": 68444,
    "nome": "VOL 1/2 BASE MESA HELIX",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.24,
    "setup": 900,
    "codigo_barra": 68444
  },
  {
    "id_erp": 51387,
    "nome": "VOL 1/2 BASE MESA INDIGO 1,44",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.32,
    "setup": 900,
    "codigo_barra": 51387
  },
  {
    "id_erp": 50731,
    "nome": "VOL 1/2 BASE MESA INDIGO 1,64/1,84/2,04",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 490,
    "setup": 900,
    "codigo_barra": 50731
  },
  {
    "id_erp": 70327,
    "nome": "VOL 1/2 BASE MESA JANTAR GUANABARA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 840,
    "setup": 900,
    "codigo_barra": 70327
  },
  {
    "id_erp": 76376,
    "nome": "VOL 1/2 BASE MESA JANTAR GUANABARA 1,80 / 2,00",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 840,
    "setup": 900,
    "codigo_barra": 76376
  },
  {
    "id_erp": 78664,
    "nome": "VOL 1/2 BASE MESA LAIKA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 560,
    "setup": 900,
    "codigo_barra": 78664
  },
  {
    "id_erp": 68486,
    "nome": "VOL 1/2 BASE MESA LEME - FEIRA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.32,
    "setup": 900,
    "codigo_barra": 68486
  },
  {
    "id_erp": 37997,
    "nome": "VOL 1/2 BASE MESA LIZZA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 315,
    "setup": 900,
    "codigo_barra": 37997
  },
  {
    "id_erp": 49178,
    "nome": "VOL 1/2 BASE MESA LUGO/SCALA 1,80/2,00",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 340,
    "setup": 900,
    "codigo_barra": 49178
  },
  {
    "id_erp": 41925,
    "nome": "VOL 1/2 BASE MESA MARIN 1,80/2,00/2,14/2,20",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 645,
    "setup": 900,
    "codigo_barra": 41925
  },
  {
    "id_erp": 49820,
    "nome": "VOL 1/2 BASE MESA MARIN 2,34/2,40",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 685,
    "setup": 900,
    "codigo_barra": 49820
  },
  {
    "id_erp": 49301,
    "nome": "VOL 1/2 BASE MESA MARIN LX 2,64/2,70/2,94/3,00",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 685,
    "setup": 900,
    "codigo_barra": 49301
  },
  {
    "id_erp": 42065,
    "nome": "VOL 1/2 BASE MESA MARIN PLUS 1,40/1,50/1,60",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 600,
    "setup": 900,
    "codigo_barra": 42065
  },
  {
    "id_erp": 38981,
    "nome": "VOL 1/2 BASE MESA MARROCOS",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 265,
    "setup": 900,
    "codigo_barra": 38981
  },
  {
    "id_erp": 38985,
    "nome": "VOL 1/2 BASE MESA MARROCOS C/ BARRA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 265,
    "setup": 900,
    "codigo_barra": 38985
  },
  {
    "id_erp": 36176,
    "nome": "VOL 1/2 BASE MESA NINA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 450,
    "setup": 900,
    "codigo_barra": 36176
  },
  {
    "id_erp": 42140,
    "nome": "VOL 1/2 BASE MESA OMEGA 2,00/2,14/2,20 /2,34/2,40",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 660,
    "setup": 900,
    "codigo_barra": 42140
  },
  {
    "id_erp": 49188,
    "nome": "VOL 1/2 BASE MESA OMEGA 2,64/2,70/2,94/3,00",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 660,
    "setup": 900,
    "codigo_barra": 49188
  },
  {
    "id_erp": 66165,
    "nome": "VOL 1/2 BASE MESA ORBITA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 600,
    "setup": 900,
    "codigo_barra": 66165
  },
  {
    "id_erp": 68462,
    "nome": "VOL 1/2 BASE MESA ORBITA MENOR",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 600,
    "setup": 900,
    "codigo_barra": 68462
  },
  {
    "id_erp": 35313,
    "nome": "VOL 1/2 BASE MESA ORNATA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 242,
    "setup": 900,
    "codigo_barra": 35313
  },
  {
    "id_erp": 70248,
    "nome": "VOL 1/2 BASE MESA OVAL",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.2,
    "setup": 900,
    "codigo_barra": 70248
  },
  {
    "id_erp": 64224,
    "nome": "VOL 1/2 BASE MESA PANAMERA 1,68",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 110,
    "setup": 900,
    "codigo_barra": 64224
  },
  {
    "id_erp": 62172,
    "nome": "VOL 1/2 BASE MESA PANAMERA 1,68 METAL",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 110,
    "setup": 900,
    "codigo_barra": 62172
  },
  {
    "id_erp": 59988,
    "nome": "VOL 1/2 BASE MESA PANAMERA 1,68/1,88/2,08",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 110,
    "setup": 900,
    "codigo_barra": 59988
  },
  {
    "id_erp": 64226,
    "nome": "VOL 1/2 BASE MESA PANAMERA 1,88/2,08",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 110,
    "setup": 900,
    "codigo_barra": 64226
  },
  {
    "id_erp": 64229,
    "nome": "VOL 1/2 BASE MESA PANAMERA 2,40",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 110,
    "setup": 900,
    "codigo_barra": 64229
  },
  {
    "id_erp": 59989,
    "nome": "VOL 1/2 BASE MESA PANAMERA 2,40",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 220,
    "setup": 900,
    "codigo_barra": 59989
  },
  {
    "id_erp": 64231,
    "nome": "VOL 1/2 BASE MESA PANAMERA 2,70/3,00",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 220,
    "setup": 900,
    "codigo_barra": 64231
  },
  {
    "id_erp": 59990,
    "nome": "VOL 1/2 BASE MESA PANAMERA 2,70/3,00 METAL",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 220,
    "setup": 900,
    "codigo_barra": 59990
  },
  {
    "id_erp": 68157,
    "nome": "VOL 1/2 BASE MESA PANAMERA 5,00 METAL",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 110,
    "setup": 900,
    "codigo_barra": 68157
  },
  {
    "id_erp": 37895,
    "nome": "VOL 1/2 BASE MESA PIETRA 2,20",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 775,
    "setup": 1500,
    "codigo_barra": 37895
  },
  {
    "id_erp": 38020,
    "nome": "VOL 1/2 BASE MESA PIETRA 2,20 ESPELHADA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 775,
    "setup": 1500,
    "codigo_barra": 38020
  },
  {
    "id_erp": 37769,
    "nome": "VOL 1/2 BASE MESA PIETRA 2,40",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 775,
    "setup": 1500,
    "codigo_barra": 37769
  },
  {
    "id_erp": 38018,
    "nome": "VOL 1/2 BASE MESA PIETRA 2,40 ESPELHADA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 775,
    "setup": 1500,
    "codigo_barra": 38018
  },
  {
    "id_erp": 35392,
    "nome": "VOL 1/2 BASE MESA PROVENCE 1,40",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 330,
    "setup": 900,
    "codigo_barra": 35392
  },
  {
    "id_erp": 34774,
    "nome": "VOL 1/2 BASE MESA PROVENCE 1,50",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 330,
    "setup": 900,
    "codigo_barra": 34774
  },
  {
    "id_erp": 34784,
    "nome": "VOL 1/2 BASE MESA PROVENCE 1,80/2,00",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 330,
    "setup": 900,
    "codigo_barra": 34784
  },
  {
    "id_erp": 34780,
    "nome": "VOL 1/2 BASE MESA PROVENCE 2,20",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 330,
    "setup": 900,
    "codigo_barra": 34780
  },
  {
    "id_erp": 49179,
    "nome": "VOL 1/2 BASE MESA SCALA 2,20/2,40",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 340,
    "setup": 900,
    "codigo_barra": 49179
  },
  {
    "id_erp": 49180,
    "nome": "VOL 1/2 BASE MESA SCALA 2,70/3,00",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 340,
    "setup": 900,
    "codigo_barra": 49180
  },
  {
    "id_erp": 71856,
    "nome": "VOL 1/2 BASE MESA SIENA 0,90",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 600,
    "setup": 900,
    "codigo_barra": 71856
  },
  {
    "id_erp": 79841,
    "nome": "VOL 1/2 BASE MESA SIENA 0,90 ALT. 650",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 600,
    "setup": 900,
    "codigo_barra": 79841
  },
  {
    "id_erp": 81745,
    "nome": "VOL 1/2 BASE MESA SIENA 0,90 ALT. 670. NOVA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 600,
    "setup": 900,
    "codigo_barra": 81745
  },
  {
    "id_erp": 81728,
    "nome": "VOL 1/2 BASE MESA SIENA 0,90 NOVA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 600,
    "setup": 900,
    "codigo_barra": 81728
  },
  {
    "id_erp": 51464,
    "nome": "VOL 1/2 BASE MESA SIENA 0,90/1,20/1,40",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 480,
    "setup": 900,
    "codigo_barra": 51464
  },
  {
    "id_erp": 68098,
    "nome": "VOL 1/2 BASE MESA SIENA 1,00",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 480,
    "setup": 900,
    "codigo_barra": 68098
  },
  {
    "id_erp": 73533,
    "nome": "VOL 1/2 BASE MESA SIENA 1,20/1,40 ALT. 650",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 600,
    "setup": 900,
    "codigo_barra": 73533
  },
  {
    "id_erp": 81775,
    "nome": "VOL 1/2 BASE MESA SIENA 1,20/1,40 ALT. 670. NOVA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 600,
    "setup": 900,
    "codigo_barra": 81775
  },
  {
    "id_erp": 81757,
    "nome": "VOL 1/2 BASE MESA SIENA 1,20/1,40 NOVA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 600,
    "setup": 900,
    "codigo_barra": 81757
  },
  {
    "id_erp": 73550,
    "nome": "VOL 1/2 BASE MESA SIENA 1,60 ALT. 650",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 600,
    "setup": 900,
    "codigo_barra": 73550
  },
  {
    "id_erp": 51466,
    "nome": "VOL 1/2 BASE MESA SIENA 1,60/1,80",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 480,
    "setup": 900,
    "codigo_barra": 51466
  },
  {
    "id_erp": 75077,
    "nome": "VOL 1/2 BASE MESA SIENA 1,60/1,80/2,00 C/ GIRATORIO",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.8,
    "setup": 900,
    "codigo_barra": 75077
  },
  {
    "id_erp": 81830,
    "nome": "VOL 1/2 BASE MESA SIENA 1,60/1,80/2,00 C/ GIRATORIO NOVA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.8,
    "setup": 900,
    "codigo_barra": 81830
  },
  {
    "id_erp": 81786,
    "nome": "VOL 1/2 BASE MESA SIENA 1,60/1,80/2,00 NOVA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.8,
    "setup": 900,
    "codigo_barra": 81786
  },
  {
    "id_erp": 47924,
    "nome": "VOL 1/2 BASE MESA TANGO",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 980,
    "setup": 1200,
    "codigo_barra": 47924
  },
  {
    "id_erp": 46371,
    "nome": "VOL 1/2 BASE MESA VERMONT 1,80/2,00/2,20/2,40",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 690,
    "setup": 900,
    "codigo_barra": 46371
  },
  {
    "id_erp": 47092,
    "nome": "VOL 1/2 BASE MESA VERMONT 2,70/3,00",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 690,
    "setup": 900,
    "codigo_barra": 47092
  },
  {
    "id_erp": 33171,
    "nome": "VOL 1/2 BASE MESA VICENZA 1,60/1,80",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 400,
    "setup": 900,
    "codigo_barra": 33171
  },
  {
    "id_erp": 33174,
    "nome": "VOL 1/2 BASE MESA VICENZA 2,00/2,20",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 400,
    "setup": 900,
    "codigo_barra": 33174
  },
  {
    "id_erp": 45322,
    "nome": "VOL 1/2 BASE MESA VITRA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 320,
    "setup": 900,
    "codigo_barra": 45322
  },
  {
    "id_erp": 50468,
    "nome": "VOL 1/2 BASE MESA VOLPI 1,20/1,40",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 300,
    "setup": 900,
    "codigo_barra": 50468
  },
  {
    "id_erp": 51052,
    "nome": "VOL 1/2 BASE MESA VOLPI 1,60/1,80",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 300,
    "setup": 900,
    "codigo_barra": 51052
  },
  {
    "id_erp": 50469,
    "nome": "VOL 1/2 BASE MESA VOLPI 2,00/2,20",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 300,
    "setup": 900,
    "codigo_barra": 50469
  },
  {
    "id_erp": 55070,
    "nome": "VOL 1/2 BASE NEPAL",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 300,
    "setup": 1200,
    "codigo_barra": 55070
  },
  {
    "id_erp": 72794,
    "nome": "VOL 1/2 BASE ORLA 1,40/1,60",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 600,
    "setup": 900,
    "codigo_barra": 72794
  },
  {
    "id_erp": 71945,
    "nome": "VOL 1/2 BASE ORLA 2,00",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 2.7,
    "setup": 900,
    "codigo_barra": 71945
  },
  {
    "id_erp": 64098,
    "nome": "VOL 1/2 BASE SCALA LX 1,80/2,00",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 305,
    "setup": 900,
    "codigo_barra": 64098
  },
  {
    "id_erp": 63833,
    "nome": "VOL 1/2 BASE SCALA LX 2,20/2,40",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 335,
    "setup": 900,
    "codigo_barra": 63833
  },
  {
    "id_erp": 63721,
    "nome": "VOL 1/2 BASE SCALA LX 2,70/3,00",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 335,
    "setup": 900,
    "codigo_barra": 63721
  },
  {
    "id_erp": 78569,
    "nome": "VOL 1/2 BASE TORA 1200/1400 RD",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.29,
    "setup": 1800,
    "codigo_barra": 78569
  },
  {
    "id_erp": 77196,
    "nome": "VOL 1/2 BASE TORA 2,20/2,40 X 1,28",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 2.914,
    "setup": 1800,
    "codigo_barra": 77196
  },
  {
    "id_erp": 76400,
    "nome": "VOL 1/2 BASE TORA 2,70/3,00/3,2 X 1,28",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 3.064,
    "setup": 1800,
    "codigo_barra": 76400
  },
  {
    "id_erp": 77202,
    "nome": "VOL 1/2 BASE TORA 2,70/3,00/3,20 X1,48",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 3.064,
    "setup": 1800,
    "codigo_barra": 77202
  },
  {
    "id_erp": 77198,
    "nome": "VOL 1/2 BASE TORA 3,50 X 1,28",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 3.064,
    "setup": 1800,
    "codigo_barra": 77198
  },
  {
    "id_erp": 76543,
    "nome": "VOL 1/2 BASE TORA 3,50 X 1,48",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 3.064,
    "setup": 1800,
    "codigo_barra": 76543
  },
  {
    "id_erp": 79124,
    "nome": "VOL 1/2 BASE TORA RED. 900",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.03,
    "setup": 1800,
    "codigo_barra": 79124
  },
  {
    "id_erp": 46951,
    "nome": "VOL 1/2 BASE UOMINI 1,40/1,60",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 700,
    "setup": 900,
    "codigo_barra": 46951
  },
  {
    "id_erp": 46987,
    "nome": "VOL 1/2 BASE UOMINI 2,20/2,40",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 700,
    "setup": 900,
    "codigo_barra": 46987
  },
  {
    "id_erp": 45872,
    "nome": "VOL 1/2 BASE UOMINI 2,70/3,00",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 700,
    "setup": 900,
    "codigo_barra": 45872
  },
  {
    "id_erp": 57671,
    "nome": "VOL 1/2 BASE UOMINI LX 2,20/2,40",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 700,
    "setup": 900,
    "codigo_barra": 57671
  },
  {
    "id_erp": 57511,
    "nome": "VOL 1/2 BASE UOMINI LX 2,70/3,00",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 700,
    "setup": 900,
    "codigo_barra": 57511
  },
  {
    "id_erp": 57969,
    "nome": "VOL 1/2 BASE UOMINI PLUS LX 1,40/1,60/1,80",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 700,
    "setup": 900,
    "codigo_barra": 57969
  },
  {
    "id_erp": 57672,
    "nome": "VOL 1/2 BASE UOMINI PLUS LX 2,00/2,19",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 700,
    "setup": 900,
    "codigo_barra": 57672
  },
  {
    "id_erp": 51130,
    "nome": "VOL 1/2 BASE VITAL 1,60/1,80",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 160,
    "setup": 900,
    "codigo_barra": 51130
  },
  {
    "id_erp": 50902,
    "nome": "VOL 1/2 BASE VITAL 2,00/2,20",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 160,
    "setup": 900,
    "codigo_barra": 50902
  },
  {
    "id_erp": 50901,
    "nome": "VOL 1/2 BASE VITAL PLUS 1,20/1,40/1,50",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 160,
    "setup": 900,
    "codigo_barra": 50901
  },
  {
    "id_erp": 83152,
    "nome": "VOL 1/2 BASE  MESA LAIKA 3,40",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 560,
    "setup": 900,
    "codigo_barra": 83152
  },
  {
    "id_erp": 40000,
    "nome": "VOL 1/2 CRISTALEIRA DUBLIN",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 110,
    "setup": 900,
    "codigo_barra": 40000
  },
  {
    "id_erp": 44423,
    "nome": "VOL 1/2 CRISTALEIRA DUBLIN C/ ESPELHO",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 100,
    "setup": 900,
    "codigo_barra": 44423
  },
  {
    "id_erp": 40006,
    "nome": "VOL 1/2 CRISTALEIRA DUBLIN DUPLA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 130,
    "setup": 900,
    "codigo_barra": 40006
  },
  {
    "id_erp": 44425,
    "nome": "VOL 1/2 CRISTALEIRA DUBLIN DUPLA C/ ESPELHO",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 120,
    "setup": 900,
    "codigo_barra": 44425
  },
  {
    "id_erp": 29266,
    "nome": "VOL 1/2 GAVETEIRO BUFFET NEVADA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 270,
    "setup": 900,
    "codigo_barra": 29266
  },
  {
    "id_erp": 14363,
    "nome": "VOL 1/2 LATERAL COLUNA LUANDA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 150,
    "setup": 900,
    "codigo_barra": 14363
  },
  {
    "id_erp": 36455,
    "nome": "VOL 1/2 PES APARADOR ASTI",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 65,
    "setup": 900,
    "codigo_barra": 36455
  },
  {
    "id_erp": 44805,
    "nome": "VOL 1/2 PES APARADOR CARDEAL",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 350,
    "setup": 900,
    "codigo_barra": 44805
  },
  {
    "id_erp": 69448,
    "nome": "VOL 1/2 PES APARADOR LEME 1,60/1,80/2,00",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 990,
    "setup": 900,
    "codigo_barra": 69448
  },
  {
    "id_erp": 66613,
    "nome": "VOL 1/2 PES BUFFET VOLPI 1,80",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 600,
    "setup": 900,
    "codigo_barra": 66613
  },
  {
    "id_erp": 61549,
    "nome": "VOL 1/2 PES ESTANTE DUBLIN",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 780,
    "setup": 900,
    "codigo_barra": 61549
  },
  {
    "id_erp": 35199,
    "nome": "VOL 1/2 PES MESA ASTI",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 65,
    "setup": 900,
    "codigo_barra": 35199
  },
  {
    "id_erp": 72608,
    "nome": "VOL 1/2 PES MESA CABECEIRA CEDRA LX 750",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 600,
    "setup": 900,
    "codigo_barra": 72608
  },
  {
    "id_erp": 72578,
    "nome": "VOL 1/2 PES MESA CABECEIRA VEDRA LX 550",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 600,
    "setup": 900,
    "codigo_barra": 72578
  },
  {
    "id_erp": 37180,
    "nome": "VOL 1/2 PES MESA LINCE",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 285,
    "setup": 900,
    "codigo_barra": 37180
  },
  {
    "id_erp": 43125,
    "nome": "VOL 1/2 PES MESA MILA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 65,
    "setup": 900,
    "codigo_barra": 43125
  },
  {
    "id_erp": 42171,
    "nome": "VOL 1/2 PES MESA NEO",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 647,
    "setup": 900,
    "codigo_barra": 42171
  },
  {
    "id_erp": 54997,
    "nome": "VOL 1/2 PES MESA NEO LX",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 647,
    "setup": 900,
    "codigo_barra": 54997
  },
  {
    "id_erp": 43098,
    "nome": "VOL 1/2 PES MESA RIVA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 370,
    "setup": 900,
    "codigo_barra": 43098
  },
  {
    "id_erp": 37025,
    "nome": "VOL 1/2 PES MESA SAMARA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 285,
    "setup": 900,
    "codigo_barra": 37025
  },
  {
    "id_erp": 24442,
    "nome": "VOL 1/2 TAMPO APARADOR BELLA B. MAD.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 60,
    "setup": 900,
    "codigo_barra": 24442
  },
  {
    "id_erp": 24216,
    "nome": "VOL 1/2 TAMPO MESA PRADES/BELLA T. M. 2,00",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 80,
    "setup": 900,
    "codigo_barra": 24216
  },
  {
    "id_erp": 21872,
    "nome": "VOL 1/3 BASE CRISTALEIRA CAROLINA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 115,
    "setup": 900,
    "codigo_barra": 21872
  },
  {
    "id_erp": 31826,
    "nome": "VOL 1/3 BASE CRISTALEIRA CAROLINA DUPLA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 115,
    "setup": 900,
    "codigo_barra": 31826
  },
  {
    "id_erp": 464,
    "nome": "VOL 1/3 BASE CRISTALEIRA PORTINARI VIDRO",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 240,
    "setup": 900,
    "codigo_barra": 464
  },
  {
    "id_erp": 34204,
    "nome": "VOL 1/3 LATERAL MESA ELEGANCE",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 170,
    "setup": 480,
    "codigo_barra": 34204
  },
  {
    "id_erp": 33345,
    "nome": "VOL 1/4 BASE CRISTALEIRA PORTINARI MAD. DUPLA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 115,
    "setup": 900,
    "codigo_barra": 33345
  },
  {
    "id_erp": 333459,
    "nome": "VOL 1/4 BASE CRISTALEIRA PORTINARI MAD. DUPLA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 130,
    "setup": 900,
    "codigo_barra": 333459
  },
  {
    "id_erp": 15138,
    "nome": "VOL 1/4 BASE CRISTALEIRA PORTINARI MAD. LUMINARIA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 80,
    "setup": 900,
    "codigo_barra": 15138
  },
  {
    "id_erp": 151389,
    "nome": "VOL 1/4 BASE CRISTALEIRA PORTINARI MAD. LUMINARIA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 90,
    "setup": 900,
    "codigo_barra": 151389
  },
  {
    "id_erp": 22720,
    "nome": "VOL 1/4 BASE EXPOSITOR CADEIRAS",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 195,
    "setup": 900,
    "codigo_barra": 22720
  },
  {
    "id_erp": 43693,
    "nome": "VOL 1-2/3 BASE MESA CALIANDRA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.06,
    "setup": 900,
    "codigo_barra": 43693
  },
  {
    "id_erp": 31564,
    "nome": "VOL 2/2 BARRA 1050 COLUNA LIANE",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 84,
    "setup": 900,
    "codigo_barra": 31564
  },
  {
    "id_erp": 36336,
    "nome": "VOL 2/2 BARRA 1300 COLUNA LIANE",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 84,
    "setup": 900,
    "codigo_barra": 36336
  },
  {
    "id_erp": 31566,
    "nome": "VOL 2/2 BARRA 550 COLUNA LIANE",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 84,
    "setup": 900,
    "codigo_barra": 31566
  },
  {
    "id_erp": 31565,
    "nome": "VOL 2/2 BARRA 800 COLUNA LIANE",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 84,
    "setup": 900,
    "codigo_barra": 31565
  },
  {
    "id_erp": 24215,
    "nome": "VOL 2/2 BASE MESA PRADES",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 80,
    "setup": 900,
    "codigo_barra": 24215
  },
  {
    "id_erp": 61493,
    "nome": "VOL 2/2 BUFFET BERLIM 1,52 PES METAL",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 200,
    "setup": 900,
    "codigo_barra": 61493
  },
  {
    "id_erp": 61495,
    "nome": "VOL 2/2 BUFFET BERLIM 2,00 PES METAL",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 230,
    "setup": 900,
    "codigo_barra": 61495
  },
  {
    "id_erp": 61497,
    "nome": "VOL 2/2 BUFFET BERLIM 2,50 PES METAL",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 300,
    "setup": 900,
    "codigo_barra": 61497
  },
  {
    "id_erp": 66614,
    "nome": "VOL 2/2 BUFFET VOLPI 1,80",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 441,
    "setup": 900,
    "codigo_barra": 66614
  },
  {
    "id_erp": 66616,
    "nome": "VOL 2/2 BUFFET VOLPI 2,20",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 528,
    "setup": 900,
    "codigo_barra": 66616
  },
  {
    "id_erp": 66618,
    "nome": "VOL 2/2 BUFFET VOLPI 2,50",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 548,
    "setup": 900,
    "codigo_barra": 66618
  },
  {
    "id_erp": 61550,
    "nome": "VOL 2/2 ESTANTE DUBLIN",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.02,
    "setup": 900,
    "codigo_barra": 61550
  },
  {
    "id_erp": 66608,
    "nome": "VOL 2/2 HOME VOLPI 1,80",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 314,
    "setup": 900,
    "codigo_barra": 66608
  },
  {
    "id_erp": 66610,
    "nome": "VOL 2/2 HOME VOLPI 2,20",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 469,
    "setup": 900,
    "codigo_barra": 66610
  },
  {
    "id_erp": 66612,
    "nome": "VOL 2/2 HOME VOLPI 2,50",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 494,
    "setup": 900,
    "codigo_barra": 66612
  },
  {
    "id_erp": 72579,
    "nome": "VOL 2/2 MESA CABECEIRA VEDRA LX 550 1 GAVETA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 600,
    "setup": 900,
    "codigo_barra": 72579
  },
  {
    "id_erp": 72610,
    "nome": "VOL 2/2 MESA CABECEIRA VEDRA LX 550 2 GAVETAS",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 600,
    "setup": 900,
    "codigo_barra": 72610
  },
  {
    "id_erp": 72669,
    "nome": "VOL 2/2 MESA CABECEIRA VEDRA LX 750 1 GAVETA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 600,
    "setup": 900,
    "codigo_barra": 72669
  },
  {
    "id_erp": 72701,
    "nome": "VOL 2/2 MESA CABECEIRA VEDRA LX 750 2 GAVETAS",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 600,
    "setup": 900,
    "codigo_barra": 72701
  },
  {
    "id_erp": 24443,
    "nome": "VOL 2/2 PE APARADOR BELLA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 235,
    "setup": 900,
    "codigo_barra": 24443
  },
  {
    "id_erp": 34644,
    "nome": "VOL 2/2 PES APARADOR MONTREAL",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 290,
    "setup": 900,
    "codigo_barra": 34644
  },
  {
    "id_erp": 79646,
    "nome": "VOL 2/2 PRATELEIRA APARADOR LUCCE 1,20",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 360,
    "setup": 900,
    "codigo_barra": 79646
  },
  {
    "id_erp": 63711,
    "nome": "VOL 2/2 PRATELEIRA APARADOR LUCCE 1,40",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 360,
    "setup": 900,
    "codigo_barra": 63711
  },
  {
    "id_erp": 63802,
    "nome": "VOL 2/2 PRATELEIRA APARADOR LUCCE 1,60",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 360,
    "setup": 900,
    "codigo_barra": 63802
  },
  {
    "id_erp": 61451,
    "nome": "VOL 2/2 PRATELEIRA APARADOR LUCCE 1,80",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 360,
    "setup": 900,
    "codigo_barra": 61451
  },
  {
    "id_erp": 61459,
    "nome": "VOL 2/2 PRATELEIRA APARADOR LUCCE 2,20",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 390,
    "setup": 900,
    "codigo_barra": 61459
  },
  {
    "id_erp": 61463,
    "nome": "VOL 2/2 PRATELEIRA APARADOR LUCCE 2,60",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 420,
    "setup": 900,
    "codigo_barra": 61463
  },
  {
    "id_erp": 77062,
    "nome": "VOL 2/2 PRATELEIRA ESTANTE PLANA 1100",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.232,
    "setup": 900,
    "codigo_barra": 77062
  },
  {
    "id_erp": 77105,
    "nome": "VOL 2/2 PRATELEIRA ESTANTE PLANA 1300",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.415,
    "setup": 900,
    "codigo_barra": 77105
  },
  {
    "id_erp": 77106,
    "nome": "VOL 2/2 PRATELEIRA ESTANTE PLANA 1400",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.438,
    "setup": 900,
    "codigo_barra": 77106
  },
  {
    "id_erp": 38021,
    "nome": "VOL 2/2 T. ESP. PIETRA 2,20",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 133,
    "setup": 900,
    "codigo_barra": 38021
  },
  {
    "id_erp": 38019,
    "nome": "VOL 2/2 T. ESP. PIETRA 2,40",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 133,
    "setup": 900,
    "codigo_barra": 38019
  },
  {
    "id_erp": 55032,
    "nome": "VOL 2/2 T. LACA APARADOR ASTI 1,20",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 100,
    "setup": 900,
    "codigo_barra": 55032
  },
  {
    "id_erp": 55033,
    "nome": "VOL 2/2 T. LACA APARADOR ASTI 1,40",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 100,
    "setup": 900,
    "codigo_barra": 55033
  },
  {
    "id_erp": 55034,
    "nome": "VOL 2/2 T. LACA APARADOR ASTI 1,60",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 100,
    "setup": 900,
    "codigo_barra": 55034
  },
  {
    "id_erp": 69705,
    "nome": "VOL 2/2 T. LACA APARADOR LEME 1,60",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.14,
    "setup": 900,
    "codigo_barra": 69705
  },
  {
    "id_erp": 69707,
    "nome": "VOL 2/2 T. LACA APARADOR LEME 1,80",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.14,
    "setup": 900,
    "codigo_barra": 69707
  },
  {
    "id_erp": 69712,
    "nome": "VOL 2/2 T. LACA APARADOR LEME 2,00",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.14,
    "setup": 900,
    "codigo_barra": 69712
  },
  {
    "id_erp": 59129,
    "nome": "VOL 2/2 T. LACA SIENA 1,40 RED.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 100,
    "setup": 900,
    "codigo_barra": 59129
  },
  {
    "id_erp": 82344,
    "nome": "VOL 2/2 T. MAD LEME 3,40 X 1,40 - MEDIDA ESPECIAL",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.02,
    "setup": 900,
    "codigo_barra": 82344
  },
  {
    "id_erp": 70024,
    "nome": "VOL 2/2 T. MAD MILA 0,80 RED.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 600,
    "setup": 900,
    "codigo_barra": 70024
  },
  {
    "id_erp": 72010,
    "nome": "VOL 2/2 T. MAD ORLA 2,00 S/ GIRATORIO",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 600,
    "setup": 900,
    "codigo_barra": 72010
  },
  {
    "id_erp": 81949,
    "nome": "VOL 2/2 T. MAD TRIADE",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 102,
    "setup": 900,
    "codigo_barra": 81949
  },
  {
    "id_erp": 71482,
    "nome": "VOL 2/2 T. MAD. AMBAR 1,40 X 1,00",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 600,
    "setup": 900,
    "codigo_barra": 71482
  },
  {
    "id_erp": 714829,
    "nome": "VOL 2/2 T. MAD. AMBAR 1,40 X 1,00",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 600,
    "setup": 900,
    "codigo_barra": 714829
  },
  {
    "id_erp": 75735,
    "nome": "VOL 2/2 T. MAD. AMBAR 1,40 X 1,00 SB",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 600,
    "setup": 900,
    "codigo_barra": 75735
  },
  {
    "id_erp": 81228,
    "nome": "VOL 2/2 T. MAD. AMBAR CORPORATIVA 1,40",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 600,
    "setup": 900,
    "codigo_barra": 81228
  },
  {
    "id_erp": 69520,
    "nome": "VOL 2/2 T. MAD. APARADOR LEME 1,60",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 268,
    "setup": 900,
    "codigo_barra": 69520
  },
  {
    "id_erp": 69449,
    "nome": "VOL 2/2 T. MAD. APARADOR LEME 1,80",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.2,
    "setup": 900,
    "codigo_barra": 69449
  },
  {
    "id_erp": 69538,
    "nome": "VOL 2/2 T. MAD. APARADOR LEME 2,00",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.14,
    "setup": 900,
    "codigo_barra": 69538
  },
  {
    "id_erp": 44021,
    "nome": "VOL 2/2 T. MAD. BISTRO CALIANDRA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 180,
    "setup": 900,
    "codigo_barra": 44021
  },
  {
    "id_erp": 75245,
    "nome": "VOL 2/2 T. MAD. DUNA LX 1,20 QUAD. - MEDIDA ESPECIAL",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.08,
    "setup": 900,
    "codigo_barra": 75245
  },
  {
    "id_erp": 55064,
    "nome": "VOL 2/2 T. MAD. DUNA PLUS LX 1,40 QUAD.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 200,
    "setup": 900,
    "codigo_barra": 55064
  },
  {
    "id_erp": 55065,
    "nome": "VOL 2/2 T. MAD. DUNA PLUS LX 1,50 QUAD.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 200,
    "setup": 900,
    "codigo_barra": 55065
  },
  {
    "id_erp": 55066,
    "nome": "VOL 2/2 T. MAD. DUNA PLUS LX 1,60 QUAD.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 200,
    "setup": 900,
    "codigo_barra": 55066
  },
  {
    "id_erp": 68146,
    "nome": "VOL 2/2 T. MAD. ELOA 1,80 QUAD. - FEIRA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.14,
    "setup": 900,
    "codigo_barra": 68146
  },
  {
    "id_erp": 79727,
    "nome": "VOL 2/2 T. MAD. FUNGI",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.71,
    "setup": 900,
    "codigo_barra": 79727
  },
  {
    "id_erp": 70660,
    "nome": "VOL 2/2 T. MAD. FUNGI 1,60 ORGANICA  S/ GIRATORIO (1ª ETAPA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.38,
    "setup": 900,
    "codigo_barra": 70660
  },
  {
    "id_erp": 706609,
    "nome": "VOL 2/2 T. MAD. FUNGI 1,60 ORGANICA  S/ GIRATORIO (2ª ETAPA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.38,
    "setup": 900,
    "codigo_barra": 706609
  },
  {
    "id_erp": 73076,
    "nome": "VOL 2/2 T. MAD. FUNGI 1,60 ORGANICA C/ GIRATORIO (1ª ETAPA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.2,
    "setup": 900,
    "codigo_barra": 73076
  },
  {
    "id_erp": 730769,
    "nome": "VOL 2/2 T. MAD. FUNGI 1,60 ORGANICA C/ GIRATORIO (2ª ETAPA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.2,
    "setup": 900,
    "codigo_barra": 730769
  },
  {
    "id_erp": 73080,
    "nome": "VOL 2/2 T. MAD. FUNGI 1,80 ORGANICA C/ GIRATORIO (1ª ETAPA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.32,
    "setup": 900,
    "codigo_barra": 73080
  },
  {
    "id_erp": 730809,
    "nome": "VOL 2/2 T. MAD. FUNGI 1,80 ORGANICA C/ GIRATORIO (2ª ETAPA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.32,
    "setup": 900,
    "codigo_barra": 730809
  },
  {
    "id_erp": 70848,
    "nome": "VOL 2/2 T. MAD. FUNGI 1,80 ORGANICA S/ GIRATORIO (1ª ETAPA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.2,
    "setup": 900,
    "codigo_barra": 70848
  },
  {
    "id_erp": 708489,
    "nome": "VOL 2/2 T. MAD. FUNGI 1,80 ORGANICA S/ GIRATORIO (2ª ETAPA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.2,
    "setup": 900,
    "codigo_barra": 708489
  },
  {
    "id_erp": 64360,
    "nome": "VOL 2/2 T. MAD. FUNGI 2,00",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 600,
    "setup": 900,
    "codigo_barra": 64360
  },
  {
    "id_erp": 66407,
    "nome": "VOL 2/2 T. MAD. FUNGI 2,00 ORGANICA (1ª ETAPA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.38,
    "setup": 900,
    "codigo_barra": 66407
  },
  {
    "id_erp": 664079,
    "nome": "VOL 2/2 T. MAD. FUNGI 2,00 ORGANICA (2ª ETAPA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.38,
    "setup": 900,
    "codigo_barra": 664079
  },
  {
    "id_erp": 73118,
    "nome": "VOL 2/2 T. MAD. FUNGI 2,00 ORGANICA C/ GIRATORIO (1ª ETAPA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.2,
    "setup": 900,
    "codigo_barra": 73118
  },
  {
    "id_erp": 731189,
    "nome": "VOL 2/2 T. MAD. FUNGI 2,00 ORGANICA C/ GIRATORIO (2ª ETAPA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.2,
    "setup": 900,
    "codigo_barra": 731189
  },
  {
    "id_erp": 77657,
    "nome": "VOL 2/2 T. MAD. FUNGI 2,00  X 1,10 - MEDIDA ESPECIAL",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 600,
    "setup": 900,
    "codigo_barra": 77657
  },
  {
    "id_erp": 64362,
    "nome": "VOL 2/2 T. MAD. FUNGI 2,20",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.38,
    "setup": 900,
    "codigo_barra": 64362
  },
  {
    "id_erp": 659479,
    "nome": "VOL 2/2 T. MAD. FUNGI 2,20 ORGANICA  S/ GIRATORIO (2ª ETAPA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.38,
    "setup": 900,
    "codigo_barra": 659479
  },
  {
    "id_erp": 73111,
    "nome": "VOL 2/2 T. MAD. FUNGI 2,20 ORGANICA C/ GIRATORIO (1ª ETAPA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.2,
    "setup": 900,
    "codigo_barra": 73111
  },
  {
    "id_erp": 731119,
    "nome": "VOL 2/2 T. MAD. FUNGI 2,20 ORGANICA C/ GIRATORIO (2ª ETAPA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.2,
    "setup": 900,
    "codigo_barra": 731119
  },
  {
    "id_erp": 65947,
    "nome": "VOL 2/2 T. MAD. FUNGI 2,20 ORGANICA S/ GIRATORIO (1ª ETAPA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.38,
    "setup": 900,
    "codigo_barra": 65947
  },
  {
    "id_erp": 64363,
    "nome": "VOL 2/2 T. MAD. FUNGI 2,40",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.38,
    "setup": 900,
    "codigo_barra": 64363
  },
  {
    "id_erp": 66445,
    "nome": "VOL 2/2 T. MAD. FUNGI 2,40 ORGANICA  S/ GIRATORIO (1ª ETAPA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.38,
    "setup": 900,
    "codigo_barra": 66445
  },
  {
    "id_erp": 664459,
    "nome": "VOL 2/2 T. MAD. FUNGI 2,40 ORGANICA  S/ GIRATORIO (2ª ETAPA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.38,
    "setup": 900,
    "codigo_barra": 664459
  },
  {
    "id_erp": 73128,
    "nome": "VOL 2/2 T. MAD. FUNGI 2,40 ORGANICA C/ GIRATORIO (1ª ETAPA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.2,
    "setup": 900,
    "codigo_barra": 73128
  },
  {
    "id_erp": 731289,
    "nome": "VOL 2/2 T. MAD. FUNGI 2,40 ORGANICA C/ GIRATORIO (2ª ETAPA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.2,
    "setup": 900,
    "codigo_barra": 731289
  },
  {
    "id_erp": 73532,
    "nome": "VOL 2/2 T. MAD. FUNGI 2,40 X 1,50 - MEDIDA ESPECIAL  (1ª ETAPA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.2,
    "setup": 900,
    "codigo_barra": 73532
  },
  {
    "id_erp": 64364,
    "nome": "VOL 2/2 T. MAD. FUNGI 2,70",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.71,
    "setup": 900,
    "codigo_barra": 64364
  },
  {
    "id_erp": 74836,
    "nome": "VOL 2/2 T. MAD. FUNGI 2,70 X 1,40 - MEDIDA ESPECIAL",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.71,
    "setup": 900,
    "codigo_barra": 74836
  },
  {
    "id_erp": 67998,
    "nome": "VOL 2/2 T. MAD. FUNGI 2,80 X 1,40 - MEDIDA ESPECIAL",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.38,
    "setup": 900,
    "codigo_barra": 67998
  },
  {
    "id_erp": 64365,
    "nome": "VOL 2/2 T. MAD. FUNGI 3,00",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.38,
    "setup": 900,
    "codigo_barra": 64365
  },
  {
    "id_erp": 70246,
    "nome": "VOL 2/2 T. MAD. FUNGI 3,20 - MEDIDA ESPECIAL",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.38,
    "setup": 900,
    "codigo_barra": 70246
  },
  {
    "id_erp": 71356,
    "nome": "VOL 2/2 T. MAD. FUNGI 3,20 X 1,50",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.8,
    "setup": 900,
    "codigo_barra": 71356
  },
  {
    "id_erp": 79549,
    "nome": "VOL 2/2 T. MAD. FUNGI 3,20 X 1,50",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.8,
    "setup": 900,
    "codigo_barra": 79549
  },
  {
    "id_erp": 71893,
    "nome": "VOL 2/2 T. MAD. FUNGI 3,40 X 1,50",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.2,
    "setup": 900,
    "codigo_barra": 71893
  },
  {
    "id_erp": 75422,
    "nome": "VOL 2/2 T. MAD. FUNGI 3,50 X 1,20 - MEDIDA ESPECIA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.8,
    "setup": 900,
    "codigo_barra": 75422
  },
  {
    "id_erp": 41743,
    "nome": "VOL 2/2 T. MAD. GENEBRA 1,60",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 102,
    "setup": 900,
    "codigo_barra": 41743
  },
  {
    "id_erp": 76719,
    "nome": "VOL 2/2 T. MAD. GUANABARA 1,80 X 1,00 (1ª ETAPA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.2,
    "setup": 900,
    "codigo_barra": 76719
  },
  {
    "id_erp": 767199,
    "nome": "VOL 2/2 T. MAD. GUANABARA 1,80 X 1,00 (2ª ETAPA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.2,
    "setup": 900,
    "codigo_barra": 767199
  },
  {
    "id_erp": 77383,
    "nome": "VOL 2/2 T. MAD. GUANABARA 1,80 X 1,10 -MEDIDA ESPECIAL",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.2,
    "setup": 900,
    "codigo_barra": 77383
  },
  {
    "id_erp": 76757,
    "nome": "VOL 2/2 T. MAD. GUANABARA 2,00 X 1,10 (1ª ETAPA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.32,
    "setup": 900,
    "codigo_barra": 76757
  },
  {
    "id_erp": 767579,
    "nome": "VOL 2/2 T. MAD. GUANABARA 2,00 X 1,10 (2ª ETAPA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.32,
    "setup": 900,
    "codigo_barra": 767579
  },
  {
    "id_erp": 68922,
    "nome": "VOL 2/2 T. MAD. GUANABARA 2,20 (1ª ETAPA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.8,
    "setup": 900,
    "codigo_barra": 68922
  },
  {
    "id_erp": 689229,
    "nome": "VOL 2/2 T. MAD. GUANABARA 2,20 (2ª ETAPA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.8,
    "setup": 900,
    "codigo_barra": 689229
  },
  {
    "id_erp": 68937,
    "nome": "VOL 2/2 T. MAD. GUANABARA 2,40 (1ª ETAPA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.32,
    "setup": 900,
    "codigo_barra": 68937
  },
  {
    "id_erp": 689379,
    "nome": "VOL 2/2 T. MAD. GUANABARA 2,40 (2ª ETAPA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.32,
    "setup": 900,
    "codigo_barra": 689379
  },
  {
    "id_erp": 68861,
    "nome": "VOL 2/2 T. MAD. GUANABARA 2,70 (1ª ETAPA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.32,
    "setup": 900,
    "codigo_barra": 68861
  },
  {
    "id_erp": 688619,
    "nome": "VOL 2/2 T. MAD. GUANABARA 2,70 (2ª ETAPA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.32,
    "setup": 900,
    "codigo_barra": 688619
  },
  {
    "id_erp": 68953,
    "nome": "VOL 2/2 T. MAD. GUANABARA 3,00 (1ª ETAPA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.32,
    "setup": 900,
    "codigo_barra": 68953
  },
  {
    "id_erp": 689539,
    "nome": "VOL 2/2 T. MAD. GUANABARA 3,00 (2ª ETAPA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.32,
    "setup": 900,
    "codigo_barra": 689539
  },
  {
    "id_erp": 68672,
    "nome": "VOL 2/2 T. MAD. HELIX 2,20 (1ª ETAPA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.02,
    "setup": 900,
    "codigo_barra": 68672
  },
  {
    "id_erp": 686729,
    "nome": "VOL 2/2 T. MAD. HELIX 2,20 (2ª ETAPA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.02,
    "setup": 900,
    "codigo_barra": 686729
  },
  {
    "id_erp": 68652,
    "nome": "VOL 2/2 T. MAD. HELIX 2,40 (1ª ETAPA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.02,
    "setup": 900,
    "codigo_barra": 68652
  },
  {
    "id_erp": 686529,
    "nome": "VOL 2/2 T. MAD. HELIX 2,40 (2ª ETAPA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.02,
    "setup": 900,
    "codigo_barra": 686529
  },
  {
    "id_erp": 68621,
    "nome": "VOL 2/2 T. MAD. HELIX 2,70 (1ª ETAPA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.02,
    "setup": 900,
    "codigo_barra": 68621
  },
  {
    "id_erp": 686219,
    "nome": "VOL 2/2 T. MAD. HELIX 2,70 (2ª ETAPA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.02,
    "setup": 900,
    "codigo_barra": 686219
  },
  {
    "id_erp": 68445,
    "nome": "VOL 2/2 T. MAD. HELIX 3,00 (1ª ETAPA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.02,
    "setup": 900,
    "codigo_barra": 68445
  },
  {
    "id_erp": 684459,
    "nome": "VOL 2/2 T. MAD. HELIX 3,00 (2ª ETAPA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.02,
    "setup": 900,
    "codigo_barra": 684459
  },
  {
    "id_erp": 70872,
    "nome": "VOL 2/2 T. MAD. HELIX 3,20 -  (MEDIDA ESPECIAL)  (1ª ETAPA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.74,
    "setup": 900,
    "codigo_barra": 70872
  },
  {
    "id_erp": 708729,
    "nome": "VOL 2/2 T. MAD. HELIX 3,20 -  (MEDIDA ESPECIAL)  (2ª ETAPA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.74,
    "setup": 900,
    "codigo_barra": 708729
  },
  {
    "id_erp": 52164,
    "nome": "VOL 2/2 T. MAD. INDIGO 1,46 B. MAD. RED.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 726,
    "setup": 1200,
    "codigo_barra": 52164
  },
  {
    "id_erp": 521649,
    "nome": "VOL 2/2 T. MAD. INDIGO 1,46 B. MAD. RED.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 350,
    "setup": 900,
    "codigo_barra": 521649
  },
  {
    "id_erp": 54588,
    "nome": "VOL 2/2 T. MAD. INDIGO 1,46 B. MAD. RED. S/ GIRATORIO",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 726,
    "setup": 1200,
    "codigo_barra": 54588
  },
  {
    "id_erp": 545889,
    "nome": "VOL 2/2 T. MAD. INDIGO 1,46 B. MAD. RED. S/ GIRATORIO",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 350,
    "setup": 900,
    "codigo_barra": 545889
  },
  {
    "id_erp": 52165,
    "nome": "VOL 2/2 T. MAD. INDIGO 1,66 B. MAD. RED.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 726,
    "setup": 1200,
    "codigo_barra": 52165
  },
  {
    "id_erp": 521659,
    "nome": "VOL 2/2 T. MAD. INDIGO 1,66 B. MAD. RED.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 350,
    "setup": 900,
    "codigo_barra": 521659
  },
  {
    "id_erp": 54589,
    "nome": "VOL 2/2 T. MAD. INDIGO 1,66 B. MAD. RED. S/ GIRATORIO",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 726,
    "setup": 1200,
    "codigo_barra": 54589
  },
  {
    "id_erp": 545899,
    "nome": "VOL 2/2 T. MAD. INDIGO 1,66 B. MAD. RED. S/ GIRATORIO",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 350,
    "setup": 900,
    "codigo_barra": 545899
  },
  {
    "id_erp": 52166,
    "nome": "VOL 2/2 T. MAD. INDIGO 1,86 B. MAD. RED.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 726,
    "setup": 1200,
    "codigo_barra": 52166
  },
  {
    "id_erp": 521669,
    "nome": "VOL 2/2 T. MAD. INDIGO 1,86 B. MAD. RED.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 350,
    "setup": 900,
    "codigo_barra": 521669
  },
  {
    "id_erp": 54590,
    "nome": "VOL 2/2 T. MAD. INDIGO 1,86 B. MAD. RED. S/ GIRATORIO",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 726,
    "setup": 1200,
    "codigo_barra": 54590
  },
  {
    "id_erp": 545909,
    "nome": "VOL 2/2 T. MAD. INDIGO 1,86 B. MAD. RED. S/ GIRATORIO",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 350,
    "setup": 900,
    "codigo_barra": 545909
  },
  {
    "id_erp": 61771,
    "nome": "VOL 2/2 T. MAD. INDIGO 2,04",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.08,
    "setup": 900,
    "codigo_barra": 61771
  },
  {
    "id_erp": 617719,
    "nome": "VOL 2/2 T. MAD. INDIGO 2,04",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.08,
    "setup": 900,
    "codigo_barra": 617719
  },
  {
    "id_erp": 73632,
    "nome": "VOL 2/2 T. MAD. INDIGO 2,04 C/ GIRATORIO",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.08,
    "setup": 900,
    "codigo_barra": 73632
  },
  {
    "id_erp": 736329,
    "nome": "VOL 2/2 T. MAD. INDIGO 2,04 C/ GIRATORIO",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.08,
    "setup": 900,
    "codigo_barra": 736329
  },
  {
    "id_erp": 76375,
    "nome": "VOL 2/2 T. MAD. LEME 2,00 X 1,00",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.02,
    "setup": 900,
    "codigo_barra": 76375
  },
  {
    "id_erp": 68478,
    "nome": "VOL 2/2 T. MAD. LEME 2,20",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.02,
    "setup": 900,
    "codigo_barra": 68478
  },
  {
    "id_erp": 83591,
    "nome": "VOL 2/2 T. MAD. LEME 2,20 X 0,90 - MEDIDA ESPECIAL",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.02,
    "setup": 900,
    "codigo_barra": 83591
  },
  {
    "id_erp": 68479,
    "nome": "VOL 2/2 T. MAD. LEME 2,40",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.02,
    "setup": 900,
    "codigo_barra": 68479
  },
  {
    "id_erp": 74720,
    "nome": "VOL 2/2 T. MAD. LEME 2,40 X 1,10 - MEDIDA ESPECIAL",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 600,
    "setup": 900,
    "codigo_barra": 74720
  },
  {
    "id_erp": 68480,
    "nome": "VOL 2/2 T. MAD. LEME 2,70 - FEIRA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 840,
    "setup": 900,
    "codigo_barra": 68480
  },
  {
    "id_erp": 84567,
    "nome": "VOL 2/2 T. MAD. LEME 2,70 X 1,10 - MEDIDA ESPECIAL",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.02,
    "setup": 900,
    "codigo_barra": 84567
  },
  {
    "id_erp": 68481,
    "nome": "VOL 2/2 T. MAD. LEME 3,00",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.02,
    "setup": 900,
    "codigo_barra": 68481
  },
  {
    "id_erp": 34193,
    "nome": "VOL 2/2 T. MAD. LINEA 1,08 QUAD.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 90,
    "setup": 900,
    "codigo_barra": 34193
  },
  {
    "id_erp": 55132,
    "nome": "VOL 2/2 T. MAD. LINEA/MENFIS 1,20 RED.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 90,
    "setup": 900,
    "codigo_barra": 55132
  },
  {
    "id_erp": 52495,
    "nome": "VOL 2/2 T. MAD. MARIN 1,80",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 200,
    "setup": 900,
    "codigo_barra": 52495
  },
  {
    "id_erp": 56313,
    "nome": "VOL 2/2 T. MAD. MARIN 2,00",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 200,
    "setup": 900,
    "codigo_barra": 56313
  },
  {
    "id_erp": 56416,
    "nome": "VOL 2/2 T. MAD. MARIN 2,20",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 100,
    "setup": 900,
    "codigo_barra": 56416
  },
  {
    "id_erp": 56417,
    "nome": "VOL 2/2 T. MAD. MARIN 2,40",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 200,
    "setup": 900,
    "codigo_barra": 56417
  },
  {
    "id_erp": 52708,
    "nome": "VOL 2/2 T. MAD. MARIN 2,70",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 200,
    "setup": 900,
    "codigo_barra": 52708
  },
  {
    "id_erp": 52709,
    "nome": "VOL 2/2 T. MAD. MARIN 3,00",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 200,
    "setup": 900,
    "codigo_barra": 52709
  },
  {
    "id_erp": 52499,
    "nome": "VOL 2/2 T. MAD. MARIN PLUS 1,40",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 200,
    "setup": 900,
    "codigo_barra": 52499
  },
  {
    "id_erp": 52500,
    "nome": "VOL 2/2 T. MAD. MARIN PLUS 1,60",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 200,
    "setup": 900,
    "codigo_barra": 52500
  },
  {
    "id_erp": 41753,
    "nome": "VOL 2/2 T. MAD. MENFIS/LINEA/ELIS 1,20 RED.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 90,
    "setup": 900,
    "codigo_barra": 41753
  },
  {
    "id_erp": 34520,
    "nome": "VOL 2/2 T. MAD. MENFIS/LINEA/MARR/MILA 1,06 RED.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 90,
    "setup": 900,
    "codigo_barra": 34520
  },
  {
    "id_erp": 34519,
    "nome": "VOL 2/2 T. MAD. MENFIS/LINEA/MARROCOS 1,08 QUAD.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 90,
    "setup": 900,
    "codigo_barra": 34519
  },
  {
    "id_erp": 34518,
    "nome": "VOL 2/2 T. MAD. MENFIS/LINEA/MARROCOS 1,20 X 0,90",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 90,
    "setup": 900,
    "codigo_barra": 34518
  },
  {
    "id_erp": 42398,
    "nome": "VOL 2/2 T. MAD. MENFIS/LINEA/MARROCOS 1,40 X 0,90",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 90,
    "setup": 900,
    "codigo_barra": 42398
  },
  {
    "id_erp": 42418,
    "nome": "VOL 2/2 T. MAD. MENFIS/LINEA/MARROCOS 1,60 X 0,90",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 90,
    "setup": 900,
    "codigo_barra": 42418
  },
  {
    "id_erp": 55146,
    "nome": "VOL 2/2 T. MAD. MILA 0,90 RED.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 90,
    "setup": 900,
    "codigo_barra": 55146
  },
  {
    "id_erp": 44014,
    "nome": "VOL 2/2 T. MAD. MILA 1,08 QUAD.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 102,
    "setup": 900,
    "codigo_barra": 44014
  },
  {
    "id_erp": 55147,
    "nome": "VOL 2/2 T. MAD. MILA 1,20 RED.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 90,
    "setup": 900,
    "codigo_barra": 55147
  },
  {
    "id_erp": 44016,
    "nome": "VOL 2/2 T. MAD. MILA 1,20 X 0,90",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 102,
    "setup": 900,
    "codigo_barra": 44016
  },
  {
    "id_erp": 44018,
    "nome": "VOL 2/2 T. MAD. MILA 1,40 X 0,90",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 102,
    "setup": 900,
    "codigo_barra": 44018
  },
  {
    "id_erp": 52491,
    "nome": "VOL 2/2 T. MAD. NEO 1,60",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 240,
    "setup": 900,
    "codigo_barra": 52491
  },
  {
    "id_erp": 52492,
    "nome": "VOL 2/2 T. MAD. NEO 1,80",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 240,
    "setup": 900,
    "codigo_barra": 52492
  },
  {
    "id_erp": 52493,
    "nome": "VOL 2/2 T. MAD. NEO 2,00",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 240,
    "setup": 900,
    "codigo_barra": 52493
  },
  {
    "id_erp": 52494,
    "nome": "VOL 2/2 T. MAD. NEO 2,20",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 240,
    "setup": 900,
    "codigo_barra": 52494
  },
  {
    "id_erp": 52036,
    "nome": "VOL 2/2 T. MAD. NEO 2,40",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 240,
    "setup": 900,
    "codigo_barra": 52036
  },
  {
    "id_erp": 52040,
    "nome": "VOL 2/2 T. MAD. NEO 2,70",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 240,
    "setup": 900,
    "codigo_barra": 52040
  },
  {
    "id_erp": 55005,
    "nome": "VOL 2/2 T. MAD. NEO LX 1,80",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 133,
    "setup": 900,
    "codigo_barra": 55005
  },
  {
    "id_erp": 55006,
    "nome": "VOL 2/2 T. MAD. NEO LX 2,00",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 133,
    "setup": 900,
    "codigo_barra": 55006
  },
  {
    "id_erp": 75547,
    "nome": "VOL 2/2 T. MAD. NEO LX 2,00 X 0,90 - MEDIDA ESPECIAL",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 133,
    "setup": 900,
    "codigo_barra": 75547
  },
  {
    "id_erp": 55007,
    "nome": "VOL 2/2 T. MAD. NEO LX 2,20",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 133,
    "setup": 900,
    "codigo_barra": 55007
  },
  {
    "id_erp": 55008,
    "nome": "VOL 2/2 T. MAD. NEO LX 2,40",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 133,
    "setup": 900,
    "codigo_barra": 55008
  },
  {
    "id_erp": 55009,
    "nome": "VOL 2/2 T. MAD. NEO LX 2,70",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 133,
    "setup": 900,
    "codigo_barra": 55009
  },
  {
    "id_erp": 61470,
    "nome": "VOL 2/2 T. MAD. NEO LX 2,70",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 102,
    "setup": 900,
    "codigo_barra": 61470
  },
  {
    "id_erp": 50423,
    "nome": "VOL 2/2 T. MAD. NEO PLUS 1,40 QUAD.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 240,
    "setup": 900,
    "codigo_barra": 50423
  },
  {
    "id_erp": 50424,
    "nome": "VOL 2/2 T. MAD. NEO PLUS 1,60 QUAD.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 240,
    "setup": 900,
    "codigo_barra": 50424
  },
  {
    "id_erp": 54998,
    "nome": "VOL 2/2 T. MAD. NEO PLUS LX 1,40 QUAD.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 133,
    "setup": 900,
    "codigo_barra": 54998
  },
  {
    "id_erp": 54999,
    "nome": "VOL 2/2 T. MAD. NEO PLUS LX 1,60 QUAD.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 133,
    "setup": 900,
    "codigo_barra": 54999
  },
  {
    "id_erp": 55075,
    "nome": "VOL 2/2 T. MAD. NEPAL 1,80",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 360,
    "setup": 900,
    "codigo_barra": 55075
  },
  {
    "id_erp": 55076,
    "nome": "VOL 2/2 T. MAD. NEPAL 2,00",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 200,
    "setup": 900,
    "codigo_barra": 55076
  },
  {
    "id_erp": 55077,
    "nome": "VOL 2/2 T. MAD. NEPAL 2,20",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 200,
    "setup": 900,
    "codigo_barra": 55077
  },
  {
    "id_erp": 55078,
    "nome": "VOL 2/2 T. MAD. NEPAL 2,40",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 200,
    "setup": 900,
    "codigo_barra": 55078
  },
  {
    "id_erp": 78911,
    "nome": "VOL 2/2 T. MAD. OBLONGO LAIKA 2,20 X 1,10",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 720,
    "setup": 900,
    "codigo_barra": 78911
  },
  {
    "id_erp": 78919,
    "nome": "VOL 2/2 T. MAD. OBLONGO LAIKA 2,40 X 1,20",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 750,
    "setup": 900,
    "codigo_barra": 78919
  },
  {
    "id_erp": 78927,
    "nome": "VOL 2/2 T. MAD. OBLONGO LAIKA 2,70 X 1,20",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 780,
    "setup": 900,
    "codigo_barra": 78927
  },
  {
    "id_erp": 78939,
    "nome": "VOL 2/2 T. MAD. OBLONGO LAIKA 3,20 X 1,20",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 820,
    "setup": 900,
    "codigo_barra": 78939
  },
  {
    "id_erp": 78944,
    "nome": "VOL 2/2 T. MAD. OBLONGO LAIKA 3,40 X 1,50",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 900,
    "setup": 900,
    "codigo_barra": 78944
  },
  {
    "id_erp": 78934,
    "nome": "VOL 2/2 T. MAD. OBLONGO MESA LAIKA 3,00 X 1,20",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 800,
    "setup": 900,
    "codigo_barra": 78934
  },
  {
    "id_erp": 52496,
    "nome": "VOL 2/2 T. MAD. OMEGA 2,00",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 200,
    "setup": 900,
    "codigo_barra": 52496
  },
  {
    "id_erp": 52591,
    "nome": "VOL 2/2 T. MAD. OMEGA 2,70",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 200,
    "setup": 900,
    "codigo_barra": 52591
  },
  {
    "id_erp": 52592,
    "nome": "VOL 2/2 T. MAD. OMEGA 3,00",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 200,
    "setup": 900,
    "codigo_barra": 52592
  },
  {
    "id_erp": 52497,
    "nome": "VOL 2/2 T. MAD. OMEGA/MARIN 2,20",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 200,
    "setup": 900,
    "codigo_barra": 52497
  },
  {
    "id_erp": 52498,
    "nome": "VOL 2/2 T. MAD. OMEGA/MARIN 2,40",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 200,
    "setup": 900,
    "codigo_barra": 52498
  },
  {
    "id_erp": 68463,
    "nome": "VOL 2/2 T. MAD. ORBITA 1,60 X 1,20 S/ DETALHE  (1ª ETAPA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.2,
    "setup": 900,
    "codigo_barra": 68463
  },
  {
    "id_erp": 684639,
    "nome": "VOL 2/2 T. MAD. ORBITA 1,60 X 1,20 S/ DETALHE  (2ª ETAPA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.2,
    "setup": 900,
    "codigo_barra": 684639
  },
  {
    "id_erp": 67749,
    "nome": "VOL 2/2 T. MAD. ORBITA 2,20 X 1,20 C/ DETALHE (1ª ETAPA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 122,
    "setup": 900,
    "codigo_barra": 67749
  },
  {
    "id_erp": 677499,
    "nome": "VOL 2/2 T. MAD. ORBITA 2,20 X 1,20 C/ DETALHE (2ª ETAPA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 723,
    "setup": 900,
    "codigo_barra": 677499
  },
  {
    "id_erp": 67748,
    "nome": "VOL 2/2 T. MAD. ORBITA 2,20 X 1,20 S/ DETALHE (1ª ETAPA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 476,
    "setup": 900,
    "codigo_barra": 67748
  },
  {
    "id_erp": 677489,
    "nome": "VOL 2/2 T. MAD. ORBITA 2,20 X 1,20 S/ DETALHE (2ª ETAPA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 311,
    "setup": 900,
    "codigo_barra": 677489
  },
  {
    "id_erp": 66167,
    "nome": "VOL 2/2 T. MAD. ORBITA 2,40 X 1,30 C/ DETALHE (1ª ETAPA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 125,
    "setup": 900,
    "codigo_barra": 66167
  },
  {
    "id_erp": 661679,
    "nome": "VOL 2/2 T. MAD. ORBITA 2,40 X 1,30 C/ DETALHE (2ª ETAPA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 760,
    "setup": 900,
    "codigo_barra": 661679
  },
  {
    "id_erp": 67750,
    "nome": "VOL 2/2 T. MAD. ORBITA 2,40 X 1,30 S/ DETALHE (1ª ETAPA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 125,
    "setup": 900,
    "codigo_barra": 67750
  },
  {
    "id_erp": 677509,
    "nome": "VOL 2/2 T. MAD. ORBITA 2,40 X 1,30 S/ DETALHE (2ª ETAPA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 333,
    "setup": 900,
    "codigo_barra": 677509
  },
  {
    "id_erp": 67753,
    "nome": "VOL 2/2 T. MAD. ORBITA 2,70 X 1,45 C/ DETALHE (1ª ETAPA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 140,
    "setup": 900,
    "codigo_barra": 67753
  },
  {
    "id_erp": 677539,
    "nome": "VOL 2/2 T. MAD. ORBITA 2,70 X 1,45 C/ DETALHE (2ª ETAPA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 801,
    "setup": 900,
    "codigo_barra": 677539
  },
  {
    "id_erp": 67752,
    "nome": "VOL 2/2 T. MAD. ORBITA 2,70 X 1,45 S/ DETALHE (1ª ETAPA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 140,
    "setup": 900,
    "codigo_barra": 67752
  },
  {
    "id_erp": 677529,
    "nome": "VOL 2/2 T. MAD. ORBITA 2,70 X 1,45 S/ DETALHE (2ª ETAPA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 368,
    "setup": 900,
    "codigo_barra": 677529
  },
  {
    "id_erp": 67701,
    "nome": "VOL 2/2 T. MAD. ORBITA 3,00 X 1,60 C/ DETALHE (1ª ETAPA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.5,
    "setup": 900,
    "codigo_barra": 67701
  },
  {
    "id_erp": 677019,
    "nome": "VOL 2/2 T. MAD. ORBITA 3,00 X 1,60 C/ DETALHE (2ª ETAPA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.272,
    "setup": 900,
    "codigo_barra": 677019
  },
  {
    "id_erp": 67590,
    "nome": "VOL 2/2 T. MAD. ORBITA 3,00 X 1,60 S/ DETALHE (1ª ETAPA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 149,
    "setup": 900,
    "codigo_barra": 67590
  },
  {
    "id_erp": 675909,
    "nome": "VOL 2/2 T. MAD. ORBITA 3,00 X 1,60 S/ DETALHE (2ª ETAPA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 397,
    "setup": 900,
    "codigo_barra": 675909
  },
  {
    "id_erp": 70794,
    "nome": "VOL 2/2 T. MAD. ORBITA 3,30",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.38,
    "setup": 900,
    "codigo_barra": 70794
  },
  {
    "id_erp": 707949,
    "nome": "VOL 2/2 T. MAD. ORBITA 3,30",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.38,
    "setup": 900,
    "codigo_barra": 707949
  },
  {
    "id_erp": 77940,
    "nome": "VOL 2/2 T. MAD. ORG. MARE 1100",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 420,
    "setup": 900,
    "codigo_barra": 77940
  },
  {
    "id_erp": 78021,
    "nome": "VOL 2/2 T. MAD. ORG. MARE 1300",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 420,
    "setup": 900,
    "codigo_barra": 78021
  },
  {
    "id_erp": 73404,
    "nome": "VOL 2/2 T. MAD. ORLA 1,40 C/ GIRATORIO",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 600,
    "setup": 900,
    "codigo_barra": 73404
  },
  {
    "id_erp": 73405,
    "nome": "VOL 2/2 T. MAD. ORLA 1,40 S/ GIRATORIO",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 600,
    "setup": 900,
    "codigo_barra": 73405
  },
  {
    "id_erp": 73343,
    "nome": "VOL 2/2 T. MAD. ORLA 1,60 C/ GIRATORIO",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 600,
    "setup": 900,
    "codigo_barra": 73343
  },
  {
    "id_erp": 73344,
    "nome": "VOL 2/2 T. MAD. ORLA 1,60 S/ GIRATORIO",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 600,
    "setup": 900,
    "codigo_barra": 73344
  },
  {
    "id_erp": 83353,
    "nome": "VOL 2/2 T. MAD. ORLA 1,70 C/ GIRATORIO - MEDIDA ESPECIAL",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 600,
    "setup": 900,
    "codigo_barra": 83353
  },
  {
    "id_erp": 72798,
    "nome": "VOL 2/2 T. MAD. ORLA 1,80 C/ GIRATORIO",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 600,
    "setup": 900,
    "codigo_barra": 72798
  },
  {
    "id_erp": 72799,
    "nome": "VOL 2/2 T. MAD. ORLA 1,80 S/ GIRATORIO",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 720,
    "setup": 900,
    "codigo_barra": 72799
  },
  {
    "id_erp": 71946,
    "nome": "VOL 2/2 T. MAD. ORLA 2,00 C/ GIRATORIO",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 600,
    "setup": 900,
    "codigo_barra": 71946
  },
  {
    "id_erp": 73634,
    "nome": "VOL 2/2 T. MAD. ORLA 2,20 C/ GIRATORIO",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 600,
    "setup": 900,
    "codigo_barra": 73634
  },
  {
    "id_erp": 70249,
    "nome": "VOL 2/2 T. MAD. OVAL 1,50 X 0,90 - MEDIDA ESPECIAL",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.2,
    "setup": 900,
    "codigo_barra": 70249
  },
  {
    "id_erp": 60148,
    "nome": "VOL 2/2 T. MAD. PANAMERA 1,68 RED.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 450,
    "setup": 900,
    "codigo_barra": 60148
  },
  {
    "id_erp": 64225,
    "nome": "VOL 2/2 T. MAD. PANAMERA 1,68 RED.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 450,
    "setup": 900,
    "codigo_barra": 64225
  },
  {
    "id_erp": 601489,
    "nome": "VOL 2/2 T. MAD. PANAMERA 1,68 RED.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 650,
    "setup": 900,
    "codigo_barra": 601489
  },
  {
    "id_erp": 60146,
    "nome": "VOL 2/2 T. MAD. PANAMERA 1,88 RED.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 450,
    "setup": 900,
    "codigo_barra": 60146
  },
  {
    "id_erp": 601469,
    "nome": "VOL 2/2 T. MAD. PANAMERA 1,88 RED.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 550,
    "setup": 900,
    "codigo_barra": 601469
  },
  {
    "id_erp": 64227,
    "nome": "VOL 2/2 T. MAD. PANAMERA 1,88 RED.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 450,
    "setup": 900,
    "codigo_barra": 64227
  },
  {
    "id_erp": 64230,
    "nome": "VOL 2/2 T. MAD. PANAMERA 2,40",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 320,
    "setup": 900,
    "codigo_barra": 64230
  },
  {
    "id_erp": 642309,
    "nome": "VOL 2/2 T. MAD. PANAMERA 2,40",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 320,
    "setup": 900,
    "codigo_barra": 642309
  },
  {
    "id_erp": 60149,
    "nome": "VOL 2/2 T. MAD. PANAMERA 2,40",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 300,
    "setup": 900,
    "codigo_barra": 60149
  },
  {
    "id_erp": 601499,
    "nome": "VOL 2/2 T. MAD. PANAMERA 2,40",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 650,
    "setup": 900,
    "codigo_barra": 601499
  },
  {
    "id_erp": 60150,
    "nome": "VOL 2/2 T. MAD. PANAMERA 2,70",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 310,
    "setup": 900,
    "codigo_barra": 60150
  },
  {
    "id_erp": 601509,
    "nome": "VOL 2/2 T. MAD. PANAMERA 2,70",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 720,
    "setup": 900,
    "codigo_barra": 601509
  },
  {
    "id_erp": 60151,
    "nome": "VOL 2/2 T. MAD. PANAMERA 3,00",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 320,
    "setup": 900,
    "codigo_barra": 60151
  },
  {
    "id_erp": 601519,
    "nome": "VOL 2/2 T. MAD. PANAMERA 3,00",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 800,
    "setup": 900,
    "codigo_barra": 601519
  },
  {
    "id_erp": 64233,
    "nome": "VOL 2/2 T. MAD. PANAMERA 3,00",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 320,
    "setup": 900,
    "codigo_barra": 64233
  },
  {
    "id_erp": 642339,
    "nome": "VOL 2/2 T. MAD. PANAMERA 3,00",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 320,
    "setup": 900,
    "codigo_barra": 642339
  },
  {
    "id_erp": 68158,
    "nome": "VOL 2/2 T. MAD. PANAMERA 5,00 METAL",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 320,
    "setup": 900,
    "codigo_barra": 68158
  },
  {
    "id_erp": 52501,
    "nome": "VOL 2/2 T. MAD. PRISMA 2,00",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 200,
    "setup": 900,
    "codigo_barra": 52501
  },
  {
    "id_erp": 52502,
    "nome": "VOL 2/2 T. MAD. PRISMA 2,20",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 200,
    "setup": 900,
    "codigo_barra": 52502
  },
  {
    "id_erp": 52503,
    "nome": "VOL 2/2 T. MAD. PRISMA 2,40",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 200,
    "setup": 900,
    "codigo_barra": 52503
  },
  {
    "id_erp": 77916,
    "nome": "VOL 2/2 T. MAD. RED. MARE 1100",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 420,
    "setup": 900,
    "codigo_barra": 77916
  },
  {
    "id_erp": 77989,
    "nome": "VOL 2/2 T. MAD. RED. MARE 1200",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 420,
    "setup": 900,
    "codigo_barra": 77989
  },
  {
    "id_erp": 78017,
    "nome": "VOL 2/2 T. MAD. RED. MARE 1300",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 420,
    "setup": 900,
    "codigo_barra": 78017
  },
  {
    "id_erp": 79192,
    "nome": "VOL 2/2 T. MAD. RED. MESA TORA 1100",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 268,
    "setup": 900,
    "codigo_barra": 79192
  },
  {
    "id_erp": 78570,
    "nome": "VOL 2/2 T. MAD. RED. MESA TORA 1200",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 286,
    "setup": 900,
    "codigo_barra": 78570
  },
  {
    "id_erp": 79643,
    "nome": "VOL 2/2 T. MAD. RED. MESA TORA 1400",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 325,
    "setup": 900,
    "codigo_barra": 79643
  },
  {
    "id_erp": 79164,
    "nome": "VOL 2/2 T. MAD. RED. TORA 0,90",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 240,
    "setup": 900,
    "codigo_barra": 79164
  },
  {
    "id_erp": 79195,
    "nome": "VOL 2/2 T. MAD. RED. TORA 1400",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 325,
    "setup": 900,
    "codigo_barra": 79195
  },
  {
    "id_erp": 81203,
    "nome": "VOL 2/2 T. MAD. RET. MILA 1,20 X 0,70 - MEDIDA ESPECIAL",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 90,
    "setup": 900,
    "codigo_barra": 81203
  },
  {
    "id_erp": 52504,
    "nome": "VOL 2/2 T. MAD. RIVA 1,80",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 200,
    "setup": 900,
    "codigo_barra": 52504
  },
  {
    "id_erp": 52505,
    "nome": "VOL 2/2 T. MAD. RIVA 2,00",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 200,
    "setup": 900,
    "codigo_barra": 52505
  },
  {
    "id_erp": 52506,
    "nome": "VOL 2/2 T. MAD. RIVA 2,20",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 200,
    "setup": 900,
    "codigo_barra": 52506
  },
  {
    "id_erp": 52507,
    "nome": "VOL 2/2 T. MAD. RIVA 2,40",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 200,
    "setup": 900,
    "codigo_barra": 52507
  },
  {
    "id_erp": 56544,
    "nome": "VOL 2/2 T. MAD. RIVA 3,00",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 200,
    "setup": 900,
    "codigo_barra": 56544
  },
  {
    "id_erp": 52508,
    "nome": "VOL 2/2 T. MAD. SCALA 1,80",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 133,
    "setup": 900,
    "codigo_barra": 52508
  },
  {
    "id_erp": 52509,
    "nome": "VOL 2/2 T. MAD. SCALA 2,00",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 133,
    "setup": 900,
    "codigo_barra": 52509
  },
  {
    "id_erp": 52510,
    "nome": "VOL 2/2 T. MAD. SCALA 2,20",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 133,
    "setup": 900,
    "codigo_barra": 52510
  },
  {
    "id_erp": 52511,
    "nome": "VOL 2/2 T. MAD. SCALA 2,40",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 133,
    "setup": 900,
    "codigo_barra": 52511
  },
  {
    "id_erp": 52512,
    "nome": "VOL 2/2 T. MAD. SCALA 2,70",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 133,
    "setup": 900,
    "codigo_barra": 52512
  },
  {
    "id_erp": 52513,
    "nome": "VOL 2/2 T. MAD. SCALA 3,00",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 133,
    "setup": 900,
    "codigo_barra": 52513
  },
  {
    "id_erp": 75196,
    "nome": "VOL 2/2 T. MAD. SCALA LX 1,80 X 0,90 - MEDIDA ESPECIAL",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 133,
    "setup": 900,
    "codigo_barra": 75196
  },
  {
    "id_erp": 81690,
    "nome": "VOL 2/2 T. MAD. SIENA 0,70 RED. - MEDIDA ESPECIAL",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 75,
    "setup": 900,
    "codigo_barra": 81690
  },
  {
    "id_erp": 55107,
    "nome": "VOL 2/2 T. MAD. SIENA 0,90 RED.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 75,
    "setup": 900,
    "codigo_barra": 55107
  },
  {
    "id_erp": 51470,
    "nome": "VOL 2/2 T. MAD. SIENA 1,20 RED.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 75,
    "setup": 900,
    "codigo_barra": 51470
  },
  {
    "id_erp": 51471,
    "nome": "VOL 2/2 T. MAD. SIENA 1,40 RED.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 100,
    "setup": 900,
    "codigo_barra": 51471
  },
  {
    "id_erp": 51472,
    "nome": "VOL 2/2 T. MAD. SIENA 1,60 RED.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 100,
    "setup": 900,
    "codigo_barra": 51472
  },
  {
    "id_erp": 73557,
    "nome": "VOL 2/2 T. MAD. SIENA 1,60 RED. C/ GIRATORIO",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 600,
    "setup": 900,
    "codigo_barra": 73557
  },
  {
    "id_erp": 72942,
    "nome": "VOL 2/2 T. MAD. SIENA 1,80 C/ GIRATORIO",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 600,
    "setup": 900,
    "codigo_barra": 72942
  },
  {
    "id_erp": 51473,
    "nome": "VOL 2/2 T. MAD. SIENA 1,80 RED.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 100,
    "setup": 900,
    "codigo_barra": 51473
  },
  {
    "id_erp": 73558,
    "nome": "VOL 2/2 T. MAD. SIENA 2,00 RED. C/ GIRATORIO",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 600,
    "setup": 900,
    "codigo_barra": 73558
  },
  {
    "id_erp": 73559,
    "nome": "VOL 2/2 T. MAD. SIENA 2,00 RED. S/ GIRATORIO",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 600,
    "setup": 900,
    "codigo_barra": 73559
  },
  {
    "id_erp": 52514,
    "nome": "VOL 2/2 T. MAD. TANGO 1,80",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 240,
    "setup": 900,
    "codigo_barra": 52514
  },
  {
    "id_erp": 52515,
    "nome": "VOL 2/2 T. MAD. TANGO 2,00",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 240,
    "setup": 900,
    "codigo_barra": 52515
  },
  {
    "id_erp": 52516,
    "nome": "VOL 2/2 T. MAD. TANGO 2,20",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 240,
    "setup": 900,
    "codigo_barra": 52516
  },
  {
    "id_erp": 55169,
    "nome": "VOL 2/2 T. MAD. TANGO LX 1,80",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 133,
    "setup": 900,
    "codigo_barra": 55169
  },
  {
    "id_erp": 55170,
    "nome": "VOL 2/2 T. MAD. TANGO LX 2,00",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 133,
    "setup": 900,
    "codigo_barra": 55170
  },
  {
    "id_erp": 55171,
    "nome": "VOL 2/2 T. MAD. TANGO LX 2,20",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 133,
    "setup": 900,
    "codigo_barra": 55171
  },
  {
    "id_erp": 60167,
    "nome": "VOL 2/2 T. MAD. TARSILA 2,20 B. LACA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 102,
    "setup": 900,
    "codigo_barra": 60167
  },
  {
    "id_erp": 60158,
    "nome": "VOL 2/2 T. MAD. TARSILA 2,20 B. LAM.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 102,
    "setup": 900,
    "codigo_barra": 60158
  },
  {
    "id_erp": 60159,
    "nome": "VOL 2/2 T. MAD. TARSILA 2,40 B. LAM.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 102,
    "setup": 900,
    "codigo_barra": 60159
  },
  {
    "id_erp": 60169,
    "nome": "VOL 2/2 T. MAD. TARSILA 2,70 B. LACA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 102,
    "setup": 900,
    "codigo_barra": 60169
  },
  {
    "id_erp": 60160,
    "nome": "VOL 2/2 T. MAD. TARSILA 2,70 B. LAM.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 102,
    "setup": 900,
    "codigo_barra": 60160
  },
  {
    "id_erp": 68155,
    "nome": "VOL 2/2 T. MAD. TARSILA 2,70 X 1,00",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 102,
    "setup": 900,
    "codigo_barra": 68155
  },
  {
    "id_erp": 60170,
    "nome": "VOL 2/2 T. MAD. TARSILA 3,00 B. LACA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 102,
    "setup": 900,
    "codigo_barra": 60170
  },
  {
    "id_erp": 60161,
    "nome": "VOL 2/2 T. MAD. TARSILA 3,00 B. LAM.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 102,
    "setup": 900,
    "codigo_barra": 60161
  },
  {
    "id_erp": 70983,
    "nome": "VOL 2/2 T. MAD. TARSILA 3,20 - MEDIDA ESPECIAL",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.38,
    "setup": 900,
    "codigo_barra": 70983
  },
  {
    "id_erp": 81359,
    "nome": "VOL 2/2 T. MAD. TORA 2,20 X 1,08 - MEDIDA ESPECIAL",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 522,
    "setup": 900,
    "codigo_barra": 81359
  },
  {
    "id_erp": 77197,
    "nome": "VOL 2/2 T. MAD. TORA 2,20 X 1,28",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 522,
    "setup": 900,
    "codigo_barra": 77197
  },
  {
    "id_erp": 77199,
    "nome": "VOL 2/2 T. MAD. TORA 2,40 X 1,28",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 534,
    "setup": 900,
    "codigo_barra": 77199
  },
  {
    "id_erp": 77200,
    "nome": "VOL 2/2 T. MAD. TORA 2,70 X 1,28",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 619,
    "setup": 900,
    "codigo_barra": 77200
  },
  {
    "id_erp": 76401,
    "nome": "VOL 2/2 T. MAD. TORA 3,00 X 1,28",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 625,
    "setup": 900,
    "codigo_barra": 76401
  },
  {
    "id_erp": 77204,
    "nome": "VOL 2/2 T. MAD. TORA 3,00 X 1,48",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 656,
    "setup": 900,
    "codigo_barra": 77204
  },
  {
    "id_erp": 77201,
    "nome": "VOL 2/2 T. MAD. TORA 3,20 X 1,28",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 663,
    "setup": 900,
    "codigo_barra": 77201
  },
  {
    "id_erp": 77269,
    "nome": "VOL 2/2 T. MAD. TORA 3,50 X 1,28",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 781,
    "setup": 900,
    "codigo_barra": 77269
  },
  {
    "id_erp": 76544,
    "nome": "VOL 2/2 T. MAD. TORA 3,50 X 1,48",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 806,
    "setup": 900,
    "codigo_barra": 76544
  },
  {
    "id_erp": 53795,
    "nome": "VOL 2/2 T. MAD. TRIADE 1,60 - MEDIDA ESPECIAL",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 102,
    "setup": 900,
    "codigo_barra": 53795
  },
  {
    "id_erp": 60750,
    "nome": "VOL 2/2 T. MAD. TRIADE 1,80 B. LAM.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 102,
    "setup": 900,
    "codigo_barra": 60750
  },
  {
    "id_erp": 75820,
    "nome": "VOL 2/2 T. MAD. TRIADE 1,80 X 0,90 - MEDIDA ESPECIAL",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 102,
    "setup": 900,
    "codigo_barra": 75820
  },
  {
    "id_erp": 75284,
    "nome": "VOL 2/2 T. MAD. TRIADE 1,90 X 0,90 -  MEDIDA ESPECIAL",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 102,
    "setup": 900,
    "codigo_barra": 75284
  },
  {
    "id_erp": 60751,
    "nome": "VOL 2/2 T. MAD. TRIADE 2,00 B. LAM.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 102,
    "setup": 900,
    "codigo_barra": 60751
  },
  {
    "id_erp": 60752,
    "nome": "VOL 2/2 T. MAD. TRIADE 2,20 B. LAM.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 102,
    "setup": 900,
    "codigo_barra": 60752
  },
  {
    "id_erp": 60753,
    "nome": "VOL 2/2 T. MAD. TRIADE 2,40 B. LAM.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 102,
    "setup": 900,
    "codigo_barra": 60753
  },
  {
    "id_erp": 71307,
    "nome": "VOL 2/2 T. MAD. TRIADE 2,40 X 1,00 B. LAM. - MEDIDA ESPECIAL",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 102,
    "setup": 900,
    "codigo_barra": 71307
  },
  {
    "id_erp": 60754,
    "nome": "VOL 2/2 T. MAD. TRIADE 2,70",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 102,
    "setup": 900,
    "codigo_barra": 60754
  },
  {
    "id_erp": 74186,
    "nome": "VOL 2/2 T. MAD. TRIADE 2,70 X 1,10 - MEDIDA ESPERCIAL",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 102,
    "setup": 900,
    "codigo_barra": 74186
  },
  {
    "id_erp": 60755,
    "nome": "VOL 2/2 T. MAD. TRIADE 3,00",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 102,
    "setup": 900,
    "codigo_barra": 60755
  },
  {
    "id_erp": 73464,
    "nome": "VOL 2/2 T. MAD. TRIADE 3,00 X 1,00",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 102,
    "setup": 900,
    "codigo_barra": 73464
  },
  {
    "id_erp": 57667,
    "nome": "VOL 2/2 T. MAD. UOMINI LX 2,20",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 900,
    "setup": 900,
    "codigo_barra": 57667
  },
  {
    "id_erp": 57668,
    "nome": "VOL 2/2 T. MAD. UOMINI LX 2,40",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 133,
    "setup": 900,
    "codigo_barra": 57668
  },
  {
    "id_erp": 57669,
    "nome": "VOL 2/2 T. MAD. UOMINI LX 2,70",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 200,
    "setup": 900,
    "codigo_barra": 57669
  },
  {
    "id_erp": 57670,
    "nome": "VOL 2/2 T. MAD. UOMINI LX 3,00",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 133,
    "setup": 900,
    "codigo_barra": 57670
  },
  {
    "id_erp": 68148,
    "nome": "VOL 2/2 T. MAD. UOMINI LX 3,20 X 1,20",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 133,
    "setup": 900,
    "codigo_barra": 68148
  },
  {
    "id_erp": 57679,
    "nome": "VOL 2/2 T. MAD. UOMINI PLUS LX 1,40 QUAD.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 102,
    "setup": 900,
    "codigo_barra": 57679
  },
  {
    "id_erp": 65674,
    "nome": "VOL 2/2 T. MAD. UOMINI PLUS LX 1,40 RED.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 200,
    "setup": 900,
    "codigo_barra": 65674
  },
  {
    "id_erp": 57974,
    "nome": "VOL 2/2 T. MAD. UOMINI PLUS LX 1,60 RED.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 904,
    "setup": 900,
    "codigo_barra": 57974
  },
  {
    "id_erp": 57975,
    "nome": "VOL 2/2 T. MAD. UOMINI PLUS LX 1,80 RED.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 100,
    "setup": 900,
    "codigo_barra": 57975
  },
  {
    "id_erp": 57977,
    "nome": "VOL 2/2 T. MAD. UOMINI PLUS LX 2,19 RED.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 200,
    "setup": 900,
    "codigo_barra": 57977
  },
  {
    "id_erp": 52586,
    "nome": "VOL 2/2 T. MAD. VERMONT 1,80",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 50,
    "setup": 900,
    "codigo_barra": 52586
  },
  {
    "id_erp": 52595,
    "nome": "VOL 2/2 T. MAD. VERMONT 2,00",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 50,
    "setup": 900,
    "codigo_barra": 52595
  },
  {
    "id_erp": 52596,
    "nome": "VOL 2/2 T. MAD. VERMONT 2,20",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 50,
    "setup": 900,
    "codigo_barra": 52596
  },
  {
    "id_erp": 52597,
    "nome": "VOL 2/2 T. MAD. VERMONT 2,40",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 50,
    "setup": 900,
    "codigo_barra": 52597
  },
  {
    "id_erp": 52704,
    "nome": "VOL 2/2 T. MAD. VERMONT 2,70",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 50,
    "setup": 900,
    "codigo_barra": 52704
  },
  {
    "id_erp": 52706,
    "nome": "VOL 2/2 T. MAD. VERMONT 3,00",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 50,
    "setup": 900,
    "codigo_barra": 52706
  },
  {
    "id_erp": 33774,
    "nome": "VOL 2/2 T. MAD. VICENZA 1,60",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 133,
    "setup": 900,
    "codigo_barra": 33774
  },
  {
    "id_erp": 33172,
    "nome": "VOL 2/2 T. MAD. VICENZA 1,80",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 133,
    "setup": 900,
    "codigo_barra": 33172
  },
  {
    "id_erp": 33765,
    "nome": "VOL 2/2 T. MAD. VICENZA 2,00",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 133,
    "setup": 900,
    "codigo_barra": 33765
  },
  {
    "id_erp": 33179,
    "nome": "VOL 2/2 T. MAD. VICENZA 2,20",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 133,
    "setup": 900,
    "codigo_barra": 33179
  },
  {
    "id_erp": 81155,
    "nome": "VOL 2/2 T. PEDRA FUNGI",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.71,
    "setup": 900,
    "codigo_barra": 81155
  },
  {
    "id_erp": 73219,
    "nome": "VOL 2/2 T. PEDRA FUNGI 2,00 B. LACA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 600,
    "setup": 900,
    "codigo_barra": 73219
  },
  {
    "id_erp": 73216,
    "nome": "VOL 2/2 T. PEDRA FUNGI 2,00 B. LAM",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 600,
    "setup": 900,
    "codigo_barra": 73216
  },
  {
    "id_erp": 73223,
    "nome": "VOL 2/2 T. PEDRA FUNGI 2,20 B.LAM",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.2,
    "setup": 900,
    "codigo_barra": 73223
  },
  {
    "id_erp": 73227,
    "nome": "VOL 2/2 T. PEDRA FUNGI 2,40 B. LAM",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 600,
    "setup": 900,
    "codigo_barra": 73227
  },
  {
    "id_erp": 70729,
    "nome": "VOL 2/2 T. PEDRA FUNGI 2,70",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.32,
    "setup": 900,
    "codigo_barra": 70729
  },
  {
    "id_erp": 73267,
    "nome": "VOL 2/2 T. PEDRA FUNGI 2,70 B. LACA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.2,
    "setup": 900,
    "codigo_barra": 73267
  },
  {
    "id_erp": 73260,
    "nome": "VOL 2/2 T. PEDRA FUNGI 2,70 B. LACA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 600,
    "setup": 900,
    "codigo_barra": 73260
  },
  {
    "id_erp": 73266,
    "nome": "VOL 2/2 T. PEDRA FUNGI 3,00 B. LAM",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 600,
    "setup": 900,
    "codigo_barra": 73266
  },
  {
    "id_erp": 75286,
    "nome": "VOL 2/2 T. PEDRA FUNGI 3,20 X 1,50 B. LAM - MEDIDA ESPECIAL (1ª ETAPA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.8,
    "setup": 900,
    "codigo_barra": 75286
  },
  {
    "id_erp": 75286,
    "nome": "VOL 2/2 T. PEDRA FUNGI 3,20 X 1,50 B. LAM - MEDIDA ESPECIAL (2ª ETAPA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.8,
    "setup": 900,
    "codigo_barra": 75286
  },
  {
    "id_erp": 79727,
    "nome": "VOL 2/2 T. PEDRA FUNGI B. LAM.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.71,
    "setup": 900,
    "codigo_barra": 79727
  },
  {
    "id_erp": 81154,
    "nome": "VOL 2/2 T. PEDRA FUNGI B. LAM.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.71,
    "setup": 900,
    "codigo_barra": 81154
  },
  {
    "id_erp": 76377,
    "nome": "VOL 2/2 T. PEDRA GUANABARA 1,80 B. LACA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.2,
    "setup": 900,
    "codigo_barra": 76377
  },
  {
    "id_erp": 76378,
    "nome": "VOL 2/2 T. PEDRA GUANABARA 1,80 B. LAM (1ª ETAPA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.2,
    "setup": 900,
    "codigo_barra": 76378
  },
  {
    "id_erp": 763789,
    "nome": "VOL 2/2 T. PEDRA GUANABARA 1,80 B. LAM (2ª ETAPA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.2,
    "setup": 900,
    "codigo_barra": 763789
  },
  {
    "id_erp": 76844,
    "nome": "VOL 2/2 T. PEDRA GUANABARA 2,00 X 1,10 B. LACA. (1ª ETAPA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.8,
    "setup": 900,
    "codigo_barra": 76844
  },
  {
    "id_erp": 768449,
    "nome": "VOL 2/2 T. PEDRA GUANABARA 2,00 X 1,10 B. LACA. (2ª ETAPA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.8,
    "setup": 900,
    "codigo_barra": 768449
  },
  {
    "id_erp": 69033,
    "nome": "VOL 2/2 T. PEDRA GUANABARA 2,20 B. LACA (1ª ETAPA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.2,
    "setup": 900,
    "codigo_barra": 69033
  },
  {
    "id_erp": 690339,
    "nome": "VOL 2/2 T. PEDRA GUANABARA 2,20 B. LACA (2ª ETAPA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.2,
    "setup": 900,
    "codigo_barra": 690339
  },
  {
    "id_erp": 69116,
    "nome": "VOL 2/2 T. PEDRA GUANABARA 2,20 B. LAM (1ª ETAPA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.8,
    "setup": 900,
    "codigo_barra": 69116
  },
  {
    "id_erp": 69116,
    "nome": "VOL 2/2 T. PEDRA GUANABARA 2,20 B. LAM (2ª ETAPA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.8,
    "setup": 900,
    "codigo_barra": 69116
  },
  {
    "id_erp": 69034,
    "nome": "VOL 2/2 T. PEDRA GUANABARA 2,40 B. LACA (1ª ETAPA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.8,
    "setup": 900,
    "codigo_barra": 69034
  },
  {
    "id_erp": 690349,
    "nome": "VOL 2/2 T. PEDRA GUANABARA 2,40 B. LACA (2ª ETAPA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.8,
    "setup": 900,
    "codigo_barra": 690349
  },
  {
    "id_erp": 69119,
    "nome": "VOL 2/2 T. PEDRA GUANABARA 2,40 B. LAM (1ª ETAPA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.02,
    "setup": 900,
    "codigo_barra": 69119
  },
  {
    "id_erp": 691199,
    "nome": "VOL 2/2 T. PEDRA GUANABARA 2,40 B. LAM (2ª ETAPA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.02,
    "setup": 900,
    "codigo_barra": 691199
  },
  {
    "id_erp": 84421,
    "nome": "VOL 2/2 T. PEDRA GUANABARA 2,40 X 0,90 B. LAM  (1ª ETAPA) - MEDIDA ESPECIAL",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.32,
    "setup": 900,
    "codigo_barra": 84421
  },
  {
    "id_erp": 84421,
    "nome": "VOL 2/2 T. PEDRA GUANABARA 2,40 X 0,90 B. LAM  (2ª ETAPA) - MEDIDA ESPECIAL",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.32,
    "setup": 900,
    "codigo_barra": 84421
  },
  {
    "id_erp": 69035,
    "nome": "VOL 2/2 T. PEDRA GUANABARA 2,70 B. LACA (1ª ETAPA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.8,
    "setup": 900,
    "codigo_barra": 69035
  },
  {
    "id_erp": 690359,
    "nome": "VOL 2/2 T. PEDRA GUANABARA 2,70 B. LACA (2ª ETAPA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.8,
    "setup": 900,
    "codigo_barra": 690359
  },
  {
    "id_erp": 69121,
    "nome": "VOL 2/2 T. PEDRA GUANABARA 2,70 B. LAM (1ª ETAPA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.32,
    "setup": 900,
    "codigo_barra": 69121
  },
  {
    "id_erp": 691219,
    "nome": "VOL 2/2 T. PEDRA GUANABARA 2,70 B. LAM (2ª ETAPA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.32,
    "setup": 900,
    "codigo_barra": 691219
  },
  {
    "id_erp": 69036,
    "nome": "VOL 2/2 T. PEDRA GUANABARA 3,00 B. LACA (1ª ETAPA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.8,
    "setup": 900,
    "codigo_barra": 69036
  },
  {
    "id_erp": 690369,
    "nome": "VOL 2/2 T. PEDRA GUANABARA 3,00 B. LACA (2ª ETAPA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.8,
    "setup": 900,
    "codigo_barra": 690369
  },
  {
    "id_erp": 69123,
    "nome": "VOL 2/2 T. PEDRA GUANABARA 3,00 B.LAM (1ª ETAPA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.38,
    "setup": 900,
    "codigo_barra": 69123
  },
  {
    "id_erp": 691239,
    "nome": "VOL 2/2 T. PEDRA GUANABARA 3,00 B.LAM (2ª ETAPA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.38,
    "setup": 900,
    "codigo_barra": 691239
  },
  {
    "id_erp": 81055,
    "nome": "VOL 2/2 T. PEDRA HELIX 2,00 B. LACA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.02,
    "setup": 900,
    "codigo_barra": 81055
  },
  {
    "id_erp": 69659,
    "nome": "VOL 2/2 T. PEDRA HELIX 2,20 B. LACA (1ª ETAPA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.02,
    "setup": 900,
    "codigo_barra": 69659
  },
  {
    "id_erp": 696599,
    "nome": "VOL 2/2 T. PEDRA HELIX 2,20 B. LACA (2ª ETAPA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.02,
    "setup": 900,
    "codigo_barra": 696599
  },
  {
    "id_erp": 69660,
    "nome": "VOL 2/2 T. PEDRA HELIX 2,20 B. LAM (1ª ETAPA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.02,
    "setup": 900,
    "codigo_barra": 69660
  },
  {
    "id_erp": 696609,
    "nome": "VOL 2/2 T. PEDRA HELIX 2,20 B. LAM (2ª ETAPA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.02,
    "setup": 900,
    "codigo_barra": 696609
  },
  {
    "id_erp": 69663,
    "nome": "VOL 2/2 T. PEDRA HELIX 2,40 B. LACA (1ª ETAPA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.02,
    "setup": 900,
    "codigo_barra": 69663
  },
  {
    "id_erp": 696639,
    "nome": "VOL 2/2 T. PEDRA HELIX 2,40 B. LACA (2ª ETAPA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.02,
    "setup": 900,
    "codigo_barra": 696639
  },
  {
    "id_erp": 69664,
    "nome": "VOL 2/2 T. PEDRA HELIX 2,40 B. LAM (1ª ETAPA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.02,
    "setup": 900,
    "codigo_barra": 69664
  },
  {
    "id_erp": 696649,
    "nome": "VOL 2/2 T. PEDRA HELIX 2,40 B. LAM (2ª ETAPA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.02,
    "setup": 900,
    "codigo_barra": 696649
  },
  {
    "id_erp": 69670,
    "nome": "VOL 2/2 T. PEDRA HELIX 2,70 B. LACA (1ª ETAPA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.02,
    "setup": 900,
    "codigo_barra": 69670
  },
  {
    "id_erp": 696709,
    "nome": "VOL 2/2 T. PEDRA HELIX 2,70 B. LACA (2ª ETAPA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.02,
    "setup": 900,
    "codigo_barra": 696709
  },
  {
    "id_erp": 69671,
    "nome": "VOL 2/2 T. PEDRA HELIX 2,70 B. LAM (1ª ETAPA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.02,
    "setup": 900,
    "codigo_barra": 69671
  },
  {
    "id_erp": 696719,
    "nome": "VOL 2/2 T. PEDRA HELIX 2,70 B. LAM (2ª ETAPA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.02,
    "setup": 900,
    "codigo_barra": 696719
  },
  {
    "id_erp": 69688,
    "nome": "VOL 2/2 T. PEDRA HELIX 3,00 B. LAM (1ª ETAPA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.02,
    "setup": 900,
    "codigo_barra": 69688
  },
  {
    "id_erp": 696889,
    "nome": "VOL 2/2 T. PEDRA HELIX 3,00 B. LAM (2ª ETAPA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.02,
    "setup": 900,
    "codigo_barra": 696889
  },
  {
    "id_erp": 85518,
    "nome": "VOL 2/2 T. PEDRA LEME 2,10 X 1,10 B. LAM - MEDIDA ESPECIAL",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.02,
    "setup": 900,
    "codigo_barra": 85518
  },
  {
    "id_erp": 69691,
    "nome": "VOL 2/2 T. PEDRA LEME 2,20 B. LAM",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.02,
    "setup": 900,
    "codigo_barra": 69691
  },
  {
    "id_erp": 69690,
    "nome": "VOL 2/2 T. PEDRA LEME 2,20 B.LACA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.02,
    "setup": 900,
    "codigo_barra": 69690
  },
  {
    "id_erp": 69693,
    "nome": "VOL 2/2 T. PEDRA LEME 2,40 B. LACA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.02,
    "setup": 900,
    "codigo_barra": 69693
  },
  {
    "id_erp": 69694,
    "nome": "VOL 2/2 T. PEDRA LEME 2,40 B. LAM",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.02,
    "setup": 900,
    "codigo_barra": 69694
  },
  {
    "id_erp": 69697,
    "nome": "VOL 2/2 T. PEDRA LEME 2,70 B. LACA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.02,
    "setup": 900,
    "codigo_barra": 69697
  },
  {
    "id_erp": 69698,
    "nome": "VOL 2/2 T. PEDRA LEME 2,70 B. LAM",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.02,
    "setup": 900,
    "codigo_barra": 69698
  },
  {
    "id_erp": 69702,
    "nome": "VOL 2/2 T. PEDRA LEME 3,00 B. LACA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.02,
    "setup": 900,
    "codigo_barra": 69702
  },
  {
    "id_erp": 69703,
    "nome": "VOL 2/2 T. PEDRA LEME 3,00 B. LAM",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.02,
    "setup": 900,
    "codigo_barra": 69703
  },
  {
    "id_erp": 78959,
    "nome": "VOL 2/2 T. PEDRA. OBLONGO LAIKA 2,00 B. LACA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 680,
    "setup": 900,
    "codigo_barra": 78959
  },
  {
    "id_erp": 78975,
    "nome": "VOL 2/2 T. PEDRA. OBLONGO LAIKA 2,70 X 1,20 B. LAM",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 780,
    "setup": 900,
    "codigo_barra": 78975
  },
  {
    "id_erp": 68144,
    "nome": "VOL 2/2 T. RECOURO INDIGO 1,44 B. MAD. S/ GIRATORIO (1ª PARTE)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 350,
    "setup": 900,
    "codigo_barra": 68144
  },
  {
    "id_erp": 681449,
    "nome": "VOL 2/2 T. RECOURO INDIGO 1,44 B. MAD. S/ GIRATORIO (2ª PARTE)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 350,
    "setup": 900,
    "codigo_barra": 681449
  },
  {
    "id_erp": 70115,
    "nome": "VOL 2/2 T. RECOURO INDIGO 1,64 B. MAD. C/ GIRATORIO",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.38,
    "setup": 900,
    "codigo_barra": 70115
  },
  {
    "id_erp": 68763,
    "nome": "VOL 2/2 T. RECOURO INDIGO 1,64 B. MAD. S/ GIRATORIO (1ª PARTE)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 350,
    "setup": 900,
    "codigo_barra": 68763
  },
  {
    "id_erp": 687639,
    "nome": "VOL 2/2 T. RECOURO INDIGO 1,64 B. MAD. S/ GIRATORIO (2ª PARTE)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 350,
    "setup": 900,
    "codigo_barra": 687639
  },
  {
    "id_erp": 68764,
    "nome": "VOL 2/2 T. RECOURO INDIGO 1,84 B. MAD. S/ GIRATORIO (1ª PARTE)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.38,
    "setup": 900,
    "codigo_barra": 68764
  },
  {
    "id_erp": 687649,
    "nome": "VOL 2/2 T. RECOURO INDIGO 1,84 B. MAD. S/ GIRATORIO (2ª PARTE)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.38,
    "setup": 900,
    "codigo_barra": 687649
  },
  {
    "id_erp": 70110,
    "nome": "VOL 2/2 T. RECOURO INDIGO 1,84  B. MAD. C/ GIRATORIO - (1ª PARTE)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.38,
    "setup": 900,
    "codigo_barra": 70110
  },
  {
    "id_erp": 701109,
    "nome": "VOL 2/2 T. RECOURO INDIGO 1,84  B. MAD. C/ GIRATORIO - (2ª PARTE)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.38,
    "setup": 900,
    "codigo_barra": 701109
  },
  {
    "id_erp": 72720,
    "nome": "VOL 2/2 T. RECOURO SIENA 0,90 RED.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 75,
    "setup": 900,
    "codigo_barra": 72720
  },
  {
    "id_erp": 71846,
    "nome": "VOL 2/2 T. RECOURO SIENA 1,20 RED.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.2,
    "setup": 900,
    "codigo_barra": 71846
  },
  {
    "id_erp": 71846,
    "nome": "VOL 2/2 T. RECOURO SIENA 1,20 RED.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 600,
    "setup": 900,
    "codigo_barra": 71846
  },
  {
    "id_erp": 72723,
    "nome": "VOL 2/2 T. RECOURO SIENA 1,40 RED.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.2,
    "setup": 900,
    "codigo_barra": 72723
  },
  {
    "id_erp": 36454,
    "nome": "VOL 2/2 T. V. APARADOR ASTI 1,60",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 100,
    "setup": 900,
    "codigo_barra": 36454
  },
  {
    "id_erp": 44806,
    "nome": "VOL 2/2 T. V. APARADOR CARDEAL",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 85,
    "setup": 900,
    "codigo_barra": 44806
  },
  {
    "id_erp": 44808,
    "nome": "VOL 2/2 T. V. APARADOR CARDEAL B. LAM.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 85,
    "setup": 900,
    "codigo_barra": 44808
  },
  {
    "id_erp": 42795,
    "nome": "VOL 2/2 T. V. ASTI 1,20 X 0,90 RET.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 133,
    "setup": 900,
    "codigo_barra": 42795
  },
  {
    "id_erp": 35200,
    "nome": "VOL 2/2 T. V. ASTI 1,40 QUAD.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 133,
    "setup": 900,
    "codigo_barra": 35200
  },
  {
    "id_erp": 35202,
    "nome": "VOL 2/2 T. V. ASTI 1,40 RET.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 133,
    "setup": 900,
    "codigo_barra": 35202
  },
  {
    "id_erp": 35201,
    "nome": "VOL 2/2 T. V. ASTI 1,50 QUAD.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 133,
    "setup": 900,
    "codigo_barra": 35201
  },
  {
    "id_erp": 35203,
    "nome": "VOL 2/2 T. V. ASTI 1,60 RET.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 133,
    "setup": 900,
    "codigo_barra": 35203
  },
  {
    "id_erp": 35204,
    "nome": "VOL 2/2 T. V. ASTI 1,80 RET.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 133,
    "setup": 900,
    "codigo_barra": 35204
  },
  {
    "id_erp": 35205,
    "nome": "VOL 2/2 T. V. ASTI 2,00 RET.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 133,
    "setup": 900,
    "codigo_barra": 35205
  },
  {
    "id_erp": 35206,
    "nome": "VOL 2/2 T. V. ASTI 2,20 RET.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 133,
    "setup": 900,
    "codigo_barra": 35206
  },
  {
    "id_erp": 44051,
    "nome": "VOL 2/2 T. V. BISTRO CALIANDRA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 180,
    "setup": 900,
    "codigo_barra": 44051
  },
  {
    "id_erp": 44111,
    "nome": "VOL 2/2 T. V. CARDEAL 1,80",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 100,
    "setup": 900,
    "codigo_barra": 44111
  },
  {
    "id_erp": 44113,
    "nome": "VOL 2/2 T. V. CARDEAL 2,00",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 100,
    "setup": 900,
    "codigo_barra": 44113
  },
  {
    "id_erp": 44061,
    "nome": "VOL 2/2 T. V. CARDEAL 2,20",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 200,
    "setup": 900,
    "codigo_barra": 44061
  },
  {
    "id_erp": 44114,
    "nome": "VOL 2/2 T. V. CARDEAL 2,40",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 200,
    "setup": 900,
    "codigo_barra": 44114
  },
  {
    "id_erp": 53076,
    "nome": "VOL 2/2 T. V. CARTAGO 1,80 CB",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 102,
    "setup": 900,
    "codigo_barra": 53076
  },
  {
    "id_erp": 50354,
    "nome": "VOL 2/2 T. V. CARTAGO 1,84",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 102,
    "setup": 900,
    "codigo_barra": 50354
  },
  {
    "id_erp": 50358,
    "nome": "VOL 2/2 T. V. CARTAGO 1,84 B. LAM.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 102,
    "setup": 900,
    "codigo_barra": 50358
  },
  {
    "id_erp": 53078,
    "nome": "VOL 2/2 T. V. CARTAGO 2,00 CB",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 102,
    "setup": 900,
    "codigo_barra": 53078
  },
  {
    "id_erp": 50355,
    "nome": "VOL 2/2 T. V. CARTAGO 2,04",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 102,
    "setup": 900,
    "codigo_barra": 50355
  },
  {
    "id_erp": 50359,
    "nome": "VOL 2/2 T. V. CARTAGO 2,04 B. LAM.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 102,
    "setup": 900,
    "codigo_barra": 50359
  },
  {
    "id_erp": 53708,
    "nome": "VOL 2/2 T. V. CARTAGO 2,20 CB",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 102,
    "setup": 900,
    "codigo_barra": 53708
  },
  {
    "id_erp": 50356,
    "nome": "VOL 2/2 T. V. CARTAGO 2,24",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 102,
    "setup": 900,
    "codigo_barra": 50356
  },
  {
    "id_erp": 50360,
    "nome": "VOL 2/2 T. V. CARTAGO 2,24 B. LAM.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 102,
    "setup": 900,
    "codigo_barra": 50360
  },
  {
    "id_erp": 50357,
    "nome": "VOL 2/2 T. V. CARTAGO 2,44",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 133,
    "setup": 900,
    "codigo_barra": 50357
  },
  {
    "id_erp": 50361,
    "nome": "VOL 2/2 T. V. CARTAGO 2,44 B. LAM.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 133,
    "setup": 900,
    "codigo_barra": 50361
  },
  {
    "id_erp": 40020,
    "nome": "VOL 2/2 T. V. DUNA 1,20 B. MAD. QUAD.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.08,
    "setup": 900,
    "codigo_barra": 40020
  },
  {
    "id_erp": 38641,
    "nome": "VOL 2/2 T. V. DUNA 1,20 QUAD.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.08,
    "setup": 900,
    "codigo_barra": 38641
  },
  {
    "id_erp": 40021,
    "nome": "VOL 2/2 T. V. DUNA 1,30 B. MAD. QUAD.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.08,
    "setup": 900,
    "codigo_barra": 40021
  },
  {
    "id_erp": 38642,
    "nome": "VOL 2/2 T. V. DUNA 1,30 QUAD.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.08,
    "setup": 900,
    "codigo_barra": 38642
  },
  {
    "id_erp": 50151,
    "nome": "VOL 2/2 T. V. DUNA 1,30 T. DUPLO",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.08,
    "setup": 900,
    "codigo_barra": 50151
  },
  {
    "id_erp": 56546,
    "nome": "VOL 2/2 T. V. DUNA 2,40",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 200,
    "setup": 900,
    "codigo_barra": 56546
  },
  {
    "id_erp": 55122,
    "nome": "VOL 2/2 T. V. DUNA PLUS 1,20 RED.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.08,
    "setup": 900,
    "codigo_barra": 55122
  },
  {
    "id_erp": 56012,
    "nome": "VOL 2/2 T. V. DUNA PLUS 1,20 RED. B. MAD.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.08,
    "setup": 900,
    "codigo_barra": 56012
  },
  {
    "id_erp": 40018,
    "nome": "VOL 2/2 T. V. DUNA PLUS 1,40 B. MAD. QUAD.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.08,
    "setup": 900,
    "codigo_barra": 40018
  },
  {
    "id_erp": 38703,
    "nome": "VOL 2/2 T. V. DUNA PLUS 1,40 QUAD.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.08,
    "setup": 900,
    "codigo_barra": 38703
  },
  {
    "id_erp": 55123,
    "nome": "VOL 2/2 T. V. DUNA PLUS 1,40 RED.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.08,
    "setup": 900,
    "codigo_barra": 55123
  },
  {
    "id_erp": 56013,
    "nome": "VOL 2/2 T. V. DUNA PLUS 1,40 RED. B. MAD.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.08,
    "setup": 900,
    "codigo_barra": 56013
  },
  {
    "id_erp": 56406,
    "nome": "VOL 2/2 T. V. DUNA PLUS 1,40 T. DUPLO",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.08,
    "setup": 900,
    "codigo_barra": 56406
  },
  {
    "id_erp": 40019,
    "nome": "VOL 2/2 T. V. DUNA PLUS 1,50 B. MAD. QUAD.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.08,
    "setup": 900,
    "codigo_barra": 40019
  },
  {
    "id_erp": 43948,
    "nome": "VOL 2/2 T. V. DUNA PLUS 1,50 B. MAD. RED.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.08,
    "setup": 900,
    "codigo_barra": 43948
  },
  {
    "id_erp": 38705,
    "nome": "VOL 2/2 T. V. DUNA PLUS 1,50 QUAD.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.08,
    "setup": 900,
    "codigo_barra": 38705
  },
  {
    "id_erp": 43947,
    "nome": "VOL 2/2 T. V. DUNA PLUS 1,50 RED.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.08,
    "setup": 900,
    "codigo_barra": 43947
  },
  {
    "id_erp": 51070,
    "nome": "VOL 2/2 T. V. DUNA PLUS 1,60 QUAD.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.08,
    "setup": 900,
    "codigo_barra": 51070
  },
  {
    "id_erp": 50877,
    "nome": "VOL 2/2 T. V. DUNA PLUS 1,60 RED.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.08,
    "setup": 900,
    "codigo_barra": 50877
  },
  {
    "id_erp": 56014,
    "nome": "VOL 2/2 T. V. DUNA PLUS 1,60 RED. B. MAD.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.08,
    "setup": 900,
    "codigo_barra": 56014
  },
  {
    "id_erp": 56223,
    "nome": "VOL 2/2 T. V. DUNA PLUS LX 1,40 B. LAM. QUAD",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.08,
    "setup": 900,
    "codigo_barra": 56223
  },
  {
    "id_erp": 55067,
    "nome": "VOL 2/2 T. V. DUNA PLUS LX 1,40 QUAD.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.08,
    "setup": 900,
    "codigo_barra": 55067
  },
  {
    "id_erp": 56225,
    "nome": "VOL 2/2 T. V. DUNA PLUS LX 1,50 B. LAM. QUAD.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.08,
    "setup": 900,
    "codigo_barra": 56225
  },
  {
    "id_erp": 55068,
    "nome": "VOL 2/2 T. V. DUNA PLUS LX 1,50 QUAD.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.08,
    "setup": 900,
    "codigo_barra": 55068
  },
  {
    "id_erp": 56228,
    "nome": "VOL 2/2 T. V. DUNA PLUS LX 1,60 B. LAM. QUAD.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.08,
    "setup": 900,
    "codigo_barra": 56228
  },
  {
    "id_erp": 55069,
    "nome": "VOL 2/2 T. V. DUNA PLUS LX 1,60 QUAD.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.08,
    "setup": 900,
    "codigo_barra": 55069
  },
  {
    "id_erp": 58134,
    "nome": "VOL 2/2 T. V. DUNA PLUS LX 1,60 RED.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 75,
    "setup": 900,
    "codigo_barra": 58134
  },
  {
    "id_erp": 42469,
    "nome": "VOL 2/2 T. V. DUNA RET. 1,60",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.08,
    "setup": 900,
    "codigo_barra": 42469
  },
  {
    "id_erp": 42470,
    "nome": "VOL 2/2 T. V. DUNA RET. 1,60 B. MAD.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.08,
    "setup": 900,
    "codigo_barra": 42470
  },
  {
    "id_erp": 46733,
    "nome": "VOL 2/2 T. V. DUNA/MARIN 1,60 B. MAD. QUAD.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 904,
    "setup": 900,
    "codigo_barra": 46733
  },
  {
    "id_erp": 36610,
    "nome": "VOL 2/2 T. V. ELIS 1,30 QUAD.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.08,
    "setup": 900,
    "codigo_barra": 36610
  },
  {
    "id_erp": 56332,
    "nome": "VOL 2/2 T. V. ELOA 1,80 B. LAM.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 102,
    "setup": 900,
    "codigo_barra": 56332
  },
  {
    "id_erp": 56334,
    "nome": "VOL 2/2 T. V. ELOA 2,00 B. LAM.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 102,
    "setup": 900,
    "codigo_barra": 56334
  },
  {
    "id_erp": 64366,
    "nome": "VOL 2/2 T. V. FUNGI 2,00",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.38,
    "setup": 900,
    "codigo_barra": 64366
  },
  {
    "id_erp": 64367,
    "nome": "VOL 2/2 T. V. FUNGI 2,20",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.38,
    "setup": 900,
    "codigo_barra": 64367
  },
  {
    "id_erp": 75822,
    "nome": "VOL 2/2 T. V. FUNGI 2,20 B. LAM.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.38,
    "setup": 900,
    "codigo_barra": 75822
  },
  {
    "id_erp": 67396,
    "nome": "VOL 2/2 T. V. FUNGI 2,20 B. LAM.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.38,
    "setup": 900,
    "codigo_barra": 67396
  },
  {
    "id_erp": 64368,
    "nome": "VOL 2/2 T. V. FUNGI 2,40",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.38,
    "setup": 900,
    "codigo_barra": 64368
  },
  {
    "id_erp": 67397,
    "nome": "VOL 2/2 T. V. FUNGI 2,40 B. LAM.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.38,
    "setup": 900,
    "codigo_barra": 67397
  },
  {
    "id_erp": 64369,
    "nome": "VOL 2/2 T. V. FUNGI 2,70",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.38,
    "setup": 900,
    "codigo_barra": 64369
  },
  {
    "id_erp": 67398,
    "nome": "VOL 2/2 T. V. FUNGI 2,70 B. LAM.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.38,
    "setup": 900,
    "codigo_barra": 67398
  },
  {
    "id_erp": 64370,
    "nome": "VOL 2/2 T. V. FUNGI 3,00",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.38,
    "setup": 900,
    "codigo_barra": 64370
  },
  {
    "id_erp": 67399,
    "nome": "VOL 2/2 T. V. FUNGI 3,00 B. LAM.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.38,
    "setup": 900,
    "codigo_barra": 67399
  },
  {
    "id_erp": 37492,
    "nome": "VOL 2/2 T. V. GENEBRA 1,40 B. MAD. QUAD.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 102,
    "setup": 900,
    "codigo_barra": 37492
  },
  {
    "id_erp": 37447,
    "nome": "VOL 2/2 T. V. GENEBRA 1,40 QUAD.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 102,
    "setup": 900,
    "codigo_barra": 37447
  },
  {
    "id_erp": 38412,
    "nome": "VOL 2/2 T. V. GENEBRA 1,40 X 0,90 B. MAD.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 102,
    "setup": 900,
    "codigo_barra": 38412
  },
  {
    "id_erp": 37489,
    "nome": "VOL 2/2 T. V. GENEBRA 1,50 B. MAD. QUAD.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 102,
    "setup": 900,
    "codigo_barra": 37489
  },
  {
    "id_erp": 37443,
    "nome": "VOL 2/2 T. V. GENEBRA 1,50 QUAD.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 102,
    "setup": 900,
    "codigo_barra": 37443
  },
  {
    "id_erp": 56424,
    "nome": "VOL 2/2 T. V. GENEBRA 1,80",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 102,
    "setup": 900,
    "codigo_barra": 56424
  },
  {
    "id_erp": 56425,
    "nome": "VOL 2/2 T. V. GENEBRA 2,00",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 102,
    "setup": 900,
    "codigo_barra": 56425
  },
  {
    "id_erp": 38396,
    "nome": "VOL 2/2 T. V. GENEBRA RET. 1,40 X 0,90",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 102,
    "setup": 900,
    "codigo_barra": 38396
  },
  {
    "id_erp": 69008,
    "nome": "VOL 2/2 T. V. GUANABARA 2,20 (1ª ETAPA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.32,
    "setup": 900,
    "codigo_barra": 69008
  },
  {
    "id_erp": 690089,
    "nome": "VOL 2/2 T. V. GUANABARA 2,20 (2ª ETAPA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.32,
    "setup": 900,
    "codigo_barra": 690089
  },
  {
    "id_erp": 69013,
    "nome": "VOL 2/2 T. V. GUANABARA 2,40 (1ª ETAPA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.32,
    "setup": 900,
    "codigo_barra": 69013
  },
  {
    "id_erp": 690139,
    "nome": "VOL 2/2 T. V. GUANABARA 2,40 (2ª ETAPA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.32,
    "setup": 900,
    "codigo_barra": 690139
  },
  {
    "id_erp": 69018,
    "nome": "VOL 2/2 T. V. GUANABARA 2,70 (1ª ETAPA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.32,
    "setup": 900,
    "codigo_barra": 69018
  },
  {
    "id_erp": 690189,
    "nome": "VOL 2/2 T. V. GUANABARA 2,70 (2ª ETAPA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.32,
    "setup": 900,
    "codigo_barra": 690189
  },
  {
    "id_erp": 69028,
    "nome": "VOL 2/2 T. V. GUANABARA 3,00 (1ª ETAPA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.32,
    "setup": 900,
    "codigo_barra": 69028
  },
  {
    "id_erp": 690289,
    "nome": "VOL 2/2 T. V. GUANABARA 3,00 (2ª ETAPA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.32,
    "setup": 900,
    "codigo_barra": 690289
  },
  {
    "id_erp": 51260,
    "nome": "VOL 2/2 T. V. INDIGO 1,46 B. MAD. RED.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 726,
    "setup": 1200,
    "codigo_barra": 51260
  },
  {
    "id_erp": 512609,
    "nome": "VOL 2/2 T. V. INDIGO 1,46 B. MAD. RED.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 350,
    "setup": 900,
    "codigo_barra": 512609
  },
  {
    "id_erp": 54585,
    "nome": "VOL 2/2 T. V. INDIGO 1,46 B. MAD. RED. S/ GIRATORIO",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 726,
    "setup": 1200,
    "codigo_barra": 54585
  },
  {
    "id_erp": 545859,
    "nome": "VOL 2/2 T. V. INDIGO 1,46 B. MAD. RED. S/ GIRATORIO",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 350,
    "setup": 900,
    "codigo_barra": 545859
  },
  {
    "id_erp": 51261,
    "nome": "VOL 2/2 T. V. INDIGO 1,66 B. MAD. RED.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 726,
    "setup": 1200,
    "codigo_barra": 51261
  },
  {
    "id_erp": 512619,
    "nome": "VOL 2/2 T. V. INDIGO 1,66 B. MAD. RED.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 350,
    "setup": 900,
    "codigo_barra": 512619
  },
  {
    "id_erp": 54586,
    "nome": "VOL 2/2 T. V. INDIGO 1,66 B. MAD. RED. S/ GIRATORIO",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 726,
    "setup": 1200,
    "codigo_barra": 54586
  },
  {
    "id_erp": 545869,
    "nome": "VOL 2/2 T. V. INDIGO 1,66 B. MAD. RED. S/ GIRATORIO",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 350,
    "setup": 900,
    "codigo_barra": 545869
  },
  {
    "id_erp": 50742,
    "nome": "VOL 2/2 T. V. INDIGO 1,86 B. MAD. RED.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 726,
    "setup": 1200,
    "codigo_barra": 50742
  },
  {
    "id_erp": 507429,
    "nome": "VOL 2/2 T. V. INDIGO 1,86 B. MAD. RED.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 350,
    "setup": 900,
    "codigo_barra": 507429
  },
  {
    "id_erp": 54587,
    "nome": "VOL 2/2 T. V. INDIGO 1,86 B. MAD. RED. S/ GIRATORIO",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 726,
    "setup": 1200,
    "codigo_barra": 54587
  },
  {
    "id_erp": 545879,
    "nome": "VOL 2/2 T. V. INDIGO 1,86 B. MAD. RED. S/ GIRATORIO",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 350,
    "setup": 900,
    "codigo_barra": 545879
  },
  {
    "id_erp": 55471,
    "nome": "VOL 2/2 T. V. INDIGO 2,06 B. MAD. RED.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 726,
    "setup": 1200,
    "codigo_barra": 55471
  },
  {
    "id_erp": 554719,
    "nome": "VOL 2/2 T. V. INDIGO 2,06 B. MAD. RED.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 350,
    "setup": 900,
    "codigo_barra": 554719
  },
  {
    "id_erp": 55472,
    "nome": "VOL 2/2 T. V. INDIGO 2,06 B. MAD. RED. S/ GIRATORIO",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 726,
    "setup": 1200,
    "codigo_barra": 55472
  },
  {
    "id_erp": 554729,
    "nome": "VOL 2/2 T. V. INDIGO 2,06 B. MAD. RED. S/ GIRATORIO",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 350,
    "setup": 900,
    "codigo_barra": 554729
  },
  {
    "id_erp": 68482,
    "nome": "VOL 2/2 T. V. LEME 2,20",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.02,
    "setup": 900,
    "codigo_barra": 68482
  },
  {
    "id_erp": 68483,
    "nome": "VOL 2/2 T. V. LEME 2,40",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.02,
    "setup": 900,
    "codigo_barra": 68483
  },
  {
    "id_erp": 68484,
    "nome": "VOL 2/2 T. V. LEME 2,70",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.02,
    "setup": 900,
    "codigo_barra": 68484
  },
  {
    "id_erp": 68485,
    "nome": "VOL 2/2 T. V. LEME 3,00",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.02,
    "setup": 900,
    "codigo_barra": 68485
  },
  {
    "id_erp": 55130,
    "nome": "VOL 2/2 T. V. LINCE 1,60",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 102,
    "setup": 900,
    "codigo_barra": 55130
  },
  {
    "id_erp": 37233,
    "nome": "VOL 2/2 T. V. LINCE 1,60 X 1,00",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 102,
    "setup": 900,
    "codigo_barra": 37233
  },
  {
    "id_erp": 37745,
    "nome": "VOL 2/2 T. V. LINCE 1,60 X 1,00 C/ FRISO",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 102,
    "setup": 900,
    "codigo_barra": 37745
  },
  {
    "id_erp": 37748,
    "nome": "VOL 2/2 T. V. LINCE 1,80",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 102,
    "setup": 900,
    "codigo_barra": 37748
  },
  {
    "id_erp": 37739,
    "nome": "VOL 2/2 T. V. LINCE 2,00",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 102,
    "setup": 900,
    "codigo_barra": 37739
  },
  {
    "id_erp": 55135,
    "nome": "VOL 2/2 T. V. LINEA/MENFIS 1,20 RED.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 90,
    "setup": 900,
    "codigo_barra": 55135
  },
  {
    "id_erp": 56849,
    "nome": "VOL 2/2 T. V. LINEA/MENFIS 1,20 RED. B. MAD.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 90,
    "setup": 900,
    "codigo_barra": 56849
  },
  {
    "id_erp": 54222,
    "nome": "VOL 2/2 T. V. LIZZA 1,80 CB",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 100,
    "setup": 900,
    "codigo_barra": 54222
  },
  {
    "id_erp": 38000,
    "nome": "VOL 2/2 T. V. LIZZA 2,20",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 100,
    "setup": 900,
    "codigo_barra": 38000
  },
  {
    "id_erp": 38080,
    "nome": "VOL 2/2 T. V. LIZZA 2,20 B. MAD.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 100,
    "setup": 900,
    "codigo_barra": 38080
  },
  {
    "id_erp": 38077,
    "nome": "VOL 2/2 T. V. LIZZA/DUNA 1,80",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 100,
    "setup": 900,
    "codigo_barra": 38077
  },
  {
    "id_erp": 37998,
    "nome": "VOL 2/2 T. V. LIZZA/DUNA 1,80 B. MAD.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 100,
    "setup": 900,
    "codigo_barra": 37998
  },
  {
    "id_erp": 38075,
    "nome": "VOL 2/2 T. V. LIZZA/DUNA 2,00 B. MAD.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 100,
    "setup": 900,
    "codigo_barra": 38075
  },
  {
    "id_erp": 37999,
    "nome": "VOL 2/2 T. V. LIZZA/DUNA RET. 2,00",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 100,
    "setup": 900,
    "codigo_barra": 37999
  },
  {
    "id_erp": 49505,
    "nome": "VOL 2/2 T. V. LUGO 1,80",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 102,
    "setup": 900,
    "codigo_barra": 49505
  },
  {
    "id_erp": 49506,
    "nome": "VOL 2/2 T. V. LUGO 1,80 B. MAD.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 102,
    "setup": 900,
    "codigo_barra": 49506
  },
  {
    "id_erp": 49507,
    "nome": "VOL 2/2 T. V. LUGO 2,00",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 102,
    "setup": 900,
    "codigo_barra": 49507
  },
  {
    "id_erp": 49508,
    "nome": "VOL 2/2 T. V. LUGO 2,00 B. MAD.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 102,
    "setup": 900,
    "codigo_barra": 49508
  },
  {
    "id_erp": 56429,
    "nome": "VOL 2/2 T. V. MARIN 2,00 T. DUPLO",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 780,
    "setup": 900,
    "codigo_barra": 56429
  },
  {
    "id_erp": 42132,
    "nome": "VOL 2/2 T. V. MARIN 2,20",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.08,
    "setup": 900,
    "codigo_barra": 42132
  },
  {
    "id_erp": 56433,
    "nome": "VOL 2/2 T. V. MARIN 2,20  T. DUPLO",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.08,
    "setup": 900,
    "codigo_barra": 56433
  },
  {
    "id_erp": 49337,
    "nome": "VOL 2/2 T. V. MARIN 2,40",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.08,
    "setup": 900,
    "codigo_barra": 49337
  },
  {
    "id_erp": 56418,
    "nome": "VOL 2/2 T. V. MARIN LX 2,14 T. DUPLO",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 90,
    "setup": 900,
    "codigo_barra": 56418
  },
  {
    "id_erp": 52200,
    "nome": "VOL 2/2 T. V. MARIN LX 2,20 X 1,20",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.08,
    "setup": 900,
    "codigo_barra": 52200
  },
  {
    "id_erp": 56419,
    "nome": "VOL 2/2 T. V. MARIN LX 2,34 T. DUPLO",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 90,
    "setup": 900,
    "codigo_barra": 56419
  },
  {
    "id_erp": 56420,
    "nome": "VOL 2/2 T. V. MARIN LX 2,64 T. DUPLO",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 780,
    "setup": 900,
    "codigo_barra": 56420
  },
  {
    "id_erp": 56421,
    "nome": "VOL 2/2 T. V. MARIN LX 2,94 T. DUPLO",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 780,
    "setup": 900,
    "codigo_barra": 56421
  },
  {
    "id_erp": 42302,
    "nome": "VOL 2/2 T. V. MARIN PLUS 1,40 QUAD.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.08,
    "setup": 900,
    "codigo_barra": 42302
  },
  {
    "id_erp": 42166,
    "nome": "VOL 2/2 T. V. MARIN PLUS 1,50 QUAD.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.08,
    "setup": 900,
    "codigo_barra": 42166
  },
  {
    "id_erp": 53498,
    "nome": "VOL 2/2 T. V. MARIN PLUS 1,60",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.08,
    "setup": 900,
    "codigo_barra": 53498
  },
  {
    "id_erp": 55138,
    "nome": "VOL 2/2 T. V. MARIN PLUS 1,60 T. DUPLO",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.08,
    "setup": 900,
    "codigo_barra": 55138
  },
  {
    "id_erp": 49858,
    "nome": "VOL 2/2 T. V. MARIN/DUNA PLUS 1,40 T. DUPLO",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.08,
    "setup": 900,
    "codigo_barra": 49858
  },
  {
    "id_erp": 49250,
    "nome": "VOL 2/2 T. V. MARIN/DUNA PLUS 1,50 T. DUPLO",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.08,
    "setup": 900,
    "codigo_barra": 49250
  },
  {
    "id_erp": 42283,
    "nome": "VOL 2/2 T. V. MARIN/RIVA 1,80",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.08,
    "setup": 900,
    "codigo_barra": 42283
  },
  {
    "id_erp": 42277,
    "nome": "VOL 2/2 T. V. MARIN/RIVA 2,00",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.08,
    "setup": 900,
    "codigo_barra": 42277
  },
  {
    "id_erp": 37364,
    "nome": "VOL 2/2 T. V. MENF/LIN 1,08 B. MAD. QUAD.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 90,
    "setup": 900,
    "codigo_barra": 37364
  },
  {
    "id_erp": 34500,
    "nome": "VOL 2/2 T. V. MENF/LIN/ELIS/MARR 1,20 X 0,90",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 90,
    "setup": 900,
    "codigo_barra": 34500
  },
  {
    "id_erp": 35551,
    "nome": "VOL 2/2 T. V. MENF/LIN/ELIS/MARR 1,40 X 0,90",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 90,
    "setup": 900,
    "codigo_barra": 35551
  },
  {
    "id_erp": 35555,
    "nome": "VOL 2/2 T. V. MENF/LIN/ELIS/MARR 1,60 X 0,90",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 90,
    "setup": 900,
    "codigo_barra": 35555
  },
  {
    "id_erp": 37342,
    "nome": "VOL 2/2 T. V. MENF/LIN/ELIS/MARR 1,60 X 0,90 B. MAD.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 90,
    "setup": 900,
    "codigo_barra": 37342
  },
  {
    "id_erp": 42666,
    "nome": "VOL 2/2 T. V. MENF/LIN/MARR 1,20 B. MAD. BARRIL",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 90,
    "setup": 900,
    "codigo_barra": 42666
  },
  {
    "id_erp": 42668,
    "nome": "VOL 2/2 T. V. MENF/LIN/MARR 1,60 B. MAD. BARRIL",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 90,
    "setup": 900,
    "codigo_barra": 42668
  },
  {
    "id_erp": 42219,
    "nome": "VOL 2/2 T. V. MENF/LIN/MARR/ELIS 1,20 BARRIL",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 90,
    "setup": 900,
    "codigo_barra": 42219
  },
  {
    "id_erp": 42667,
    "nome": "VOL 2/2 T. V. MENF/LIN/MARR/ELIS 1,40 B. MAD. BARRIL",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 90,
    "setup": 900,
    "codigo_barra": 42667
  },
  {
    "id_erp": 42664,
    "nome": "VOL 2/2 T. V. MENF/LIN/MARR/ELIS 1,40 BARRIL",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 90,
    "setup": 900,
    "codigo_barra": 42664
  },
  {
    "id_erp": 42665,
    "nome": "VOL 2/2 T. V. MENF/LIN/MARR/ELIS 1,60 BARRIL",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 90,
    "setup": 900,
    "codigo_barra": 42665
  },
  {
    "id_erp": 37354,
    "nome": "VOL 2/2 T. V. MENF/LINEA/MARR 1,20 X 0,90 B. MAD.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 90,
    "setup": 900,
    "codigo_barra": 37354
  },
  {
    "id_erp": 37352,
    "nome": "VOL 2/2 T. V. MENFIS/LINEA 1,06 B. MAD. RED.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 90,
    "setup": 900,
    "codigo_barra": 37352
  },
  {
    "id_erp": 34514,
    "nome": "VOL 2/2 T. V. MENFIS/LINEA 1,08 QUAD.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 90,
    "setup": 900,
    "codigo_barra": 34514
  },
  {
    "id_erp": 37344,
    "nome": "VOL 2/2 T. V. MENFIS/LINEA 1,30 B. MAD. RED.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 90,
    "setup": 900,
    "codigo_barra": 37344
  },
  {
    "id_erp": 37340,
    "nome": "VOL 2/2 T. V. MENFIS/LINEA 1,40 X 0,90 B. MAD.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 90,
    "setup": 900,
    "codigo_barra": 37340
  },
  {
    "id_erp": 35159,
    "nome": "VOL 2/2 T. V. MENFIS/LINEA/ELIS 1,30 RED.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 90,
    "setup": 900,
    "codigo_barra": 35159
  },
  {
    "id_erp": 34513,
    "nome": "VOL 2/2 T. V. MENFIS/LINEA/MARR 1,06 RED.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 90,
    "setup": 900,
    "codigo_barra": 34513
  },
  {
    "id_erp": 55148,
    "nome": "VOL 2/2 T. V. MILA 0,90 RED.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 90,
    "setup": 900,
    "codigo_barra": 55148
  },
  {
    "id_erp": 56510,
    "nome": "VOL 2/2 T. V. MILA 1,06 RED.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 90,
    "setup": 900,
    "codigo_barra": 56510
  },
  {
    "id_erp": 43143,
    "nome": "VOL 2/2 T. V. MILA 1,08 QUAD.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 102,
    "setup": 900,
    "codigo_barra": 43143
  },
  {
    "id_erp": 55149,
    "nome": "VOL 2/2 T. V. MILA 1,20 RED.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 90,
    "setup": 900,
    "codigo_barra": 55149
  },
  {
    "id_erp": 43140,
    "nome": "VOL 2/2 T. V. MILA 1,20 RET.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 102,
    "setup": 900,
    "codigo_barra": 43140
  },
  {
    "id_erp": 43128,
    "nome": "VOL 2/2 T. V. MILA 1,40 RET.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 102,
    "setup": 900,
    "codigo_barra": 43128
  },
  {
    "id_erp": 42650,
    "nome": "VOL 2/2 T. V. NEO 1,60 X 1,00",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 240,
    "setup": 900,
    "codigo_barra": 42650
  },
  {
    "id_erp": 42649,
    "nome": "VOL 2/2 T. V. NEO 1,80 X 1,10",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 240,
    "setup": 900,
    "codigo_barra": 42649
  },
  {
    "id_erp": 42648,
    "nome": "VOL 2/2 T. V. NEO 2,00 X 1,10",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 240,
    "setup": 900,
    "codigo_barra": 42648
  },
  {
    "id_erp": 42576,
    "nome": "VOL 2/2 T. V. NEO 2,20 X 1,20",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 240,
    "setup": 900,
    "codigo_barra": 42576
  },
  {
    "id_erp": 58072,
    "nome": "VOL 2/2 T. V. NEO LX 1,60",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 133,
    "setup": 900,
    "codigo_barra": 58072
  },
  {
    "id_erp": 55002,
    "nome": "VOL 2/2 T. V. NEO LX 1,80",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 133,
    "setup": 900,
    "codigo_barra": 55002
  },
  {
    "id_erp": 55003,
    "nome": "VOL 2/2 T. V. NEO LX 2,00",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 133,
    "setup": 900,
    "codigo_barra": 55003
  },
  {
    "id_erp": 55004,
    "nome": "VOL 2/2 T. V. NEO LX 2,20",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 133,
    "setup": 900,
    "codigo_barra": 55004
  },
  {
    "id_erp": 64357,
    "nome": "VOL 2/2 T. V. NEO LX 2,40",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 133,
    "setup": 900,
    "codigo_barra": 64357
  },
  {
    "id_erp": 64358,
    "nome": "VOL 2/2 T. V. NEO LX 2,70",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 133,
    "setup": 900,
    "codigo_barra": 64358
  },
  {
    "id_erp": 59459,
    "nome": "VOL 2/2 T. V. NEO LX 2,70 X 1,10",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 102,
    "setup": 900,
    "codigo_barra": 59459
  },
  {
    "id_erp": 50425,
    "nome": "VOL 2/2 T. V. NEO PLUS 1,40 QUAD.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 240,
    "setup": 900,
    "codigo_barra": 50425
  },
  {
    "id_erp": 50426,
    "nome": "VOL 2/2 T. V. NEO PLUS 1,60 QUAD.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 240,
    "setup": 900,
    "codigo_barra": 50426
  },
  {
    "id_erp": 55000,
    "nome": "VOL 2/2 T. V. NEO PLUS LX 1,40 QUAD.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 133,
    "setup": 900,
    "codigo_barra": 55000
  },
  {
    "id_erp": 55001,
    "nome": "VOL 2/2 T. V. NEO PLUS LX 1,60 QUAD.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 133,
    "setup": 900,
    "codigo_barra": 55001
  },
  {
    "id_erp": 55071,
    "nome": "VOL 2/2 T. V. NEPAL 1,80",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 200,
    "setup": 900,
    "codigo_barra": 55071
  },
  {
    "id_erp": 55440,
    "nome": "VOL 2/2 T. V. NEPAL 1,80 B. LAM.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 200,
    "setup": 900,
    "codigo_barra": 55440
  },
  {
    "id_erp": 55072,
    "nome": "VOL 2/2 T. V. NEPAL 2,00",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 200,
    "setup": 900,
    "codigo_barra": 55072
  },
  {
    "id_erp": 55767,
    "nome": "VOL 2/2 T. V. NEPAL 2,00 B. LAM.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 200,
    "setup": 900,
    "codigo_barra": 55767
  },
  {
    "id_erp": 55073,
    "nome": "VOL 2/2 T. V. NEPAL 2,20",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 200,
    "setup": 900,
    "codigo_barra": 55073
  },
  {
    "id_erp": 55768,
    "nome": "VOL 2/2 T. V. NEPAL 2,20 B. LAM.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 200,
    "setup": 900,
    "codigo_barra": 55768
  },
  {
    "id_erp": 55074,
    "nome": "VOL 2/2 T. V. NEPAL 2,40",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 200,
    "setup": 900,
    "codigo_barra": 55074
  },
  {
    "id_erp": 55769,
    "nome": "VOL 2/2 T. V. NEPAL 2,40 B. LAM.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 200,
    "setup": 900,
    "codigo_barra": 55769
  },
  {
    "id_erp": 42252,
    "nome": "VOL 2/2 T. V. OMEGA 2,00 T. DUPLO",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 780,
    "setup": 900,
    "codigo_barra": 42252
  },
  {
    "id_erp": 42239,
    "nome": "VOL 2/2 T. V. OMEGA 2,40",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 100,
    "setup": 900,
    "codigo_barra": 42239
  },
  {
    "id_erp": 52189,
    "nome": "VOL 2/2 T. V. OMEGA LX 2,14 T. DUPLO",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 90,
    "setup": 900,
    "codigo_barra": 52189
  },
  {
    "id_erp": 62891,
    "nome": "VOL 2/2 T. V. OMEGA LX 2,70 T. DUPLO",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 780,
    "setup": 900,
    "codigo_barra": 62891
  },
  {
    "id_erp": 49292,
    "nome": "VOL 2/2 T. V. OMEGA LX 2,94 T. DUPLO",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 780,
    "setup": 900,
    "codigo_barra": 49292
  },
  {
    "id_erp": 50930,
    "nome": "VOL 2/2 T. V. OMEGA LX/MARIN LX 2,34 T. DUPLO",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 780,
    "setup": 900,
    "codigo_barra": 50930
  },
  {
    "id_erp": 49267,
    "nome": "VOL 2/2 T. V. OMEGA LX/MARIN LX 2,64 T. DUPLO",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 780,
    "setup": 900,
    "codigo_barra": 49267
  },
  {
    "id_erp": 51194,
    "nome": "VOL 2/2 T. V. OMEGA/MARIN 1,60 RED. T. DUPLO",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 780,
    "setup": 900,
    "codigo_barra": 51194
  },
  {
    "id_erp": 45763,
    "nome": "VOL 2/2 T. V. OMEGA/MARIN 1,80 T. DUPLO",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 780,
    "setup": 900,
    "codigo_barra": 45763
  },
  {
    "id_erp": 42141,
    "nome": "VOL 2/2 T. V. OMEGA/MARIN 2,20 T. DUPLO",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 780,
    "setup": 900,
    "codigo_barra": 42141
  },
  {
    "id_erp": 37907,
    "nome": "VOL 2/2 T. V. PIETRA 2,20",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 133,
    "setup": 900,
    "codigo_barra": 37907
  },
  {
    "id_erp": 37883,
    "nome": "VOL 2/2 T. V. PIETRA 2,40",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 133,
    "setup": 900,
    "codigo_barra": 37883
  },
  {
    "id_erp": 38710,
    "nome": "VOL 2/2 T. V. PRISMA 1,80",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 200,
    "setup": 900,
    "codigo_barra": 38710
  },
  {
    "id_erp": 38920,
    "nome": "VOL 2/2 T. V. PRISMA 2,00",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 200,
    "setup": 900,
    "codigo_barra": 38920
  },
  {
    "id_erp": 38922,
    "nome": "VOL 2/2 T. V. PRISMA/DUNA RET. 2,20",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 200,
    "setup": 900,
    "codigo_barra": 38922
  },
  {
    "id_erp": 39581,
    "nome": "VOL 2/2 T. V. PRISMA/DUNA RET. 2,40",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 200,
    "setup": 900,
    "codigo_barra": 39581
  },
  {
    "id_erp": 34783,
    "nome": "VOL 2/2 T. V. PROVENCE 2,20",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 133,
    "setup": 900,
    "codigo_barra": 34783
  },
  {
    "id_erp": 79639,
    "nome": "VOL 2/2 T. V. RED. TORA 1200",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 286,
    "setup": 900,
    "codigo_barra": 79639
  },
  {
    "id_erp": 79634,
    "nome": "VOL 2/2 T. V. RED. TORA 900",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 240,
    "setup": 900,
    "codigo_barra": 79634
  },
  {
    "id_erp": 56323,
    "nome": "VOL 2/2 T. V. RIVA 1,80",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 100,
    "setup": 900,
    "codigo_barra": 56323
  },
  {
    "id_erp": 44171,
    "nome": "VOL 2/2 T. V. RIVA 1,80 B. LAM.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 100,
    "setup": 900,
    "codigo_barra": 44171
  },
  {
    "id_erp": 56326,
    "nome": "VOL 2/2 T. V. RIVA 2,00",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 100,
    "setup": 900,
    "codigo_barra": 56326
  },
  {
    "id_erp": 44172,
    "nome": "VOL 2/2 T. V. RIVA 2,00 B. LAM.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 100,
    "setup": 900,
    "codigo_barra": 44172
  },
  {
    "id_erp": 45010,
    "nome": "VOL 2/2 T. V. RIVA 2,20",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 200,
    "setup": 900,
    "codigo_barra": 45010
  },
  {
    "id_erp": 44173,
    "nome": "VOL 2/2 T. V. RIVA 2,20 B. LAM.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 200,
    "setup": 900,
    "codigo_barra": 44173
  },
  {
    "id_erp": 43315,
    "nome": "VOL 2/2 T. V. RIVA 2,40",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 200,
    "setup": 900,
    "codigo_barra": 43315
  },
  {
    "id_erp": 44174,
    "nome": "VOL 2/2 T. V. RIVA 2,40 B. LAM.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 200,
    "setup": 900,
    "codigo_barra": 44174
  },
  {
    "id_erp": 37356,
    "nome": "VOL 2/2 T. V. SAMA/LINCE S/FR 1,60 X 1,00 B. MAD.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 102,
    "setup": 900,
    "codigo_barra": 37356
  },
  {
    "id_erp": 38103,
    "nome": "VOL 2/2 T. V. SAMARA/GENEBRA 1,60 X 0,90",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 102,
    "setup": 900,
    "codigo_barra": 38103
  },
  {
    "id_erp": 38104,
    "nome": "VOL 2/2 T. V. SAMARA/GENEBRA 1,60 X 0,90 B. MAD.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 102,
    "setup": 900,
    "codigo_barra": 38104
  },
  {
    "id_erp": 37349,
    "nome": "VOL 2/2 T. V. SAMARA/GENEBRA 2,20 B. MAD.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 102,
    "setup": 900,
    "codigo_barra": 37349
  },
  {
    "id_erp": 37113,
    "nome": "VOL 2/2 T. V. SAMARA/GENEBRA RET. 2,20",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 102,
    "setup": 900,
    "codigo_barra": 37113
  },
  {
    "id_erp": 37026,
    "nome": "VOL 2/2 T. V. SAMARA/LINCE S/FR/GENEBRA 1,80",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 102,
    "setup": 900,
    "codigo_barra": 37026
  },
  {
    "id_erp": 37358,
    "nome": "VOL 2/2 T. V. SAMARA/LINCE S/FR/GENEBRA 1,80 B. MAD.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 102,
    "setup": 900,
    "codigo_barra": 37358
  },
  {
    "id_erp": 37110,
    "nome": "VOL 2/2 T. V. SAMARA/LINCE S/FR/GENEBRA 2,00",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 102,
    "setup": 900,
    "codigo_barra": 37110
  },
  {
    "id_erp": 37361,
    "nome": "VOL 2/2 T. V. SAMARA/LINCE S/FR/GENEBRA 2,00 B. MAD.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 102,
    "setup": 900,
    "codigo_barra": 37361
  },
  {
    "id_erp": 49232,
    "nome": "VOL 2/2 T. V. SCALA 1,80",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 133,
    "setup": 900,
    "codigo_barra": 49232
  },
  {
    "id_erp": 49885,
    "nome": "VOL 2/2 T. V. SCALA 1,80 B. LAM.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 133,
    "setup": 900,
    "codigo_barra": 49885
  },
  {
    "id_erp": 49233,
    "nome": "VOL 2/2 T. V. SCALA 2,00",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 133,
    "setup": 900,
    "codigo_barra": 49233
  },
  {
    "id_erp": 49886,
    "nome": "VOL 2/2 T. V. SCALA 2,00 B. LAM.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 133,
    "setup": 900,
    "codigo_barra": 49886
  },
  {
    "id_erp": 49234,
    "nome": "VOL 2/2 T. V. SCALA 2,20",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 133,
    "setup": 900,
    "codigo_barra": 49234
  },
  {
    "id_erp": 49887,
    "nome": "VOL 2/2 T. V. SCALA 2,20 B. LAM.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 133,
    "setup": 900,
    "codigo_barra": 49887
  },
  {
    "id_erp": 49235,
    "nome": "VOL 2/2 T. V. SCALA 2,40",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 133,
    "setup": 900,
    "codigo_barra": 49235
  },
  {
    "id_erp": 49888,
    "nome": "VOL 2/2 T. V. SCALA 2,40 B. LAM.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 133,
    "setup": 900,
    "codigo_barra": 49888
  },
  {
    "id_erp": 49236,
    "nome": "VOL 2/2 T. V. SCALA 2,70",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 133,
    "setup": 900,
    "codigo_barra": 49236
  },
  {
    "id_erp": 49355,
    "nome": "VOL 2/2 T. V. SCALA 2,70 B. LAM.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 133,
    "setup": 900,
    "codigo_barra": 49355
  },
  {
    "id_erp": 49237,
    "nome": "VOL 2/2 T. V. SCALA 3,00",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 133,
    "setup": 900,
    "codigo_barra": 49237
  },
  {
    "id_erp": 49356,
    "nome": "VOL 2/2 T. V. SCALA 3,00 B. LAM.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 133,
    "setup": 900,
    "codigo_barra": 49356
  },
  {
    "id_erp": 63834,
    "nome": "VOL 2/2 T. V. SCALA LX 2,40",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 133,
    "setup": 900,
    "codigo_barra": 63834
  },
  {
    "id_erp": 55161,
    "nome": "VOL 2/2 T. V. SIENA 0,90 RED.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 75,
    "setup": 900,
    "codigo_barra": 55161
  },
  {
    "id_erp": 51465,
    "nome": "VOL 2/2 T. V. SIENA 1,20 RED.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 75,
    "setup": 900,
    "codigo_barra": 51465
  },
  {
    "id_erp": 51465,
    "nome": "VOL 2/2 T. V. SIENA 1,20 RED.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 660,
    "setup": 900,
    "codigo_barra": 51465
  },
  {
    "id_erp": 51467,
    "nome": "VOL 2/2 T. V. SIENA 1,40 RED.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 100,
    "setup": 900,
    "codigo_barra": 51467
  },
  {
    "id_erp": 51468,
    "nome": "VOL 2/2 T. V. SIENA 1,60 RED.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 100,
    "setup": 900,
    "codigo_barra": 51468
  },
  {
    "id_erp": 51469,
    "nome": "VOL 2/2 T. V. SIENA 1,80 RED.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 100,
    "setup": 900,
    "codigo_barra": 51469
  },
  {
    "id_erp": 48805,
    "nome": "VOL 2/2 T. V. TANGO 1,80 X 1,10",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 240,
    "setup": 900,
    "codigo_barra": 48805
  },
  {
    "id_erp": 48806,
    "nome": "VOL 2/2 T. V. TANGO 2,00 X 1,10",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 240,
    "setup": 900,
    "codigo_barra": 48806
  },
  {
    "id_erp": 48807,
    "nome": "VOL 2/2 T. V. TANGO 2,20 X 1,20",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 240,
    "setup": 900,
    "codigo_barra": 48807
  },
  {
    "id_erp": 55172,
    "nome": "VOL 2/2 T. V. TANGO LX 1,80",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 133,
    "setup": 900,
    "codigo_barra": 55172
  },
  {
    "id_erp": 55173,
    "nome": "VOL 2/2 T. V. TANGO LX 2,00",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 133,
    "setup": 900,
    "codigo_barra": 55173
  },
  {
    "id_erp": 55174,
    "nome": "VOL 2/2 T. V. TANGO LX 2,20",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 133,
    "setup": 900,
    "codigo_barra": 55174
  },
  {
    "id_erp": 60162,
    "nome": "VOL 2/2 T. V. TARSILA 2,20",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 102,
    "setup": 900,
    "codigo_barra": 60162
  },
  {
    "id_erp": 60171,
    "nome": "VOL 2/2 T. V. TARSILA 2,20 B. LAM.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 102,
    "setup": 900,
    "codigo_barra": 60171
  },
  {
    "id_erp": 60163,
    "nome": "VOL 2/2 T. V. TARSILA 2,40",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 102,
    "setup": 900,
    "codigo_barra": 60163
  },
  {
    "id_erp": 60172,
    "nome": "VOL 2/2 T. V. TARSILA 2,40 B. LAM.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 102,
    "setup": 900,
    "codigo_barra": 60172
  },
  {
    "id_erp": 60164,
    "nome": "VOL 2/2 T. V. TARSILA 2,70",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 102,
    "setup": 900,
    "codigo_barra": 60164
  },
  {
    "id_erp": 60173,
    "nome": "VOL 2/2 T. V. TARSILA 2,70 B. LAM.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 102,
    "setup": 900,
    "codigo_barra": 60173
  },
  {
    "id_erp": 60165,
    "nome": "VOL 2/2 T. V. TARSILA 3,00",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 102,
    "setup": 900,
    "codigo_barra": 60165
  },
  {
    "id_erp": 60174,
    "nome": "VOL 2/2 T. V. TARSILA 3,00 B. LAM.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 102,
    "setup": 900,
    "codigo_barra": 60174
  },
  {
    "id_erp": 79582,
    "nome": "VOL 2/2 T. V. TRIADE 1,80 X 0,90",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 102,
    "setup": 900,
    "codigo_barra": 79582
  },
  {
    "id_erp": 60745,
    "nome": "VOL 2/2 T. V. TRIADE 2,00",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 102,
    "setup": 900,
    "codigo_barra": 60745
  },
  {
    "id_erp": 60746,
    "nome": "VOL 2/2 T. V. TRIADE 2,20",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 102,
    "setup": 900,
    "codigo_barra": 60746
  },
  {
    "id_erp": 60747,
    "nome": "VOL 2/2 T. V. TRIADE 2,40",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 102,
    "setup": 900,
    "codigo_barra": 60747
  },
  {
    "id_erp": 60748,
    "nome": "VOL 2/2 T. V. TRIADE 2,70",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 102,
    "setup": 900,
    "codigo_barra": 60748
  },
  {
    "id_erp": 60749,
    "nome": "VOL 2/2 T. V. TRIADE 3,00",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 102,
    "setup": 900,
    "codigo_barra": 60749
  },
  {
    "id_erp": 56423,
    "nome": "VOL 2/2 T. V. UOMINI 1,60 B. MAD. QUAD.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 904,
    "setup": 900,
    "codigo_barra": 56423
  },
  {
    "id_erp": 50219,
    "nome": "VOL 2/2 T. V. UOMINI 2,00 B. MAD.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 990,
    "setup": 900,
    "codigo_barra": 50219
  },
  {
    "id_erp": 46729,
    "nome": "VOL 2/2 T. V. UOMINI 2,20 B. MAD.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 990,
    "setup": 900,
    "codigo_barra": 46729
  },
  {
    "id_erp": 46730,
    "nome": "VOL 2/2 T. V. UOMINI 2,70 B. MAD.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.057,
    "setup": 900,
    "codigo_barra": 46730
  },
  {
    "id_erp": 62316,
    "nome": "VOL 2/2 T. V. UOMINI LX 2,20",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.08,
    "setup": 900,
    "codigo_barra": 62316
  },
  {
    "id_erp": 57663,
    "nome": "VOL 2/2 T. V. UOMINI LX 2,20 B. LAM.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 102,
    "setup": 900,
    "codigo_barra": 57663
  },
  {
    "id_erp": 62317,
    "nome": "VOL 2/2 T. V. UOMINI LX 2,40",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 200,
    "setup": 900,
    "codigo_barra": 62317
  },
  {
    "id_erp": 57664,
    "nome": "VOL 2/2 T. V. UOMINI LX 2,40 B. LAM.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 102,
    "setup": 900,
    "codigo_barra": 57664
  },
  {
    "id_erp": 62318,
    "nome": "VOL 2/2 T. V. UOMINI LX 2,70",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 200,
    "setup": 900,
    "codigo_barra": 62318
  },
  {
    "id_erp": 57665,
    "nome": "VOL 2/2 T. V. UOMINI LX 2,70 B. LAM.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 200,
    "setup": 900,
    "codigo_barra": 57665
  },
  {
    "id_erp": 62319,
    "nome": "VOL 2/2 T. V. UOMINI LX 3,00",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 200,
    "setup": 900,
    "codigo_barra": 62319
  },
  {
    "id_erp": 57666,
    "nome": "VOL 2/2 T. V. UOMINI LX 3,00 B. LAM.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 200,
    "setup": 900,
    "codigo_barra": 57666
  },
  {
    "id_erp": 57678,
    "nome": "VOL 2/2 T. V. UOMINI PLUS LX 1,60 QUAD. B. LAM.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 904,
    "setup": 900,
    "codigo_barra": 57678
  },
  {
    "id_erp": 57978,
    "nome": "VOL 2/2 T. V. UOMINI PLUS LX 1,60 RED. B. LAM.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 904,
    "setup": 900,
    "codigo_barra": 57978
  },
  {
    "id_erp": 46732,
    "nome": "VOL 2/2 T. V. UOMINI/DUNA/MARIN 1,40 B. MAD. QUAD.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 825,
    "setup": 900,
    "codigo_barra": 46732
  },
  {
    "id_erp": 45873,
    "nome": "VOL 2/2 T. V. UOMINI/VERMONT 2,40 B. MAD.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.115,
    "setup": 900,
    "codigo_barra": 45873
  },
  {
    "id_erp": 46731,
    "nome": "VOL 2/2 T. V. UOMINI/VERMONT 3,00 B. MAD.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.08,
    "setup": 900,
    "codigo_barra": 46731
  },
  {
    "id_erp": 46720,
    "nome": "VOL 2/2 T. V. VERMONT 1,80",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 50,
    "setup": 900,
    "codigo_barra": 46720
  },
  {
    "id_erp": 46558,
    "nome": "VOL 2/2 T. V. VERMONT 1,80 B. LAM.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 50,
    "setup": 900,
    "codigo_barra": 46558
  },
  {
    "id_erp": 46722,
    "nome": "VOL 2/2 T. V. VERMONT 2,00",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 50,
    "setup": 900,
    "codigo_barra": 46722
  },
  {
    "id_erp": 46559,
    "nome": "VOL 2/2 T. V. VERMONT 2,00 B. LAM.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 50,
    "setup": 900,
    "codigo_barra": 46559
  },
  {
    "id_erp": 46723,
    "nome": "VOL 2/2 T. V. VERMONT 2,20",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 50,
    "setup": 900,
    "codigo_barra": 46723
  },
  {
    "id_erp": 46727,
    "nome": "VOL 2/2 T. V. VERMONT 2,20 B. LAM.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 50,
    "setup": 900,
    "codigo_barra": 46727
  },
  {
    "id_erp": 56408,
    "nome": "VOL 2/2 T. V. VERMONT 2,20 B. MAD.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 990,
    "setup": 900,
    "codigo_barra": 56408
  },
  {
    "id_erp": 46724,
    "nome": "VOL 2/2 T. V. VERMONT 2,40",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 50,
    "setup": 900,
    "codigo_barra": 46724
  },
  {
    "id_erp": 46728,
    "nome": "VOL 2/2 T. V. VERMONT 2,40 B. LAM.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 50,
    "setup": 900,
    "codigo_barra": 46728
  },
  {
    "id_erp": 56409,
    "nome": "VOL 2/2 T. V. VERMONT 2,40 B. MAD.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 50,
    "setup": 900,
    "codigo_barra": 56409
  },
  {
    "id_erp": 64384,
    "nome": "VOL 2/2 T. V. VERMONT 2,70 B. LACA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.057,
    "setup": 900,
    "codigo_barra": 64384
  },
  {
    "id_erp": 65047,
    "nome": "VOL 2/2 T. V. VERMONT 2,70 B. LAM. - BATER COR COM A BASE",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.057,
    "setup": 900,
    "codigo_barra": 65047
  },
  {
    "id_erp": 56410,
    "nome": "VOL 2/2 T. V. VERMONT 2,70 B. MAD.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.057,
    "setup": 900,
    "codigo_barra": 56410
  },
  {
    "id_erp": 62370,
    "nome": "VOL 2/2 T. V. VERMONT 2,70 X 1,10",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 50,
    "setup": 900,
    "codigo_barra": 62370
  },
  {
    "id_erp": 64385,
    "nome": "VOL 2/2 T. V. VERMONT 3,00 B. LACA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.08,
    "setup": 900,
    "codigo_barra": 64385
  },
  {
    "id_erp": 65049,
    "nome": "VOL 2/2 T. V. VERMONT 3,00 B. LAM.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 50,
    "setup": 900,
    "codigo_barra": 65049
  },
  {
    "id_erp": 56411,
    "nome": "VOL 2/2 T. V. VERMONT 3,00 B. MAD.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.08,
    "setup": 900,
    "codigo_barra": 56411
  },
  {
    "id_erp": 33775,
    "nome": "VOL 2/2 T. V. VICENZA 1,60",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 133,
    "setup": 900,
    "codigo_barra": 33775
  },
  {
    "id_erp": 43242,
    "nome": "VOL 2/2 T. V. VICENZA 2,20",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 102,
    "setup": 900,
    "codigo_barra": 43242
  },
  {
    "id_erp": 43245,
    "nome": "VOL 2/2 T. V. VICENZA 2,20 B. MAD.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 102,
    "setup": 900,
    "codigo_barra": 43245
  },
  {
    "id_erp": 50905,
    "nome": "VOL 2/2 T. V. VITAL 1,60",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 80,
    "setup": 900,
    "codigo_barra": 50905
  },
  {
    "id_erp": 51042,
    "nome": "VOL 2/2 T. V. VITAL 1,60 B. MAD",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 80,
    "setup": 900,
    "codigo_barra": 51042
  },
  {
    "id_erp": 50906,
    "nome": "VOL 2/2 T. V. VITAL 1,80",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 80,
    "setup": 900,
    "codigo_barra": 50906
  },
  {
    "id_erp": 51045,
    "nome": "VOL 2/2 T. V. VITAL 1,80 B. MAD.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 80,
    "setup": 900,
    "codigo_barra": 51045
  },
  {
    "id_erp": 50907,
    "nome": "VOL 2/2 T. V. VITAL 2,00",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 80,
    "setup": 900,
    "codigo_barra": 50907
  },
  {
    "id_erp": 51034,
    "nome": "VOL 2/2 T. V. VITAL 2,00 B. MAD.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 80,
    "setup": 900,
    "codigo_barra": 51034
  },
  {
    "id_erp": 50908,
    "nome": "VOL 2/2 T. V. VITAL 2,20",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 80,
    "setup": 900,
    "codigo_barra": 50908
  },
  {
    "id_erp": 51039,
    "nome": "VOL 2/2 T. V. VITAL 2,20 B. MAD.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 80,
    "setup": 900,
    "codigo_barra": 51039
  },
  {
    "id_erp": 51048,
    "nome": "VOL 2/2 T. V. VITAL PLUS 1,20 B. MAD. QUAD.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 80,
    "setup": 900,
    "codigo_barra": 51048
  },
  {
    "id_erp": 50903,
    "nome": "VOL 2/2 T. V. VITAL PLUS 1,20 QUAD.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 80,
    "setup": 900,
    "codigo_barra": 50903
  },
  {
    "id_erp": 51324,
    "nome": "VOL 2/2 T. V. VITAL PLUS 1,40 B. MAD. QUAD.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 80,
    "setup": 900,
    "codigo_barra": 51324
  },
  {
    "id_erp": 51323,
    "nome": "VOL 2/2 T. V. VITAL PLUS 1,40 QUAD.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 80,
    "setup": 900,
    "codigo_barra": 51323
  },
  {
    "id_erp": 51019,
    "nome": "VOL 2/2 T. V. VITAL PLUS 1,50 B. MAD. QUAD.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 80,
    "setup": 900,
    "codigo_barra": 51019
  },
  {
    "id_erp": 50904,
    "nome": "VOL 2/2 T. V. VITAL PLUS 1,50 QUAD.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 80,
    "setup": 900,
    "codigo_barra": 50904
  },
  {
    "id_erp": 46764,
    "nome": "VOL 2/2 T. V. VITRA 1,60",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 102,
    "setup": 900,
    "codigo_barra": 46764
  },
  {
    "id_erp": 45847,
    "nome": "VOL 2/2 T. V. VITRA/ELOA 1,80",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 102,
    "setup": 900,
    "codigo_barra": 45847
  },
  {
    "id_erp": 45849,
    "nome": "VOL 2/2 T. V. VITRA/ELOA 2,00",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 102,
    "setup": 900,
    "codigo_barra": 45849
  },
  {
    "id_erp": 45838,
    "nome": "VOL 2/2 T. V. VITRA/ELOA 2,20",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 133,
    "setup": 900,
    "codigo_barra": 45838
  },
  {
    "id_erp": 45851,
    "nome": "VOL 2/2 T. V. VITRA/ELOA 2,40",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 133,
    "setup": 900,
    "codigo_barra": 45851
  },
  {
    "id_erp": 50662,
    "nome": "VOL 2/2 T. V. VOLPI 1,20",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 102,
    "setup": 900,
    "codigo_barra": 50662
  },
  {
    "id_erp": 50668,
    "nome": "VOL 2/2 T. V. VOLPI 1,20 B. MAD.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 102,
    "setup": 900,
    "codigo_barra": 50668
  },
  {
    "id_erp": 50663,
    "nome": "VOL 2/2 T. V. VOLPI 1,40",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 102,
    "setup": 900,
    "codigo_barra": 50663
  },
  {
    "id_erp": 50669,
    "nome": "VOL 2/2 T. V. VOLPI 1,40 B. MAD.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 102,
    "setup": 900,
    "codigo_barra": 50669
  },
  {
    "id_erp": 50664,
    "nome": "VOL 2/2 T. V. VOLPI 1,60",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 102,
    "setup": 900,
    "codigo_barra": 50664
  },
  {
    "id_erp": 50670,
    "nome": "VOL 2/2 T. V. VOLPI 1,60 B. MAD.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 102,
    "setup": 900,
    "codigo_barra": 50670
  },
  {
    "id_erp": 50665,
    "nome": "VOL 2/2 T. V. VOLPI 1,80",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 102,
    "setup": 900,
    "codigo_barra": 50665
  },
  {
    "id_erp": 50671,
    "nome": "VOL 2/2 T. V. VOLPI 1,80 B. MAD.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 102,
    "setup": 900,
    "codigo_barra": 50671
  },
  {
    "id_erp": 50666,
    "nome": "VOL 2/2 T. V. VOLPI 2,00",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 102,
    "setup": 900,
    "codigo_barra": 50666
  },
  {
    "id_erp": 50672,
    "nome": "VOL 2/2 T. V. VOLPI 2,00 B. MAD.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 102,
    "setup": 900,
    "codigo_barra": 50672
  },
  {
    "id_erp": 50667,
    "nome": "VOL 2/2 T. V. VOLPI 2,20",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 102,
    "setup": 900,
    "codigo_barra": 50667
  },
  {
    "id_erp": 50673,
    "nome": "VOL 2/2 T. V. VOLPI 2,20 B. MAD.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 102,
    "setup": 900,
    "codigo_barra": 50673
  },
  {
    "id_erp": 70700,
    "nome": "VOL 2/2 T. VIDRO ORBITA 2,20 X 1,20 S/ DETALHE",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 720,
    "setup": 900,
    "codigo_barra": 70700
  },
  {
    "id_erp": 707009,
    "nome": "VOL 2/2 T. VIDRO ORBITA 2,20 X 1,20 S/ DETALHE",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 720,
    "setup": 900,
    "codigo_barra": 707009
  },
  {
    "id_erp": 81243,
    "nome": "VOL 2/2 T.MAD. AMBAR CORPORATIVA 1,60",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.2,
    "setup": 900,
    "codigo_barra": 81243
  },
  {
    "id_erp": 57050,
    "nome": "VOL 2/2 T.MAD. FUNGI 2,60 - MEDIDA ESPECIAL",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.38,
    "setup": 900,
    "codigo_barra": 57050
  },
  {
    "id_erp": 84335,
    "nome": "VOL 2/2 T.MAD. LEME 3,10 X 1,20 - MEDIDA ESPECIAL",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.02,
    "setup": 900,
    "codigo_barra": 84335
  },
  {
    "id_erp": 77914,
    "nome": "VOL 2/2 T.MAD. ORG. MARE 0,90",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 420,
    "setup": 900,
    "codigo_barra": 77914
  },
  {
    "id_erp": 73228,
    "nome": "VOL 2/2 T.PEDRA FUNGI 2,40 B. LACA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.38,
    "setup": 900,
    "codigo_barra": 73228
  },
  {
    "id_erp": 69687,
    "nome": "VOL 2/2 T.PEDRA HELIX 3,00 B. LACA (1ª ETAPA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.02,
    "setup": 900,
    "codigo_barra": 69687
  },
  {
    "id_erp": 73336,
    "nome": "VOL 2/2 T.PEDRA ORBITA 2,40 - TAMPO ESPECIAL",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 600,
    "setup": 900,
    "codigo_barra": 73336
  },
  {
    "id_erp": 733369,
    "nome": "VOL 2/2 T.PEDRA ORBITA 2,40 - TAMPO ESPECIAL",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 600,
    "setup": 900,
    "codigo_barra": 733369
  },
  {
    "id_erp": 71525,
    "nome": "VOL 2/2 T.V. AMBAR 1,40 X 1,00",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 600,
    "setup": 900,
    "codigo_barra": 71525
  },
  {
    "id_erp": 71454,
    "nome": "VOL 2/2 T.V. AMBAR 1,60 X 1,20",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.2,
    "setup": 900,
    "codigo_barra": 71454
  },
  {
    "id_erp": 71973,
    "nome": "VOL 2/2 T.V. FUNGI 3,20 B. LACA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.38,
    "setup": 900,
    "codigo_barra": 71973
  },
  {
    "id_erp": 76753,
    "nome": "VOL 2/2 T.V. GUANABARA 1,80 X 1,00 (1ª ETAPA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.2,
    "setup": 900,
    "codigo_barra": 76753
  },
  {
    "id_erp": 76753,
    "nome": "VOL 2/2 T.V. GUANABARA 1,80 X 1,00 (2ª ETAPA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.2,
    "setup": 900,
    "codigo_barra": 76753
  },
  {
    "id_erp": 76837,
    "nome": "VOL 2/2 T.V. GUANABARA 2,00 X 1,10 (1ª ETAPA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.32,
    "setup": 900,
    "codigo_barra": 76837
  },
  {
    "id_erp": 768379,
    "nome": "VOL 2/2 T.V. GUANABARA 2,00 X 1,10 (2ª ETAPA)",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.32,
    "setup": 900,
    "codigo_barra": 768379
  },
  {
    "id_erp": 76433,
    "nome": "VOL 2/2 T.V. LEME 2,00 X 1,00",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.02,
    "setup": 900,
    "codigo_barra": 76433
  },
  {
    "id_erp": 70312,
    "nome": "VOL 2/2 T.V. LINEA 1,40 RED -  MEDIDA ESPECIAL",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.56,
    "setup": 900,
    "codigo_barra": 70312
  },
  {
    "id_erp": 71046,
    "nome": "VOL 2/2 T.V. NEO LX 1,80 X 0,90 - MEDIDA ESPECIAL",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.08,
    "setup": 900,
    "codigo_barra": 71046
  },
  {
    "id_erp": 73402,
    "nome": "VOL 2/2 T.V. ORLA 1,40 C/ GIRATORIO",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 600,
    "setup": 900,
    "codigo_barra": 73402
  },
  {
    "id_erp": 73400,
    "nome": "VOL 2/2 T.V. ORLA 1,60 C/ GIRATORIO",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 600,
    "setup": 900,
    "codigo_barra": 73400
  },
  {
    "id_erp": 72921,
    "nome": "VOL 2/2 T.V. ORLA 1,80 C/ GIRATORIO",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 3.6,
    "setup": 900,
    "codigo_barra": 72921
  },
  {
    "id_erp": 72923,
    "nome": "VOL 2/2 T.V. ORLA 1,80 S/ GIRATORIO",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 600,
    "setup": 900,
    "codigo_barra": 72923
  },
  {
    "id_erp": 72078,
    "nome": "VOL 2/2 T.V. ORLA 2,00 C/ GIRATORIO",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 600,
    "setup": 900,
    "codigo_barra": 72078
  },
  {
    "id_erp": 73556,
    "nome": "VOL 2/2 T.V. SIENA 1,60 RED. C/ GIRATORIO",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 600,
    "setup": 900,
    "codigo_barra": 73556
  },
  {
    "id_erp": 73137,
    "nome": "VOL 2/2 T.V. SIENA 1,80 C/ GIRATORIO",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 600,
    "setup": 900,
    "codigo_barra": 73137
  },
  {
    "id_erp": 73560,
    "nome": "VOL 2/2 T.V. SIENA 2,00 RED. S/ GIRATORIO",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 600,
    "setup": 900,
    "codigo_barra": 73560
  },
  {
    "id_erp": 75822,
    "nome": "VOL 2/2 T.V. TRIADE 2,40 X 0,90 - MEDIDA ESPECIAL",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 102,
    "setup": 900,
    "codigo_barra": 75822
  },
  {
    "id_erp": 70576,
    "nome": "VOL 2/2 T.V. UOMINI PLUS LX 1,60 RED",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 900,
    "setup": 900,
    "codigo_barra": 70576
  },
  {
    "id_erp": 76616,
    "nome": "VOL 2/2 TAMPO FUNGI 2,50 X 1,10 T. PEDRA - MEDIDA ESPECIAL",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.38,
    "setup": 900,
    "codigo_barra": 76616
  },
  {
    "id_erp": 62250,
    "nome": "VOL 2/2 TAMPO MITRE 3,00 T. MAD.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 180,
    "setup": 900,
    "codigo_barra": 62250
  },
  {
    "id_erp": 34287,
    "nome": "VOL 2/3 BARRA 1010 MESA ELEGANCE 1,80",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 170,
    "setup": 480,
    "codigo_barra": 34287
  },
  {
    "id_erp": 34205,
    "nome": "VOL 2/3 BARRA 1160 MESA ELEGANCE 2,00/2,20",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 170,
    "setup": 480,
    "codigo_barra": 34205
  },
  {
    "id_erp": 35595,
    "nome": "VOL 2/3 BARRA 810 MESA ELEGANCE 1,60",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 170,
    "setup": 480,
    "codigo_barra": 35595
  },
  {
    "id_erp": 21873,
    "nome": "VOL 2/3 LATERAL/FUNDO/BASE CRIST. CAROLINA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 60,
    "setup": 900,
    "codigo_barra": 21873
  },
  {
    "id_erp": 21873,
    "nome": "VOL 2/3 LATERAL/FUNDO/BASE CRIST. CAROLINA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 60,
    "setup": 900,
    "codigo_barra": 21873
  },
  {
    "id_erp": 31827,
    "nome": "VOL 2/3 LATERAL/FUNDO/BASE CRIST. CAROLINA DUPLA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 90,
    "setup": 900,
    "codigo_barra": 31827
  },
  {
    "id_erp": 31827,
    "nome": "VOL 2/3 LATERAL/FUNDO/BASE CRIST. CAROLINA DUPLA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 60,
    "setup": 900,
    "codigo_barra": 31827
  },
  {
    "id_erp": 56894,
    "nome": "VOL 2/3 TAMPO MITRE 2,20",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 180,
    "setup": 900,
    "codigo_barra": 56894
  },
  {
    "id_erp": 568949,
    "nome": "VOL 2/3 TAMPO MITRE 2,20",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 470,
    "setup": 1200,
    "codigo_barra": 568949
  },
  {
    "id_erp": 56895,
    "nome": "VOL 2/3 TAMPO MITRE 2,40",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 180,
    "setup": 900,
    "codigo_barra": 56895
  },
  {
    "id_erp": 568959,
    "nome": "VOL 2/3 TAMPO MITRE 2,40",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 470,
    "setup": 1200,
    "codigo_barra": 568959
  },
  {
    "id_erp": 56896,
    "nome": "VOL 2/3 TAMPO MITRE 2,70",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 180,
    "setup": 900,
    "codigo_barra": 56896
  },
  {
    "id_erp": 568969,
    "nome": "VOL 2/3 TAMPO MITRE 2,70",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 660,
    "setup": 1200,
    "codigo_barra": 568969
  },
  {
    "id_erp": 56897,
    "nome": "VOL 2/3 TAMPO MITRE 3,00",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 180,
    "setup": 900,
    "codigo_barra": 56897
  },
  {
    "id_erp": 568979,
    "nome": "VOL 2/3 TAMPO MITRE 3,00",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 470,
    "setup": 1200,
    "codigo_barra": 568979
  },
  {
    "id_erp": 33346,
    "nome": "VOL 2/4 LATERAL CRISTALEIRA PORTINARI MAD. DUPLA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.08,
    "setup": 900,
    "codigo_barra": 33346
  },
  {
    "id_erp": 36950,
    "nome": "VOL 3/3 T. V. ELEGANCE 1,60",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 133,
    "setup": 900,
    "codigo_barra": 36950
  },
  {
    "id_erp": 35284,
    "nome": "VOL 3/3 T. V. ELEGANCE 2,40",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 133,
    "setup": 900,
    "codigo_barra": 35284
  },
  {
    "id_erp": 33348,
    "nome": "VOL 4/4 FUNDO/ESP. CRIST. PORTINARI MAD. DUPLA",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 1.08,
    "setup": 900,
    "codigo_barra": 33348
  },
  {
    "id_erp": 62462,
    "nome": "VOL  TAMPO MITRE 2,40 T. MAD.",
    "equipamentos": [
      4,
      5
    ],
    "tempo": 180,
    "setup": 900,
    "codigo_barra": 62462
  }
]

def safe_int(value, default=1):
    """Converte valor para inteiro de forma segura."""
    try:
        return int(value)
    except (ValueError, TypeError):
        return default

class Model:
    def __init__(self, nome, equipamentos, tempo, codigo_barra, id_erp):
        self.nome = str(nome)
        self.equipamentos = [safe_int(e) for e in equipamentos] if isinstance(equipamentos, list) else []
        self.tempo = safe_int(tempo)
        self.codigo_barra = str(codigo_barra)
        self.id_erp = str(id_erp)

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            nome=data.get("nome", ""),
            equipamentos=data.get("equipamentos", []),
            tempo=data.get("tempo", 0),
            codigo_barra=data.get("codigo_barra", ""),
            id_erp=data.get("id_erp", "")
        )

    def to_dict(self):
        return {
            "nome": self.nome,
            "equipamentos": self.equipamentos,
            "tempo": self.tempo,
            "codigo_barra": self.codigo_barra,
            "id_erp": self.id_erp
        }


objetos = [Model.from_dict(item) for item in dados]
saida = [obj.to_dict() for obj in objetos]

with open("saida.txt", "w", encoding="utf-8") as f:
    json.dump(saida, f, ensure_ascii=False, indent=2)

print("Arquivo 'saida.txt' gerado com sucesso ✅")