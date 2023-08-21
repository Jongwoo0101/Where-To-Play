const fs = require('fs')

module.exports = {
    devServer: {
        https: true,
        allowedHosts: 'all',
        devMiddleware: {
            publicPath: ''
        },
    },
    pwa: {
      manifestOptions: {
          name: "WhereToPlay",
          short_name: "WhereToPlay",
          start_url: "./public/img/icons/",
          display: "fullscreen",
          theme_color: "#ffffff",
          background_color: "#ffffff",
          icons: [
              {
                  "src": "favicon-16x16.png",
                  "type": "image/png",
                  "sizes": "16x16",
                  "purpose": "any"
              },
              {
                  "src": "favicon-32x32.png",
                  "type": "image/png",
                  "sizes": "32x32",
                  "purpose": "any"
              },
              {
                  "src": "msapplication-icon-144x144.png",
                  "type": "image/png",
                  "sizes": "144x144",
                  "purpose": "any"
              },
              {
                  "src": "mstile-150x150.png",
                  "type": "image/png",
                  "sizes": "150x150",
                  "purpose": "any"
              },
              {
                  "src": "android-chrome-192x192.png",
                  "type": "image/png",
                  "sizes": "192x192",
                  "purpose": "any"
              },
              {
                  "src": "android-chrome-512x512.png",
                  "type": "image/png",
                  "sizes": "512x512",
                  "purpose": "any"
              },
              {
                  "src": "android-chrome-maskable-192x192.png",
                  "type": "image/png",
                  "sizes": "192x192",
                  "purpose": "any"
              },
              {
                  "src": "android-chrome-maskable-512x512.png",
                  "type": "image/png",
                  "sizes": "512x512",
                  "purpose": "any"
              },
              {
                "src": "apple-touch-icon-60x60.png",
                "type": "image/png",
                "sizes": "60x60",
                "purpose": "any"
              },
              {
                "src": "apple-touch-icon-76x76.png",
                "type": "image/png",
                "sizes": "76x76",
                "purpose": "any"
              },
              {
                "src": "apple-touch-icon-120x120.png",
                "type": "image/png",
                "sizes": "120x120",
                "purpose": "any"
              },
              {
                "src": "apple-touch-icon-152x152.png",
                "type": "image/png",
                "sizes": "152x152",
                "purpose": "any"
              },
              {
                "src": "apple-touch-icon-180x180.png",
                "type": "image/png",
                "sizes": "180x180",
                "purpose": "any"
              },
          ],
      },

      themeColor: "#ffffff",
      msTileColor: "#ffffff",
      appleMobileWebAppCapable: "yes",
      appleMobileWebAppStatusBarStyle: "black",
      iconPaths: {
          favicon32: 'img/icons/favicon-32x32.png',
          favicon16: 'img/icons/favicon-16x16.png',
          appleTouchIcon: 'img/icons/apple-touch-icon-152x152.png',
          maskIcon: 'img/icons/safari-pinned-tab.svg',
          msTileImage: 'img/icons/msapplication-icon-144x144.png'
      },
    },
}