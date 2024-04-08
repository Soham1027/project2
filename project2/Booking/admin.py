from django.contrib import admin
from django.db.models import Case, Value, When, CharField
from .models import(
    Bookings,
    Reviews,
    PaymentDatas
)
# Register your models here.
class BookingAdmin(admin.ModelAdmin):

    
    list_display = ('user','player_data_ids','player_1','player_2','player_3','coach_data_ids','ground_provider_ids','court_payment','coach_payment','created_at','updated_at','confirm_status') # type: ignore

admin.site.register(Bookings,BookingAdmin)



admin.site.register(PaymentDatas)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'rating', 'review', 'created_at', 'updated_at', 'players_data_id','review_from', 'coach_data_id']

    # def get_queryset(self, request):
    #     queryset = super().get_queryset(request)
    #     # Customize queryset based on the value of coach_to_player field
    #     return queryset.annotate(
    #         review_from=Case(
    #             When(coach_to_player=True, then=Value('Coach')),
    #             When(coach_to_player=False, then=Value('Player')),
    #             output_field=CharField(),
    #         ),
    #         review_to=Case(
    #             When(coach_to_player=True, then=Value('Player')),
    #             When(coach_to_player=False, then=Value('Coach')),
    #             output_field=CharField(),
    #         ),
    #     )

    # def review_from(self, obj):
    #     return obj.review_from

    # def review_to(self, obj):
    #     return obj.review_to

admin.site.register(Reviews, ReviewsAdmin)
