<!DOCTYPE html>
		<html lang="en">
			<head>
		    	<meta charset="utf-8">
		    	<meta name="viewport" content="width=device-width, initial-scale=1">
		    	<title>Optical Character Recognition</title>

				<!-- Bootstrap -->
				<link rel="stylesheet" type="text/css" href="assets/css/bootstrap.min.css">
				<!-- Main Style -->
				<link rel="stylesheet" type="text/css" href="assets/css/main.css">
				<!-- Responsive Style -->
				<link rel="stylesheet" type="text/css" href="assets/css/responsive.css">
				<!--Icon Fonts-->
				<link rel="stylesheet" media="screen" href="assets/fonts/font-awesome/font-awesome.min.css">
				<!-- Extras -->
				<link rel="stylesheet" type="text/css" href="assets/extras/animate.css">
				<link rel="stylesheet" type="text/css" href="assets/extras/lightbox.css">
				<!-- jQuery Load -->
				<script src="assets/js/jquery-min.js"></script>
				<!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media queries -->
				<!--[if lt IE 9]>
				  <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
				  <script src="https://oss.maxcdn.com/libs/respond.js/1.4.2/respond.min.js"></script>
				<![endif]-->
			</head>

			<body data-spy="scroll" data-offset="20" data-target="#navbar">
				<!-- Nav Menu Section End -->
				<!-- Hero Area Section -->
				<section id="hero-area">
					<div class="container">
						<div class="row">
						<div class="col-md-12">
							<h2 class="title">Optical Character Recognition</h2>
							<h3 class="subtitle">Extract data from documents!</h3>
						<div class="col-md-6 col-sm-6 col-xs-12 animated fadeInRight delay-0-5 button" style="text-align:center;">
							<form action="up.php" enctype="multipart/form-data" method="post" style="float: right; width:100%;">
								<input type="file" name="files[]" id="files" multiple="" directory="" webkitdirectory="" mozdirectory=""> <br/>
								<select class="btn col-md-4 col-md-offset-3" name="typeofdoc" style="color:black; top: 0%;position: absolute;">
									<option >Choose Option</option>
									<option value="aadhaar">Aadhaar Card</option>
									<option value="cheque">Cheque</option>
									<option value="pan">PAN Card</option>
									<option value="license">Driving License</option>
									<option value="other">Other</option>		
								</select>
								<input class="btn col-md-4 col-md-offset-3" type="submit" value="Process" name="Submit" style="margin-top: 20%; color:black;" />
								<img class="col-md-6 col-sm-6 col-xs-12 animated fadeInLeft uimage" id="output" />
							</form>
						</div>
						</div>
						</div>
					</div>
				</section>

				<!-- Hero Area Section End-->
				<!-- Copyright Section End-->
				<!-- Bootstrap JS -->
				<script src="assets/js/bootstrap.min.js"></script>
				<!-- Smooth Scroll -->
				<!-- Smooth Scroll -->
				<script src="assets/js/smooth-scroll.js"></script>
				<script src="assets/js/lightbox.min.js"></script>
				<!-- All JS plugin Triggers -->
				<script src="assets/js/main.js"></script>
			</body>
		</html>
