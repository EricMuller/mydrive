angular.module('my-ged.login')
  .controller('signCtrl',['$scope','$rootScope','loginSvc',

      function  ($scope, $rootScope , loginSvc) {

			     $scope.options=null;      	

			     $scope.signIn = function(username,password) {
          			loginSvc.signIn(username,password);
          	}

        }

]);