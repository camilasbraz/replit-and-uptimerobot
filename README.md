# replit-and-uptimerobot
How to use repl.it and UpTimeRobot to run Python Scripts on a schedule in the cloud 24/7 for free

1. Create a replt account: [Here](https://replit.com/)
2. New python repl
3. Upload the files (except .env)
4. Use the Secret tab to add the .env vars
5. Run the code!!!
6. A webdriver tab will open on the left side of the page. Copy the url

<img width="338" alt="url_webdriver" src="https://user-images.githubusercontent.com/45129483/215798184-89026c92-20c2-41fd-9068-cd41a1e8015f.png">

7. Create an UpTimeRobot account  [Here](https://uptimerobot.com)
8. Click on  `Add New Monitor` and set the following configs:

`Monitor type: http`

`Name: anything you want`

`URL: the URL copied in step 6`

`Interval: 5 minutes`

`Timeout: 30 seconds`

The remaining configurations can be default, just scroll down and click on `Create the Monitor`


