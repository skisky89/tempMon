<html>
<meta name="viewport" content="width=device-width, initial-scale=1.50">
<head>
<?php 
//////////////////////////////////////////Colors
if (isset($_POST['Red']))
{
exec('sudo python /var/www/gpio/red.py');
}
if (isset($_POST['Blue']))
{
exec('sudo python /var/www/gpio/blue.py');
}
if (isset($_POST['Cyan']))
{
exec('sudo python /var/www/gpio/cyan.py');
}
if (isset($_POST['Green']))
{
exec('sudo python /var/www/gpio/green.py');
}
if (isset($_POST['OFF']))
{
exec('sudo python /var/www/gpio/off.py');
}
if (isset($_POST['Yellow']))
{
exec('sudo python /var/www/gpio/yellow.py');
}
if (isset($_POST['White']))
{
exec('sudo python /var/www/gpio/white.py');
}
if (isset($_POST['Custom']))
{

exec('sudo python /var/www/gpio/custom.py');
}
////////////////////////////////////////////Brightness
if (isset($_POST['LOW']))
{
exec('sudo python /var/www/gpio/LOW.py');
}
if (isset($_POST['25B']))
{
exec('sudo python /var/www/gpio/25B.py');
}
if (isset($_POST['50B']))
{
exec('sudo python /var/www/gpio/50B.py');
}
if (isset($_POST['75B']))
{
exec('sudo python /var/www/gpio/75B.py');
}
if (isset($_POST['100B']))
{
exec('sudo python /var/www/gpio/100B.py');
}
?>

  <title>BG Lights</title>
</head>
<body>
<td style="text-align: center;"> Entertainment Lighting</td>
<br>
<form method="post">
  <table
 style="width: 15%; "
 border="0" cellpadding="3" cellspacing="3">
    <tbody>
      
	<tr>
        <td style="text-align: center;"> Color</td>
	<td style="text-align: center;"> Brightness</td>
        
  </tr>
  <tr>
    <td style="text-align: center;"><button name="Red">Red</button></td>
    <td style="text-align: center;"><button name="25B">25%</button></td>
   </tr>
  <tr>
    <td style="text-align: center;"><button name="Cyan">Cyan </button></td>
    <td style="text-align: center;"><button name="50B">50%</button></td>
  </tr>
  <tr>
    <td style="text-align: center;"><button name="Green">Green </button></td>
    <td style="text-align: center;"><button name="75B">75%</button></td>
     </tr>
<tr>
    <td style="text-align: center;"><button name="Yellow">Yellow </button></td>
    <td style="text-align: center;"><button name="100B">100%</button></td>
     </tr>
<tr>
	<td style="text-align: center;"><button name="Blue">Blue </button></td>
	<td style="text-align: center;"><button name="LOW">Low Glow</button></td>
</tr>
<tr>
	<td style="text-align: center;"><button name="White">White </button></td>

  <tr>
	<td style="text-align: center;"><button name="OFF">OFF </button></td>
</tbody>
  </table>

<br>
<table id="opener">
    <tr id="row1">
        <td>one</td>
        <td>two</td>
        <td>three</td>
    </tr>
	<tr id = "button">
	<td style="text-align: center;"><button name="Custom">Custom </button></td>
	</tr>
</table>
</form>
</body>
</html>