(function(){
    'use strict';

  angular.module('my-ged.common', ['restangular', 'ngCookies', 'Postman', 'angularFileUpload', 'angular-loading-bar']	)
  .config(['RestangularProvider', function(RestangularProvider) {
           // RestangularProvider.setBaseUrl('apis/');
           // RestangularProvider.setMethodOverriders(["put", "delete"]);
        }]);

	angular.module('my-ged.common')
  .config(function(RestangularProvider) {
      RestangularProvider.setBaseUrl('/drive/');
      //RestangularProvider.setMethodOverriders(["put", "delete"]);
      RestangularProvider.setRequestSuffix('/?format=json');
      RestangularProvider.setDefaultHeaders({'Content-Type': 'application/json'});
     // AuthRestangular.setDefaultHeaders({'Authorization': 'Token ' + $rootScope.globals.token });
      
	});

 angular.module('my-ged.common')
 .config(['cfpLoadingBarProvider', function(cfpLoadingBarProvider) {
    cfpLoadingBarProvider.spinnerTemplate = '<div><span class="fa fa-spinner">Loading...</div>';
  }]);

  angular.module('my-ged.common')
  .factory("TokenRestangular", function (Restangular, $rootScope, $cookies, alertSvc) {
       return Restangular.withConfig(function (RestangularConfigurer) {
       //var token = $cookies.get('authtoken');
       // Set access token in header.
       RestangularConfigurer.setBaseUrl('/drive/');
       RestangularConfigurer.setRequestSuffix('/?format=json');
       RestangularConfigurer.setDefaultHeaders({'Content-Type': 'application/json'});
       //RestangularConfigurer.setDefaultHeaders({'Authorization': 'Token ' + $rootScope.globals.authtoken });
       //RestangularConfigurer.setDefaultHeaders({'Authorization': 'Token ' + token });
       //$httpProvider.defaults.headers.common['X-CSRFToken'] = $rootScope.globals.csrftoken;
      /* RestangularProvider.setRequestInterceptor(function(elem, operation) {
        if (operation === "remove") {
          return null;
        }
        return elem;
        })
        */
        

    });
})

})();