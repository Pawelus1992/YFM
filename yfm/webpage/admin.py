from django.contrib import admin
from webpage.models import PageSection, Opinion, TimeSlot, Booking

#admin.site.register(PageSection)

@admin.register(PageSection)
class PageSectionAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']

@admin.register(Opinion)
class OpinionAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'creation_date', 'opinion_short_desc']

    def opinion_short_desc(selft, obj):
        return 'asdf ghj'
    
    opinion_short_desc.short_description = 'Krótki opis'

@admin.register(TimeSlot)
class TimeSlotAdmin(admin.ModelAdmin):
    list_display = ['id', 'date', 'time', 'is_booked']

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['id', 'slot', 'name', 'email']