angular.module('my-ged.upload', [ 'ngRoute' ]).config(
		function($routeProvider) {
			 $routeProvider
        		.when('/upload', {
            		templateUrl: 'partials/upload.html',
            		controller: 'uploadCtrl'
        		});
		});