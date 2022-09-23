import json

from django.views import View
from django.views.generic.edit import UpdateView
from django.contrib import messages
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.forms.models import model_to_dict
from django.db.models.signals import post_save
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from MyApp.models import Contact, Order, OrderItem, Product
from MyApp.utilis import products_category, product, products
from MyApp.forms import CreateUserForm, EditProfileForm


class SignupView(View):
    def post(self, request):
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "You are registered successfully")

            return redirect('/login')

        return render(request, "signup.html", {'form': form})

    def get(self, request):
        return render(request, "signup.html", {'form': CreateUserForm()})


class LoginView(View):
    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(username=email, password=password)
        if user:
            login(request, user)
            return redirect("/")
        else:
            messages.error(request, 'Invalid credentials.')

            return redirect("login")

    def get(self, request):
        return render(request, "login.html")


class LogoutView(View):
    def get(self, request):
        logout(request)
        return render(request, "index.html")


class HomepageView(View):
    def get(self, request):
        return render(request, "index.html")


class AllProductsView(View):
    def get(self, request):
        all_products = products()
        return render(request, "all_products.html", {'products': all_products})


class CategoryView(View):
    def get(self, request, category):
        products = products_category(category)
        return render(request, "category.html", {'products': products})


class ProductView(View):
    def get(self, request, retailer_sku):
        products = product(retailer_sku)
        return render(request, "product.html", {'products': products})


class CartView(View):
    @method_decorator(login_required(login_url='/login'))
    def get(self, request, retailer_sku):
        cart = request.session.get('cart', {})
        products = Product.objects.get(retailer_sku=retailer_sku)
        json_obj = model_to_dict(products)
        cart[products.retailer_sku] = json_obj
        cart[products.retailer_sku]['quantity'] = 1
        cart[products.retailer_sku]['item_price'] = float(
            cart[products.retailer_sku]['price']) * cart[products.retailer_sku]['quantity']
        request.session['cart'] = cart

        return render(request, "cart.html", {'cart': cart.values()})


class UpdatedCartView(View):
    @method_decorator(login_required(login_url='/login'))
    def get(self, request):
        cart = request.session.get('cart', {})
        return render(request, "cart.html", {"cart": cart.values()})


class DeleteCartItemView(View):
    def get(self, request):
        cart = request.session.get('cart', {})
        cart.pop(request.GET.get('id', None))
        request.session['cart'] = cart

        return render(request, "cart.html", {"cart": cart.values()})


class UpdateCartPriceView(View):
    def get(self, request):
        cart = request.session.get('cart', {})
        cart[request.GET.get('id', None)]['quantity'] = int(request.GET.get('quantity', None))
        cart[request.GET.get('id', None)]['item_price'] = float(cart[request.GET.get(
            'id', None)]['price']) * cart[request.GET.get('id', None)]['quantity']
        request.session['cart'] = cart

        return render(request, "cart.html", {"cart": cart.values()})


class UpdateTotalPrice(View):
    def get(self, request):
        total_price = request.session.get('total_price', {})
        total_price['subtotal'] = request.GET.get('total_price', None)
        total_price['total'] = float(request.GET.get('total_price', None)) + 5
        request.session['total_price'] = total_price
        cart = request.session.get('cart', {})

        return render(request, "cart.html", {"cart": cart.values()})


class CheckoutView(View):
    @method_decorator(login_required(login_url='/login'))
    def get(self, request):
        cart = request.session.get('cart', {})
        total_price = request.session.get('total_price', {})
        return render(request, "checkout.html", {"cart": cart.values(), "total_price": total_price})


class SearchView(View):
    def post(self, request):
        searched = request.POST.get('searched')
        products = Product.objects.filter(name__contains=searched)
        return render(request, "search.html", {'searched': searched, 'products': products})

    def get(self, request):
        return render(request, "search.html")


class ContactUsView(View):
    @method_decorator(login_required(login_url='/login'))
    def post(self, request):
        name = request.POST.get('name')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        complain = request.POST.get('complain')
        contact_us = Contact(name=name, email=email, contact=contact, complain=complain)
        contact_us.save()
        messages.success(request, 'Successfully submitted')

        return redirect('/')

    def get(self, request):
        return render(request, "contact.html")


class UploadFileView(View):
    @method_decorator(login_required(login_url='/login'))
    def post(self, request):
        if request.user.is_superuser:
            request_file = request.FILES['document'] if 'document' in request.FILES else None
            if request_file:
                fs = FileSystemStorage()
                file = fs.save(request_file.name, request_file)
                fileurl = fs.url(file)
            file_path = "/media/results.json"

            with open(file_path, 'r') as products_file:
                products = json.loads(products_file.read())

            for product in products:
                brand = product['brand']
                care = product['care']
                category = product['category']
                currency = product['currency']
                description = product['description']
                images_urls = product['image_urls']
                color = list(images_urls)[0]
                image_urls = list(images_urls.values())[0]
                image = image_urls[0]
                lang = product['lang']
                name = product['name']
                price = product['price']
                retailer_sku = product['retailer_sku']
                skus = product['skus']
                url = product['url']
                trail = product['trail'][0]
                products = Product(brand=brand,
                                   care=care,
                                   category=category,
                                   currency=currency,
                                   description=description,
                                   image=image,
                                   image_urls=image_urls,
                                   color=color,
                                   lang=lang,
                                   name=name,
                                   price=price,
                                   retailer_sku=retailer_sku,
                                   skus=skus,
                                   url=url,
                                   trail=trail)
                products.save()
            messages.success(request, 'Successfully submitted')

            return redirect("/")

    def get(self, request):
        return render(request, "fileupload.html")


class EditProfileView(UpdateView):
    form_class = EditProfileForm
    template_name = 'profile.html'
    success_url = '/'

    def get_object(self):
        return self.request.user


class UpdatePassword(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = '/profile'
    template_name = 'change-password.html'


class OrderDetails(View):
    def post(self, request):
        order = Order()
        order.user = request.user
        order.first_name = request.POST.get('fname')
        order.email = request.POST.get('email')
        order.last_name = request.POST.get('lname')
        order.contact_information = request.POST.get('Contact')
        order.address = request.POST.get('address')
        order.city = request.POST.get('city')
        order.postal_code = request.POST.get('code')
        order.save()
        order_id = Order.objects.filter(first_name=request.POST.get('fname'))
        order_num = order_id.values_list('id', flat=True).last()
        html_body = render_to_string("order_confirmation.html")

        message = EmailMultiAlternatives(
            subject='Thank you for shopping with us!',
            body=html_body,
            from_email='hurmatilyas4105@gmail.com',
            to=['customer4105@gmail.com']
        )
        message.attach_alternative(html_body, "/html")
        message.send(fail_silently=False)

        cart = request.session.get('cart', {})
        context = {"product": cart.values()}
        total_price = request.session.get('total_price', {})

        for item in cart.keys():
            OrderItem.objects.create(
                order=order,
                product=Product.objects.get(retailer_sku=item),
                price=total_price['total']
            )

        request.session['cart'] = {}

        return render(request, "order_confirmation.html", {"order": order_num, "product": context['product'], "price":  total_price, 'order_details': order})


post_save.connect(OrderDetails, sender=Order)
