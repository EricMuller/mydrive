angular.module('my-ged.login')
  .controller('loginCtrl',['$scope','$rootScope', '$location', 'users','loginSvc','$cookies',

      function  ($scope, $rootScope, $location, users, loginSvc,$cookies) {
      			
      	$scope.users=users;
      	$scope.username= $rootScope.globals.username;
      	$scope.password='';

			  $scope.options=null;      	

			  $scope.signIn = function(username,password) {
          			
	          	  loginSvc.signIn(username,password).then(function(result) {
                     $location.path('home');
                }

              );;
          			
          	}

        }

]);