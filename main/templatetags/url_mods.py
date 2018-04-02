from django import template
import requests

register = template.Library()


@register.filter(name='spacetodash')
def spacetodash(value):
    return value.replace(' ', '-')


@register.filter(name='dashtospace')
def dashtospace(value):
    return value.replace('-', ' ')


@register.filter(name='multiply')
def multiply(value, arg):
    return float(value) * float(arg)


@register.simple_tag
def currency_converter(value, code):
    if code == "KWD":
        r = requests.get('http://free.currencyconverterapi.com/api/v5/convert?q=' + 'AED_' + code + '&compact=ultra')
        json = r.json()
        rate = json['AED_' + code]
        converted = float(rate) * float(value)
        return float("{0:.2f}".format(converted))
    elif code == 'OMR':
        r = requests.get('http://free.currencyconverterapi.com/api/v5/convert?q=' + 'AED_' + code + '&compact=ultra')
        json = r.json()
        rate = json['AED_' + code]
        converted = float(rate) * float(value)
        return float("{0:.2f}".format(converted))
    elif code == 'BHD':
        r = requests.get('http://free.currencyconverterapi.com/api/v5/convert?q=' + 'AED_' + code + '&compact=ultra')
        json = r.json()
        rate = json['AED_' + code]
        converted = float(rate) * float(value)
        return float("{0:.2f}".format(converted))
    elif code == 'AED':
        tax = float(value) * (5 / 100)
        final = float(value + tax)
        return float("{0:.2f}".format(final))
    elif code == 'JOD':
        r = requests.get('http://free.currencyconverterapi.com/api/v5/convert?q=' + 'AED_' + code + '&compact=ultra')
        json = r.json()
        rate = json['AED_' + code]
        converted = float(rate) * float(value)
        price_with_tax = float(converted + (converted * (16 / 100)))
        return float("{0:.2f}".format(price_with_tax))
    elif code == 'SAR':
        r = requests.get('http://free.currencyconverterapi.com/api/v5/convert?q=' + 'AED_' + code + '&compact=ultra')
        json = r.json()
        rate = json['AED_' + code]
        converted = float(rate) * float(value)
        price_with_tax = float(converted + (converted * (5 / 100)))
        return float("{0:.2f}".format(price_with_tax))
    elif code == 'QAR':
        r = requests.get('http://free.currencyconverterapi.com/api/v5/convert?q=' + 'AED_' + code + '&compact=ultra')
        json = r.json()
        result = json['AED_' + code]
        final = float(result * value)
        return float("{0:.2f}".format(final))
    elif code == 'LBP':
        r = requests.get('http://free.currencyconverterapi.com/api/v5/convert?q=' + 'AED_' + code + '&compact=ultra')
        json = r.json()
        rate = json['AED_' + code]
        converted = float(rate) * float(value)
        price_with_tax = float(converted + (converted * (11 / 100)))
        return float("{0:.2f}".format(price_with_tax))
