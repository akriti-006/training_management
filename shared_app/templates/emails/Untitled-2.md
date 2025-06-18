
- student add journey
    - add
    - email send
    - course enrollment
    - fee add
    - login
        - hr
        - stu
    - access revoke

Query parameter for student enq

add gender and status through backend 



database
    - SQL
        - MySQL
        - PgSQL
        - Oracle
        - SqLite
        - 

Fixture
    - dumpdata
        - DB --->> Json
        - json
    - loaddata
        - Json --->> DB
        - json


all data
app level
model level


python manage.py dumpdata

python manage.py loaddata



all_auth_obj = Author.objects.all()

for obj in all_auth_obj:
    print(obj.name)
    print(obj.book_set.all())



all_book_obj = Books.objects.all().selected_related('author')

for obj in all_book_obj:
    print(obj.name)
    print(obj.author.name)



selecte_related
prefetch_related


email
    - enquiry
    - course start
    - new course assign
    - course unassigned
    - course complete
    - fee submit
    - account block
    - account unblock
