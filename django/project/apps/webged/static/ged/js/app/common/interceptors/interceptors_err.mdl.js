(function(){

'use strict';
angular.module('my-ged.errInterceptor', []);

angular.module('my-ged.errInterceptor')
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

angular.module('my-ged.errInterceptor')
.factory('httpErrorHandler', function ($rootScope, errInterceptorConfig, $q, alertSvc) {
  return {
    'responseError': function (rejection) {
      if (rejection.status === 400) {
         //$log.log(rejection.status + ' responded');
         $rootScope.$broadcast(errInterceptorConfig.ERR_400_EVENT, rejection.data);
      } else {
         $rootScope.$broadcast(errInterceptorConfig.ERR_EVENT, rejection.data);
      }
      return $q.reject(rejection);
    }
  };
});

angular.module('my-ged.errInterceptor')
.config(function ($httpProvider) {
    $httpProvider.interceptors.push('httpErrorHandler');
});

})();