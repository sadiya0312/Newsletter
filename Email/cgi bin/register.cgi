#!/usr/bin/perl -w
use strict; 
use CGI; 
use CGI::Carp qw ( fatalsToBrowser );
use File::Basename;

#$CGI::POST_MAX = 1024 * 5000;

#my $safe_filename_characters = "a-zA-Z0-9_.-";

#my $upload_dir = "http://cs99.bradley.edu/~sgovil/images";
use Fcntl qw(:flock);
    
            my $cgi = new CGI;
            my $fname = $cgi->param( "fname" );
            my $lname = $cgi->param( "lname" );
	        my $dob = $cgi->param( "dob" );
	        my $uname = $cgi->param( "uname" );
			my $password = $cgi->param( "password" );
            my $email = $cgi->param( "email" );	
          	my $gender = $cgi->param( "gender" );	
			my $address = $cgi->param( "address" );
			my $state = $cgi->param( "state" );
			my $city = $cgi->param( "city" );
			my $zip = $cgi->param( "zip" );
			my $phone = $cgi->param( "phone" );
			#my $filename = <img src="/upload/$filename" alt="Photo" />;

my @dancetype = $cgi->param( "dancetype" );

		my $home = 'http://playground.bradley.edu/~sgovil/sample_login.html';
	        my $salt = "21";
			my $enpass = crypt($password,$salt);			

            open(FILE, ">>passwd.txt") or die "cannot open file";
	    print FILE "$uname $enpass $fname $lname $dob $email $gender $address $state $city $zip $phone @dancetype \n";
            close FILE;
#use Email::Valid;
#if( Email::Valid->address($Emaild) ) { }
my $to = $email;
my $from = 'noreply@abcd.com';
my $subject = 'Registration Confirmation from Anybody Can Dance club';
my $message = 'Hi,
Regestration Confirmation:
Your regestration is succesfull now you can enjoy our services have fun....!!!


Thanks& Regards
Anybody Can Dance Club';


open(MAIL, "|/usr/sbin/sendmail -t");

# Email Header
print MAIL "To: $to\n";
print MAIL "From: $from\n";
print MAIL "Subject: $subject\n\n";
# Email Body
#print MAIL $message;
#print MAIL "Content-type: text/html\n";
print MAIL $message;
close(MAIL);

				
            print $cgi->header( "text/html" ),
            $cgi->start_html(
                    -title    => "Welcome to Anybody Can Dance Club !!! ",                   
                    -topmargin =>"auto"
            ),
            
            $cgi->h1( {-style=>"color:#ff2b20"}, "Welcome to Anybody Can Dance Club $fname !!! "),
            $cgi->h2( {-style=>"color:#ff2b20"}, "Successfully registered"),
            $cgi->h2( {-style=>"color:#ff2b20"},"Please login with your username : $uname"),
            $cgi->h2( {-style=>"color:#ff2b20"},"Your account details :"),
            $cgi->h3( {-style=>"color:#ff2b20"}, "First Name: $fname"),
            $cgi->h3( {-style=>"color:#ff2b20"}, "Last Name : $lname"),
			$cgi->h3( {-style=>"color:#ff2b20"}, "Date of Birth : $dob"),
			$cgi->h3( {-style=>"color:#ff2b20"}, "User Name : $uname"),
			$cgi->h3( {-style=>"color:#ff2b20"}, "Email : $email"),
			$cgi->h3( {-style=>"color:#ff2b20"}, "Gender : $gender"),
			$cgi->h3( {-style=>"color:#ff2b20"}, "Address : $address"),
			$cgi->h3( {-style=>"color:#ff2b20"}, "State : $state"),
			$cgi->h3( {-style=>"color:#ff2b20"}, "City : $city"),
			$cgi->h3( {-style=>"color:#ff2b20"}, "Zip : $zip"),			
			$cgi->h3( {-style=>"color:#ff2b20"}, "Phone number : $phone"),
			#$cgi->h3($filename),
			$cgi->h3( {-style=>"color:#ff2b20"}, "Your Dance Choice : @dancetype"),

			$cgi->h3( {-style=>"color:#ff2b20"}, "Registration confirmation has been emailed to $email"),   		
	$cgi->a( {-href=>"http://playground.bradley.edu/~sgovil/sample_login.html", -style=>"color:#ff2b20", -target=>"_parent"}, "Login")