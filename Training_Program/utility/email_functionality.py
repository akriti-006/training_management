from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings


def send_welcome_email(training_enquiry_obj, password, start_date, end_date):
    print('\n\n\n')
    print("inside send_welcome_email")
    print("training_enquiry_obj : ", training_enquiry_obj)

    subject = 'Welcome to Our AVIOX!'

    first_name = training_enquiry_obj.first_name
    last_name = training_enquiry_obj.last_name
    course_name = training_enquiry_obj.course.name
    to_email = training_enquiry_obj.email
    from_email = settings.EMAIL_HOST_USER
    login_link = settings.PLATFORM_LOGIN_LINK

    context = {
        'first_name': first_name,
        'last_name': last_name,
        'to_email': from_email,
        'course_name': course_name,
        'from_email': to_email,
        'login_link': login_link,
        'password': password,
        'start_date': start_date,
        'end_date': end_date,
    }
    print('context : ', context)

    html_content = render_to_string('emails/welcome_email.html', context)

    text_content = 'Welcome to our platform!'  # fallback for non-HTML email clients

    email = EmailMultiAlternatives(subject, text_content, from_email, [to_email])
    email.attach_alternative(html_content, "text/html")
    email.send()

    print("DONE")



def send_enquiry_email(training_enquiry_obj):
    print('\n\n\n')
    print("inside Enquiry_email")
    print("training_enquiry_obj : ", training_enquiry_obj)

    subject = 'Welcome to Our AVIOX!'

    first_name = training_enquiry_obj.first_name
    last_name = training_enquiry_obj.last_name
    course_name = training_enquiry_obj.course.name
    to_email = training_enquiry_obj.email
    from_email = settings.EMAIL_HOST_USER

    context = {
        'first_name': first_name,
        'last_name': last_name,
        'to_email': from_email,
        'course_name': course_name,
        'from_email': to_email,
    }
    print('context : ', context)

    html_content = render_to_string('emails/Enquiry_email.html', context)

    text_content = 'Welcome to our platform!'  # fallback for non-HTML email clients

    email = EmailMultiAlternatives(subject, text_content, from_email, [to_email])
    email.attach_alternative(html_content, "text/html")
    email.send()

    print("DONE")
    
def send_course_assign(training_enquiry_obj, start_date, end_date):
    print('\n\n\n')
    print("inside New Assigned Course Email")
    print("training_enquiry_obj : ", training_enquiry_obj)

    subject = 'Welcome to Our AVIOX!'

    first_name = training_enquiry_obj.first_name
    last_name = training_enquiry_obj.last_name
    course_name = training_enquiry_obj.course.name
    to_email = training_enquiry_obj.email
    from_email = settings.EMAIL_HOST_USER
    login_link = settings.PLATFORM_LOGIN_LINK

    context = {
        'first_name': first_name,
        'last_name': last_name,
        'to_email': from_email,
        'course_name': course_name,
        'start_date' : start_date,
        'end_date': end_date,
        'from_email': to_email,
    }
    print('context : ', context)

    html_content = render_to_string('emails/new_assigned_course.html', context)

    text_content = 'Welcome to our platform!'  # fallback for non-HTML email clients

    email = EmailMultiAlternatives(subject, text_content, from_email, [to_email])
    email.attach_alternative(html_content, "text/html")
    email.send()
    

