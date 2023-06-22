from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from .models import EvenOdd,ReverseNum,PrimeNum,Userdata,QuestionKey,HomeTime,LoginTime,TestTime,FinishTime
from .models import UserHiddenData,HiddenEvenOdd,HiddenPrimeNum,HiddenReverseNum,PostiveNum,HiddenPositiveNum,MagicNum,HiddenMagicNum,CapitalizeVowels,HiddenCapitalizeVowels,UnitNum,HiddenUnitNum,Tensdigit,HiddenTensdigit,Palindrome,HiddenPalindrome,Armstrong,HiddenArmstrong

class CustomUserAdmin(UserAdmin):
    """Define admin model for custom User model with no username field."""
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)

class UserDataAdmin(admin.ModelAdmin):
    list_display=['input_part','output_part']

class EvenOddAdmin(admin.ModelAdmin):
    list_display=['tnum','input','output']

class ReverseNumAdmin(admin.ModelAdmin):
    list_display=['tnum','input','output']

class PrimeNumAdmin(admin.ModelAdmin):
    list_display=['tnum','input','output']

class PostiveNumAdmin(admin.ModelAdmin):
    list_display=['tnum','input','output']

class MagicNumAdmin(admin.ModelAdmin):
    list_display=['tnum','input','output']

class CapitalizeVowelsAdmin(admin.ModelAdmin):
    list_display=['tnum','input','output']

class UnitNumAdmin(admin.ModelAdmin):
    list_display=['tnum','input','output']

class TensdigitAdmin(admin.ModelAdmin):
    list_display=['tnum','input','output']

class PalindromeAdmin(admin.ModelAdmin):
    list_display=['tnum','input','output']

class ArmstrongAdmin(admin.ModelAdmin):
    list_display=['tnum','input','output']



class KeyAdmin(admin.ModelAdmin):
    list_display=['key']

class  HomeTimeAdmin(admin.ModelAdmin):
    list_display=['home']

class  LoginTimeAdmin(admin.ModelAdmin):
    list_display=['login']

class  TestTimeAdmin(admin.ModelAdmin):
    list_display=['test']

class  FinishTimeAdmin(admin.ModelAdmin):
    list_display=['finish']

class HiddenEvenOddAdmin(admin.ModelAdmin):
    list_display=['tnum','input','output']

class HiddenReverseNumAdmin(admin.ModelAdmin):
    list_display=['tnum','input','output']

class HiddenPrimeNumAdmin(admin.ModelAdmin):
    list_display=['tnum','input','output']

class HiddenPositiveNumAdmin(admin.ModelAdmin):
    list_display=['tnum','input','output']

class HiddenMagicNumAdmin(admin.ModelAdmin):
    list_display=['tnum','input','output']

class HiddenCapitalizeVowelsAdmin(admin.ModelAdmin):
    list_display=['tnum','input','output']

class HiddenUnitNumAdmin(admin.ModelAdmin):
    list_display=['tnum','input','output']

class HiddenTensdigitAdmin(admin.ModelAdmin):
    list_display=['tnum','input','output']

class HiddenPalindromeAdmin(admin.ModelAdmin):
    list_display=['tnum','input','output']

class HiddenArmstrongAdmin(admin.ModelAdmin):
    list_display=['tnum','input','output']

class UserHiddenDataAdmin(admin.ModelAdmin):
    list_display=['tnum','input','output']

admin.site.register(Userdata,UserDataAdmin)
admin.site.register(EvenOdd,EvenOddAdmin)
admin.site.register(ReverseNum,ReverseNumAdmin)
admin.site.register(PrimeNum,PrimeNumAdmin)
admin.site.register(PostiveNum,PostiveNumAdmin)
admin.site.register(MagicNum,MagicNumAdmin)
admin.site.register(CapitalizeVowels,CapitalizeVowelsAdmin)
admin.site.register(UnitNum,UnitNumAdmin)
admin.site.register(Tensdigit,TensdigitAdmin)
admin.site.register(Palindrome,PalindromeAdmin)
admin.site.register(Armstrong,ArmstrongAdmin)


admin.site.register(QuestionKey,KeyAdmin)
admin.site.register(HomeTime,HomeTimeAdmin)
admin.site.register(LoginTime,LoginTimeAdmin)
admin.site.register(TestTime,TestTimeAdmin)
admin.site.register(FinishTime,FinishTimeAdmin)
admin.site.register(UserHiddenData,UserHiddenDataAdmin)
admin.site.register(HiddenEvenOdd,HiddenEvenOddAdmin)
admin.site.register(HiddenReverseNum,HiddenReverseNumAdmin)
admin.site.register(HiddenPrimeNum,HiddenPrimeNumAdmin)
admin.site.register(HiddenMagicNum,HiddenMagicNumAdmin)
admin.site.register(HiddenPositiveNum,HiddenPositiveNumAdmin)
admin.site.register(HiddenCapitalizeVowels,HiddenCapitalizeVowelsAdmin)
admin.site.register(HiddenUnitNum,HiddenUnitNumAdmin)
admin.site.register(HiddenTensdigit,HiddenTensdigitAdmin)
admin.site.register(HiddenPalindrome,HiddenPalindromeAdmin)
admin.site.register(HiddenArmstrong,HiddenArmstrongAdmin)

admin.site.register(get_user_model(), CustomUserAdmin)
