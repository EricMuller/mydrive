angular.module('my-ged.documents')
    .controller('documentsCtrl',['$scope', '$rootScope', '$window', 'uploaderSvc', 'documents',

	function  ($scope, $rootScope, $window, uploaderSvc, documents) {
            
    
        $scope.documents =documents;

    }

]);