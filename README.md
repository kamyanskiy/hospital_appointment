# hospital_appointment on Heroku:
hospital appointment form demo deployed on Heroku  

https://pure-springs-78142.herokuapp.com/appointment_form/

Django admin UI https://pure-springs-78142.herokuapp.com/admin/

# Docker container:
```
$ docker run -d -p 8000:8000 --name website kamyanskiy/hospital
```
http://localhost:8000/appointment_form/
http://localhost:8000/admin/appointment_form/appointment/


### Form looks like: 
![form](./doc/img/form.png)

### Filled form looks like:
![filled_form](./doc/img/filled_form.png)

### Appointment was created successful:
![thanks](./doc/img/thanks.png)

### Appointment time was busy - sorry, we show free/busy time for that date:
![sorry](./doc/img/sorry.png)

### Admin site, Appoinments list: 
![report](./doc/img/report.png)
