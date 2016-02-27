angular.module('my-ged.plan', [ 'ngRoute' ]).config(
		function($routeProvider) {
			 $routeProvider
        		.when('/plan', {
            		templateUrl: 'partials/plan.html',
            		controller: 'planCtrl'
        		});
		});