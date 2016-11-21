# Put your commands here
COMMAND1 = "name a bird"
COMMAND2 = "name ten breeds of dogs"

# Your handling code goes in this function
def handle_command(command):
    """
        Determine if the command is valid. If so, take action and return
        a response, if necessary.
    """
    response = ""
    if command.find(COMMAND1) >= 0:
        response = "Owl"
    elif command.find(COMMAND2) >= 0:
        response = "Poodle,Pug,Bulldog,Bloodhound,Foxhound I don't know any more."   
    return response

