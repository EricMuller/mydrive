angular.module('my-ged.login', [ 'ngRoute','ngCookies' ]).config(
		function($routeProvider) {
			 $routeProvider
                .when('/login', {
            		templateUrl: 'partials/login.html',
            		controller: 'loginCtrl',
            		resolve: {
         				   users : function(userSvc){
                				return userSvc.getAll();
                		   }
        			}
        		});
		});