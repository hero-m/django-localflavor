"""
Iran-specific Form helpers
"""

from __future__ import absolute_import, unicode_literals

from django.forms.fields import Select


class IRProvinceSelect(Select):
    """
    A Select widget that uses a list of Iranian Provinces as its choices.
    """
    def __init__(self, attrs=None):
        from .ir_provinces import PROVINCE_CHOICES
        super(IRProvinceSelect, self).__init__(attrs, choices=PROVINCE_CHOICES)
