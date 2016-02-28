angular.module('my-ged.plan', [ 'ngRoute']).config(
		function($routeProvider) {
			 $routeProvider
        		.when('/plan', {
            		templateUrl: 'partials/plan.html',
            		controller: 'planCtrl',
            		resolve: {
         				   plan : function(planSvc){
                				return planSvc.getPlan();
                			},
                            folders: function(planSvc){
                                return planSvc.getFolders();
                            }

        			}
        		});
		});