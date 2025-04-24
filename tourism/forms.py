from django import forms
from .models import Booking, Venue, Hotel, TourismPlace

class BookingForm(forms.ModelForm):
    extra_amenities = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows': 3}))

    class Meta:
        model = Booking
        fields = ['place', 'venue', 'hotel', 'start_date', 'end_date', 'number_of_persons', 'time_of_visit', 'extra_amenities']
        widgets = {
            'number_of_persons': forms.NumberInput(attrs={'min': 1, 'step': 1}),
            'start_date': forms.DateInput(format='%d/%m/%Y', attrs={'type': 'date'}),
            'end_date': forms.DateInput(format='%d/%m/%Y', attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['place'].queryset = TourismPlace.objects.all()
        self.fields['venue'].queryset = Venue.objects.all()
        self.fields['hotel'].queryset = Hotel.objects.all()
        self.fields['start_date'].widget.attrs.update({'type': 'date'})
        self.fields['end_date'].widget.attrs.update({'type': 'date'})
        self.fields['time_of_visit'].widget.attrs.update({'type': 'time'})
