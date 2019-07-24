/*
JavaScript in Chrome
Here are the steps to turn on or turn off JavaScript in Chrome −

Click the Chrome menu at the top right hand corner of your browser.

Select Settings.

Click Show advanced settings at the end of the page.

Under the Privacy section, click the Content settings button.

In the "Javascript" section, select "Do not allow any site to run JavaScript" or "Allow all sites to run JavaScript (recommended)".


Warning for Non-JavaScript Browsers
If you have to do something important using JavaScript, 
then you can display a warning message to the user using <noscript> tags.

You can add a noscript block immediately after the script block as follows −

<html>
   <body>
      <script language = "javascript" type = "text/javascript">
         <!--
            document.write("Hello World!")
         //-->
      </script>
      
      <noscript>
         Sorry...JavaScript is needed to go ahead.
      </noscript>      
   </body>
</html>
Now, if the user's browser does not support JavaScript or JavaScript is not enabled, 
then the message from </noscript> will be displayed on the screen.
*/