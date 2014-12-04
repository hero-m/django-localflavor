from django.utils.translation import ugettext_lazy as _
from django.db.models.fields import CharField

from .ir_provinces import PROVINCE_CHOICES


class IRProvinceField(CharField):
    """
    A model field that forms represent as a ``forms.IRProvinceField`` field and
    stores the ISO3166:2-IR code for that province in the database.
    """
    description = _("Iranian province (ISO3166:2-IR code)")

    def __init__(self, *args, **kwargs):
        kwargs['choices'] = PROVINCE_CHOICES
        kwargs['max_length'] = 2
        super(IRProvinceField, self).__init__(*args, **kwargs)
