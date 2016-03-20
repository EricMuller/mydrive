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
            getCurrentUser : getCurrentUser
        };

        var user={
            username:'',
            authtoken:''
        };

        return service;
        

        function getCurrentUser() {
            restoreUser();
            return user;
        }

        function signIn(username,password) {
    
          var deferred = $q.defer();
            
          Restangular.all("authentification").post({ username: username, password: password }).then(
                (function(result) {
                    // $rootScope.status = result.status;
                        if(result){
                            user.username=username;
                            user.authtoken=result.token;
                            storeUser(user);
                            deferred.resolve(true);
                        }else{
                            deferred.resolve(false);
                        }
                    })
                );
            
          return deferred.promise;

        }

        function storeUser(user){
                $cookies.put('username',user.username);
                $cookies.put('authtoken',user.authtoken);
        }
        
        function restoreUser(){
            user.username = $cookies.get('username') || '';
            user.authtoken = $cookies.get('authtoken') || '';
        }

        function signOut() {
            var deferred = $q.defer();
            $cookies.put('authtoken','');
            user.authtoken='';
            deferred.resolve(true);
            return deferred.promise;
        }

    }

})();
