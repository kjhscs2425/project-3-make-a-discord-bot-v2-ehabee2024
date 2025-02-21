"""
**Do NOT change the name of this function.**

This function will be called every time anyone says anything on a channel where the bot lives.

* It returns `True` if the bot notices something it wants to repond to.
* You can have certain words or patterns in the messages trigger the bot.
* You can have the bot respond differently to different users
"""
def should_i_respond(user_message, user_name):
  if user_message == "Hi":
    return True
  if user_message == "Can you help me?":
    return True
  if "robot" in user_message:
    return True
  if user_message =="You can help me with an issue i've been having":
   return True 
  if user_message =="I cant get this stupid discord bot to work. It's not loading":
   return True 
  if user_message =="No, I have not thought about that. Let me try that":
   return True 
  if user_message =="It didnt work":
   return True 
  if user_message =="Its still not working":
   return True 
  else:
    return False
  

"""
**Do NOT change the name of this function.**

This function will be called every time the `should_i_respond` function returns `True`.

* This function returns a string.
* The bot will post the returned string on the channel where the original message was sent.
* You can have the bot respond differently to different messages and users
"""
def respond(user_message, user_name):
  if user_message == "You can help me with an issue i've been having":

    return "Sure no thing, what seems to be the issue"
  if user_message == "Hi": 
    print("asdf")
    return "Hi, how are you?"
  if user_message == "Can you help me?":   
    return "Yes, how can I help"
  if user_message == "I cant get this stupid discord bot to work. It's not loading":   
    return "Have you thought about refreshing the page"
  if user_message == "No, I have not thought about that. Let me try that":   
    return "Sure, try that"
  if user_message == "It didnt work":   
    return "Try it again"
  if user_message == "Its still not working":   
    return "Try it again"
  return user_message.replace("robot", user_name)
