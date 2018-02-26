from rest_framework import serializers

from Devices.models import Device, DeviceAssingment, DeviceType


class DeviceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceType
        fields = "__all__"
        read_only_field = "id"


class DeviceAssingmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceAssingment
        exclude = ("device",)
        read_only_field = "id"


class DeviceSerializer(serializers.ModelSerializer):
    assigned = DeviceAssingmentSerializer(required=False)

    class Meta:
        model = Device
        fields = "__all__"
        read_only_field = 'id'

    def to_representation(self, obj):
        response = super(DeviceSerializer, self).to_representation(obj)
        response['type'] = obj.type.name
        if response['assigned']:
            if response['assigned']['assign_to']:
                response['assigned']['assign_to'] = \
                    obj.assigned.assign_to.first_name \
                    + " "+obj.assigned.assign_to.last_name
            if response['assigned']['possess_by']:
                response['assigned']['possess_by'] = \
                    obj.assigned.assign_to.first_name \
                    + " "+obj.assigned.assign_to.last_name
            if response['assigned']['possess_place']:
                response['assigned']['possess_place'] = \
                    obj.assigned.possess_place.place
        if response['whose_name']:
            response['whose_name'] = obj.whose_name.first_name \
                + " " + obj.whose_name.last_name

        return response

    def update(self, instance, validated_data):
        assigned_data = validated_data.pop('assigned')
        super(DeviceSerializer, self).update(instance, validated_data)
        try:
            device_assigned = instance.assigned
        except DeviceAssingment.DoesNotExist:
            device_assigned = DeviceAssingment.objects.create(device=instance,
                                                              **assigned_data)
        else:
            DeviceAssingmentSerializer().update(device_assigned, assigned_data)

        return instance
