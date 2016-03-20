	
angular.module('my-ged.home')
.controller('homeCtrl',['$scope','$rootScope','$timeout','$mdSidenav','$log','loginSvc','alertSvc','errInterceptorConfig','$location','planSvc',

	function($scope, $rootScope, $timeout, $mdSidenav, $log, loginSvc, alertSvc, errInterceptorConfig, $location, planSvc) {
		
		$rootScope.selectedMenuName= function(title){
			$rootScope.selectedMenu=title;
		//	$('#title').text(title);
		};
		
		$rootScope.selectedMenuName('Welcome');
		$scope.uploadFiles = [];

		$scope.$on('connectionStateChanged', function (event, data) {
  				console.log(data); 
		});

		$scope.plan = '';
		//
		
		$rootScope.$on(errInterceptorConfig.ERR_500_EVENT, interceptError);
    	$rootScope.$on(errInterceptorConfig.ERR_408_EVENT, interceptError);
    	$rootScope.$on(errInterceptorConfig.ERR_403_EVENT, interceptError);
    	$rootScope.$on(errInterceptorConfig.ERR_401_EVENT, interceptError);
    	$rootScope.$on(errInterceptorConfig.ERR_400_EVENT, interceptError);
    	$rootScope.$on(errInterceptorConfig.ERR_EVENT, interceptError);
	

		// var signIn = function() {
		// 	var loggedIn = $rootScope.globals.authtoken;
		// 	if (loggedIn){	
  //              $scope.plan = planSvc.getPlan(); 
  //      		}	
  //       };

    	// $scope.$on("loginStateChanged", signIn);

   		function interceptError(event, message) {
        	alertSvc.error('', message || '');
        	//$scope.signOut();
    	}

		// bar 
		$scope.toggleLeft = buildDelayedToggler('left');
	    $scope.toggleRight = buildToggler('right');
	    


	    $scope.signOut = function(){
	    	 loginSvc.signOut().then(function(result) {
	    		$location.path('home');
                $rootScope.$broadcast("loginStateChanged", {
                              someProp: 'signOut OK'     
                      });
                }
              );
            };
	    

	    $scope.isOpenRight = function(){
	      return $mdSidenav('right').isOpen();
	    };
	    /**
	     * Supplies a function that will continue to operate until the
	     * time is up.
	     */
	    function debounce(func, wait, context) {
	      var timer;
	      return function debounced() {
	        var context = $scope,
	            args = Array.prototype.slice.call(arguments);
	        $timeout.cancel(timer);
	        timer = $timeout(function() {
	          timer = undefined;
	          func.apply(context, args);
	        }, wait || 10);
	      };
	    }
	    /**
	     * Build handler to open/close a SideNav; when animation finishes
	     * report completion in console
	     */
	    function buildDelayedToggler(navID) {
	      return debounce(function() {
	        $mdSidenav(navID)
	          .toggle()
	          .then(function () {
	            $log.debug("toggle " + navID + " is done");
	          });
	      }, 200);
	    }

	    function buildToggler(navID) {
	      return function() {
	        $mdSidenav(navID)
	          .toggle()
	          .then(function () {
	            $log.debug("toggle " + navID + " is done");
	          });
	      }
	    
	    }

	    $scope.close = function () {
      			$mdSidenav('left').close()
        			.then(function () {
          			$log.debug("close LEFT is done");
        		});
        }		

		//
		var imagePath = 'img/list/60.jpeg';
	    $scope.messages = [{
	      face : imagePath,
	      what: 'Brunch this weekend?',
	      who: 'Min Li Chan',
	      when: '3:08PM',
	      notes: " I'll be in your neighborhood doing errands"
	    }, {
	      face : imagePath,
	      what: 'Brunch this weekend?',
	      who: 'Min Li Chan',
	      when: '3:08PM',
	      notes: " I'll be in your neighborhood doing errands"
	    }, {
	      face : imagePath,
	      what: 'Brunch this weekend?',
	      who: 'Min Li Chan',
	      when: '3:08PM',
	      notes: " I'll be in your neighborhood doing errands"
	    }, {
	      face : imagePath,
	      what: 'Brunch this weekend?',
	      who: 'Min Li Chan',
	      when: '3:08PM',
	      notes: " I'll be in your neighborhood doing errands"
	    }, {
	      face : imagePath,
	      what: 'Brunch this weekend?',
	      who: 'Min Li Chan',
	      when: '3:08PM',
	      notes: " I'll be in your neighborhood doing errands"
	    }];
    	
  //$scope.loaded=true;
}]);