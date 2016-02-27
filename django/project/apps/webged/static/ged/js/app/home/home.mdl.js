	
angular.module('my-ged.home', [ 'ngRoute' ]).config(
		function($routeProvider) {
			 $routeProvider
        		.when('/home', {
            	templateUrl: 'partials/home.html',
            	controller: 'appCtrl'
        		});
		});