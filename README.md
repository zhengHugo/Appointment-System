## General Features
Students are able to:
- View/edit my appointments
- Apply for a new appointment
- Change password

Teachers are able to:
- Set office hours
- View/edit my appointments
- Change password

## View/Edit My Appointments in Students Interface
My Appointments:

| Teacher | Date       | Start time | End time | Status    |
| ------- | ---------- | ---------- | -------- | --------- |
| Alice   | 2019-01-01 | 3:00 PM    | 5:00 PM  | Initiated |


Status: initiated, approved, completed, refused, canceled, missed

Operations allowed here:
- Cancel an appointment
- Modify an appointment (re-apply for an appointment)

## Apply for a New Appointment in Students Interface
Operations:
- Search by teacher’s name - use contain-exact matching
- Search by time available - use my available times

Set office hours in teacher’s interface
My office hours:

| Weekday   | Start time | End time |
| --------- | ---------- | -------- |
| Wednesday | 3:00 PM    | 5:00 PM  |

Two options here: Edit entry, new entry

## View/Edit my appointments in teachers’ interface
My Appointments:

| Student | Date       | Start time | End time | Status    |
| ------- | ---------- | ---------- | -------- | --------- |
| Bob     | 2019-01-01 | 3:00 PM    | 5:00 PM  | Initiated |

Status: initiated, approved, completed, refused, canceled, missed

Operations: 
- Approve an appointment
- Cancel an appointment
- Mark a missing appointment
- Go to home page


Change password interface
- Old password:
- New password:
- Repeat new password:
- Go to home page

## Database Design:
### Table "student":

| Field    | Type          | Null | Key | Defaul | Extra |
| -------- | ------------- | ---- | --- | ------ | ----- |
| SID      | int           | NO   | PRI | NULL   |       |
| NAME     | varchar (255) | NO   |     | NULL   |       |
| PASSWORD | varchar (255) | NO   |     | NULL   |       |
    


### Table "teacher":

| Field    | Type          | Null | Key | Defaul | Extra |
| -------- | ------------- | ---- | --- | ------ | ----- |
| TID      | int           | NO   | PRI | NULL   |       |
| NAME     | varchar (255) | NO   |     | NULL   |       |
| PASSWORD | varchar (255) | NO   |     | NULL   |       |
| ADDRESS  | varchar (255) | NO   |     | NULL   |       |

### Table "appointment":

| Field  | Type    | Null | Key | Defaul | Extra          |
| ------ | ------- | ---- | --- | ------ | -------------- |
| ID     | int     | NO   | PRI | NULL   | auto_increment |
| TID    | int     | NO   |     | NULL   |                |
| SID    | int     | NO   |     | NULL   |                |
| STIME  | time    | NO   |     | NULL   |                |
| ETIME  | time    | NO   |     | NULL   |                |
| STATUS | tinyint | NO   |     | NULL   |                |
| DATE   | date    | NO   |     | NULL   |                |

Status code explanation:
- 0 = initiated
- 1 = approved
- 2 = completed
- 3 = refused
- 4 = canceled
- 5 = missed

### Table "teacher_officehour" 

| Field   | Type    | Null | Key | Defaul | Extra          |
| ------- | ------- | ---- | --- | ------ | -------------- |
| ID      | int     | NO   | PRI | NULL   | auto_increment |
| TID     | int     | NO   |     | NULL   |                |
| WEEKDAY | tinyint | NO   |     | NULL   |                |
| STIME   | time    | NO   |     | NULL   |                |
| ETIME   | time    | NO   |     | NULL   |                |
