angular.module('my-ged.login', [ 'ui.router','ngCookies' ]).config(
		function($stateProvider) {
			 $stateProvider
                .state('login', {
                    url: '/login',
            		templateUrl: 'partials/login.html',
            		controller: 'loginCtrl',
            		resolve: {
         				   users : function(userSvc){
                				return userSvc.getAll();
                		   }
        			}
        		})
                /*.when('/logout', {
                    templateUrl: 'partials/login.html',
                    controller: 'logoutCtrl',
                    resolve: {
                           users : function(userSvc){
                                return userSvc.getAll();
                           }
                    }
                })*/
                ;
		});