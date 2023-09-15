import json
import urllib

from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI
import urllib.request as url_request
import requests

api = NinjaAPI()
HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36"
}
ALL_CURRENCIES = {
    "AED": "United Arab Emirates Dirham", "AFN": "Afghan Afghani", "ALL": "Albanian Lek", "AMD": "Armenian Dram",
    "ANG": "Netherlands Antillean Guilder", "AOA": "Angolan Kwanza", "ARS": "Argentine Peso",
    "AUD": "Australian Dollar",
    "AWG": "Aruban Florin", "AZN": "Azerbaijani Manat", "BAM": "Bosnia-Herzegovina Convertible Mark",
    "BBD": "Barbadian Dollar", "BDT": "Bangladeshi Taka", "BGN": "Bulgarian Lev", "BHD": "Bahraini Dinar",
    "BIF": "Burundian Franc", "BMD": "Bermudan Dollar", "BND": "Brunei Dollar", "BOB": "Bolivian Boliviano",
    "BRL": "Brazilian Real", "BSD": "Bahamian Dollar", "BTC": "Bitcoin", "BTN": "Bhutanese Ngultrum",
    "BWP": "Botswanan Pula", "BYN": "New Belarusian Ruble", "BYR": "Belarusian Ruble", "BZD": "Belize Dollar",
    "CAD": "Canadian Dollar", "CDF": "Congolese Franc", "CHF": "Swiss Franc", "CLF": "Chilean Unit of Account (UF)",
    "CLP": "Chilean Peso", "CNY": "Chinese Yuan", "COP": "Colombian Peso", "CRC": "Costa Rican Col\u00f3n",
    "CUC": "Cuban Convertible Peso", "CUP": "Cuban Peso", "CVE": "Cape Verdean Escudo", "CZK": "Czech Republic Koruna",
    "DJF": "Djiboutian Franc", "DKK": "Danish Krone", "DOP": "Dominican Peso", "DZD": "Algerian Dinar",
    "EGP": "Egyptian Pound", "ERN": "Eritrean Nakfa", "ETB": "Ethiopian Birr", "EUR": "Euro", "FJD": "Fijian Dollar",
    "FKP": "Falkland Islands Pound", "GBP": "British Pound Sterling", "GEL": "Georgian Lari", "GGP": "Guernsey Pound",
    "GHS": "Ghanaian Cedi", "GIP": "Gibraltar Pound", "GMD": "Gambian Dalasi", "GNF": "Guinean Franc",
    "GTQ": "Guatemalan Quetzal", "GYD": "Guyanaese Dollar", "HKD": "Hong Kong Dollar", "HNL": "Honduran Lempira",
    "HRK": "Croatian Kuna", "HTG": "Haitian Gourde", "HUF": "Hungarian Forint", "IDR": "Indonesian Rupiah",
    "ILS": "Israeli New Sheqel", "IMP": "Manx pound", "INR": "Indian Rupee", "IQD": "Iraqi Dinar",
    "IRR": "Iranian Rial",
    "ISK": "Icelandic Kr\u00f3na", "JEP": "Jersey Pound", "JMD": "Jamaican Dollar", "JOD": "Jordanian Dinar",
    "JPY": "Japanese Yen", "KES": "Kenyan Shilling", "KGS": "Kyrgystani Som", "KHR": "Cambodian Riel",
    "KMF": "Comorian Franc", "KPW": "North Korean Won", "KRW": "South Korean Won", "KWD": "Kuwaiti Dinar",
    "KYD": "Cayman Islands Dollar", "KZT": "Kazakhstani Tenge", "LAK": "Laotian Kip", "LBP": "Lebanese Pound",
    "LKR": "Sri Lankan Rupee", "LRD": "Liberian Dollar", "LSL": "Lesotho Loti", "LTL": "Lithuanian Litas",
    "LVL": "Latvian Lats", "LYD": "Libyan Dinar", "MAD": "Moroccan Dirham", "MDL": "Moldovan Leu",
    "MGA": "Malagasy Ariary", "MKD": "Macedonian Denar", "MMK": "Myanma Kyat", "MNT": "Mongolian Tugrik",
    "MOP": "Macanese Pataca", "MRO": "Mauritanian Ouguiya", "MUR": "Mauritian Rupee", "MVR": "Maldivian Rufiyaa",
    "MWK": "Malawian Kwacha", "MXN": "Mexican Peso", "MYR": "Malaysian Ringgit", "MZN": "Mozambican Metical",
    "NAD": "Namibian Dollar", "NGN": "Nigerian Naira", "NIO": "Nicaraguan C\u00f3rdoba", "NOK": "Norwegian Krone",
    "NPR": "Nepalese Rupee", "NZD": "New Zealand Dollar", "OMR": "Omani Rial", "PAB": "Panamanian Balboa",
    "PEN": "Peruvian Nuevo Sol", "PGK": "Papua New Guinean Kina", "PHP": "Philippine Peso", "PKR": "Pakistani Rupee",
    "PLN": "Polish Zloty", "PYG": "Paraguayan Guarani", "QAR": "Qatari Rial", "RON": "Romanian Leu",
    "RSD": "Serbian Dinar", "RUB": "Russian Ruble", "RWF": "Rwandan Franc", "SAR": "Saudi Riyal",
    "SBD": "Solomon Islands Dollar", "SCR": "Seychellois Rupee", "SDG": "Sudanese Pound", "SEK": "Swedish Krona",
    "SGD": "Singapore Dollar", "SHP": "Saint Helena Pound", "SLE": "Sierra Leonean Leone",
    "SLL": "Sierra Leonean Leone",
    "SOS": "Somali Shilling", "SRD": "Surinamese Dollar", "SSP": "South Sudanese Pound",
    "STD": "S\u00e3o Tom\u00e9 and Pr\u00edncipe Dobra", "SVC": "Salvadoran Col\u00f3n", "SYP": "Syrian Pound",
    "SZL": "Swazi Lilangeni", "THB": "Thai Baht", "TJS": "Tajikistani Somoni", "TMT": "Turkmenistani Manat",
    "TND": "Tunisian Dinar", "TOP": "Tongan Pa\u02bbanga", "TRY": "Turkish Lira", "TTD": "Trinidad and Tobago Dollar",
    "TWD": "New Taiwan Dollar", "TZS": "Tanzanian Shilling", "UAH": "Ukrainian Hryvnia", "UGX": "Ugandan Shilling",
    "USD": "United States Dollar", "UYU": "Uruguayan Peso", "UZS": "Uzbekistan Som",
    "VEF": "Venezuelan Bol\u00edvar Fuerte", "VES": "Sovereign Bolivar", "VND": "Vietnamese Dong",
    "VUV": "Vanuatu Vatu",
    "WST": "Samoan Tala", "XAF": "CFA Franc BEAC", "XAG": "Silver (troy ounce)", "XAU": "Gold (troy ounce)",
    "XCD": "East Caribbean Dollar", "XDR": "Special Drawing Rights", "XOF": "CFA Franc BCEAO", "XPF": "CFP Franc",
    "YER": "Yemeni Rial", "ZAR": "South African Rand", "ZMK": "Zambian Kwacha (pre-2013)", "ZMW": "Zambian Kwacha",
    "ZWL": "Zimbabwean Dollar"}


@api.get("/add")
def add(request, a: int, b: int):
    """
    This is a test API function
    :param request:
    :param a:
    :param b:
    :return: dict of form: "result": a + b}
    """
    return {"result": a + b}


@api.get("/rates")
def rates1(request):
    """
    The function calculate amount of currency at conversion among 160+ currencies
    http string : http://127.0.0.1:8000/api/rates?from=USD&to=RUB&value=4
    :param request:
    :return:  dict of form  {"result": 386.69}
    """
    fr = request.GET.get('from', '')
    to = request.GET.get('to', '')
    value = request.GET.get('value', '')
    global HEADERS
    fr = fr.upper()
    to = to.upper()
    try:
        value = int(value)
    except ValueError:
        return {"error": "Incorrect Amount"}
    if fr not in ALL_CURRENCIES or to not in ALL_CURRENCIES:
        return {"error": "Incorrect Currency"}
    api_url = f'https://api.api-ninjas.com/v1/convertcurrency?want={to}&have={fr}&amount={value}'
    response = requests.get(api_url, headers=HEADERS)
    if response.status_code == requests.codes.ok:
        response_dict = json.loads(response.text)
        # {"new_amount": 0.01, "new_currency": "EUR", "old_currency": "RUB", "old_amount": 1.0}
        return {"result": response_dict["new_amount"]}
    else:
        print("Error:", response.status_code, response.text)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", api.urls),
]
