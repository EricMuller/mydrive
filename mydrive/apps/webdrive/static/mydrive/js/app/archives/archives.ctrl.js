

  angular.module('my-ged.archives')
  .controller('archivesCtrl',['$scope','$http','$rootScope','names',

	function($scope, $http, $rootScope,names) {
  	
  	$scope.showIt=true;

		$rootScope.selectedMenuName('Archives');

    $scope.names=names;
		/*var d = new Date();
  		console.log(d);
  		$http.get("apis/documents/")
  			.success(function(response) {
  				$scope.names = response;
  				$scope.text=d;
  			});*/
	}	

])