from django.shortcuts import render
from django.views import generic
from django.views.generic import TemplateView
import requests
import json
import datetime
#python_bitbankccのパッケージをインポート
import python_bitbankcc

class IndexTemplateView(TemplateView):
    template_name = 'index.html'
    coinList = []

    def coinView(parameter_list):
        URL = 'https://coincheck.com/api/ticker'
        coincheck = requests.get(URL).json()
        for key, item in coincheck.items():
            data = ("%-9s : %-10.9s " % (key, item))
            coinList.append(data)

    # coins = {'BTC': 'btc_jpy', 'ETH': 'eth_jpy',
    #         'XEM': 'xem_jpy', 'BCH': 'bch_jpy'}

    # URL = 'https://coincheck.com/api/rate/'

    # for key, item in coins.items():
    #     coincheck = requests.get(URL+item).json()
    #     print("%-4s : %-10s" % (key, coincheck['rate']))
    #     pass


def coinfunc(request):
    URL = 'https://coincheck.com/api/ticker'
    coincheck = requests.get(URL).json()
    coinList = []


    #coincheck
    for key, item in coincheck.items():
        data = ("%-9s : %-10.9s " % (key, item))
        coinList.append(data)

    #zaif
    URL = 'https://api.zaif.jp/api/1/ticker/btc_jpy'
    zaif = requests.get(URL).json()
    zaifList = []
    #coincheck
    for key, item in zaif.items():
        data = ("%-9s : %-10.9s " % (key, item))
        zaifList.append(data)

    #context
    context = {
    'coinList': coinList,
    'zaif': zaifList,
    }


    #return
    return render(request, 'index.html', context)


