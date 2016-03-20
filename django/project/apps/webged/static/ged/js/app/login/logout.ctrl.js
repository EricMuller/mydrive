angular.module('my-ged.login')
  .controller('logoutCtrl',['$scope','$rootScope', '$location', 'users','loginSvc','$cookies',

      function  ($scope, $rootScope, $location, users, loginSvc,$cookies) {
      			
      	$scope.users=users;
      	$scope.username= $rootScope.globals.username;
      	$scope.password='';

			  $scope.options=null;      	

        loginSvc.signOut().then(function(result) {
              $rootScope.$broadcast("loginStateChanged", {
                              someProp: 'signOut OK'     
                    });
              });

			  
        }

]);