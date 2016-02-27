angular.module('my-ged.archives').controller('archivesCtrl',['$scope','$http','$rootScope',

	function($scope, $http, $rootScope) {
  	
  		$scope.showIt=true;

		$rootScope.selectedMenuName('Archives');

		var d = new Date();
  		console.log(d);
  		$http.get("apis/documents/")
  			.success(function(response) {
  				$scope.names = response;
  				$scope.text=d;
  			});
	}	

])