# incident report for site outage #

![internal server error 500](https://www.lifewire.com/thmb/5hOU7hTnn89zLe-szoztWtlmCXo=/650x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/500-internal-server-error-explained-2622938-1485165a9b6942f09f2f5257682c0b6e.png)<br />
## Postmortem <br />
###### issue summary<br />
On February 17th, 2022 from 6:30 PM to 7:30 PM WAT, the company's website was down for one hour. 100% of the users expexperienced ** 500 internal server error ** caused by a typo error in a filename in a configuration file. <br />

######Timeline <br />
-6:30 PM Deployed site outage begins <br />
-6:31 PM Error Logs checked by the DevOps team <br />
-6:50 PM Configuration updated to log extra errors <br />
-7:15 PM Filename error caught in config file <br />
-7:20 PM Execute Puppet manifest across all company servers <br />
-7:30 PM 100% restored and back online <br />

###### Root Cause and Resolution <br />

After a smaall update was deployed without being tested first, the site started given error. No error was found in our "error.log" files we modified our configuration file to allow for more error logging.

With the help of "Strace," we found out that there was a filename typo error which triggered errors when the site was requested.

The server was attempting to locate the file as normal procedure but failed to find the file ending in ".phpp" when it should be searching for ".php".

After fixing this line in the '/var/www/html/wp-settings.php' file, tests succeded to show the site was okay. Apuppet manifest was written and executed across all company servers immediately after to restore service.
<br />

###### Corrective and Preventive Measures <br />

After a discussion with the team members it has been decided that we can prevent this in future by :
<br />
- Test before deploying on all servers no matter how small an update is, since this is a minute incident we were able to rectify it on time. <br />
- Modifying configuration files for more error logging to accelerate response time.
