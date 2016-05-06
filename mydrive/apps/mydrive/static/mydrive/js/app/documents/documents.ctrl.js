angular.module('my-ged.documents')
    .controller('documentsCtrl',['$scope', '$rootScope', '$window', 'uploaderSvc', 'documents','alertSvc','driveSvc','$state',

	function  ($scope, $rootScope, $window, uploaderSvc, documents, alertSvc, driveSvc, $state) {
    
        $scope.documents =documents;
debugger
		//after upload
        $scope.$on('transferComplete', function(event,data) { 
		        if (data.status == '200' ) {
		          var json = JSON.parse(data.response);
		          alertSvc.info('file '+json.name+' uploaded ');
		          driveSvc.getDocumentsByFolder($rootScope.globals.user, $state.params.id).then(function (documents){

		          		$scope.documents= documents;
		          });
		        }else{
		          alertSvc.error(json);
		        }
      		}
      	);	

    }

]);