# -terminchecker
A Python script that automatically checks whether a termin (appointment) is available at the Munich Ausländerbehörde (https://stadt.muenchen.de/buergerservice/terminvereinbarung.html#/services/10339027/locations/10187259).

# set the sender/reciever email
-sender email : sender's email address
-receiver email : recipient's email address
password : sender's email password. For Gmail, an app password must be used.

Prerequisites
Ensure that terminchecker.py is located on your system, and you know its full path (e.g., /home/user/scripts/terminchecker.py).

You have access to the terminal and permissions to edit your cron table.

Steps
1. Open the Terminal
Open the terminal on your system to access the command line interface.

2. Locate Your Python Script
Make sure you know the full path to your terminchecker.py script. For example:

bash
Copy
Edit
/home/user/scripts/terminchecker.py
3. Edit the Cron Table
Run the following command to open your cron table for editing:

bash
Copy
Edit
crontab -e
4. Add a New Cron Job
In the editor that opens, add a new line at the bottom to specify when and how to run the script. The general syntax for a cron job is as follows:

bash
Copy
Edit
* * * * * /path/to/python /path/to/terminchecker.py
Each asterisk represents a scheduling component (minute, hour, day of the month, month, day of the week).

Example Schedules:
* * * * * — Run every minute

0 0 * * * — Run at midnight every day

30 2 * * * — Run at 2:30 AM every day

For example, to run the script every day at midnight:

bash
Copy
Edit
0 0 * * * /usr/bin/python3 /home/user/scripts/terminchecker.py
5. Save and Exit the Editor
If using nano, press Ctrl + O to save, then Ctrl + X to exit.

If using vim, press Esc, then type :wq and press Enter.

6. Confirm the Cron Job
To verify that your cron job was added successfully, run:

bash
Copy
Edit
crontab -l
This will list all the current cron jobs, including the one you just added.

7. (Optional) Check Cron Logs
If you want to check whether the cron job is running correctly, view the cron logs (typically located in /var/log/syslog) by running:

bash
Copy
Edit
grep CRON /var/log/syslog
