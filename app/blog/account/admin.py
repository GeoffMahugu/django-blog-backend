from django.contrib import admin
# Register your models here.
from .models import Account, UserRegistration, WalletPin


# class CartItemInline(admin.TabularInline):
# 	model = CartItem

# class UserRegistrationAdmin(admin.ModelAdmin):
#     model = UserRegistration
#     # exclude = ['slug']


class UserRegistrationAdmin(admin.ModelAdmin):
    class Meta:
        model = UserRegistration
    # inlines = [
        # 	CartItemInline
        # ]


class AccountAdmin(admin.ModelAdmin):
    model = Account
    exclude = ['slug']

# class AccountAdmin(admin.ModelAdmin):
# 	# inlines = [
# 	# 	CartItemInline
# 	# ]
# 	class Meta:
# 		model = Account


# admin.site.register(Cart, CartAdmin)
# admin.site.register(UserRegistration, UserRegistrationAdmin)
# admin.site.register(AuthToken)
admin.site.register(WalletPin)
admin.site.register(Account, AccountAdmin)
admin.site.register(UserRegistration, UserRegistrationAdmin)
