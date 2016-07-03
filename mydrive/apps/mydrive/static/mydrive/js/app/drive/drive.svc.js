(function(){
    'use strict';

    angular
        .module('my-ged.drive')
        .service('driveSvc', PlanSvc);

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
            getDocumentsByFolder: getDocumentsByFolder,
        };

        return service;

        /*root fct*/
        function getFolders() {
           return TokenRestangular.one("v1").one("root").one("repositories").get()  ;      
        }
        
        function getPlan() {
          return TokenRestangular.one("v1").one("root").one("tree").get();
        }

        function getDocumentsByFolder(user, id) {
          
            return TokenRestangular.one("v1").one(user.username).one("repositories",id).one("files").get();
           
        }

        /* user fct*/
        function createPlan(user) {
          var deferred = $q.defer();
           TokenRestangular.all("v1").all(user.username).post({username: user.username}).then(
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

        

        function getBreadCrumb(user) {        
          var deferred = $q.defer();
          TokenRestangular.one("v1").one(user.username).one("tree")
          .get().then(
            function (plan){
                var data = new function (){
                  this.plan = plan;
                  var folders= asMap(plan[0],{});
                  var paths = [];
                  this.breadcrumb=_breadcrumbNode(folders,plan[0],paths);
                }

                deferred.resolve(data);
            }
          );
          return deferred.promise;
        }

        function getTree(user) {
          var deferred = $q.defer();
          TokenRestangular.one("v1").one(user.username).one("tree")
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
           return TokenRestangular.all("v1").one("root").one("repositories",node.id).customDELETE()  ;      
        }

        function addChild(node){
           return TokenRestangular.all("v1").one("root").all("repositories").post(node)  ;      
        }

        function updateChild(repository){
        
          var deferred = $q.defer();
          TokenRestangular.all("v1").one("root").one("repositories",repository.id).all("update").customPUT(repository).then(
                (function(repository) {
                        if(repository){
                            deferred.resolve(true);
                        }else{
                            deferred.resolve(false);
                        }
                    })
                );
          return deferred.promise;
        }


        function _breadcrumbNode(folders,node,paths){

          if(node){
            paths.push(node);
            if(node.parent_id){
              var parent = folders[node.parent_id];
              _breadcrumbNode(folders,parent,paths);
            }
          }
        }

        function breadcrumb(id){
         
          var paths= [];
          var currentNode = this.folders[id];
          if(currentNode){
              _breadcrumbNode(this.folders,currentNode,paths);
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
