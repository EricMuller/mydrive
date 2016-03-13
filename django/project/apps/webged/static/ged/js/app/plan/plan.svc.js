(function(){
    'use strict';

    angular
        .module('my-ged.plan')
        .service('planSvc', PlanSvc);

    PlanSvc.$inject = ['$rootScope', '$q', 'TokenRestangular'];


    function PlanSvc( $rootScope , $q, TokenRestangular) {
        var self = this;

        var service = {
            getPlan: getPlan,
            getFolders: getFolders,
            addChild: addChild,
            updateChild: updateChild,
            removeChild: removeChild
        };

        return service;

        function getFolders() {
           return TokenRestangular.one("folders").get()  ;      
        }
        
        function getPlan() {

          /* var data = ;
            
           var deferred = $q.defer();

           deferred.resolve(data);

            //return $q.when(data);
           return deferred.promise;
*/
           return TokenRestangular.one("plan").get();
        }

        function removeChild(node){
           return TokenRestangular.one("plan",node.id).customDELETE()  ;      
        }

        function addChild(node){
           return TokenRestangular.all("plan").post(node)  ;      
        }

        function updateChild(parentId,libelle){

        }
        
    }

})();
