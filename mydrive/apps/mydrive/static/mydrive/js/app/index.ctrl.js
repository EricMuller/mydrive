	
angular.module('my-ged')
.controller('indexCtrl',['$scope', '$rootScope', '$timeout', '$mdSidenav', '$log', 'loginSvc', 'alertSvc'
							, 'errInterceptorConfig', '$location', 'driveSvc', '$state', '$websocket',

	function($scope, $rootScope, $timeout, $mdSidenav, $log, loginSvc, alertSvc, errInterceptorConfig, $location, driveSvc, $state , $websocket) {
		
		$rootScope.selectedMenuName= function(title){
			$rootScope.selectedMenu=title;
		//	$('#title').text(title);
		};
		
		$rootScope.selectedMenuName('Mon drive');
		$scope.uploadFiles = [];

		$scope.$on('connectionStateChanged', function (event, data) {
  				console.log(data); 
		});
		

		$rootScope.$on('$stateChangeSuccess', function (ev, to, toParams, from, fromParams) {

			 $scope.currentState ={
			 	to : to,
			 	params : toParams,
			 };
			 var link = $scope.getLinkUrl();
			 if(link){
				$scope.documentState= link;
			 }
			 
		});

		$scope.plan = '';
		$scope.currentState = {};
		$scope.documentState = $state.href('documents.documents', {id: 0 });
		
		
		$scope.getDocumentState = function() {		
			return $scope.documentState ;
		}

		$scope.getLinkUrl = function() {
			
			
			if ($scope.currentState.to){
				if ($scope.currentState.to.name.indexOf('documentState') === 0 ){
					return $state.href($scope.currentState.to.name, {id: $scope.currentState.params.id });
				}

			}	
  			return '';
		};

		//
		
		$rootScope.$on(errInterceptorConfig.ERR_500_EVENT, interceptError);
    	$rootScope.$on(errInterceptorConfig.ERR_408_EVENT, interceptError);
    	$rootScope.$on(errInterceptorConfig.ERR_403_EVENT, interceptError);
    	$rootScope.$on(errInterceptorConfig.ERR_401_EVENT, interceptError);
    	$rootScope.$on(errInterceptorConfig.ERR_400_EVENT, interceptError);
    	$rootScope.$on(errInterceptorConfig.ERR_EVENT, interceptError);


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

		$scope.messages = [];
 		var protocol = 'chat';

		var ws = $websocket.$new({'url': 'ws://127.0.0.1:8000/ws', 'protocols': [], 'subprotocols': ['base46'] });
        $scope.ws= ws;

        ws.$on('$open', function () {
            console.log('Oh my gosh, websocket is really OPEN! Fukken awesome!');
            ws.$emit('ping', 'PING hi listening websocket server'); // send a message to the websocket server
        });

        ws.$on('pong', function (message) {
            console.log('The server has sent the following data:');
            console.log(message);
            $scope.messages.push(message);
            $scope.$apply();
            //ws.$close();
        });

        ws.$on('$close', function () {
            console.log('Noooooooooou,  Websocket CLOSE , damn it!');
        });

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