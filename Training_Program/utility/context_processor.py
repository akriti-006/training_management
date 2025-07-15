from datetime import datetime

def my_context_processor(request):

    current_year = datetime.now().year

    return({"current_year":current_year})


def current_user_group_check(request):
    data = {}
    if request.user.is_authenticated:
        data = {
            'is_admin': False,
            'is_hr': False,
            'is_student': False,
            'is_teacher': False,
        }
        if request.user.groups.filter(name='Admin').exists():
            data['is_admin'] = 'True'

        if request.user.groups.filter(name='HR').exists():
            data['is_hr'] = 'True'

        if request.user.groups.filter(name='Student').exists():
            data['is_student'] = 'True'
        
        if request.user.groups.filter(name='Teacher').exists():
            data['is_teacher'] = 'True'
        
    return data
