use git-dumper and change head to insecure commit
find creds for stuart->

ssh with creds ->
run linpeas, find sitebackup.zip
get hashes with zip2john, cracket pass ->

creds+finds:
public $mailfrom = 'chloe@challenge.lab'; 
public $secret = 'Ee24zIK4cDhJHL4H';
public $user = 'joomla';
public $password = 'Password@1';                      
public $db = 'jooml';               
public $dbprefix = 'o83rl_';


switch user to chloe:Ee24zIK4cDhJHL4H
it is root user

