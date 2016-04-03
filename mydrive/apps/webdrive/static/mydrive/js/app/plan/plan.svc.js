(function(){
    'use strict';

    angular
        .module('my-ged.plan')
        .service('planSvc', PlanSvc);

    PlanSvc.$inject = ['$rootScope', '$q', 'TokenRestangular'];


    function PlanSvc( $rootScope , $q, TokenRestangular) {
        var self = this;

        var service = {
            getPlan: getPlan,
            createPlan: createPlan,
            getTree: getTree,
            getFolders: getFolders,
            addChild: addChild,
            updateChild: updateChild,
            removeChild: removeChild,
            breadcrumb: breadcrumb,
        };

        return service;

        function getFolders() {
           return TokenRestangular.one("folders").get()  ;      
        }
        
        function createPlan(user) {
          var deferred = $q.defer();
           TokenRestangular.all("plan").post({username: user.username}).then(
            function (plan){
                var data = new function (){
                  this.plan = plan;
                  this.folders= asMap(plan[0],{});
                  this.breadcrumb = breadcrumb;
                }

                deferred.resolve(data);
            }
          );
          return deferred.promise;
        }

        function getPlan() {
          return TokenRestangular.one("plan").get();
        }

        function getTree(user) {
          var deferred = $q.defer();
          TokenRestangular.one("plan").one(user.username).one("plan")
          .get().then(
            function (plan){
                var data = new function (){
                  this.plan = plan;
                  this.folders= asMap(plan[0],{});
                  this.breadcrumb = breadcrumb;
                }

                deferred.resolve(data);
            }
          );
          return deferred.promise;
        }


        function removeChild(node){
           return TokenRestangular.all("plan").one("folders",node.id).customDELETE()  ;      
        }

        function addChild(node){
           return TokenRestangular.all("plan").all("folders").post(node)  ;      
        }

        function updateChild(parentId,libelle){

        }

        function breadcrumbNode(folders,node,paths){

          if(node){
            paths.push(node);
            if(node.parent_id){
              var parent = folders[node.parent_id];
              breadcrumbNode(folders,parent,paths);
            }
          }
        }

        function breadcrumb(id){

          var paths= [];
          
           var currentNode = this.folders[id];
           if(currentNode){
              breadcrumbNode(this.folders,currentNode,paths);
           }
           return paths.reverse();
        }

        function asMap (node,map){
          if(node ){
            map[node.id] = node;
            if(node.items){
              for (var i = node.items.length - 1; i >= 0; i--) {
                asMap(node.items[i],map);
              }
            }
          }
          return map;
        }



        
    }

})();
