# Django Task

This is a Django task that is given to me by Repliq company.

## Installation

1. Clone the repository: `git clone https://github.com/[ehitimum]/[djangoFirst].git`
2. Install required packages: `pip install -r requirements.txt`
3. Create a new PostgreSQL database: `createdb [devicesystem]`
4. Set up database tables: `python manage.py migrate`
5. Start the development server: `python manage.py runserver`

## Usage

1. Visit `http://localhost:8000` to access the site.
2. Since its only backend project, I build it on the base of JSON request and response.
3. Downlode PostMan Software and send various post request using the links below:
     add_company: http://localhost:8000/myapp/api/companies/                               
     update_company: http://localhost:8000/myapp/api/companies/<int:id>/                    
     get_company_informantion: http://localhost:8000/myapp/api/companies/<int:id>/show/               
    

     add employees: http://localhost:8000/myapp/api/companies/<int:id>/employees/           
     update employee information: http://localhost:8000/myapp/api/companies/<int:id>/employees/<int:emp_id>/
     show employee list: http://localhost:8000/myapp/api/companies/<int:id>/employees/show/
     get employee information: http://localhost:8000/myapp/api/companies/<int:id>/employees/<int:emp_id>/show/


     add devices: http://localhost:8000/myapp/api/companies/<int:id>/devices/
     show devices list: http://localhost:8000/myapp/api/companies/<int:id>/devices/show/
     update device information: http://localhost:8000/myapp/api/companies/<int:id>/devices/show/<int:de_id>/


     add device logs: http://localhost:8000/myapp/api/companies/<int:id>/devices/show/<int:de_id>/devicelogs/
     show device logs: http://localhost:8000/myapp/api/companies/<int:id>/devices/show/<int:de_id>/devicelogs/show/
     update device logs: http://localhost:8000/myapp/api/companies/<int:id>/devices/show/<int:de_id>/devicelogs/show/<int:log_id>/
     
     ### <int:id> = here goes the company id, <int:emp_id> = employee id, <int:de_id> = device id, <int:log_id> = log id

## Requirements

- The application might be used by several companies
- Each company might add all or some of its employees
- Each company and its staff might delegate one or more devices to employees for a certain period of time
- Each company should be able to see when a Device was checked out and returned
- Each device should have a log of what condition it was handed out and returned

## How Its Done

After reading the requirements, I first build a database schema. Below the database schema:

## Credits

- John Doe
- Jane Smith




