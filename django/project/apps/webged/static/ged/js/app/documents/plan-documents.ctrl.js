angular.module('my-ged.documents')
    .controller('plandocumentCtrl',['$scope', '$rootScope', '$window', 'plan',

	function  ($scope, $rootScope, $window, plan) {
    
        $scope.plan = plan;

    }

]);