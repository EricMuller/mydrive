(function(){
    'use strict';

    angular
        .module('my-ged.plan')
        .service('planSvc', PlanSvc);

    PlanSvc.$inject = ['$rootScope', '$q', 'Restangular'];


    function PlanSvc( $rootScope ,$q , Restangular ) {
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

           return Restangular.one("folders").get()  ;      
        }
        
        function getPlan() {

          /* var data = ;
            
           var deferred = $q.defer();

           deferred.resolve(data);

            //return $q.when(data);
           return deferred.promise;
*/
           return Restangular.one("plan").get();

        }

        function removeChild(node){
           
           return Restangular.one("plan",node.id).customDELETE()  ;      

        }

        function addChild(node){
          
          
           return Restangular.all("plan").post(node)  ;      


        }

        function updateChild(parentId,libelle){

        }
        
    }

})();
