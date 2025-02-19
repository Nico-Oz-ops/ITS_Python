# Match statement and OR
# http status (match statement version)

http_status = 200

match http_status:
    case 200|201:
        print("Success")
    case 400:
        print("Bad Request")
    case 404:
        print("Not Found")
    case 500|501:
        print("Server Error")
    case _:
        print("Unknown status code")
# In this example, the match statement is used to match the value of the variable http_status.
# The match statement is followed by a series of case statements, each of which specifies a possible value of http_status.
# The case statement can also contain multiple values separated by the | operator.

