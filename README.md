# Interrupt Details and IRQ Tuning REST API Implemented using Swagger

A prototype Python application for retrieving interrupt details and for tuning irq channels by pinning them to a specific CPU implemented using Swagger.

## Usage

1. install and activate python virtual environment

`sudo pip install virtualenv`

`cd server/`

`virtualenv venv`

`. venv/bin/activate`

2. install required packages

`pip install -r requirements.txt`

3. run server 

`cd server/`

`python flask_app.py`

## Requires

- python 2.x
- virtualenv

## License

The cm_irq library is open-sourced software licensed under the [MIT license](http://opensource.org/licenses/MIT).