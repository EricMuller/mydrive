angular.module('my-ged.login')
  .controller('loginCtrl',['$scope','$rootScope', '$location', 'users','loginSvc','$cookies','alertSvc',

      function  ($scope, $rootScope, $location, users, loginSvc, $cookies, alertSvc) {
      			
      	$scope.users=users;
      	$scope.username= $rootScope.globals.username;
      	$scope.password='';

			  $scope.options=null;      	

			  $scope.signIn = function(username,password) {
          			
	          	loginSvc.signIn(username,password).then(function(result) {

                    if(result == false){
                      alertSvc.error('Erreur de connection');
                    }else {

                      $rootScope.globals.user =loginSvc.getCurrentUser();

                      $location.path('home');
                      $rootScope.$broadcast("loginStateChanged", {
                              someProp: 'signIn OK'     
                      });

                   }
                }

              );
          			
          	};

        

        /*$scope.signOut = function(username,password) {
              loginSvc.signOut(username,password).then(function(result) {
                $rootScope.globals.user.authtoken
                $rootScope.$broadcast("loginStateChanged", {
                              someProp: 'signOut OK'     
                      });
                }
              );
            };*/

      }

]);