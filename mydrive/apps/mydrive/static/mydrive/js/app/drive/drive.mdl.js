angular.module('my-ged.plan', [ 'ui.router' ]).config(
		function($stateProvider) {
			 $stateProvider
        		.state('plan', {
                    url: '/plan',
            		templateUrl: 'partials/plan.html',
            		controller: 'planCtrl',
            		resolve: {
         				   plan : function(driveSvc){
                				return driveSvc.getPlan();
                			},
                            folders: function(driveSvc){
                                return driveSvc.getFolders();
                            }

        			}
        		});
		});