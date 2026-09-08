# Mice test task
Task: develop REST API for table reservation in restaurant.

# Requirements 
- Python >= 3.11

# Run from source
```bash
git clone git@github.com:guyrilla/mice_task.git # clone this repo

cd mice_task # open project folder

python -m venv .venv # create virtual environment

source .venv/bin/activate # activate virtual environment

python -m pip install -r "requirements.txt" # install python requirements

uvicorn core.app:entry --reload # start uvicorn server on 127.0.0.1:8000
```

# Usage examples
```bash
# add new reservation
curl -X POST "http://127.0.0.1:8000/bookings" \
             -H "Content-Type: application/json" \
             -d '{
           "name": "Semenov Artem",
           "phone": "89991234567",
           "booking_date": "2026-12-15",
           "booking_time": "20:00:00",
           "number_of_guests": 4
         }'

# get all reservations 
curl -X GET "http://127.0.0.1:8000/bookings" 

# get all reservations filtered by date
curl -X GET "http://127.0.0.1:8000/bookings?date=2026-12-15"

# get reservation with id=1
curl -X GET "http://127.0.0.1:8000/booking/1"

# cancel reservation with id=1
curl -X DELETE "http://127.0.0.1:8000/booking/1"
```
