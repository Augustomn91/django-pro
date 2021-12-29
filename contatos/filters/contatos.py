# import django_filters as filters
#
# from contas.models import ContaModel
#
#
# class ContasFilter(filters.FilterSet):
#     NR_INTERNO_CONTA = filters.CharFilter(lookup_expr="icontains")
#     conta = filters.CharFilter(lookup_expr="icontains", field_name="NR_INTERNO_CONTA")
#     conta2 = filters.CharFilter(method="filter_conta2")
#
#     class Meta:
#         model = ContaModel
#         fields = ('NR_INTERNO_CONTA', 'NR_ATENDIMENTO', 'DS_ESTABELECIMENTO', 'DS_CONVENIO', 'conta2')
#
#     @staticmethod
#     def filter_conta2(queryset, name, value):
#         return queryset.filter(NR_INTERNO_CONTA__icontains=value)
