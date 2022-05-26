# Leave Request System

to set up the project
step 1: go to home directory ie leave-request-sys-main 
step 2: run the command:  pipenv install   -> this will install all dependencies of this project
step 3: run : pipenv shell 
step 4: run : python manage.py runserver   // for linux systems
              py manage.py runserver  // for windows systems



## to view all users' leave request
Login as admin user
go to http://127.0.0.1:8000/leaves


## to apply for a leave
send request to http://127.0.0.1:8000/applyleave
in format 
  {
    "user": (your_username),
    "start_date": (date),
    "end_date" : (date)
  }
  
 ## to approve or disapprove a leave 
 send request to http://127.0.0.1:8000/getapproval/<leave-id>
 in form 
  {"status" : (AP/DA) }     // for AP - approved   DP - disapproved
  
  
  
## to view a user's all requested leaves
 go to 127.0.0.1:8000/auth/jwt/create
  send request in format 
  {
    "username": "",
    "password": ""
  }
 with the user's access token in the header in format  Authorization JWT ...access token ...
 send request to http://127.0.0.1:8000/myleaves
 
  
  ## for any end point that requires authentication
   go to 127.0.0.1:8000/auth/jwt/create
  send request in format 
  {
    "username": "",
    "password": ""
  }
 with the user's access token in the header in format  Authorization JWT ...access token ...
