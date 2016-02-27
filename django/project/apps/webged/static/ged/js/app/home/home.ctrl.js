	
angular.module('my-ged.home').controller('appCtrl',['$scope','$rootScope',

	function($scope, $rootScope) {
		
		$rootScope.selectedMenuName= function(title){
			$rootScope.selectedMenu=title;
			$('#title').text(title);
		};

		$rootScope.selectedMenuName('Welcome');
		$scope.uploadFiles = [];
}]);