from twilio.rest import Client
from config import ACCOUNT_SID, AUTH_TOKEN, TWILIO_NUMBER


def validates_choice(user_choice):
    """Returns bool of user's choice"""

    if user_choice.lower() == ("y" or "yes"):
        return True
    else:
        return False


def gets_to_number():
    """Ask user for phone number, returns it with +1 added"""

    user_number = raw_input("What's yo numba? ")

    user_number.strip("-")
    return user_number
    user_number.strip("(")
    return user_number
    user_number.strip(")")
    return user_number
    user_number.strip("\n")
    return user_number

    if len(user_number) == 10 and user_number.isdigit() == True:
        user_number = "+1" + user_number
        return user_number
    else:
        print "Not valid entry. Enter an 8 digit numba!"
        gets_to_number()


def gets_message_to_send():
    """Ask user for message to send"""

    user_msg = raw_input("What is your message? ")

    return user_msg


def send_message(to_number, to_message, ACCOUNT_SID,
                            AUTH_TOKEN, TWILIO_NUMBER):
    """Using Twilio, sends sms message"""

    client = Client(ACCOUNT_SID, AUTH_TOKEN)

    message = client.messages.create(
                    to=to_number,
                    from_=TWILIO_NUMBER,
                    body=to_message)

    print "Message set. Message Id: {}".format(message.sid)


def main(ACCOUNT_SID, AUTH_TOKEN, TWILIO_NUMBER):

    print "Welcome to this Twilio API Demo"

    user_choice = raw_input("""Would you like to send a next message? """)

    validated_user_choice = validates_choice(user_choice)

    while validated_user_choice:

        print validated_user_choice
        to_number = gets_to_number()
        to_message = gets_message_to_send()

        send_message(to_number, to_message, ACCOUNT_SID,
                            AUTH_TOKEN, TWILIO_NUMBER)

        user_choice = raw_input("""Would you like to send another next message? """)

        validated_user_choice = validates_choice(user_choice)


if __name__ == '__main__':
    main(ACCOUNT_SID, AUTH_TOKEN, TWILIO_NUMBER)
