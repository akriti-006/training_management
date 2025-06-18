from datetime import datetime

def my_context_processor(request):

    current_year = datetime.now().year

    return({"current_year":current_year})
