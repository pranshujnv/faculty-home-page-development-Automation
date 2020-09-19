# faculty-home-page-development-Automation
Topic : Intelligent Web Development
Specification:

Framework : Django framework
It is an website model for college faculty.
They register themselves first. After that they can fill theirs
information after filling the information their own page will be rady.
They can fill about themselves, teaching/courses, Publications, Work
and experince, Conatcts, Reseach areas ,etc.
They can also update their informations.
Some urls by entering those urls you can see demo
Note :- this project is for django version less than 2;
if you are usinh django version greater than 2 then replace this line
user = models.ForeignKey(User)
by below line in each models
user = models.ForeignKey(User,on_delete=models.CASCADE)


Go to dirctory IWDproject.
the run the server by typig the command in terminal

python manage.py runserver


After running server just click below link one by one
you and fill the informations and see the demo

● http://127.0.0.1:8000/home/register/

9above link redirect you to profile page then to
fill the information about you and your research projects,qualifications
teaching courses ,your works etc using the appropriate below links


10fill your information about you using the below url after getting logged in
http://127.0.0.1:8000/home/portal/home/

11its will redirect you to profile page where you
will get your own input information with beautifull layout.

12fill the teaching details in teaching form by using below link
http://127.0.0.1:8000/home/portal/teaching/
it will redirect you to profile page then click on teaching button then yu will get your teaching page with input information

13fill informatin of your research projects and other details related to it using below link
http://127.0.0.1:8000/home/portal/project/
it will redirect you to profile page then click on the button named "Research" you will get your research project page with project information

14similarly you can put your publication information using the below link
http://127.0.0.1:8000/home/portal/publication/

it will redirect you to profile page then click on publications you will get publication page

15other similar urls
http://127.0.0.1:8000/home/portal/experience/
http://127.0.0.1:8000/home/portal/qualification/

● http://127.0.0.1:8000/home/login/
● http://127.0.0.1:8000/home/profile/
● http://127.0.0.1:8000/home/portal/home/
9. As you login it direct you those pages where you can fill your
information. As press submit button you will get your ownpage.
