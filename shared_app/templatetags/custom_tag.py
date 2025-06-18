from django import template

register = template.Library()


@register.filter
def sum_values(queryset, field_name):
    # total = 0
    # for i in queryset:
    #     total = total+i.amount_paid

    total = sum(getattr(item, field_name, 0) for item in queryset)
    return total


@register.filter(is_safe=True)
def pending_amount(total, qs):
    paid = 0
    for i in qs:
        paid = paid+i.amount_paid
    
    print(f"{total=}")
    print(f"{paid=}")

    return total -paid
    