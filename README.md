# Automated_Google_Meet

Here we are automating the google meet login with the email credentials and joining the meet.

In my college, at 8:30, there will be a telegram message consisting of google meet credentials. So at sharp 8:30, the selenium python code goes to my telegram account, gets the latest message data, searches for the meet link in the text, and stores it in the variable. The next step thee selenium downloads the latest chrome web driver and start to add the data to the chrome, and automatically log in.
After login, the software disables the camera and microphone automatically and enters into the meet

The additional feature added here is that if all the process works correctly, a message is sent to the user through Twilio API as "Joined successfully."
Otherwise, if any issue is found, it returns a message as "Issue in joining the meet."
