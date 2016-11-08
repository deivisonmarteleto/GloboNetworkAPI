# -*- coding: utf-8 -*-
from django.db.models import get_model

from networkapi.util.serializers import DynamicFieldsModelSerializer


class VrfV3Serializer(DynamicFieldsModelSerializer):

    class Meta:
        Vrf = get_model('api_vrf', 'Vrf')
        depth = 1
        model = Vrf

        fields = (
            'id',
            'internal_name',
            'vrf'
        )

        default_fields = (
            'id',
            'internal_name',

        )

        basic_fields = (
            'id',
            'internal_name',
            'vrf'
        )

        details_fields = fields
