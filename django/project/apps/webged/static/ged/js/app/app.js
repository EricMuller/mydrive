  
(function () {
    'use strict';

var app = angular.module('my-ged', ['ngRoute', 'ngCookies', 'mdr.file', 'ui.tree', 'ngMaterial', 'material'
  , 'my-ged.home', 'my-ged.archives', 'my-ged.upload', 'my-ged.plan', 'my-ged.login', 'my-ged.common', 'restangular', 'my-ged.errInterceptor']);

app.config(['$routeProvider',
    function($routeProvider) { 
        // Système de routage
        $routeProvider.otherwise({
            redirectTo: '/home'
        });
        //$locationProvider.html5Mode(true);
    }
]);

/*
app.config(function ($httpProvider) {
    $httpProvider.interceptors.push(function ($location) {
        return {
            'responseError': function (rejection) {
                if (rejection.status === 401) {
                    $location.url('/ged/#/login?returnUrl=' + $location.path());
                }
            }
        };
    });
});

*/
/*
angular.module('my-ged')
.constant('errInterceptorConfig', {
    ERR_500_EVENT: 'event:err500event',
    ERR_400_EVENT: 'event:err400event',
    ERR_401_EVENT: 'event:err401event',
    ERR_403_EVENT: 'event:err403event',
    ERR_408_EVENT: 'event:err408event',
    ERR_418_EVENT: 'event:err418event',
    ERR_REPLAY_EVENT: 'event:errreplayevent',
    ERR_EVENT: 'event:errevent',
});

angular.module('my-ged')
.factory('httpErrorHandler', function ($rootScope, errInterceptorConfig) {
  return {
    'responseError': function (rejection) {
        
      if (rejection.status === 400) {
         $log.log(rejection.status + ' responded');
         $rootScope.$broadcast(errInterceptorConfig.ERR_400_EVENT, rejection.data.message);
      } else {
         $rootScope.$broadcast(errInterceptorConfig.ERR_EVENT, rejection.data.message);
      }
      return $q.reject(rejection);
    }
  };
});

angular.module('my-ged')
.config(function ($httpProvider) {
    $httpProvider.interceptors.push('httpErrorHandler');
});

*/

//
app.filter('searchFor', function(){

	// All filters must return a function. The first parameter
	// is the data that is to be filtered, and the second is an
	// argument that may be passed with a colon (searchFor:searchString)

	return function(arr, searchString){

		if(!searchString){
			return arr;
		}

		var result = [];

		searchString = searchString.toLowerCase();

		// Using the forEach helper method to loop through the array
		angular.forEach(arr, function(item){

			if(item.title.toLowerCase().indexOf(searchString) !== -1){
				result.push(item);
			}

		});

		return result;
	};

});


app.factory('httpPostFactory', function ($http) {
    return function (file, data, callback) {
        $http({
            url: file,
            method: "POST",
            data: data,
            headers: {'Content-Type': undefined}
        }).success(function (response) {
            callback(response);
        });
    };
});

run.$inject = ['$rootScope', '$location', 'loginSvc', '$http'];

function run($rootScope, $location, loginSvc, $http) {
        // keep user logged in after page refresh
        $rootScope.globals={};
        loginSvc.restoreglobals();
        /*if ($rootScope.globals.currentUser) {
            $http.defaults.headers.common['Authorization'] = 'Basic ' + $rootScope.globals.currentUser.authdata; // jshint ignore:line
        }*/

        $rootScope.$on('$locationChangeStart', function (event, next, current) {
            // redirect to login page if not logged in and trying to access a restricted page
            var restrictedPage = $.inArray($location.path(), ['/login', '/register']) === -1;
            var loggedIn = $rootScope.globals.authtoken;
            if (restrictedPage && !loggedIn) {
                $location.path('/login');
            }
        });
    }

app.run(run);

/*
app.run(['$location', '$rootScope', '$log', 'loginSvc', '$route',
        function ($location, $rootScope, $log, loginSvc, $route) {
 
              function handleRouteChangeStart(event, next, current) {
   
                  var returnUrl = $location.url();

                 /* if (!next.allowAnonymous && !authService.isAuthenticated()) {
                      $log.log('authentication required. redirect to login');
   
                      var returnUrl = $location.url();
                      $log.log('returnUrl=' + returnUrl);
   
                      //TODO: BUG -> THIS IS NOT PREVENTING THE CURRENT ROUTE
                      //This has a side effect, which is load of the controller/view configured to the route
                      //The redirect to login occurs later.
                      //Possible solutions: 
                      // 1 - use $locationChangeStart (it is hard to get the route being used)
                      // 2 - Use a resolver in controller, returning a promise, and reject when needs auth
                      event.preventDefault();
                  */
  /*                console.log('handleRouteChangeStart'+returnUrl);
                  event.preventDefault();
                  $location.path('/login').search({ returnUrl: returnUrl })
                  
                  }

              $rootScope.$on('$routeChangeStart', handleRouteChangeStart);
             
 
        }]);
*/
/*
http://docs.angularjs.org/api/ng.$interpolateProvider
app.config(function($interpolateProvider) {
$interpolateProvider.startSymbol('{[{');
$interpolateProvider.endSymbol('}]}');
});
*/

})();