---
layout: post
title:  Vue http request settings
created: 2017-10-21 15:57:20 +08:00
modified: 2017-10-21 16:31:46 +08:00
tags: [Vue]
---


#### Step 1: install axios

```
$ npm install --save axios
```


#### Step 2: config files

```
// config/index.js
module.exports = {
  dev: {
    proxyTable: {
      '/api': {
        target: 'https://www.somewhere.com',
        changeOrigin: true,
        pathRewrite: {
          '^/api': '/api'
        }
      }
    },
  ...

// src/main.js
import axios from 'axios'
Vue.prototype.$http = axios

// use
  methods: {
    hello: function (event) {
      this.$http.get('/hello').then(function (res) {
        console.log(res)
      })
    }
  }
```
