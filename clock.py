from apscheduler.schedulers.blocking import BlockingScheduler
import stack_overflow_page
import stack_exchange_api
import logging
from sendgrid_helper import send_mail

schedule = BlockingScheduler()

@schedule.scheduled_job('interval', hours=3)
def access_stack_overflow_page():
    try:
        stack_overflow_page.login()
    except:
        message = "Error during login. Access stackoverflow.com to save your login streak"
        logging.error(message)
        send_mail("Login overdue alert!", message)

@schedule.scheduled_job('interval', hours=3)
def access_stack_overflow_api():
    delta_hours = 12

    if stack_exchange_api.have_logged_in(delta_hours) is False:
        message = "You haven't logged in for at least " + str(delta_hours) + " hours! \n " + \
                  "Access stackoverflow.com to save your login streak"
        logging.error(message)
        send_mail("Login overdue alert!", message)

schedule.start()
