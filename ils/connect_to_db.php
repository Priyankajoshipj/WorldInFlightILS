
<?PHP
	$db_host = "localhost";
	$db_username = "root";
	$db_library ="accounts";
	$db_pass = "MyNewPass";
	$connection = mysql_connect("$db_host","$db_username","$db_pass");
if(!$connection){
	die("Could not connect to MySQL: ".mysql_error());
}
if (mysql_query("Use accounts",$connection))
{echo "Accounts Database being Used!";}
else
{
	echo "Error:Cannot find DB".mysql_error();}
mysql_close($connection);
?>
