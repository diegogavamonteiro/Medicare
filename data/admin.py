from django.contrib import admin

from .models import *

class CustomerAdmin(admin.ModelAdmin):

    list_display = ['full_name','id', 'created', 'modified']
    search_fields = ['full_name']
    list_filter = ['created','modified']

class SupplierAdmin(admin.ModelAdmin):

    list_display = ['full_name', 'id','created', 'modified']
    search_fields = ['full_name']
    list_filter = ['created','modified']

class DonationAdmin(admin.ModelAdmin):
    list_display = ['id','date','created', 'modified']
    search_fields = ['id']
    list_filter = ['created','modified']

class Donation_ItensAdmin(admin.ModelAdmin):
    list_display = ['id','id_donation','id_supplier','get_name_supplier','id_apresentation', 'get_name_apresentation','get_size','get_unit','pills','created', 'modified']
    search_fields = ['get_name_supplier','id','id_donation','get_name_apresentation']
    list_filter = ['created','modified']

    def get_name_supplier(self,obj):
        return obj.id_supplier.full_name

    def get_name_apresentation(self,obj):
        return obj.id_apresentation.id_medicine.remedio

    def get_size(self,obj):
        return obj.id_apresentation.size

    def get_unit(self,obj):
        return obj.id_apresentation.size_unit

    get_name_supplier.admin_order_field = 'id_supplier'
    get_name_supplier.short_description = 'Fornecedor'

    get_name_apresentation.admin_order_field = 'id_apresentation'
    get_name_apresentation.short_description = 'Medicamento'

    get_size.admin_order_field = 'id_apresentation'
    get_size.short_description = 'Tamanho'

    get_unit.admin_order_field = 'id_apresentation'
    get_unit.short_description = 'Unidade'

class ReservationAdmin(admin.ModelAdmin):
    list_display = ['id','prescription','date','created', 'modified']
    search_fields = ['id']
    list_filter = ['created','modified']


class Reservation_ItensAdmin(admin.ModelAdmin):

    list_display = ['id','id_reservation','id_doctor','get_name_doctor','id_customer','get_name_customer','id_apresentation','get_name_apresentation','get_size','get_unit','pills','created', 'modified']
    search_fields = ['id']
    list_filter = ['created','modified']

    def get_name_doctor(self,obj):
        return obj.id_doctor.full_name

    def get_name_customer(self,obj):
        return obj.id_customer.full_name

    def get_name_apresentation(self,obj):
        return obj.id_apresentation.id_medicine.remedio

    def get_size(self,obj):
        return obj.id_apresentation.size

    def get_unit(self,obj):
        return obj.id_apresentation.size_unit

    get_name_doctor.admin_order_field = 'id_doctor'
    get_name_doctor.short_description = 'Médico'

    get_name_customer.admin_order_field = 'id_customer'
    get_name_customer.short_description = 'Cliente'

    get_name_apresentation.admin_order_field = 'id_apresentation'
    get_name_apresentation.short_description = 'Medicamento'

    get_size.admin_order_field = 'id_apresentation'
    get_size.short_description = 'Tamanho'

    get_unit.admin_order_field = 'id_apresentation'
    get_unit.short_description = 'Unidade'

class MedicineAdmin(admin.ModelAdmin):
    list_display = ['remedio','id','active_principle','tarja', 'created', 'modified']
    search_fields = ['id_medicine','id','get_name_doctor','get_name_customer','get_name_apresentation']
    list_filter = ['created','modified']

class Medicine_ApresentationAdmin(admin.ModelAdmin):
    list_display = ['id','get_name_remedio','id_medicine','ggrem','size','size_unit','laboratory','complement', 'created', 'modified']
    search_fields = ['get_name_remedio']
    list_filter = ['created','modified']

    def get_name_remedio(self,obj):
        return obj.id_medicine.remedio

    get_name_remedio.admin_order_field = 'id_medicine'
    get_name_remedio.short_description = 'Medicamento'

class DoctorAdmin(admin.ModelAdmin):
    list_display = ['full_name','id','crm','state']
    search_fields = ['full_name']
    list_filter = ['created','modified']

class StockAdmin(admin.ModelAdmin):
    list_display = ['id','id_reservation_itens','id_donation_itens','stock_quantity','minimun_quantity']
    search_fields = ['id']
    list_filter = ['created','modified']

class Stock_ItensAdmin(admin.ModelAdmin):
    list_display = ['id','get_name_customer','get_name_remedio_customer','get_size_customer',
    'get_unit_customer','get_pills_customer','get_name_supplier','get_name_remedio_fornecedor',
    'get_size_supplier','get_unit_supllier','get_pills_supplier','id_stock','manufacture_date','due_date']
    search_fields = ['get_name_remedio','id']
    list_filter = ['created','modified']

    def get_name_customer(self,obj):
        return obj.id_stock.id_reservation_itens.id_customer.full_name

    def get_name_remedio_customer(self,obj):
        return obj.id_stock.id_reservation_itens.id_apresentation.id_medicine.remedio

    def get_name_supplier(self,obj):
        return obj.id_stock.id_donation_itens.id_supplier.full_name

    def get_name_remedio_fornecedor(self,obj):
        return obj.id_stock.id_donation_itens.id_apresentation.id_medicine.remedio

    def get_size_customer(self,obj):
        return obj.id_stock.id_reservation_itens.id_apresentation.size

    def get_pills_customer(self,obj):
        return obj.id_stock.id_reservation_itens.pills

    def get_unit_customer(self,obj):
        return obj.id_stock.id_reservation_itens.id_apresentation.size_unit

    def get_size_supplier(self,obj):
        return obj.id_stock.id_donation_itens.id_apresentation.size

    def get_unit_supllier(self,obj):
        return obj.id_stock.id_donation_itens.id_apresentation.size_unit

    def get_pills_supplier(self,obj):
        return obj.id_stock.id_donation_itens.pills

    get_name_remedio_fornecedor.admin_order_field = 'id_stock'
    get_name_remedio_fornecedor.short_description = 'Medicamento Fornecedor'

    get_name_remedio_customer.admin_order_field = 'id_stock'
    get_name_remedio_customer.short_description = 'Medicamento Cliente'

    get_name_supplier.admin_order_field = 'id_stock'
    get_name_supplier.short_description = 'Fornecedor'

    get_name_customer.admin_order_field = 'id_stock'
    get_name_customer.short_description = 'Cliente'

    get_size_customer.admin_order_field = 'id_stock'
    get_size_customer.short_description = 'Tamanho'

    get_unit_customer.admin_order_field = 'id_stock'
    get_unit_customer.short_description = 'Unidade'

    get_size_supplier.admin_order_field = 'id_stock'
    get_size_supplier.short_description = 'Tamanho'

    get_unit_supllier.admin_order_field = 'id_stock'
    get_unit_supllier.short_description = 'Unidade'

    get_pills_customer.admin_order_field = 'id_stock'
    get_pills_customer.short_description = 'Quantidade'

    get_pills_supplier.admin_order_field = 'id_stock'
    get_pills_supplier.short_description = 'Quantidade'

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Supplier, SupplierAdmin)

admin.site.register(Reservation, ReservationAdmin)
admin.site.register(Reservation_Itens, Reservation_ItensAdmin)

admin.site.register(Donation,DonationAdmin)
admin.site.register(Donation_Itens, Donation_ItensAdmin)


admin.site.register(Medicine, MedicineAdmin)
admin.site.register(Medicine_Apresentation, Medicine_ApresentationAdmin)

admin.site.register(Doctor, DoctorAdmin)

admin.site.register(Stock,StockAdmin)
admin.site.register(Stock_Itens,Stock_ItensAdmin)
