angular.module('my-ged.login')
  .controller('loginCtrl',['$scope','$rootScope','users','loginSvc',

      function  ($scope, $rootScope, users , loginSvc) {
      			
      		$scope.users=users;

			$scope.options=null;      		
			            
        }

]);