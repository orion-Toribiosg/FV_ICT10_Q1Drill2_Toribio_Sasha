from js import document
from pyscript import display 

def generate_message(event): #used "def" again the same way used in Drill 1 for easier use and to bind the variables together 
    boxname1 = document.getElementById("input1").value
    boxage2 = document.getElementById("input2").value
    boxschool3 = document.getElementById("input3").value

    message = (
    f"⭐ YOUR STUDENT PROFILE: ⭐\n\n"
    f"Name: {boxname1}\n\n"
    f"Age: {boxage2}\n\n"
    f"School: {boxschool3}\n\n"
    f"""📚 NOTES: 📚
    {boxname1} is currently {boxage2}, wow! 
    Studying at {boxschool3} 🏫, they undoubtedly will do their best in coding this school year. 💯"""
    ) 
    #used parenthesis to make the info for student profile a string variable and so that they would all appear together 
    #used "f" before each one so that I could insert the variables needed that makes the info change when input values change too !! 
    #multiline string for NOTES was used

    replacedmessage = message.replace("\n", "<br/>") 
    #whenever i tried to make the \n work and get the other student profile info to be on another line, 
    #\n would keep reappearing as part of the text, so I used the .replace we learned in class to replace \n with a <br> since it's easier to fix
    document.getElementById("output1").innerHTML = replacedmessage 
    #kept trying to use display, but it didn't work with the replacedmessage variable
    #so instead, I used my knowledge from last sy about the document.getElementById and directly input(??) it into the output1 div so that
    #when the button was clicked, the replacedmessage variable would directly go to the div 