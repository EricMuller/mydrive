(function(){
    'use strict';

    angular
      .module('my-ged.common', ['restangular']	)
      .config(['RestangularProvider', function(RestangularProvider) {
           // RestangularProvider.setBaseUrl('apis/');
           // RestangularProvider.setMethodOverriders(["put", "delete"]);
        }]);

})();