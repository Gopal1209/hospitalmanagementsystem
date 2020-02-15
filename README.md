# hospitalmanagementsystem
This is the Django project I created for my Sophomore Year project Submission

## Dependencies
1. Django version - 2.1.5
2. PostgreSQL vesion - 11
3. psycopg2
4. Pillow

## Running the project
After installing all the dependencies

Step 1: Create a database and update Setting.py according to your Database

Step 2: Migrate the Models to databse using command

        python manage.py migrate
        
Step 3: Create a superuser using the command

       python manage.py createsuperuser
       
Step 4: Run the development server using the command
       
       python manage.py runserver 

## Further Steps Required
<pre>We have the following Users for the project:

1. Patient
2. Doctor
3. Mediocre (Someone who takes your Blood Pressure and Temperature reading before you see the doctor)
4. Medicos / Pharmacy / Chemist
5. Laboratory

The registeration page by default registers all the users as Patients,
To use the project, we have to update the values from the admin panel

Step 1: Register on the registeration page as normal Patient
Step 2: Sign in to the admin panel and change the value of the field role in table Profiles as:
       "doctor" for doctor
       "lab" for Laboratory
       "medic" for Medicos / Pharmacy / Chemist
       "mediocre" for mediocre


Also, in tha table Current
create a new Row with every value as 1

The project will be up and running after this

</pre>
