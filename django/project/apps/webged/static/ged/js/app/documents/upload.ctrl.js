angular.module('my-ged.documents')
    .controller('uploadCtrl',['$scope','$rootScope','$window','uploaderSvc', 

	function  ($scope, $rootScope, $window, uploaderSvc) {
            
    $rootScope.selectedMenuName('Upload');
    $scope.text ='eee';
    
    $scope.$on('transferComplete', function(event,data) { 
    
        console.log(data);
        if (data.status == '200' ) {
          console.log(data.response);
          var json = JSON.parse(data.response);
          console.log(json); 
          $scope.uploadFiles.push(json); 
        }else{
          //alert(data);
          $window.alert(data.response);
        }
      });

     $scope.document = {
        editMode: true,
        id_type: '',
        date_evenement: parseInt(moment().startOf('day').format('x')),
        isAvenant: false,
        pieces_jointes: null,
        uploader: uploaderSvc.getUploader('rest/participations/', null, 10, null, null, false)
    };
    
     

    }

]);