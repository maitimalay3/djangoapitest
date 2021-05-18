from rest_framework import serializers
from api.tasks import process_wind_test_calculation
from api.models import LongRunningTask


class WindTestSerializer(serializers.Serializer):
    # revenue Input
    InstalledCapacity = serializers.IntegerField(required=True)
    Turbines = serializers.IntegerField(required=True)
    CapacityFactor = serializers.FloatField(required=True)
    Curtailment = serializers.FloatField(required=True)
    PriceInflation = serializers.FloatField(required=True)
    start_year = serializers.IntegerField(required=True)
    years_of_operation = serializers.IntegerField(required=True)
    receivable_period = serializers.IntegerField(required=True)
    ppaprice = serializers.IntegerField(required=True)

    # Cost Input
    setupcost = serializers.IntegerField(required=True)
    baseoperationcost = serializers.IntegerField(required=True)
    CapexCost = serializers.IntegerField(required=True)
    DpsYear = serializers.IntegerField(required=True)
    payble_period = serializers.IntegerField(required=True)

    # Tax Input
    tax_rate = serializers.FloatField(required=True)
    sync = serializers.BooleanField(default=False)

    def create(self, validated_data):
        task_id = self.context['task_id']
        print(task_id)
        revinputdata = {
            'InstalledCapacity': validated_data['InstalledCapacity'],
            'Turbines': validated_data['Turbines'],
            'CapacityFactor': validated_data['CapacityFactor'],
            'PriceInflation': validated_data['PriceInflation'],
            'ppaprice': validated_data['ppaprice'],
            'receivable_period': validated_data['receivable_period']
        }
        contractinfo = {
            'start_year': validated_data['start_year'],
            'years_of_operation': validated_data['years_of_operation']
        }
        costinput = {
            'setupcost': validated_data['setupcost'],
            'baseoperationcost': validated_data['baseoperationcost'],
            'CapexCost': validated_data['CapexCost'],
            'DpsYear': validated_data['DpsYear'],
            'payble_period': validated_data['payble_period']
        }
        sync = validated_data.get('sync', False)
        result = {}
        if sync:
            result = process_wind_test_calculation(
                task_id,
                revinputdata,
                contractinfo,
                costinput,
            )
        else:
            process_wind_test_calculation.delay(
                task_id,
                revinputdata,
                contractinfo,
                costinput,
            )
        return task_id, result


class LongRunningTaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = LongRunningTask
        fields = [
            'id',
            'result'
        ]