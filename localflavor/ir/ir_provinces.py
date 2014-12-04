# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _

#: A tuple representing Iranian provinces (as per ISO3166:2-IR).
IR_PROVINCES = (
    ('01', _('East Azarbaijan')),
    ('02', _('West Azarbaijan')),
    ('03', _('Ardabil')),
    ('04', _('Isfahan')),
    ('05', _('Ilam')),
    ('06', _('Bushehr')),
    ('07', _('Tehran')),
    ('08', _('Chahar Mahaal and Bakhtiari')),
    ('10', _('Khuzestan')),
    ('11', _('Zanjan')),
    ('12', _('Semnan')),
    ('13', _('Sistan and Baluchestan')),
    ('14', _('Fars')),
    ('15', _('Kerman')),
    ('16', _('Kordestan')),
    ('17', _('Kermanshah')),
    ('18', _('Kohgiluyeh and Boyer-Ahmad')),
    ('19', _('Gilan')),
    ('20', _('Lorestan')),
    ('21', _('Mazandaran')),
    ('22', _('Markazi')),
    ('23', _('Hormozgan')),
    ('24', _('Hamadan')),
    ('25', _('Yazd')),
    ('26', _('Qom')),
    ('27', _('Golestan')),
    ('28', _('Qazvin')),
    ('29', _('South Khorasan')),
    ('30', _('Razavi Khorasan')),
    ('31', _('North Khorasan')),
    ('32', _('Alborz')), # Formed in 2010, still not in ISO3166:2
)

PROVINCE_CHOICES = sorted(IR_PROVINCES, key=lambda x: x[1])
