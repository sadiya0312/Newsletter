
  <?php
  print "outside mail handler";
  if(isset($_POST['Email'])){ 
// --- CONFIG PARAMETERS --- //
//
print "Iside mail handler";
   $email_recipient = "fns.sadiya@gmail.com";
   $email_sender = $_POST['name'];
   $email_return_to = $_POST['email'];
   $Phone = $_POST['Phone_number'];
   $time = $_POST['day_clock'];
   $opt = $_POST['opt'];
  
   
   $email_content_type = "text/html; charset=us-ascii";
   $email_client = "PHP/" . phpversion();
//
// ------------------------- //

// --- DEFINE HEADERS --- //
//
   $email_header = "From: " . $email_sender . "\r\n";
   $email_header .= "Reply-To: " . $email_return_to . "\r\n";
   $email_header .= "Return-Path: " . $email_return_to . "\r\n";
   $email_header .= "Content-type: " . $email_content_type . "\r\n";
   $email_header .= "X-Mailer: " . $email_client . "\r\n"; 
   $email_subject = "Newsletter";
   ob_start();
   ?>


     
<table align="center" border="1" cellpadding="0" cellspacing="0" width="600" style="border-collapse: collapse;">
 <tr>
  <td align="center" bgcolor="#70bbd9" style="padding: 40px 0 30px 0;">
   <img src="http://cs99.bradley.edu/~ashaik5/Sad/Email/shutterstock_33358642.jpg" alt="Creating Email Magic" width="300" height="230" style="display: block;" />
   
  </td>
  </tr>
  <tr>
   <td bgcolor="#ffffff" style="padding: 40px 30px 40px 30px;">
 <table border="1" cellpadding="0" cellspacing="0" width="100%">
  <tr>
   <td align="left">
    Dear <br>
    
   </td>
  </tr>
  <tr>
   <td style="padding: 20px 0 30px 0;" align="left">
    Enjoy broad, affordable professional liability insurance coverage from partners who <br> are committed to understanding you and your firm’s specific needs—Pearl<br> Insurance and Swiss Re Corporate Solutions, with products underwritten<br> by Westport Insurance Corporation.<br><br>
Button: Get a Lawyers Professional Liability Insurance Premium Estimate!<br> 
Why You Should Partner With Pearl Insurance and Swiss Re Corporate Solutions<br>
New and improved rate filings for every full-time attorney practicing at a<br> firm of nineteen (19) attorneys or fewer are designed to offer<br> significant premium reductions<br>
Affordable options for lawyers who work part-time or need coverage<br> options outside their main employment<br>
A+ financial ratings provide superior security<br>
Broad professional liability coverage, including continuity of coverage<br> and true consent to settle<br>
Swiss Re Corporate Solutions’ claims team of primarily attorneys averages<br> nineteen (19) years of industry experience and an<br> accumulation of fifty-two (52) years of Pennsylvania claims experience,<br> providing decades of knowledge with the laws, rules, judges, opposing<br> counsel, expert witnesses, and mediators in Pennsylvania<br><br>
Our free risk management is unmatched. For example, we provide three<br> (3) hours of free on-demand CLE approved webinars to every<br> covered attorney<br>
Learn more about our coverage features. (Link pearlinsurance.com/palawyers) If<br> you are a current Swiss Re Corporate Solutions policyholder, it’s never too<br> early to start thinking about renewing your Professional Liability Insurance<br> policy with us. Please choose the button below that applies to you,<br> and receive more information.<br><br>
Button: I am a current Swiss Re Corporate Solutions policyholder.<br><br>
Button: I have a policy with a different carrier. <br><br>
Please feel free to contact me at anytime. You may reach me at<br> palawyers@pearlinsurance.com or call 800.845.8941. I look forward to working<br> with you.<br> <br> 
    
   </td>
  </tr>
 </table>

<?php
//copy current buffer contents into $message variable and delete current output buffer
   $email_contents.= ob_get_clean();
   $email_contents.="Source Code: \r\n";
   $email_contents.="Pearl ID:\r\n";
   $email_contents.="Following is the customer information:\r\n";
   $email_contents.="Phone Number:" .$Phone. "\r\n";
   $email_contents.="Product Selected: ".$opt."\r\n";
   $email_contents.="Best day and time to contact: ".$time."\r\n";
  
   
//
// ---------------------------- //

$email_result = mail($email_recipient, $email_subject, $email_contents,$email_header);
if ($email_result) echo " Email has been sent!";
else echo "Email has failed!"; 
  }
 ?>