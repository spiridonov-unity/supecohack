from django.contrib.auth.models import User, Group
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render
from django.template.loader import get_template
from django.views import generic

from shop.forms import OrderModelForm
from shop.models import Product, Section, Order


def index(request):
    sections = Section.objects.all().order_by('title')
    products = Product.objects.all()[:4]
    context = {'sections': sections, 'products': products}
    return render(
        request,
        'index.html',
        context=context
    )


class ProductDetailView(generic.DetailView):
    model = Product


def order(request):
    form = OrderModelForm()
    context = {'form': form}
    return render(
        request,
        'order.html',
        context=context
    )


def add_user(name, email):
    if User.objects.filter(email=email).exists() or User.objects.filter(username=email).exists():
        return
    password = User.objects.make_random_password()
    user = User.objects.create_user(email, email, password)
    user.first_name = name
    group = Group.objects.get(name='Клиенты')
    user.groups.add(group)
    user.save

    text = get_template('registration/registration_email.html')
    html = get_template('registration/registration_email.html')

    context = {'username': email, 'password': password}

    subject = 'Регистрация'
    from_email = 'from@supeco.ru'
    text_content = text.render(context)
    html_content = html.render(context)
    msg = EmailMultiAlternatives(subject, text_content, from_email, [email])
    msg.attach_alternative(html_content, 'text/html')
    msg.send()


def orders(request):
    user_orders = Order.objects.filter(email__exact=request.user.email)
    return render(
        request,
        'orders.html',
        context={'orders': user_orders}
    )


def investoram(request):
    sections = Section.objects.all().order_by('title')
    return render(
        request,
        'investoram.html',
        context={'investoram': investoram}
    )


def enterpriser(request):
    sections = Section.objects.all().order_by('title')
    return render(
        request,
        'enterpriser.html',
        context={'enterpriser': enterpriser}
    )