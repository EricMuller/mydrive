(function(){
    'use strict';

    angular
        .module('my-ged.documents')
        .service('documentSvc', DocumentSvc);

    DocumentSvc.$inject = ['$rootScope', '$q', 'TokenRestangular'];

    function DocumentSvc( $rootScope , $q, TokenRestangular) {
        var self = this;

        var service = {
            getDocuments: getDocuments,
        };

        return service;

        /*function getDocumentsByFolder(user, id) {
        

           return TokenRestangular.one("v1").one().get({id: id});
        }*/

        function getDocuments(page) {
            
            if (page != undefined) {
                return TokenRestangular.one("files").get({page: page});
            }else{
                return TokenRestangular.one("files").get();     
            }
           
        }        
        
    }

})();
