angular.module('my-ged.documents')
    .controller('plandocumentCtrl',['$scope', '$rootScope', '$window', 'tree', 'alertSvc', '$state', 'planSvc',

	function  ($scope, $rootScope, $window, tree, alertSvc, $state, planSvc) {
    
        $scope.tree = tree;
        $scope.breadcrumb = tree.breadcrumb($state.params.id);
		$scope.folder = {
        	id : $state.params.id
        };

        $scope.currentView= 'documents.documents';

        $scope.navigate = function(id) { 
			$scope.folder.id = id;
			$scope.breadcrumb = tree.breadcrumb(id);
			$state.go($state.current.name, {id: id});
        }

		$scope.selectNode = function(plan) { 
			var id = plan.currentNode.id;
			$scope.folder.id = id;
			$scope.breadcrumb = tree.breadcrumb(id);
			$state.go($state.current.name, {id: id});
			
		};

		 $scope.getClass = function (strValue) {
            if (strValue == $state.current.name){
                return "active";
            }
        }

}

]);