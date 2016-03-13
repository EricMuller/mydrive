(function(){
    'use strict';

    angular
        .module('my-ged.login')
        .service('loginSvc', LoginSvc);

    LoginSvc.$inject = ['$rootScope', '$q', 'Restangular' ,'userSvc','$cookies'];

    function LoginSvc($rootScope, $q, Restangular, userSvc, $cookies) {

        var self = this;

        var service = {
            signIn: signIn,
            signOut: signOut,
            restoreglobals : restoreglobals
        };

        return service;

        function signIn(username,password) {
            
           /* $http.post('/api/authenticate', { username: username, password: password })
                .success(function (response) {
                    callback(response);
                }); 
            */
          //  return Restangular.all("authentification").post({ username: username, password: password })  ;      

    
          var deferred = $q.defer();
            
          Restangular.all("authentification").post({ username: username, password: password }).then(
                (function(result) {
                    // $rootScope.status = result.status;
                    if(result){
                        $cookies.put('authtoken',result.token);
                        $cookies.put('username',username);
                        restoreglobals();
                        deferred.resolve(true);
                        $rootScope.$broadcast("loginStateChanged", {
                            someProp: 'signIn OK'     
                        });
                    }else{
                        deferred.resolve(false);
                    }

                    })
                );
            
          return deferred.promise;
            
            

        }

        function restoreglobals(){
            $rootScope.globals.username = $cookies.get('username') || {};
            $rootScope.globals.authtoken = $cookies.get('authtoken') || {};

        }

        function signOut() {
            $cookies.put('authtoken','');
            $rootScope.globals.authtoken = '';            
            $rootScope.$broadcast("loginStateChanged");
        }

    }

})();
