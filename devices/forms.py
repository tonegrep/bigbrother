from django.forms import Form, IntegerField, CharField

class LightControllerBrightnessForm(Form):
    controller = CharField(label="item_id")
    brightness = CharField(label="brightness_range")