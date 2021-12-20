<!DOCTYPE html>
<html lang="en">

<head>
	<meta charset="UTF-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<link rel="stylesheet" href="css/bootstrap.min.css">
	<script src="jquery/jquery.min.js"></script>
	<title>Sensor | Kreshna Putra</title>

	<script type="text/javascript">
		$(document).ready(function(){
			setInterval(function(){
				$("#ceksensor").load('ceksensor.php');
			}, 1000);
		});
	</script>
</head>

<body>
	<div class="container" style="text-align: center; padding-top: 10%; width: 500px; ">
		<h2>Nilai Sensor</h2>
		<div class="panel panel-default">
			<div class="panel-body">
				<h1><span id="ceksensor"></span></h1>
			</div>
		</div>
		<img src="images/nama.png" alt="nama">
	</div>
</body>

</html>
