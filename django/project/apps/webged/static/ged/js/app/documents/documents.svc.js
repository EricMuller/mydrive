(function(){
    'use strict';

    angular
        .module('my-ged.documents')
        .service('documentSvc', DocumentSvc);

    DocumentSvc.$inject = ['$rootScope', '$q', 'TokenRestangular'];

    function DocumentSvc( $rootScope , $q, TokenRestangular) {
        var self = this;

        var service = {
            getDocumentsByFolder: getDocumentsByFolder,
            getDocuments: getDocuments
        };

        return service;

        function getDocumentsByFolder(id) {
           return TokenRestangular.one("documents").get({id: id});
        }

        function getDocuments() {
           return TokenRestangular.one("documents").get();
        }        
        
    }

})();
