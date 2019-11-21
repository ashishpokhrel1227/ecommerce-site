from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, View
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.utils import timezone
from .forms import CheckoutForm
from .models import Item, OrderItem, Order, CheckOut
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

class report(View):
    def get(self, *args, **kwargs):
        order = OrderItem.objects.all()
        count_for_cabbage = 0
        for item in order:
            if (item.item.title == 'Cabbage(बन्दागोभी)'):
                count_for_cabbage += 1
                print(count_for_cabbage)
        context = {
            'order': order,
            'count1': count_for_cabbage,
        }
        return render(self.request, 'report.html', context)
class HomeView(ListView):
    model = Item
    paginate_by = 20
    template_name = 'home.html'

class OrderedItem(LoginRequiredMixin, View):
    def get(self, *args, ** kwargs):
        try:
            order = OrderItem.objects.filter(user=self.request.user, ordered=True, delievered=False)
            delievered = OrderItem.objects.filter(user=self.request.user, ordered=True, delievered=True)
            context = {
                'order': order,
                'delievered': delievered
            }
            return render(self.request, 'ordered_items.html', context)
        except ObjectDoesNotExist:
            messages.success(self.request, 'You havn\'t ordered anything')
            return redirect('/')



class OrderSummaryView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            context = {
                'object': order,
            }
            return render(self.request, 'order_summary.html', context)
        except ObjectDoesNotExist:
            messages.success(self.request, 'You don\'t have an active order')
            return redirect('/')   

class CheckoutView(View):
    def get(self, *args, **kwargs):
        order = Order.objects.get(user=self.request.user, ordered=False)
        form = CheckoutForm()
        context = {
            'form': form,
            'order': order
        }
        return render(self.request, 'checkout.html', context)

    def post(self, *args, **kwargs):
        form = CheckoutForm(self.request.POST or None)
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            if form.is_valid():
                address = form.cleaned_data.get('address')
                phonenumber = form.cleaned_data['phonenumber']
                paymentoption = form.cleaned_data['paymentoption'] 
                deliveryoption = form.cleaned_data['deliveryoption']
                billingadd = CheckOut(
                    user = self.request.user,
                    address = address,
                    phonenumber = phonenumber,
                    paymentoption = paymentoption,
                    deliveryoption = deliveryoption,
                )
                billingadd.save()
                order.billingadd = billingadd
                order_items = order.items.all()
                order_items.update(ordered=True, 
                deliveryoption=deliveryoption)
                for item in order_items:
                    item.save()
                order.ordered = True
                order.save()
                messages.success(self.request, 'Your order was successful')
                return redirect('/')
            else:
                if len(form.errors) == 2 :
                    messages.warning(self.request, 'Failed checkout due to invalid time setup and invalid phone number.')
                else:
                    messages.warning(self.request, 'Failed checkout due to invalid phone number or invalid timesetup.')
                return redirect('core:checkout')
        except ObjectDoesNotExist:
            messages.error(self.request, 'You don\'t have an active order')
            return redirect('core:order-summary')

        

class ItemDetailView(DetailView):
    model = Item
    template_name = 'product.html'

@login_required
def add_to_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_item, created = OrderItem.objects.get_or_create(
        item=item,
        user=request.user,
        ordered=False
        )
    print('I am fucked up: ', order_item.item.price)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__slug=item.slug).exists():
            
            order_item.quantity += 1
            order_item.save()
            messages.info(request, 'This item quantity was updated.')
            return redirect('core:order-summary')
        else:
            order.items.add(order_item)
            messages.info(request, 'This item was added to your cart.')
            return redirect('core:order-summary')
    else:
        ordered_date = timezone.now()
        # order_item = OrderItem.objects.update(ordered_date=ordered_date)
        order = Order.objects.create(user=request.user, ordered_date=ordered_date)
        order.items.add(order_item)
        messages.info(request, 'This item was added to your cart.')
        return redirect('core:order-summary')

@login_required
def add_single_item_to_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_item, created = OrderItem.objects.get_or_create(
        item=item,
        user=request.user,
        ordered=False
        )
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__slug=item.slug).exists():
            print(order.items)
            order_item.quantity += 0.5
            order_item.save()
            messages.info(request, 'This item quantity was updated.')
            return redirect('core:order-summary')
        else:
            order.items.add(order_item)
            messages.info(request, 'This item was added to your cart.')
            return redirect('core:order-summary')
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(user=request.user, ordered_date=ordered_date)
        order.items.add(order_item)
        messages.info(request, 'This item was added to your cart.')
        return redirect('core:order-summary')

@login_required
def remove_from_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(
            item=item,
            user=request.user,
            ordered=False
            )[0]
            order.items.remove(order_item)
            messages.info(request, 'This item was removed from your cart.')
            return redirect('core:order-summary')
        else:
            messages.info(request, 'This item was not in your cart.')
            return redirect('core:product', slug=slug)
    else:
        messages.info(request, 'You don\'t have an active ordered.')
        return redirect('core:product', slug=slug)


@login_required
def remove_single_item_from_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(
            item=item,
            user=request.user,
            ordered=False
            )[0]
            if order_item.quantity > 1:
                order_item.quantity -= 0.5
                order_item.save()
            else:
                order.items.remove(order_item)
            messages.info(request, 'This item quantity was updated.')
            return redirect('core:order-summary')
        else:
            messages.info(request, 'This item was not in your cart.')
            return redirect('core:product', slug=slug)
    else:
        messages.info(request, 'You don\'t have an active ordered.')
        return redirect('core:product', slug=slug)

