from django.contrib import admin
from products.models import Product, ProductAttribute, ProductAttributeValue, Category, Review, ManyFacture \
    ,Warranty
# Register your models here.


# inline
class ProductAttributeValueInline(admin.TabularInline):
    model = ProductAttributeValue
    extra = 0
    min_num = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ['deleted_at', 'is_deleted']
    prepopulated_fields = {'en_slug': ('en_title',), 'fa_slug': ('fa_title',)}
    raw_id_fields = ['image', 'category']
    inlines = [ProductAttributeValueInline]
    list_display = ['en_title', 'id', 'category', 'price', 'review_count']


@admin.register(ProductAttribute)
class ProductAttributeAdmin(admin.ModelAdmin):
    pass


@admin.register(ProductAttributeValue)
class ProductAttributeValueAdmin(admin.ModelAdmin):
    list_select_related = ['attribute']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_select_related = ['parent']


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['product', 'user', 'title', 'is_active', 'create_at', 'update_at']
    list_select_related = ['product', 'user']
    list_filter = ['create_at', 'update_at', 'is_active']
    search_fields = ['product__fa_title']
    list_max_show_all = 30


@admin.register(ManyFacture)
class ManyFactureAdmin(admin.ModelAdmin):
    pass


@admin.register(Warranty)
class WarrantyAdmin(admin.ModelAdmin):
    pass
