(function () {
    'use strict';
 
    angular.module('app')
    .constant('APP_ROOT', angular.element('#linkAppRoot').attr('href'))
    .config(['$routeProvider', '$httpProvider', '$locationProvider', 

        function ($routeProvider, $httpProvider, $locationProvider) {
 
        function checkLoggedIn($q, $log, authService) {
            var deferred = $q.defer();
 
            if (!authService.isAuthenticated()) {
                $log.log('authentication required. redirect to login');
                deferred.reject({ needsAuthentication: true });
            } else {
                deferred.resolve();
            }
 
            return deferred.promise;
        }
 
        $routeProvider.whenAuthenticated = function (path, route) {
            route.resolve = route.resolve || {};
            angular.extend(route.resolve, { isLoggedIn: ['$q', '$log', 'authService', checkLoggedIn] });
            return $routeProvider.when(path, route);
        }
 
 
        $routeProvider
            .when('/', { redirectTo: '/integrations' })
            .when('/login', { templateUrl: 'app/views/login.html', controller: 'LoginCtrl' })
            .when('/register', { templateUrl: 'app/views/register.html', controller: 'RegisterCtrl' })
            .whenAuthenticated('/integrations', { templateUrl: 'app/views/integrations.html', controller: 'IntegrationsCtrl' })
            .whenAuthenticated('/integration/new/:integrationType', { templateUrl: 'app/views/editIntegration.html', controller: 'EditIntegrationCtrl' })
            .whenAuthenticated('/integration/:integrationType/:integrationId', { templateUrl: 'app/views/editIntegration.html', controller: 'EditIntegrationCtrl' })
            .whenAuthenticated('/activity', { templateUrl: 'app/views/activity.html', controller: 'ActivityCtrl' })
            .whenAuthenticated('/changePassword', { templateUrl: 'app/views/changePassword.html', controller: 'ChangePasswordCtrl' })
            //.whenAuthenticated('/settings', { templateUrl: 'app/views/settings.html', controller: 'SettingsCtrl' })
            .whenAuthenticated('/externalaccounts', { templateUrl: 'app/views/externalAccounts.html', controller: 'ExternalAccountsCtrl' })
            .when('/404', { templateUrl: 'app/views/404.html', controller: 'NotFoundErrorCtrl' })
            .when('/apierror', {templateUrl: 'app/views/apierror.html', controller: 'ApiErrorCtrl' })
            .otherwise({ redirectTo: '/404' });
 
        $httpProvider.interceptors.push('processErrorHttpInterceptor');
    }]);
 
    angular.module('app').run(['$location', '$rootScope', '$log', 'authService', '$route',
        function ($location, $rootScope, $log, authService, $route,) {
 
            $rootScope.$on('$routeChangeError', function (ev, current, previous, rejection) {
                if (rejection && rejection.needsAuthentication === true) {
                    var returnUrl = $location.url();
                    $log.log('returnUrl=' + returnUrl);
                    $location.path('/login').search({ returnUrl: returnUrl });
                }
            });
 
        }]);
 
})();
 