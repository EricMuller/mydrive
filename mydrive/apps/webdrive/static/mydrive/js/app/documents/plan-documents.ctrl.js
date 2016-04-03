angular.module('my-ged.documents')
    .controller('plandocumentCtrl',['$scope', '$rootScope', '$window', 'tree', 'alertSvc', '$state', 'planSvc',

	function  ($scope, $rootScope, $window, tree, alertSvc, $state, planSvc) {
    
    
        $scope.tree = tree;
    
		$scope.folder = {
        	id : $state.params.id
        };

        $scope.navigate = function(id) { 
			$scope.folder.id = id;
			$scope.fbreadcrumb(id);
			$state.go($state.current.name, {id: id});
        }

		$scope.nodeSelected = function(node) { 

			var id = node.id;
			$scope.folder.id = id;
			$scope.fbreadcrumb(id);
			$state.go($state.current.name, {id: id});
			
		};

		$scope.fbreadcrumb = function (id) {
			debugger
			$scope.breadcrumb = $scope.tree.breadcrumb(id);
			$scope.emptyTree =  $.isEmptyObject($scope.tree.folders);
		}

		$scope.getClass = function (strValue) {
            if (strValue == $state.current.name){
                return "active";
            }
        };

		$scope.createPlan = function() { 
		
			var user = $rootScope.globals.user;
			planSvc.createPlan(user).then(function(tree){
				$scope.tree = tree;
				$scope.navigate(0);
			});
			
		};
        
		$scope.fbreadcrumb($state.params.id);

}

]);