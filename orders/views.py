from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from django.core.serializers.json import DjangoJSONEncoder
from .forms import CreateOrder
from .models import Order, DataOrder
from datetime import datetime
from random import Random
from client import RestClient
from django.conf import settings
import json


def new_order(request):
    if request.method == "POST":
        form = CreateOrder(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            client = RestClient(settings.API_LOGIN, API_PASS)
            post_data = dict()
            post.lang = 'en'
            post_data[len(post_data)] = dict(
                language_code="en",
                location_code=post.location.code,
                keyword=post.keyword,
                pingback_url=settings.API_PING,
            )
            response = client.post(f"/v3/serp/{post.engine.name}/organic/task_post", post_data)
            if response["status_code"] == 20000:
                post.id_api = response['tasks'][0]['id']
            else:
                print("error. Code: %d Message: %s" % (response["status_code"], response["status_message"]))
            post.user = request.user
            post.start = datetime.now()
            post.save()
            return redirect(f'/orders/{post.id}')
    else:
        form = CreateOrder()
        return render(request, 'orders/new_order.html', {'form': form})


def my_order(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'orders/my.html', {'orders': orders})


def order(request, order_id):
    orders = Order.objects.get(id=order_id)
    if orders:
        if orders.status is False:
            status = "Task in Progress"
        else:
            status = "Task Done"
        return render(request, 'orders/order.html', {'order': orders, 'status': status})


@csrf_exempt
def post_back(request, order_id):
    orders = Order.objects.get(id_api=order_id)
    if orders.status is False:
        client = RestClient(settings.API_LOGIN, API_PASS)
        response = client.get(f"/v3/serp/{orders.engine.name}/organic/task_get/regular/{order_id}")
        if response['status_code'] == 20000:
            res = response['tasks'][0]['result'][0]['items']
            for obj in res:
                data = DataOrder()
                setattr(data, 'order', orders)
                for k, v in obj.items():
                    setattr(data, k, v)
                data.save()
            orders.status = True
            orders.save()
        else:
            print("error. Code: %d Message: %s" % (response["status_code"], response["status_message"]))
    return HttpResponse('ok')


def get_data_order(request, order_id):
    orders = Order.objects.get(id=order_id)
    object_data = DataOrder.objects.filter(order=orders).values('order', 'type', 'rank_group', 'rank_absolute', 'domain', 'title', 'description', 'url', 'breadcrumb')
    if object_data:
        data = json.dumps(list(object_data), cls=DjangoJSONEncoder)
        return JsonResponse(data, safe=False)
    else:
        return HttpResponse(None)
