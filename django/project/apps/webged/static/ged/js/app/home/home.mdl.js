	
angular.module('my-ged.home', [ 'ngRoute','ngMaterial']).config(
		function($routeProvider) {
			 $routeProvider
        		.when('/home', {
            	templateUrl: 'partials/home.html',
            	controller: 'homeCtrl'
        		});
		});