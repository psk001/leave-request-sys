# Leave Request System

to set up the project <br>
step 1: go to home directory ie leave-request-sys-main <br>
step 2: run the command:  pipenv install   -> this will install all dependencies of this project <br>
step 3: run : pipenv shell  <br>
step 4: run : python manage.py runserver   // for linux systems <br>
           &nbsp; &nbsp;  &nbsp; &nbsp;  &nbsp; &nbsp;  &nbsp; &nbsp;  &nbsp; &nbsp;    py manage.py runserver  // for windows systems  <br>

## for any end point that requires authentication
   go to 127.0.0.1:8000/auth/jwt/create
    <br>
  send request in format 
  {
    "username": "",
    "password": ""
  }
  <br>
  this wil return an access_token and a refresh_token
  <br>
  in the request header set:   Authorization = [ JWT ...access token ...]
  <br>
  send request to the desired end point



## to view all users' leave request
Login as admin user   <br>
go to http://127.0.0.1:8000/leaves   <br>


## to apply for a leave
send request to http://127.0.0.1:8000/applyleave  <br>
in format   <br>
  {
    "user": (your_username),   <br>
    "start_date": (date),  <br>
    "end_date" : (date)    <br>
  }   <br>
  
 ## to approve or disapprove a leave 
 send request to http://127.0.0.1:8000/getapproval/<leave-id>   <br>
 in form   <br>
  {"status" : (AP/DA) }     // for AP - approved   DP - disapproved   <br>
  
  
  
## to view a user's all requested leaves
 go to 127.0.0.1:8000/auth/jwt/create   <br>
  send request in format   <br>
  {
    "username": "",   <br>
    "password": ""    <br>
  }   <br>
 with the user's access token in the header in format  Authorization JWT ...access token ...   <br>
 send request to http://127.0.0.1:8000/myleaves
 
  
  
