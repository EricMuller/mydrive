angular.module('my-ged.upload').controller('uploadCtrl',['$scope','$rootScope','$window',

	function  ($scope, $rootScope,$window) {
            
    $rootScope.selectedMenuName('Upload');
    
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
    
    }

])