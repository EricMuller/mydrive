angular.module('my-ged.drive', [ 'ui.router' ]).config(
		function($stateProvider) {
			 $stateProvider
        		.state('repositories', {
                    url: '/repositories',
            		templateUrl: 'partials/drive/repositories.html',
            		controller: 'repositoryCtrl',
            		resolve: {
         				   repositories: function(driveSvc){
                				return driveSvc.getPlan();
                			},
                            folders: function(driveSvc){
                                return driveSvc.getFolders();
                            }

        			}
        		});
		});