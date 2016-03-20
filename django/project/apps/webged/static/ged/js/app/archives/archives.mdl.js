
	angular.module('my-ged.archives', [ 'ui.router' ])
	.config(
		function($stateProvider) {
			 $stateProvider
        		.state('archives', {
                    url: '/archives',
            		templateUrl: 'partials/archives.html',
            		controller: 'archivesCtrl',
            		resolve: {
            			names : function(TokenRestangular) {
                        	return TokenRestangular.one("documents").get()  ;
                    	}
            		}
        		});
		});