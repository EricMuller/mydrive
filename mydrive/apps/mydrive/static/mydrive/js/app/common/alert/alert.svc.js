(function(){
    'use strict';

    angular
        .module('my-ged.common')
        .service('alertSvc', AlertSvc);

    AlertSvc.$inject = ['$rootScope', 'postman'];


    function AlertSvc($rootScope, postman) {
      var self = this;

      var service = {
            info: info,
            error: error,
            warning: warning
       };
        
      return service;

      function info(title, body) {
        postman.info(title, body);
      }  
      function error(title, body) {
        postman.error(title, body);
      }  
      function warning(title, body) {
        postman.warning(title, body);
      }  
     }

})();
