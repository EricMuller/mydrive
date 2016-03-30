

angular.module( "my-ged.login")
    .directive("hideWhenConnected", function ($rootScope) {
    return {
        restrict: 'A',
        link: function (scope, element, attrs) {
            var hideIfConnected = function() {
                if($rootScope.globals.user.authtoken) {
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

angular.module( "my-ged.login")
.directive("showWhenConnected", function ($rootScope) {
    return {
        restrict: 'A',
        link: function (scope, element, attrs) {
            var showIfConnected = function() {
                if($rootScope.globals.user.authtoken) {
                    $(element).show();
                } else {
                    $(element).hide();
                }
            };
 
            showIfConnected();
            scope.$on("loginStateChanged", showIfConnected);
        }
    };
});