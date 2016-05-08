	
angular.module('my-ged.home')
.controller('homeCtrl',['$scope', '$rootScope', '$timeout', '$mdSidenav', '$log', 'loginSvc', 'alertSvc'
							, 'errInterceptorConfig', '$location', 'driveSvc', '$state', '$websocket',

	function($scope, $rootScope, $timeout, $mdSidenav, $log, loginSvc, alertSvc, errInterceptorConfig, $location, driveSvc, $state , $websocket) {

    	$scope.pong = function () {

    	 	var message = {
    	 		origin: 'Client',
    	 		code: 'pong' ,
				user: $rootScope.globals.user.username,
				date: moment().format('MMMM Do YYYY, h:mm:ss a')
                /*level: 1,
                text: 'ngWebsocket rocks!',
                array: ['one', 'two', 'three'],
                nested: {
                    level: 2,
                    deeper: [{
                        hell: 'yeah'
                    }, {
                        so: 'good'
                    }]
                    }
				*/                    
                
            };

            $scope.ws.$emit('pong', message);
      		
        }

  //$scope.loaded=true;
}]);