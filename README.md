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
Table "Student" (
    SID     int             NOT NULL
    NAME    varchar (255)   NOT NULL
    PRIMARY KEY (SID)
)

Table "Teacher" (
    TID     int             NOT NULL
    NAME    varchar (255)   NOT NULL
    PRIMARY KEY (TID)
)

Table "Appointment" (
    ID      int         NOT NULL
    TID     int         NOT NULL
    SID     int         NOT NULL
    DATE    date        NOT NULL
    STIME   time        NOT NULL
    ETIME   time        NOT NULL
    STATUS  tinyint     NOT NULL
)
Status code explanation:
- 0 = initiated
- 1 = approved
- 2 = completed
- 3 = refused
- 4 = canceled
- 5 = missed
