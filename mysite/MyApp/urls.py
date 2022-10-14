from django.conf import settings
from django.urls import path
from django.conf.urls.static import static

from MyApp import views


urlpatterns = [
    path("", views.HomepageView.as_view(), name="homepage"),
    path("login", views.LoginView.as_view(), name="login"),
    path("logout", views.LogoutView.as_view(), name="logout"),
    path("profile", views.EditProfileView.as_view(), name="profile"),
    path("all_collection", views.AllProductsView.as_view(), name="all_products"),
    path("category/<str:category>", views.CategoryView.as_view(), name="category"),
    path("product/<int:retailer_sku>", views.ProductView.as_view(), name="product"),
    path("cart/<int:retailer_sku>", views.CartView.as_view(), name="cart"),
    path("updated_cart", views.UpdatedCartView.as_view(), name="updated_cart"),
    path("delete_cart_item", views.DeleteCartItemView.as_view(), name="deletecartitem"),
    path("updated_cart_price", views.UpdateCartPriceView.as_view(), name="cartprice"),
    path("update_total", views.UpdateTotalPrice.as_view(), name="updateTotal"),
    path("checkout", views.CheckoutView.as_view(), name="checkout"),
    path("order_confirmation", views.OrderDetails.as_view(), name="order"),
    path("connect", views.ContactUsView.as_view(), name="contact"),
    path("upload_file", views.UploadFileView.as_view(), name="uploadfile"),
    path("password/", views.UpdatePassword.as_view(), name="update_password"),
    path("search", views.SearchView.as_view(), name="search"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
