(function(){
    'use strict';

    angular
        .module('my-ged.login')
        .service('loginSvc', LoginSvc);

    LoginSvc.$inject = ['$rootScope', '$q', 'Restangular' ,'userSvc'];

    function LoginSvc($rootScope, $q, Restangular, userSvc) {

        var self = this;

        var service = {
            signIn: signIn,
            signOut: signOut
        };

        return service;

        function signIn(username,password) {
            
            //$http.post('/api/authenticate', { username: username, password: password })
            //    .success(function (response) {
            //        callback(response);
            //    }); 

            
            return userSvc.getByUsername(username); 
            
            /*$rootScope.$broadcast("connectionStateChanged", {
               someProp: 'signIn OK'     
            });*/

        }

        function signOut() {
        
            $rootScope.$broadcast("connectionStateChanged");
        }

    }

})();
