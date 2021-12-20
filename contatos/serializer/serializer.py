from rest_framework import serializers
from contatos.models import Contato


class ContatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contato
        fields = ['id', 'nome', 'sobrenome', 'email', 'categoria']
