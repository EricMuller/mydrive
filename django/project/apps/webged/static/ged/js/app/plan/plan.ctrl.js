angular.module('my-ged.plan').controller('planCtrl',['$scope','$rootScope',

	
function  ($scope, $rootScope) {
            
  $rootScope.selectedMenuName('File Plan');
  
  $scope.remove = function (scope) {
    scope.remove();
  };

  $scope.toggle = function (scope) {
    scope.toggle();
  };

  $scope.newSubItem = function (scope) {
    var nodeData = scope.$modelValue;
   // debugger
    nodeData.items.push({
      id: nodeData.id * 10 + nodeData.items.length,
      title: nodeData.title + '.' + (nodeData.items.length + 1),
      items: []
    });
  };

$scope.data2=[
      {
        "id": 1,
        "code": "TRAVAIL",
        "title": "Travail",
        "items": []
      },
      ];

  $scope.data=
    [
      {
        "id": 1,
        "code": "TRAVAIL",
        "title": "Travail",
        "items": [
          {
            "id": 11,
            "code": "Contrat",
            "title": "Contrat",
            "items": []
          },
          {
            "id": 12,
            "code": "fiche de paie",
            "title": "Fiches de paie",
            "items": []
          }
        ]
      }
      ,
      {
        "id": 2,
        "title": "Vie courante",
        "code": "Vie courante",
        "items": [
          {
            "id": 21,
            "title": "Factures",
            "items": []
          }
         ]
      },
      {
        "id": 3,
        "title": "Sante",
        "items": [
            {
              "id": 31,
              "title": "Medecin",
              "items": []
            },
            {
              "id": 32,
              "title": "Ophtalmo",
              "items": []
            }
         ]
      }
    ];

}


])