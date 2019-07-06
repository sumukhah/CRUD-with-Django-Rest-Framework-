How to run this?

 <Open the terminal/shell and insert>

                    > git clone https://github.com/sumukhah/Featured-Blog.git

 <move to that directory(Featured-Blog)>

 <You can create virtual environment but its optional>

                                > pip install -r requirements.txt

                                > python3 manage.py makemigrations

                                > python3 manage.py migrate

                                > python3 manage.py runserver

 <Then open browser and go to 'http://127.0.0.1:8000/' >

  " http://127.0.0.1:8000/ " is the root of project. Then you can navigate to 
                        "http://127.0.0.1:8000/authentication/"
                        or 
                        "http://127.0.0.1:8000/news"


  Better if you go to "http://127.0.0.1:8000/authentication/register"
  After register navigate " http://127.0.0.1:8000/authentication/login "

  Then you are an Authenticated User

 visit "http://127.0.0.1:8000/newslist"

 If you want to know more about post & its comments go to "http://127.0.0.1:8000/newsdetail/<pk>" 
               ^where <pk> is any id of the post(try giving 1,2,3,4,)

  you can view related comments to that post by navigating to http://127.0.0.1:8000/newsdetail/<pk>/comments
                ^where <pk> is any id of the post(try giving 1,2,3,4,)