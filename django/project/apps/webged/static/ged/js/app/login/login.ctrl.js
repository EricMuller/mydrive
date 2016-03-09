angular.module('my-ged.login')
  .controller('loginCtrl',['$scope','$rootScope', '$location', 'users','loginSvc',

      function  ($scope, $rootScope, $location, users, loginSvc) {
      			
      		$scope.users=users;
      		$scope.user='webdev';
      		$scope.password='webdev';

			$scope.options=null;      	

			$scope.signIn = function(username,password) {
          			
	          	loginSvc.signIn(username,password).then(function(result) {
                    // $rootScope.status = result.status;
                    if(result){
                     	$rootScope.globals.currentUser= true;
             		}else{
             			$rootScope.globals.currentUser= false;
             		}
                     debugger
                     $location.path('home');

                 });;
          			
          	}

        }

]);