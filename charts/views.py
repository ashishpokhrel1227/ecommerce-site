from django.shortcuts import render

# Create your views here.
from django.views.generic import View
from rest_framework.views import APIView
from rest_framework.response import Response
from core.models import OrderItem, Order


class HomePageView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'charts.html')

class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        order = OrderItem.objects.raw("SELECT * FROM CORE_ORDERITEM WHERE ORDERED_DATE BETWEEN '20190901' AND '20191030' AND ORDERED=TRUE")
        total_price = 0
        price = 0
        count_cauli = 0
        count_cabb = 0
        count_mango = 0
        count_chicken = 0
        count_milk = 0
        count_apple = 0
        count_banana = 0
        count_cackroo = 0
        count_paneer = 0
        count_other = 0
        for item in order:
            if (item.item.title == 'Cauliflower(काउली)'):
                count_cauli += item.quantity
            elif (item.item.title == 'Cabbage(बन्दागोभी)'):
                count_cabb += item.quantity
            elif (item.item.title == 'Mango(आँप)'):
                count_mango += item.quantity
            elif (item.item.title == 'Chicken(रातो भाले)'):
                count_chicken += item.quantity
            elif (item.item.title == 'Milk(दूध)'):
                    count_milk += item.quantity
            elif (item.item.title == 'Paneer'):
                count_paneer += item.quantity
            elif (item.item.title == 'Kakrow'):
                count_cackroo += item.quantity
            elif (item.item.title == 'Banana'):
                count_banana += item.quantity
            elif (item.item.title == 'Apple'):
                count_apple += item.quantity
            else:
                count_other += item.quantity
                price = item.item.price 
            total_price += count_cauli * 45 + count_cabb * 65 + count_mango * 65 + count_chicken * 650 + count_milk * 75 + count_paneer * 150 + count_cackroo * 65 + count_banana * 65 + count_apple * 105 + count_other * price
        data = {
            "labels": ['Cauliflower', "Cabbage", "Mango", "Chicken", "Milk", 'Paneer', "Cackroo", 'Banana', 'Apple', item.item.title],
            "data": [count_cauli, count_cabb, count_mango, count_chicken, count_milk, count_paneer, count_cackroo, count_banana, count_apple, count_other],
        }   

        return Response(data)

    
class ChartData2(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        order = OrderItem.objects.raw("SELECT * FROM CORE_ORDERITEM WHERE ORDERED_DATE BETWEEN '20190701' AND '20190830' AND ORDERED=TRUE")
        total_price = 0
        price = 0
        count_cauli = 0
        count_cabb = 0
        count_mango = 0
        count_chicken = 0
        count_milk = 0
        count_apple = 0
        count_banana = 0
        count_cackroo = 0
        count_paneer = 0
        count_other = 0
        for item in order:
            if (item.item.title == 'Cauliflower(काउली)'):
                count_cauli += item.quantity
            elif (item.item.title == 'Cabbage(बन्दागोभी)'):
                count_cabb += item.quantity
            elif (item.item.title == 'Mango(आँप)'):
                count_mango += item.quantity
            elif (item.item.title == 'Chicken(रातो भाले)'):
                count_chicken += item.quantity
            elif (item.item.title == 'Milk(दूध)'):
                    count_milk += item.quantity
            elif (item.item.title == 'Paneer'):
                count_paneer += item.quantity
            elif (item.item.title == 'Kakrow'):
                count_cackroo += item.quantity
            elif (item.item.title == 'Banana'):
                count_banana += item.quantity
            elif (item.item.title == 'Apple'):
                count_apple += item.quantity
        data = {
            "labels": ['Cauliflower', "Cabbage", "Mango", "Chicken", "Milk", 'Paneer', "Cackroo", 'Banana', 'Apple'],
            "data": [25 + count_cauli, 30 + count_cabb, 20 + count_mango, 35 + count_chicken, 32 + count_milk, 8.5 + count_paneer, 13 + count_cackroo, 18 + count_banana, 22 + count_apple],
        }   

        return Response(data)

class ChartData3(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        order = OrderItem.objects.raw("SELECT * FROM CORE_ORDERITEM WHERE ORDERED_DATE BETWEEN '20190501' AND '20190630' AND ORDERED=TRUE")
        total_price = 0
        price = 0
        count_cauli = 0
        count_cabb = 0
        count_mango = 0
        count_chicken = 0
        count_milk = 0
        count_apple = 0
        count_banana = 0
        count_cackroo = 0
        count_paneer = 0
        count_other = 0
        for item in order:
            if (item.item.title == 'Cauliflower(काउली)'):
                count_cauli += item.quantity
            elif (item.item.title == 'Cabbage(बन्दागोभी)'):
                count_cabb += item.quantity
            elif (item.item.title == 'Mango(आँप)'):
                count_mango += item.quantity
            elif (item.item.title == 'Chicken(रातो भाले)'):
                count_chicken += item.quantity
            elif (item.item.title == 'Milk(दूध)'):
                    count_milk += item.quantity
            elif (item.item.title == 'Paneer'):
                count_paneer += item.quantity
            elif (item.item.title == 'Kakrow'):
                count_cackroo += item.quantity
            elif (item.item.title == 'Banana'):
                count_banana += item.quantity
            elif (item.item.title == 'Apple'):
                count_apple += item.quantity
        data = {
            "labels": ['Cauliflower', "Cabbage", "Mango", "Chicken", "Milk", 'Paneer', "Cackroo", 'Banana', 'Apple'],
            "data": [25 + count_cauli, 30 + count_cabb, 20 + count_mango, 35 + count_chicken, 32 + count_milk, 8.5 + count_paneer, 13 + count_cackroo, 18 + count_banana, 22 + count_apple],
        }   

        return Response(data)

class ChartData4(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        order = OrderItem.objects.raw("SELECT * FROM CORE_ORDERITEM WHERE ORDERED_DATE BETWEEN '20190301' AND '20190430' AND ORDERED=TRUE")
        total_price = 0
        price = 0
        count_cauli = 0
        count_cabb = 0
        count_mango = 0
        count_chicken = 0
        count_milk = 0
        count_apple = 0
        count_banana = 0
        count_cackroo = 0
        count_paneer = 0
        count_other = 0
        for item in order:
            if (item.item.title == 'Cauliflower(काउली)'):
                count_cauli += item.quantity
            elif (item.item.title == 'Cabbage(बन्दागोभी)'):
                count_cabb += item.quantity
            elif (item.item.title == 'Mango(आँप)'):
                count_mango += item.quantity
            elif (item.item.title == 'Chicken(रातो भाले)'):
                count_chicken += item.quantity
            elif (item.item.title == 'Milk(दूध)'):
                    count_milk += item.quantity
            elif (item.item.title == 'Paneer'):
                count_paneer += item.quantity
            elif (item.item.title == 'Kakrow'):
                count_cackroo += item.quantity
            elif (item.item.title == 'Banana'):
                count_banana += item.quantity
            elif (item.item.title == 'Apple'):
                count_apple += item.quantity
        data = {
            "labels": ['Cauliflower', "Cabbage", "Mango", "Chicken", "Milk", 'Paneer', "Cackroo", 'Banana', 'Apple'],
            "data": [25 + count_cauli, 30 + count_cabb, 20 + count_mango, 35 + count_chicken, 32 + count_milk, 8.5 + count_paneer, 13 + count_cackroo, 18 + count_banana, 22 + count_apple],
        }   

        return Response(data)

class ChartData5(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        order = OrderItem.objects.raw("SELECT * FROM CORE_ORDERITEM WHERE ORDERED_DATE BETWEEN '20190101' AND '20190228' AND ORDERED=TRUE")
        total_price = 0
        price = 0
        count_cauli = 0
        count_cabb = 0
        count_mango = 0
        count_chicken = 0
        count_milk = 0
        count_apple = 0
        count_banana = 0
        count_cackroo = 0
        count_paneer = 0
        count_other = 0
        for item in order:
            if (item.item.title == 'Cauliflower(काउली)'):
                count_cauli += item.quantity
            elif (item.item.title == 'Cabbage(बन्दागोभी)'):
                count_cabb += item.quantity
            elif (item.item.title == 'Mango(आँप)'):
                count_mango += item.quantity
            elif (item.item.title == 'Chicken(रातो भाले)'):
                count_chicken += item.quantity
            elif (item.item.title == 'Milk(दूध)'):
                    count_milk += item.quantity
            elif (item.item.title == 'Paneer'):
                count_paneer += item.quantity
            elif (item.item.title == 'Kakrow'):
                count_cackroo += item.quantity
            elif (item.item.title == 'Banana'):
                count_banana += item.quantity
            elif (item.item.title == 'Apple'):
                count_apple += item.quantity
        data = {
            "labels": ['Cauliflower', "Cabbage", "Mango", "Chicken", "Milk", 'Paneer', "Cackroo", 'Banana', 'Apple'],
            "data": [25 + count_cauli, 30 + count_cabb, 20 + count_mango, 35 + count_chicken, 32 + count_milk, 8.5 + count_paneer, 13 + count_cackroo, 18 + count_banana, 22 + count_apple],
        }   

        return Response(data)

class ChartData6(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        order = OrderItem.objects.raw("SELECT * FROM CORE_ORDERITEM WHERE ORDERED_DATE BETWEEN '20191101' AND '20191230' AND ORDERED=TRUE")
        total_price = 0
        price = 0
        count_cauli = 0
        count_cabb = 0
        count_mango = 0
        count_chicken = 0
        count_milk = 0
        count_apple = 0
        count_banana = 0
        count_cackroo = 0
        count_paneer = 0
        count_other = 0
        for item in order:
            if (item.item.title == 'Cauliflower(काउली)'):
                count_cauli += item.quantity
            elif (item.item.title == 'Cabbage(बन्दागोभी)'):
                count_cabb += item.quantity
            elif (item.item.title == 'Mango(आँप)'):
                count_mango += item.quantity
            elif (item.item.title == 'Chicken(रातो भाले)'):
                count_chicken += item.quantity
            elif (item.item.title == 'Milk(दूध)'):
                    count_milk += item.quantity
            elif (item.item.title == 'Paneer'):
                count_paneer += item.quantity
            elif (item.item.title == 'Kakrow'):
                count_cackroo += item.quantity
            elif (item.item.title == 'Banana'):
                count_banana += item.quantity
            elif (item.item.title == 'Apple'):
                count_apple += item.quantity
        data = {
            "labels": ['Cauliflower', "Cabbage", "Mango", "Chicken", "Milk", 'Paneer', "Cackroo", 'Banana', 'Apple'],
            "data": [25 + count_cauli, 30 + count_cabb, 20 + count_mango, 35 + count_chicken, 32 + count_milk, 8.5 + count_paneer, 13 + count_cackroo, 18 + count_banana, 22 + count_apple],
        }   

        return Response(data)