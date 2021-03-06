class ExcelDreamsMapping:

    def __init__(self):
        pass

    @staticmethod
    def marital_status_codes():
        return {
            'Single': 1,
            'Married / Cohabiting': 2,
            'Separated / Devorced': 3,
            'Widowed': 4,
        }

    @staticmethod
    def implementing_partner():
        return {
            'Afya Jijini': 1,
            'AIHA': 2,
            'Aphiaplus Western': 3,
            'Global Communities': 4,
            'Henry Jackson Foundation': 5,
            'HWWK' : 6,
            'IMC': 7,
            'IRDO': 8,
            'LVCT Health': 9,
            'Peace Corps': 10,
        }

    @staticmethod
    def county():
        return {
            'HOMA_BAY': 3,
            'KISUMU': 2,
            'NAIROBI': 1,
            'SIAYA': 4,
        }

    @staticmethod
    def sub_county():
        return {
            'ALEGO USONGA': 39 ,
            'BONDO': 40 ,
            'DAGORETTI NORTH': 45 ,
            'DAGORETTI SOUTH': 46 ,
            'EMBAKASI CENTRAL': 47 ,
            'EMBAKASI EAST': 48 ,
            'EMBAKASI NORTH': 49 ,
            'EMBAKASI SOUTH': 50 ,
            'EMBAKASI WEST': 51 ,
            'GEM': 41 ,
            'HOMA BAY TOWN': 61 ,
            'KABONDO KASIPUL': 62 ,
            'KAMUKUNJI': 52 ,
            'KARACHUONYO': 63 ,
            'KASARANI': 53 ,
            'KASIPUL': 64 ,
            'KIBRA': 54 ,
            'KISUMU CENTRAL': 69 ,
            'KISUMU EAST': 70 ,
            'KISUMU WEST': 71 ,
            'LANGATA': 55 ,
            'MAKADARA': 56 ,
            'MATHARE': 57 ,
            'MBITA': 65 ,
            'MUHORONI': 72 ,
            'NDHIWA': 66 ,
            'NYAKACH': 73 ,
            'NYANDO': 74 ,
            'RANGWE': 67 ,
            'RARIEDA': 42 ,
            'ROYSAMBU': 76 ,
            'RUARAKA': 58 ,
            'SEME': 75 ,
            'STAREHE': 59 ,
            'SUBA': 68 ,
            'UGENYA': 43 ,
            'UGUNJA': 44 ,
            'WESTLANDS': 60 ,
        }

    @staticmethod
    def ward_by_code():
        return {
            '1208': 257,
            '1437': 300,
            '1207': 258,
            '1401': 334,
            '1438': 301,
            '1232': 199,
            '1165': 350,
            '1171': 362,
            '1223': 206,
            '1192': 242,
            '1218': 252,
            '1176': 356,
            '1203': 262,
            '1214': 247,
            '1396': 305,
            '1412': 286,
            '1413': 287,
            '1414': 288,
            '1415': 289,
            '1181': 368,
            '1173': 223,
            '1238': 363,
            '1224': 207,
            '1206': 259,
            '1204': 263,
            '1159': 373,
            '1435': 302,
            '1436': 303,
            '1423': 281,
            '1373': 266,
            '1255': 211,
            '1391': 330,
            '1258': 227,
            '1257': 228,
            '1432': 320,
            '1242': 191,
            '1241': 192,
            '1244': 193,
            '1243': 194,
            '1445': 324,
            '1447': 325,
            '1406': 291,
            '1375': 267,
            '1226': 195,
            '1227': 196,
            '1209': 260,
            '1249': 216,
            '1239': 224,
            '1395': 331,
            '1392': 332,
            '1186': 237,
            '1259': 229,
            '1369': 345,
            '1246': 217,
            '1233': 200,
            '1250': 218,
            '1251': 219,
            '1247': 220,
            '1381': 315,
            '1411': 290,
            '1429': 296,
            '1368': 346,
            '1398': 306,
            '1254': 212,
            '1372': 268,
            '1417': 276,
            '1416': 277,
            '1418': 278,
            '1236': 201,
            '1450': 326,
            '1234': 202,
            '1374': 269,
            '1371': 270,
            '1193': 243,
            '1366': 347,
            '1210': 261,
            '1240': 225,
            '1229': 197,
            '1228': 198,
            '1190': 238,
            '1187': 239,
            '1419': 279,
            '1200': 231,
            '1405': 335,
            '1407': 292,
            '1408': 293,
            '1245': 221,
            '1410': 294,
            '1386': 310,
            '1256': 213,
            '1443': 339,
            '1387': 311,
            '1422': 282,
            '1404': 336,
            '1446': 327,
            '1388': 312,
            '1433': 321,
            '1188': 240,
            '1430': 322,
            '1199': 232,
            '1213': 248,
            '1403': 337,
            '1420': 280,
            '1252': 214,
            '1197': 233,
            '1425': 283,
            '1211': 249,
            '1449': 328,
            '1370': 348,
            '1428': 297,
            '1383': 316,
            '1215': 250,
            '1376': 271,
            '1397': 307,
            '1439': 340,
            '1444': 341,
            '1382': 317,
            '1377': 272,
            '1440': 342,
            '1448': 329,
            '1399': 308,
            '1167': 351,
            '1169': 364,
            '1248': 222,
            '1231': 203,
            '1217': 253,
            '1180': 357,
            '1205': 264,
            '1158': 374,
            '1183': 369,
            '1195': 244,
            '1189': 241,
            '1201': 234,
            '1385': 318,
            '1212': 251,
            '1442': 343,
            '1367': 349,
            '1409': 295,
            '1434': 304,
            '1196': 235,
            '1378': 273,
            '1394': 354, # Roysambu needs to be corrected
            '1400': 309,
            '1260': 230,
            '1253': 215,
            '1390': 313,
            '1198': 236,
            '1166': 352,
            '1160': 377,
            '1161': 378,
            '1168': 353,
            '1220': 254,
            '1174': 365,
            '1222': 208,
            '1177': 358,
            '1184': 370,
            '1191': 245,
            '1216': 255,
            '1384': 319,
            '1162': 379,
            '1157': 375,
            '1426': 298,
            '1427': 299,
            '1421': 284,
            '1163': 354,
            '1402': 338,
            '1424': 285,
            '1379': 274,
            '1431': 323,
            '1380': 275,
            '1235': 204,
            '1164': 355,
            '1182': 371,
            '1170': 226,
            '1237': 366,
            '1225': 209,
            '1230': 205,
            '1221': 210,
            '1194': 246,
            '1219': 256,
            '1179': 359,
            '1202': 265,
            '1156': 376,
            '1185': 372,
            '1175': 360,
            '1389': 314,
            '1172': 367,
            '1178': 361,
            '1393': 333,
            '1441': 344,
        }

    @staticmethod
    def ward_by_name():
        return {
            'AHERO': '257',
            'AIRBASE': '300',
            'AWASI/ONJIKO': '258',
            'BABA DOGO': '334',
            'CALIFORNIA': '301',
            'CENTRAL': '199',
            'CENTRAL ALEGO': '350',
            'CENTRAL GEM': '362',
            'CENTRAL KASIPUL': '206',
            'CENTRAL KISUMU': '242',
            'CENTRAL NYAKACH': '252',
            'CENTRAL SAKWA': '356',
            'CENTRAL SEME': '262',
            'CHEMELIL': '247',
            'CLAYCITY': '305',
            'DANDORA AREA I': '286',
            'DANDORA AREA II': '287',
            'DANDORA AREA III': '288',
            'DANDORA AREA IV': '289',
            'EAST ASEMBO': '368',
            'EAST GEM': '223',
            'EAST GEM': '363',
            'EAST KAMAGAK': '207',
            'EAST KANO/WAWIDHI': '259',
            'EAST SEME': '263',
            'EAST UGENYA': '373',
            'EASTLEIGH NORTH': '302',
            'EASTLEIGH SOUTH': '303',
            'EMBAKASI': '281',
            'GATINA': '266',
            'GEMBE': '211',
            'GITHURAI': '330',
            'GWASSI NORTH': '227',
            'GWASSI SOUTH': '228',
            'HARAMBEE': '320',
            'HOMA BAY ARUJO': '191',
            'HOMA BAY CENTRAL': '192',
            'HOMA BAY EAST': '193',
            'HOMA BAY WEST': '194',
            'HOSPITAL': '324',
            'HURUMA': '325',
            'IMARA DAIMA': '291',
            'KABIRO': '267',
            'KABONDO EAST': '195',
            'KABONDO WEST': '196',
            'KABONYO/KANYAGWAL': '260',
            'KABUOCH SOUTH/PALA': '216',
            'KAGAN': '224',
            'KAHAWA': '331',
            'KAHAWA WEST': '332',
            'KAJULU': '237',
            'KAKSINGRI WEST': '229',
            'KANGEMI': '345',
            'KANYADOTO': '217',
            'KANYALUO': '200',
            'KANYAMWA KOLOGI': '218',
            'KANYAMWA KOSEWE': '219',
            'KANYIKELA': '220',
            'KAREN': '315',
            'KARIOBANGI NORTH': '290',
            'KARIOBANGI SOUTH': '296',
            'KARURA': '346',
            'KASARANI': '306',
            'KASGUNGA': '212',
            'KAWANGWARE': '268',
            'KAYOLE CENTRAL': '276',
            'KAYOLE NORTH': '277',
            'KAYOLE SOUTH': '278',
            'KENDU BAY TOWN': '201',
            'KIAMAIKO': '326',
            'KIBIRI': '202',
            'KILELESHWA': '269',
            'KILIMANI': '270',
            'KISUMU NORTH': '243',
            'KITISURU': '347',
            'KOBURA': '261',
            'KOCHIA': '225',
            'KOJWACH': '197',
            'KOKWANYO/KAKELO': '198',
            'KOLWA CENTRAL': '238',
            'KOLWA EAST': '239',
            'KOMAROCK': '279',
            'KONDELE': '231',
            'KOROGOCHO': '335',
            'KWA NJENGA': '292',
            'KWA REUBEN': '293',
            'KWABWAI': '221',
            'KWARE': '294',
            'LAINI SABA': '310',
            'LAMBWE': '213',
            'LANDIMAWE': '339',
            'LINDI': '311',
            'LOWER SAVANNAH': '282',
            'LUCKY SUMMER': '336',
            'MABATINI': '327',
            'MAKINA': '312',
            'MAKONGENI': '321',
            'MANYATTA 'B'': '240',
            'MARINGO/HAMZA': '322',
            'MARKET MILIMANI': '232',
            'MASOGO/NYANG\'OMA': '248',
            'MATHARE NORTH': '337',
            'MATOPENI': '280',
            'MFANGANO ISLAND': '214',
            'MIGOSI': '233',
            'MIHANGO': '283',
            'MIWANI': '249',
            'MLANGO KUBWA': '328',
            'MOUNTAIN VIEW': '348',
            'MOWLEM': '297',
            'MUGUMO-INI': '316',
            'MUHORONI/KORU': '250',
            'MUTUINI': '271',
            'MWIKI': '307',
            'NAIROBI CENTRAL': '340',
            'NAIROBI SOUTH': '341',
            'NAIROBI WEST': '317',
            'NGANDO': '272',
            'NGARA': '342',
            'NGEI': '329',
            'NJIRU': '308',
            'NORTH ALEGO': '351',
            'NORTH GEM': '364',
            'NORTH KABUOCH': '222',
            'NORTH KARACHUONYO': '203',
            'NORTH NYAKACH': '253',
            'NORTH SAKWA': '357',
            'NORTH SEME': '264',
            'NORTH UGENYA': '374',
            'NORTH UYOMA': '369',
            'NORTH WEST KISUMU': '244',
            'NYALENDA \'A\'': '241',
            'NYALENDA B': '234',
            'NYAYO HIGHRISE': '318',
            'OMBEYI': '251',
            'PANGANI': '343',
            'PARKLANDS/HIGHRIDGE': '349',
            'PIPELINE': '295',
            'PUMWANI': '304',
            'RAILWAYS': '235',
            'RIRUTA': '273',
            'ROYSAMBU': '10000', # this should be corrected on dreams app
            'RUAI': '309',
            'RUMA KAKSINGRI EAST': '230',
            'RUSINGA ISLAND': '215',
            'SARANGOMBE': '313',
            'SHAURIMOYO KALOLENI ': '236',
            'SIAYA TOWNSHIP': '352',
            'SIDINDI': '377',
            'SIGOMERE': '378',
            'SOUTH EAST ALEGO': '353',
            'SOUTH EAST NYAKACH': '254',
            'SOUTH GEM': '365',
            'SOUTH KASIPUL': '208',
            'SOUTH SAKWA': '358',
            'SOUTH UYOMA': '370',
            'SOUTH WEST KISUMU': '245',
            'SOUTH WEST NYAKACH': '255',
            'SOUTH-C': '319',
            'UGUNJA': '379',
            'UKWALA': '375',
            'UMOJA I': '298',
            'UMOJA II': '299',
            'UPPER SAVANNAH': '284',
            'USONGA': '354',
            'UTALII': '338',
            'UTAWALA': '285',
            'UTHIRU/RUTHIMITU': '274',
            'VIWANDANI': '323',
            'WAITHAKA': '275',
            'WANGCHIENG': '204',
            'WEST ALEGO': '355',
            'WEST ASEMBO': '371',
            'WEST GEM': '226',
            'WEST GEM': '366',
            'WEST KAMAGAK': '209',
            'WEST KARACHUONYO': '205',
            'WEST KASIPUL': '210',
            'WEST KISUMU': '246',
            'WEST NYAKACH': '256',
            'WEST SAKWA': '359',
            'WEST SEME': '265',
            'WEST UGENYA': '376',
            'WEST UYOMA': '372',
            'WEST YIMBO': '360',
            'WOODLEY/KENYATTA GOLF ': '314',
            'YALA TOWNSHIP': '367',
            'YIMBO EAST': '361',
            'ZIMMERMAN': '333',
            'ZIWANI/KARIOKOR': '344',
        }
    @staticmethod
    def verification_document():
        return {
            'Baptismal card': 4,
            'Birth Certificate': 1,
            'National ID': 2,
            'National ID waiting card': 3,
        }
    @staticmethod
    def excel_demographics():
        return {
            'd.implementing_partner_id': 2,
            # 'IP_Code': 3,
            'd.first_name': 4,
            'd.middle_name': 5,
            'd.last_name': 6,
            'd.date_of_birth': 7,
            'd.verification_document_id': 8,
            # 'verification_doc_other': 9,
            'd.verification_doc_no': 10,
            'd.date_of_enrollment': 11,
            'd.marital_status_id': 14,
            'd.phone_number': 15,
            'd.county_of_residence_id': 16,
            'd.sub_county_id': 17,
            'd.ward_id': 18,
            #'ward_code': 19,
            'd.informal_settlement': 20,
            'd.village': 21,
            'd.land_mark': 22,
            'd.dreams_id': 23,
            'd.dss_id_number': 24,
            #'caregiver_first_name': 25,
            #'caregiver_middle_name': 26,
            #'caregiver_last_name': 27,
            'd.relationship_with_guardian': 28,
            #'caregiver_relationship_other': 29,
            'd.guardian_phone_number': 30,
            'd.guardian_national_id': 31,
        }

