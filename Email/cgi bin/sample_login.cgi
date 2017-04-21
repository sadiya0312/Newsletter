#!/usr/bin/perl -wT
use strict; 
use CGI; 
use CGI::Carp qw/fatalsToBrowser/;
use Fcntl qw(:flock);

my $cgi = new CGI;

my $uname = $cgi->param( "username" );
my $password = $cgi->param( "password" ); 
my $login = "fail";
		
my $salt = "21";
my $enpass = crypt($password,$salt);
open(PASSWDDATA, "<passwd.txt") or die "Can not open passwd.txt";

break: while(<PASSWDDATA>)
{
	my $line = $_;
	my @namepass = split(' ',$line);
	if($namepass[0] eq $uname && $namepass[1] eq $enpass)
	{
	  $login = "success";
	  last break;
	}
		  
}
close(PASSWDDATA);
#displayOtherHTMLPage($cgi);

if($login eq "success")
{		
	displayOtherHTMLPage($cgi);
}
else
{
	print $cgi->header( "text/html" );
	print "Content-type: text/html\n";
	print $cgi->start_html( 
                -title    => "Welcome To Anybody Can Dance Club",			
		-topmargin =>"0"
        ),
	$cgi->h2( {-style=>"color:#ff2b20"}, " Sorry! Login Failed, Click Here to Try Again"),
	$cgi->a( {-href=>"http://playground.bradley.edu/~sgovil/sample_login.html", -target=>"_parent", -style=>"color:#ff2b20"}, "Login"),
	$cgi->end_html;
}


# creates the Other page
sub displayOtherHTMLPage {
	my( $cgi ) = @_;
	my @username = split('@',$cgi->param( "username" ));
	my $user = $username[0];
	
	print $cgi->header( "text/html" ),
	$cgi->start_html(
        	-title    => "Welcome To Anybody Can Dance Club",			
		-topmargin =>"0"
        ),
	
	$cgi->h1( {-style=>"color:#ff2b20"}, "Welcome to Anybody Can Dance Club!  $user "),
	$cgi->a( {-href=>"http://playground.bradley.edu/~sgovil/upcoming_classes.html", -target=>"_parent", -style=>"color:#ff2b20"}, "Upcoming Classes at Anybody Can Dance Club!"),
	$cgi->br,
	$cgi->a( {-href=>"http://playground.bradley.edu/~sgovil/videos.html", -target=>"_parent", -style=>"color:#ff2b20"}, "Videos"),
	$cgi->br,
        $cgi->a( {-href=>"http://playground.bradley.edu/~sgovil", -target=>"_parent", -style=>"color:#ff2b20"}, "Logout"),
	$cgi->end_html;    
}
