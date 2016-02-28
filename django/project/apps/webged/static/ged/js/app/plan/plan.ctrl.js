angular.module('my-ged.plan')
  .controller('planCtrl',['$scope','$rootScope','plan','folders','planSvc',

      function  ($scope, $rootScope, plan, folders, planSvc) {
                  
        $rootScope.selectedMenuName('File Plan');

        $scope.removeItem = function (scope) {
         
          var nodeData = scope.$modelValue;
          var node ={
            id: nodeData.id ,
            libelle: nodeData.libelle + '.' + (nodeData.items.length + 1),
            items: []
          };

          planSvc.removeChild(node).then(function(newNode){
              scope.remove();
          });          
          

        };

        $scope.toggle = function (scope) {

          var nodeData = scope.$modelValue;

          console.log(nodeData)

          $scope.selectedNode = nodeData;
          scope.toggle();
        };

        $scope.newSubItem = function (scope) {
          var nodeData = scope.$modelValue;


          var node ={
            id: nodeData.id,
            libelle: nodeData.libelle + '.' + (nodeData.items.length + 1),
            items: []
          };

          planSvc.addChild(node).then(function(newNode){
              newNode.items = [];
              nodeData.items.push(newNode);
          });


        };

        $scope.plan = plan ;
        $scope.folders = folders;
        $scope.selectedNode = {};
        
      }


])