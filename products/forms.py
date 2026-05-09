from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category, Review


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = "__all__"

    image = forms.ImageField(
        label="Image", required=False, widget=CustomClearableFileInput
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields["category"].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "border-black rounded-0"


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ['rating', 'title', 'body']
        widgets = {
            'rating': forms.RadioSelect(),
            'title': forms.TextInput(attrs={
                'class': 'form-control border-black rounded-0',
                'placeholder': 'Give your review a title',
            }),
            'body': forms.Textarea(attrs={
                'class': 'form-control border-black rounded-0',
                'rows': 4,
                'placeholder': 'Share your thoughts about this product...',
            }),
        }
