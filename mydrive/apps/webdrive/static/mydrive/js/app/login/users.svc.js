(function () {
    'use strict';
 
    angular
        .module('my-ged.login')
        .factory('userSvc', UserService);
 
    UserService.$inject = ['Restangular', '$q', '$filter'];

    function UserService(Restangular, $q , $filter) {
        var service = {};
 
        service.getAll = getAll;
        service.getByUsername = getByUsername;
 
        return service;
 
        function getAll() {
            return Restangular.one("users").getList();
        }
 
        function getByUsername(username) {
            //return $http.get('/api/users/' + username).then(handleSuccess, handleError('Error getting user by username'));
            
          /*var deferred = $q.defer();
            var filtered = $filter('filter')(getUsers(), { username: username });
            var user = filtered.length ? filtered[0] : null;
            deferred.resolve(user);
            return deferred.promise;
          */
            var deferred = $q.defer();
            Restangular.one("users").getList().then(function(users){
                var filtered = $filter('filter')(users , { username: username });
                var user = filtered.length ? filtered[0] : null;
                deferred.resolve(user);
            });
            
            return deferred.promise; 
        }
 
        function handleSuccess(res) {
            return res.data;
        }
 
        function handleError(error) {
            return function () {
                return { success: false, message: error };
            };
        }
    }
 
})();