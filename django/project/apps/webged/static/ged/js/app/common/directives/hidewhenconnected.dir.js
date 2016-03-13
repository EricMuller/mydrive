

angular.module( "my-ged.common")
    .directive("hideWhenConnected", function ($rootScope) {
    return {
        restrict: 'A',
        link: function (scope, element, attrs) {
            var hideIfConnected = function() {
                if($rootScope.globals.authtoken) {
                    $(element).hide();
                } else {
                    $(element).show();
                }
            };
 
            hideIfConnected();
            scope.$on("loginStateChanged", hideIfConnected);
        }
    };
});