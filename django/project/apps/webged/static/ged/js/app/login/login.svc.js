(function(){
    'use strict';

    angular
        .module('my-ged.login')
        .service('loginSvc', LoginSvc);

    LoginSvc.$inject = ['$rootScope', '$q', 'Restangular'];


    function LoginSvc( $rootScope ,$q , Restangular ) {
        var self = this;

        var service = {
            login: login,
            getUsers: getUsers
        };

        return service;

        function login() {

          /* var data = ;
            
           var deferred = $q.defer();

           deferred.resolve(data);

            //return $q.when(data);
           return deferred.promise;
*/
           return Restangular.one("plan").get();
        }

        function getUsers(){

          return Restangular.one("users").get();

        }
    }

})();
