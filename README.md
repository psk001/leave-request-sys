# Leave Request System

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
 send request to http://127.0.0.1:8000/me
 with the user's access token in the header
  
