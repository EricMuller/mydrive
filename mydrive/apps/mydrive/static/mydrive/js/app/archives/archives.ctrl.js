

  angular.module('my-ged.archives')
  .controller('archivesCtrl',['$scope','$http','$rootScope','names','alertSvc','documentSvc',

	function($scope, $http, $rootScope, names, alertSvc, documentSvc) {
  	
  	$scope.showIt=true;

		//$rootScope.selectedMenuName('Archives');

    $scope.names=names;
		/*var d = new Date();
  		console.log(d);
  		$http.get("apis/documents/")
  			.success(function(response) {
  				$scope.names = response;
  				$scope.text=d;
  			});*/

     /* $scope.next = function(page){
        documentSvc.getDocuments(page).then(
            function(res){
              $scope.names=res;
            }
          );
      }*/

      $scope.pageChanged = function() {
          documentSvc.getDocuments($scope.names.current).then(
            function(res){
              $scope.names=res;
            }
          );
      };

      $scope.maxSize = 5;
      //$scope.bigTotalItems = 175;
      //$scope.bigCurrentPage = 1;
	}	

])