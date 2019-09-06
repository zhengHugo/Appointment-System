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
Table "student" (
    sid     	int             student id
    name    	varchar (255)   
    password	varchar (255)
    PRIMARY KEY (SID)
)

Table "teacher" (
    tid     	int		teacher id
    name    	varchar (255)   
    password	varchar (255)
    address	varchar(255)

    PRIMARY KEY (TID)
)

Table "appointment" (
    ID      int         primary key
    TID     int         teacher id
    SID     int         student id
    DATE    date        
    STIME   time        start time
    ETIME   time        end time
    STATUS  tinyint     as explained below
)

Status code explanation:
- 0 = initiated
- 1 = approved
- 2 = completed
- 3 = refused
- 4 = canceled
- 5 = missed

Table "teacher_officehour" (
    id		int 		primary key
    tid		int 		teacher id
    weekday	tinyint		as explained below	
    stime	time		start time	
    etime	time 		end time
)
