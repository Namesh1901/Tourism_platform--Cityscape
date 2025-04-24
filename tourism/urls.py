from django.urls import path
from django.shortcuts import redirect
from .views import RegisterView, LoginView, LogoutView, DashboardView, CityPlacesView, BookingListView, HomeView, PlaceDetailView, HotelDetailView, VenueDetailView, PlaceBookingView, HotelBookingView, VenueBookingView
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('dashboard/', login_required(DashboardView.as_view()), name='dashboard'),
    path('city/<int:city_id>/places/', login_required(CityPlacesView.as_view()), name='city_places'),
    path('place/<int:pk>/', login_required(PlaceDetailView.as_view()), name='place_detail'),
    path('venue/<int:pk>/', login_required(VenueDetailView.as_view()), name='venue_detail'),
    path('hotel/<int:pk>/', login_required(HotelDetailView.as_view()), name='hotel_detail'),
    path('place/<int:pk>/book/', login_required(PlaceBookingView.as_view()), name='place_booking'),
    path('hotel/<int:pk>/book/', login_required(HotelBookingView.as_view()), name='hotel_booking'),
    path('venue/<int:pk>/book/', login_required(VenueBookingView.as_view()), name='venue_booking'),
    path('bookings/', login_required(BookingListView.as_view()), name='booking_list'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)