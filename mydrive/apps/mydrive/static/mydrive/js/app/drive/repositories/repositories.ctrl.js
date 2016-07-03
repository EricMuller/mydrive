angular.module('my-ged.drive')
  .controller('repositoryCtrl',['$scope','$rootScope','repositories','folders','driveSvc', 'toast', 'alertSvc',
      function  ($scope, $rootScope, repositories, folders,  driveSvc, toast, alertSvc) {
      
        $scope.repositories = repositories ;
        $scope.folders = folders;
        $scope.selectedNode = {};

        $scope.data = {
          repeatSelect: null,
          availableTypes: [
            {id: 1 , code: 'DRVF', name: 'MyDrive File'},
            {id: 2 , code: 'DRVG', name: 'Google Drive'}
          ],
        };

        $scope.parseInt = function(number) {
          return parseInt(number, 10);
        }

        /*remove repository*/
        $scope.removeItem = function (scope) {
         
          var nodeData = scope.$modelValue;
          var node ={
            id: nodeData.id ,
            libelle: nodeData.libelle + '.' + (nodeData.items.length + 1),
            items: []
          };

          driveSvc.removeChild(node).then(function(newNode){
              scope.remove();
          });          

        };

        /*update repository*/
        $scope.updateItem = function (scope) {

            driveSvc.updateChild($scope.selectedNode).then(
                    function(res) {
                        if(res){
                            alertSvc.info($scope.selectedNode.libelle + ' updated.');
                        }else{
                            alertSvc.error($scope.selectedNode.libelle + ' Error.');
                        }
                    });
        };

        

        $scope.selected = function (scope) {
          var nodeData = scope.$modelValue;
          $scope.selectedNode = nodeData;
        };

        $scope.toggle = function (scope) {
          var nodeData = scope.$modelValue;
          $scope.selectedNode = nodeData;
          scope.toggle();
        };

        /*new repository*/
        $scope.newSubItem = function (scope) {
          var nodeData = scope.$modelValue;

          var node ={
            id: nodeData.id,
            libelle: nodeData.libelle + '.' + (nodeData.items.length + 1),
            items: []
          };

          driveSvc.addChild(node).then(function(newNode){
              newNode.items = [];
              nodeData.items.push(newNode);
              toast.showSimpleToast('ok');
          });


        };

        
        /*$scope.treedata = 
        [
            { "label" : "User", "id" : "role1", "children" : [
                { "label" : "subUser1", "id" : "role11", "children" : [] },
                { "label" : "subUser2", "id" : "role12", "children" : [
                    { "label" : "subUser2-1", "id" : "role121", "children" : [
                        { "label" : "subUser2-1-1", "id" : "role1211", "children" : [] },
                        { "label" : "subUser2-1-2", "id" : "role1212", "children" : [] }
                    ]}
                ]}
            ]},
            { "label" : "Admin", "id" : "role2", "children" : [] },
            { "label" : "Guest", "id" : "role3", "children" : [] }
        ];*/ 

        /*function addDirigeant() {
            var modalInstance = $modal.open({
                templateUrl: 'participation/informations/dirigeants/nouveau_dirigeant.tpl.html',
                controller: 'NouveauDirigeantCtrl',
                backdrop: false,
                keyboard: false,
                resolve: {
                    referentiel: function($stateParams, Restangular) {
                        return Restangular.one('referentiels/interlocuteurs').get();
                    }
                }
            });
            modalInstance.result.then(function() {
                $state.reload();
            }, function(err) {
                console.log("Erreur fermeture modale: ", err);
            });
        } */ 

      }

]);