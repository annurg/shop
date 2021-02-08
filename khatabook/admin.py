from django.contrib import admin
from .models import Item, Person, Record
from django.db.models import Sum
from django.utils.html import format_html
# Register your models here.
class ItemInline(admin.TabularInline):
    model = Item
    extra = 0

class RecordInline(admin.TabularInline):
    model = Record

class RecordAdmin(admin.ModelAdmin):
    list_display = ('for_person', 'date', 'amount', 'bill_data',)
    search_fields = ('date', 'user__name')
    list_filter = ('date', 'user__name',)
    list_per_page = 10

    inlines = [ItemInline]
    actions = []

    def for_person(self, obj):
        return obj.user.name

    def bill_data(self, obj):
        items = list(obj.item_set.all())
        return items

    def amount(self, obj):
        s = lambda records: sum([(record.price * record.quantity) for record in records])
        total_bill_amount = s(obj.item_set.all())
        obj.total_amount = total_bill_amount
        obj.save()
        return total_bill_amount

    bill_data.short_description = "bill_data(item_weight, price, quantity)"

    #def has_delete_permission(self, obj):
     #   return False

class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'records', 'total', 'paid', 'due')
    search_fields = ('name', 'phone',)

    #def has_delete_permission(self, obj):
    #   return False

    def due(self, obj):
        s = lambda records: sum([record.total_amount for record in records])
        return s(obj.record_set.all()) - obj.paid

    def total(self, obj):
        s = lambda records: sum([record.total_amount for record in records])
        return s(obj.record_set.all())

    def records(self, obj):
    	return list(obj.record_set.all())

#admin.site.register(Item)
admin.site.register(Record, RecordAdmin)
admin.site.register(Person, PersonAdmin)
