<?php<?php
if(isset($_POST['submit'])){
	$from = $_POST['email'];
	$subject = $_POST['name'];
	$Phone = $_POST['Phone_number'];
	$time = $_POST['time'];
	$to = "nida_nurain@yahoo.com";
	$headers = "From:" . $from;
	mail($to,$subject,$headers);
	echo "Mail Sent.";
}
?>