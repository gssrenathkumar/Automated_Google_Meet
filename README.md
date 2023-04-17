<h1>Automated Google Meet</h1>
<p>This project automates the process of joining a Google Meet call using Selenium and Twilio API.</p>

<h2>Overview</h2>
<p>In my college, at 8:30, there will be a telegram message consisting of google meet credentials. So at sharp 8:30, the selenium python code goes to my telegram account, gets the latest message data, searches for the meet link in the text, and stores it in the variable. The next step thee selenium downloads the latest chrome web driver and start to add the data to the chrome, and automatically log in. After login, the software disables the camera and microphone automatically and enters into the meet</p>

<h2>Features</h2>
<ul>
  <li>Automatically joins a Google Meet call at a specified time</li>
  <li>Retrieves the call link from a Telegram message</li>
  <li>Logs in to the call using email credentials</li>
  <li>Disables camera and microphone automatically</li>
  <li>Sends a Twilio message to the user if the process works correctly or if there's an issue joining the call</li>
</ul>

<h2>Usage</h2>
<p>To use this program, you need to provide your Telegram API token, Twilio account SID, and auth token in the <code>config.py</code> file. Also, make sure you have the latest version of Chrome and the ChromeDriver installed on your system. Then, simply run the <code>main.py</code> file at the time you want to join the call.</p>

<h2>Example</h2>
<p>Here's an example of the program running:</p>
<img src="example.png" alt="Example screenshot" width="600">

<h2>Dependencies</h2>
<ul>
  <li>Selenium</li>
  <li>Twilio</li>
  <li>Telethon</li>
</ul>

<h2>License</h2>
<p>This project is licensed under the MIT License - see the <code>LICENSE</code> file for details.</p>
