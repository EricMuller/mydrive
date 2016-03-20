	
angular.module('my-ged.home', [ 'ui.router','ngMaterial'])
.config(
		function($stateProvider) {

			 $stateProvider
        		.state('home', {
                   url:'/home',
            	   templateUrl: 'partials/home.html',
            	   controller: 'homeCtrl'

        		});
		});