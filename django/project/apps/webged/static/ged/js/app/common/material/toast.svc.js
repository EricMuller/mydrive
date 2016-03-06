(function(){
    'use strict';

    angular
        .module('material')
        .service('toast', ToastSvc);

    ToastSvc.$inject = ['$rootScope','$mdToast'];


    function ToastSvc($rootScope, $mdToast) {
        var self = this;

        var service = {
            showSimpleToast: showSimpleToast
        };
        
        var last = {
            bottom: false,
            top: true,
            left: false,
            right: true
        };

       self.toastPosition = angular.extend({},last);
        
       return service;

        function sanitizePosition() {
          debugger
            var current = self.toastPosition;
            if ( current.bottom && last.top ) current.top = false;
            if ( current.top && last.bottom ) current.bottom = false;
            if ( current.right && last.left ) current.left = false;
            if ( current.left && last.right ) current.right = false;
            last = angular.extend({},current);
        }

        function getToastPosition() {
              sanitizePosition();
              return Object.keys(self.toastPosition)
              .filter(function(pos) { return self.toastPosition[pos]; })
              .join(' ');

        };

        function showSimpleToast(mess) {
         
            $mdToast.show(
                $mdToast.simple()
                .textContent(mess)
                .position(getToastPosition())
              .hideDelay(3000)
              );
        }    
     }

})();
