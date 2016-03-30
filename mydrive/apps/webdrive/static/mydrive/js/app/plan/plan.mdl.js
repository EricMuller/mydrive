angular.module('my-ged.plan', [ 'ui.router' ]).config(
		function($stateProvider) {
			 $stateProvider
        		.state('plan', {
                    url: '/plan',
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