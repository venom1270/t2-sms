# T-2 SMS

This is an unoffical way to send SMS from a T-2 phone number via their control panel 'Horizont'.

On 'Horizon', T-2 offers a nice functionality of sending SMS from any of our T-2 phone numbers via an HTML form.
Unfortunately, public API is not available.

The script creates a series of requests, which mimic manual entering of form values and its submission.
In essence there are two steps:

* Login, to obtain an authenticated session id
* Submit the form for sending messages

Note that the Horizont webpage might change at any time, which could break the script! 

## main.py

Script for testing plain SMS sending.
Parameters you need to change are written like so: *[PARAMETER]*:

* *USERNAME*: T-2 username
* *PASSWORD*: T-2 password
* *SENDER NUMBER*: One of your T-2 numbers, in format "386..."
* *MESSAGE*: Message to send
* *RECIPIENT PHONE NUMBER*: Recipient phone number in format "031...". Can input multiple numbers (in array).

## hassio.py

Script for implementing this functionality as an event driven AppDaemon application.
The app listens for *SEND_SMS* event, which triggers sending of SMS.

Parameters are the same as in *main.py*, with the exception of *MESSAGE* and *RECIPIENT*, which get sent by Home Assistant when event is fired.

To trigger SMS sending, fire an event inside Home Assistant Automation with name: *SEND_SMS*. 
You need to include two parameters in the event:

* *message*: string message to send
* *recipients*: comma separated string of recipient numbers, without spaces 

# Remarks

This is more or less a 'hack' as there is no public API available, so it might stop working at any time if there's significant changes to the 'Horizont' website.
In the meantime, I will be using it until it breaks, as I was not able to find any (free) alternatives for SMS sending API :).


