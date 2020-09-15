from rest_framework import serializers

from clientes.models import Cliente
from . import validators


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

    def validate(self, data):
        print(data)
        if not validators.cpf_valido(data['cpf']):
            raise serializers.ValidationError({'cpf': "O CPF deve conter 11 dígitos"})
        if not validators.nome_valido(data['nome']):
            raise serializers.ValidationError({'nome': "Não inclua números no nome"})
        if not validators.rg_valido(data['rg']):
            raise serializers.ValidationError({'rg': "O RG deve conter 9 dígitos"})
        if not validators.celular_valido(data['celular']):
            raise serializers.ValidationError({'celular': "O CELULAR deve conter 11 dígitos"})
        return data
