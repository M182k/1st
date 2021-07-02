<!DOCTYPE html>
<html lang="en">
	<head>
	    
	    <meta name="viewport" content="width=device-width, initial-scale=1">

	    <title>eCommerce Product Detail</title>
	    <link href="https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css" rel="stylesheet">
	    <link href="https://fonts.googleapis.com/css?family=Open+Sans:400,700" rel="stylesheet">
	     <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css" rel="stylesheet" 
	     integrity="sha384-eOJMYsd53ii+scO/bJGFsiCZc+5NDVN2yr8+0RDqr0Ql0h+rP48ckxlpbzKgwra6" crossorigin="anonymous">
	    
	    <style types="text/css">

	    body {
		  font-family: 'open sans';
		  overflow-x: hidden; }

		img {
		  max-width: 100%; }

		.preview {
		    display: -webkit-box;
		    display: -webkit-flex;
		    display: -ms-flexbox;
		    display: flex;
		    -webkit-box-orient: vertical;
		    -webkit-box-direction: normal;
		    -webkit-flex-direction: column;
		        	-ms-flex-direction: column;
		          			flex-direction: column; }
		    @media screen and (max-width: 996px) {
		    	.preview {
		    		margin-bottom: 20px; } }

		.preview-pic {
		    -webkit-box-flex: 1;
		    -webkit-flex-grow: 1;
		        	-ms-flex-positive: 1;
		          			flex-grow: 1; }

		.preview-thumbnail.nav-tabs {
		    border: none;
		    margin-top: 15px; }
		   .preview-thumbnail.nav-tabs li {
		    	width: 18%;
		    	margin-right: 2.5%; }
		    	.preview-thumbnail.nav-tabs li img {
		    		max-width: 100%;
		    		display: block; }
		    	.preview-thumbnail.nav-tabs li a {
		    		padding: 0;
		    		margin: 0; }
		    	.preview-thumbnail.nav-tabs li:last-of-type {
		      		margin-right: 0; }

		.tab-content {
			overflow: hidden; }
		    .tab-content img {
		    	width: 100%;
		    	-webkit-animation-name: opacity;
		            			animation-name: opacity;
		    	-webkit-animation-duration: .3s;
		            			animation-duration: .3s; }

		.card {
		    margin-top: 50px;
		    background: #eee;
		    padding: 3em;
		    line-height: 1.5em; }

		@media screen and (min-width: 997px) {
			.wrapper {
		    	display: -webkit-box;
		    	display: -webkit-flex;
		    	display: -ms-flexbox;
		    	display: flex; } }

		.details {
		    display: -webkit-box;
		    display: -webkit-flex;
		    display: -ms-flexbox;
		    display: flex;
		    -webkit-box-orient: vertical;
		    -webkit-box-direction: normal;
		    -webkit-flex-direction: column;
		    		-ms-flex-direction: column;
		        			flex-direction: column; }

		.colors {
			-webkit-box-flex: 1;
			-webkit-flex-grow: 1;
		    		-ms-flex-positive: 1;
		          			flex-grow: 1; }

		.product-title, .price, .sizes, .colors {
			text-transform: UPPERCASE;
			font-weight: bold; }

		.checked, .price span {
			color: #ff9f1a; }

		.product-title, .rating, .product-description, .price, .vote, .sizes {
			margin-bottom: 15px; }

		.product-title {
			margin-top: 0; }

		.size {
			margin-right: 10px; }
			.size:first-of-type {
				margin-left: 40px; }

		.color {
			display: inline-block;
			vertical-align: middle;
			margin-right: 10px;
			height: 2em;
			width: 2em;
			border-radius: 2px; }
			.color:first-of-type {
		    	margin-left: 20px; }

		.add-to-cart, .like {
			background: #ff9f1a;
			pad
