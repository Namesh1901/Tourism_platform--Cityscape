from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import ListView, DetailView
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import City, TourismPlace, Venue, Hotel, Booking
from .forms import BookingForm
from django.views.generic import ListView

class HomeView(View):
    def get(self, request):
        return render(request, 'tourism/home.html')

class RegisterView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'tourism/register.html', {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
        return render(request, 'tourism/register.html', {'form': form})

class LoginView(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'tourism/login.html', {'form': form})

    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
        return render(request, 'tourism/login.html', {'form': form})

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')

class DashboardView(LoginRequiredMixin, View):
    def get(self, request):
        cities = City.objects.all()
        bookings = Booking.objects.filter(user=request.user).order_by('-created_at')
        return render(request, 'tourism/dashboard.html', {'cities': cities, 'bookings': bookings})

class CityPlacesView(LoginRequiredMixin, ListView):
    model = TourismPlace
    template_name = 'tourism/city_places.html'
    context_object_name = 'places'

    def get_queryset(self):
        city_id = self.kwargs.get('city_id')
        queryset = TourismPlace.objects.filter(city_id=city_id)

        # Filters for places
        place_name = self.request.GET.get('place_name')
        if place_name:
            queryset = queryset.filter(name__icontains=place_name)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        city = get_object_or_404(City, id=self.kwargs.get('city_id'))

        # Hotels queryset with filters
        hotels = Hotel.objects.filter(city_id=city.id)
        hotel_name = self.request.GET.get('hotel_name')
        min_price = self.request.GET.get('min_price')
        max_price = self.request.GET.get('max_price')
        if hotel_name:
            hotels = hotels.filter(name__icontains=hotel_name)
        if min_price:
            hotels = hotels.filter(price_per_night__gte=min_price)
        if max_price:
            hotels = hotels.filter(price_per_night__lte=max_price)

        # Venues queryset with filters
        venues = Venue.objects.filter(city_id=city.id)
        venue_name = self.request.GET.get('venue_name')
        min_price_venue = self.request.GET.get('min_price_venue')
        max_price_venue = self.request.GET.get('max_price_venue')
        if venue_name:
            venues = venues.filter(name__icontains=venue_name)
        if min_price_venue:
            venues = venues.filter(price_per_day__gte=min_price_venue)
        if max_price_venue:
            venues = venues.filter(price_per_day__lte=max_price_venue)

        context['city'] = city
        context['hotels'] = hotels
        context['venues'] = venues
        return context

class PlaceBookingView(LoginRequiredMixin, View):
    def get(self, request, pk):
        place = get_object_or_404(TourismPlace, pk=pk)
        form = BookingForm(initial={'place': place})
        return render(request, 'tourism/place_booking_form.html', {'form': form, 'place': place})

    def post(self, request, pk):
        place = get_object_or_404(TourismPlace, pk=pk)
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.place = place
            booking.save()
            return redirect('dashboard')
        return render(request, 'tourism/place_booking_form.html', {'form': form, 'place': place})

class HotelBookingView(LoginRequiredMixin, View):
    def get(self, request, pk):
        hotel = get_object_or_404(Hotel, pk=pk)
        form = BookingForm(initial={'hotel': hotel})
        return render(request, 'tourism/hotel_booking_form.html', {'form': form, 'hotel': hotel})

    def post(self, request, pk):
        hotel = get_object_or_404(Hotel, pk=pk)
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.hotel = hotel
            booking.save()
            return redirect('dashboard')
        return render(request, 'tourism/hotel_booking_form.html', {'form': form, 'hotel': hotel})

class VenueBookingView(LoginRequiredMixin, View):
    def get(self, request, pk):
        venue = get_object_or_404(Venue, pk=pk)
        form = BookingForm(initial={'venue': venue})
        return render(request, 'tourism/venue_booking_form.html', {'form': form, 'venue': venue})

    def post(self, request, pk):
        venue = get_object_or_404(Venue, pk=pk)
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.venue = venue
            booking.save()
            return redirect('dashboard')
        return render(request, 'tourism/venue_booking_form.html', {'form': form, 'venue': venue})

class PlaceDetailView(LoginRequiredMixin, View):
    def get(self, request, pk):
        place = get_object_or_404(TourismPlace, pk=pk)
        return render(request, 'tourism/place_detail.html', {'place': place})

class HotelDetailView(LoginRequiredMixin, View):
    def get(self, request, pk):
        hotel = get_object_or_404(Hotel, pk=pk)
        return render(request, 'tourism/hotel_detail.html', {'hotel': hotel})

class VenueDetailView(LoginRequiredMixin, View):
    def get(self, request, pk):
        venue = get_object_or_404(Venue, pk=pk)
        return render(request, 'tourism/venue_detail.html', {'venue': venue})

class BookingListView(LoginRequiredMixin, ListView):
    model = Booking
    template_name = 'tourism/booking_list.html'
    context_object_name = 'bookings'

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user).order_by('-created_at')
