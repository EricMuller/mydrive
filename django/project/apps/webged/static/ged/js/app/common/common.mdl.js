(function(){
    'use strict';

    angular
        .module('my-ged.common', ['restangular'])
        .config(['RestangularProvider', function(RestangularProvider) {
            RestangularProvider.setBaseUrl('rest/');
            RestangularProvider.setMethodOverriders(["put", "delete"]);
        }]);
})();