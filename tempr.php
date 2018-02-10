<!DOCTYPE HTML>
<html>
	<head>
	<title>Temperature Monitor</title>
	</head>
	<font size="5" >Temperature Monitoring/Logging system</font><br>
	<font size="3" ><i>Now wireless and portable! Current Location, 32501</i></font>
	<body>
	
	<br><br>
	<font size="3">Indoor Temperature: </font>
	
		<?php 
		$section = file_get_contents('./check.txt',null,null,0,4); 
		print_r($section);
			?>	
	
	<br>
	<font size="3">   Outdoor Temperature : </font>
	<?php 
		$section = file_get_contents('./check.txt',null,null,5,4); 
		print_r($section);
			?>	
<br>
	<font size="3">   Set Temperature : </font>
	<?php 
		$section = file_get_contents('./check.txt',null,null,9,4); 
		print_r($section);
			?>	

	<br><br>
	<font size="2" color="blue"> press F5 to refesh  (back-end data is refreshed every 5 minutes) </font>
	
	</body>
</html>
