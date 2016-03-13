
	angular.module('my-ged.archives', [ 'ngRoute' ])
	.config(
		function($routeProvider) {
			 $routeProvider
        		.when('/archives', {
            		templateUrl: 'partials/archives.html',
            		controller: 'archivesCtrl',
            		resolve: {
            			names : function(TokenRestangular) {
                        	return TokenRestangular.one("documents").get()  ;
                    	}
            		}
        		});
		});