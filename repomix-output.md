This file is a merged representation of the entire codebase, combined into a single document by Repomix.

# File Summary

## Purpose
This file contains a packed representation of the entire repository's contents.
It is designed to be easily consumable by AI systems for analysis, code review,
or other automated processes.

## File Format
The content is organized as follows:
1. This summary section
2. Repository information
3. Directory structure
4. Repository files (if enabled)
5. Multiple file entries, each consisting of:
  a. A header with the file path (## File: path/to/file)
  b. The full contents of the file in a code block

## Usage Guidelines
- This file should be treated as read-only. Any changes should be made to the
  original repository files, not this packed version.
- When processing this file, use the file path to distinguish
  between different files in the repository.
- Be aware that this file may contain sensitive information. Handle it with
  the same level of security as you would the original repository.

## Notes
- Some files may have been excluded based on .gitignore rules and Repomix's configuration
- Binary files are not included in this packed representation. Please refer to the Repository Structure section for a complete list of file paths, including binary files
- Files matching patterns in .gitignore are excluded
- Files matching default ignore patterns are excluded
- Files are sorted by Git change count (files with more changes are at the bottom)

# Directory Structure
```
backend/
  alembic/
    versions/
      3d77d5196130_add_phone_and_avatar_to_users.py
      d129ebf1174b_add_payments_table_model_sync.py
      ec78b9a97891_add_storefront_models_and_relations.py
    env.py
    README
    script.py.mako
  app/
    api/
      routes/
        auth.py
        cart.py
        categories.py
        checkout.py
        customer_auth.py
        customer_order.py
        customer_profiles.py
        order_items.py
        orders.py
        payments.py
        permissions.py
        product_categories.py
        product_variants.py
        products.py
        reviews.py
        role_permissions.py
        roles.py
        users.py
        wishlist.py
    core/
      auth.py
      cart_helpers.py
      config.py
      email.py
      jwt.py
      permissions.py
      security.py
      test_seed.py
    database/
      base.py
      session.py
    models/
      __init__.py
      address.py
      cart_item.py
      cart.py
      category.py
      coupon.py
      customer_order.py
      customer_profile.py
      order_item.py
      order.py
      payment.py
      permission.py
      product_category.py
      product_variant.py
      product.py
      return_request.py
      review.py
      role_permission.py
      role.py
      user.py
      wishlist.py
    repositories/
      cart_repository.py
    schemas/
      __init__.py
      address.py
      auth.py
      cart.py
      category.py
      customer_auth.py
      customer_order.py
      customer_profile.py
      order_item.py
      order.py
      permission.py
      product_category.py
      product_variant.py
      product.py
      review.py
      role_permission.py
      role.py
      user.py
      wishlist.py
    main.py
    seed.py
  tests/
    __init__.py
    conftest.py
    test_checkout.py
    test_customer_auth.py
    test_customer_order.py
    test_customer_profiles.py
    test_payments.py
    test_reviews.py
    test_wishlist.py
  .dockerignore
  alembic.ini
  Dockerfile
  pytest.ini
  requirements-dev.txt
  requirements.txt
frontend/
  .claude/
    rules/
      guardrails.md
  .github/
    copilot-instructions.md
  app/
    (auth)/
      forgot-password/
        page.tsx
      login/
        page.tsx
      register/
        page.tsx
      reset-password/
        page.tsx
      verify-email/
        page.tsx
      layout.tsx
    (protected)/
      account/
        page.tsx
      addresses/
        page.tsx
      chat-history/
        page.tsx
      checkout/
        order-confirmation/
          [orderId]/
            page.tsx
        page.tsx
      notifications/
        page.tsx
      orders/
        [orderId]/
          return/
            page.tsx
          page.tsx
        page.tsx
      profile/
        page.tsx
      settings/
        page.tsx
      wishlist/
        page.tsx
      layout.tsx
    (public)/
      about/
        page.tsx
      cart/
        page.tsx
      categories/
        [slug]/
          page.tsx
        page.tsx
      contact/
        page.tsx
      faq/
        page.tsx
      privacy/
        page.tsx
      products/
        [slug]/
          loading.tsx
          page.tsx
        loading.tsx
        page.tsx
      return-policy/
        page.tsx
      search/
        page.tsx
      terms/
        page.tsx
      layout.tsx
      loading.tsx
      page.tsx
    api/
      auth/
        login/
          route.ts
        logout/
          route.ts
      checkout/
        create-payment-intent/
          route.ts
      webhooks/
        stripe/
          route.ts
    error.tsx
    globals.css
    layout.tsx
    not-found.tsx
    page.tsx
    robots.ts
    sitemap.ts
  e2e/
    auth.spec.ts
    checkout.spec.ts
    phase1-checkpoint.spec.ts
  hooks/
    useDebouncedValue.ts
    useOrderStatusPolling.ts
    useWebSocket.ts
  lib/
    api/
      auth.ts
      cart.ts
      client.ts
      notifications.ts
      orders.ts
      products.ts
      reviews.ts
      users.ts
      wishlist.ts
    stores/
      authStore.ts
      cartStore.ts
      checkoutStore.ts
      notificationStore.ts
      wishlistStore.ts
    stripe/
      client.ts
      paymentIntent.ts
    utils/
      format.ts
    validation/
      address.ts
      auth.ts
      contact.ts
      review.ts
    websocket/
      chatConnection.ts
      connectionManager.ts
  tests/
    smoke.test.tsx
  types/
    address.ts
    api.ts
    auth.ts
    cart.ts
    category.ts
    chats.ts
    notification.ts
    order.ts
    product.ts
    review.ts
    role.ts
    user.ts
    wishlist.ts
  .env.example
  .prettierrc
  eslint.config.mjs
  gitignore
  jest.config.ts
  jest.setup.ts
  next.config.ts
  package.json
  playwright.config.ts
  postcss.config.js
  PROGRESS.md
  proxy.ts
  tsconfig.jest.json
  tsconfig.json
  tsconfig.tsbuildinfo
  update_progress.py
.gitignore
package.json
```

# Files

## File: frontend/tsconfig.tsbuildinfo
````
{"fileNames":["./node_modules/typescript/lib/lib.es5.d.ts","./node_modules/typescript/lib/lib.es2015.d.ts","./node_modules/typescript/lib/lib.es2016.d.ts","./node_modules/typescript/lib/lib.es2017.d.ts","./node_modules/typescript/lib/lib.es2018.d.ts","./node_modules/typescript/lib/lib.es2019.d.ts","./node_modules/typescript/lib/lib.es2020.d.ts","./node_modules/typescript/lib/lib.es2021.d.ts","./node_modules/typescript/lib/lib.es2022.d.ts","./node_modules/typescript/lib/lib.es2023.d.ts","./node_modules/typescript/lib/lib.es2024.d.ts","./node_modules/typescript/lib/lib.esnext.d.ts","./node_modules/typescript/lib/lib.dom.d.ts","./node_modules/typescript/lib/lib.dom.iterable.d.ts","./node_modules/typescript/lib/lib.es2015.core.d.ts","./node_modules/typescript/lib/lib.es2015.collection.d.ts","./node_modules/typescript/lib/lib.es2015.generator.d.ts","./node_modules/typescript/lib/lib.es2015.iterable.d.ts","./node_modules/typescript/lib/lib.es2015.promise.d.ts","./node_modules/typescript/lib/lib.es2015.proxy.d.ts","./node_modules/typescript/lib/lib.es2015.reflect.d.ts","./node_modules/typescript/lib/lib.es2015.symbol.d.ts","./node_modules/typescript/lib/lib.es2015.symbol.wellknown.d.ts","./node_modules/typescript/lib/lib.es2016.array.include.d.ts","./node_modules/typescript/lib/lib.es2016.intl.d.ts","./node_modules/typescript/lib/lib.es2017.arraybuffer.d.ts","./node_modules/typescript/lib/lib.es2017.date.d.ts","./node_modules/typescript/lib/lib.es2017.object.d.ts","./node_modules/typescript/lib/lib.es2017.sharedmemory.d.ts","./node_modules/typescript/lib/lib.es2017.string.d.ts","./node_modules/typescript/lib/lib.es2017.intl.d.ts","./node_modules/typescript/lib/lib.es2017.typedarrays.d.ts","./node_modules/typescript/lib/lib.es2018.asyncgenerator.d.ts","./node_modules/typescript/lib/lib.es2018.asynciterable.d.ts","./node_modules/typescript/lib/lib.es2018.intl.d.ts","./node_modules/typescript/lib/lib.es2018.promise.d.ts","./node_modules/typescript/lib/lib.es2018.regexp.d.ts","./node_modules/typescript/lib/lib.es2019.array.d.ts","./node_modules/typescript/lib/lib.es2019.object.d.ts","./node_modules/typescript/lib/lib.es2019.string.d.ts","./node_modules/typescript/lib/lib.es2019.symbol.d.ts","./node_modules/typescript/lib/lib.es2019.intl.d.ts","./node_modules/typescript/lib/lib.es2020.bigint.d.ts","./node_modules/typescript/lib/lib.es2020.date.d.ts","./node_modules/typescript/lib/lib.es2020.promise.d.ts","./node_modules/typescript/lib/lib.es2020.sharedmemory.d.ts","./node_modules/typescript/lib/lib.es2020.string.d.ts","./node_modules/typescript/lib/lib.es2020.symbol.wellknown.d.ts","./node_modules/typescript/lib/lib.es2020.intl.d.ts","./node_modules/typescript/lib/lib.es2020.number.d.ts","./node_modules/typescript/lib/lib.es2021.promise.d.ts","./node_modules/typescript/lib/lib.es2021.string.d.ts","./node_modules/typescript/lib/lib.es2021.weakref.d.ts","./node_modules/typescript/lib/lib.es2021.intl.d.ts","./node_modules/typescript/lib/lib.es2022.array.d.ts","./node_modules/typescript/lib/lib.es2022.error.d.ts","./node_modules/typescript/lib/lib.es2022.intl.d.ts","./node_modules/typescript/lib/lib.es2022.object.d.ts","./node_modules/typescript/lib/lib.es2022.string.d.ts","./node_modules/typescript/lib/lib.es2022.regexp.d.ts","./node_modules/typescript/lib/lib.es2023.array.d.ts","./node_modules/typescript/lib/lib.es2023.collection.d.ts","./node_modules/typescript/lib/lib.es2023.intl.d.ts","./node_modules/typescript/lib/lib.es2024.arraybuffer.d.ts","./node_modules/typescript/lib/lib.es2024.collection.d.ts","./node_modules/typescript/lib/lib.es2024.object.d.ts","./node_modules/typescript/lib/lib.es2024.promise.d.ts","./node_modules/typescript/lib/lib.es2024.regexp.d.ts","./node_modules/typescript/lib/lib.es2024.sharedmemory.d.ts","./node_modules/typescript/lib/lib.es2024.string.d.ts","./node_modules/typescript/lib/lib.esnext.array.d.ts","./node_modules/typescript/lib/lib.esnext.collection.d.ts","./node_modules/typescript/lib/lib.esnext.intl.d.ts","./node_modules/typescript/lib/lib.esnext.disposable.d.ts","./node_modules/typescript/lib/lib.esnext.promise.d.ts","./node_modules/typescript/lib/lib.esnext.decorators.d.ts","./node_modules/typescript/lib/lib.esnext.iterator.d.ts","./node_modules/typescript/lib/lib.esnext.float16.d.ts","./node_modules/typescript/lib/lib.esnext.error.d.ts","./node_modules/typescript/lib/lib.esnext.sharedmemory.d.ts","./node_modules/typescript/lib/lib.decorators.d.ts","./node_modules/typescript/lib/lib.decorators.legacy.d.ts","./node_modules/@types/react/global.d.ts","./node_modules/csstype/index.d.ts","./node_modules/@types/react/index.d.ts","./node_modules/next/dist/styled-jsx/types/css.d.ts","./node_modules/next/dist/styled-jsx/types/macro.d.ts","./node_modules/next/dist/styled-jsx/types/style.d.ts","./node_modules/next/dist/styled-jsx/types/global.d.ts","./node_modules/next/dist/styled-jsx/types/index.d.ts","./node_modules/next/dist/server/get-page-files.d.ts","./node_modules/@types/node/compatibility/disposable.d.ts","./node_modules/@types/node/compatibility/indexable.d.ts","./node_modules/@types/node/compatibility/iterators.d.ts","./node_modules/@types/node/compatibility/index.d.ts","./node_modules/@types/node/globals.typedarray.d.ts","./node_modules/@types/node/buffer.buffer.d.ts","./node_modules/@types/node/globals.d.ts","./node_modules/@types/node/web-globals/abortcontroller.d.ts","./node_modules/@types/node/web-globals/domexception.d.ts","./node_modules/@types/node/web-globals/events.d.ts","./node_modules/undici-types/header.d.ts","./node_modules/undici-types/readable.d.ts","./node_modules/undici-types/file.d.ts","./node_modules/undici-types/fetch.d.ts","./node_modules/undici-types/formdata.d.ts","./node_modules/undici-types/connector.d.ts","./node_modules/undici-types/client.d.ts","./node_modules/undici-types/errors.d.ts","./node_modules/undici-types/dispatcher.d.ts","./node_modules/undici-types/global-dispatcher.d.ts","./node_modules/undici-types/global-origin.d.ts","./node_modules/undici-types/pool-stats.d.ts","./node_modules/undici-types/pool.d.ts","./node_modules/undici-types/handlers.d.ts","./node_modules/undici-types/balanced-pool.d.ts","./node_modules/undici-types/agent.d.ts","./node_modules/undici-types/mock-interceptor.d.ts","./node_modules/undici-types/mock-agent.d.ts","./node_modules/undici-types/mock-client.d.ts","./node_modules/undici-types/mock-pool.d.ts","./node_modules/undici-types/mock-errors.d.ts","./node_modules/undici-types/proxy-agent.d.ts","./node_modules/undici-types/env-http-proxy-agent.d.ts","./node_modules/undici-types/retry-handler.d.ts","./node_modules/undici-types/retry-agent.d.ts","./node_modules/undici-types/api.d.ts","./node_modules/undici-types/interceptors.d.ts","./node_modules/undici-types/util.d.ts","./node_modules/undici-types/cookies.d.ts","./node_modules/undici-types/patch.d.ts","./node_modules/undici-types/websocket.d.ts","./node_modules/undici-types/eventsource.d.ts","./node_modules/undici-types/filereader.d.ts","./node_modules/undici-types/diagnostics-channel.d.ts","./node_modules/undici-types/content-type.d.ts","./node_modules/undici-types/cache.d.ts","./node_modules/undici-types/index.d.ts","./node_modules/@types/node/web-globals/fetch.d.ts","./node_modules/@types/node/assert.d.ts","./node_modules/@types/node/assert/strict.d.ts","./node_modules/@types/node/async_hooks.d.ts","./node_modules/@types/node/buffer.d.ts","./node_modules/@types/node/child_process.d.ts","./node_modules/@types/node/cluster.d.ts","./node_modules/@types/node/console.d.ts","./node_modules/@types/node/constants.d.ts","./node_modules/@types/node/crypto.d.ts","./node_modules/@types/node/dgram.d.ts","./node_modules/@types/node/diagnostics_channel.d.ts","./node_modules/@types/node/dns.d.ts","./node_modules/@types/node/dns/promises.d.ts","./node_modules/@types/node/domain.d.ts","./node_modules/@types/node/events.d.ts","./node_modules/@types/node/fs.d.ts","./node_modules/@types/node/fs/promises.d.ts","./node_modules/@types/node/http.d.ts","./node_modules/@types/node/http2.d.ts","./node_modules/@types/node/https.d.ts","./node_modules/@types/node/inspector.generated.d.ts","./node_modules/@types/node/module.d.ts","./node_modules/@types/node/net.d.ts","./node_modules/@types/node/os.d.ts","./node_modules/@types/node/path.d.ts","./node_modules/@types/node/perf_hooks.d.ts","./node_modules/@types/node/process.d.ts","./node_modules/@types/node/punycode.d.ts","./node_modules/@types/node/querystring.d.ts","./node_modules/@types/node/readline.d.ts","./node_modules/@types/node/readline/promises.d.ts","./node_modules/@types/node/repl.d.ts","./node_modules/@types/node/sea.d.ts","./node_modules/@types/node/stream.d.ts","./node_modules/@types/node/stream/promises.d.ts","./node_modules/@types/node/stream/consumers.d.ts","./node_modules/@types/node/stream/web.d.ts","./node_modules/@types/node/string_decoder.d.ts","./node_modules/@types/node/test.d.ts","./node_modules/@types/node/timers.d.ts","./node_modules/@types/node/timers/promises.d.ts","./node_modules/@types/node/tls.d.ts","./node_modules/@types/node/trace_events.d.ts","./node_modules/@types/node/tty.d.ts","./node_modules/@types/node/url.d.ts","./node_modules/@types/node/util.d.ts","./node_modules/@types/node/v8.d.ts","./node_modules/@types/node/vm.d.ts","./node_modules/@types/node/wasi.d.ts","./node_modules/@types/node/worker_threads.d.ts","./node_modules/@types/node/zlib.d.ts","./node_modules/@types/node/index.d.ts","./node_modules/@types/react/canary.d.ts","./node_modules/@types/react/experimental.d.ts","./node_modules/@types/react-dom/index.d.ts","./node_modules/@types/react-dom/canary.d.ts","./node_modules/@types/react-dom/experimental.d.ts","./node_modules/next/dist/lib/fallback.d.ts","./node_modules/next/dist/compiled/webpack/webpack.d.ts","./node_modules/next/dist/shared/lib/modern-browserslist-target.d.ts","./node_modules/next/dist/shared/lib/entry-constants.d.ts","./node_modules/next/dist/shared/lib/constants.d.ts","./node_modules/next/dist/lib/bundler.d.ts","./node_modules/next/dist/server/config.d.ts","./node_modules/next/dist/lib/load-custom-routes.d.ts","./node_modules/next/dist/shared/lib/image-config.d.ts","./node_modules/next/dist/build/webpack/plugins/subresource-integrity-plugin.d.ts","./node_modules/next/dist/server/body-streams.d.ts","./node_modules/next/dist/server/request/search-params.d.ts","./node_modules/next/dist/shared/lib/segment-cache/vary-params-decoding.d.ts","./node_modules/next/dist/server/app-render/vary-params.d.ts","./node_modules/next/dist/server/request/params.d.ts","./node_modules/next/dist/server/route-kind.d.ts","./node_modules/next/dist/server/route-definitions/route-definition.d.ts","./node_modules/next/dist/server/route-matches/route-match.d.ts","./node_modules/next/dist/client/components/app-router-headers.d.ts","./node_modules/next/dist/server/lib/cache-control.d.ts","./node_modules/next/dist/shared/lib/app-router-types.d.ts","./node_modules/next/dist/server/lib/cache-handlers/types.d.ts","./node_modules/next/dist/server/use-cache/use-cache-wrapper.d.ts","./node_modules/next/dist/server/resume-data-cache/cache-store.d.ts","./node_modules/next/dist/server/resume-data-cache/resume-data-cache.d.ts","./node_modules/next/dist/lib/constants.d.ts","./node_modules/next/dist/server/render-result.d.ts","./node_modules/next/dist/server/response-cache/types.d.ts","./node_modules/next/dist/server/response-cache/index.d.ts","./node_modules/@types/react/jsx-runtime.d.ts","./node_modules/next/dist/next-devtools/userspace/pages/pages-dev-overlay-setup.d.ts","./node_modules/next/dist/build/static-paths/types.d.ts","./node_modules/next/dist/server/route-definitions/app-page-route-definition.d.ts","./node_modules/next/dist/build/adapter/setup-node-env.external.d.ts","./node_modules/next/dist/server/instrumentation/types.d.ts","./node_modules/next/dist/lib/setup-exception-listeners.d.ts","./node_modules/next/dist/lib/worker.d.ts","./node_modules/next/dist/server/lib/experimental/ppr.d.ts","./node_modules/next/dist/lib/page-types.d.ts","./node_modules/next/dist/build/segment-config/app/app-segment-config.d.ts","./node_modules/next/dist/build/segment-config/pages/pages-segment-config.d.ts","./node_modules/next/dist/build/analysis/get-page-static-info.d.ts","./node_modules/next/dist/build/webpack/loaders/get-module-build-info.d.ts","./node_modules/next/dist/build/webpack/plugins/middleware-plugin.d.ts","./node_modules/next/dist/server/require-hook.d.ts","./node_modules/next/dist/server/node-polyfill-crypto.d.ts","./node_modules/next/dist/server/node-environment-baseline.d.ts","./node_modules/next/dist/server/node-environment-extensions/error-inspect.d.ts","./node_modules/next/dist/server/node-environment-extensions/console-file.d.ts","./node_modules/next/dist/server/node-environment-extensions/console-exit.d.ts","./node_modules/next/dist/server/node-environment-extensions/console-dim.external.d.ts","./node_modules/next/dist/server/node-environment-extensions/unhandled-rejection.external.d.ts","./node_modules/next/dist/server/node-environment-extensions/random.d.ts","./node_modules/next/dist/server/node-environment-extensions/date.d.ts","./node_modules/next/dist/server/node-environment-extensions/web-crypto.d.ts","./node_modules/next/dist/server/node-environment-extensions/node-crypto.d.ts","./node_modules/next/dist/server/node-environment-extensions/fast-set-immediate.external.d.ts","./node_modules/next/dist/server/node-environment.d.ts","./node_modules/next/dist/build/page-extensions-type.d.ts","./node_modules/next/dist/server/route-modules/app-page/module.compiled.d.ts","./node_modules/next/dist/server/route-definitions/app-route-route-definition.d.ts","./node_modules/next/dist/server/lib/i18n-provider.d.ts","./node_modules/next/dist/server/web/next-url.d.ts","./node_modules/next/dist/compiled/@edge-runtime/cookies/index.d.ts","./node_modules/next/dist/server/web/spec-extension/cookies.d.ts","./node_modules/next/dist/server/web/spec-extension/request.d.ts","./node_modules/next/dist/shared/lib/deep-readonly.d.ts","./node_modules/next/dist/server/lib/incremental-cache/index.d.ts","./node_modules/next/dist/shared/lib/router/utils/middleware-route-matcher.d.ts","./node_modules/next/dist/build/webpack/plugins/flight-manifest-plugin.d.ts","./node_modules/next/dist/build/webpack/plugins/next-font-manifest-plugin.d.ts","./node_modules/next/dist/server/route-definitions/locale-route-definition.d.ts","./node_modules/next/dist/server/route-definitions/pages-route-definition.d.ts","./node_modules/next/dist/shared/lib/mitt.d.ts","./node_modules/next/dist/client/with-router.d.ts","./node_modules/next/dist/client/router.d.ts","./node_modules/next/dist/client/route-loader.d.ts","./node_modules/next/dist/client/page-loader.d.ts","./node_modules/next/dist/shared/lib/bloom-filter.d.ts","./node_modules/next/dist/shared/lib/router/router.d.ts","./node_modules/next/dist/shared/lib/router-context.shared-runtime.d.ts","./node_modules/next/dist/shared/lib/loadable-context.shared-runtime.d.ts","./node_modules/next/dist/shared/lib/loadable.shared-runtime.d.ts","./node_modules/next/dist/shared/lib/image-config-context.shared-runtime.d.ts","./node_modules/next/dist/client/components/readonly-url-search-params.d.ts","./node_modules/next/dist/shared/lib/hooks-client-context.shared-runtime.d.ts","./node_modules/next/dist/shared/lib/head-manager-context.shared-runtime.d.ts","./node_modules/next/dist/client/flight-data-helpers.d.ts","./node_modules/next/dist/client/components/segment-cache/cache-key.d.ts","./node_modules/next/dist/client/components/router-reducer/fetch-server-response.d.ts","./node_modules/next/dist/client/components/segment-cache/types.d.ts","./node_modules/next/dist/shared/lib/segment-cache/segment-value-encoding.d.ts","./node_modules/next/dist/client/components/segment-cache/scheduler.d.ts","./node_modules/next/dist/client/components/segment-cache/cache-map.d.ts","./node_modules/next/dist/client/components/segment-cache/vary-path.d.ts","./node_modules/next/dist/client/components/segment-cache/cache.d.ts","./node_modules/next/dist/client/components/router-reducer/ppr-navigations.d.ts","./node_modules/next/dist/client/components/segment-cache/navigation.d.ts","./node_modules/next/dist/client/components/router-reducer/router-reducer-types.d.ts","./node_modules/next/dist/shared/lib/app-router-context.shared-runtime.d.ts","./node_modules/next/dist/shared/lib/server-inserted-html.shared-runtime.d.ts","./node_modules/next/dist/server/route-modules/pages/vendored/contexts/entrypoints.d.ts","./node_modules/next/dist/server/route-modules/pages/module.compiled.d.ts","./node_modules/next/dist/build/templates/pages.d.ts","./node_modules/next/dist/server/route-modules/pages/module.d.ts","./node_modules/next/dist/server/render.d.ts","./node_modules/next/dist/build/webpack/plugins/pages-manifest-plugin.d.ts","./node_modules/next/dist/server/route-definitions/pages-api-route-definition.d.ts","./node_modules/next/dist/server/route-matches/pages-api-route-match.d.ts","./node_modules/next/dist/server/route-matchers/route-matcher.d.ts","./node_modules/next/dist/server/route-matcher-providers/route-matcher-provider.d.ts","./node_modules/next/dist/server/route-matcher-managers/route-matcher-manager.d.ts","./node_modules/next/dist/server/normalizers/normalizer.d.ts","./node_modules/next/dist/server/normalizers/locale-route-normalizer.d.ts","./node_modules/next/dist/server/normalizers/request/pathname-normalizer.d.ts","./node_modules/next/dist/server/normalizers/request/suffix.d.ts","./node_modules/next/dist/server/normalizers/request/rsc.d.ts","./node_modules/next/dist/server/normalizers/request/next-data.d.ts","./node_modules/next/dist/server/after/builtin-request-context.d.ts","./node_modules/next/dist/server/normalizers/request/segment-prefix-rsc.d.ts","./node_modules/next/dist/server/route-modules/pages/builtin/_error.d.ts","./node_modules/next/dist/server/load-default-error-components.d.ts","./node_modules/next/dist/server/base-server.d.ts","./node_modules/next/dist/server/after/after.d.ts","./node_modules/next/dist/server/after/after-context.d.ts","./node_modules/next/dist/server/use-cache/cache-life.d.ts","./node_modules/next/dist/server/app-render/work-async-storage-instance.d.ts","./node_modules/next/dist/server/lib/lazy-result.d.ts","./node_modules/next/dist/server/app-render/create-error-handler.d.ts","./node_modules/next/dist/shared/lib/action-revalidation-kind.d.ts","./node_modules/next/dist/server/app-render/work-async-storage.external.d.ts","./node_modules/next/dist/server/async-storage/work-store.d.ts","./node_modules/next/dist/server/web/http.d.ts","./node_modules/next/dist/client/components/hooks-server-context.d.ts","./node_modules/next/dist/server/route-modules/app-route/shared-modules.d.ts","./node_modules/next/dist/client/components/redirect-status-code.d.ts","./node_modules/next/dist/client/components/redirect-error.d.ts","./node_modules/next/dist/server/web/spec-extension/adapters/request-cookies.d.ts","./node_modules/next/dist/server/async-storage/draft-mode-provider.d.ts","./node_modules/next/dist/server/web/spec-extension/adapters/headers.d.ts","./node_modules/next/dist/server/app-render/cache-signal.d.ts","./node_modules/next/dist/server/app-render/instant-validation/boundary-tracking.d.ts","./node_modules/next/dist/server/app-render/instant-validation/instant-validation-error.d.ts","./node_modules/next/dist/shared/lib/router/utils/parse-relative-url.d.ts","./node_modules/next/dist/server/app-render/instant-validation/instant-samples.d.ts","./node_modules/next/dist/server/app-render/dynamic-rendering.d.ts","./node_modules/next/dist/server/app-render/work-unit-async-storage-instance.d.ts","./node_modules/next/dist/server/lib/implicit-tags.d.ts","./node_modules/next/dist/server/app-render/staged-rendering.d.ts","./node_modules/next/dist/server/app-render/work-unit-async-storage.external.d.ts","./node_modules/next/dist/build/templates/app-route.d.ts","./node_modules/next/dist/server/app-render/action-async-storage-instance.d.ts","./node_modules/next/dist/server/app-render/action-async-storage.external.d.ts","./node_modules/next/dist/server/route-modules/app-route/module.d.ts","./node_modules/next/dist/server/route-modules/app-route/module.compiled.d.ts","./node_modules/next/dist/build/segment-config/app/app-segments.d.ts","./node_modules/next/dist/build/get-supported-browsers.d.ts","./node_modules/next/dist/build/utils.d.ts","./node_modules/next/dist/build/rendering-mode.d.ts","./node_modules/next/dist/server/lib/router-utils/build-prefetch-segment-data-route.d.ts","./node_modules/next/dist/server/lib/cpu-profile.d.ts","./node_modules/next/dist/build/turborepo-access-trace/types.d.ts","./node_modules/next/dist/build/turborepo-access-trace/result.d.ts","./node_modules/next/dist/build/turborepo-access-trace/helpers.d.ts","./node_modules/next/dist/build/turborepo-access-trace/index.d.ts","./node_modules/next/dist/export/routes/types.d.ts","./node_modules/next/dist/export/types.d.ts","./node_modules/next/dist/export/worker.d.ts","./node_modules/next/dist/build/worker.d.ts","./node_modules/next/dist/build/index.d.ts","./node_modules/next/dist/lib/coalesced-function.d.ts","./node_modules/next/dist/server/lib/router-utils/types.d.ts","./node_modules/next/dist/trace/types.d.ts","./node_modules/next/dist/trace/trace.d.ts","./node_modules/next/dist/trace/shared.d.ts","./node_modules/next/dist/trace/index.d.ts","./node_modules/next/dist/build/load-jsconfig.d.ts","./node_modules/@next/env/dist/index.d.ts","./node_modules/next/dist/build/webpack/plugins/telemetry-plugin/use-cache-tracker-utils.d.ts","./node_modules/next/dist/build/webpack/plugins/telemetry-plugin/telemetry-plugin.d.ts","./node_modules/next/dist/telemetry/storage.d.ts","./node_modules/next/dist/build/build-context.d.ts","./node_modules/next/dist/build/webpack-config.d.ts","./node_modules/next/dist/build/swc/generated-native.d.ts","./node_modules/next/dist/build/define-env.d.ts","./node_modules/next/dist/build/swc/index.d.ts","./node_modules/next/dist/build/swc/types.d.ts","./node_modules/next/dist/server/dev/parse-version-info.d.ts","./node_modules/next/dist/next-devtools/shared/types.d.ts","./node_modules/next/dist/server/dev/dev-indicator-server-state.d.ts","./node_modules/next/dist/next-devtools/dev-overlay/cache-indicator.d.ts","./node_modules/next/dist/server/lib/parse-stack.d.ts","./node_modules/next/dist/next-devtools/server/shared.d.ts","./node_modules/next/dist/next-devtools/shared/stack-frame.d.ts","./node_modules/next/dist/next-devtools/dev-overlay/utils/get-error-by-type.d.ts","./node_modules/next/dist/next-devtools/dev-overlay/container/runtime-error/render-error.d.ts","./node_modules/next/dist/next-devtools/dev-overlay/shared.d.ts","./node_modules/next/dist/server/dev/debug-channel.d.ts","./node_modules/next/dist/server/dev/hot-reloader-types.d.ts","./node_modules/next/dist/server/web/spec-extension/fetch-event.d.ts","./node_modules/next/dist/server/web/spec-extension/response.d.ts","./node_modules/next/dist/build/segment-config/middleware/middleware-config.d.ts","./node_modules/next/dist/server/web/types.d.ts","./node_modules/next/dist/shared/lib/router/utils/parse-url.d.ts","./node_modules/next/dist/server/base-http/node.d.ts","./node_modules/next/dist/server/lib/async-callback-set.d.ts","./node_modules/next/dist/shared/lib/router/utils/route-regex.d.ts","./node_modules/next/dist/shared/lib/router/utils/route-matcher.d.ts","./node_modules/@img/colour/index.d.ts","./node_modules/sharp/dist/index.d.mts","./node_modules/next/dist/server/image-optimizer.d.ts","./node_modules/next/dist/server/next-server.d.ts","./node_modules/next/dist/server/lib/types.d.ts","./node_modules/next/dist/server/lib/lru-cache.d.ts","./node_modules/next/dist/server/lib/dev-bundler-service.d.ts","./node_modules/next/dist/server/dev/static-paths-worker.d.ts","./node_modules/next/dist/server/dev/next-dev-server.d.ts","./node_modules/next/dist/server/next.d.ts","./node_modules/next/dist/server/lib/render-server.d.ts","./node_modules/next/dist/server/lib/router-server.d.ts","./node_modules/next/dist/shared/lib/router/utils/path-match.d.ts","./node_modules/next/dist/server/lib/router-utils/filesystem.d.ts","./node_modules/next/dist/server/lib/router-utils/setup-dev-bundler.d.ts","./node_modules/next/dist/server/lib/router-utils/router-server-context.d.ts","./node_modules/next/dist/server/route-modules/route-module.d.ts","./node_modules/next/dist/server/load-components.d.ts","./node_modules/next/dist/server/web/adapter.d.ts","./node_modules/next/dist/server/app-render/types.d.ts","./node_modules/next/dist/build/webpack/loaders/metadata/types.d.ts","./node_modules/next/dist/build/webpack/loaders/next-app-loader/index.d.ts","./node_modules/next/dist/server/lib/app-dir-module.d.ts","./node_modules/next/dist/server/app-render/app-render.d.ts","./node_modules/next/dist/server/route-modules/app-page/vendored/contexts/entrypoints.d.ts","./node_modules/next/dist/client/components/error-boundary.d.ts","./node_modules/next/dist/client/components/layout-router.d.ts","./node_modules/next/dist/client/components/render-from-template-context.d.ts","./node_modules/next/dist/client/components/client-page.d.ts","./node_modules/next/dist/client/components/client-segment.d.ts","./node_modules/next/dist/client/components/http-access-fallback/error-boundary.d.ts","./node_modules/next/dist/lib/metadata/types/alternative-urls-types.d.ts","./node_modules/next/dist/lib/metadata/types/extra-types.d.ts","./node_modules/next/dist/lib/metadata/types/metadata-types.d.ts","./node_modules/next/dist/lib/metadata/types/manifest-types.d.ts","./node_modules/next/dist/lib/metadata/types/opengraph-types.d.ts","./node_modules/next/dist/lib/metadata/types/twitter-types.d.ts","./node_modules/next/dist/lib/metadata/types/metadata-interface.d.ts","./node_modules/next/dist/lib/metadata/types/resolvers.d.ts","./node_modules/next/dist/lib/metadata/types/icons.d.ts","./node_modules/next/dist/lib/metadata/resolve-metadata.d.ts","./node_modules/next/dist/lib/metadata/metadata.d.ts","./node_modules/next/dist/lib/framework/boundary-components.d.ts","./node_modules/next/dist/server/app-render/rsc/preloads.d.ts","./node_modules/next/dist/server/app-render/rsc/postpone.d.ts","./node_modules/next/dist/server/app-render/rsc/taint.d.ts","./node_modules/next/dist/server/app-render/collect-segment-data.d.ts","./node_modules/next/dist/server/app-render/instant-validation/instant-validation.d.ts","./node_modules/next/dist/next-devtools/userspace/app/segment-explorer-node.d.ts","./node_modules/next/dist/server/app-render/entry-base.d.ts","./node_modules/next/dist/build/templates/app-page.d.ts","./node_modules/next/dist/server/route-modules/app-page/helpers/prerender-manifest-matcher.d.ts","./node_modules/@types/react/jsx-dev-runtime.d.ts","./node_modules/@types/react/compiler-runtime.d.ts","./node_modules/next/dist/server/route-modules/app-page/vendored/rsc/entrypoints.d.ts","./node_modules/@types/react-dom/client.d.ts","./node_modules/@types/react-dom/static.d.ts","./node_modules/@types/react-dom/server.d.ts","./node_modules/next/dist/server/route-modules/app-page/vendored/ssr/entrypoints.d.ts","./node_modules/next/dist/server/route-modules/app-page/module.d.ts","./node_modules/next/dist/server/request/fallback-params.d.ts","./node_modules/next/dist/server/web/spec-extension/image-response.d.ts","./node_modules/next/dist/server/web/spec-extension/user-agent.d.ts","./node_modules/next/dist/server/web/spec-extension/url-pattern.d.ts","./node_modules/next/dist/server/after/index.d.ts","./node_modules/next/dist/server/request/connection.d.ts","./node_modules/next/dist/server/web/exports/index.d.ts","./node_modules/next/dist/server/request-meta.d.ts","./node_modules/next/dist/cli/next-test.d.ts","./node_modules/next/dist/shared/lib/size-limit.d.ts","./node_modules/next/dist/server/config-shared.d.ts","./node_modules/next/dist/server/base-http/index.d.ts","./node_modules/next/dist/server/api-utils/index.d.ts","./node_modules/next/dist/build/adapter/build-complete.d.ts","./node_modules/next/dist/types.d.ts","./node_modules/next/dist/shared/lib/html-context.shared-runtime.d.ts","./node_modules/next/dist/shared/lib/utils.d.ts","./node_modules/next/dist/pages/_app.d.ts","./node_modules/next/app.d.ts","./node_modules/next/dist/server/web/spec-extension/unstable-cache.d.ts","./node_modules/next/dist/server/web/spec-extension/revalidate.d.ts","./node_modules/next/dist/server/web/spec-extension/unstable-no-store.d.ts","./node_modules/next/dist/server/use-cache/cache-tag.d.ts","./node_modules/next/cache.d.ts","./node_modules/next/dist/pages/_document.d.ts","./node_modules/next/document.d.ts","./node_modules/next/dist/shared/lib/dynamic.d.ts","./node_modules/next/dynamic.d.ts","./node_modules/next/dist/pages/_error.d.ts","./node_modules/next/dist/client/components/catch-error.d.ts","./node_modules/next/dist/api/error.d.ts","./node_modules/next/error.d.ts","./node_modules/next/dist/shared/lib/head.d.ts","./node_modules/next/head.d.ts","./node_modules/next/dist/server/request/cookies.d.ts","./node_modules/next/dist/server/request/headers.d.ts","./node_modules/next/dist/server/request/draft-mode.d.ts","./node_modules/next/headers.d.ts","./node_modules/next/dist/shared/lib/get-img-props.d.ts","./node_modules/next/dist/client/image-component.d.ts","./node_modules/next/dist/shared/lib/image-external.d.ts","./node_modules/next/image.d.ts","./node_modules/next/dist/client/link.d.ts","./node_modules/next/link.d.ts","./node_modules/next/dist/client/components/unrecognized-action-error.d.ts","./node_modules/next/dist/client/components/redirect.d.ts","./node_modules/next/dist/client/components/not-found.d.ts","./node_modules/next/dist/client/components/forbidden.d.ts","./node_modules/next/dist/client/components/unauthorized.d.ts","./node_modules/next/dist/client/components/unstable-rethrow.server.d.ts","./node_modules/next/dist/client/components/unstable-rethrow.d.ts","./node_modules/next/dist/client/components/navigation.react-server.d.ts","./node_modules/next/dist/client/components/navigation.d.ts","./node_modules/next/navigation.d.ts","./node_modules/next/router.d.ts","./node_modules/next/dist/client/script.d.ts","./node_modules/next/script.d.ts","./node_modules/next/dist/compiled/@edge-runtime/primitives/url.d.ts","./node_modules/next/dist/compiled/@vercel/og/satori/index.d.ts","./node_modules/next/dist/compiled/@vercel/og/types.d.ts","./node_modules/next/server.d.ts","./node_modules/next/types/global.d.ts","./node_modules/next/types/compiled.d.ts","./node_modules/next/types.d.ts","./node_modules/next/index.d.ts","./node_modules/next/image-types/global.d.ts","./.next/dev/types/routes.d.ts","./next-env.d.ts","./node_modules/@jest/pattern/build/index.d.ts","./node_modules/collect-v8-coverage/index.d.ts","./node_modules/@types/istanbul-lib-coverage/index.d.ts","./node_modules/chalk/index.d.ts","./node_modules/@types/istanbul-lib-report/index.d.ts","./node_modules/@types/istanbul-reports/index.d.ts","./node_modules/@types/yargs-parser/index.d.ts","./node_modules/@types/yargs/index.d.ts","./node_modules/@types/yargs/index.d.mts","./node_modules/@sinclair/typebox/build/esm/type/symbols/symbols.d.mts","./node_modules/@sinclair/typebox/build/esm/type/symbols/index.d.mts","./node_modules/@sinclair/typebox/build/esm/type/any/any.d.mts","./node_modules/@sinclair/typebox/build/esm/type/any/index.d.mts","./node_modules/@sinclair/typebox/build/esm/type/mapped/mapped-key.d.mts","./node_modules/@sinclair/typebox/build/esm/type/mapped/mapped-result.d.mts","./node_modules/@sinclair/typebox/build/esm/type/async-iterator/async-iterator.d.mts","./node_modules/@sinclair/typebox/build/esm/type/async-iterator/index.d.mts","./node_modules/@sinclair/typebox/build/esm/type/readonly/readonly.d.mts","./node_modules/@sinclair/typebox/build/esm/type/readonly/readonly-from-mapped-result.d.mts","./node_modules/@sinclair/typebox/build/esm/type/readonly/index.d.mts","./node_modules/@sinclair/typebox/build/esm/type/readonly-optional/readonly-optional.d.mts","./node_modules/@sinclair/typebox/build/esm/type/readonly-optional/index.d.mts","./node_modules/@sinclair/typebox/build/esm/type/constructor/constructor.d.mts","./node_modules/@sinclair/typebox/build/esm/type/constructor/index.d.mts","./node_modules/@sinclair/typebox/build/esm/type/literal/literal.d.mts","./node_modules/@sinclair/typebox/build/esm/type/literal/index.d.mts","./node_modules/@sinclair/typebox/build/esm/type/enum/enum.d.mts","./node_modules/@sinclair/typebox/build/esm/type/enum/index.d.mts","./node_modules/@sinclair/typebox/build/esm/type/function/function.d.mts","./node_modules/@sinclair/typebox/build/esm/type/function/index.d.mts","./node_modules/@sinclair/typebox/build/esm/type/computed/computed.d.mts","./node_modules/@sinclair/typebox/build/esm/type/computed/index.d.mts","./node_modules/@sinclair/typebox/build/esm/type/never/never.d.mts","./node_modules/@sinclair/typebox/build/esm/type/never/index.d.mts","./node_modules/@sinclair/typebox/build/esm/type/intersect/intersect-type.d.mts","./node_modules/@sinclair/typebox/build/esm/type/intersect/intersect-evaluated.d.mts","./node_modules/@sinclair/typebox/build/esm/type/intersect/intersect.d.mts","./node_modules/@sinclair/typebox/build/esm/type/intersect/index.d.mts","./node_modules/@sinclair/typebox/build/esm/type/union/union-type.d.mts","./node_modules/@sinclair/typebox/build/esm/type/union/union-evaluated.d.mts","./node_modules/@sinclair/typebox/build/esm/type/union/union.d.mts","./node_modules/@sinclair/typebox/build/esm/type/union/index.d.mts","./node_modules/@sinclair/typebox/build/esm/type/recursive/recursive.d.mts","./node_modules/@sinclair/typebox/build/esm/type/recursive/index.d.mts","./node_modules/@sinclair/typebox/build/esm/type/unsafe/unsafe.d.mts","./node_modules/@sinclair/typebox/build/esm/type/unsafe/index.d.mts","./node_modules/@sinclair/typebox/build/esm/type/ref/ref.d.mts","./node_modules/@sinclair/typebox/build/esm/type/ref/index.d.mts","./node_modules/@sinclair/typebox/build/esm/type/tuple/tuple.d.mts","./node_modules/@sinclair/typebox/build/esm/type/tuple/index.d.mts","./node_modules/@sinclair/typebox/build/esm/type/error/error.d.mts","./node_modules/@sinclair/typebox/build/esm/type/error/index.d.mts","./node_modules/@sinclair/typebox/build/esm/type/string/string.d.mts","./node_modules/@sinclair/typebox/build/esm/type/string/index.d.mts","./node_modules/@sinclair/typebox/build/esm/type/boolean/boolean.d.mts","./node_modules/@sinclair/typebox/build/esm/type/boolean/index.d.mts","./node_modules/@sinclair/typebox/build/esm/type/number/number.d.mts","./node_modules/@sinclair/typebox/build/esm/type/number/index.d.mts","./node_modules/@sinclair/typebox/build/esm/type/integer/integer.d.mts","./node_modules/@sinclair/typebox/build/esm/type/integer/index.d.mts","./node_modules/@sinclair/typebox/build/esm/type/bigint/bigint.d.mts","./node_modules/@sinclair/typebox/build/esm/type/bigint/index.d.mts","./node_modules/@sinclair/typebox/build/esm/type/template-literal/parse.d.mts","./node_modules/@sinclair/typebox/build/esm/type/template-literal/finite.d.mts","./node_modules/@sinclair/typebox/build/esm/type/template-literal/generate.d.mts","./node_modules/@sinclair/typebox/build/esm/type/template-literal/syntax.d.mts","./node_modules/@sinclair/typebox/build/esm/type/template-literal/pattern.d.mts","./node_modules/@sinclair/typebox/build/esm/type/template-literal/template-literal.d.mts","./node_modules/@sinclair/typebox/build/esm/type/template-literal/union.d.mts","./node_modules/@sinclair/typebox/build/esm/type/template-literal/index.d.mts","./node_modules/@sinclair/typebox/build/esm/type/indexed/indexed-property-keys.d.mts","./node_modules/@sinclair/typebox/build/esm/type/indexed/indexed-from-mapped-result.d.mts","./node_modules/@sinclair/typebox/build/esm/type/indexed/indexed.d.mts","./node_modules/@sinclair/typebox/build/esm/type/indexed/indexed-from-mapped-key.d.mts","./node_modules/@sinclair/typebox/build/esm/type/indexed/index.d.mts","./node_modules/@sinclair/typebox/build/esm/type/iterator/iterator.d.mts","./node_modules/@sinclair/typebox/build/esm/type/iterator/index.d.mts","./node_modules/@sinclair/typebox/build/esm/type/promise/promise.d.mts","./node_modules/@sinclair/typebox/build/esm/type/promise/index.d.mts","./node_modules/@sinclair/typebox/build/esm/type/sets/set.d.mts","./node_modules/@sinclair/typebox/build/esm/type/sets/index.d.mts","./node_modules/@sinclair/typebox/build/esm/type/mapped/mapped.d.mts","./node_modules/@sinclair/typebox/build/esm/type/mapped/index.d.mts","./node_modules/@sinclair/typebox/build/esm/type/optional/optional.d.mts","./node_modules/@sinclair/typebox/build/esm/type/optional/optional-from-mapped-result.d.mts","./node_modules/@sinclair/typebox/build/esm/type/optional/index.d.mts","./node_modules/@sinclair/typebox/build/esm/type/awaited/awaited.d.mts","./node_modules/@sinclair/typebox/build/esm/type/awaited/index.d.mts","./node_modules/@sinclair/typebox/build/esm/type/keyof/keyof-property-keys.d.mts","./node_modules/@sinclair/typebox/build/esm/type/keyof/keyof.d.mts","./node_modules/@sinclair/typebox/build/esm/type/keyof/keyof-from-mapped-result.d.mts","./node_modules/@sinclair/typebox/build/esm/type/keyof/keyof-property-entries.d.mts","./node_modules/@sinclair/typebox/build/esm/type/keyof/index.d.mts","./node_modules/@sinclair/typebox/build/esm/type/omit/omit-from-mapped-result.d.mts","./node_modules/@sinclair/typebox/build/esm/type/omit/omit.d.mts","./node_modules/@sinclair/typebox/build/esm/type/omit/omit-from-mapped-key.d.mts","./node_modules/@sinclair/typebox/build/esm/type/omit/index.d.mts","./node_modules/@sinclair/typebox/build/esm/type/pick/pick-from-mapped-result.d.mts","./node_modules/@sinclair/typebox/build/esm/type/pick/pick.d.mts","./node_modules/@sinclair/typebox/build/esm/type/pick/pick-from-mapped-key.d.mts","./node_modules/@sinclair/typebox/build/esm/type/pick/index.d.mts","./node_modules/@sinclair/typebox/build/esm/type/null/null.d.mts","./node_modules/@sinclair/typebox/build/esm/type/null/index.d.mts","./node_modules/@sinclair/typebox/build/esm/type/symbol/symbol.d.mts","./node_modules/@sinclair/typebox/build/esm/type/symbol/index.d.mts","./node_modules/@sinclair/typebox/build/esm/type/undefined/undefined.d.mts","./node_modules/@sinclair/typebox/build/esm/type/undefined/index.d.mts","./node_modules/@sinclair/typebox/build/esm/type/partial/partial.d.mts","./node_modules/@sinclair/typebox/build/esm/type/partial/partial-from-mapped-result.d.mts","./node_modules/@sinclair/typebox/build/esm/type/partial/index.d.mts","./node_modules/@sinclair/typebox/build/esm/type/regexp/regexp.d.mts","./node_modules/@sinclair/typebox/build/esm/type/regexp/index.d.mts","./node_modules/@sinclair/typebox/build/esm/type/record/record.d.mts","./node_modules/@sinclair/typebox/build/esm/type/record/index.d.mts","./node_modules/@sinclair/typebox/build/esm/type/required/required.d.mts","./node_modules/@sinclair/typebox/build/esm/type/required/required-from-mapped-result.d.mts","./node_modules/@sinclair/typebox/build/esm/type/required/index.d.mts","./node_modules/@sinclair/typebox/build/esm/type/transform/transform.d.mts","./node_modules/@sinclair/typebox/build/esm/type/transform/index.d.mts","./node_modules/@sinclair/typebox/build/esm/type/module/compute.d.mts","./node_modules/@sinclair/typebox/build/esm/type/module/infer.d.mts","./node_modules/@sinclair/typebox/build/esm/type/module/module.d.mts","./node_modules/@sinclair/typebox/build/esm/type/module/index.d.mts","./node_modules/@sinclair/typebox/build/esm/type/not/not.d.mts","./node_modules/@sinclair/typebox/build/esm/type/not/index.d.mts","./node_modules/@sinclair/typebox/build/esm/type/static/static.d.mts","./node_modules/@sinclair/typebox/build/esm/type/static/index.d.mts","./node_modules/@sinclair/typebox/build/esm/type/object/object.d.mts","./node_modules/@sinclair/typebox/build/esm/type/object/index.d.mts","./node_modules/@sinclair/typebox/build/esm/type/helpers/helpers.d.mts","./node_modules/@sinclair/typebox/build/esm/type/helpers/index.d.mts","./node_modules/@sinclair/typebox/build/esm/type/array/array.d.mts","./node_modules/@sinclair/typebox/build/esm/type/array/index.d.mts","./node_modules/@sinclair/typebox/build/esm/type/date/date.d.mts","./node_modules/@sinclair/typebox/build/esm/type/date/index.d.mts","./node_modules/@sinclair/typebox/build/esm/type/uint8array/uint8array.d.mts","./node_modules/@sinclair/typebox/build/esm/type/uint8array/index.d.mts","./node_modules/@sinclair/typebox/build/esm/type/unknown/unknown.d.mts","./node_modules/@sinclair/typebox/build/esm/type/unknown/index.d.mts","./node_modules/@sinclair/typebox/build/esm/type/void/void.d.mts","./node_modules/@sinclair/typebox/build/esm/type/void/index.d.mts","./node_modules/@sinclair/typebox/build/esm/type/schema/schema.d.mts","./node_modules/@sinclair/typebox/build/esm/type/schema/anyschema.d.mts","./node_modules/@sinclair/typebox/build/esm/type/schema/index.d.mts","./node_modules/@sinclair/typebox/build/esm/type/clone/type.d.mts","./node_modules/@sinclair/typebox/build/esm/type/clone/value.d.mts","./node_modules/@sinclair/typebox/build/esm/type/clone/index.d.mts","./node_modules/@sinclair/typebox/build/esm/type/create/type.d.mts","./node_modules/@sinclair/typebox/build/esm/type/create/index.d.mts","./node_modules/@sinclair/typebox/build/esm/type/argument/argument.d.mts","./node_modules/@sinclair/typebox/build/esm/type/argument/index.d.mts","./node_modules/@sinclair/typebox/build/esm/type/guard/kind.d.mts","./node_modules/@sinclair/typebox/build/esm/type/guard/type.d.mts","./node_modules/@sinclair/typebox/build/esm/type/guard/value.d.mts","./node_modules/@sinclair/typebox/build/esm/type/guard/index.d.mts","./node_modules/@sinclair/typebox/build/esm/type/patterns/patterns.d.mts","./node_modules/@sinclair/typebox/build/esm/type/patterns/index.d.mts","./node_modules/@sinclair/typebox/build/esm/type/registry/format.d.mts","./node_modules/@sinclair/typebox/build/esm/type/registry/type.d.mts","./node_modules/@sinclair/typebox/build/esm/type/registry/index.d.mts","./node_modules/@sinclair/typebox/build/esm/type/composite/composite.d.mts","./node_modules/@sinclair/typebox/build/esm/type/composite/index.d.mts","./node_modules/@sinclair/typebox/build/esm/type/const/const.d.mts","./node_modules/@sinclair/typebox/build/esm/type/const/index.d.mts","./node_modules/@sinclair/typebox/build/esm/type/constructor-parameters/constructor-parameters.d.mts","./node_modules/@sinclair/typebox/build/esm/type/constructor-parameters/index.d.mts","./node_modules/@sinclair/typebox/build/esm/type/exclude/exclude-from-template-literal.d.mts","./node_modules/@sinclair/typebox/build/esm/type/exclude/exclude.d.mts","./node_modules/@sinclair/typebox/build/esm/type/exclude/exclude-from-mapped-result.d.mts","./node_modules/@sinclair/typebox/build/esm/type/exclude/index.d.mts","./node_modules/@sinclair/typebox/build/esm/type/extends/extends-check.d.mts","./node_modules/@sinclair/typebox/build/esm/type/extends/extends-from-mapped-result.d.mts","./node_modules/@sinclair/typebox/build/esm/type/extends/extends.d.mts","./node_modules/@sinclair/typebox/build/esm/type/extends/extends-from-mapped-key.d.mts","./node_modules/@sinclair/typebox/build/esm/type/extends/extends-undefined.d.mts","./node_modules/@sinclair/typebox/build/esm/type/extends/index.d.mts","./node_modules/@sinclair/typebox/build/esm/type/extract/extract-from-template-literal.d.mts","./node_modules/@sinclair/typebox/build/esm/type/extract/extract.d.mts","./node_modules/@sinclair/typebox/build/esm/type/extract/extract-from-mapped-result.d.mts","./node_modules/@sinclair/typebox/build/esm/type/extract/index.d.mts","./node_modules/@sinclair/typebox/build/esm/type/instance-type/instance-type.d.mts","./node_modules/@sinclair/typebox/build/esm/type/instance-type/index.d.mts","./node_modules/@sinclair/typebox/build/esm/type/instantiate/instantiate.d.mts","./node_modules/@sinclair/typebox/build/esm/type/instantiate/index.d.mts","./node_modules/@sinclair/typebox/build/esm/type/intrinsic/intrinsic-from-mapped-key.d.mts","./node_modules/@sinclair/typebox/build/esm/type/intrinsic/intrinsic.d.mts","./node_modules/@sinclair/typebox/build/esm/type/intrinsic/capitalize.d.mts","./node_modules/@sinclair/typebox/build/esm/type/intrinsic/lowercase.d.mts","./node_modules/@sinclair/typebox/build/esm/type/intrinsic/uncapitalize.d.mts","./node_modules/@sinclair/typebox/build/esm/type/intrinsic/uppercase.d.mts","./node_modules/@sinclair/typebox/build/esm/type/intrinsic/index.d.mts","./node_modules/@sinclair/typebox/build/esm/type/parameters/parameters.d.mts","./node_modules/@sinclair/typebox/build/esm/type/parameters/index.d.mts","./node_modules/@sinclair/typebox/build/esm/type/rest/rest.d.mts","./node_modules/@sinclair/typebox/build/esm/type/rest/index.d.mts","./node_modules/@sinclair/typebox/build/esm/type/return-type/return-type.d.mts","./node_modules/@sinclair/typebox/build/esm/type/return-type/index.d.mts","./node_modules/@sinclair/typebox/build/esm/type/type/json.d.mts","./node_modules/@sinclair/typebox/build/esm/type/type/javascript.d.mts","./node_modules/@sinclair/typebox/build/esm/type/type/index.d.mts","./node_modules/@sinclair/typebox/build/esm/index.d.mts","./node_modules/@jest/schemas/build/index.d.ts","./node_modules/@jest/types/build/index.d.ts","./node_modules/@types/stack-utils/index.d.ts","./node_modules/@jest/console/node_modules/jest-message-util/build/index.d.ts","./node_modules/@jest/console/build/index.d.ts","./node_modules/jest-haste-map/build/index.d.ts","./node_modules/unrs-resolver/index.d.ts","./node_modules/jest-resolve/build/index.d.ts","./node_modules/@jest/test-result/build/index.d.ts","./node_modules/@jest/reporters/build/index.d.ts","./node_modules/jest-changed-files/build/index.d.ts","./node_modules/emittery/index.d.ts","./node_modules/jest-watcher/build/index.d.ts","./node_modules/jest-runner/build/index.d.ts","./node_modules/@jest/core/build/index.d.ts","./node_modules/jest-cli/build/index.d.ts","./node_modules/jest-validate/build/index.d.ts","./node_modules/jest-config/build/index.d.ts","./node_modules/jest/build/index.d.ts","./jest.config.ts","./node_modules/@jest/expect-utils/build/index.d.ts","./node_modules/jest-diff/node_modules/@sinclair/typebox/typebox.d.ts","./node_modules/jest-diff/node_modules/@jest/schemas/build/index.d.ts","./node_modules/jest-diff/node_modules/pretty-format/build/index.d.ts","./node_modules/jest-diff/build/index.d.ts","./node_modules/jest-matcher-utils/build/index.d.ts","./node_modules/expect/build/index.d.ts","./node_modules/@types/jest/node_modules/pretty-format/build/index.d.ts","./node_modules/@types/jest/index.d.ts","./node_modules/@types/aria-query/index.d.ts","./node_modules/@testing-library/jest-dom/types/matchers.d.ts","./node_modules/@testing-library/jest-dom/types/jest.d.ts","./node_modules/@testing-library/jest-dom/types/index.d.ts","./jest.setup.ts","./next.config.ts","./node_modules/playwright-core/types/protocol.d.ts","./node_modules/playwright-core/types/structs.d.ts","./node_modules/zod/v3/helpers/typealiases.d.cts","./node_modules/zod/v3/helpers/util.d.cts","./node_modules/zod/v3/index.d.cts","./node_modules/zod/v3/zoderror.d.cts","./node_modules/zod/v3/locales/en.d.cts","./node_modules/zod/v3/errors.d.cts","./node_modules/zod/v3/helpers/parseutil.d.cts","./node_modules/zod/v3/helpers/enumutil.d.cts","./node_modules/zod/v3/helpers/errorutil.d.cts","./node_modules/zod/v3/helpers/partialutil.d.cts","./node_modules/zod/v3/standard-schema.d.cts","./node_modules/zod/v3/types.d.cts","./node_modules/zod/v3/external.d.cts","./node_modules/zod/index.d.cts","./node_modules/playwright-core/types/types.d.ts","./node_modules/playwright-core/index.d.ts","./node_modules/playwright/types/test.d.ts","./node_modules/playwright/test.d.ts","./node_modules/@playwright/test/index.d.ts","./playwright.config.ts","./proxy.ts","./app/robots.ts","./app/sitemap.ts","./app/api/auth/login/route.ts","./app/api/auth/logout/route.ts","./app/api/checkout/create-payment-intent/route.ts","./app/api/webhooks/stripe/route.ts","./e2e/auth.spec.ts","./e2e/checkout.spec.ts","./e2e/phase1-checkpoint.spec.ts","./hooks/usedebouncedvalue.ts","./hooks/useorderstatuspolling.ts","./hooks/usewebsocket.ts","./types/api.ts","./lib/api/client.ts","./types/user.ts","./lib/validation/auth.ts","./lib/api/auth.ts","./lib/api/cart.ts","./lib/api/notifications.ts","./types/order.ts","./lib/api/orders.ts","./types/product.ts","./lib/api/products.ts","./lib/api/reviews.ts","./types/address.ts","./lib/api/users.ts","./lib/api/wishlist.ts","./node_modules/zustand/esm/vanilla.d.mts","./node_modules/zustand/esm/react.d.mts","./node_modules/zustand/esm/index.d.mts","./lib/stores/authstore.ts","./lib/stores/cartstore.ts","./lib/stores/checkoutstore.ts","./lib/stores/notificationstore.ts","./lib/stores/wishliststore.ts","./lib/stripe/client.ts","./lib/stripe/paymentintent.ts","./lib/utils/format.ts","./lib/validation/address.ts","./lib/validation/contact.ts","./lib/validation/review.ts","./lib/websocket/chatconnection.ts","./lib/websocket/connectionmanager.ts","./types/auth.ts","./types/cart.ts","./types/category.ts","./types/chats.ts","./types/notification.ts","./types/review.ts","./types/role.ts","./types/wishlist.ts","./app/error.tsx","./app/layout.tsx","./app/not-found.tsx","./app/page.tsx","./app/(auth)/layout.tsx","./app/(auth)/forgot-password/page.tsx","./node_modules/react-hook-form/dist/constants.d.ts","./node_modules/react-hook-form/dist/utils/createsubject.d.ts","./node_modules/react-hook-form/dist/types/events.d.ts","./node_modules/react-hook-form/dist/types/path/common.d.ts","./node_modules/react-hook-form/dist/types/path/eager.d.ts","./node_modules/react-hook-form/dist/types/path/index.d.ts","./node_modules/react-hook-form/dist/types/fieldarray.d.ts","./node_modules/react-hook-form/dist/types/resolvers.d.ts","./node_modules/react-hook-form/dist/types/form.d.ts","./node_modules/react-hook-form/dist/types/utils.d.ts","./node_modules/react-hook-form/dist/types/fields.d.ts","./node_modules/react-hook-form/dist/types/errors.d.ts","./node_modules/react-hook-form/dist/types/validator.d.ts","./node_modules/react-hook-form/dist/types/controller.d.ts","./node_modules/react-hook-form/dist/types/watch.d.ts","./node_modules/react-hook-form/dist/types/index.d.ts","./node_modules/react-hook-form/dist/controller.d.ts","./node_modules/react-hook-form/dist/fieldarray.d.ts","./node_modules/react-hook-form/dist/form.d.ts","./node_modules/react-hook-form/dist/formstatesubscribe.d.ts","./node_modules/react-hook-form/dist/logic/appenderrors.d.ts","./node_modules/react-hook-form/dist/logic/createformcontrol.d.ts","./node_modules/react-hook-form/dist/logic/index.d.ts","./node_modules/react-hook-form/dist/usecontroller.d.ts","./node_modules/react-hook-form/dist/usefieldarray.d.ts","./node_modules/react-hook-form/dist/useform.d.ts","./node_modules/react-hook-form/dist/useformcontext.d.ts","./node_modules/react-hook-form/dist/useformstate.d.ts","./node_modules/react-hook-form/dist/usewatch.d.ts","./node_modules/react-hook-form/dist/utils/get.d.ts","./node_modules/react-hook-form/dist/utils/set.d.ts","./node_modules/react-hook-form/dist/utils/index.d.ts","./node_modules/react-hook-form/dist/watch.d.ts","./node_modules/react-hook-form/dist/index.d.ts","./node_modules/zod/v4/core/standard-schema.d.cts","./node_modules/zod/v4/core/util.d.cts","./node_modules/zod/v4/core/versions.d.cts","./node_modules/zod/v4/core/schemas.d.cts","./node_modules/zod/v4/core/checks.d.cts","./node_modules/zod/v4/core/errors.d.cts","./node_modules/zod/v4/core/core.d.cts","./node_modules/zod/v4/core/parse.d.cts","./node_modules/zod/v4/core/regexes.d.cts","./node_modules/zod/v4/locales/ar.d.cts","./node_modules/zod/v4/locales/az.d.cts","./node_modules/zod/v4/locales/be.d.cts","./node_modules/zod/v4/locales/ca.d.cts","./node_modules/zod/v4/locales/cs.d.cts","./node_modules/zod/v4/locales/de.d.cts","./node_modules/zod/v4/locales/en.d.cts","./node_modules/zod/v4/locales/eo.d.cts","./node_modules/zod/v4/locales/es.d.cts","./node_modules/zod/v4/locales/fa.d.cts","./node_modules/zod/v4/locales/fi.d.cts","./node_modules/zod/v4/locales/fr.d.cts","./node_modules/zod/v4/locales/fr-ca.d.cts","./node_modules/zod/v4/locales/he.d.cts","./node_modules/zod/v4/locales/hu.d.cts","./node_modules/zod/v4/locales/id.d.cts","./node_modules/zod/v4/locales/it.d.cts","./node_modules/zod/v4/locales/ja.d.cts","./node_modules/zod/v4/locales/kh.d.cts","./node_modules/zod/v4/locales/ko.d.cts","./node_modules/zod/v4/locales/mk.d.cts","./node_modules/zod/v4/locales/ms.d.cts","./node_modules/zod/v4/locales/nl.d.cts","./node_modules/zod/v4/locales/no.d.cts","./node_modules/zod/v4/locales/ota.d.cts","./node_modules/zod/v4/locales/ps.d.cts","./node_modules/zod/v4/locales/pl.d.cts","./node_modules/zod/v4/locales/pt.d.cts","./node_modules/zod/v4/locales/ru.d.cts","./node_modules/zod/v4/locales/sl.d.cts","./node_modules/zod/v4/locales/sv.d.cts","./node_modules/zod/v4/locales/ta.d.cts","./node_modules/zod/v4/locales/th.d.cts","./node_modules/zod/v4/locales/tr.d.cts","./node_modules/zod/v4/locales/ua.d.cts","./node_modules/zod/v4/locales/ur.d.cts","./node_modules/zod/v4/locales/vi.d.cts","./node_modules/zod/v4/locales/zh-cn.d.cts","./node_modules/zod/v4/locales/zh-tw.d.cts","./node_modules/zod/v4/locales/index.d.cts","./node_modules/zod/v4/core/registries.d.cts","./node_modules/zod/v4/core/doc.d.cts","./node_modules/zod/v4/core/function.d.cts","./node_modules/zod/v4/core/api.d.cts","./node_modules/zod/v4/core/json-schema.d.cts","./node_modules/zod/v4/core/to-json-schema.d.cts","./node_modules/zod/v4/core/index.d.cts","./node_modules/@hookform/resolvers/zod/dist/zod.d.ts","./node_modules/@hookform/resolvers/zod/dist/index.d.ts","./app/(auth)/login/page.tsx","./app/(auth)/register/page.tsx","./app/(auth)/reset-password/page.tsx","./app/(auth)/verify-email/page.tsx","./app/(protected)/layout.tsx","./app/(protected)/account/page.tsx","./app/(protected)/addresses/page.tsx","./app/(protected)/chat-history/page.tsx","./app/(protected)/checkout/page.tsx","./app/(protected)/checkout/order-confirmation/[orderid]/page.tsx","./app/(protected)/notifications/page.tsx","./app/(protected)/orders/page.tsx","./app/(protected)/orders/[orderid]/page.tsx","./app/(protected)/orders/[orderid]/return/page.tsx","./app/(protected)/profile/page.tsx","./app/(protected)/settings/page.tsx","./app/(protected)/wishlist/page.tsx","./app/(public)/layout.tsx","./app/(public)/loading.tsx","./app/(public)/page.tsx","./app/(public)/about/page.tsx","./app/(public)/cart/page.tsx","./app/(public)/categories/page.tsx","./app/(public)/categories/[slug]/page.tsx","./app/(public)/contact/page.tsx","./app/(public)/faq/page.tsx","./app/(public)/privacy/page.tsx","./app/(public)/products/loading.tsx","./app/(public)/products/page.tsx","./app/(public)/products/[slug]/loading.tsx","./app/(public)/products/[slug]/page.tsx","./app/(public)/return-policy/page.tsx","./app/(public)/search/page.tsx","./app/(public)/terms/page.tsx","./node_modules/@testing-library/dom/types/matches.d.ts","./node_modules/@testing-library/dom/types/wait-for.d.ts","./node_modules/@testing-library/dom/types/query-helpers.d.ts","./node_modules/@testing-library/dom/types/queries.d.ts","./node_modules/@testing-library/dom/types/get-queries-for-element.d.ts","./node_modules/pretty-format/build/types.d.ts","./node_modules/pretty-format/build/index.d.ts","./node_modules/@testing-library/dom/types/screen.d.ts","./node_modules/@testing-library/dom/types/wait-for-element-to-be-removed.d.ts","./node_modules/@testing-library/dom/types/get-node-text.d.ts","./node_modules/@testing-library/dom/types/events.d.ts","./node_modules/@testing-library/dom/types/pretty-dom.d.ts","./node_modules/@testing-library/dom/types/role-helpers.d.ts","./node_modules/@testing-library/dom/types/config.d.ts","./node_modules/@testing-library/dom/types/suggestions.d.ts","./node_modules/@testing-library/dom/types/index.d.ts","./node_modules/@types/react-dom/test-utils/index.d.ts","./node_modules/@testing-library/react/types/index.d.ts","./tests/smoke.test.tsx","./.next/dev/types/cache-life.d.ts","./.next/dev/types/validator.ts","./node_modules/@babel/types/lib/index.d.ts","./node_modules/@types/babel__generator/index.d.ts","./node_modules/@babel/parser/typings/babel-parser.d.ts","./node_modules/@types/babel__template/index.d.ts","./node_modules/@types/babel__traverse/index.d.ts","./node_modules/@types/babel__core/index.d.ts","./node_modules/@types/esrecurse/index.d.ts","./node_modules/@types/estree/index.d.ts","./node_modules/parse5/dist/common/html.d.ts","./node_modules/parse5/dist/common/token.d.ts","./node_modules/parse5/dist/common/error-codes.d.ts","./node_modules/parse5/dist/tokenizer/preprocessor.d.ts","./node_modules/entities/dist/esm/generated/decode-data-html.d.ts","./node_modules/entities/dist/esm/generated/decode-data-xml.d.ts","./node_modules/entities/dist/esm/decode-codepoint.d.ts","./node_modules/entities/dist/esm/decode.d.ts","./node_modules/parse5/dist/tokenizer/index.d.ts","./node_modules/parse5/dist/tree-adapters/interface.d.ts","./node_modules/parse5/dist/parser/open-element-stack.d.ts","./node_modules/parse5/dist/parser/formatting-element-list.d.ts","./node_modules/parse5/dist/parser/index.d.ts","./node_modules/parse5/dist/tree-adapters/default.d.ts","./node_modules/parse5/dist/serializer/index.d.ts","./node_modules/parse5/dist/common/foreign-content.d.ts","./node_modules/parse5/dist/index.d.ts","./node_modules/tough-cookie/dist/cookie/constants.d.ts","./node_modules/tough-cookie/dist/cookie/cookie.d.ts","./node_modules/tough-cookie/dist/utils.d.ts","./node_modules/tough-cookie/dist/store.d.ts","./node_modules/tough-cookie/dist/memstore.d.ts","./node_modules/tough-cookie/dist/pathmatch.d.ts","./node_modules/tough-cookie/dist/permutedomain.d.ts","./node_modules/tough-cookie/dist/getpublicsuffix.d.ts","./node_modules/tough-cookie/dist/validators.d.ts","./node_modules/tough-cookie/dist/version.d.ts","./node_modules/tough-cookie/dist/cookie/canonicaldomain.d.ts","./node_modules/tough-cookie/dist/cookie/cookiecompare.d.ts","./node_modules/tough-cookie/dist/cookie/cookiejar.d.ts","./node_modules/tough-cookie/dist/cookie/defaultpath.d.ts","./node_modules/tough-cookie/dist/cookie/domainmatch.d.ts","./node_modules/tough-cookie/dist/cookie/formatdate.d.ts","./node_modules/tough-cookie/dist/cookie/parsedate.d.ts","./node_modules/tough-cookie/dist/cookie/permutepath.d.ts","./node_modules/tough-cookie/dist/cookie/index.d.ts","./node_modules/@types/jsdom/base.d.ts","./node_modules/@types/jsdom/index.d.ts","./node_modules/@types/json-schema/index.d.ts","./node_modules/@types/json5/index.d.ts","./node_modules/@types/tough-cookie/index.d.ts"],"fileIdsList":[[97,143,484,485,486,487],[97,143],[97,143,226,525,528,531,844,846,847,848,941,942,943,944,945,946,947,948,949,950,951,952,953,954,955,956,957,958,960,961,962,963,964,965,966,967,969,971,972,973,974],[97,143,226],[85,97,143,226],[85,97,143,226,508,518,805,807,822,882,940],[85,97,143,226,518,822],[97,143,226,526,529],[97,143,226,508],[97,143,226,529],[97,143,226,752],[97,143,226,805,806,807],[97,143,226,804,805],[97,143,226,804],[97,143,226,804,805,811],[97,143,226,804,805,813],[97,143,226,805,806,816],[97,143,226,806,807,808,821],[97,143,226,784],[97,143,529,530,531],[97,143,996],[97,143,939],[97,143,773,882,938],[97,143,146,183,185,735,737],[97,143,735,736],[97,143,533,735,742,743,744,746,747],[97,143,183,735,742],[97,143,733],[97,143,534,535,735,738,739,741],[97,143,166,533,535,536,538,541,734],[97,143,788],[97,143,543,545,549,552,554,556,558,560,562,566,570,574,576,578,580,582,584,586,588,590,592,594,602,607,609,611,613,615,618,620,625,629,633,635,637,639,642,644,646,649,651,655,657,659,661,663,665,667,669,671,673,676,679,681,683,687,689,692,694,696,698,702,708,712,714,716,723,725,727,729,732],[97,143,543,676],[97,143,544],[97,143,682],[97,143,543,659,663,676],[97,143,664],[97,143,543,659,676],[97,143,548],[97,143,564,570,574,580,611,663,676],[97,143,619],[97,143,593],[97,143,587],[97,143,677,678],[97,143,676],[97,143,566,570,607,613,625,661,663,676],[97,143,693],[97,143,542,676],[97,143,563],[97,143,545,552,558,562,566,582,594,635,637,639,661,663,667,669,671,676],[97,143,695],[97,143,556,566,582,676],[97,143,697],[97,143,543,552,554,618,659,663,676],[97,143,555],[97,143,680],[97,143,674],[97,143,666],[97,143,543,558,676],[97,143,559],[97,143,583],[97,143,615,661,676,700],[97,143,602,676,700],[97,143,566,574,602,615,659,663,676,699,701],[97,143,699,700,701],[97,143,584,676],[97,143,558,615,661,663,676,705],[97,143,615,661,676,705],[97,143,574,615,659,663,676,704,706],[97,143,703,704,705,706,707],[97,143,615,661,676,710],[97,143,602,676,710],[97,143,566,574,602,615,659,663,676,709,711],[97,143,709,710,711],[97,143,561],[97,143,684,685,686],[97,143,543,545,549,552,556,558,562,564,566,570,574,576,578,580,582,586,588,590,592,594,602,609,611,615,618,635,637,639,644,646,651,655,657,661,665,667,669,671,673,676,683],[97,143,543,545,549,552,556,558,562,564,566,570,574,576,578,580,582,584,586,588,590,592,594,602,609,611,615,618,635,637,639,644,646,651,655,657,661,665,667,669,671,673,676,683],[97,143,566,661,676],[97,143,662],[97,143,603,604,605,606],[97,143,605,615,661,663,676],[97,143,603,607,615,661,676],[97,143,558,574,590,592,602,676],[97,143,564,566,570,574,576,580,582,603,604,606,615,661,663,665,676],[97,143,713],[97,143,556,566,676],[97,143,715],[97,143,549,552,554,556,562,570,574,582,609,611,618,646,661,665,671,676,683],[97,143,591],[97,143,567,568,569],[97,143,552,566,567,618,676],[97,143,566,567,676],[97,143,676,718],[97,143,717,718,719,720,721,722],[97,143,558,615,661,663,676,718],[97,143,558,574,602,615,676,717],[97,143,608],[97,143,621,622,623,624],[97,143,615,622,661,663,676],[97,143,570,574,576,582,613,661,663,665,676],[97,143,558,564,574,580,590,615,621,623,663,676],[97,143,557],[97,143,546,547,614],[97,143,543,661,676],[97,143,546,547,549,552,556,558,560,562,570,574,582,607,609,611,613,618,661,663,665,676],[97,143,549,552,556,560,562,564,566,570,574,580,582,607,609,618,620,625,629,633,642,646,649,651,661,663,665,676],[97,143,654],[97,143,549,552,556,560,562,570,574,576,580,582,609,618,646,659,661,663,665,676],[97,143,543,652,653,659,661,676],[97,143,565],[97,143,656],[97,143,634],[97,143,589],[97,143,660],[97,143,543,552,618,659,663,676],[97,143,626,627,628],[97,143,615,627,661,676],[97,143,615,627,661,663,676],[97,143,558,564,570,574,576,580,607,615,626,628,661,663,676],[97,143,616,617],[97,143,615,616,661],[97,143,543,615,617,663,676],[97,143,724],[97,143,562,566,582,676],[97,143,640,641],[97,143,615,640,661,663,676],[97,143,552,554,558,564,570,574,576,580,586,588,590,592,594,615,618,635,637,639,641,661,663,676],[97,143,688],[97,143,630,631,632],[97,143,615,631,661,676],[97,143,615,631,661,663,676],[97,143,558,564,570,574,576,580,607,615,630,632,661,663,676],[97,143,610],[97,143,553],[97,143,552,618,676],[97,143,550,551],[97,143,550,615,661],[97,143,543,551,615,663,676],[97,143,645],[97,143,543,545,558,560,566,574,586,588,590,592,602,644,659,661,663,676],[97,143,575],[97,143,579],[97,143,543,578,659,676],[97,143,643],[97,143,690,691],[97,143,647,648],[97,143,615,647,661,663,676],[97,143,552,554,558,564,570,574,576,580,586,588,590,592,594,615,618,635,637,639,648,661,663,676],[97,143,726],[97,143,570,574,582,676],[97,143,728],[97,143,562,566,676],[97,143,545,549,556,558,560,562,570,574,576,580,582,586,588,590,592,594,602,609,611,635,637,639,644,646,657,661,665,667,669,671,673,674],[97,143,674,675],[97,143,543],[97,143,612],[97,143,658],[97,143,549,552,556,560,562,566,570,574,576,578,580,582,609,611,618,646,651,655,657,661,663,665,676],[97,143,585],[97,143,636],[97,143,542],[97,143,558,574,584,586,588,590,592,594,595,602],[97,143,558,574,584,588,595,596,602,663],[97,143,595,596,597,598,599,600,601],[97,143,584],[97,143,584,602],[97,143,558,574,586,588,590,594,602,663],[97,143,543,558,566,574,586,588,590,592,594,598,659,663,676],[97,143,558,574,600,659,663],[97,143,650],[97,143,581],[97,143,730,731],[97,143,549,556,562,594,609,611,620,637,639,644,667,669,673,676,683,698,714,716,725,729,730],[97,143,545,552,554,558,560,566,570,574,576,578,580,582,586,588,590,592,602,607,615,618,625,629,633,635,642,646,649,651,655,657,661,665,671,676,694,696,702,708,712,723,727],[97,143,668],[97,143,638],[97,143,571,572,573],[97,143,552,566,571,618,676],[97,143,566,571,676],[97,143,670],[97,143,577],[97,143,672],[97,143,978],[97,143,975,976,977,978,979,982,983,984,985,986,987,988,989],[97,143,763],[97,143,981],[97,143,975,976,977],[97,143,975,976],[97,143,978,979,981],[97,143,976],[97,143,765],[97,143,762,764],[85,97,143,196,460,990,991],[97,143,996,997,998,999,1000],[97,143,996,998],[97,143,535],[97,143,537],[97,143,757,760],[97,143,756],[97,143,154,187,191,1020,1039,1041],[97,143,1040],[97,140,143],[97,142,143],[143],[97,143,148,176],[97,143,144,149,154,162,173,184],[97,143,144,145,154,162],[92,93,94,97,143],[97,143,146,185],[97,143,147,148,155,163],[97,143,148,173,181],[97,143,149,151,154,162],[97,142,143,150],[97,143,151,152],[97,143,153,154],[97,142,143,154],[97,143,154,155,156,173,184],[97,143,154,155,156,169,173,176],[97,143,151,154,157,162,173,184],[97,143,154,155,157,158,162,173,181,184],[97,143,157,159,173,181,184],[95,96,97,98,99,100,101,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176,177,178,179,180,181,182,183,184,185,186,187,188,189,190],[97,143,154,160],[97,143,161,184,189],[97,143,151,154,162,173],[97,143,163],[97,143,164],[97,142,143,165],[97,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176,177,178,179,180,181,182,183,184,185,186,187,188,189,190],[97,143,167],[97,143,168],[97,143,154,169,170],[97,143,169,171,185,187],[97,143,154,173,174,176],[97,143,175,176],[97,143,173,174],[97,143,176],[97,143,177],[97,140,143,173,178],[97,143,154,179,180],[97,143,179,180],[97,143,148,162,173,181],[97,143,182],[97,143,162,183],[97,143,157,168,184],[97,143,148,185],[97,143,173,186],[97,143,161,187],[97,143,188],[97,138,143],[97,138,143,154,156,165,173,176,184,187,189],[97,143,173,190],[85,89,97,143,192,193,194,196,479,524],[85,97,143],[85,89,97,143,192,193,194,195,460,479,524],[85,89,97,143,192,193,195,196,479,524],[85,97,143,196,460,461],[85,97,143,196,460],[85,89,97,143,193,194,195,196,479,524],[85,89,97,143,192,194,195,196,479,524],[83,84,97,143],[97,143,540],[97,143,539],[97,143,160,191],[97,143,1008,1009,1010],[97,143,754,759],[97,143,541,735],[97,143,735,750],[97,143,757],[97,143,755],[97,143,155,735],[97,143,536,758],[97,143,739,740],[97,143,735,742,746],[97,143,183,735,742,745],[97,143,735,748,749,751],[97,143,482],[97,143,430,493,494],[97,143,201,202,204,216,240,355,366,475],[97,143,204,235,236,237,239,475],[97,143,204,372,374,376,377,379,475,477],[97,143,204,238,275,475],[97,143,202,204,215,216,222,228,233,354,355,356,365,475,477],[97,143,475],[97,143,211,217,236,256,351],[97,143,204],[97,143,197,211,217],[97,143,383],[97,143,380,381,383],[97,143,380,382,475],[97,143,157,256,454,472],[97,143,157,327,330,346,351,472],[97,143,157,299,472],[97,143,359],[97,143,358,359,360],[97,143,358],[91,97,143,157,197,204,216,222,228,234,236,240,241,254,255,322,352,353,366,475,479],[97,143,201,204,238,275,372,373,378,475,527],[97,143,238,527],[97,143,201,255,425,475,527],[97,143,527],[97,143,204,238,239,527],[97,143,375,527],[97,143,241,354,357,364],[85,97,143,430],[97,143,168,211,226],[97,143,211,226],[85,97,143,296],[85,97,143,217,226,430],[97,143,211,282,296,297,509,516],[97,143,281,510,511,512,513,515],[97,143,332],[97,143,332,333],[97,143,215,217,284,285],[97,143,217,291,292],[97,143,217,286,294],[97,143,291],[97,143,209,217,284,285,286,287,288,289,290,291,294],[97,143,217,284,291,292,293,295],[97,143,217,285,287,288],[97,143,285,287,290,292],[97,143,514],[97,143,217],[85,97,143,205,503],[85,97,143,184],[85,97,143,238,273],[85,97,143,238,366],[97,143,271,276],[85,97,143,272,481],[85,89,97,143,157,192,193,194,195,196,479,523],[97,143,157,217],[97,143,157,216,221,302,319,361,362,366,422,424,475,476],[97,143,254,363],[97,143,479],[97,143,203],[85,97,143,208,211,427,443,445],[97,143,168,211,427,442,443,444,526],[97,143,436,437,438,439,440,441],[97,143,438],[97,143,442],[97,143,226,390,391,393],[85,97,143,217,384,385,386,387,392],[97,143,390,392],[97,143,388],[97,143,389],[85,97,143,226,272,481],[85,97,143,226,480,481],[85,97,143,226,481],[97,143,319,320],[97,143,320],[97,143,157,476,481],[97,143,349],[97,142,143,348],[97,143,211,217,223,225,327,340,344,346,424,427,464,465,472,476],[97,143,217,266,288],[97,143,327,338,341,346],[85,97,143,208,211,327,330,346,349,383,431,432,433,434,435,446,447,448,449,450,451,452,453,527],[97,143,208,211,236,327,334,335,336,339,340],[97,143,173,217,236,338,345,427,428,472],[97,143,342],[97,143,157,168,205,217,221,231,263,264,267,319,322,387,422,423,464,475,476,477,479,527],[97,143,208,209,211],[97,143,327],[97,142,143,236,263,264,321,322,323,324,325,326,476],[97,143,346],[97,142,143,210,211,221,225,261,327,334,335,336,337,338,341,342,343,344,345,465],[97,143,157,261,262,334,476,477],[97,143,236,264,319,322,327,424,476],[97,143,157,475,477],[97,143,157,173,472,476,477],[97,143,157,168,197,211,216,223,225,228,231,238,258,263,264,265,266,267,302,303,305,308,310,313,314,315,316,318,366,422,424,472,475,476,477],[97,143,157,173],[97,143,204,205,206,234,472,473,474,479,481,527],[97,143,201,202,475],[97,143,395],[97,143,157,173,184,213,379,383,384,385,386,387,393,394,527],[97,143,168,184,197,211,213,225,228,264,303,308,318,319,372,399,400,401,408,411,412,422,424,472,475],[97,143,228,234,241,254,264,322,475],[97,143,157,184,205,216,225,264,406,472,475],[97,143,426],[97,143,157,395,409,410,419],[97,143,472,475],[97,143,324,465],[97,143,225,263,366,481],[97,143,157,168,203,308,368,372,401,408,411,414,472],[97,143,157,241,254,372,415],[97,143,204,265,366,417,475,477],[97,143,157,184,387,475],[97,143,157,238,265,366,367,368,377,395,416,418,475],[91,97,143,157,263,421,479,481],[97,143,317,422],[97,143,157,168,211,214,216,217,223,225,231,240,241,254,264,267,303,305,315,318,319,366,399,400,401,402,404,407,422,424,472,481],[97,143,157,173,241,408,413,419,472],[97,143,244,245,246,247,248,249,250,251,252,253],[97,143,258,309],[97,143,311],[97,143,309],[97,143,311,312],[97,143,157,215,216,217,221,222,476],[97,143,157,168,203,205,223,227,263,266,267,301,422,472,477,479,481],[97,143,157,168,184,207,214,215,225,227,264,420,465,471,476],[97,143,334],[97,143,335],[97,143,217,228,464],[97,143,336],[97,143,210],[97,143,212,224],[97,143,157,212,216,223],[97,143,219,224],[97,143,220],[97,143,212,213],[97,143,212,268],[97,143,212],[97,143,214,258,307],[97,143,306],[97,143,211,213,214],[97,143,214,304],[97,143,211,213],[97,143,263,366],[97,143,464],[97,143,157,184,223,225,229,263,366,421,424,427,428,429,455,456,459,463,465,472,476],[97,143,277,280,282,283,296,297],[85,97,143,194,196,226,457,458],[85,97,143,194,196,226,457,458,462],[97,143,350],[97,143,236,257,262,263,327,328,329,330,331,333,346,347,349,352,421,424,475,477],[97,143,296],[97,143,157,301,472],[97,143,301],[97,143,157,223,269,298,300,302,421,472,479,481],[97,143,277,278,279,280,282,283,296,297,480],[91,97,143,157,168,184,212,213,225,231,263,264,267,366,419,420,422,472,475,476,479],[97,143,208,211,218],[97,143,262,264,396,399],[97,143,262,397,466,467,468,469,470],[97,143,157,258,475],[97,143,157],[97,143,261,346],[97,143,260],[97,143,262,315],[97,143,259,261,475],[97,143,157,207,262,396,397,398,472,475,476],[85,97,143,211,217,295],[85,97,143,209],[97,143,199,200],[85,97,143,205],[85,97,143,211,281],[85,91,97,143,263,267,479,481],[97,143,205,503,504],[85,97,143,276],[85,97,143,168,184,203,270,272,274,275,481],[97,143,211,238,476],[97,143,211,403],[85,97,143,155,157,168,201,203,276,374,479,480],[85,97,143,192,193,194,195,196,479,524],[85,86,87,88,89,97,143],[97,143,148],[97,143,369,370,371],[97,143,369],[85,89,97,143,157,159,168,191,192,193,194,195,196,197,203,231,236,414,442,477,478,481,524],[97,143,489],[97,143,491],[97,143,495],[97,143,497],[97,143,499,500,501],[97,143,505],[90,97,143,483,488,490,492,496,498,502,506,508,518,519,521,525,526,527,528],[97,143,507],[97,143,517],[97,143,272],[97,143,520],[97,142,143,262,396,397,399,466,467,469,470,522,524],[97,143,191],[97,143,1005],[97,143,1004,1005],[97,143,1004],[97,143,1004,1005,1006,1012,1013,1016,1017,1018,1019],[97,143,1005,1013],[97,143,1004,1005,1006,1012,1013,1014,1015],[97,143,1004,1013],[97,143,1013,1017],[97,143,1005,1006,1007,1011],[97,143,1006],[97,143,1004,1005,1013],[97,143,785],[97,143,144,155,173,769,770,773,784],[97,143,787],[97,143,786],[97,143,980],[85,97,143,864],[97,143,864,865,866,867,868,871,872,873,874,875,876,877,880,881],[97,143,864],[97,143,869,870],[85,97,143,861,864],[97,143,858,859,861],[97,143,854,857,859,861],[97,143,858,861],[85,97,143,849,850,851,854,855,856,858,859,860,861],[97,143,851,854,855,856,857,858,859,860,861,862,863],[97,143,858],[97,143,852,858,859],[97,143,852,853],[97,143,857,859,860],[97,143,857],[97,143,849,854,857,859,860],[85,97,143,854,857,858,859],[97,143,878,879],[97,143,173,191,405],[97,143,1023],[97,143,1021],[97,143,1022],[97,143,1021,1022,1023,1024],[97,143,1021,1022,1023,1024,1025,1026,1027,1028,1029,1030,1031,1032,1033,1034,1035,1036,1037,1038],[97,143,1022,1023,1024],[97,143,1023,1039],[97,110,114,143,184],[97,110,143,173,184],[97,105,143],[97,107,110,143,181,184],[97,143,162,181],[97,105,143,191],[97,107,110,143,162,184],[97,102,103,106,109,143,154,173,184],[97,110,117,143],[97,102,108,143],[97,110,131,132,143],[97,106,110,143,176,184,191],[97,131,143,191],[97,104,105,143,191],[97,110,143],[97,104,105,106,107,108,109,110,111,112,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,132,133,134,135,136,137,143],[97,110,125,143],[97,110,117,118,143],[97,108,110,118,119,143],[97,109,143],[97,102,105,110,143],[97,110,114,118,119,143],[97,114,143],[97,108,110,113,143,184],[97,102,107,110,117,143],[97,143,173],[97,105,110,131,143,189,191],[97,143,783],[97,143,774,775],[97,143,771,772,774,776,777,782],[97,143,772,774],[97,143,782],[97,143,774],[97,143,771,772,774,777,778,779,780,781],[97,143,771,772,773],[97,143,884,886,887,888,889],[97,143,884,886,888,889],[97,143,884,886,888],[97,143,884,886,887,889],[97,143,884,886,889],[97,143,884,885,886,887,888,889,890,891,931,932,933,934,935,936,937],[97,143,886,889],[97,143,883,884,885,887,888,889],[97,143,886,932,936],[97,143,886,887,888,889],[97,143,888],[97,143,892,893,894,895,896,897,898,899,900,901,902,903,904,905,906,907,908,909,910,911,912,913,914,915,916,917,918,919,920,921,922,923,924,925,926,927,928,929,930],[97,143,819,820],[97,143,819],[97,143,226,789],[97,143,226,525],[85,97,143,226,846,992]],"fileInfos":[{"version":"c430d44666289dae81f30fa7b2edebf186ecc91a2d4c71266ea6ae76388792e1","affectsGlobalScope":true,"impliedFormat":1},{"version":"45b7ab580deca34ae9729e97c13cfd999df04416a79116c3bfb483804f85ded4","impliedFormat":1},{"version":"3facaf05f0c5fc569c5649dd359892c98a85557e3e0c847964caeb67076f4d75","impliedFormat":1},{"version":"e44bb8bbac7f10ecc786703fe0a6a4b952189f908707980ba8f3c8975a760962","impliedFormat":1},{"version":"5e1c4c362065a6b95ff952c0eab010f04dcd2c3494e813b493ecfd4fcb9fc0d8","impliedFormat":1},{"version":"68d73b4a11549f9c0b7d352d10e91e5dca8faa3322bfb77b661839c42b1ddec7","impliedFormat":1},{"version":"5efce4fc3c29ea84e8928f97adec086e3dc876365e0982cc8479a07954a3efd4","impliedFormat":1},{"version":"feecb1be483ed332fad555aff858affd90a48ab19ba7272ee084704eb7167569","impliedFormat":1},{"version":"ee7bad0c15b58988daa84371e0b89d313b762ab83cb5b31b8a2d1162e8eb41c2","impliedFormat":1},{"version":"27bdc30a0e32783366a5abeda841bc22757c1797de8681bbe81fbc735eeb1c10","impliedFormat":1},{"version":"8fd575e12870e9944c7e1d62e1f5a73fcf23dd8d3a321f2a2c74c20d022283fe","impliedFormat":1},{"version":"2ab096661c711e4a81cc464fa1e6feb929a54f5340b46b0a07ac6bbf857471f0","impliedFormat":1},{"version":"080941d9f9ff9307f7e27a83bcd888b7c8270716c39af943532438932ec1d0b9","affectsGlobalScope":true,"impliedFormat":1},{"version":"2e80ee7a49e8ac312cc11b77f1475804bee36b3b2bc896bead8b6e1266befb43","affectsGlobalScope":true,"impliedFormat":1},{"version":"c57796738e7f83dbc4b8e65132f11a377649c00dd3eee333f672b8f0a6bea671","affectsGlobalScope":true,"impliedFormat":1},{"version":"dc2df20b1bcdc8c2d34af4926e2c3ab15ffe1160a63e58b7e09833f616efff44","affectsGlobalScope":true,"impliedFormat":1},{"version":"515d0b7b9bea2e31ea4ec968e9edd2c39d3eebf4a2d5cbd04e88639819ae3b71","affectsGlobalScope":true,"impliedFormat":1},{"version":"0559b1f683ac7505ae451f9a96ce4c3c92bdc71411651ca6ddb0e88baaaad6a3","affectsGlobalScope":true,"impliedFormat":1},{"version":"0dc1e7ceda9b8b9b455c3a2d67b0412feab00bd2f66656cd8850e8831b08b537","affectsGlobalScope":true,"impliedFormat":1},{"version":"ce691fb9e5c64efb9547083e4a34091bcbe5bdb41027e310ebba8f7d96a98671","affectsGlobalScope":true,"impliedFormat":1},{"version":"8d697a2a929a5fcb38b7a65594020fcef05ec1630804a33748829c5ff53640d0","affectsGlobalScope":true,"impliedFormat":1},{"version":"4ff2a353abf8a80ee399af572debb8faab2d33ad38c4b4474cff7f26e7653b8d","affectsGlobalScope":true,"impliedFormat":1},{"version":"fb0f136d372979348d59b3f5020b4cdb81b5504192b1cacff5d1fbba29378aa1","affectsGlobalScope":true,"impliedFormat":1},{"version":"d15bea3d62cbbdb9797079416b8ac375ae99162a7fba5de2c6c505446486ac0a","affectsGlobalScope":true,"impliedFormat":1},{"version":"68d18b664c9d32a7336a70235958b8997ebc1c3b8505f4f1ae2b7e7753b87618","affectsGlobalScope":true,"impliedFormat":1},{"version":"eb3d66c8327153d8fa7dd03f9c58d351107fe824c79e9b56b462935176cdf12a","affectsGlobalScope":true,"impliedFormat":1},{"version":"38f0219c9e23c915ef9790ab1d680440d95419ad264816fa15009a8851e79119","affectsGlobalScope":true,"impliedFormat":1},{"version":"69ab18c3b76cd9b1be3d188eaf8bba06112ebbe2f47f6c322b5105a6fbc45a2e","affectsGlobalScope":true,"impliedFormat":1},{"version":"a680117f487a4d2f30ea46f1b4b7f58bef1480456e18ba53ee85c2746eeca012","affectsGlobalScope":true,"impliedFormat":1},{"version":"2f11ff796926e0832f9ae148008138ad583bd181899ab7dd768a2666700b1893","affectsGlobalScope":true,"impliedFormat":1},{"version":"4de680d5bb41c17f7f68e0419412ca23c98d5749dcaaea1896172f06435891fc","affectsGlobalScope":true,"impliedFormat":1},{"version":"954296b30da6d508a104a3a0b5d96b76495c709785c1d11610908e63481ee667","affectsGlobalScope":true,"impliedFormat":1},{"version":"ac9538681b19688c8eae65811b329d3744af679e0bdfa5d842d0e32524c73e1c","affectsGlobalScope":true,"impliedFormat":1},{"version":"0a969edff4bd52585473d24995c5ef223f6652d6ef46193309b3921d65dd4376","affectsGlobalScope":true,"impliedFormat":1},{"version":"9e9fbd7030c440b33d021da145d3232984c8bb7916f277e8ffd3dc2e3eae2bdb","affectsGlobalScope":true,"impliedFormat":1},{"version":"811ec78f7fefcabbda4bfa93b3eb67d9ae166ef95f9bff989d964061cbf81a0c","affectsGlobalScope":true,"impliedFormat":1},{"version":"717937616a17072082152a2ef351cb51f98802fb4b2fdabd32399843875974ca","affectsGlobalScope":true,"impliedFormat":1},{"version":"d7e7d9b7b50e5f22c915b525acc5a49a7a6584cf8f62d0569e557c5cfc4b2ac2","affectsGlobalScope":true,"impliedFormat":1},{"version":"71c37f4c9543f31dfced6c7840e068c5a5aacb7b89111a4364b1d5276b852557","affectsGlobalScope":true,"impliedFormat":1},{"version":"576711e016cf4f1804676043e6a0a5414252560eb57de9faceee34d79798c850","affectsGlobalScope":true,"impliedFormat":1},{"version":"89c1b1281ba7b8a96efc676b11b264de7a8374c5ea1e6617f11880a13fc56dc6","affectsGlobalScope":true,"impliedFormat":1},{"version":"74f7fa2d027d5b33eb0471c8e82a6c87216223181ec31247c357a3e8e2fddc5b","affectsGlobalScope":true,"impliedFormat":1},{"version":"d6d7ae4d1f1f3772e2a3cde568ed08991a8ae34a080ff1151af28b7f798e22ca","affectsGlobalScope":true,"impliedFormat":1},{"version":"063600664504610fe3e99b717a1223f8b1900087fab0b4cad1496a114744f8df","affectsGlobalScope":true,"impliedFormat":1},{"version":"934019d7e3c81950f9a8426d093458b65d5aff2c7c1511233c0fd5b941e608ab","affectsGlobalScope":true,"impliedFormat":1},{"version":"52ada8e0b6e0482b728070b7639ee42e83a9b1c22d205992756fe020fd9f4a47","affectsGlobalScope":true,"impliedFormat":1},{"version":"3bdefe1bfd4d6dee0e26f928f93ccc128f1b64d5d501ff4a8cf3c6371200e5e6","affectsGlobalScope":true,"impliedFormat":1},{"version":"59fb2c069260b4ba00b5643b907ef5d5341b167e7d1dbf58dfd895658bda2867","affectsGlobalScope":true,"impliedFormat":1},{"version":"639e512c0dfc3fad96a84caad71b8834d66329a1f28dc95e3946c9b58176c73a","affectsGlobalScope":true,"impliedFormat":1},{"version":"368af93f74c9c932edd84c58883e736c9e3d53cec1fe24c0b0ff451f529ceab1","affectsGlobalScope":true,"impliedFormat":1},{"version":"af3dd424cf267428f30ccfc376f47a2c0114546b55c44d8c0f1d57d841e28d74","affectsGlobalScope":true,"impliedFormat":1},{"version":"995c005ab91a498455ea8dfb63aa9f83fa2ea793c3d8aa344be4a1678d06d399","affectsGlobalScope":true,"impliedFormat":1},{"version":"959d36cddf5e7d572a65045b876f2956c973a586da58e5d26cde519184fd9b8a","affectsGlobalScope":true,"impliedFormat":1},{"version":"965f36eae237dd74e6cca203a43e9ca801ce38824ead814728a2807b1910117d","affectsGlobalScope":true,"impliedFormat":1},{"version":"3925a6c820dcb1a06506c90b1577db1fdbf7705d65b62b99dce4be75c637e26b","affectsGlobalScope":true,"impliedFormat":1},{"version":"0a3d63ef2b853447ec4f749d3f368ce642264246e02911fcb1590d8c161b8005","affectsGlobalScope":true,"impliedFormat":1},{"version":"8cdf8847677ac7d20486e54dd3fcf09eda95812ac8ace44b4418da1bbbab6eb8","affectsGlobalScope":true,"impliedFormat":1},{"version":"8444af78980e3b20b49324f4a16ba35024fef3ee069a0eb67616ea6ca821c47a","affectsGlobalScope":true,"impliedFormat":1},{"version":"3287d9d085fbd618c3971944b65b4be57859f5415f495b33a6adc994edd2f004","affectsGlobalScope":true,"impliedFormat":1},{"version":"b4b67b1a91182421f5df999988c690f14d813b9850b40acd06ed44691f6727ad","affectsGlobalScope":true,"impliedFormat":1},{"version":"df83c2a6c73228b625b0beb6669c7ee2a09c914637e2d35170723ad49c0f5cd4","affectsGlobalScope":true,"impliedFormat":1},{"version":"436aaf437562f276ec2ddbee2f2cdedac7664c1e4c1d2c36839ddd582eeb3d0a","affectsGlobalScope":true,"impliedFormat":1},{"version":"8e3c06ea092138bf9fa5e874a1fdbc9d54805d074bee1de31b99a11e2fec239d","affectsGlobalScope":true,"impliedFormat":1},{"version":"87dc0f382502f5bbce5129bdc0aea21e19a3abbc19259e0b43ae038a9fc4e326","affectsGlobalScope":true,"impliedFormat":1},{"version":"b1cb28af0c891c8c96b2d6b7be76bd394fddcfdb4709a20ba05a7c1605eea0f9","affectsGlobalScope":true,"impliedFormat":1},{"version":"2fef54945a13095fdb9b84f705f2b5994597640c46afeb2ce78352fab4cb3279","affectsGlobalScope":true,"impliedFormat":1},{"version":"ac77cb3e8c6d3565793eb90a8373ee8033146315a3dbead3bde8db5eaf5e5ec6","affectsGlobalScope":true,"impliedFormat":1},{"version":"56e4ed5aab5f5920980066a9409bfaf53e6d21d3f8d020c17e4de584d29600ad","affectsGlobalScope":true,"impliedFormat":1},{"version":"4ece9f17b3866cc077099c73f4983bddbcb1dc7ddb943227f1ec070f529dedd1","affectsGlobalScope":true,"impliedFormat":1},{"version":"0a6282c8827e4b9a95f4bf4f5c205673ada31b982f50572d27103df8ceb8013c","affectsGlobalScope":true,"impliedFormat":1},{"version":"1c9319a09485199c1f7b0498f2988d6d2249793ef67edda49d1e584746be9032","affectsGlobalScope":true,"impliedFormat":1},{"version":"e3a2a0cee0f03ffdde24d89660eba2685bfbdeae955a6c67e8c4c9fd28928eeb","affectsGlobalScope":true,"impliedFormat":1},{"version":"811c71eee4aa0ac5f7adf713323a5c41b0cf6c4e17367a34fbce379e12bbf0a4","affectsGlobalScope":true,"impliedFormat":1},{"version":"51ad4c928303041605b4d7ae32e0c1ee387d43a24cd6f1ebf4a2699e1076d4fa","affectsGlobalScope":true,"impliedFormat":1},{"version":"60037901da1a425516449b9a20073aa03386cce92f7a1fd902d7602be3a7c2e9","affectsGlobalScope":true,"impliedFormat":1},{"version":"d4b1d2c51d058fc21ec2629fff7a76249dec2e36e12960ea056e3ef89174080f","affectsGlobalScope":true,"impliedFormat":1},{"version":"22adec94ef7047a6c9d1af3cb96be87a335908bf9ef386ae9fd50eeb37f44c47","affectsGlobalScope":true,"impliedFormat":1},{"version":"196cb558a13d4533a5163286f30b0509ce0210e4b316c56c38d4c0fd2fb38405","affectsGlobalScope":true,"impliedFormat":1},{"version":"73f78680d4c08509933daf80947902f6ff41b6230f94dd002ae372620adb0f60","affectsGlobalScope":true,"impliedFormat":1},{"version":"c5239f5c01bcfa9cd32f37c496cf19c61d69d37e48be9de612b541aac915805b","affectsGlobalScope":true,"impliedFormat":1},{"version":"8e7f8264d0fb4c5339605a15daadb037bf238c10b654bb3eee14208f860a32ea","affectsGlobalScope":true,"impliedFormat":1},{"version":"782dec38049b92d4e85c1585fbea5474a219c6984a35b004963b00beb1aab538","affectsGlobalScope":true,"impliedFormat":1},{"version":"7e29f41b158de217f94cb9676bf9cbd0cd9b5a46e1985141ed36e075c52bf6ad","affectsGlobalScope":true,"impliedFormat":1},{"version":"ac51dd7d31333793807a6abaa5ae168512b6131bd41d9c5b98477fc3b7800f9f","impliedFormat":1},{"version":"dc782ff85b2cb10075ecffc158af7bfb27ff97bf8491c917efea0c3d622d5ac4","impliedFormat":1},{"version":"acd8fd5090ac73902278889c38336ff3f48af6ba03aa665eb34a75e7ba1dccc4","impliedFormat":1},{"version":"d6258883868fb2680d2ca96bc8b1352cab69874581493e6d52680c5ffecdb6cc","impliedFormat":1},{"version":"1b61d259de5350f8b1e5db06290d31eaebebc6baafd5f79d314b5af9256d7153","impliedFormat":1},{"version":"f258e3960f324a956fc76a3d3d9e964fff2244ff5859dcc6ce5951e5413ca826","impliedFormat":1},{"version":"643f7232d07bf75e15bd8f658f664d6183a0efaca5eb84b48201c7671a266979","impliedFormat":1},{"version":"21da358700a3893281ce0c517a7a30cbd46be020d9f0c3f2834d0a8ad1f5fc75","impliedFormat":1},{"version":"70521b6ab0dcba37539e5303104f29b721bfb2940b2776da4cc818c07e1fefc1","affectsGlobalScope":true,"impliedFormat":1},{"version":"ab41ef1f2cdafb8df48be20cd969d875602483859dc194e9c97c8a576892c052","affectsGlobalScope":true,"impliedFormat":1},{"version":"d153a11543fd884b596587ccd97aebbeed950b26933ee000f94009f1ab142848","affectsGlobalScope":true,"impliedFormat":1},{"version":"21d819c173c0cf7cc3ce57c3276e77fd9a8a01d35a06ad87158781515c9a438a","impliedFormat":1},{"version":"98cffbf06d6bab333473c70a893770dbe990783904002c4f1a960447b4b53dca","affectsGlobalScope":true,"impliedFormat":1},{"version":"ba481bca06f37d3f2c137ce343c7d5937029b2468f8e26111f3c9d9963d6568d","affectsGlobalScope":true,"impliedFormat":1},{"version":"6d9ef24f9a22a88e3e9b3b3d8c40ab1ddb0853f1bfbd5c843c37800138437b61","affectsGlobalScope":true,"impliedFormat":1},{"version":"1db0b7dca579049ca4193d034d835f6bfe73096c73663e5ef9a0b5779939f3d0","affectsGlobalScope":true,"impliedFormat":1},{"version":"9798340ffb0d067d69b1ae5b32faa17ab31b82466a3fc00d8f2f2df0c8554aaa","affectsGlobalScope":true,"impliedFormat":1},{"version":"f26b11d8d8e4b8028f1c7d618b22274c892e4b0ef5b3678a8ccbad85419aef43","affectsGlobalScope":true,"impliedFormat":1},{"version":"5929864ce17fba74232584d90cb721a89b7ad277220627cc97054ba15a98ea8f","impliedFormat":1},{"version":"763fe0f42b3d79b440a9b6e51e9ba3f3f91352469c1e4b3b67bfa4ff6352f3f4","impliedFormat":1},{"version":"25c8056edf4314820382a5fdb4bb7816999acdcb929c8f75e3f39473b87e85bc","impliedFormat":1},{"version":"c464d66b20788266e5353b48dc4aa6bc0dc4a707276df1e7152ab0c9ae21fad8","impliedFormat":1},{"version":"78d0d27c130d35c60b5e5566c9f1e5be77caf39804636bc1a40133919a949f21","impliedFormat":1},{"version":"c6fd2c5a395f2432786c9cb8deb870b9b0e8ff7e22c029954fabdd692bff6195","impliedFormat":1},{"version":"1d6e127068ea8e104a912e42fc0a110e2aa5a66a356a917a163e8cf9a65e4a75","impliedFormat":1},{"version":"5ded6427296cdf3b9542de4471d2aa8d3983671d4cac0f4bf9c637208d1ced43","impliedFormat":1},{"version":"7f182617db458e98fc18dfb272d40aa2fff3a353c44a89b2c0ccb3937709bfb5","impliedFormat":1},{"version":"cadc8aced301244057c4e7e73fbcae534b0f5b12a37b150d80e5a45aa4bebcbd","impliedFormat":1},{"version":"385aab901643aa54e1c36f5ef3107913b10d1b5bb8cbcd933d4263b80a0d7f20","impliedFormat":1},{"version":"9670d44354bab9d9982eca21945686b5c24a3f893db73c0dae0fd74217a4c219","impliedFormat":1},{"version":"0b8a9268adaf4da35e7fa830c8981cfa22adbbe5b3f6f5ab91f6658899e657a7","impliedFormat":1},{"version":"11396ed8a44c02ab9798b7dca436009f866e8dae3c9c25e8c1fbc396880bf1bb","impliedFormat":1},{"version":"ba7bc87d01492633cb5a0e5da8a4a42a1c86270e7b3d2dea5d156828a84e4882","impliedFormat":1},{"version":"4893a895ea92c85345017a04ed427cbd6a1710453338df26881a6019432febdd","impliedFormat":1},{"version":"c21dc52e277bcfc75fac0436ccb75c204f9e1b3fa5e12729670910639f27343e","impliedFormat":1},{"version":"13f6f39e12b1518c6650bbb220c8985999020fe0f21d818e28f512b7771d00f9","impliedFormat":1},{"version":"9b5369969f6e7175740bf51223112ff209f94ba43ecd3bb09eefff9fd675624a","impliedFormat":1},{"version":"4fe9e626e7164748e8769bbf74b538e09607f07ed17c2f20af8d680ee49fc1da","impliedFormat":1},{"version":"24515859bc0b836719105bb6cc3d68255042a9f02a6022b3187948b204946bd2","impliedFormat":1},{"version":"ea0148f897b45a76544ae179784c95af1bd6721b8610af9ffa467a518a086a43","impliedFormat":1},{"version":"24c6a117721e606c9984335f71711877293a9651e44f59f3d21c1ea0856f9cc9","impliedFormat":1},{"version":"dd3273ead9fbde62a72949c97dbec2247ea08e0c6952e701a483d74ef92d6a17","impliedFormat":1},{"version":"405822be75ad3e4d162e07439bac80c6bcc6dbae1929e179cf467ec0b9ee4e2e","impliedFormat":1},{"version":"0db18c6e78ea846316c012478888f33c11ffadab9efd1cc8bcc12daded7a60b6","impliedFormat":1},{"version":"e61be3f894b41b7baa1fbd6a66893f2579bfad01d208b4ff61daef21493ef0a8","impliedFormat":1},{"version":"bd0532fd6556073727d28da0edfd1736417a3f9f394877b6d5ef6ad88fba1d1a","impliedFormat":1},{"version":"89167d696a849fce5ca508032aabfe901c0868f833a8625d5a9c6e861ef935d2","impliedFormat":1},{"version":"615ba88d0128ed16bf83ef8ccbb6aff05c3ee2db1cc0f89ab50a4939bfc1943f","impliedFormat":1},{"version":"a4d551dbf8746780194d550c88f26cf937caf8d56f102969a110cfaed4b06656","impliedFormat":1},{"version":"8bd86b8e8f6a6aa6c49b71e14c4ffe1211a0e97c80f08d2c8cc98838006e4b88","impliedFormat":1},{"version":"317e63deeb21ac07f3992f5b50cdca8338f10acd4fbb7257ebf56735bf52ab00","impliedFormat":1},{"version":"4732aec92b20fb28c5fe9ad99521fb59974289ed1e45aecb282616202184064f","impliedFormat":1},{"version":"2e85db9e6fd73cfa3d7f28e0ab6b55417ea18931423bd47b409a96e4a169e8e6","impliedFormat":1},{"version":"c46e079fe54c76f95c67fb89081b3e399da2c7d109e7dca8e4b58d83e332e605","impliedFormat":1},{"version":"bf67d53d168abc1298888693338cb82854bdb2e69ef83f8a0092093c2d562107","impliedFormat":1},{"version":"b52476feb4a0cbcb25e5931b930fc73cb6643fb1a5060bf8a3dda0eeae5b4b68","affectsGlobalScope":true,"impliedFormat":1},{"version":"e2677634fe27e87348825bb041651e22d50a613e2fdf6a4a3ade971d71bac37e","impliedFormat":1},{"version":"7394959e5a741b185456e1ef5d64599c36c60a323207450991e7a42e08911419","impliedFormat":1},{"version":"8c0bcd6c6b67b4b503c11e91a1fb91522ed585900eab2ab1f61bba7d7caa9d6f","impliedFormat":1},{"version":"8cd19276b6590b3ebbeeb030ac271871b9ed0afc3074ac88a94ed2449174b776","affectsGlobalScope":true,"impliedFormat":1},{"version":"696eb8d28f5949b87d894b26dc97318ef944c794a9a4e4f62360cd1d1958014b","impliedFormat":1},{"version":"3f8fa3061bd7402970b399300880d55257953ee6d3cd408722cb9ac20126460c","impliedFormat":1},{"version":"35ec8b6760fd7138bbf5809b84551e31028fb2ba7b6dc91d95d098bf212ca8b4","affectsGlobalScope":true,"impliedFormat":1},{"version":"5524481e56c48ff486f42926778c0a3cce1cc85dc46683b92b1271865bcf015a","impliedFormat":1},{"version":"68bd56c92c2bd7d2339457eb84d63e7de3bd56a69b25f3576e1568d21a162398","affectsGlobalScope":true,"impliedFormat":1},{"version":"3e93b123f7c2944969d291b35fed2af79a6e9e27fdd5faa99748a51c07c02d28","impliedFormat":1},{"version":"9d19808c8c291a9010a6c788e8532a2da70f811adb431c97520803e0ec649991","impliedFormat":1},{"version":"87aad3dd9752067dc875cfaa466fc44246451c0c560b820796bdd528e29bef40","impliedFormat":1},{"version":"4aacb0dd020eeaef65426153686cc639a78ec2885dc72ad220be1d25f1a439df","impliedFormat":1},{"version":"f0bd7e6d931657b59605c44112eaf8b980ba7f957a5051ed21cb93d978cf2f45","impliedFormat":1},{"version":"8db0ae9cb14d9955b14c214f34dae1b9ef2baee2fe4ce794a4cd3ac2531e3255","affectsGlobalScope":true,"impliedFormat":1},{"version":"15fc6f7512c86810273af28f224251a5a879e4261b4d4c7e532abfbfc3983134","impliedFormat":1},{"version":"58adba1a8ab2d10b54dc1dced4e41f4e7c9772cbbac40939c0dc8ce2cdb1d442","impliedFormat":1},{"version":"641942a78f9063caa5d6b777c99304b7d1dc7328076038c6d94d8a0b81fc95c1","impliedFormat":1},{"version":"1123a83f35cf56c97de746f0a7250012153c61a167e4a61668bf50e558162d14","impliedFormat":1},{"version":"855cd5f7eb396f5f1ab1bc0f8580339bff77b68a770f84c6b254e319bbfd1ac7","impliedFormat":1},{"version":"5650cf3dace09e7c25d384e3e6b818b938f68f4e8de96f52d9c5a1b3db068e86","impliedFormat":1},{"version":"1354ca5c38bd3fd3836a68e0f7c9f91f172582ba30ab15bb8c075891b91502b7","affectsGlobalScope":true,"impliedFormat":1},{"version":"7e20d899c28ca26a2a7afc98beaa69e63ff7fba0a8bc47b4e3bf3ede5e09e424","impliedFormat":1},{"version":"2d2fcaab481b31a5882065c7951255703ddbe1c0e507af56ea42d79ac3911201","impliedFormat":1},{"version":"a192fe8ec33f75edbc8d8f3ed79f768dfae11ff5735e7fe52bfa69956e46d78d","impliedFormat":1},{"version":"ca867399f7db82df981d6915bcbb2d81131d7d1ef683bc782b59f71dda59bc85","affectsGlobalScope":true,"impliedFormat":1},{"version":"372413016d17d804e1d139418aca0c68e47a83fb6669490857f4b318de8cccb3","affectsGlobalScope":true,"impliedFormat":1},{"version":"9e043a1bc8fbf2a255bccf9bf27e0f1caf916c3b0518ea34aa72357c0afd42ec","impliedFormat":1},{"version":"b4f70ec656a11d570e1a9edce07d118cd58d9760239e2ece99306ee9dfe61d02","impliedFormat":1},{"version":"3bc2f1e2c95c04048212c569ed38e338873f6a8593930cf5a7ef24ffb38fc3b6","impliedFormat":1},{"version":"6e70e9570e98aae2b825b533aa6292b6abd542e8d9f6e9475e88e1d7ba17c866","impliedFormat":1},{"version":"f9d9d753d430ed050dc1bf2667a1bab711ccbb1c1507183d794cc195a5b085cc","impliedFormat":1},{"version":"9eece5e586312581ccd106d4853e861aaaa1a39f8e3ea672b8c3847eedd12f6e","impliedFormat":1},{"version":"085f552d005479e2e6a7311cdbbe5d8c55c497b4d19274285df161ee9684cd9c","impliedFormat":1},{"version":"37ba7b45141a45ce6e80e66f2a96c8a5ab1bcef0fc2d0f56bb58df96ec67e972","impliedFormat":1},{"version":"45650f47bfb376c8a8ed39d4bcda5902ab899a3150029684ee4c10676d9fbaee","impliedFormat":1},{"version":"007faacc9268357caa21d24169f3f3f2497af3e9241308df2d89f6e6d9bb3f2e","affectsGlobalScope":true,"impliedFormat":1},{"version":"74cf591a0f63db318651e0e04cb55f8791385f86e987a67fd4d2eaab8191f730","impliedFormat":1},{"version":"5eab9b3dc9b34f185417342436ec3f106898da5f4801992d8ff38ab3aff346b5","impliedFormat":1},{"version":"12ed4559eba17cd977aa0db658d25c4047067444b51acfdcbf38470630642b23","affectsGlobalScope":true,"impliedFormat":1},{"version":"f3ffabc95802521e1e4bcba4c88d8615176dc6e09111d920c7a213bdda6e1d65","impliedFormat":1},{"version":"809821b8a065e3234a55b3a9d7846231ed18d66dd749f2494c66288d890daf7f","impliedFormat":1},{"version":"ae56f65caf3be91108707bd8dfbccc2a57a91feb5daabf7165a06a945545ed26","impliedFormat":1},{"version":"a136d5de521da20f31631a0a96bf712370779d1c05b7015d7019a9b2a0446ca9","impliedFormat":1},{"version":"c3b41e74b9a84b88b1dca61ec39eee25c0dbc8e7d519ba11bb070918cfacf656","affectsGlobalScope":true,"impliedFormat":1},{"version":"4737a9dc24d0e68b734e6cfbcea0c15a2cfafeb493485e27905f7856988c6b29","affectsGlobalScope":true,"impliedFormat":1},{"version":"36d8d3e7506b631c9582c251a2c0b8a28855af3f76719b12b534c6edf952748d","impliedFormat":1},{"version":"1ca69210cc42729e7ca97d3a9ad48f2e9cb0042bada4075b588ae5387debd318","impliedFormat":1},{"version":"f5ebe66baaf7c552cfa59d75f2bfba679f329204847db3cec385acda245e574e","impliedFormat":1},{"version":"ed59add13139f84da271cafd32e2171876b0a0af2f798d0c663e8eeb867732cf","affectsGlobalScope":true,"impliedFormat":1},{"version":"b7c5e2ea4a9749097c347454805e933844ed207b6eefec6b7cfd418b5f5f7b28","impliedFormat":1},{"version":"b1810689b76fd473bd12cc9ee219f8e62f54a7d08019a235d07424afbf074d25","impliedFormat":1},{"version":"2beff543f6e9a9701df88daeee3cdd70a34b4a1c11cb4c734472195a5cb2af54","impliedFormat":1},{"version":"2e07abf27aa06353d46f4448c0bbac73431f6065eef7113128a5cd804d0c384d","impliedFormat":1},{"version":"be1cc4d94ea60cbe567bc29ed479d42587bf1e6cba490f123d329976b0fe4ee5","impliedFormat":1},{"version":"42bc0e1a903408137c3df2b06dfd7e402cdab5bbfa5fcfb871b22ebfdb30bd0b","impliedFormat":1},{"version":"9894dafe342b976d251aac58e616ac6df8db91fb9d98934ff9dd103e9e82578f","impliedFormat":1},{"version":"413df52d4ea14472c2fa5bee62f7a40abd1eb49be0b9722ee01ee4e52e63beb2","impliedFormat":1},{"version":"db6d2d9daad8a6d83f281af12ce4355a20b9a3e71b82b9f57cddcca0a8964a96","impliedFormat":1},{"version":"446a50749b24d14deac6f8843e057a6355dd6437d1fac4f9e5ce4a5071f34bff","impliedFormat":1},{"version":"182e9fcbe08ac7c012e0a6e2b5798b4352470be29a64fdc114d23c2bab7d5106","impliedFormat":1},{"version":"2f4e6b4d39426a1b85ecf4bdeb9dddbf4d9b3397d95d8555d46f925c9519ec7d","impliedFormat":1},{"version":"78a2869ad0cbf3f9045dda08c0d4562b7e1b2bfe07b19e0db072f5c3c56e9584","impliedFormat":1},{"version":"89d5d28d4f57e000b836ac273079be1b75710e28ce14750d081fb420d37e2ca5","impliedFormat":1},{"version":"fd4e24ccff3966390600d7f5d6aa1fed5a512e92ada735ea5fbc933d313ad3d3","impliedFormat":1},{"version":"b7cddfe1aa6b86b5fad3c9ccb30d05b3ccb165aebbf112f48d2d8a5f69dd98b1","impliedFormat":1},{"version":"a86f82d646a739041d6702101afa82dcb935c416dd93cbca7fd754fd0282ce1f","impliedFormat":1},{"version":"ad0d1d75d129b1c80f911be438d6b61bfa8703930a8ff2be2f0e1f8a91841c64","impliedFormat":1},{"version":"bd2c7ada3dee03653d3f601011d30072194bc3970cd93208f9588fbdc0c69347","impliedFormat":1},{"version":"e480da45d32313e7174b265674da504f075f59ef326852f0c5a5d863b438ae85","impliedFormat":1},{"version":"ad54850f61fcf5d014e11be80d2f46fea9265cfa7e77456da876f7833ef81769","impliedFormat":1},{"version":"6f7c9e8bd2b5b6a080b07080065f94900bd3c7e5ebbd3047bc33fcce2fab1dd8","impliedFormat":1},{"version":"3e7efde639c6a6c3edb9847b3f61e308bf7a69685b92f665048c45132f51c218","impliedFormat":1},{"version":"df45ca1176e6ac211eae7ddf51336dc075c5314bc5c253651bae639defd5eec5","impliedFormat":1},{"version":"8a0e762ceb20c7e72504feef83d709468a70af4abccb304f32d6b9bac1129b2c","impliedFormat":1},{"version":"da5950ee2a90721df6f3fba45f5d05308f7e4c35835392215dd2cd404505e2de","impliedFormat":1},{"version":"ce75b1aebb33d510ff28af960a9221410a3eaf7f18fc5f21f9404075fba77256","impliedFormat":1},{"version":"f42d5fed19610d485c646a0c430e768115567d078c7fc855c57b0c578b3d6cd3","impliedFormat":1},{"version":"ee8df1cb8d0faaca4013a1b442e99130769ce06f438d18d510fed95890067563","impliedFormat":1},{"version":"d5630f2ad9b4541e5ce891648121022f9412ecdca1820baa1f0104f70fd7eff7","impliedFormat":1},{"version":"4d15375ab13497104bc8fe56fdef2b5fd6853f29255737d23a33fa306ff7fd69","impliedFormat":1},{"version":"2cd3fc1d0d6a1e85baffd2d4f50f5efb192b5446eef567e97c94765402f0aad4","impliedFormat":1},{"version":"e4cbf2f1e89ecccaddd2c045e600ae41b732295953fb06247c7dcbc2d281ed30","impliedFormat":1},{"version":"6dcedaef57dff0d79a05ab0ab602cde74db803d1e765468bf91263786a383e1b","impliedFormat":1},{"version":"8c1697d90c394a6fd955b98eae01238eff628e129b987a68aea10f898a48e7da","impliedFormat":1},{"version":"7580e62139cb2b44a0270c8d01abcbfcba2819a02514a527342447fa69b34ef1","impliedFormat":1},{"version":"b838d4c72740eb0afd284bf7575b74c624b105eff2e8c7b4aeead57e7ac320ff","impliedFormat":1},{"version":"f374cb24e93e7798c4d9e83ff872fa52d2cdb36306392b840a6ddf46cb925cb6","impliedFormat":1},{"version":"d10d63718e1646c2279e3b33831f82c60e31f622b2b7020f1196409ca4c09242","impliedFormat":1},{"version":"106c6025f1d99fd468fd8bf6e5bda724e11e5905a4076c5d29790b6c3745e50c","impliedFormat":1},{"version":"e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855","impliedFormat":1},{"version":"148679c6d0f449210a96e7d2e562d589e56fcde87f843a92808b3ff103f1a774","impliedFormat":1},{"version":"e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855","impliedFormat":1},{"version":"02436d7e9ead85e09a2f8e27d5f47d9464bced31738dec138ca735390815c9f0","impliedFormat":1},{"version":"f8d5ff8eafd37499f2b6a98659dd9b45a321de186b8db6b6142faed0fea3de77","impliedFormat":1},{"version":"c86fe861cf1b4c46a0fb7d74dffe596cf679a2e5e8b1456881313170f092e3fa","impliedFormat":1},{"version":"a22dd55aa4d39906252000ab8e8a1b83b195eef7f4274eb51e457c1f11cf6580","impliedFormat":1},{"version":"540cc83ab772a2c6bc509fe1354f314825b5dba3669efdfbe4693ecd3048e34f","impliedFormat":1},{"version":"121b0696021ab885c570bbeb331be8ad82c6efe2f3b93a6e63874901bebc13e3","impliedFormat":1},{"version":"612d9da66bb046a9c1e2e8d026245ded881fc4b9f98cbfae714415d57ee0ae0b","impliedFormat":1},{"version":"32c2ad9494dad5d11b0564a619fee18f388db6c1e9e2cd3c360b3122549691eb","impliedFormat":1},{"version":"6c301d40aec56a74ec7bd7324e31a728dadf9bfba3e96def02938d3d973534ec","impliedFormat":1},{"version":"e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855","impliedFormat":1},{"version":"e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855","impliedFormat":1},{"version":"8e609bb71c20b858c77f0e9f90bb1319db8477b13f9f965f1a1e18524bf50881","impliedFormat":1},{"version":"8e609bb71c20b858c77f0e9f90bb1319db8477b13f9f965f1a1e18524bf50881","impliedFormat":1},{"version":"aa14cee20aa0db79f8df101fc027d929aec10feb5b8a8da3b9af3895d05b7ba2","impliedFormat":1},{"version":"493c700ac3bd317177b2eb913805c87fe60d4e8af4fb39c41f04ba81fae7e170","impliedFormat":1},{"version":"aeb554d876c6b8c818da2e118d8b11e1e559adbe6bf606cc9a611c1b6c09f670","impliedFormat":1},{"version":"acf5a2ac47b59ca07afa9abbd2b31d001bf7448b041927befae2ea5b1951d9f9","impliedFormat":1},{"version":"8e609bb71c20b858c77f0e9f90bb1319db8477b13f9f965f1a1e18524bf50881","impliedFormat":1},{"version":"d71291eff1e19d8762a908ba947e891af44749f3a2cbc5bd2ec4b72f72ea795f","impliedFormat":1},{"version":"c0480e03db4b816dff2682b347c95f2177699525c54e7e6f6aa8ded890b76be7","impliedFormat":1},{"version":"25a5f6fd3a2243c859eddc99ab5fba11d970af2fe7a5df9c32b7668f76f97b01","impliedFormat":1},{"version":"8d207e1f9d2c30d6f77dfa693f3827c3fbf0d89240297e10bdfe1041d433df68","impliedFormat":1},{"version":"b620391fe8060cf9bedc176a4d01366e6574d7a71e0ac0ab344a4e76576fcbb8","impliedFormat":1},{"version":"6ac6715916fa75a1f7ebdfeacac09513b4d904b667d827b7535e84ff59679aff","impliedFormat":1},{"version":"2652448ac55a2010a1f71dd141f828b682298d39728f9871e1cdf8696ef443fd","impliedFormat":1},{"version":"d682336018141807fb602709e2d95a192828fcb8d5ba06dda3833a8ea98f69e3","impliedFormat":1},{"version":"6124e973eab8c52cabf3c07575204efc1784aca6b0a30c79eb85fe240a857efa","impliedFormat":1},{"version":"0d891735a21edc75df51f3eb995e18149e119d1ce22fd40db2b260c5960b914e","impliedFormat":1},{"version":"3b414b99a73171e1c4b7b7714e26b87d6c5cb03d200352da5342ab4088a54c85","impliedFormat":1},{"version":"4fbd3116e00ed3a6410499924b6403cc9367fdca303e34838129b328058ede40","impliedFormat":1},{"version":"9c82171d836c47486074e4ca8e059735bf97b205e70b196535b5efd40cbe1bc5","impliedFormat":1},{"version":"48dcc919f76c040a999c0d46d2bf25ab089645ca21b837f120b222f56a86cd76","impliedFormat":1},{"version":"2f9c89cbb29d362290531b48880a4024f258c6033aaeb7e59fbc62db26819650","impliedFormat":1},{"version":"a365c4d3bed3be4e4e20793c999c51f5cd7e6792322f14650949d827fbcd170f","impliedFormat":1},{"version":"c5426dbfc1cf90532f66965a7aa8c1136a78d4d0f96d8180ecbfc11d7722f1a5","impliedFormat":1},{"version":"65a15fc47900787c0bd18b603afb98d33ede930bed1798fc984d5ebb78b26cf9","impliedFormat":1},{"version":"9d202701f6e0744adb6314d03d2eb8fc994798fc83d91b691b75b07626a69801","impliedFormat":1},{"version":"de9d2df7663e64e3a91bf495f315a7577e23ba088f2949d5ce9ec96f44fba37d","impliedFormat":1},{"version":"c7af78a2ea7cb1cd009cfb5bdb48cd0b03dad3b54f6da7aab615c2e9e9d570c5","impliedFormat":1},{"version":"1ee45496b5f8bdee6f7abc233355898e5bf9bd51255db65f5ff7ede617ca0027","impliedFormat":1},{"version":"273782b8454e78f6a8b30d2cfbf6860499c930595095fcc1689637115f0eddda","affectsGlobalScope":true,"impliedFormat":1},{"version":"3fbdd025f9d4d820414417eeb4107ffa0078d454a033b506e22d3a23bc3d9c41","affectsGlobalScope":true,"impliedFormat":1},{"version":"dba114fb6a32b355a9cfc26ca2276834d72fe0e94cd2c3494005547025015369","impliedFormat":1},{"version":"a8f8e6ab2fa07b45251f403548b78eaf2022f3c2254df3dc186cb2671fe4996d","affectsGlobalScope":true,"impliedFormat":1},{"version":"fa6c12a7c0f6b84d512f200690bfc74819e99efae69e4c95c4cd30f6884c526e","impliedFormat":1},{"version":"f1c32f9ce9c497da4dc215c3bc84b722ea02497d35f9134db3bb40a8d918b92b","impliedFormat":1},{"version":"b73c319af2cc3ef8f6421308a250f328836531ea3761823b4cabbd133047aefa","affectsGlobalScope":true,"impliedFormat":1},{"version":"e433b0337b8106909e7953015e8fa3f2d30797cea27141d1c5b135365bb975a6","impliedFormat":1},{"version":"9f9bb6755a8ce32d656ffa4763a8144aa4f274d6b69b59d7c32811031467216e","impliedFormat":1},{"version":"5c32bdfbd2d65e8fffbb9fbda04d7165e9181b08dad61154961852366deb7540","impliedFormat":1},{"version":"ddff7fc6edbdc5163a09e22bf8df7bef75f75369ebd7ecea95ba55c4386e2441","impliedFormat":1},{"version":"0c05e9842ec4f8b7bfebfd3ca61604bb8c914ba8da9b5337c4f25da427a005f2","impliedFormat":1},{"version":"faed7a5153215dbd6ebe76dfdcc0af0cfe760f7362bed43284be544308b114cf","impliedFormat":1},{"version":"7029e566b8df176f703fb59fd437a38670c7a0e02c58b2d66dfb5b2e2b2defdb","impliedFormat":1},{"version":"7f2aa4d4989a82530aaac3f72b3dceca90e9c25bee0b1a327e8a08a1262435ad","impliedFormat":1},{"version":"d96b39301d0ded3f1a27b47759676a33a02f6f5049bfcbde81e533fd10f50dcb","impliedFormat":1},{"version":"e9f147ecca73d9346a4c073432843c159ccbe50bdcb678a78f6da10eae2cecf4","impliedFormat":1},{"version":"de061f7d72bd65c06fc1419f841dfdcb29a8e22fe6fa527d1e6eb20b897d4de0","impliedFormat":1},{"version":"663beafc2446079574570cba86e9b15f986f908ddb1b01274509970126fee945","impliedFormat":1},{"version":"a3102887d5058bf4cb5b37fa6964c09e9527c42053b3b5c642b89878620748de","impliedFormat":1},{"version":"0aaaa1727edd29673d85c9b26d7ca4d54e5407a48586903c51b48b7f7d196f61","impliedFormat":1},{"version":"d35bca0b261bff02635758c48e8ab99c61c420d0dfabbcf467e847171d876b7d","impliedFormat":1},{"version":"3bc12c40d90c342ff88a3d876996c555ed5cbee5fe8c3308a240b321f401ee46","impliedFormat":1},{"version":"ba130768aae855a5477e9e148e5c879548e6e7ccbcc56fd1934c8a18ea5b7569","impliedFormat":1},{"version":"2e4f37ffe8862b14d8e24ae8763daaa8340c0df0b859d9a9733def0eee7562d9","impliedFormat":1},{"version":"d38530db0601215d6d767f280e3a3c54b2a83b709e8d9001acb6f61c67e965fc","impliedFormat":1},{"version":"6ac6715916fa75a1f7ebdfeacac09513b4d904b667d827b7535e84ff59679aff","impliedFormat":1},{"version":"b499af2054a037a162b3b72cd886f48bbf32a3502c865c6e29fac7d2ab3ce0b5","impliedFormat":1},{"version":"b83cb14474fa60c5f3ec660146b97d122f0735627f80d82dd03e8caa39b4388c","impliedFormat":1},{"version":"48773ca557b0319c2ee62ae249cf52a81709e8be139920d6479a66274de7c4ed","impliedFormat":1},{"version":"7274fbffbd7c9589d8d0ffba68157237afd5cecff1e99881ea3399127e60572f","impliedFormat":1},{"version":"b73cbf0a72c8800cf8f96a9acfe94f3ad32ca71342a8908b8ae484d61113f647","impliedFormat":1},{"version":"bae6dd176832f6423966647382c0d7ba9e63f8c167522f09a982f086cd4e8b23","impliedFormat":1},{"version":"20865ac316b8893c1a0cc383ccfc1801443fbcc2a7255be166cf90d03fac88c9","impliedFormat":1},{"version":"c9958eb32126a3843deedda8c22fb97024aa5d6dd588b90af2d7f2bfac540f23","impliedFormat":1},{"version":"461d0ad8ae5f2ff981778af912ba71b37a8426a33301daa00f21c6ccb27f8156","impliedFormat":1},{"version":"e927c2c13c4eaf0a7f17e6022eee8519eb29ef42c4c13a31e81a611ab8c95577","impliedFormat":1},{"version":"fcafff163ca5e66d3b87126e756e1b6dfa8c526aa9cd2a2b0a9da837d81bbd72","impliedFormat":1},{"version":"70246ad95ad8a22bdfe806cb5d383a26c0c6e58e7207ab9c431f1cb175aca657","impliedFormat":1},{"version":"f00f3aa5d64ff46e600648b55a79dcd1333458f7a10da2ed594d9f0a44b76d0b","impliedFormat":1},{"version":"772d8d5eb158b6c92412c03228bd9902ccb1457d7a705b8129814a5d1a6308fc","impliedFormat":1},{"version":"802e797bcab5663b2c9f63f51bdf67eff7c41bc64c0fd65e6da3e7941359e2f7","impliedFormat":1},{"version":"b01bd582a6e41457bc56e6f0f9de4cb17f33f5f3843a7cf8210ac9c18472fb0f","impliedFormat":1},{"version":"8b4327413e5af38cd8cb97c59f48c3c866015d5d642f28518e3a891c469f240e","impliedFormat":1},{"version":"4cceef18d7f088e797a463e90b7a9dad10c6bc667724b7686e3e740ae00122be","impliedFormat":1},{"version":"7ee86fbb3754388e004de0ef9e6505485ddfb3be7640783d6d015711c03d302d","impliedFormat":1},{"version":"cc1954b539604b1e562319119ac7e888172208b32ca873f9a357a92c826bd046","impliedFormat":1},{"version":"a67b87d0281c97dfc1197ef28dfe397fc2c865ccd41f7e32b53f647184cc7307","impliedFormat":1},{"version":"771ffb773f1ddd562492a6b9aaca648192ac3f056f0e1d997678ff97dbb6bf9b","impliedFormat":1},{"version":"43e96a3d5d1411ab40ba2f61d6a3192e58177bcf3b133a80ad2a16591611726d","impliedFormat":1},{"version":"232f70c0cf2b432f3a6e56a8dc3417103eb162292a9fd376d51a3a9ea5fbbf6f","impliedFormat":1},{"version":"bb8f2dbc03533abca2066ce4655c119bff353dd4514375beb93c08590c03e023","impliedFormat":1},{"version":"706dd95827e7ebaabda91d5db2b755233e0952d98570e9c032b0f066a15c1177","affectsGlobalScope":true,"impliedFormat":1},{"version":"0b103e9abfe82d14c0ad06a55d9f91d6747154ef7cacc73cf27ecad2bfb3afcf","impliedFormat":1},{"version":"cd9304972e6d616197fb44fce00540a904f38b54306a1951b5dbeaf3c01ab5bd","impliedFormat":1},{"version":"77438e2c397a3db78407621cfc57241a305b310ddea2c185f1d555248297f587","impliedFormat":1},{"version":"120599fd965257b1f4d0ff794bc696162832d9d8467224f4665f713a3119078b","impliedFormat":1},{"version":"43ba4f2fa8c698f5c304d21a3ef596741e8e85a810b7c1f9b692653791d8d97a","impliedFormat":1},{"version":"5433f33b0a20300cca35d2f229a7fc20b0e8477c44be2affeb21cb464af60c76","impliedFormat":1},{"version":"db036c56f79186da50af66511d37d9fe77fa6793381927292d17f81f787bb195","impliedFormat":1},{"version":"a6805fcafed712aea7759f8bc731014f9d22738c1d6ef9d43b8091d1d48346d5","impliedFormat":1},{"version":"c49469a5349b3cc1965710b5b0f98ed6c028686aa8450bcb3796728873eb923e","impliedFormat":1},{"version":"4a889f2c763edb4d55cb624257272ac10d04a1cad2ed2948b10ed4a7fda2a428","impliedFormat":1},{"version":"7bb79aa2fead87d9d56294ef71e056487e848d7b550c9a367523ee5416c44cfa","impliedFormat":1},{"version":"d88ea80a6447d7391f52352ec97e56b52ebec934a4a4af6e2464cfd8b39c3ba8","impliedFormat":1},{"version":"142617b3cdf902b69c6464c9fbd942b60ab3e733ca18c032b19e0f7e2adbefe8","impliedFormat":1},{"version":"0b603555f1881f87256ffd6344d3e3ed6d466c2e701eabf381f28be8c2125892","impliedFormat":1},{"version":"897e4f7662488e3ecc79e743bdd3b78f13bdb69a97851afa5b440c4211e32ea9","impliedFormat":1},{"version":"e2e1c6d3b2d93add5200bd7bc1a8cccb4e446836b2111ece45db8683a2c765de","impliedFormat":1},{"version":"251b03d5cd243854ce870d9a9a39f491faf69898c5d6b5eee28cc7649c57417b","impliedFormat":1},{"version":"27ff4196654e6373c9af16b6165120e2dd2169f9ad6abb5c935af5abd8c7938c","impliedFormat":1},{"version":"2c4de79f406d137390608e8c0a44fba2ff8e00bacfcae7c9d1781fef10e9440d","impliedFormat":1},{"version":"07ba23a10465791be5d22deaf5ef7de7658774ddff53721e5ea17fedea1bc721","impliedFormat":1},{"version":"dca8c645c5afeb03b1ecedbf16323f33e7d0afaa6256c8e047e6e38087a97f53","impliedFormat":1},{"version":"775f181bd4a533d6f8b5e55ec1d9f1624559720ae8a70e9432258da26b38d27c","impliedFormat":1},{"version":"796273b2edc72e78a04e86d7c58ae94d370ab93a0ddf40b1aa85a37a1c29ecd7","impliedFormat":1},{"version":"5df15a69187d737d6d8d066e189ae4f97e41f4d53712a46b2710ff9f8563ec9f","impliedFormat":1},{"version":"7715134a0cf07dd41a9da2895d708625a3a303a0385e355ecaaf0b8bfaef2550","impliedFormat":1},{"version":"6ac6715916fa75a1f7ebdfeacac09513b4d904b667d827b7535e84ff59679aff","impliedFormat":1},{"version":"622694a8522b46f6310c2a9b5d2530dde1e2854cb5829354e6d1ff8f371cf469","impliedFormat":1},{"version":"cd8ce8d68567f62dd580b3c3c37777ac3f5b81944c7417f5ea83030eab533385","impliedFormat":1},{"version":"e5c939d896565dcac0f6fbdbada11284e7728ef26a069561c09aa5aa4a788393","impliedFormat":1},{"version":"9e2739b32f741859263fdba0244c194ca8e96da49b430377930b8f721d77c000","impliedFormat":1},{"version":"a9e6c0ff3f8186fccd05752cf75fc94e147c02645087ac6de5cc16403323d870","impliedFormat":1},{"version":"49af4b52f0d4d2304c5f2c6fe5fab3e153e0acc38830d0202821b877c097dd02","impliedFormat":1},{"version":"49c346823ba6d4b12278c12c977fb3a31c06b9ca719015978cb145eb86da1c61","impliedFormat":1},{"version":"bfac6e50eaa7e73bb66b7e052c38fdc8ccfc8dbde2777648642af33cf349f7f1","impliedFormat":1},{"version":"92f7c1a4da7fbfd67a2228d1687d5c2e1faa0ba865a94d3550a3941d7527a45d","impliedFormat":1},{"version":"f53b120213a9289d9a26f5af90c4c686dd71d91487a0aa5451a38366c70dc64b","impliedFormat":1},{"version":"e68b8e5a1df7c1be2bc105141456ecba70215806e1c28bfbc5c12bfce4be6e68","impliedFormat":1},{"version":"511c8f02329808d47d00b859c532ae9115590048b17325a946c74dac48428650","impliedFormat":1},{"version":"57d67b72e06059adc5e9454de26bbfe567d412b962a501d263c75c2db430f40e","impliedFormat":1},{"version":"b5f9e66625783eefcbe3d2da074b2e7ba2066d61ce3fc6ef4f22805ad946cab4","impliedFormat":1},{"version":"e37115962d284b9f7a37c2bdd2add50f88365dde41f5e0ff591ffc48a8ec7575","impliedFormat":1},{"version":"6459054aabb306821a043e02b89d54da508e3a6966601a41e71c166e4ea1474f","impliedFormat":1},{"version":"bb37588926aba35c9283fe8d46ebf4e79ffe976343105f5c6d45f282793352b2","impliedFormat":1},{"version":"f89488602bec98a142072fae7ea5ba99431a569ff580c64b7be39896474799d8","impliedFormat":1},{"version":"bbbc47961f39a57df103cf4ca3bb8f8732b4b6678a18225a0aa76d59c466956c","impliedFormat":1},{"version":"2e6114a7dd6feeef85b2c80120fdbfb59a5529c0dcc5bfa8447b6996c97a69f5","impliedFormat":1},{"version":"2ffb043dc5163458e473b7010859f86e01dc4edffcae0a93d885d028b426a546","impliedFormat":1},{"version":"c8f004e6036aa1c764ad4ec543cf89a5c1893a9535c80ef3f2b653e370de45e6","impliedFormat":1},{"version":"dd80b1e600d00f5c6a6ba23f455b84a7db121219e68f89f10552c54ba46e4dc9","impliedFormat":1},{"version":"b064c36f35de7387d71c599bfcf28875849a1dbc733e82bd26cae3d1cd060521","impliedFormat":1},{"version":"05c7280d72f3ed26f346cbe7cbbbb002fb7f15739197cbbee6ab3fd1a6cb9347","impliedFormat":1},{"version":"8de9fe97fa9e00ec00666fa77ab6e91b35d25af8ca75dabcb01e14ad3299b150","impliedFormat":1},{"version":"04b7b2e0832dfd3c31e81df3975e8d8fda28e7ff999b0aa2932608a8f6661d5c","impliedFormat":1},{"version":"ca2d34c6ed5cbd3070b8b6f32f42ae54adcc6499c1e4b99f0a5798b3f27cc653","impliedFormat":1},{"version":"9ec68995e66dd6b9dac834bf5ae85fde802714ea2e82151a5d1d53ef01b463ef","impliedFormat":1},{"version":"5c4d626b4902f2ef8a1cc146d761d276cef988016dc674e3b98fbad70e64bc9f","impliedFormat":1},{"version":"fdfaa0aad899524962e2955287b5b991ffe3be50f64e02eb60c933ca44644a94","impliedFormat":1},{"version":"53c972a0f9bc3a4ec70fff7314123ea8cfcf75b3703046f767d2dc1eea87b2fb","impliedFormat":1},{"version":"f974e4a06953682a2c15d5bd5114c0284d5abf8bc0fe4da25cb9159427b70072","impliedFormat":1},{"version":"50256e9c31318487f3752b7ac12ff365c8949953e04568009c8705db802776fb","impliedFormat":1},{"version":"7d73b24e7bf31dfb8a931ca6c4245f6bb0814dfae17e4b60c9e194a631fe5f7b","impliedFormat":1},{"version":"d130c5f73768de51402351d5dc7d1b36eaec980ca697846e53156e4ea9911476","impliedFormat":1},{"version":"413586add0cfe7369b64979d4ec2ed56c3f771c0667fbde1bf1f10063ede0b08","impliedFormat":1},{"version":"06472528e998d152375ad3bd8ebcb69ff4694fd8d2effaf60a9d9f25a37a097a","impliedFormat":1},{"version":"7303b45138d2511035056a5901a1490ebdcbf055cbb1276f8629c5121cbe733e","impliedFormat":1},{"version":"27f874cd5327507eeff699a74567f60c1215b94509f4308633a7b01922471ed2","impliedFormat":1},{"version":"a401617604fa1f6ce437b81689563dfdc377069e4c58465dbd8d16069aede0a5","impliedFormat":1},{"version":"2c6cf04bc525caf6546e859e8ef10bfb9573837ec0bc5ec7b53a7b1b8ca72781","impliedFormat":1},{"version":"8695dec09ad439b0ceef3776ea68a232e381135b516878f0901ed2ea114fd0fe","impliedFormat":1},{"version":"304b44b1e97dd4c94697c3313df89a578dca4930a104454c99863f1784a54357","impliedFormat":1},{"version":"0a437ae178f999b46b6153d79095b60c42c996bc0458c04955f1c996dc68b971","impliedFormat":1},{"version":"74b2a5e5197bd0f2e0077a1ea7c07455bbea67b87b0869d9786d55104006784f","impliedFormat":1},{"version":"4a7baeb6325920044f66c0f8e5e6f1f52e06e6d87588d837bdf44feb6f35c664","impliedFormat":1},{"version":"87cc05fe13108f02e12da7e3efd8e360fef78d96a0c9e11408ea1b1b9fb3e03d","impliedFormat":1},{"version":"1abbf67c218d23c2ce76887caac2df6c7dab3d97ba2b65348432b876f510002a","impliedFormat":1},{"version":"1a82deef4c1d39f6882f28d275cad4c01f907b9b39be9cbc472fcf2cf051e05b","impliedFormat":1},{"version":"4b20fcf10a5413680e39f5666464859fc56b1003e7dfe2405ced82371ebd49b6","impliedFormat":1},{"version":"c06ef3b2569b1c1ad99fcd7fe5fba8d466e2619da5375dfa940a94e0feea899b","impliedFormat":1},{"version":"f7d628893c9fa52ba3ab01bcb5e79191636c4331ee5667ecc6373cbccff8ae12","impliedFormat":1},{"version":"2467b00d963828f540f4acd7910f4c04cfe4b489550e6bb682212f65583bca5b","impliedFormat":1},{"version":"854e50b93090b3f8fd6e355b074e1d24dce1ae0240f1ce46563e35fea210a6d5","impliedFormat":99},{"version":"5a16e93d5d53d987dddda1ec606c9821f6bd31d1bdf0635e05e3841312cefa8b","impliedFormat":1},{"version":"a6dba407fc287f1e25454e75028c91bbc00675f2d1c4e8b3edcc36c08611a486","impliedFormat":1},{"version":"d663134457d8d669ae0df34eabd57028bddc04fc444c4bc04bc5215afc91e1f4","impliedFormat":1},{"version":"e91f7b1344577a02f051b9b471f33044fef8334a76dc9e1de003d17595a5219b","impliedFormat":1},{"version":"c0723195c85e19656d6b5b9fdb81d3f3403c1ae4679e722c6ea058c516b38d12","impliedFormat":1},{"version":"b55eb9f72166093b5460d34b34f5d8699c968de3bc3fc696e40f2c93f2ebf650","impliedFormat":1},{"version":"71d9eb4c4e99456b78ae182fb20a5dfc20eb1667f091dbb9335b3c017dd1c783","impliedFormat":1},{"version":"cfa846a7b7847a1d973605fbb8c91f47f3a0f0643c18ac05c47077ebc72e71c7","impliedFormat":1},{"version":"1594da19968752a22b2ac48c2d0e60575700e745c577a8a4a676b841238ad5bb","impliedFormat":1},{"version":"e0cee12109e0a10a4c3d6769fcc7644b7c1ea7f52365bea51728f5af29f8a137","impliedFormat":1},{"version":"7d4254b4c6c67a29d5e7f65e67d72540480ac2cfb041ca484847f5ae70480b62","impliedFormat":1},{"version":"3536968defef8a75514f547ead5e2e9c1e984820290ec9b00c5fdfb6ef786535","impliedFormat":1},{"version":"d83773870080c30a230e322ce13a9c6f3398e8dacea4ea8a83e26370f3bac23e","impliedFormat":1},{"version":"dcfeaf98d66314fec29a9076c4290e45d0b196a65827becc19138e9c7b855f37","impliedFormat":1},{"version":"6849fe9210fe4946d5f085bfed36758f33dc6ae15a751338d178dd4daa017c46","impliedFormat":1},{"version":"888cda0fa66d7f74e985a3f7b1af1f64b8ff03eb3d5e80d051c3cbdeb7f32ab7","impliedFormat":1},{"version":"60681e13f3545be5e9477acb752b741eae6eaf4cc01658a25ec05bff8b82a2ef","impliedFormat":1},{"version":"ffae4e1e06aa848a1e4bcef162cd1c48e5909b26223515981310af9c036bdfc7","impliedFormat":1},{"version":"a57b1802794433adec9ff3fed12aa79d671faed86c49b09e02e1ac41b4f1d33a","impliedFormat":1},{"version":"34e16eb7c31768a11a08aebcfb3d70d7b8f0b016197e98d8419e566ceae6d6c8","impliedFormat":1},{"version":"f94ec1f7e4b709d26960306c9082a7a1b728a6e13089346aa48ba57c74cbf47e","impliedFormat":1},{"version":"9a11cb4033405e96c247cd5aa29790212aaffdd127869e8a5219103f0b389fd5","impliedFormat":1},{"version":"01479d9d5a5dda16d529b91811375187f61a06e74be294a35ecce77e0b9e8d6c","impliedFormat":1},{"version":"aff5213585cb72e94054dfe17250ff315f3569b3919d1ef1ad235f37c4ee894e","impliedFormat":1},{"version":"fb2ea35e1be6388d722d7725e2b49c697d34d9c890c3b96758faaeb86d35cef8","impliedFormat":1},{"version":"ce0df82a9ae6f914ba08409d4d883983cc08e6d59eb2df02d8e4d68309e7848b","impliedFormat":1},{"version":"1a4dc28334a926d90ba6a2d811ba0ff6c22775fcc13679521f034c124269fd40","impliedFormat":1},{"version":"f05315ff85714f0b87cc0b54bcd3dde2716e5a6b99aedcc19cad02bf2403e08c","impliedFormat":1},{"version":"5fad3b31fc17a5bc58095118a8b160f5260964787c52e7eb51e3d4fcf5d4a6f0","impliedFormat":1},{"version":"72105519d0390262cf0abe84cf41c926ade0ff475d35eb21307b2f94de985778","impliedFormat":1},{"version":"456006a6975b26c0a1785feddae165f6d307e2d601ffde27e21fc4a790e448a4","impliedFormat":1},{"version":"c857e0aae3f5f444abd791ec81206020fbcc1223e187316677e026d1c1d6fe08","impliedFormat":1},{"version":"ccf6dd45b708fb74ba9ed0f2478d4eb9195c9dfef0ff83a6092fa3cf2ff53b4f","impliedFormat":1},{"version":"1fe0d18b111e1145a7e7601855bccd4ca20f24e3b9a5aba6bb1fa9d1a7059170","impliedFormat":1},{"version":"5632c3c26d420c063eebe64c45b1248b9492a67bf44f1d0c57e9dc8f6cf449bb","impliedFormat":1},{"version":"0df5aa619ab12993a39ea6dae062ee46eadbb4d738916460e636ada52bced75b","impliedFormat":1},{"version":"8fca3039857709484e5893c05c1f9126ab7451fa6c29e19bb8c2411a2e937345","impliedFormat":1},{"version":"35069c2c417bd7443ae7c7cafd1de02f665bf015479fec998985ffbbf500628c","impliedFormat":1},{"version":"10ab7be91f87ebe8916b62cf28af2e45b5601fc7b0e311adf838f912c6b31dd8","impliedFormat":1},{"version":"bc636fbc08e0979ceb7eb0731a33000283d77a33b62e1f71ee65be50394e40ba","impliedFormat":1},{"version":"7e0b7f91c5ab6e33f511efc640d36e6f933510b11be24f98836a20a2dc914c2d","impliedFormat":1},{"version":"045b752f44bf9bbdcaffd882424ab0e15cb8d11fa94e1448942e338c8ef19fba","impliedFormat":1},{"version":"2894c56cad581928bb37607810af011764a2f511f575d28c9f4af0f2ef02d1ab","impliedFormat":1},{"version":"0a72186f94215d020cb386f7dca81d7495ab6c17066eb07d0f44a5bf33c1b21a","impliedFormat":1},{"version":"75bbd3be047d539988a0ff0b56384ef7a6a25f3b676ad96bee547d44c31622a7","impliedFormat":1},{"version":"42960001a776b089ade681ab5cfddc936e0afb0615133ec1841f3dee89d3e1bf","impliedFormat":1},{"version":"0aedb02516baf3e66b2c1db9fef50666d6ed257edac0f866ea32f1aa05aa474f","impliedFormat":1},{"version":"da47712b394d944328245482603bc6f416d3949b67c9392279caab595076b510","affectsGlobalScope":true,"impliedFormat":1},{"version":"37d0071d8f0a06dc55c2c5e0ec3391affd4fd107c53410bf358196ec0bf3923f","impliedFormat":1},{"version":"b213dad76ca37fd552274c9499056e1c0d9c1bd38a55bb7f68b22ba6b84c3ad7","impliedFormat":1},{"version":"c30436b130b6218b7714314dc41d3f459590db4bdf099eecd51cb1bda32109a8","impliedFormat":1},{"version":"20fa37b636fdcc1746ea0738f733d0aed17890d1cd7cb1b2f37010222c23f13e","impliedFormat":1},{"version":"d90b9f1520366d713a73bd30c5a9eb0040d0fb6076aff370796bc776fd705943","impliedFormat":1},{"version":"bc03c3c352f689e38c0ddd50c39b1e65d59273991bfc8858a9e3c0ebb79c023b","impliedFormat":1},{"version":"19df3488557c2fc9b4d8f0bac0fd20fb59aa19dec67c81f93813951a81a867f8","affectsGlobalScope":true,"impliedFormat":1},{"version":"b25350193e103ae90423c5418ddb0ad1168dc9c393c9295ef34980b990030617","affectsGlobalScope":true,"impliedFormat":1},{"version":"bef86adb77316505c6b471da1d9b8c9e428867c2566270e8894d4d773a1c4dc2","impliedFormat":1},{"version":"5a49adaef698b7ad7e6127949fa1b0bbd3d46b7cbd11c54e392a4dcdd51f5190","impliedFormat":1},{"version":"6ee598cdfdd0fa52039dca135b3dfff7b49035dc13292143e0a93843e3861967","impliedFormat":1},{"version":"27be6622e2922a1b412eb057faa854831b95db9db5035c3f6d4b677b902ab3b7","impliedFormat":1},{"version":"5c634644d45a1b6bc7b05e71e05e52ec04f3d73d9ac85d5927f647a5f965181a","impliedFormat":1},{"version":"2489bf04d77dc025ba67f49f1a56eb24b9db477d5ff88123d887e163ed1776aa","impliedFormat":1},{"version":"63a7595a5015e65262557f883463f934904959da563b4f788306f699411e9bac","impliedFormat":1},{"version":"4ba137d6553965703b6b55fd2000b4e07ba365f8caeb0359162ad7247f9707a6","impliedFormat":1},{"version":"0b77b819b5417775fccb20c678293cf614c054a5b1a65421a5b933a9124ba998","impliedFormat":1},{"version":"eb5acb58487367e502d994b57e2c58255d8241f481ea8efa8e79af23af3f41c2","impliedFormat":1},{"version":"9252d498a77517aab5d8d4b5eb9d71e4b225bbc7123df9713e08181de63180f6","impliedFormat":1},{"version":"b1f1d57fde8247599731b24a733395c880a6561ec0c882efaaf20d7df968c5af","impliedFormat":1},{"version":"f282cb0bc62e0cc771d4c2e7ece6359a5f4a3dff664584e97476fd37154816bb","impliedFormat":1},{"version":"35e6379c3f7cb27b111ad4c1aa69538fd8e788ab737b8ff7596a1b40e96f4f90","impliedFormat":1},{"version":"1fffe726740f9787f15b532e1dc870af3cd964dbe29e191e76121aa3dd8693f2","impliedFormat":1},{"version":"5a3ea721d03a361ccbdd7390ccd75f6e84cbca3a3f01f4b331ecc9af31890c49","impliedFormat":1},{"version":"e7dfaee4af38d45b1cab8a1ee0b3bc1f85ddcf64545ed391d675d78ae6526274","affectsGlobalScope":true,"impliedFormat":1},{"version":"e8daa443eaf9a27fd382cc1f8ebe30330c0f4d89511cfb469166874806751d35","impliedFormat":1},{"version":"af48e58339188d5737b608d41411a9c054685413d8ae88b8c1d0d9bfabdf6e7e","impliedFormat":1},{"version":"616775f16134fa9d01fc677ad3f76e68c051a056c22ab552c64cc281a9686790","impliedFormat":1},{"version":"65c24a8baa2cca1de069a0ba9fba82a173690f52d7e2d0f1f7542d59d5eb4db0","impliedFormat":1},{"version":"f9fe6af238339a0e5f7563acee3178f51db37f32a2e7c09f85273098cee7ec49","impliedFormat":1},{"version":"1de8c302fd35220d8f29dea378a4ae45199dc8ff83ca9923aca1400f2b28848a","impliedFormat":1},{"version":"77e71242e71ebf8528c5802993697878f0533db8f2299b4d36aa015bae08a79c","impliedFormat":1},{"version":"98a787be42bd92f8c2a37d7df5f13e5992da0d967fab794adbb7ee18370f9849","impliedFormat":1},{"version":"332248ee37cca52903572e66c11bef755ccc6e235835e63d3c3e60ddda3e9b93","impliedFormat":1},{"version":"94e8cc88ae2ef3d920bb3bdc369f48436db123aa2dc07f683309ad8c9968a1e1","impliedFormat":1},{"version":"4545c1a1ceca170d5d83452dd7c4994644c35cf676a671412601689d9a62da35","impliedFormat":1},{"version":"320f4091e33548b554d2214ce5fc31c96631b513dffa806e2e3a60766c8c49d9","impliedFormat":1},{"version":"a2d648d333cf67b9aeac5d81a1a379d563a8ffa91ddd61c6179f68de724260ff","impliedFormat":1},{"version":"d90d5f524de38889d1e1dbc2aeef00060d779f8688c02766ddb9ca195e4a713d","impliedFormat":1},{"version":"07ed3ddab975995eea41b22f3010506fb9f5fb301d04820b07d7a1aee5477d7c","impliedFormat":1},{"version":"969d8b0965849f4bae7cab0ba90bd1e1220e95999c2c6f01117fa7500901c017","impliedFormat":1},{"version":"6ec840ee5e2bc103f557fe38b1d585ee250540468713d7634ee066de372bf332","impliedFormat":1},{"version":"b0309e1eda99a9e76f87c18992d9c3689b0938266242835dd4611f2b69efe456","impliedFormat":1},{"version":"47699512e6d8bebf7be488182427189f999affe3addc1c87c882d36b7f2d0b0e","impliedFormat":1},{"version":"6ceb10ca57943be87ff9debe978f4ab73593c0c85ee802c051a93fc96aaf7a20","impliedFormat":1},{"version":"1de3ffe0cc28a9fe2ac761ece075826836b5a02f340b412510a59ba1d41a505a","impliedFormat":1},{"version":"e46d6cc08d243d8d0d83986f609d830991f00450fb234f5b2f861648c42dc0d8","impliedFormat":1},{"version":"1c0a98de1323051010ce5b958ad47bc1c007f7921973123c999300e2b7b0ecc0","impliedFormat":1},{"version":"ff863d17c6c659440f7c5c536e4db7762d8c2565547b2608f36b798a743606ca","impliedFormat":1},{"version":"5412ad0043cd60d1f1406fc12cb4fb987e9a734decbdd4db6f6acf71791e36fe","impliedFormat":1},{"version":"ad036a85efcd9e5b4f7dd5c1a7362c8478f9a3b6c3554654ca24a29aa850a9c5","impliedFormat":1},{"version":"fedebeae32c5cdd1a85b4e0504a01996e4a8adf3dfa72876920d3dd6e42978e7","impliedFormat":1},{"version":"e297c0a524edee7677939122f90027bfbe5f2698939d9a85728e5044b39c7124","impliedFormat":1},{"version":"cdf21eee8007e339b1b9945abf4a7b44930b1d695cc528459e68a3adc39a622e","impliedFormat":1},{"version":"bc9ee0192f056b3d5527bcd78dc3f9e527a9ba2bdc0a2c296fbc9027147df4b2","impliedFormat":1},{"version":"b62381cae176db34f003cc6172ee8f3e0122014889d66391aa73698105cf4934","impliedFormat":1},{"version":"1d9c0a9a6df4e8f29dc84c25c5aa0bb1da5456ebede7a03e03df08bb8b27bae6","impliedFormat":1},{"version":"84380af21da938a567c65ef95aefb5354f676368ee1a1cbb4cae81604a4c7d17","impliedFormat":1},{"version":"1af3e1f2a5d1332e136f8b0b95c0e6c0a02aaabd5092b36b64f3042a03debf28","impliedFormat":1},{"version":"30d8da250766efa99490fc02801047c2c6d72dd0da1bba6581c7e80d1d8842a4","impliedFormat":1},{"version":"03566202f5553bd2d9de22dfab0c61aa163cabb64f0223c08431fb3fc8f70280","impliedFormat":1},{"version":"41eb514d9ce0a6e87957f08a4b7af70d93f87637f37dee706e2d92a6601c25a9","impliedFormat":1},{"version":"e7765aa8bcb74a38b3230d212b4547686eb9796621ffb4367a104451c3f9614f","impliedFormat":1},{"version":"1de80059b8078ea5749941c9f863aa970b4735bdbb003be4925c853a8b6b4450","impliedFormat":1},{"version":"1d079c37fa53e3c21ed3fa214a27507bda9991f2a41458705b19ed8c2b61173d","impliedFormat":1},{"version":"5bf5c7a44e779790d1eb54c234b668b15e34affa95e78eada73e5757f61ed76a","impliedFormat":1},{"version":"5835a6e0d7cd2738e56b671af0e561e7c1b4fb77751383672f4b009f4e161d70","impliedFormat":1},{"version":"4b7f74b772140395e7af67c4841be1ab867c11b3b82a51b1aeb692822b76c872","impliedFormat":1},{"version":"7bd01f0f28cd3aeb2046274d85208e245965f6f2948edf4f7b2057bcf9f22ccc","impliedFormat":99},{"version":"d2f2cf2b8cc92bea913cda4a076e0f790b23a21e84f989d12f0116a7fe3906e0","impliedFormat":99},{"version":"6de125ea94866c736c6d58d68eb15272cf7d1020a5b459fea1c660027eca9a90","affectsGlobalScope":true,"impliedFormat":1},{"version":"f5b20bc288ee49989c95b20847fc93b96bf61cc0845598897a6a53a967dd7d07","affectsGlobalScope":true,"impliedFormat":1},{"version":"064ac1c2ac4b2867c2ceaa74bbdce0cb6a4c16e7c31a6497097159c18f74aa7c","impliedFormat":1},{"version":"3dc14e1ab45e497e5d5e4295271d54ff689aeae00b4277979fdd10fa563540ae","impliedFormat":1},{"version":"d3b315763d91265d6b0e7e7fa93cfdb8a80ce7cdd2d9f55ba0f37a22db00bdb8","impliedFormat":1},{"version":"b789bf89eb19c777ed1e956dbad0925ca795701552d22e68fd130a032008b9f9","impliedFormat":1},{"version":"10985be809793f413a3289e8c150675d6d3312b6ff7180f156955d9eeb06f3a8","affectsGlobalScope":true},"083e23c4c5e7761db151134ea1ef7896120c86c5888cdc8a861f534f7e86d6fd",{"version":"d39a6aa806ba0839e7bd858138bb3ba1b84745f5ee6d60ab773504f6c923726f","impliedFormat":1},{"version":"0fd641a3b3e3ec89058051a284135a3f30b94a325fb809c4e4159ec5495b5cdc","impliedFormat":1},{"version":"035a5df183489c2e22f3cf59fc1ed2b043d27f357eecc0eb8d8e840059d44245","impliedFormat":1},{"version":"0d14fa22c41fdc7277e6f71473b20ebc07f40f00e38875142335d5b63cdfc9d2","impliedFormat":1},{"version":"a4809f4d92317535e6b22b01019437030077a76fec1d93b9881c9ed4738fcc54","impliedFormat":1},{"version":"5f53fa0bd22096d2a78533f94e02c899143b8f0f9891a46965294ee8b91a9434","impliedFormat":1},{"version":"bae8d023ef6b23df7da26f51cea44321f95817c190342a36882e93b80d07a960","impliedFormat":1},{"version":"26a770cec4bd2e7dbba95c6e536390fffe83c6268b78974a93727903b515c4e7","impliedFormat":1},{"version":"dd5115b329c19c4385af13eda13e3ab03355e711c3f313173fd54ed7d08cfd39","impliedFormat":99},{"version":"b104e2da53231a529373174880dc0abfbc80184bb473b6bf2a9a0746bebb663d","impliedFormat":99},{"version":"3d4bb4d84af5f0b348f01c85537da1c7afabc174e48806c8b20901377c57b8e4","impliedFormat":99},{"version":"a2500b15294325d9784a342145d16ef13d9efb1c3c6cb4d89934b2c0d521b4ab","impliedFormat":99},{"version":"79d5c409e84764fabdd276976a31928576dcf9aea37be3b5a81f74943f01f3ff","impliedFormat":99},{"version":"8ea020ea63ecc981b9318fc532323e31270c911a7ade4ba74ab902fcf8281c45","impliedFormat":99},{"version":"c81e1a9b03e4de1225b33ac84aaf50a876837057828e0806d025daf919bf2d51","impliedFormat":99},{"version":"bb7264d8bd6152524f2ef5dae5c260ae60d459bf406202258bd0ce57c79e5a6d","impliedFormat":99},{"version":"fb66165c4976bc21a4fde14101e36c43d46f907489b7b6a5f2a2679108335d4a","impliedFormat":99},{"version":"628c2e0a0b61be3e44f296083e6af9b5a9b6881037dd43e7685ee473930a4404","impliedFormat":99},{"version":"4776f1e810184f538d55c5da92da77f491999054a1a1ee69a2d995ab2e8d1bc0","impliedFormat":99},{"version":"11544c4e626eab113df9432e97a371693c98c17ae4291d2ad425af5ef00e580b","impliedFormat":99},{"version":"e1847b81166d25f29213d37115253c5b82ec9ee78f19037592aa173e017636d5","impliedFormat":99},{"version":"fe0bd60f36509711c4a69c0e00c0111f5ecdc685e6c1a2ae99bd4d56c76c07fc","impliedFormat":99},{"version":"b8f3f4ee9aae88a9cec9797d166209eb2a7e4beb8a15e0fc3c8b90c9682c337d","impliedFormat":99},{"version":"ea3c4f5121fe2e86101c155ebe60b435c729027ae50025b2a4e1d12a476002ae","impliedFormat":99},{"version":"372db10bea0dbe1f8588f82b339152b11847e6a4535d57310292660c8a9acfc5","impliedFormat":99},{"version":"6f9fba6349c16eed21d139d5562295e8d5aafa5abe6e8ebcde43615a80c69ac1","impliedFormat":99},{"version":"1474533e27d0e3e45a417ea153d4612f0adbff055f244a29606a1fae6db56cda","impliedFormat":99},{"version":"c7fd8a79d0495955d55bfea34bbdb85235b0f27b417a81afc395655ef43d091d","impliedFormat":99},{"version":"987405949bfafbb1c93d976c3352fe33bfb85303a79fc5d9588b681e4af6c3b3","impliedFormat":99},{"version":"867bc1f5a168fd86d12d828dfafd77c557f13b4326588615b19e301f6856f70c","impliedFormat":99},{"version":"6beddab08d635b4c16409a748dcd8de38a8e444a501b8e79d89f458ae88579d1","impliedFormat":99},{"version":"1dea5c7bf28569228ffcc83e69e1c759e7f0133c232708e09cfa4d7ed3ec7079","impliedFormat":99},{"version":"6114545678bb75e581982c990597ca3ba7eeef185256a14c906edfc949db2cd1","impliedFormat":99},{"version":"5c8625f8dbbd94ab6ca171d621049c810cce4fce6ec1fd1c24c331d9858dce17","impliedFormat":99},{"version":"af36e5f207299ba2013f981dffacd4a04cdce2dd4bd255fff084e7257bf8b947","impliedFormat":99},{"version":"c69c720b733cdaa3b4542f4c1206d9f0fcf3696f87a6e88adb15db6882fbcd69","impliedFormat":99},{"version":"9c37e66916cbbe7d96301934b665ec712679c3cb99081ccaae4034b987533a59","impliedFormat":99},{"version":"2e1a163ab5b5c2640d7f5a100446bbcaeda953a06439c901b2ae307f7088dc30","impliedFormat":99},{"version":"f0b3406d2bc2c262f218c42a125832e026997278a890ef3549fa49e62177ce86","impliedFormat":99},{"version":"756cf223ca25eb36c413b2a286fa108f19a5ac39dc6d65f2c590dc118f6150df","impliedFormat":99},{"version":"70ce03da8740ca786a1a78b8a61394ecf812dd1acf2564d0ce6be5caf29e58d9","impliedFormat":99},{"version":"e0f5707d91bb950edb6338e83dd31b6902b6620018f6aa5fd0f504c2b0ea61f5","impliedFormat":99},{"version":"0dc7ae20eab8097b0c7a48b5833f6329e976f88af26055cdae6337141ff2c12e","impliedFormat":99},{"version":"76b6db79c0f5b326ff98b15829505efd25d36ce436b47fe59781ac9aec0d7f1b","impliedFormat":99},{"version":"786f3f186af874ea3e34c2aeef56a0beab90926350f3375781c0a3aa844cd76e","impliedFormat":99},{"version":"63dbc8fa1dcbfb8af6c48f004a1d31988f42af171596c5cca57e4c9d5000d291","impliedFormat":99},{"version":"aa235b26568b02c10d74007f577e0fa21a266745029f912e4fba2c38705b3abe","impliedFormat":99},{"version":"3d6d570b5f36cf08d9ad8d93db7ddc90fa7ccc0c177de2e9948bb23cde805d32","impliedFormat":99},{"version":"9a60faaa0d582db70f85a94a3439bd83720a9468928b76b4db561a1a0137fa90","impliedFormat":99},{"version":"627e2ac450dcd71bdd8c1614b5d3a02b214ad92a1621ebeb2642dffb9be93715","impliedFormat":99},{"version":"813514ef625cb8fc3befeec97afddfb3b80b80ced859959339d99f3ad538d8fe","impliedFormat":99},{"version":"624f8a7a76f26b9b0af9524e6b7fa50f492655ab7489c3f5f0ddd2de5461b0c3","impliedFormat":99},{"version":"d6b6fa535b18062680e96b2f9336e301312a2f7bdaeb47c4a5b3114c3de0c08b","impliedFormat":99},{"version":"818e8f95d3851073e92bcad7815367dd8337863aaf50d79e703ac479cca0b6a4","impliedFormat":99},{"version":"29b716ff24d0db64060c9a90287f9de2863adf0ef1efef71dbaba33ebc20b390","impliedFormat":99},{"version":"2530c36527a988debd39fed6504d8c51a3e0f356aaf2d270edd492f4223bdeff","impliedFormat":99},{"version":"2553cfd0ec0164f3ea228c5badd1ba78607d034fc2dec96c781026a28095204b","impliedFormat":99},{"version":"6e943693dbc91aa2c6c520e7814316469c8482d5d93df51178d8ded531bb29ee","impliedFormat":99},{"version":"e74e1249b69d9f49a6d9bfa5305f2a9f501e18de6ab0829ab342abf6d55d958b","impliedFormat":99},{"version":"16f60d6924a9e0b4b9961e42b5e586b28ffd57cdfa236ae4408f7bed9855a816","impliedFormat":99},{"version":"493c2d42f1b6cfe3b13358ff3085b90fa9a65d4858ea4d02d43772c0795006ec","impliedFormat":99},{"version":"3702c7cbcd937d7b96e5376fe562fd77b4598fe93c7595ee696ebbfefddac70f","impliedFormat":99},{"version":"848621f6b65b3963f86c51c8b533aea13eadb045da52515e6e1407dea19b8457","impliedFormat":99},{"version":"c15b679c261ce17551e17a40a42934aeba007580357f1a286c79e8e091ee3a76","impliedFormat":99},{"version":"156108cedad653a6277b1cb292b18017195881f5fe837fb7f9678642da8fa8f2","impliedFormat":99},{"version":"0a0bb42c33e9faf63e0b49a429e60533ab392f4f02528732ecbd62cfc2d54c10","impliedFormat":99},{"version":"70fa95cd7cb511e55c9262246de1f35f3966c50e8795a147a93c538db824cdc8","impliedFormat":99},{"version":"bc28d8cec56b5f91c8a2ec131444744b13f63c53ce670cb31d4dffdfc246ba34","impliedFormat":99},{"version":"7bd87c0667376e7d6325ada642ec29bf28e940cb146d21d270cac46b127e5313","impliedFormat":99},{"version":"0318969deede7190dd3567433a24133f709874c5414713aac8b706a5cb0fe347","impliedFormat":99},{"version":"3770586d5263348c664379f748428e6f17e275638f8620a60490548d1fada8b4","impliedFormat":99},{"version":"ff65e6f720ba4bf3da5815ca1c2e0df2ece2911579f307c72f320d692410e03d","impliedFormat":99},{"version":"edb4f17f49580ebcec71e1b7217ad1139a52c575e83f4f126db58438a549b6df","impliedFormat":99},{"version":"353c0cbb6e39e73e12c605f010fddc912c8212158ee0c49a6b2e16ede22cdaab","impliedFormat":99},{"version":"e125fdbea060b339306c30c33597b3c677e00c9e78cd4bf9a15b3fb9474ebb5d","impliedFormat":99},{"version":"ee141f547382d979d56c3b059fc12b01a88b7700d96f085e74268bc79f48c40a","impliedFormat":99},{"version":"1d64132735556e2a1823044b321c929ad4ede45b81f3e04e0e23cf76f4cbf638","impliedFormat":99},{"version":"8b4a3550a3cac035fe928701bc046f5fac76cca32c7851376424b37312f4b4ca","impliedFormat":99},{"version":"5fd7f9b36f48d6308feba95d98817496274be1939a9faa5cd9ed0f8adf3adf3a","impliedFormat":99},{"version":"15a8f79b1557978d752c0be488ee5a70daa389638d79570507a3d4cfc620d49d","impliedFormat":99},{"version":"d4c14ea7d76619ef4244e2c220c2caeec78d10f28e1490eeac89df7d2556b79f","impliedFormat":99},{"version":"8096207a00346207d9baf7bc8f436ef45a20818bf306236a4061d6ccc45b0372","impliedFormat":99},{"version":"040f2531989793c4846be366c100455789834ba420dfd6f36464fe73b68e35b6","impliedFormat":99},{"version":"c5c7020a1d11b7129eb8ddffb7087f59c83161a3792b3560dcd43e7528780ab0","impliedFormat":99},{"version":"d1f97ea020060753089059e9b6de1ab05be4cb73649b595c475e2ec197cbce0f","impliedFormat":99},{"version":"b5ddca6fd676daf45113412aa2b8242b8ee2588e99d68c231ab7cd3d88b392fa","impliedFormat":99},{"version":"77404ec69978995e3278f4a2d42940acbf221da672ae9aba95ffa485d0611859","impliedFormat":99},{"version":"4e6672fb142798b69bcb8d6cd5cc2ec9628dbea9744840ee3599b3dcd7b74b09","impliedFormat":99},{"version":"609653f5b74ef61422271a28dea232207e7ab8ad1446de2d57922e3678160f01","impliedFormat":99},{"version":"9f96251a94fbff4038b464ee2d99614bca48e086e1731ae7a2b5b334826d3a86","impliedFormat":99},{"version":"cacbb7f3e679bdea680c6c609f4403574a5de8b66167b8867967083a40821e2a","impliedFormat":99},{"version":"ee4cf97e8bad27c9e13a17a9f9cbd86b32e9fbc969a5c3f479dafb219209848c","impliedFormat":99},{"version":"3a4e35b6e99ed398e77583ffc17f8774cb4253f8796c0e04ce07c26636fed4a9","impliedFormat":99},{"version":"08d323cb848564baef1ecbe29df14f7ad84e5b2eaf2e02ea8cb422f069dcb2fa","impliedFormat":99},{"version":"a05b53646fa669b87d8b97c1fb7c0183d771680fdd1276b12e68bed4e84cf556","impliedFormat":99},{"version":"c3b9c02a31b36dd3a4067f420316c550f93d463e46b2704391100428e145fd7f","impliedFormat":99},{"version":"b2a4d01fcf005530c3f8689ac0197e5fd6b75eb031e73ca39e5a27d41793a5d8","impliedFormat":99},{"version":"e99d9167596f997dd2da0de0751a9f0e2f4100f07bddf049378719191aee87f6","impliedFormat":99},{"version":"40cc853264e24e0578580194c76e25628acdd1111b54ec8abf59b834c4942839","impliedFormat":99},{"version":"403971c465292dedc8dff308f430c6b69ec5e19ea98d650dae40c70f2399dc14","impliedFormat":99},{"version":"fd3774aa27a30b17935ad360d34570820b26ec70fa5fcfd44c7e884247354d37","impliedFormat":99},{"version":"7b149b38e54fe0149fe500c5d5a049654ce17b1705f6a1f72dd50d84c6a678b9","impliedFormat":99},{"version":"3eb76327823b6288eb4ed4648ebf4e75cf47c6fbc466ed920706b801399f7dc3","impliedFormat":99},{"version":"c6a219d0d39552594a4cc75970768004f99684f28890fc36a42b853af04997b7","impliedFormat":99},{"version":"2110d74b178b022ca8c5ae8dcc46e759c34cf3b7e61cb2f8891fd8d24cb614ef","impliedFormat":99},{"version":"38f5e025404a3108f5bb41e52cead694a86d16ad0005e0ef7718a2a31e959d1e","impliedFormat":99},{"version":"8db133d270ebb1ba3fa8e2c4ab48df2cc79cb03a705d47ca9f959b0756113d3d","impliedFormat":99},{"version":"fc9294185089a62f8287130bc100fa5ab11f3e6af8874127bbdf7600f19913ee","impliedFormat":99},{"version":"f06e5783d10123b74b14e141426a80234b9d6e5ad94bfc4850ea912719f4987c","impliedFormat":99},{"version":"de9466be4b561ad0079ac95ca7445c99fdf45ef115a93af8e2e933194b3cdf4c","impliedFormat":99},{"version":"0c1eed961c15e1242389b0497628709f59d7afd50d5a1955daa10b5bd3b68fc2","impliedFormat":99},{"version":"5e07a9f7f130e5404c202bf7b0625a624c9d266b980576f5d62608ef21d96eab","impliedFormat":99},{"version":"2f97d5063ab69bf32d6417d71765fc154dc6ff7c16700db7c4af5341a965c277","impliedFormat":99},{"version":"a8a9459dd76ef5eeef768da4ce466c5539d73b26334131bd1dd6cbd74ce48fa2","impliedFormat":99},{"version":"123ff203ffba727213e5095b9a59091cdbc9d1d94bae0d6adb98060ef410016c","impliedFormat":99},{"version":"9e4d81dd52d5a8b6c159c0b2f2b5fbe2566f12fcc81f7ba7ebb46ca604657b45","impliedFormat":99},{"version":"9ee245e7c6aa2d81ee0d7f30ff6897334842c469b0e20da24b3cddc6f635cc06","impliedFormat":99},{"version":"e7d5132674ddcd01673b0517eebc44c17f478126284c3eabd0a552514cb992bb","impliedFormat":99},{"version":"a820710a917f66fa88a27564465a033c393e1322a61eb581d1f20e0680b498f1","impliedFormat":99},{"version":"19086752f80202e6a993e2e45c0e7fc7c7fc4315c4805f3464625f54d919fa2e","impliedFormat":99},{"version":"141aebe2ee4fecd417d44cf0dabf6b80592c43164e1fbd9bfaf03a4ec377c18e","impliedFormat":99},{"version":"72c35a5291e2e913387583717521a25d15f1e77d889191440dc855c7e821b451","impliedFormat":99},{"version":"ec1c67b32d477ceeebf18bdeb364646d6572e9dd63bb736f461d7ea8510aca4f","impliedFormat":99},{"version":"fb555843022b96141c2bfaf9adcc3e5e5c2d3f10e2bcbd1b2b666bd701cf9303","impliedFormat":99},{"version":"f851083fc20ecc00ff8aaf91ba9584e924385768940654518705423822de09e8","impliedFormat":99},{"version":"c8d53cdb22eedf9fc0c8e41a1d9a147d7ad8997ed1e306f1216ed4e8daedb6b3","impliedFormat":99},{"version":"6c052f137bab4ba9ed6fd76f88a8d00484df9d5cb921614bb4abe60f51970447","impliedFormat":99},{"version":"e182c297b81a8cb2614ebf5d5d29500987deb641ea310802754d2fec3ef3ff00","impliedFormat":99},{"version":"7d5c2df0c3706f45b77970232aa3a38952561311ccc8fcb7591e1b7a469ad761","impliedFormat":99},{"version":"2c41502b030205006ea3849c83063c4327342fbf925d8ed93b18309428fdd832","impliedFormat":99},{"version":"d12eecede214f8807a719178d7d7e2fc32f227d4705d123c3f45d8a3b5765f38","impliedFormat":99},{"version":"c8893abd114f341b860622b92c9ffc8c9eb9f21f6541bd3cbc9a4aa9b1097e42","impliedFormat":99},{"version":"825674da70d892b7e32c53f844c5dfce5b15ea67ceda4768f752eed2f02d8077","impliedFormat":99},{"version":"2c676d27ef1afbc8f8e514bb46f38550adf177ae9b0102951111116fa7ea2e10","impliedFormat":99},{"version":"a6072f5111ea2058cb4d592a4ee241f88b198498340d9ad036499184f7798ae2","impliedFormat":99},{"version":"ab87c99f96d9b1bf93684b114b27191944fef9a164476f2c6c052b93eaac0a4f","impliedFormat":99},{"version":"13e48eaca1087e1268f172607ae2f39c72c831a482cab597076c6073c97a15e7","impliedFormat":99},{"version":"19597dbe4500c782a4252755510be8324451847354cd8e204079ae81ab8d0ef6","impliedFormat":99},{"version":"f7d487e5f0104f0737951510ea361bc919f5b5f3ebc51807f81ce54934a3556f","impliedFormat":99},{"version":"efa8c5897e0239017e5b53e3f465d106b00d01ee94c9ead378a33284a2998356","impliedFormat":99},{"version":"fe3c53940b26832930246d4c39d6e507c26a86027817882702cf03bff314fa1d","impliedFormat":99},{"version":"53ee33b91d4dc2787eccebdbd396291e063db1405514bb3ab446e1ca3fd81a90","impliedFormat":99},{"version":"c4a97da118b4e6dde7c1daa93c4da17f0c4eedece638fc6dcc84f4eb1d370808","impliedFormat":99},{"version":"71666363fbdb0946bfc38a8056c6010060d1a526c0584145a9560151c6962b4f","impliedFormat":99},{"version":"1326f3630d26716257e09424f33074a945940afd64f2482e2bbc885258fca6bb","impliedFormat":99},{"version":"cc2eb5b23140bbceadf000ef2b71d27ac011d1c325b0fc5ecd42a3221db5fb2e","impliedFormat":99},{"version":"d04f5f3e90755ed40b25ed4c6095b6ad13fc9ce98b34a69c8da5ed38e2dbab5a","impliedFormat":99},{"version":"280b04a2238c0636dad2f25bbbbac18cf7bb933c80e8ec0a44a1d6a9f9d69537","impliedFormat":99},{"version":"0e9a2d784877b62ad97ed31816b1f9992563fdda58380cd696e796022a46bfdf","impliedFormat":99},{"version":"1b1411e7a3729bc632d8c0a4d265de9c6cbba4dc36d679c26dad87507faedee3","impliedFormat":99},{"version":"c478cfb0a2474672343b932ea69da64005bbfc23af5e661b907b0df8eb87bcb7","impliedFormat":99},{"version":"1a7bff494148b6e66642db236832784b8b2c9f5ad9bff82de14bcdb863dadcd9","impliedFormat":99},{"version":"65e6ad2d939dd38d03b157450ba887d2e9c7fd0f8f9d3008c0d1e59a0d8a73b4","impliedFormat":99},{"version":"f72b400dbf8f27adbda4c39a673884cb05daf8e0a1d8152eec2480f5700db36c","impliedFormat":99},{"version":"347f6fe4308288802eb123596ad9caf06755e80cfc7f79bbe56f4141a8ee4c50","impliedFormat":99},{"version":"5f5baa59149d3d6d6cef2c09d46bb4d19beb10d6bee8c05b7850c33535b3c438","impliedFormat":99},{"version":"a8f0c99380c9e91a73ecfc0a8582fbdefde3a1351e748079dc8c0439ea97b6db","impliedFormat":99},{"version":"be02e3c3cb4e187fd252e7ae12f6383f274e82288c8772bb0daf1a4e4af571ad","impliedFormat":99},{"version":"82ca40fb541799273571b011cd9de6ee9b577ef68acc8408135504ae69365b74","impliedFormat":99},{"version":"e671e3fc9b6b2290338352606f6c92e6ecf1a56459c3f885a11080301ca7f8de","impliedFormat":99},{"version":"a2e4b90260194318b1fa1e6b0554d257a0862c10e982c8907d30d1e7f3d463af","impliedFormat":99},{"version":"5559ab4aa1ba9fac7225398231a179d63a4c4dccd982a17f09404b536980dae8","impliedFormat":99},{"version":"2d7b9e1626f44684252d826a8b35770b77ce7c322734a5d3236b629a301efdcf","impliedFormat":99},{"version":"5b8dafbb90924201f655931d429a4eceb055f11c836a6e9cbc7c3aecf735912d","impliedFormat":99},{"version":"0b9be1f90e5e154b61924a28ed2de133fd1115b79c682b1e3988ac810674a5c4","impliedFormat":99},{"version":"7a9477ba5fc17786ee74340780083f39f437904229a0cd57fc9a468fd6567eb8","impliedFormat":99},{"version":"3da1dd252145e279f23d85294399ed2120bf8124ed574d34354a0a313c8554b6","impliedFormat":99},{"version":"e5c4080de46b1a486e25a54ddbb6b859312359f9967a7dc3c9d5cf4676378201","impliedFormat":99},{"version":"cfe1cdf673d2db391fd1a1f123e0e69c7ca06c31d9ac8b35460130c5817c8d29","impliedFormat":99},{"version":"b9701f688042f44529f99fd312c49fea853e66538c19cfcbb9ef024fdb5470cc","impliedFormat":99},{"version":"6daa62c5836cc12561d12220d385a4a243a4a5a89afd6f2e48009a8dd8f0ad83","impliedFormat":99},{"version":"c74550758053cf21f7fea90c7f84fa66c27c5f5ac1eca77ce6c2877dbfdec4d1","impliedFormat":99},{"version":"bd8310114a3a5283faac25bfbfc0d75b685a3a3e0d827ee35d166286bdd4f82e","impliedFormat":99},{"version":"1459ae97d13aeb6e457ccffac1fbb5c5b6d469339729d9ef8aeb8f0355e1e2c9","impliedFormat":99},{"version":"1bf03857edaebf4beba27459edf97f9407467dc5c30195425cb8a5d5a573ea52","impliedFormat":99},{"version":"f6b4833d66c12c9106a3299e520ed46f9a4c443cefc22c993315c4bb97a28db1","impliedFormat":99},{"version":"746c02f8b99bd90c4d135badaab575c6cfce0d030528cf90190c8914b0934ea3","impliedFormat":99},{"version":"a858ba8df5e703977dee467b10af084398919e99c9e42559180e75953a1f6ef6","impliedFormat":99},{"version":"d2dcd6105c195d0409abd475b41363789c63ae633282f04465e291a68a151685","impliedFormat":99},{"version":"0b569ed836f0431c2efaef9b6017e8b700a7fed319866d7667f1189957275045","impliedFormat":99},{"version":"9371612fd8638d7f6a249a14843132e7adb0b5c84edba9ed7905e835b644c013","impliedFormat":99},{"version":"0c72189b6ec67331476a36ec70a2b8ce6468dc4db5d3eb52deb9fefbd6981ebb","impliedFormat":99},{"version":"af8dd6bb70bfcb2c6b2de0d42240c2c952b9040af259a287e78eaf883ef1ce0d","impliedFormat":99},{"version":"7e4a27fd17dbb256314c2513784236f2ae2023573e83d0e65ebddfda336701db","impliedFormat":99},{"version":"131ecac1c7c961041df80a1dc353223af4e658d56ba1516317f79bd5400cffeb","impliedFormat":99},{"version":"f3a55347fb874828e442c2916716d56552ac3478204c29c0d47e698c00eb5d28","impliedFormat":99},{"version":"49ebbdfe7427d784ccdc8325bdecc8dda1719a7881086f14751879b4f8d70c21","impliedFormat":99},{"version":"c1692845412646f17177eb62feb9588c8b5d5013602383f02ae9d38f3915020c","impliedFormat":99},{"version":"b1b440e6c973d920935591a3d360d79090b8cf58947c0230259225b02cf98a83","impliedFormat":99},{"version":"defc2ae12099f46649d12aa4872ce23ba43fba275920c00c398487eaf091bbae","impliedFormat":99},{"version":"620390fbef44884902e4911e7473531e9be4db37eeef2da52a34449d456b4617","impliedFormat":99},{"version":"e60440cbd3ec916bc5f25ada3a6c174619745c38bfca58d3554f7d62905dc376","impliedFormat":99},{"version":"86388eda63dcb65b4982786eec9f80c3ef21ca9fb2808ff58634e712f1f39a27","impliedFormat":99},{"version":"022cd098956e78c9644e4b3ad1fe460fac6914ca9349d6213f518386baf7c96b","impliedFormat":99},{"version":"dfc67e73325643e92f71f94276b5fb3be09c59a1eeee022e76c61ae99f3eda4b","impliedFormat":99},{"version":"8c3d6c9abaa0b383f43cac0c227f063dc4018d851a14b6c2142745a78553c426","impliedFormat":99},{"version":"ee551dc83df0963c1ee03dc32ce36d83b3db9793f50b1686dc57ec2bbffc98af","impliedFormat":99},{"version":"968832c4ffd675a0883e3d208b039f205e881ae0489cc13060274cf12e0e4370","impliedFormat":99},{"version":"c593ca754961cfd13820add8b34da35a114cda7215d214e4177a1b0e1a7f3377","impliedFormat":99},{"version":"ed88c51aa3b33bb2b6a8f2434c34f125946ba7b91ed36973169813fdad57f1ec","impliedFormat":99},{"version":"a9ea477d5607129269848510c2af8bcfd8e262ebfbd6cd33a6c451f0cd8f5257","impliedFormat":99},{"version":"c9b868ce3c992a9f81fa8aa3d7839356d677c3f03c0b4584dce4ecd710ee601b","impliedFormat":1},{"version":"286b3e741470ad5b1852586371b8282d019a7e65d782a134e8d29ef22179e727","impliedFormat":1},{"version":"ab82804a14454734010dcdcd43f564ff7b0389bee4c5692eec76ff5b30d4cf66","impliedFormat":1},{"version":"c8a00bc0b7ab4eb73c27b724caf172c54037f7c675a5a3797a34efdc13951c28","impliedFormat":1},{"version":"2858d043f6f96454fd3c6b65865e6486fc5b77c8ea3d41a095515a92826a2654","impliedFormat":1},{"version":"864ab8ff5bf55724b079afdf98c9f3deccb408cd218a1d3fe218fc1805ae39ba","impliedFormat":1},{"version":"2e36248ff3cc1b0b20adc82e596d519539cd892bd98d8338c4bd4a1ed625634d","impliedFormat":1},{"version":"f486cf60e744cbb9408a0e04267179fc8beb18789a5abd9110332304efccc7e9","impliedFormat":1},{"version":"276dd3adedc2ded8dd4c02b29d6d82df787b0d317aba48ef86e55f30518242cc","impliedFormat":1},{"version":"0e0b1793645789ceb94164bc33d966a42a3b10d652050ff4cb9b4b15ad046656","impliedFormat":1},{"version":"6f5ae6f035943562bc1fcfacbd45bb5d58eafbf47277f7c704d608f6689250be","impliedFormat":1},{"version":"6ab1224e0149cc983d5da72ff3540bc0cad8ee7b23cf2a3da136f77f76d01763","impliedFormat":1},{"version":"19e9a0ae178ca6c3667eec26bff09ec4da669809823c83dd2a268757e4cf43bc","impliedFormat":1},{"version":"4cbba81c370a90689b28e2350a3ddfc11352f548a93460f868cb3f535696f9d2","impliedFormat":1},{"version":"6b65ad8e422a59e22748ba6c79408fa3c5e45a451d6f2adf0ab937ccdd770796","impliedFormat":1},{"version":"d444864ba582fafd0327d768dd1046d8c883345f8558cbd28fc975dbba0308dd","impliedFormat":1},{"version":"1f95c5511ed07626d276cc54474651ba5d18099f94997fca96d0b5addbe7f08c","impliedFormat":1},{"version":"0a7a8342189f5eb1f0611878469977fd9cd265398d52148880b8d8badf96ca4d","impliedFormat":1},{"version":"9b2d58aace64bb984ee53cdd341f108a86dfdd54c0278fc78f48140006f7f27e","impliedFormat":1},"3a4e5f03274754b8561e9ccffb22ab6cf5bcb425388886b62aab38ce5e334cf4",{"version":"cdcc132f207d097d7d3aa75615ab9a2e71d6a478162dde8b67f88ea19f3e54de","impliedFormat":1},{"version":"e1028394c1cf96d5d057ecc647e31e457b919092f882ed0c7092152b077fed9d","impliedFormat":1},{"version":"f315e1e65a1f80992f0509e84e4ae2df15ecd9ef73df975f7c98813b71e4c8da","impliedFormat":1},{"version":"5b9586e9b0b6322e5bfbd2c29bd3b8e21ab9d871f82346cb71020e3d84bae73e","impliedFormat":1},{"version":"3e70a7e67c2cb16f8cd49097360c0309fe9d1e3210ff9222e9dac1f8df9d4fb6","impliedFormat":1},{"version":"ab68d2a3e3e8767c3fba8f80de099a1cfc18c0de79e42cb02ae66e22dfe14a66","impliedFormat":1},{"version":"d96cc6598148bf1a98fb2e8dcf01c63a4b3558bdaec6ef35e087fd0562eb40ec","impliedFormat":1},{"version":"5b9586e9b0b6322e5bfbd2c29bd3b8e21ab9d871f82346cb71020e3d84bae73e","impliedFormat":1},{"version":"f8db4fea512ab759b2223b90ecbbe7dae919c02f8ce95ec03f7fb1cf757cfbeb","affectsGlobalScope":true,"impliedFormat":1},{"version":"ae77d81a5541a8abb938a0efedf9ac4bea36fb3a24cc28cfa11c598863aba571","impliedFormat":1},{"version":"f329dfad7970297cbf07ddc8fce2ad4a24e2a3855917c661922ef86eb24dd1f1","impliedFormat":1},{"version":"841784cfa9046a2b3e453d638ea5c3e53680eb8225a45db1c13813f6ea4095e5","affectsGlobalScope":true,"impliedFormat":1},{"version":"646ef1cff0ec3cf8e96adb1848357788f244b217345944c2be2942a62764b771","impliedFormat":1},"fbc1a3e9671191b4012ee4085438bde9529a209f8a78aee0ceaa89c384e61c7e","d085e6a24815c8ebec29bca2e0c70abaf81a9994a8da495475f7b20a229e3b25",{"version":"b836eed98b79fabb54f1df73252a0ce178b8df4a89794251ade2fa0c5e52b678","impliedFormat":1},{"version":"9c411c65ce8af558d20a6068b751315505c26e5e048012cea30a999b21b54fd5","impliedFormat":1},{"version":"d3cfde44f8089768ebb08098c96d01ca260b88bccf238d55eee93f1c620ff5a5","impliedFormat":1},{"version":"293eadad9dead44c6fd1db6de552663c33f215c55a1bfa2802a1bceed88ff0ec","impliedFormat":1},{"version":"833e92c058d033cde3f29a6c7603f517001d1ddd8020bc94d2067a3bc69b2a8e","impliedFormat":1},{"version":"08b2fae7b0f553ad9f79faec864b179fc58bc172e295a70943e8585dd85f600c","impliedFormat":1},{"version":"f12edf1672a94c578eca32216839604f1e1c16b40a1896198deabf99c882b340","impliedFormat":1},{"version":"e3498cf5e428e6c6b9e97bd88736f26d6cf147dedbfa5a8ad3ed8e05e059af8a","impliedFormat":1},{"version":"dba3f34531fd9b1b6e072928b6f885aa4d28dd6789cbd0e93563d43f4b62da53","impliedFormat":1},{"version":"f672c876c1a04a223cf2023b3d91e8a52bb1544c576b81bf64a8fec82be9969c","impliedFormat":1},{"version":"e4b03ddcf8563b1c0aee782a185286ed85a255ce8a30df8453aade2188bbc904","impliedFormat":1},{"version":"2329d90062487e1eaca87b5e06abcbbeeecf80a82f65f949fd332cfcf824b87b","impliedFormat":1},{"version":"25b3f581e12ede11e5739f57a86e8668fbc0124f6649506def306cad2c59d262","impliedFormat":1},{"version":"4fdb529707247a1a917a4626bfb6a293d52cd8ee57ccf03830ec91d39d606d6d","impliedFormat":1},{"version":"a9ebb67d6bbead6044b43714b50dcb77b8f7541ffe803046fdec1714c1eba206","impliedFormat":1},{"version":"5780b706cece027f0d4444fbb4e1af62dc51e19da7c3d3719f67b22b033859b9","impliedFormat":1},{"version":"6c688250f2b7061cec3a17ab8797671137b653f8c4e81a6df3190cb112a7579a","impliedFormat":1},{"version":"7a8ec10b0834eb7183e4bfcd929838ac77583828e343211bb73676d1e47f6f01","impliedFormat":1},{"version":"138c4489023da880e7219a31b8049ef9cba13d90c5d7cf9538148001d7066f50","affectsGlobalScope":true,"impliedFormat":1},{"version":"3f00324f263189b385c3a9383b1f4dae6237697bcf0801f96aa35c340512d79c","impliedFormat":1},{"version":"ec8997c2e5cea26befc76e7bf990750e96babb16977673a9ff3b5c0575d01e48","impliedFormat":1},"6eb0be33a0526003fa6749358f637b45ef04aa27b2f3a909e78d4791e9441b41","aa4f05cce60529b459783da69711e8c166036ea203f0c7d5bc3c83dcac4fa058","79676c908e223782907d92bd837db9bb9534ca1d0a91768f4499e0d900c600ff","a6d89de1284e49769aa36bc5b02c409068b64204e38d6ae3301bfc80ff2fe410","e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855","e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855","e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855","e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855","e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855","e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855","e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855","e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855","e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855","e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855","3bf64f52c18c21b5a2994c4cca6389d969dae6457eac337c67dc60bcb028e9ea","1157ff9a97cae4a62baad49a629e1fb5f7ea43f9f651d3f8166044356afc5780","52c826a150de603df684f4c7af4fe6f8b9475e29f5c68163706d16e10ed6b3c7","bdc1d27ab1ce89ceb98e4fb9fa463ed187a643d4a094b30a3da0ab5297243654","889b0a1bbd6255c3bff8bc02e0e016ac9775b17aeffe6d14fd5209b38dbcb4c3","0d816246818cc4968582288d0342eeb025e898731fc9eeb117f3573d7a26b580","e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855","89c620601ad18c109d1598ab4dbf77c1a00fc88cdffbade33f1333f84a1ce586","eff3b3105e4c82c664fbea471bd5d343e3f05a364f71f97c86dd1c9224c01cb1","7e2fc0f637be0d18e2ef7b190af0764858f6405f518d42ef94d8171bf263349c","3e971b3a0b27d7051b8e78b8e722a6deb2ea5b6a02943df939ffaeac43a959d6","e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855","265675ee67631fcdb1cea3cf3c9b6495b863e9cb8fd3a0340a7bfb291d594fcb","20610df550d7421c551f1b6a0749a2acdc529b761fed1c0aa724ab823cf3142c","e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",{"version":"4d7d964609a07368d076ce943b07106c5ebee8138c307d3273ba1cf3a0c3c751","impliedFormat":99},{"version":"0e48c1354203ba2ca366b62a0f22fec9e10c251d9d6420c6d435da1d079e6126","impliedFormat":99},{"version":"0662a451f0584bb3026340c3661c3a89774182976cd373eca502a1d3b5c7b580","impliedFormat":99},"488727f68470fee966bede617461884b71f998980bb08c566b5b2c405a5404c9","e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855","e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855","e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855","e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855","e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855","e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855","e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855","1e59c7caa185907a7b456841ac8a37f65ab59420cf602069bb5c0ff9d3f23dc3","e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855","e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855","e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855","e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855","e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855","e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855","e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855","e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855","e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855","e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855","e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855","e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855","67104ceafa8a1d7fb312c1f8ec0e1ea95e4fa3472ea7515f6cc0f50a3d164a6c","91ac5841c91202b57a4fa39c08a5a9166c14e5c611be01d0daacf395ba4e2e9b","588c9f755e5647d5f7cef169b4ad45b3dd3c769aa7e1fe34bec9c78186ed48ec","08ac0cbf5fbb0e63595080b06dd2d8a964e422346975ba5306753f6ed91a1a58","a6207c72aedf80b70f308ca628d95f1b5928b0beb29500be0856c58f1d37fa1d","3bd684956936c9487efa30bad3bdc8740a1aa4e30ef46a78d253c53f344db533",{"version":"800de8bb8ea525980e16dd155bb6e6847e7fdeccaf816e5c2674e1a24c5bfc9a","impliedFormat":1},{"version":"88efe27bebddb62da9655a9f093e0c27719647e96747f16650489dc9671075d6","impliedFormat":1},{"version":"e348f128032c4807ad9359a1fff29fcbc5f551c81be807bfa86db5a45649b7ba","impliedFormat":1},{"version":"69fbd801af2b1b88b86bda5b74aef5fc013a7cc0c7422d33c8918bf8e7fdc6a9","impliedFormat":1},{"version":"4791c9bacdc47bdf94fcf377e2f0e198c07ad8e06425e23e1dda2d96e7685c11","impliedFormat":1},{"version":"5f12132800d430adbe59b49c2c0354d85a71ada7d756e34250a655baa8ad4ae5","impliedFormat":1},{"version":"ec27c0cee1436f58e785f621703d19d588ebbd489eca245e5198b4d6b715790d","impliedFormat":1},{"version":"b16e757e4c35434065120a2b3bf13a518fc9e621dc9c2ed668f91635a9dc4e75","impliedFormat":1},{"version":"aedbd50d6af5098b3ed02ed1ae7e3d58c86fe30ab71ce9b5f8c4376c44205cde","impliedFormat":1},{"version":"bb546af29295599cdea263bf8e7aaf98981017193ac178709353b8cc14dc572e","impliedFormat":1},{"version":"4374cefdde5c6e9bad52b0436e887b8325b8f407c12035194ad02c28f1553a3a","impliedFormat":1},{"version":"9f36000a33d44e49f677af6f274bc23c7e18c18c1ddb1aae3095d43b927b1e00","impliedFormat":1},{"version":"f83f059b53d5dd6251ce68353264820647653f93ae73f53c405c918bdbed969c","impliedFormat":1},{"version":"ee933420aacba1f60aa70fb8ba47c5e69001b005073b71973114587089a13c7f","impliedFormat":1},{"version":"ffde106aa78275d720e2956f7e449158b2890739a452335812ef0b913eb8463b","impliedFormat":1},{"version":"56584bfc655f9df64afc0f22f7d1122c29e5b74b342c203b891e19de9fa37de8","impliedFormat":1},{"version":"40ec58f0fadd0b3981b3d383e1c12fa0680115ae9f018387fc2cfc0bbcf23204","impliedFormat":1},{"version":"59709e26e08d4fd4c6a133552ad8f94c5b31463f295c4bf75fae1907738b8441","impliedFormat":1},{"version":"849b9e7283b7309a4556c9b90bb8e2dfc27751f157798065bbc513dcddb09a8c","impliedFormat":1},{"version":"76bba0c97594248c1be19af32d5799f7eff51cec2926d8e4dd59267d7636a0b4","impliedFormat":1},{"version":"10e109212c7be8a9f66e988e5d6c2a8900c9d14bf6beadf5fa70d32ada3425cf","impliedFormat":1},{"version":"f4558bcdc26690cc593cd59217cd17d8e00af0f5fbd0c4f1c0d71ba75029c42e","impliedFormat":1},{"version":"51d621c4e724720dd1b7ba6374d8a5b988beeda22d620ac84634a13691b631d9","impliedFormat":1},{"version":"f57a588d8f6b3ce5c8b494f2dc759a8885eaee18e80a4952df47de45403fedbe","impliedFormat":1},{"version":"34735727b3fe7a0ed0651a0f88d06449163d1989a2b2de7f047473adc7c1c383","impliedFormat":1},{"version":"a5b13abc88ab3186e713c445e59e2f6eee20c6167943517bc2f56985d89b8c55","impliedFormat":1},{"version":"8b29e3ed0c90b2ebc40b2bce5a518a0e86c0c417f7fe99a5e7658a61166bd9cd","impliedFormat":1},{"version":"9d609c44db4805332285b28d039d1e9b94bf97a074c652faff4dc1949f71718b","impliedFormat":1},{"version":"6e28d186dfadf5624b2e4f0ade02bae83d6067a4f4527733afdf0749740edeb1","impliedFormat":1},{"version":"369b7270eeeb37982203b2cb18c7302947b89bf5818c1d3d2e95a0418f02b74e","impliedFormat":1},{"version":"94f95d223e2783b0aef4d15d7f6990a6a550fe17d099c501395f690337f7105e","impliedFormat":1},{"version":"945be5a9505194381cfd4a8551a5f0ae48090847e454fecf834e054207c5a57b","impliedFormat":1},{"version":"d1e8b78a5ce49cee9ef4cd2565d4645d269c6fd0650e3592f85ba481f13da3a3","impliedFormat":1},{"version":"61be8f1d5345cf5750aed87af2869888ca1b675ffa481f1d4d80554e10084b4a","impliedFormat":1},{"version":"309ebd217636d68cf8784cbc3272c16fb94fb8e969e18b6fe88c35200340aef1","impliedFormat":1},{"version":"91cf9887208be8641244827c18e620166edf7e1c53114930b54eaeaab588a5be","impliedFormat":1},{"version":"ef9b6279acc69002a779d0172916ef22e8be5de2d2469ff2f4bb019a21e89de2","impliedFormat":1},{"version":"71623b889c23a332292c85f9bf41469c3f2efa47f81f12c73e14edbcffa270d3","affectsGlobalScope":true,"impliedFormat":1},{"version":"88863d76039cc550f8b7688a213dd051ae80d94a883eb99389d6bc4ce21c8688","impliedFormat":1},{"version":"e9ce511dae7201b833936d13618dff01815a9db2e6c2cc28646e21520c452d6c","impliedFormat":1},{"version":"243649afb10d950e7e83ee4d53bd2fbd615bb579a74cf6c1ce10e64402cdf9bb","impliedFormat":1},{"version":"35575179030368798cbcd50da928a275234445c9a0df32d4a2c694b2b3d20439","impliedFormat":1},{"version":"c939cb12cb000b4ec9c3eca3fe7dee1fe373ccb801237631d9252bad10206d61","impliedFormat":1},{"version":"b42d3651103a532f7492e719a828647af97306b2356ae757ebb7f17f4a8c41e5","impliedFormat":1},{"version":"b42d3651103a532f7492e719a828647af97306b2356ae757ebb7f17f4a8c41e5","impliedFormat":1},{"version":"b42d3651103a532f7492e719a828647af97306b2356ae757ebb7f17f4a8c41e5","impliedFormat":1},{"version":"b42d3651103a532f7492e719a828647af97306b2356ae757ebb7f17f4a8c41e5","impliedFormat":1},{"version":"b42d3651103a532f7492e719a828647af97306b2356ae757ebb7f17f4a8c41e5","impliedFormat":1},{"version":"b42d3651103a532f7492e719a828647af97306b2356ae757ebb7f17f4a8c41e5","impliedFormat":1},{"version":"26384fb401f582cae1234213c3dc75fdc80e3d728a0a1c55b405be8a0c6dddbe","impliedFormat":1},{"version":"26384fb401f582cae1234213c3dc75fdc80e3d728a0a1c55b405be8a0c6dddbe","impliedFormat":1},{"version":"b42d3651103a532f7492e719a828647af97306b2356ae757ebb7f17f4a8c41e5","impliedFormat":1},{"version":"b42d3651103a532f7492e719a828647af97306b2356ae757ebb7f17f4a8c41e5","impliedFormat":1},{"version":"b42d3651103a532f7492e719a828647af97306b2356ae757ebb7f17f4a8c41e5","impliedFormat":1},{"version":"b42d3651103a532f7492e719a828647af97306b2356ae757ebb7f17f4a8c41e5","impliedFormat":1},{"version":"b42d3651103a532f7492e719a828647af97306b2356ae757ebb7f17f4a8c41e5","impliedFormat":1},{"version":"b42d3651103a532f7492e719a828647af97306b2356ae757ebb7f17f4a8c41e5","impliedFormat":1},{"version":"b42d3651103a532f7492e719a828647af97306b2356ae757ebb7f17f4a8c41e5","impliedFormat":1},{"version":"b42d3651103a532f7492e719a828647af97306b2356ae757ebb7f17f4a8c41e5","impliedFormat":1},{"version":"b42d3651103a532f7492e719a828647af97306b2356ae757ebb7f17f4a8c41e5","impliedFormat":1},{"version":"b42d3651103a532f7492e719a828647af97306b2356ae757ebb7f17f4a8c41e5","impliedFormat":1},{"version":"b42d3651103a532f7492e719a828647af97306b2356ae757ebb7f17f4a8c41e5","impliedFormat":1},{"version":"b42d3651103a532f7492e719a828647af97306b2356ae757ebb7f17f4a8c41e5","impliedFormat":1},{"version":"b42d3651103a532f7492e719a828647af97306b2356ae757ebb7f17f4a8c41e5","impliedFormat":1},{"version":"b42d3651103a532f7492e719a828647af97306b2356ae757ebb7f17f4a8c41e5","impliedFormat":1},{"version":"b42d3651103a532f7492e719a828647af97306b2356ae757ebb7f17f4a8c41e5","impliedFormat":1},{"version":"b42d3651103a532f7492e719a828647af97306b2356ae757ebb7f17f4a8c41e5","impliedFormat":1},{"version":"b42d3651103a532f7492e719a828647af97306b2356ae757ebb7f17f4a8c41e5","impliedFormat":1},{"version":"b42d3651103a532f7492e719a828647af97306b2356ae757ebb7f17f4a8c41e5","impliedFormat":1},{"version":"b42d3651103a532f7492e719a828647af97306b2356ae757ebb7f17f4a8c41e5","impliedFormat":1},{"version":"b42d3651103a532f7492e719a828647af97306b2356ae757ebb7f17f4a8c41e5","impliedFormat":1},{"version":"b42d3651103a532f7492e719a828647af97306b2356ae757ebb7f17f4a8c41e5","impliedFormat":1},{"version":"b42d3651103a532f7492e719a828647af97306b2356ae757ebb7f17f4a8c41e5","impliedFormat":1},{"version":"b42d3651103a532f7492e719a828647af97306b2356ae757ebb7f17f4a8c41e5","impliedFormat":1},{"version":"b42d3651103a532f7492e719a828647af97306b2356ae757ebb7f17f4a8c41e5","impliedFormat":1},{"version":"b42d3651103a532f7492e719a828647af97306b2356ae757ebb7f17f4a8c41e5","impliedFormat":1},{"version":"26384fb401f582cae1234213c3dc75fdc80e3d728a0a1c55b405be8a0c6dddbe","impliedFormat":1},{"version":"b42d3651103a532f7492e719a828647af97306b2356ae757ebb7f17f4a8c41e5","impliedFormat":1},{"version":"b42d3651103a532f7492e719a828647af97306b2356ae757ebb7f17f4a8c41e5","impliedFormat":1},{"version":"b42d3651103a532f7492e719a828647af97306b2356ae757ebb7f17f4a8c41e5","impliedFormat":1},{"version":"b42d3651103a532f7492e719a828647af97306b2356ae757ebb7f17f4a8c41e5","impliedFormat":1},{"version":"b42d3651103a532f7492e719a828647af97306b2356ae757ebb7f17f4a8c41e5","impliedFormat":1},{"version":"03268b4d02371bdf514f513797ed3c9eb0840b0724ff6778bda0ef74c35273be","impliedFormat":1},{"version":"3511847babb822e10715a18348d1cbb0dae73c4e4c0a1bcf7cbc12771b310d45","impliedFormat":1},{"version":"80e653fbbec818eecfe95d182dc65a1d107b343d970159a71922ac4491caa0af","impliedFormat":1},{"version":"53f00dc83ccceb8fad22eb3aade64e4bcdb082115f230c8ba3d40f79c835c30e","impliedFormat":1},{"version":"35475931e8b55c4d33bfe3abc79f5673924a0bd4224c7c6108a4e08f3521643c","impliedFormat":1},{"version":"9078205849121a5d37a642949d687565498da922508eacb0e5a0c3de427f0ae5","impliedFormat":1},{"version":"e8f8f095f137e96dc64b56e59556c02f3c31db4b354801d6ae3b90dceae60240","impliedFormat":1},{"version":"451abef2a26cebb6f54236e68de3c33691e3b47b548fd4c8fa05fd84ab2238ff","impliedFormat":1},{"version":"73527af71681973a8ed31754896088a0f03a5480e67be9274d4440f834fd1058","impliedFormat":1},{"version":"58da08d1fe876c79c47dcf88be37c5c3fab55d97b34c8c09a666599a2191208d","impliedFormat":1},"509ca5c148334c3c52d109491726e49a34b987b7c1f7d88f88f4a63d87f76fee","10cedf5e06539df17e892ad4a34a4d9130c4a030e900fd17aef6d88baf707f2c","d7501f0e561f193a36198f8b29b9c72ececaf0d7e33ef32f0bc8675422d6cd5f","762ca5eb3d9605718b96ae46bc83871a4e6abed8c1b728160174ce704e17cd7a","24eea65c4103f6e9dfaa3c8153e74aa97ae48dd076e908736f9ad384b5eb182f","d6d2449f90295dcf886569abc48e28a8987c754bf0a773e910cff4c0e4de3024","72065c676a77ee09e97a558fb961c2826496d2455cbd8cb03c48e42fd774c94a","2ae30ab7d9df2f16bb2a02fd322a7e94e9df485a6d472b01d0ece27a77d88e7e","a4806d11b49de1bedd95847fc96db2c54282d12631bc77f566bd56bf3e27d97a","fd59012456cf3fafab5bd45bce46971101e8b162d348b9e2e969f93d173eb477","f49bb535cd4b77e2189829d9e8bacfb2854991a175bad86225ea8219f82800c0","30495c02fd4832b1a807ddc4d622289c31d62fb72c3bf5af74d85b17d104e0fe","a10dc8ba6fbb4b0e66341ebbba144bda6037d513284972b3b62e0188da4ee613","1564e8cbd2b9330435517aa175e8b3b9053b83631d8dfc375212ab1027739460","d1a37506cdd5ca9fe792dc1b06acb4a65281132d4fbdeff3ec1ed2f2b785bac8","872d4cf9c983741062e489db65114ab3e7237b54949d620c0afce351124b7830","20d97cef8b4696f25dce319acb7a317f0dab1a8c6eb6452f9ba9b383cba1def9","2f35ec4cde793cb8ad0de0d31f2f893407ce0a71d1d4594fcaad9f251822249f","bffa25a9488ddab1a1435d3b1e9c87e1cd26d77060c66d54a3aa9440bccd6950","463b14455226174e35ec422e850832205e4bde2c59e980f4e8ba53e01d64cd93","3ebe2ce6ff4eda1278ae371d5bd6475e53460be21e6dbde732103e617db0304f","c580aedc6384e7492c652b7f30ee18d44082fd2026da249a5caae1c050f700e4","1a0fb940718d7b6b64ff21c305df3742d8fce7bf349bb0ecfbef2138a8d0cfeb","b2dbd8bf35783f3bf48bef72295c1c5c1d9967e078edebc4433803331f80a14b","3becd19681c1c4e4357dfbdf25c72367200096b24d45e3b50d73315f949111a3","14518bb82f5d73a795974ca36e06a7e4b457ec2045e31a1610c8e8f52859af40","a4f96c8a933777f876f428c71ae3f7d72f1736604920ca705d35e869e154914c","b0ac88b03bd14382828218ffb73734b243dbcfce29e9e7af04235ae361900fa1","02a843a3b456f8354f0687f01eb149b194635a4c07d70c36c1799571ae2cc99b","868163c44c863c65171437ea44df02686057a802e94977d7a3d4479f3321ba00","93fa7caa8bc0d57576678175d40769508c934ff78fade9ed401d9c33399681bd","aaabe9b098b643d2de9195d8036ccde4aba0408a8cf1c8fd7757a4e4a94fa95f","cb083d5abcc69f3a79cf7ffeaf7de0f5eab5deaf703ccec9054317415229450e","08d589473ec9c5dae5d3d64ec3aab337d2ee46d17d61151667fd2c69be2bca10",{"version":"3cfb7c0c642b19fb75132154040bb7cd840f0002f9955b14154e69611b9b3f81","impliedFormat":1},{"version":"8387ec1601cf6b8948672537cf8d430431ba0d87b1f9537b4597c1ab8d3ade5b","impliedFormat":1},{"version":"d16f1c460b1ca9158e030fdf3641e1de11135e0c7169d3e8cf17cc4cc35d5e64","impliedFormat":1},{"version":"a934063af84f8117b8ce51851c1af2b76efe960aa4c7b48d0343a1b15c01aedf","impliedFormat":1},{"version":"e3c5ad476eb2fca8505aee5bdfdf9bf11760df5d0f9545db23f12a5c4d72a718","impliedFormat":1},{"version":"462bccdf75fcafc1ae8c30400c9425e1a4681db5d605d1a0edb4f990a54d8094","impliedFormat":1},{"version":"5923d8facbac6ecf7c84739a5c701a57af94a6f6648d6229a6c768cf28f0f8cb","impliedFormat":1},{"version":"d0570ce419fb38287e7b39c910b468becb5b2278cf33b1000a3d3e82a46ecae2","impliedFormat":1},{"version":"3aca7f4260dad9dcc0a0333654cb3cde6664d34a553ec06c953bce11151764d7","impliedFormat":1},{"version":"a0a6f0095f25f08a7129bc4d7cb8438039ec422dc341218d274e1e5131115988","impliedFormat":1},{"version":"b58f396fe4cfe5a0e4d594996bc8c1bfe25496fbc66cf169d41ac3c139418c77","impliedFormat":1},{"version":"45785e608b3d380c79e21957a6d1467e1206ac0281644e43e8ed6498808ace72","impliedFormat":1},{"version":"bece27602416508ba946868ad34d09997911016dbd6893fb884633017f74e2c5","impliedFormat":1},{"version":"2a90177ebaef25de89351de964c2c601ab54d6e3a157cba60d9cd3eaf5a5ee1a","impliedFormat":1},{"version":"82200e963d3c767976a5a9f41ecf8c65eca14a6b33dcbe00214fcbe959698c46","impliedFormat":1},{"version":"b4966c503c08bbd9e834037a8ab60e5f53c5fd1092e8873c4a1c344806acdab2","impliedFormat":1},{"version":"3d3208d0f061e4836dd5f144425781c172987c430f7eaee483fadaa3c5780f9f","impliedFormat":1},{"version":"34a8a5b4c21e7a6d07d3b6bce72371da300ec1aed58961067e13f1f4dc849712","impliedFormat":1},"8d82034250dbefc81b03f42a2161c2a0e48bcf81d6f6248755651f1b9f7d7e97","d1986184a09a52db8228cb2bb2a61a8c05c9354e5b93cec8e2628d8579c892d7","4c65f19d3a64b51a42c79d2e8d0e9f0654d83e34d7f7cd16e056b411b2810e1c",{"version":"556ccd493ec36c7d7cb130d51be66e147b91cc1415be383d71da0f1e49f742a9","impliedFormat":1},{"version":"b6d03c9cfe2cf0ba4c673c209fcd7c46c815b2619fd2aad59fc4229aaef2ed43","impliedFormat":1},{"version":"95aba78013d782537cc5e23868e736bec5d377b918990e28ed56110e3ae8b958","impliedFormat":1},{"version":"670a76db379b27c8ff42f1ba927828a22862e2ab0b0908e38b671f0e912cc5ed","impliedFormat":1},{"version":"13b77ab19ef7aadd86a1e54f2f08ea23a6d74e102909e3c00d31f231ed040f62","impliedFormat":1},{"version":"069bebfee29864e3955378107e243508b163e77ab10de6a5ee03ae06939f0bb9","impliedFormat":1},{"version":"d5799bcf7fe4e6de3063abf4e321c14b051706f03cf5716d8a19f22fe1f69519","impliedFormat":1},{"version":"751764bb94219b4ce8f5475dc35d3de2e432fea01a0c9610cd7f69ad05e398c6","impliedFormat":1},{"version":"19990350fca066265b2c190c9b6cde1229f35002ea2d4df8c9e397e9942f6c89","impliedFormat":99},{"version":"8fb8fdda477cd7382477ffda92c2bb7d9f7ef583b1aa531eb6b2dc2f0a206c10","impliedFormat":99},{"version":"66995b0c991b5c5d42eff1d950733f85482c7419f7296ab8952e03718169e379","impliedFormat":99},{"version":"9863f888da357e35e013ca3465b794a490a198226bd8232c2f81fb44e16ff323","impliedFormat":99},{"version":"84bc2d80326a83ee4a6e7cba2fd480b86502660770c0e24da96535af597c9f1e","impliedFormat":99},{"version":"ea27768379b866ee3f5da2419650acdb01125479f7af73580a4bceb25b79e372","impliedFormat":99},{"version":"598931eeb4362542cae5845f95c5f0e45ac668925a40ce201e244d7fe808e965","impliedFormat":99},{"version":"da9ef88cde9f715756da642ad80c4cd87a987f465d325462d6bc2a0b11d202c8","impliedFormat":99},{"version":"b4c6184d78303b0816e779a48bef779b15aea4a66028eb819aac0abee8407dea","impliedFormat":99},{"version":"db085d2171d48938a99e851dafe0e486dce9859e5dfa73c21de5ed3d4d6fb0c5","impliedFormat":99},{"version":"62a3ad1ddd1f5974b3bf105680b3e09420f2230711d6520a521fab2be1a32838","impliedFormat":99},{"version":"a77be6fc44c876bc10c897107f84eaba10790913ebdcad40fcda7e47469b2160","impliedFormat":99},{"version":"06cf55b6da5cef54eaaf51cdc3d4e5ebf16adfdd9ebd20cec7fe719be9ced017","impliedFormat":99},{"version":"91f5dbcdb25d145a56cffe957ec665256827892d779ef108eb2f3864faff523b","impliedFormat":99},{"version":"052ba354bab8fb943e0bc05a0769f7b81d7c3b3c6cd0f5cfa53c7b2da2a525c5","impliedFormat":99},{"version":"927955a3de5857e0a1c575ced5a4245e74e6821d720ed213141347dd1870197f","impliedFormat":99},{"version":"fec804d54cd97dd77e956232fc37dc13f53e160d4bbeeb5489e86eeaa91f7ebd","impliedFormat":99},{"version":"c1d53a14aad7cda2cb0b91f5daccd06c8e3f25cb26c09e008f46ad2896c80bf1","impliedFormat":1},{"version":"c789127b81f23a44e7cd20eaff043bb8ddd8b75aca955504b81217d6347709d8","impliedFormat":1},{"version":"1e13bda0589d714493973ae87a135aadb8bdadc2b8ba412a62d6a8f05f13ae76","impliedFormat":1},{"version":"9e9217786bc4dced2d11b82eaf62c77f172a2b4671f1a6353835dcbf7eef0843","impliedFormat":1},{"version":"8c18473f354a9648fd8798196f520b3c3868181c315ab6a726177e5b5d2ada1c","impliedFormat":1},{"version":"067fe0fe11f79aa3eef819ee2f1d7beecc7a6d9e95ee1b2b84553495fb61b2fe","impliedFormat":1},{"version":"65e7aa0d38b9513dad1d66fa622ca0897efd8f6e11cb3887231451eb1dde719a","impliedFormat":1},{"version":"cf8d966c5b46aa3b4e2bc55aeaf5932253a734d2c09fc9e05867d47f7fc3fe31","impliedFormat":1},{"version":"e11fb3c6b0788cddcda16e472a173c03d8729201dc325beb1251f54d2630ebbb","impliedFormat":1},{"version":"9034c961e85ef73bdd4e07e2c56d7adfa4c00ee6cf568dcfc13d059575aac8a8","impliedFormat":1},{"version":"48676769d0f4904e916425f778ae25c140370fb90b33ad85151c7ebab166a0cc","impliedFormat":1},{"version":"b70a8d1c0d9628260158c2e96982f5ffb415ca87f97388ea743e52bd6ef37a9c","impliedFormat":1},{"version":"709bae51a9b0263a888c6adf48fb1380634e37267abcea46a52eb02a14b76292","impliedFormat":1},{"version":"7a625afe5721361715736bc3f9548206e1f173dcdc43eecaf7f70557f5151361","impliedFormat":1},{"version":"4d114e382693704d3792d2d6da45adc1aa2d8a86c1b8ebe5fc225dccd30aaf36","impliedFormat":1},{"version":"329760175a249a5e13e16f281ede4d8da4a4a72d511bf631bf7e5bd363146a80","impliedFormat":1},{"version":"9fbdb40eb68109a83dcc5f19c450556b20699b4fa19783dabdfc06a9937c9c30","impliedFormat":1},{"version":"afb75becf7075fc3673a6f1f7b669b5bb909ae67609284ce6548ec44d8038a61","impliedFormat":1},{"version":"4018b7fb337b14d2a40dd091208fbd39b3400136dfda00e9995b51cf64783a9f","impliedFormat":1},{"version":"6f5a9b68ce8608014210f5a777f8dd82e6382285f6278c811b7b0214bbcac5bd","impliedFormat":1},{"version":"af11413ffc8c34a2a2475cb9d2982b4cc87a9317bf474474eedaacc4aaab4582","affectsGlobalScope":true,"impliedFormat":1},{"version":"f3d8c757e148ad968f0d98697987db363070abada5f503da3c06aefd9d4248c1","impliedFormat":1},{"version":"96d14f21b7652903852eef49379d04dbda28c16ed36468f8c9fa08f7c14c9538","impliedFormat":1},{"version":"03c258e060b7da220973f84b89615e4e9850e9b5d30b3a8e4840b3e3268ae8eb","impliedFormat":1}],"root":[531,532,753,767,768,[790,818],[822,848],[941,974],[993,995]],"options":{"allowJs":true,"esModuleInterop":true,"jsx":4,"module":99,"skipLibCheck":true,"strict":true,"target":7},"referencedMap":[[994,1],[531,2],[995,3],[848,4],[847,5],[941,6],[942,6],[943,4],[944,4],[946,7],[947,4],[948,4],[950,4],[949,4],[945,4],[951,4],[953,4],[954,4],[952,4],[955,4],[956,4],[957,4],[961,4],[962,4],[964,4],[963,4],[965,4],[966,4],[958,4],[959,4],[960,4],[967,4],[970,4],[971,4],[968,4],[969,4],[972,4],[973,4],[974,4],[794,4],[795,4],[796,4],[797,4],[843,5],[844,8],[845,9],[846,5],[792,10],[793,10],[798,4],[799,4],[800,4],[801,4],[802,4],[803,4],[753,11],[767,4],[808,12],[809,13],[805,14],[810,4],[812,15],[814,16],[815,4],[817,17],[818,4],[822,18],[823,4],[824,4],[825,4],[826,4],[827,4],[828,4],[829,4],[830,19],[807,19],[831,4],[832,4],[833,4],[834,4],[532,20],[768,10],[998,21],[996,2],[940,22],[939,23],[405,2],[738,24],[737,25],[748,26],[754,2],[533,2],[743,27],[734,28],[742,29],[735,30],[374,2],[789,31],[733,32],[544,33],[545,34],[682,33],[683,35],[664,36],[665,37],[548,38],[549,39],[619,40],[620,41],[593,33],[594,42],[587,33],[588,43],[679,44],[677,45],[678,2],[693,46],[694,47],[563,48],[564,49],[695,50],[696,51],[697,52],[698,53],[555,54],[556,55],[681,56],[680,57],[666,33],[667,58],[559,59],[560,60],[583,2],[584,61],[701,62],[699,63],[700,64],[702,65],[703,66],[706,67],[704,68],[707,45],[705,69],[708,70],[711,71],[709,72],[710,73],[712,74],[561,54],[562,75],[687,76],[684,77],[685,78],[686,2],[662,79],[663,80],[607,81],[606,82],[604,83],[603,84],[605,85],[714,86],[713,87],[716,88],[715,89],[592,90],[591,33],[570,91],[568,92],[567,38],[569,93],[719,94],[723,95],[717,96],[718,97],[720,94],[721,94],[722,94],[609,98],[608,38],[625,99],[623,100],[624,45],[621,101],[622,102],[558,103],[557,33],[615,104],[546,33],[547,105],[614,106],[652,107],[655,108],[653,109],[654,110],[566,111],[565,33],[657,112],[656,38],[635,113],[634,33],[590,114],[589,33],[661,115],[660,116],[629,117],[628,118],[626,119],[627,120],[618,121],[617,122],[616,123],[725,124],[724,125],[642,126],[641,127],[640,128],[689,129],[688,2],[633,130],[632,131],[630,132],[631,133],[611,134],[610,38],[554,135],[553,136],[552,137],[551,138],[550,139],[646,140],[645,141],[576,142],[575,38],[580,143],[579,144],[644,145],[643,33],[690,2],[692,146],[691,2],[649,147],[648,148],[647,149],[727,150],[726,151],[729,152],[728,153],[675,154],[676,155],[674,156],[613,157],[612,2],[659,158],[658,159],[586,160],[585,33],[637,161],[636,33],[543,162],[542,2],[596,163],[597,164],[602,165],[595,166],[599,167],[598,168],[600,169],[601,170],[651,171],[650,38],[582,172],[581,38],[732,173],[731,174],[730,175],[669,176],[668,33],[639,177],[638,33],[574,178],[572,179],[571,38],[573,180],[671,181],[670,33],[578,182],[577,33],[673,183],[672,33],[988,2],[985,2],[984,2],[979,184],[990,185],[975,186],[986,187],[978,188],[977,189],[987,2],[982,190],[989,2],[983,191],[976,2],[766,192],[765,193],[764,186],[992,194],[763,2],[1001,195],[997,21],[999,196],[1000,21],[1002,2],[1003,2],[535,2],[537,197],[538,198],[762,199],[761,200],[1040,201],[1041,202],[1042,2],[1043,2],[140,203],[141,203],[142,204],[97,205],[143,206],[144,207],[145,208],[92,2],[95,209],[93,2],[94,2],[146,210],[147,211],[148,212],[149,213],[150,214],[151,215],[152,215],[153,216],[154,217],[155,218],[156,219],[98,2],[96,2],[157,220],[158,221],[159,222],[191,223],[160,224],[161,225],[162,226],[163,227],[164,228],[165,229],[166,230],[167,231],[168,232],[169,233],[170,233],[171,234],[172,2],[173,235],[175,236],[174,237],[176,238],[177,239],[178,240],[179,241],[180,242],[181,243],[182,244],[183,245],[184,246],[185,247],[186,248],[187,249],[188,250],[99,2],[100,2],[101,2],[139,251],[189,252],[190,253],[195,254],[460,255],[196,256],[194,257],[462,258],[461,259],[991,255],[192,260],[458,2],[193,261],[83,2],[85,262],[457,255],[226,255],[736,2],[1044,2],[539,2],[541,263],[540,264],[536,2],[534,265],[84,2],[745,2],[1010,2],[1011,266],[1008,2],[1009,2],[760,267],[744,2],[749,268],[751,269],[758,270],[756,271],[755,2],[757,200],[739,272],[759,273],[741,274],[747,275],[750,268],[746,276],[752,277],[483,278],[488,1],[495,279],[478,280],[230,2],[238,281],[378,282],[381,283],[353,2],[366,284],[373,285],[255,2],[355,2],[236,2],[352,286],[398,287],[237,2],[228,288],[380,289],[382,290],[383,291],[455,292],[347,293],[300,294],[360,295],[361,296],[359,297],[358,2],[354,298],[379,299],[239,300],[425,2],[426,301],[266,302],[240,303],[267,302],[303,302],[206,302],[376,304],[375,2],[365,305],[473,2],[215,2],[494,306],[433,307],[434,308],[430,309],[512,2],[330,2],[435,5],[431,310],[517,311],[516,312],[511,2],[281,2],[333,313],[332,2],[510,314],[432,255],[286,315],[293,316],[295,317],[285,2],[290,318],[292,319],[294,320],[289,321],[287,2],[291,322],[513,2],[509,2],[515,323],[514,2],[284,324],[504,325],[507,326],[274,327],[273,328],[272,329],[520,255],[271,330],[260,2],[522,2],[523,255],[524,331],[198,2],[362,332],[363,333],[364,334],[202,2],[367,2],[222,335],[197,2],[447,255],[204,336],[446,337],[445,338],[436,2],[437,2],[444,2],[439,2],[442,339],[438,2],[440,340],[443,341],[441,340],[235,2],[232,2],[233,302],[387,2],[392,342],[393,343],[391,344],[389,345],[390,346],[385,2],[453,5],[227,5],[482,347],[489,348],[493,349],[321,350],[320,2],[315,2],[469,351],[477,352],[348,353],[349,354],[428,355],[337,2],[451,356],[325,255],[342,357],[454,358],[338,2],[341,359],[339,2],[452,360],[449,361],[448,2],[450,2],[345,2],[424,362],[210,363],[323,364],[327,365],[343,366],[346,367],[335,368],[328,369],[476,370],[401,371],[319,372],[207,373],[475,374],[203,375],[394,376],[386,2],[395,377],[413,378],[384,2],[412,379],[91,2],[407,380],[231,2],[427,381],[402,2],[216,2],[218,2],[357,2],[411,382],[234,2],[258,383],[344,384],[264,385],[324,2],[410,2],[388,2],[415,386],[416,387],[356,2],[418,388],[420,389],[419,390],[368,2],[409,373],[422,391],[318,392],[408,393],[414,394],[243,2],[247,2],[246,2],[245,2],[250,2],[244,2],[253,2],[252,2],[249,2],[248,2],[251,2],[254,395],[242,2],[310,396],[309,2],[314,397],[311,398],[313,399],[316,397],[312,398],[223,400],[302,401],[472,402],[470,2],[499,403],[501,404],[465,405],[500,406],[211,407],[208,407],[241,2],[225,408],[224,409],[220,410],[221,411],[229,412],[257,412],[268,412],[304,413],[269,413],[213,414],[212,2],[308,415],[307,416],[306,417],[305,418],[214,419],[456,420],[256,421],[464,422],[429,423],[459,424],[463,425],[351,426],[350,427],[331,428],[317,429],[299,430],[301,431],[298,432],[421,433],[322,2],[487,2],[219,434],[423,435],[471,436],[329,2],[259,437],[336,438],[334,439],[261,440],[396,441],[466,2],[262,442],[397,442],[485,2],[484,2],[486,2],[468,2],[467,2],[399,443],[326,2],[296,444],[217,445],[275,2],[201,446],[263,2],[491,255],[200,2],[503,447],[283,255],[497,5],[282,448],[480,449],[280,447],[205,2],[505,450],[278,255],[279,255],[270,2],[199,2],[277,451],[276,452],[265,453],[340,232],[400,232],[417,2],[404,454],[403,2],[288,324],[209,2],[297,255],[474,335],[481,455],[86,255],[89,456],[90,457],[87,255],[88,2],[377,458],[372,459],[371,2],[370,460],[369,2],[479,461],[490,462],[492,463],[496,464],[498,465],[502,466],[530,467],[506,467],[529,468],[508,469],[518,470],[519,471],[521,472],[525,473],[528,335],[527,2],[526,474],[1006,475],[1019,476],[1004,2],[1005,477],[1020,478],[1015,479],[1016,480],[1014,481],[1018,482],[1012,483],[1007,484],[1017,485],[1013,476],[786,486],[769,2],[770,486],[785,487],[788,488],[787,489],[981,490],[980,2],[849,2],[865,491],[866,491],[867,491],[868,491],[882,492],[869,493],[870,493],[871,494],[862,495],[860,496],[851,2],[855,497],[859,498],[857,499],[864,500],[852,501],[853,502],[854,503],[856,504],[858,505],[861,506],[863,507],[872,493],[873,493],[874,493],[875,491],[876,493],[877,493],[850,493],[878,2],[880,508],[879,493],[881,491],[406,509],[1031,510],[1021,2],[1022,511],[1032,512],[1033,513],[1034,510],[1035,510],[1036,2],[1039,514],[1037,510],[1038,2],[1028,2],[1025,515],[1026,2],[1027,2],[1024,516],[1023,2],[1029,510],[1030,2],[81,2],[82,2],[13,2],[14,2],[16,2],[15,2],[2,2],[17,2],[18,2],[19,2],[20,2],[21,2],[22,2],[23,2],[24,2],[3,2],[25,2],[26,2],[4,2],[27,2],[31,2],[28,2],[29,2],[30,2],[32,2],[33,2],[34,2],[5,2],[35,2],[36,2],[37,2],[38,2],[6,2],[42,2],[39,2],[40,2],[41,2],[43,2],[7,2],[44,2],[49,2],[50,2],[45,2],[46,2],[47,2],[48,2],[8,2],[54,2],[51,2],[52,2],[53,2],[55,2],[9,2],[56,2],[57,2],[58,2],[60,2],[59,2],[61,2],[62,2],[10,2],[63,2],[64,2],[65,2],[11,2],[66,2],[67,2],[68,2],[69,2],[70,2],[1,2],[71,2],[72,2],[12,2],[76,2],[74,2],[79,2],[78,2],[73,2],[77,2],[75,2],[80,2],[117,517],[127,518],[116,517],[137,519],[108,520],[107,521],[136,474],[130,522],[135,523],[110,524],[124,525],[109,526],[133,527],[105,528],[104,474],[134,529],[106,530],[111,531],[112,2],[115,531],[102,2],[138,532],[128,533],[119,534],[120,535],[122,536],[118,537],[121,538],[131,474],[113,539],[114,540],[123,541],[103,542],[126,533],[125,531],[129,2],[132,543],[740,2],[784,544],[776,545],[783,546],[778,2],[779,2],[777,547],[780,548],[771,2],[772,2],[773,544],[775,549],[781,2],[782,550],[774,551],[935,552],[887,553],[889,554],[933,2],[888,555],[934,556],[938,557],[936,2],[890,553],[891,2],[932,558],[886,559],[883,2],[937,560],[884,561],[885,2],[892,562],[893,562],[894,562],[895,562],[896,562],[897,562],[898,562],[899,562],[900,562],[901,562],[902,562],[904,562],[903,562],[905,562],[906,562],[907,562],[931,563],[908,562],[909,562],[910,562],[911,562],[912,562],[913,562],[914,562],[915,562],[916,562],[918,562],[917,562],[919,562],[920,562],[921,562],[922,562],[923,562],[924,562],[925,562],[926,562],[927,562],[928,562],[929,562],[930,562],[821,564],[820,565],[819,2],[790,566],[791,567],[993,568],[816,4],[804,4],[835,4],[836,4],[837,4],[838,4],[839,4],[811,4],[813,4],[840,4],[841,4],[806,4],[842,4]],"semanticDiagnosticsPerFile":[[805,[{"start":4611,"length":7,"code":2339,"category":1,"messageText":"Property 'message' does not exist on type 'ApiErrorResponse'."},{"start":4656,"length":7,"code":2339,"category":1,"messageText":"Property 'message' does not exist on type 'ApiErrorResponse'."}]],[809,[{"start":58,"length":11,"messageText":"Module '\"@/types/api\"' has no exported member 'ApiResponse'.","category":1,"code":2305},{"start":71,"length":16,"messageText":"Module '\"@/types/api\"' has no exported member 'CartResponseData'.","category":1,"code":2305}]],[812,[{"start":58,"length":11,"messageText":"Module '\"@/types/api\"' has no exported member 'ApiResponse'.","category":1,"code":2305}]],[814,[{"start":58,"length":11,"messageText":"Module '\"@/types/api\"' has no exported member 'ApiResponse'.","category":1,"code":2305}]],[995,[{"start":12346,"length":38,"messageText":"File 'D:/1.Phebsoft/Internship/Internship tasks/Tasks by Phebsoft/Ecommerce WebApp/frontend/app/api/auth/login/route.ts' is not a module.","category":1,"code":2306},{"start":12655,"length":39,"messageText":"File 'D:/1.Phebsoft/Internship/Internship tasks/Tasks by Phebsoft/Ecommerce WebApp/frontend/app/api/auth/logout/route.ts' is not a module.","category":1,"code":2306},{"start":13003,"length":58,"messageText":"File 'D:/1.Phebsoft/Internship/Internship tasks/Tasks by Phebsoft/Ecommerce WebApp/frontend/app/api/checkout/create-payment-intent/route.ts' is not a module.","category":1,"code":2306},{"start":13340,"length":43,"messageText":"File 'D:/1.Phebsoft/Internship/Internship tasks/Tasks by Phebsoft/Ecommerce WebApp/frontend/app/api/webhooks/stripe/route.ts' is not a module.","category":1,"code":2306}]]],"affectedFilesPendingEmit":[995,848,847,941,942,943,944,946,947,948,950,949,945,951,953,954,952,955,956,957,961,962,964,963,965,966,958,959,960,967,970,971,968,969,972,973,974,794,795,796,797,843,844,845,846,792,793,798,799,800,801,802,803,753,767,808,809,805,810,812,814,815,817,818,822,823,824,825,826,827,828,829,830,807,831,832,833,834,768,790,791,993,816,804,835,836,837,838,839,811,813,840,841,806,842],"version":"5.9.3"}
````

## File: backend/alembic/versions/3d77d5196130_add_phone_and_avatar_to_users.py
````python
"""add_phone_and_avatar_to_users

Revision ID: 3d77d5196130
Revises: ec78b9a97891
Create Date: 2026-07-14 17:02:56.416928

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3d77d5196130'
down_revision: Union[str, Sequence[str], None] = 'ec78b9a97891'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('phone_number', sa.String(length=20), nullable=True))
    op.add_column('users', sa.Column('avatar_url', sa.String(length=512), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'avatar_url')
    op.drop_column('users', 'phone_number')
    # ### end Alembic commands ###
````

## File: backend/alembic/versions/d129ebf1174b_add_payments_table_model_sync.py
````python
"""add payments table model sync

Revision ID: d129ebf1174b
Revises: 3d77d5196130
Create Date: 2026-07-23 19:06:17.245688

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'd129ebf1174b'
down_revision: Union[str, Sequence[str], None] = '3d77d5196130'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('coupon_redemptions')
    op.drop_table('variant_values')
    op.drop_table('product_variant_options')
    op.drop_table('coupon_categories')
    op.drop_table('review_images')
    op.drop_table('order_status_history')
    op.drop_table('chat_messages')
    op.drop_table('chat_threads')
    op.drop_table('notifications')
    op.drop_table('product_promotions')
    op.drop_table('product_variant_images')
    op.drop_table('return_requests')
    op.drop_table('variant_types')
    op.drop_table('wishlist_items')
    op.drop_table('promotions')
    op.alter_column('addresses', 'customer_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.create_index(op.f('ix_addresses_id'), 'addresses', ['id'], unique=False)
    op.drop_constraint(op.f('uq_cart_variant'), 'cart_items', type_='unique')
    op.create_index(op.f('ix_cart_items_id'), 'cart_items', ['id'], unique=False)
    op.drop_constraint(op.f('fk_cart_items_product_variant'), 'cart_items', type_='foreignkey')
    op.create_foreign_key(None, 'cart_items', 'product_variants', ['product_variant_id'], ['id'])
    op.drop_constraint(op.f('carts_guest_token_key'), 'carts', type_='unique')
    op.create_index(op.f('ix_carts_guest_token'), 'carts', ['guest_token'], unique=True)
    op.create_index(op.f('ix_carts_id'), 'carts', ['id'], unique=False)
    op.drop_constraint(op.f('coupons_code_key'), 'coupons', type_='unique')
    op.create_index(op.f('ix_coupons_code'), 'coupons', ['code'], unique=True)
    op.create_index(op.f('ix_coupons_id'), 'coupons', ['id'], unique=False)
    op.create_index(op.f('ix_customer_profiles_id'), 'customer_profiles', ['id'], unique=False)
    op.drop_column('order_items', 'tax_amount')
    op.drop_column('order_items', 'discount_amount')
    op.add_column('orders', sa.Column('created_by_user_id', sa.Integer(), nullable=True))
    op.add_column('orders', sa.Column('status', sa.String(length=20), nullable=False))
    op.add_column('orders', sa.Column('customer_name', sa.String(length=100), nullable=True))
    op.alter_column('orders', 'customer_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.drop_constraint(op.f('fk_orders_coupon'), 'orders', type_='foreignkey')
    op.drop_constraint(op.f('fk_orders_billing_address'), 'orders', type_='foreignkey')
    op.drop_constraint(op.f('fk_orders_shipping_address'), 'orders', type_='foreignkey')
    op.drop_constraint(op.f('fk_orders_customer'), 'orders', type_='foreignkey')
    op.create_foreign_key(None, 'orders', 'customer_profiles', ['customer_id'], ['id'], ondelete='RESTRICT')
    op.create_foreign_key(None, 'orders', 'users', ['created_by_user_id'], ['id'], ondelete='SET NULL')
    op.drop_column('orders', 'coupon_id')
    op.drop_column('orders', 'notes')
    op.drop_column('orders', 'placed_at')
    op.drop_column('orders', 'tax_amount')
    op.drop_column('orders', 'shipping_amount')
    op.drop_column('orders', 'order_status')
    op.drop_column('orders', 'discount_amount')
    op.drop_column('orders', 'billing_address_id')
    op.drop_column('orders', 'subtotal')
    op.drop_column('orders', 'guest_phone')
    op.drop_column('orders', 'guest_email')
    op.drop_column('orders', 'shipping_address_id')
    op.drop_column('orders', 'guest_name')
    op.add_column('payments', sa.Column('provider', sa.String(length=50), nullable=True))
    op.add_column('payments', sa.Column('stripe_payment_intent_id', sa.String(length=255), nullable=True))
    op.add_column('payments', sa.Column('status', sa.String(length=20), nullable=False))
    op.alter_column('payments', 'payment_method',
               existing_type=sa.VARCHAR(length=50),
               nullable=True)
    op.drop_constraint(op.f('payments_order_id_key'), 'payments', type_='unique')
    op.drop_constraint(op.f('payments_transaction_reference_key'), 'payments', type_='unique')
    op.create_index(op.f('ix_payments_id'), 'payments', ['id'], unique=False)
    op.create_index(op.f('ix_payments_stripe_payment_intent_id'), 'payments', ['stripe_payment_intent_id'], unique=True)
    op.drop_column('payments', 'paid_at')
    op.drop_column('payments', 'payment_status')
    op.drop_column('payments', 'transaction_reference')
    op.drop_column('payments', 'payment_provider')
    op.create_index(op.f('ix_reviews_id'), 'reviews', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_reviews_id'), table_name='reviews')
    op.add_column('payments', sa.Column('payment_provider', sa.VARCHAR(length=100), autoincrement=False, nullable=True))
    op.add_column('payments', sa.Column('transaction_reference', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.add_column('payments', sa.Column('payment_status', sa.VARCHAR(length=20), autoincrement=False, nullable=False))
    op.add_column('payments', sa.Column('paid_at', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=True))
    op.drop_index(op.f('ix_payments_stripe_payment_intent_id'), table_name='payments')
    op.drop_index(op.f('ix_payments_id'), table_name='payments')
    op.create_unique_constraint(op.f('payments_transaction_reference_key'), 'payments', ['transaction_reference'], postgresql_nulls_not_distinct=False)
    op.create_unique_constraint(op.f('payments_order_id_key'), 'payments', ['order_id'], postgresql_nulls_not_distinct=False)
    op.alter_column('payments', 'payment_method',
               existing_type=sa.VARCHAR(length=50),
               nullable=False)
    op.drop_column('payments', 'status')
    op.drop_column('payments', 'stripe_payment_intent_id')
    op.drop_column('payments', 'provider')
    op.add_column('orders', sa.Column('guest_name', sa.VARCHAR(length=100), autoincrement=False, nullable=True))
    op.add_column('orders', sa.Column('shipping_address_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('orders', sa.Column('guest_email', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.add_column('orders', sa.Column('guest_phone', sa.VARCHAR(length=20), autoincrement=False, nullable=True))
    op.add_column('orders', sa.Column('subtotal', sa.NUMERIC(precision=10, scale=2), server_default=sa.text('0'), autoincrement=False, nullable=False))
    op.add_column('orders', sa.Column('billing_address_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('orders', sa.Column('discount_amount', sa.NUMERIC(precision=10, scale=2), server_default=sa.text('0'), autoincrement=False, nullable=False))
    op.add_column('orders', sa.Column('order_status', sa.VARCHAR(length=20), server_default=sa.text("'open'::character varying"), autoincrement=False, nullable=False))
    op.add_column('orders', sa.Column('shipping_amount', sa.NUMERIC(precision=10, scale=2), server_default=sa.text('0'), autoincrement=False, nullable=False))
    op.add_column('orders', sa.Column('tax_amount', sa.NUMERIC(precision=10, scale=2), server_default=sa.text('0'), autoincrement=False, nullable=False))
    op.add_column('orders', sa.Column('placed_at', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=True))
    op.add_column('orders', sa.Column('notes', sa.TEXT(), autoincrement=False, nullable=True))
    op.add_column('orders', sa.Column('coupon_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'orders', type_='foreignkey')
    op.drop_constraint(None, 'orders', type_='foreignkey')
    op.create_foreign_key(op.f('fk_orders_customer'), 'orders', 'customer_profiles', ['customer_id'], ['id'], ondelete='SET NULL')
    op.create_foreign_key(op.f('fk_orders_shipping_address'), 'orders', 'addresses', ['shipping_address_id'], ['id'], ondelete='SET NULL')
    op.create_foreign_key(op.f('fk_orders_billing_address'), 'orders', 'addresses', ['billing_address_id'], ['id'], ondelete='SET NULL')
    op.create_foreign_key(op.f('fk_orders_coupon'), 'orders', 'coupons', ['coupon_id'], ['id'], ondelete='SET NULL')
    op.alter_column('orders', 'customer_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.drop_column('orders', 'customer_name')
    op.drop_column('orders', 'status')
    op.drop_column('orders', 'created_by_user_id')
    op.add_column('order_items', sa.Column('discount_amount', sa.NUMERIC(precision=10, scale=2), server_default=sa.text('0'), autoincrement=False, nullable=False))
    op.add_column('order_items', sa.Column('tax_amount', sa.NUMERIC(precision=10, scale=2), server_default=sa.text('0'), autoincrement=False, nullable=False))
    op.drop_index(op.f('ix_customer_profiles_id'), table_name='customer_profiles')
    op.drop_index(op.f('ix_coupons_id'), table_name='coupons')
    op.drop_index(op.f('ix_coupons_code'), table_name='coupons')
    op.create_unique_constraint(op.f('coupons_code_key'), 'coupons', ['code'], postgresql_nulls_not_distinct=False)
    op.drop_index(op.f('ix_carts_id'), table_name='carts')
    op.drop_index(op.f('ix_carts_guest_token'), table_name='carts')
    op.create_unique_constraint(op.f('carts_guest_token_key'), 'carts', ['guest_token'], postgresql_nulls_not_distinct=False)
    op.drop_constraint(None, 'cart_items', type_='foreignkey')
    op.create_foreign_key(op.f('fk_cart_items_product_variant'), 'cart_items', 'product_variants', ['product_variant_id'], ['id'], ondelete='CASCADE')
    op.drop_index(op.f('ix_cart_items_id'), table_name='cart_items')
    op.create_unique_constraint(op.f('uq_cart_variant'), 'cart_items', ['cart_id', 'product_variant_id'], postgresql_nulls_not_distinct=False)
    op.drop_index(op.f('ix_addresses_id'), table_name='addresses')
    op.alter_column('addresses', 'customer_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.create_table('promotions',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=150), autoincrement=False, nullable=False),
    sa.Column('description', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('discount_type', sa.VARCHAR(length=20), autoincrement=False, nullable=False),
    sa.Column('discount_value', sa.NUMERIC(precision=10, scale=2), autoincrement=False, nullable=False),
    sa.Column('start_date', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=False),
    sa.Column('end_date', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=False),
    sa.Column('is_active', sa.BOOLEAN(), server_default=sa.text('true'), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=False),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=False),
    sa.CheckConstraint("discount_type::text = ANY (ARRAY['percentage'::character varying, 'fixed'::character varying]::text[])", name=op.f('promotions_discount_type_check')),
    sa.CheckConstraint('discount_value >= 0::numeric', name=op.f('promotions_discount_value_check')),
    sa.CheckConstraint('end_date > start_date', name=op.f('chk_promotion_dates')),
    sa.PrimaryKeyConstraint('id', name=op.f('promotions_pkey'))
    )
    op.create_table('wishlist_items',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('customer_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('product_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['customer_id'], ['customer_profiles.id'], name=op.f('fk_wishlist_customer'), ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['product_id'], ['products.id'], name=op.f('fk_wishlist_product'), ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name=op.f('wishlist_items_pkey')),
    sa.UniqueConstraint('customer_id', 'product_id', name=op.f('uq_customer_product_wishlist'), postgresql_include=[], postgresql_nulls_not_distinct=False)
    )
    op.create_table('variant_types',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('type_name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('variant_types_pkey'))
    )
    op.create_table('return_requests',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('order_item_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('customer_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('reason', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('status', sa.VARCHAR(length=20), server_default=sa.text("'pending'::character varying"), autoincrement=False, nullable=False),
    sa.Column('refund_amount', sa.NUMERIC(precision=10, scale=2), autoincrement=False, nullable=True),
    sa.Column('admin_notes', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('requested_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=False),
    sa.Column('processed_at', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=True),
    sa.CheckConstraint("status::text = ANY (ARRAY['pending'::character varying, 'approved'::character varying, 'rejected'::character varying, 'received'::character varying, 'refunded'::character varying, 'completed'::character varying]::text[])", name=op.f('return_requests_status_check')),
    sa.ForeignKeyConstraint(['customer_id'], ['customer_profiles.id'], name=op.f('fk_return_requests_customer'), ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['order_item_id'], ['order_items.id'], name=op.f('fk_return_requests_order_item'), ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name=op.f('return_requests_pkey'))
    )
    op.create_table('product_variant_images',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('product_variant_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('image_url', sa.VARCHAR(length=512), autoincrement=False, nullable=False),
    sa.Column('alt_text', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('display_order', sa.INTEGER(), server_default=sa.text('0'), autoincrement=False, nullable=False),
    sa.Column('is_primary', sa.BOOLEAN(), server_default=sa.text('false'), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['product_variant_id'], ['product_variants.id'], name=op.f('fk_product_variant_images_variant'), ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name=op.f('product_variant_images_pkey'))
    )
    op.create_table('product_promotions',
    sa.Column('product_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('promotion_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['product_id'], ['products.id'], name=op.f('fk_product_promotions_product'), ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['promotion_id'], ['promotions.id'], name=op.f('fk_product_promotions_promotion'), ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('product_id', 'promotion_id', name=op.f('product_promotions_pkey'))
    )
    op.create_table('notifications',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('customer_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('title', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('message', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('notification_type', sa.VARCHAR(length=30), autoincrement=False, nullable=False),
    sa.Column('is_read', sa.BOOLEAN(), server_default=sa.text('false'), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=False),
    sa.Column('read_at', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=True),
    sa.CheckConstraint("notification_type::text = ANY (ARRAY['order'::character varying, 'payment'::character varying, 'promotion'::character varying, 'coupon'::character varying, 'system'::character varying, 'account'::character varying]::text[])", name=op.f('notifications_notification_type_check')),
    sa.ForeignKeyConstraint(['customer_id'], ['customer_profiles.id'], name=op.f('fk_notifications_customer'), ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name=op.f('notifications_pkey'))
    )
    op.create_table('chat_threads',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('customer_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('guest_token', sa.UUID(), autoincrement=False, nullable=True),
    sa.Column('status', sa.VARCHAR(length=20), server_default=sa.text("'open'::character varying"), autoincrement=False, nullable=False),
    sa.Column('assigned_agent_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=False),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=False),
    sa.CheckConstraint("status::text = ANY (ARRAY['open'::character varying, 'assigned'::character varying, 'closed'::character varying]::text[])", name=op.f('chat_threads_status_check')),
    sa.ForeignKeyConstraint(['assigned_agent_id'], ['users.id'], name=op.f('fk_chat_threads_agent'), ondelete='SET NULL'),
    sa.ForeignKeyConstraint(['customer_id'], ['customer_profiles.id'], name=op.f('fk_chat_threads_customer'), ondelete='SET NULL'),
    sa.PrimaryKeyConstraint('id', name=op.f('chat_threads_pkey'))
    )
    op.create_table('chat_messages',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('thread_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('sender_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('sender_type', sa.VARCHAR(length=20), autoincrement=False, nullable=False),
    sa.Column('message', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('attachment_url', sa.VARCHAR(length=512), autoincrement=False, nullable=True),
    sa.Column('is_read', sa.BOOLEAN(), server_default=sa.text('false'), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=False),
    sa.CheckConstraint("sender_type::text = ANY (ARRAY['customer'::character varying, 'guest'::character varying, 'agent'::character varying, 'system'::character varying]::text[])", name=op.f('chat_messages_sender_type_check')),
    sa.ForeignKeyConstraint(['sender_id'], ['users.id'], name=op.f('fk_chat_messages_sender'), ondelete='SET NULL'),
    sa.ForeignKeyConstraint(['thread_id'], ['chat_threads.id'], name=op.f('fk_chat_messages_thread'), ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name=op.f('chat_messages_pkey'))
    )
    op.create_table('order_status_history',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('order_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('status', sa.VARCHAR(length=20), autoincrement=False, nullable=False),
    sa.Column('changed_by_user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('notes', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('changed_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['changed_by_user_id'], ['users.id'], name=op.f('fk_order_status_history_user'), ondelete='SET NULL'),
    sa.ForeignKeyConstraint(['order_id'], ['orders.id'], name=op.f('fk_order_status_history_order'), ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name=op.f('order_status_history_pkey'))
    )
    op.create_table('review_images',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('review_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('image_url', sa.VARCHAR(length=512), autoincrement=False, nullable=False),
    sa.Column('alt_text', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('display_order', sa.INTEGER(), server_default=sa.text('0'), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['review_id'], ['reviews.id'], name=op.f('fk_review_images_review'), ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name=op.f('review_images_pkey'))
    )
    op.create_table('coupon_categories',
    sa.Column('coupon_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('category_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['category_id'], ['categories.id'], name=op.f('fk_coupon_categories_category'), ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['coupon_id'], ['coupons.id'], name=op.f('fk_coupon_categories_coupon'), ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('coupon_id', 'category_id', name=op.f('coupon_categories_pkey'))
    )
    op.create_table('product_variant_options',
    sa.Column('product_variant_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('variant_value_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['product_variant_id'], ['product_variants.id'], name=op.f('product_variant_options_product_variant_id_fkey'), ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['variant_value_id'], ['variant_values.id'], name=op.f('product_variant_options_variant_value_id_fkey'), ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('product_variant_id', 'variant_value_id', name=op.f('product_variant_options_pkey'))
    )
    op.create_table('variant_values',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('variant_type_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('value_name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['variant_type_id'], ['variant_types.id'], name=op.f('fk_variant_values_variant_type'), ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name=op.f('variant_values_pkey'))
    )
    op.create_table('coupon_redemptions',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('coupon_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('customer_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('order_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('redeemed_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['coupon_id'], ['coupons.id'], name=op.f('fk_coupon_redemptions_coupon'), ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['customer_id'], ['customer_profiles.id'], name=op.f('fk_coupon_redemptions_customer'), ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['order_id'], ['orders.id'], name=op.f('fk_coupon_redemptions_order'), ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name=op.f('coupon_redemptions_pkey')),
    sa.UniqueConstraint('coupon_id', 'customer_id', 'order_id', name=op.f('uq_coupon_redemption'), postgresql_include=[], postgresql_nulls_not_distinct=False)
    )
    # ### end Alembic commands ###
````

## File: backend/alembic/versions/ec78b9a97891_add_storefront_models_and_relations.py
````python
"""add_storefront_models_and_relations

Revision ID: ec78b9a97891
Revises: 
Create Date: 2026-07-14 16:40:57.480891

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'ec78b9a97891'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    
    # 1. Drop tables in strict dependency order to prevent FK errors
    op.drop_table('product_variant_options')
    op.drop_table('variant_values')
    op.drop_table('variant_types')
    op.drop_table('knex_migrations_lock')
    op.drop_table('knex_migrations')
    
    # 2. Apply index additions and structural adjustments
    op.create_index(op.f('ix_branches_id'), 'branches', ['id'], unique=False)
    op.create_index(op.f('ix_categories_id'), 'categories', ['id'], unique=False)
    op.alter_column('order_items', 'product_variant_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.create_index(op.f('ix_order_items_id'), 'order_items', ['id'], unique=False)
    op.drop_constraint(op.f('order_items_product_variant_id_foreign'), 'order_items', type_='foreignkey')
    op.create_foreign_key(None, 'order_items', 'product_variants', ['product_variant_id'], ['id'], ondelete='SET NULL')
    op.alter_column('orders', 'created_at',
               existing_type=postgresql.TIMESTAMP(timezone=True),
               nullable=False,
               existing_server_default=sa.text('CURRENT_TIMESTAMP'))
    op.create_index(op.f('ix_orders_id'), 'orders', ['id'], unique=False)
    op.create_index(op.f('ix_permissions_id'), 'permissions', ['id'], unique=False)
    op.create_index(op.f('ix_product_categories_id'), 'product_categories', ['id'], unique=False)
    op.create_index(op.f('ix_product_variants_id'), 'product_variants', ['id'], unique=False)
    op.create_index(op.f('ix_products_id'), 'products', ['id'], unique=False)
    op.create_index(op.f('ix_role_permissions_id'), 'role_permissions', ['id'], unique=False)
    op.create_index(op.f('ix_roles_id'), 'roles', ['id'], unique=False)
    op.create_index(op.f('ix_user_branches_id'), 'user_branches', ['id'], unique=False)
    op.create_index(op.f('ix_users_id'), 'users', ['id'], unique=False)
    op.drop_constraint(op.f('users_role_id_foreign'), 'users', type_='foreignkey')
    op.create_foreign_key(None, 'users', 'roles', ['role_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='foreignkey')
    op.create_foreign_key(op.f('users_role_id_foreign'), 'users', 'roles', ['role_id'], ['id'], ondelete='RESTRICT')
    op.drop_index(op.f('ix_users_id'), table_name='users')
    op.drop_index(op.f('ix_user_branches_id'), table_name='user_branches')
    op.drop_index(op.f('ix_roles_id'), table_name='roles')
    op.drop_index(op.f('ix_role_permissions_id'), table_name='role_permissions')
    op.drop_index(op.f('ix_products_id'), table_name='products')
    op.drop_index(op.f('ix_product_variants_id'), table_name='product_variants')
    op.drop_index(op.f('ix_product_categories_id'), table_name='product_categories')
    op.drop_index(op.f('ix_permissions_id'), table_name='permissions')
    op.drop_index(op.f('ix_orders_id'), table_name='orders')
    op.alter_column('orders', 'created_at',
               existing_type=postgresql.TIMESTAMP(timezone=True),
               nullable=True,
               existing_server_default=sa.text('CURRENT_TIMESTAMP'))
    op.drop_constraint(None, 'order_items', type_='foreignkey')
    op.create_foreign_key(op.f('order_items_product_variant_id_foreign'), 'order_items', 'product_variants', ['product_variant_id'], ['id'], ondelete='RESTRICT')
    op.drop_index(op.f('ix_order_items_id'), table_name='order_items')
    op.alter_column('order_items', 'product_variant_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.drop_index(op.f('ix_categories_id'), table_name='categories')
    op.drop_index(op.f('ix_branches_id'), table_name='branches')
    op.create_table('product_variant_options',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('product_variant_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('variant_value_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=False),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['product_variant_id'], ['product_variants.id'], name=op.f('product_variant_options_product_variant_id_foreign'), ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['variant_value_id'], ['variant_values.id'], name=op.f('product_variant_options_variant_value_id_foreign'), ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name=op.f('product_variant_options_pkey')),
    sa.UniqueConstraint('product_variant_id', 'variant_value_id', name=op.f('product_variant_options_product_variant_id_variant_value_id_uni'), postgresql_include=[], postgresql_nulls_not_distinct=False)
    )
    op.create_table('variant_values',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('variant_type_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('value_name', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=False),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['variant_type_id'], ['variant_types.id'], name=op.f('variant_values_variant_type_id_foreign'), ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name=op.f('variant_values_pkey'))
    )
    op.create_table('knex_migrations',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('batch', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('migration_time', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('knex_migrations_pkey'))
    )
    op.create_table('variant_types',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('type_name', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=False),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('variant_types_pkey')),
    sa.UniqueConstraint('type_name', name=op.f('variant_types_type_name_unique'), postgresql_include=[], postgresql_nulls_not_distinct=False)
    )
    op.create_table('knex_migrations_lock',
    sa.Column('index', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('is_locked', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('index', name=op.f('knex_migrations_lock_pkey'))
    )
    # ### end Alembic commands ###
````

## File: backend/alembic/README
````
Generic single-database configuration.
````

## File: backend/alembic/script.py.mako
````
"""${message}

Revision ID: ${up_revision}
Revises: ${down_revision | comma,n}
Create Date: ${create_date}

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
${imports if imports else ""}

# revision identifiers, used by Alembic.
revision: str = ${repr(up_revision)}
down_revision: Union[str, Sequence[str], None] = ${repr(down_revision)}
branch_labels: Union[str, Sequence[str], None] = ${repr(branch_labels)}
depends_on: Union[str, Sequence[str], None] = ${repr(depends_on)}


def upgrade() -> None:
    """Upgrade schema."""
    ${upgrades if upgrades else "pass"}


def downgrade() -> None:
    """Downgrade schema."""
    ${downgrades if downgrades else "pass"}
````

## File: backend/app/api/routes/reviews.py
````python
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.session import get_db
from app.models.customer_profile import CustomerProfile
from app.models.product import Product
from app.models.review import Review
from app.models.user import User
from app.schemas.review import ReviewCreate, ReviewOut, ReviewUpdate
from app.core.auth import get_current_user

router = APIRouter()


async def _get_or_create_customer_profile(db: AsyncSession, user: User) -> CustomerProfile:
    result = await db.execute(select(CustomerProfile).where(CustomerProfile.user_id == user.id))
    profile = result.scalar_one_or_none()
    if not profile:
        profile = CustomerProfile(user_id=user.id)
        db.add(profile)
        await db.commit()
        await db.refresh(profile)
    return profile


@router.get("/products/{product_id}/reviews", response_model=list[ReviewOut])
async def get_product_reviews(
    product_id: int,
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(select(Product).where(Product.id == product_id))
    product = result.scalar_one_or_none()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    result = await db.execute(select(Review).where(Review.product_id == product_id))
    return result.scalars().all()


@router.post("/products/{product_id}/reviews", response_model=ReviewOut, status_code=201)
async def create_product_review(
    product_id: int,
    payload: ReviewCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    result = await db.execute(select(Product).where(Product.id == product_id))
    product = result.scalar_one_or_none()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    profile = await _get_or_create_customer_profile(db, current_user)

    # TODO: BYPASSED VERIFIED-PURCHASE CHECK.
    # Checkout isn't built yet, so there's no real link from order_item_id -> this
    # customer. Once POST /checkout exists and Order has a customer_id, replace this
    # block with a real check, e.g.:
    #   - fetch OrderItem by payload.order_item_id
    #   - join to Order, confirm Order.customer_id == profile.id
    #   - confirm OrderItem.product_variant -> product_id == product_id
    #   - 404/403 if any of that fails
    # For now we only confirm the order_item_id points to a row that exists.
    from app.models.order_item import OrderItem
    result = await db.execute(select(OrderItem).where(OrderItem.id == payload.order_item_id))
    order_item = result.scalar_one_or_none()
    if not order_item:
        raise HTTPException(status_code=404, detail="Order item not found")

    new_review = Review(
        customer_id=profile.id,
        product_id=product_id,
        order_item_id=payload.order_item_id,
        rating=payload.rating,
        comment=payload.comment,
    )
    db.add(new_review)
    await db.commit()
    await db.refresh(new_review)
    return new_review


@router.put("/reviews/{review_id}", response_model=ReviewOut)
async def update_review(
    review_id: int,
    payload: ReviewUpdate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    profile = await _get_or_create_customer_profile(db, current_user)

    result = await db.execute(select(Review).where(Review.id == review_id))
    review = result.scalar_one_or_none()
    if not review:
        raise HTTPException(status_code=404, detail="Review not found")

    if review.customer_id != profile.id:
        raise HTTPException(status_code=403, detail="You can only edit your own reviews")

    update_data = payload.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(review, field, value)

    await db.commit()
    await db.refresh(review)
    return review


@router.delete("/reviews/{review_id}", status_code=204)
async def delete_review(
    review_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    profile = await _get_or_create_customer_profile(db, current_user)

    result = await db.execute(select(Review).where(Review.id == review_id))
    review = result.scalar_one_or_none()
    if not review:
        raise HTTPException(status_code=404, detail="Review not found")

    if review.customer_id != profile.id:
        raise HTTPException(status_code=403, detail="You can only delete your own reviews")

    await db.delete(review)
    await db.commit()
    return None
````

## File: backend/app/api/routes/wishlist.py
````python
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.session import get_db
from app.core.auth import get_current_user
from app.models.user import User
from app.models.customer_profile import CustomerProfile
from app.models.product import Product
from app.models.wishlist import Wishlist
from app.schemas.wishlist import WishlistCreate, WishlistResponse

router = APIRouter(prefix="/wishlist", tags=["Wishlist"])


async def _get_or_create_customer_profile(db: AsyncSession, user: User) -> CustomerProfile:
    result = await db.execute(select(CustomerProfile).where(CustomerProfile.user_id == user.id))
    profile = result.scalar_one_or_none()
    if not profile:
        profile = CustomerProfile(user_id=user.id)
        db.add(profile)
        await db.commit()
        await db.refresh(profile)
    return profile


@router.get("", response_model=list[WishlistResponse])
async def get_wishlist(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    profile = await _get_or_create_customer_profile(db, current_user)
    result = await db.execute(select(Wishlist).where(Wishlist.customer_id == profile.id))
    return result.scalars().all()


@router.post("", response_model=WishlistResponse, status_code=status.HTTP_201_CREATED)
async def add_to_wishlist(
    payload: WishlistCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    profile = await _get_or_create_customer_profile(db, current_user)

    product = await db.execute(select(Product).where(Product.id == payload.product_id))
    if not product.scalar_one_or_none():
        raise HTTPException(status_code=404, detail="Product not found")

    existing = await db.execute(
        select(Wishlist).where(
            Wishlist.customer_id == profile.id,
            Wishlist.product_id == payload.product_id,
        )
    )
    if existing.scalar_one_or_none():
        raise HTTPException(status_code=400, detail="Product already in wishlist")

    item = Wishlist(customer_id=profile.id, product_id=payload.product_id)
    db.add(item)
    await db.commit()
    await db.refresh(item)
    return item


@router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
async def remove_from_wishlist(
    product_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    profile = await _get_or_create_customer_profile(db, current_user)
    result = await db.execute(
        select(Wishlist).where(
            Wishlist.customer_id == profile.id,
            Wishlist.product_id == product_id,
        )
    )
    item = result.scalar_one_or_none()
    if not item:
        raise HTTPException(status_code=404, detail="Product not found in wishlist")

    await db.delete(item)
    await db.commit()
````

## File: backend/app/core/cart_helpers.py
````python

````

## File: backend/app/core/email.py
````python
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from app.core.config import settings

FROM_EMAIL = settings.FROM_EMAIL


def send_email(to: str, subject: str, body: str, html: bool = False) -> None:
    msg = MIMEMultipart()
    msg["From"] = FROM_EMAIL
    msg["To"] = to
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "html" if html else "plain"))

    with smtplib.SMTP(settings.SMTP_HOST, settings.SMTP_PORT) as server:
        server.starttls()
        server.login(settings.SMTP_USERNAME, settings.SMTP_PASSWORD)
        server.sendmail(FROM_EMAIL, [to], msg.as_string())


def send_verification_email(to: str, token: str) -> None:
    link = f"{settings.FRONTEND_URL}/verify-email?token={token}"
    subject = "Verify your email"
    body = f"Click the link to verify your email: {link}\nThis link expires in 24 hours."
    send_email(to, subject, body)


def send_password_reset_email(to: str, token: str) -> None:
    link = f"{settings.FRONTEND_URL}/reset-password?token={token}"
    subject = "Reset your password"
    body = f"Click the link to reset your password: {link}\nThis link expires in 1 hour."
    send_email(to, subject, body)
````

## File: backend/app/core/permissions.py
````python
from fastapi import Depends, HTTPException, status

from app.models.user import User
from app.core.auth import get_current_user

ADMIN = 1
MANAGER = 2
STAFF = 3


def require_role(*allowed_role_ids: int):
    """
    Returns a FastAPI dependency that checks whether the current user's
    role_id is in the allowed list.

    Usage:
        @router.post("/products")
        def create_product(
            current_user: User = Depends(require_role(ADMIN, MANAGER, STAFF))
        ):
            ...
    """

    def dependency(current_user: User = Depends(get_current_user)) -> User:
        if current_user.role_id not in allowed_role_ids:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="You do not have permission to perform this action",
            )
        return current_user

    return dependency


def block_manager_on_admin_target(current_user: User, target_role_id: int):
    """
    Managers can manage roles/permissions for everyone except Admins.
    Call this after fetching the target resource's role_id.
    """
    if current_user.role_id == MANAGER and target_role_id == ADMIN:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Managers cannot modify Admin-level roles or users",
        )
````

## File: backend/app/core/security.py
````python
import bcrypt


def hash_password(password: str) -> str:
    password_bytes = password.encode("utf-8")
    hashed = bcrypt.hashpw(password_bytes, bcrypt.gensalt())
    return hashed.decode("utf-8")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    password_bytes = plain_password.encode("utf-8")
    hashed_bytes = hashed_password.encode("utf-8")
    return bcrypt.checkpw(password_bytes, hashed_bytes)
````

## File: backend/app/core/test_seed.py
````python
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.product import Product
from app.models.product_variant import ProductVariant
from app.models.coupon import Coupon
from datetime import datetime, timedelta, timezone

BOGUS_PRODUCT_ID = 999001
BOGUS_VARIANT_ID = 999001
BOGUS_VARIANT_SKU = "BOGUS-TEST-SKU"
BOGUS_COUPON_CODE = "TESTCODE10"


async def ensure_bogus_data(db: AsyncSession) -> None:
    result = await db.execute(select(Product).where(Product.id == BOGUS_PRODUCT_ID))
    product = result.scalar_one_or_none()
    if not product:
        product = Product(
            id=BOGUS_PRODUCT_ID,
            name="Bogus Test Product",
            description="Auto-seeded for TEST_MODE. Safe to delete.",
            price=9.99,
            is_active=True,
        )
        db.add(product)
        await db.flush()

    result = await db.execute(select(ProductVariant).where(ProductVariant.id == BOGUS_VARIANT_ID))
    variant = result.scalar_one_or_none()
    if not variant:
        variant = ProductVariant(
            id=BOGUS_VARIANT_ID,
            product_id=BOGUS_PRODUCT_ID,
            sku=BOGUS_VARIANT_SKU,
            price=9.99,
            stock_quantity=1000,
            is_active=True,
        )
        db.add(variant)

    result = await db.execute(select(Coupon).where(Coupon.code == BOGUS_COUPON_CODE))
    coupon = result.scalar_one_or_none()
    if not coupon:
        coupon = Coupon(
            code=BOGUS_COUPON_CODE,
            name="Bogus Test Coupon",
            description="Auto-seeded for TEST_MODE. Safe to delete.",
            discount_type="percentage",
            discount_value=10,
            minimum_order_amount=0,
            usage_limit=None,
            usage_count=0,
            start_date=datetime.now(timezone.utc) - timedelta(days=1),
            end_date=datetime.now(timezone.utc) + timedelta(days=365),
            is_active=True,
        )
        db.add(coupon)

    await db.commit()
````

## File: backend/app/models/address.py
````python
from datetime import datetime

from sqlalchemy import Boolean, DateTime, ForeignKey, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class Address(Base):
    __tablename__ = "addresses"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    customer_id: Mapped[int] = mapped_column(
        ForeignKey("customer_profiles.id", ondelete="CASCADE"), nullable=False
    )
    country: Mapped[str] = mapped_column(String(100), nullable=False)
    state: Mapped[str | None] = mapped_column(String(100), nullable=True)
    city: Mapped[str] = mapped_column(String(100), nullable=False)
    postal_code: Mapped[str | None] = mapped_column(String(20), nullable=True)
    address_line_1: Mapped[str] = mapped_column(String(255), nullable=False)
    address_line_2: Mapped[str | None] = mapped_column(String(255), nullable=True)
    is_default: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )

    customer: Mapped["CustomerProfile"] = relationship(back_populates="addresses")
````

## File: backend/app/models/coupon.py
````python
from datetime import datetime

from sqlalchemy import Boolean, DateTime, Integer, Numeric, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class Coupon(Base):
    __tablename__ = "coupons"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    code: Mapped[str] = mapped_column(String(50), unique=True, nullable=False, index=True)
    name: Mapped[str] = mapped_column(String(150), nullable=False)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)

    discount_type: Mapped[str] = mapped_column(String(20), nullable=False)
    discount_value: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False)

    minimum_order_amount: Mapped[float | None] = mapped_column(Numeric(10, 2), nullable=True, default=0)
    usage_limit: Mapped[int | None] = mapped_column(Integer, nullable=True)
    usage_count: Mapped[int] = mapped_column(Integer, nullable=False, default=0)

    start_date: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    end_date: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)

    is_active: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
    )

    # Relationships
    carts: Mapped[list["Cart"]] = relationship(back_populates="coupon")
````

## File: backend/app/models/customer_order.py
````python
# Customer-domain re-export.
# orders/order_items/return_requests are single shared tables — the ORM
# models live in app/models/order.py, app/models/order_item.py, and
# app/models/return_request.py. This module re-exports them under the
# customer namespace so customer_order router/schema imports stay
# consistent, without creating a second mapper on the same tables.

from app.models.order import Order
from app.models.order_item import OrderItem
from app.models.return_request import ReturnRequest

__all__ = ["Order", "OrderItem", "ReturnRequest"]
````

## File: backend/app/models/customer_profile.py
````python
from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class CustomerProfile(Base):
    __tablename__ = "customer_profiles"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"), nullable=False, unique=True
    )
    status: Mapped[str] = mapped_column(String(20), nullable=False, default="active")

    created_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )

   # Relationships
    user: Mapped["User"] = relationship(back_populates="customer_profile")
    cart: Mapped["Cart"] = relationship(back_populates="customer", uselist=False)
    addresses: Mapped[list["Address"]] = relationship(back_populates="customer")
````

## File: backend/app/models/payment.py
````python
from datetime import datetime
from sqlalchemy import DateTime, ForeignKey, Numeric, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database.base import Base


class Payment(Base):
    __tablename__ = "payments"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    order_id: Mapped[int] = mapped_column(ForeignKey("orders.id", ondelete="CASCADE"), nullable=False)

    payment_method: Mapped[str | None] = mapped_column(String(50), nullable=True)
    provider: Mapped[str | None] = mapped_column(String(50), nullable=True)
    stripe_payment_intent_id: Mapped[str | None] = mapped_column(
        String(255), unique=True, nullable=True, index=True
    )
    amount: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False)
    currency: Mapped[str] = mapped_column(String(10), nullable=False, default="usd")
    status: Mapped[str] = mapped_column(String(20), nullable=False, default="pending")

    created_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    order: Mapped["Order"] = relationship()
````

## File: backend/app/models/permission.py
````python
from sqlalchemy import DateTime, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class Permission(Base):
    __tablename__ = "permissions"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    name: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)

    description: Mapped[str | None] = mapped_column(String(255), nullable=True)

    created_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    updated_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )

    # Relationships
    role_links: Mapped[list["RolePermission"]] = relationship(
        back_populates="permission",
        cascade="all, delete-orphan"
    )
````

## File: backend/app/models/product_category.py
````python
from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, UniqueConstraint, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class ProductCategory(Base):
    __tablename__ = "product_categories"
    __table_args__ = (
        UniqueConstraint("product_id", "category_id", name="product_categories_product_id_category_id_unique"),
    )

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    product_id: Mapped[int] = mapped_column(ForeignKey("products.id", ondelete="CASCADE"), nullable=False)
    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id", ondelete="CASCADE"), nullable=False)

    created_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now()
    )
    updated_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )

    # Relationships
    product: Mapped["Product"] = relationship(back_populates="category_links")
    category: Mapped["Category"] = relationship(back_populates="product_links")
````

## File: backend/app/models/product_variant.py
````python
from datetime import datetime

from sqlalchemy import Boolean, DateTime, ForeignKey, Integer, Numeric, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class ProductVariant(Base):
    __tablename__ = "product_variants"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    product_id: Mapped[int] = mapped_column(ForeignKey("products.id", ondelete="CASCADE"), nullable=False)
    sku: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    price: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False)
    stock_quantity: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)

    created_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now()
    )
    updated_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )

    # Relationships
    product: Mapped["Product"] = relationship(back_populates="variants")
````

## File: backend/app/models/product.py
````python
from datetime import datetime
from sqlalchemy import Boolean, DateTime, Numeric, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(150), nullable=False)
    description: Mapped[str | None] = mapped_column(String(500), nullable=True)
    price: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)

    created_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now()
    )
    updated_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )

    # Relationships
    category_links: Mapped[list["ProductCategory"]] = relationship(
        back_populates="product",
        cascade="all, delete-orphan"
    )
    variants: Mapped[list["ProductVariant"]] = relationship(
        back_populates="product",
        cascade="all, delete-orphan"
    )

    @property
    def categories(self) -> list["Category"]:
        return [link.category for link in self.category_links]
````

## File: backend/app/models/return_request.py
````python
from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Numeric, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class ReturnRequest(Base):
    __tablename__ = "return_requests"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    order_item_id: Mapped[int] = mapped_column(
        ForeignKey("order_items.id", ondelete="CASCADE"), nullable=False
    )
    customer_id: Mapped[int] = mapped_column(
        ForeignKey("customer_profiles.id", ondelete="CASCADE"), nullable=False
    )

    reason: Mapped[str | None] = mapped_column(Text, nullable=True)
    status: Mapped[str] = mapped_column(String(20), nullable=False, default="pending")
    refund_amount: Mapped[float | None] = mapped_column(Numeric(10, 2), nullable=True)

    requested_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    processed_at: Mapped[DateTime | None] = mapped_column(DateTime(timezone=True), nullable=True)

    # Relationships
    order_item: Mapped["OrderItem"] = relationship()
    customer: Mapped["CustomerProfile"] = relationship()
````

## File: backend/app/models/review.py
````python
from datetime import datetime

from sqlalchemy import CheckConstraint, DateTime, ForeignKey, Integer, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class Review(Base):
    __tablename__ = "reviews"
    __table_args__ = (
        CheckConstraint("rating >= 1 AND rating <= 5", name="reviews_rating_check"),
    )

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    customer_id: Mapped[int] = mapped_column(
        ForeignKey("customer_profiles.id", ondelete="CASCADE"), nullable=False
    )
    product_id: Mapped[int] = mapped_column(
        ForeignKey("products.id", ondelete="CASCADE"), nullable=False
    )
    order_item_id: Mapped[int] = mapped_column(
        ForeignKey("order_items.id", ondelete="CASCADE"), nullable=False
    )

    rating: Mapped[int] = mapped_column(Integer, nullable=False)
    comment: Mapped[str | None] = mapped_column(Text, nullable=True)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )

    # Relationships
    customer: Mapped["CustomerProfile"] = relationship()
    product: Mapped["Product"] = relationship()
    order_item: Mapped["OrderItem"] = relationship()
````

## File: backend/app/models/role_permission.py
````python
from sqlalchemy import DateTime, ForeignKey, UniqueConstraint, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class RolePermission(Base):
    __tablename__ = "role_permissions"
    __table_args__ = (
        UniqueConstraint("role_id", "permission_id", name="role_permissions_role_id_permission_id_unique"),
    )

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    role_id: Mapped[int] = mapped_column(ForeignKey("roles.id", ondelete="CASCADE"), nullable=False)
    permission_id: Mapped[int] = mapped_column(ForeignKey("permissions.id", ondelete="CASCADE"), nullable=False)

    created_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    updated_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )

    # Relationships
    role: Mapped["Role"] = relationship(back_populates="permission_links")
    permission: Mapped["Permission"] = relationship(back_populates="role_links")
````

## File: backend/app/models/role.py
````python
from sqlalchemy import (
    DateTime,
    Integer,
    String,
    func
)

from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class Role(Base):
    __tablename__ = "roles"

    # Primary Key
    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True
    )

    # Basic Fields
    name: Mapped[str] = mapped_column(
        String(50),
        unique=True,
        nullable=False
    )

    description: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True
    )

    # Timestamps
    created_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    updated_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )

     # Relationships
    users = relationship("User", back_populates="role")
    permission_links: Mapped[list["RolePermission"]] = relationship(
        back_populates="role",
        cascade="all, delete-orphan"
    )
````

## File: backend/app/models/wishlist.py
````python
from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, UniqueConstraint, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class Wishlist(Base):
    __tablename__ = "wishlist_items"
    __table_args__ = (
    UniqueConstraint("customer_id", "product_id", name="uq_customer_product_wishlist"),
)

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    customer_id: Mapped[int] = mapped_column(
        ForeignKey("customer_profiles.id", ondelete="CASCADE"), nullable=False
    )
    product_id: Mapped[int] = mapped_column(
        ForeignKey("products.id", ondelete="CASCADE"), nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )

    customer: Mapped["CustomerProfile"] = relationship()
    product: Mapped["Product"] = relationship()
````

## File: backend/app/repositories/cart_repository.py
````python

````

## File: backend/app/schemas/__init__.py
````python

````

## File: backend/app/schemas/address.py
````python
from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class AddressBase(BaseModel):
    country: str
    state: Optional[str] = None
    city: str
    postal_code: Optional[str] = None
    address_line_1: str
    address_line_2: Optional[str] = None
    is_default: bool = False


class AddressCreate(AddressBase):
    pass


class AddressUpdate(BaseModel):
    country: Optional[str] = None
    state: Optional[str] = None
    city: Optional[str] = None
    postal_code: Optional[str] = None
    address_line_1: Optional[str] = None
    address_line_2: Optional[str] = None
    is_default: Optional[bool] = None


class AddressOut(AddressBase):
    id: int
    customer_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
````

## File: backend/app/schemas/customer_profile.py
````python
from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime


class CustomerRegister(BaseModel):
    name: str
    email: EmailStr
    password: str
    phone_number: Optional[str] = None


class EmailVerifyRequest(BaseModel):
    token: str


class CustomerProfileOut(BaseModel):
    id: int
    name: str
    email: EmailStr
    phone_number: Optional[str]
    avatar_url: Optional[str]
    email_verified: bool
    created_at: datetime

    class Config:
        from_attributes = True


class CustomerProfileUpdate(BaseModel):
    name: Optional[str] = None
    phone_number: Optional[str] = None
    avatar_url: Optional[str] = None
````

## File: backend/app/schemas/order_item.py
````python
from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field


class OrderItemOut(BaseModel):
    id: int
    order_id: int
    product_variant_id: int | None
    quantity: int
    price_at_purchase: float
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class OrderItemCreate(BaseModel):
    product_variant_id: int
    quantity: int = Field(gt=0)
    price_at_purchase: float = Field(gt=0)


class OrderItemUpdate(BaseModel):
    quantity: int | None = Field(default=None, gt=0)
    price_at_purchase: float | None = Field(default=None, gt=0)
````

## File: backend/app/schemas/permission.py
````python
from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field


class PermissionOut(BaseModel):
    id: int
    name: str
    description: str | None = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class PermissionCreate(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    description: str | None = None


class PermissionUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=1, max_length=100)
    description: str | None = None
````

## File: backend/app/schemas/product_category.py
````python
from datetime import datetime
from pydantic import BaseModel, ConfigDict

from app.schemas.category import CategoryOut


class ProductCategoryOut(BaseModel):
    id: int
    product_id: int
    category_id: int
    category: CategoryOut
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class ProductCategoryCreate(BaseModel):
    category_id: int
````

## File: backend/app/schemas/product_variant.py
````python
from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field


class ProductVariantOut(BaseModel):
    id: int
    product_id: int
    sku: str
    price: float
    stock_quantity: int
    is_active: bool
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class ProductVariantCreate(BaseModel):
    sku: str = Field(min_length=1, max_length=100)
    price: float = Field(gt=0)
    stock_quantity: int = Field(default=0, ge=0)
    is_active: bool = True


class ProductVariantUpdate(BaseModel):
    sku: str | None = Field(default=None, min_length=1, max_length=100)
    price: float | None = Field(default=None, gt=0)
    stock_quantity: int | None = Field(default=None, ge=0)
    is_active: bool | None = None
````

## File: backend/app/schemas/product.py
````python
from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field

from app.schemas.category import CategoryOut


class ProductOut(BaseModel):
    id: int
    name: str
    description: str | None = None
    price: float
    is_active: bool
    created_at: datetime
    updated_at: datetime
    categories: list[CategoryOut] = []

    model_config = ConfigDict(from_attributes=True)


class ProductCreate(BaseModel):
    name: str = Field(min_length=1, max_length=150)
    description: str | None = Field(default=None, max_length=500)
    price: float = Field(gt=0)
    is_active: bool = True


class ProductUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=1, max_length=150)
    description: str | None = Field(default=None, max_length=500)
    price: float | None = Field(default=None, gt=0)
    is_active: bool | None = None
````

## File: backend/app/schemas/review.py
````python
from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class ReviewCreate(BaseModel):
    order_item_id: int
    rating: int = Field(ge=1, le=5)
    comment: str | None = None


class ReviewUpdate(BaseModel):
    rating: int | None = Field(default=None, ge=1, le=5)
    comment: str | None = None


class ReviewOut(BaseModel):
    id: int
    customer_id: int
    product_id: int
    order_item_id: int
    rating: int
    comment: str | None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
````

## File: backend/app/schemas/role_permission.py
````python
from datetime import datetime
from pydantic import BaseModel, ConfigDict

from app.schemas.permission import PermissionOut


class RolePermissionOut(BaseModel):
    id: int
    role_id: int
    permission_id: int
    permission: PermissionOut
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class RolePermissionCreate(BaseModel):
    permission_id: int
````

## File: backend/app/schemas/role.py
````python
from pydantic import BaseModel, ConfigDict, Field


class RoleOut(BaseModel):
    id: int
    name: str
    description: str | None = None

    model_config = ConfigDict(from_attributes=True)

class RoleCreate(BaseModel):
    name: str = Field(min_length=1, max_length=50)
    description: str | None = None


class RoleUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=1, max_length=50)
    description: str | None = None
````

## File: backend/app/schemas/wishlist.py
````python
from datetime import datetime

from pydantic import BaseModel, ConfigDict


class WishlistCreate(BaseModel):
    product_id: int


class WishlistResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    customer_id: int
    product_id: int
    created_at: datetime
````

## File: backend/tests/__init__.py
````python

````

## File: backend/tests/test_checkout.py
````python
import pytest
from sqlalchemy import select

from app.models.customer_profile import CustomerProfile
from app.models.product_variant import ProductVariant
from app.models.order import Order

pytestmark = pytest.mark.asyncio


async def test_checkout_success(client, make_customer, auth_headers, make_product_variant, make_cart_with_item, db):
    user, _ = await make_customer(email="checkoutsuccess@example.com")
    headers = auth_headers(user)

    result = await db.execute(select(CustomerProfile).where(CustomerProfile.user_id == user.id))
    profile = result.scalar_one()

    variant = await make_product_variant(price=25.00, stock_quantity=10)
    await make_cart_with_item(profile.id, variant, quantity=2)

    resp = await client.post("/checkout", headers=headers)
    assert resp.status_code == 201
    body = resp.json()
    assert body["status"] == "open"
    assert body["total_amount"] == 50.0
    assert len(body["items"]) == 1
    assert body["items"][0]["quantity"] == 2

    await db.refresh(variant)
    assert variant.stock_quantity == 8


async def test_checkout_empty_cart(client, make_customer, auth_headers):
    user, _ = await make_customer(email="checkoutempty@example.com")
    headers = auth_headers(user)

    resp = await client.post("/checkout", headers=headers)
    assert resp.status_code == 400
    assert resp.json()["detail"] == "Cart is empty"


async def test_checkout_no_cart_at_all(client, make_customer, auth_headers):
    user, _ = await make_customer(email="checkoutnocart@example.com")
    headers = auth_headers(user)

    resp = await client.post("/checkout", headers=headers)
    assert resp.status_code == 400
    assert resp.json()["detail"] == "Cart is empty"


async def test_checkout_insufficient_stock(client, make_customer, auth_headers, make_product_variant, make_cart_with_item, db):
    user, _ = await make_customer(email="checkoutstock@example.com")
    headers = auth_headers(user)

    result = await db.execute(select(CustomerProfile).where(CustomerProfile.user_id == user.id))
    profile = result.scalar_one()

    variant = await make_product_variant(price=10.00, stock_quantity=1)
    await make_cart_with_item(profile.id, variant, quantity=5)

    resp = await client.post("/checkout", headers=headers)
    assert resp.status_code == 400
    assert "Insufficient stock" in resp.json()["detail"]

    await db.refresh(variant)
    assert variant.stock_quantity == 1


async def test_checkout_inactive_variant(client, make_customer, auth_headers, make_product_variant, make_cart_with_item, db):
    user, _ = await make_customer(email="checkoutinactive@example.com")
    headers = auth_headers(user)

    result = await db.execute(select(CustomerProfile).where(CustomerProfile.user_id == user.id))
    profile = result.scalar_one()

    variant = await make_product_variant(price=10.00, stock_quantity=10, is_active=False)
    await make_cart_with_item(profile.id, variant, quantity=1)

    resp = await client.post("/checkout", headers=headers)
    assert resp.status_code == 400
    assert "no longer available" in resp.json()["detail"]


async def test_checkout_clears_cart_items(client, make_customer, auth_headers, make_product_variant, make_cart_with_item, db):
    user, _ = await make_customer(email="checkoutclears@example.com")
    headers = auth_headers(user)

    result = await db.execute(select(CustomerProfile).where(CustomerProfile.user_id == user.id))
    profile = result.scalar_one()

    variant = await make_product_variant(price=15.00, stock_quantity=5)
    cart = await make_cart_with_item(profile.id, variant, quantity=1)

    resp = await client.post("/checkout", headers=headers)
    assert resp.status_code == 201

    db.expire_all()

    second_resp = await client.post("/checkout", headers=headers)
    assert second_resp.status_code == 400
    assert second_resp.json()["detail"] == "Cart is empty"


async def test_checkout_unauthenticated(client):
    resp = await client.post("/checkout")
    assert resp.status_code == 401


async def test_checkout_multiple_items_total(client, make_customer, auth_headers, make_product_variant, make_cart_with_item, db):
    user, _ = await make_customer(email="checkoutmulti@example.com")
    headers = auth_headers(user)

    result = await db.execute(select(CustomerProfile).where(CustomerProfile.user_id == user.id))
    profile = result.scalar_one()

    variant_a = await make_product_variant(price=10.00, stock_quantity=10)
    cart = await make_cart_with_item(profile.id, variant_a, quantity=3)

    from app.models.cart_item import CartItem
    variant_b = await make_product_variant(price=5.00, stock_quantity=10)
    db.add(CartItem(cart_id=cart.id, product_variant_id=variant_b.id, quantity=4))
    await db.commit()

    resp = await client.post("/checkout", headers=headers)
    assert resp.status_code == 201
    body = resp.json()
    assert body["total_amount"] == 50.0
    assert len(body["items"]) == 2
````

## File: backend/tests/test_customer_order.py
````python
import pytest
from httpx import AsyncClient
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.order import Order
from app.models.order_item import OrderItem
from app.models.customer_profile import CustomerProfile


async def _get_profile(db: AsyncSession, user) -> CustomerProfile:
    result = await db.execute(select(CustomerProfile).where(CustomerProfile.user_id == user.id))
    return result.scalar_one()


async def _make_order(
    db: AsyncSession,
    customer_id: int,
    order_status: str = "open",
    total_amount: float = 0,
) -> Order:
    order = Order(
        customer_id=customer_id,
        order_status=order_status,
        total_amount=total_amount,
    )
    db.add(order)
    await db.commit()
    await db.refresh(order)
    return order


async def _make_order_item(
    db: AsyncSession,
    order_id: int,
    variant,
    quantity: int = 2,
) -> OrderItem:
    item = OrderItem(
        order_id=order_id,
        product_variant_id=variant.id,
        quantity=quantity,
        price_at_purchase=variant.price,
    )
    db.add(item)
    await db.commit()
    await db.refresh(item)
    return item


# ---- Orders: cancel ----

@pytest.mark.asyncio
async def test_cancel_order_success(client: AsyncClient, db: AsyncSession, make_customer, auth_headers):
    user, _ = await make_customer()
    profile = await _get_profile(db, user)
    order = await _make_order(db, profile.id, order_status="open")

    response = await client.post(f"/orders/{order.id}/cancel", headers=auth_headers(user))

    assert response.status_code == 200
    assert response.json()["order_status"] == "cancelled"


@pytest.mark.asyncio
async def test_cancel_order_wrong_status(client: AsyncClient, db: AsyncSession, make_customer, auth_headers):
    user, _ = await make_customer()
    profile = await _get_profile(db, user)
    order = await _make_order(db, profile.id, order_status="completed")

    response = await client.post(f"/orders/{order.id}/cancel", headers=auth_headers(user))

    assert response.status_code == 400


@pytest.mark.asyncio
async def test_cancel_order_not_owned(client: AsyncClient, db: AsyncSession, make_customer, auth_headers):
    owner, _ = await make_customer(email="owner@example.com")
    other, _ = await make_customer(email="other@example.com")
    profile = await _get_profile(db, owner)
    order = await _make_order(db, profile.id, order_status="open")

    response = await client.post(f"/orders/{order.id}/cancel", headers=auth_headers(other))

    assert response.status_code == 404


# ---- Orders: reorder ----

@pytest.mark.asyncio
async def test_reorder_creates_cart_items(
    client: AsyncClient, db: AsyncSession, make_customer, make_product_variant, auth_headers
):
    user, _ = await make_customer()
    profile = await _get_profile(db, user)
    variant = await make_product_variant()
    order = await _make_order(db, profile.id, order_status="completed")
    await _make_order_item(db, order.id, variant, quantity=3)

    response = await client.post(f"/orders/{order.id}/reorder", headers=auth_headers(user))

    assert response.status_code == 201
    assert response.json()["id"] == order.id


@pytest.mark.asyncio
async def test_reorder_not_owned(client: AsyncClient, db: AsyncSession, make_customer, auth_headers):
    owner, _ = await make_customer(email="owner2@example.com")
    other, _ = await make_customer(email="other2@example.com")
    profile = await _get_profile(db, owner)
    order = await _make_order(db, profile.id, order_status="completed")

    response = await client.post(f"/orders/{order.id}/reorder", headers=auth_headers(other))

    assert response.status_code == 404


# ---- Orders: invoice ----

@pytest.mark.asyncio
async def test_get_invoice_success(client: AsyncClient, db: AsyncSession, make_customer, auth_headers):
    user, _ = await make_customer()
    profile = await _get_profile(db, user)
    order = await _make_order(db, profile.id, order_status="completed", total_amount=100)

    response = await client.get(f"/orders/{order.id}/invoice", headers=auth_headers(user))

    assert response.status_code == 200
    assert response.json()["id"] == order.id


@pytest.mark.asyncio
async def test_get_invoice_not_found(client: AsyncClient, make_customer, auth_headers):
    user, _ = await make_customer()

    response = await client.get("/orders/999999/invoice", headers=auth_headers(user))

    assert response.status_code == 404


# ---- Return Requests: create ----

@pytest.mark.asyncio
async def test_create_return_request_success(
    client: AsyncClient, db: AsyncSession, make_customer, make_product_variant, auth_headers
):
    user, _ = await make_customer()
    profile = await _get_profile(db, user)
    variant = await make_product_variant()
    order = await _make_order(db, profile.id, order_status="completed")
    item = await _make_order_item(db, order.id, variant)

    response = await client.post(
        "/return-requests",
        json={"order_item_id": item.id, "reason": "Wrong size"},
        headers=auth_headers(user),
    )

    assert response.status_code == 201
    body = response.json()
    assert body["order_item_id"] == item.id
    assert body["status"] == "pending"


@pytest.mark.asyncio
async def test_create_return_request_duplicate(
    client: AsyncClient, db: AsyncSession, make_customer, make_product_variant, auth_headers
):
    user, _ = await make_customer()
    profile = await _get_profile(db, user)
    variant = await make_product_variant()
    order = await _make_order(db, profile.id, order_status="completed")
    item = await _make_order_item(db, order.id, variant)

    await client.post(
        "/return-requests",
        json={"order_item_id": item.id, "reason": "Wrong size"},
        headers=auth_headers(user),
    )
    response = await client.post(
        "/return-requests",
        json={"order_item_id": item.id, "reason": "Wrong size again"},
        headers=auth_headers(user),
    )

    assert response.status_code == 400


@pytest.mark.asyncio
async def test_create_return_request_item_not_owned(
    client: AsyncClient, db: AsyncSession, make_customer, make_product_variant, auth_headers
):
    owner, _ = await make_customer(email="owner3@example.com")
    other, _ = await make_customer(email="other3@example.com")
    profile = await _get_profile(db, owner)
    variant = await make_product_variant()
    order = await _make_order(db, profile.id, order_status="completed")
    item = await _make_order_item(db, order.id, variant)

    response = await client.post(
        "/return-requests",
        json={"order_item_id": item.id, "reason": "Not mine"},
        headers=auth_headers(other),
    )

    assert response.status_code == 404


# ---- Return Requests: list ----

@pytest.mark.asyncio
async def test_list_return_requests_scoped_to_customer(
    client: AsyncClient, db: AsyncSession, make_customer, make_product_variant, auth_headers
):
    user, _ = await make_customer(email="user4@example.com")
    other, _ = await make_customer(email="other4@example.com")
    profile = await _get_profile(db, user)
    other_profile = await _get_profile(db, other)
    variant = await make_product_variant()

    order = await _make_order(db, profile.id, order_status="completed")
    item = await _make_order_item(db, order.id, variant)
    other_order = await _make_order(db, other_profile.id, order_status="completed")
    other_item = await _make_order_item(db, other_order.id, variant)

    await client.post("/return-requests", json={"order_item_id": item.id}, headers=auth_headers(user))
    await client.post("/return-requests", json={"order_item_id": other_item.id}, headers=auth_headers(other))

    response = await client.get("/return-requests", headers=auth_headers(user))

    assert response.status_code == 200
    body = response.json()
    assert len(body) == 1
    assert body[0]["order_item_id"] == item.id


# ---- Return Requests: status update (staff-only) ----

@pytest.mark.asyncio
async def test_update_return_request_status_as_staff(
    client: AsyncClient, db: AsyncSession, make_customer, make_staff, make_product_variant, auth_headers
):
    user, _ = await make_customer(email="user5@example.com")
    staff, _ = await make_staff()
    profile = await _get_profile(db, user)
    variant = await make_product_variant()
    order = await _make_order(db, profile.id, order_status="completed")
    item = await _make_order_item(db, order.id, variant)

    create_resp = await client.post(
        "/return-requests", json={"order_item_id": item.id}, headers=auth_headers(user)
    )
    request_id = create_resp.json()["id"]

    response = await client.patch(
        f"/return-requests/{request_id}/status",
        json={"status": "approved", "refund_amount": 20.00},
        headers=auth_headers(staff),
    )

    assert response.status_code == 200
    body = response.json()
    assert body["status"] == "approved"
    assert body["refund_amount"] == 20.00
    assert body["processed_at"] is not None


@pytest.mark.asyncio
async def test_update_return_request_status_as_customer_forbidden(
    client: AsyncClient, db: AsyncSession, make_customer, make_product_variant, auth_headers
):
    user, _ = await make_customer(email="user6@example.com")
    profile = await _get_profile(db, user)
    variant = await make_product_variant()
    order = await _make_order(db, profile.id, order_status="completed")
    item = await _make_order_item(db, order.id, variant)

    create_resp = await client.post(
        "/return-requests", json={"order_item_id": item.id}, headers=auth_headers(user)
    )
    request_id = create_resp.json()["id"]

    response = await client.patch(
        f"/return-requests/{request_id}/status",
        json={"status": "approved"},
        headers=auth_headers(user),
    )

    assert response.status_code == 403


@pytest.mark.asyncio
async def test_update_return_request_status_not_found(client: AsyncClient, make_staff, auth_headers):
    staff, _ = await make_staff()

    response = await client.patch(
        "/return-requests/999999/status",
        json={"status": "approved"},
        headers=auth_headers(staff),
    )

    assert response.status_code == 404
````

## File: backend/tests/test_customer_profiles.py
````python
import pytest

pytestmark = pytest.mark.asyncio


async def test_get_profile_success(client, make_customer, auth_headers):
    user, _ = await make_customer(email="profileget@example.com")
    headers = auth_headers(user)

    resp = await client.get("/me", headers=headers)
    assert resp.status_code == 200
    body = resp.json()
    assert body["email"] == "profileget@example.com"
    assert body["id"] == user.id


async def test_get_profile_unauthenticated(client):
    resp = await client.get("/me")
    assert resp.status_code == 401


async def test_get_profile_invalid_token(client):
    resp = await client.get("/me", headers={"Authorization": "Bearer not-a-real-token"})
    assert resp.status_code == 401


async def test_update_profile_success(client, make_customer, auth_headers):
    user, _ = await make_customer(email="profileupdate@example.com")
    headers = auth_headers(user)

    resp = await client.put("/me", json={"name": "Updated Name"}, headers=headers)
    assert resp.status_code == 200
    body = resp.json()
    assert body["name"] == "Updated Name"


async def test_update_profile_partial_fields_unchanged(client, make_customer, auth_headers):
    user, _ = await make_customer(email="profilepartial@example.com")
    headers = auth_headers(user)

    resp = await client.put("/me", json={"phone_number": "+19998887777"}, headers=headers)
    assert resp.status_code == 200
    body = resp.json()
    assert body["phone_number"] == "+19998887777"
    assert body["name"] == "Test Customer"


async def test_update_profile_unauthenticated(client):
    resp = await client.put("/me", json={"name": "Nope"})
    assert resp.status_code == 401


async def test_list_addresses_empty(client, make_customer, auth_headers):
    user, _ = await make_customer(email="addrlistempty@example.com")
    headers = auth_headers(user)

    resp = await client.get("/addresses", headers=headers)
    assert resp.status_code == 200
    assert resp.json() == []


async def test_create_address_success(client, make_customer, auth_headers):
    user, _ = await make_customer(email="addrcreate@example.com")
    headers = auth_headers(user)

    payload = {
        "country": "USA",
        "state": "CA",
        "city": "Los Angeles",
        "postal_code": "90001",
        "address_line_1": "123 Main St",
        "address_line_2": None,
        "is_default": True,
    }
    resp = await client.post("/addresses", json=payload, headers=headers)
    assert resp.status_code == 201
    body = resp.json()
    assert body["city"] == "Los Angeles"
    assert body["is_default"] is True


async def test_create_address_unauthenticated(client):
    payload = {
        "country": "USA",
        "city": "Los Angeles",
        "address_line_1": "123 Main St",
    }
    resp = await client.post("/addresses", json=payload)
    assert resp.status_code == 401


async def test_create_second_default_address_unsets_first(client, make_customer, auth_headers):
    user, _ = await make_customer(email="addrdefault@example.com")
    headers = auth_headers(user)

    first_payload = {
        "country": "USA",
        "city": "Austin",
        "address_line_1": "1 First St",
        "is_default": True,
    }
    first_resp = await client.post("/addresses", json=first_payload, headers=headers)
    assert first_resp.status_code == 201
    first_id = first_resp.json()["id"]

    second_payload = {
        "country": "USA",
        "city": "Dallas",
        "address_line_1": "2 Second St",
        "is_default": True,
    }
    second_resp = await client.post("/addresses", json=second_payload, headers=headers)
    assert second_resp.status_code == 201

    list_resp = await client.get("/addresses", headers=headers)
    addresses = {a["id"]: a["is_default"] for a in list_resp.json()}
    assert addresses[first_id] is False


async def test_update_address_success(client, make_customer, auth_headers):
    user, _ = await make_customer(email="addrupdate@example.com")
    headers = auth_headers(user)

    create_payload = {
        "country": "USA",
        "city": "Denver",
        "address_line_1": "1 Old St",
    }
    create_resp = await client.post("/addresses", json=create_payload, headers=headers)
    address_id = create_resp.json()["id"]

    update_resp = await client.put(
        f"/addresses/{address_id}", json={"city": "Boulder"}, headers=headers
    )
    assert update_resp.status_code == 200
    assert update_resp.json()["city"] == "Boulder"


async def test_update_address_not_found(client, make_customer, auth_headers):
    user, _ = await make_customer(email="addrupdatenotfound@example.com")
    headers = auth_headers(user)

    resp = await client.put("/addresses/999999", json={"city": "Nowhere"}, headers=headers)
    assert resp.status_code == 404


async def test_update_address_belonging_to_another_customer(client, make_customer, auth_headers):
    owner, _ = await make_customer(email="addrowner@example.com")
    intruder, _ = await make_customer(email="addrintruder@example.com")

    create_resp = await client.post(
        "/addresses",
        json={"country": "USA", "city": "Miami", "address_line_1": "1 Owner St"},
        headers=auth_headers(owner),
    )
    address_id = create_resp.json()["id"]

    resp = await client.put(
        f"/addresses/{address_id}",
        json={"city": "Hacked"},
        headers=auth_headers(intruder),
    )
    assert resp.status_code == 404


async def test_update_address_set_default_unsets_others(client, make_customer, auth_headers):
    user, _ = await make_customer(email="addrupdatedefault@example.com")
    headers = auth_headers(user)

    first_resp = await client.post(
        "/addresses",
        json={"country": "USA", "city": "Seattle", "address_line_1": "1 A St", "is_default": True},
        headers=headers,
    )
    first_id = first_resp.json()["id"]

    second_resp = await client.post(
        "/addresses",
        json={"country": "USA", "city": "Portland", "address_line_1": "2 B St", "is_default": False},
        headers=headers,
    )
    second_id = second_resp.json()["id"]

    await client.put(f"/addresses/{second_id}", json={"is_default": True}, headers=headers)

    list_resp = await client.get("/addresses", headers=headers)
    addresses = {a["id"]: a["is_default"] for a in list_resp.json()}
    assert addresses[first_id] is False
    assert addresses[second_id] is True


async def test_delete_address_success(client, make_customer, auth_headers):
    user, _ = await make_customer(email="addrdelete@example.com")
    headers = auth_headers(user)

    create_resp = await client.post(
        "/addresses",
        json={"country": "USA", "city": "Phoenix", "address_line_1": "1 Delete St"},
        headers=headers,
    )
    address_id = create_resp.json()["id"]

    delete_resp = await client.delete(f"/addresses/{address_id}", headers=headers)
    assert delete_resp.status_code == 204

    list_resp = await client.get("/addresses", headers=headers)
    assert all(a["id"] != address_id for a in list_resp.json())


async def test_delete_address_not_found(client, make_customer, auth_headers):
    user, _ = await make_customer(email="addrdeletenotfound@example.com")
    headers = auth_headers(user)

    resp = await client.delete("/addresses/999999", headers=headers)
    assert resp.status_code == 404


async def test_delete_address_belonging_to_another_customer(client, make_customer, auth_headers):
    owner, _ = await make_customer(email="addrdelowner@example.com")
    intruder, _ = await make_customer(email="addrdelintruder@example.com")

    create_resp = await client.post(
        "/addresses",
        json={"country": "USA", "city": "Tampa", "address_line_1": "1 Owner Ave"},
        headers=auth_headers(owner),
    )
    address_id = create_resp.json()["id"]

    resp = await client.delete(f"/addresses/{address_id}", headers=auth_headers(intruder))
    assert resp.status_code == 404
````

## File: backend/tests/test_payments.py
````python
import json
import pytest
import stripe
from sqlalchemy import select

from app.models.customer_profile import CustomerProfile

pytestmark = pytest.mark.asyncio


class FakePaymentIntent:
    def __init__(self, client_secret="pi_test_secret_123"):
        self.client_secret = client_secret


async def test_create_intent_success(client, make_customer, auth_headers, make_product_variant, make_cart_with_item, db, monkeypatch):
    user, _ = await make_customer(email="paycreateintent@example.com")
    headers = auth_headers(user)

    result = await db.execute(select(CustomerProfile).where(CustomerProfile.user_id == user.id))
    profile = result.scalar_one()

    variant = await make_product_variant(price=20.00, stock_quantity=10)
    await make_cart_with_item(profile.id, variant, quantity=3)

    captured = {}

    def fake_create(**kwargs):
        captured.update(kwargs)
        return FakePaymentIntent()

    monkeypatch.setattr(stripe.PaymentIntent, "create", fake_create)

    resp = await client.post("/payments/create-intent", headers=headers)
    assert resp.status_code == 200
    assert resp.json()["client_secret"] == "pi_test_secret_123"
    assert captured["amount"] == 6000
    assert captured["currency"] == "usd"


async def test_create_intent_empty_cart(client, make_customer, auth_headers, monkeypatch):
    user, _ = await make_customer(email="paynocart@example.com")
    headers = auth_headers(user)

    monkeypatch.setattr(stripe.PaymentIntent, "create", lambda **kwargs: FakePaymentIntent())

    resp = await client.post("/payments/create-intent", headers=headers)
    assert resp.status_code == 400
    assert resp.json()["detail"] == "Cart is empty"


async def test_create_intent_insufficient_stock(client, make_customer, auth_headers, make_product_variant, make_cart_with_item, db, monkeypatch):
    user, _ = await make_customer(email="payinsufficientstock@example.com")
    headers = auth_headers(user)

    result = await db.execute(select(CustomerProfile).where(CustomerProfile.user_id == user.id))
    profile = result.scalar_one()

    variant = await make_product_variant(price=10.00, stock_quantity=1)
    await make_cart_with_item(profile.id, variant, quantity=5)

    monkeypatch.setattr(stripe.PaymentIntent, "create", lambda **kwargs: FakePaymentIntent())

    resp = await client.post("/payments/create-intent", headers=headers)
    assert resp.status_code == 400
    assert "Insufficient stock" in resp.json()["detail"]


async def test_create_intent_inactive_variant(client, make_customer, auth_headers, make_product_variant, make_cart_with_item, db, monkeypatch):
    user, _ = await make_customer(email="payinactivevariant@example.com")
    headers = auth_headers(user)

    result = await db.execute(select(CustomerProfile).where(CustomerProfile.user_id == user.id))
    profile = result.scalar_one()

    variant = await make_product_variant(price=10.00, stock_quantity=10, is_active=False)
    await make_cart_with_item(profile.id, variant, quantity=1)

    monkeypatch.setattr(stripe.PaymentIntent, "create", lambda **kwargs: FakePaymentIntent())

    resp = await client.post("/payments/create-intent", headers=headers)
    assert resp.status_code == 400
    assert "no longer available" in resp.json()["detail"]


async def test_create_intent_unauthenticated(client, monkeypatch):
    monkeypatch.setattr(stripe.PaymentIntent, "create", lambda **kwargs: FakePaymentIntent())
    resp = await client.post("/payments/create-intent")
    assert resp.status_code == 401


async def test_webhook_invalid_payload(client, monkeypatch):
    def fake_construct_event(payload, sig_header, secret):
        raise ValueError("bad payload")

    monkeypatch.setattr(stripe.Webhook, "construct_event", fake_construct_event)

    resp = await client.post(
        "/payments/webhook",
        content=b"not-real-json",
        headers={"stripe-signature": "fake-sig"},
    )
    assert resp.status_code == 400
    assert resp.json()["detail"] == "Invalid payload"


async def test_webhook_invalid_signature(client, monkeypatch):
    def fake_construct_event(payload, sig_header, secret):
        raise stripe.error.SignatureVerificationError("bad sig", sig_header)

    monkeypatch.setattr(stripe.Webhook, "construct_event", fake_construct_event)

    resp = await client.post(
        "/payments/webhook",
        content=b"{}",
        headers={"stripe-signature": "fake-sig"},
    )
    assert resp.status_code == 400
    assert resp.json()["detail"] == "Invalid signature"


async def test_webhook_payment_succeeded_creates_order(client, make_customer, make_product_variant, make_cart_with_item, db, monkeypatch):
    user, _ = await make_customer(email="paywebhooksuccess@example.com")

    result = await db.execute(select(CustomerProfile).where(CustomerProfile.user_id == user.id))
    profile = result.scalar_one()

    variant = await make_product_variant(price=30.00, stock_quantity=10)
    cart = await make_cart_with_item(profile.id, variant, quantity=2)

    fake_event = {
        "type": "payment_intent.succeeded",
        "data": {
            "object": {
                "metadata": {
                    "cart_id": str(cart.id),
                    "customer_id": str(profile.id),
                }
            }
        },
    }

    def fake_construct_event(payload, sig_header, secret):
        return fake_event

    monkeypatch.setattr(stripe.Webhook, "construct_event", fake_construct_event)

    resp = await client.post(
        "/payments/webhook",
        content=b"{}",
        headers={"stripe-signature": "fake-sig"},
    )
    assert resp.status_code == 200
    assert resp.json()["status"] == "success"

    from app.models.order import Order
    order_result = await db.execute(select(Order).where(Order.customer_id == profile.id))
    order = order_result.scalar_one_or_none()
    assert order is not None
    assert order.status == "paid"
    assert order.total_amount == 60.0

    await db.refresh(variant)
    assert variant.stock_quantity == 8


async def test_webhook_ignores_other_event_types(client, make_customer, make_product_variant, make_cart_with_item, db, monkeypatch):
    user, _ = await make_customer(email="paywebhookother@example.com")

    result = await db.execute(select(CustomerProfile).where(CustomerProfile.user_id == user.id))
    profile = result.scalar_one()

    variant = await make_product_variant(price=15.00, stock_quantity=10)
    cart = await make_cart_with_item(profile.id, variant, quantity=1)

    fake_event = {
        "type": "payment_intent.payment_failed",
        "data": {
            "object": {
                "metadata": {
                    "cart_id": str(cart.id),
                    "customer_id": str(profile.id),
                }
            }
        },
    }

    monkeypatch.setattr(stripe.Webhook, "construct_event", lambda payload, sig_header, secret: fake_event)

    resp = await client.post(
        "/payments/webhook",
        content=b"{}",
        headers={"stripe-signature": "fake-sig"},
    )
    assert resp.status_code == 200

    from app.models.order import Order
    order_result = await db.execute(select(Order).where(Order.customer_id == profile.id))
    assert order_result.scalar_one_or_none() is None

    await db.refresh(variant)
    assert variant.stock_quantity == 10


async def test_webhook_missing_metadata_no_crash(client, monkeypatch):
    fake_event = {
        "type": "payment_intent.succeeded",
        "data": {"object": {"metadata": {}}},
    }
    monkeypatch.setattr(stripe.Webhook, "construct_event", lambda payload, sig_header, secret: fake_event)

    resp = await client.post(
        "/payments/webhook",
        content=b"{}",
        headers={"stripe-signature": "fake-sig"},
    )
    assert resp.status_code == 200


async def test_webhook_retry_does_not_duplicate_order(client, make_customer, make_product_variant, make_cart_with_item, db, monkeypatch):
    user, _ = await make_customer(email="paywebhookretry@example.com")

    result = await db.execute(select(CustomerProfile).where(CustomerProfile.user_id == user.id))
    profile = result.scalar_one()
    profile_id = profile.id

    variant = await make_product_variant(price=10.00, stock_quantity=10)
    cart = await make_cart_with_item(profile.id, variant, quantity=1)

    fake_event = {
        "type": "payment_intent.succeeded",
        "data": {
            "object": {
                "metadata": {
                    "cart_id": str(cart.id),
                    "customer_id": str(profile_id),
                }
            }
        },
    }
    monkeypatch.setattr(stripe.Webhook, "construct_event", lambda payload, sig_header, secret: fake_event)

    first_resp = await client.post(
        "/payments/webhook", content=b"{}", headers={"stripe-signature": "fake-sig"}
    )
    assert first_resp.status_code == 200

    await db.refresh(profile)

    second_resp = await client.post(
        "/payments/webhook", content=b"{}", headers={"stripe-signature": "fake-sig"}
    )
    assert second_resp.status_code == 200

    from app.models.order import Order
    order_result = await db.execute(select(Order).where(Order.customer_id == profile_id))
    orders = order_result.scalars().all()
    assert len(orders) == 1
````

## File: backend/tests/test_reviews.py
````python
import pytest
from sqlalchemy import select

from app.models.customer_profile import CustomerProfile

pytestmark = pytest.mark.asyncio


async def test_get_product_reviews_empty(client, make_product_variant):
    variant = await make_product_variant()
    resp = await client.get(f"/products/{variant.product_id}/reviews")
    assert resp.status_code == 200
    assert resp.json() == []


async def test_get_product_reviews_product_not_found(client):
    resp = await client.get("/products/999999/reviews")
    assert resp.status_code == 404
    assert resp.json()["detail"] == "Product not found"


async def test_create_review_success(client, make_customer, auth_headers, make_order_item, db):
    user, _ = await make_customer(email="reviewcreate@example.com")
    headers = auth_headers(user)

    result = await db.execute(select(CustomerProfile).where(CustomerProfile.user_id == user.id))
    profile = result.scalar_one()

    order_item, product_id = await make_order_item(profile.id)

    payload = {"order_item_id": order_item.id, "rating": 5, "comment": "Great product"}
    resp = await client.post(f"/products/{product_id}/reviews", json=payload, headers=headers)
    assert resp.status_code == 201
    body = resp.json()
    assert body["rating"] == 5
    assert body["comment"] == "Great product"
    assert body["product_id"] == product_id


async def test_create_review_product_not_found(client, make_customer, auth_headers, make_order_item, db):
    user, _ = await make_customer(email="reviewproductnotfound@example.com")
    headers = auth_headers(user)

    result = await db.execute(select(CustomerProfile).where(CustomerProfile.user_id == user.id))
    profile = result.scalar_one()

    order_item, _ = await make_order_item(profile.id)

    payload = {"order_item_id": order_item.id, "rating": 4}
    resp = await client.post("/products/999999/reviews", json=payload, headers=headers)
    assert resp.status_code == 404
    assert resp.json()["detail"] == "Product not found"


async def test_create_review_order_item_not_found(client, make_customer, auth_headers, make_product_variant):
    user, _ = await make_customer(email="reviewitemnotfound@example.com")
    headers = auth_headers(user)

    variant = await make_product_variant()

    payload = {"order_item_id": 999999, "rating": 3}
    resp = await client.post(f"/products/{variant.product_id}/reviews", json=payload, headers=headers)
    assert resp.status_code == 404
    assert resp.json()["detail"] == "Order item not found"


async def test_create_review_invalid_rating(client, make_customer, auth_headers, make_order_item, db):
    user, _ = await make_customer(email="reviewinvalidrating@example.com")
    headers = auth_headers(user)

    result = await db.execute(select(CustomerProfile).where(CustomerProfile.user_id == user.id))
    profile = result.scalar_one()

    order_item, product_id = await make_order_item(profile.id)

    payload = {"order_item_id": order_item.id, "rating": 6}
    resp = await client.post(f"/products/{product_id}/reviews", json=payload, headers=headers)
    assert resp.status_code == 422


async def test_create_review_unauthenticated(client, make_product_variant):
    variant = await make_product_variant()
    payload = {"order_item_id": 1, "rating": 5}
    resp = await client.post(f"/products/{variant.product_id}/reviews", json=payload)
    assert resp.status_code == 401


async def test_get_product_reviews_after_creation(client, make_customer, auth_headers, make_order_item, db):
    user, _ = await make_customer(email="reviewlistafter@example.com")
    headers = auth_headers(user)

    result = await db.execute(select(CustomerProfile).where(CustomerProfile.user_id == user.id))
    profile = result.scalar_one()

    order_item, product_id = await make_order_item(profile.id)

    await client.post(
        f"/products/{product_id}/reviews",
        json={"order_item_id": order_item.id, "rating": 4, "comment": "Nice"},
        headers=headers,
    )

    resp = await client.get(f"/products/{product_id}/reviews")
    assert resp.status_code == 200
    body = resp.json()
    assert len(body) == 1
    assert body[0]["rating"] == 4


async def test_update_review_success(client, make_customer, auth_headers, make_order_item, db):
    user, _ = await make_customer(email="reviewupdate@example.com")
    headers = auth_headers(user)

    result = await db.execute(select(CustomerProfile).where(CustomerProfile.user_id == user.id))
    profile = result.scalar_one()

    order_item, product_id = await make_order_item(profile.id)

    create_resp = await client.post(
        f"/products/{product_id}/reviews",
        json={"order_item_id": order_item.id, "rating": 2, "comment": "Meh"},
        headers=headers,
    )
    review_id = create_resp.json()["id"]

    update_resp = await client.put(
        f"/reviews/{review_id}", json={"rating": 5, "comment": "Actually great"}, headers=headers
    )
    assert update_resp.status_code == 200
    body = update_resp.json()
    assert body["rating"] == 5
    assert body["comment"] == "Actually great"


async def test_update_review_not_found(client, make_customer, auth_headers):
    user, _ = await make_customer(email="reviewupdatenotfound@example.com")
    headers = auth_headers(user)

    resp = await client.put("/reviews/999999", json={"rating": 3}, headers=headers)
    assert resp.status_code == 404
    assert resp.json()["detail"] == "Review not found"


async def test_update_review_belonging_to_another_customer(client, make_customer, auth_headers, make_order_item, db):
    owner, _ = await make_customer(email="reviewowner@example.com")
    intruder, _ = await make_customer(email="reviewintruder@example.com")

    result = await db.execute(select(CustomerProfile).where(CustomerProfile.user_id == owner.id))
    owner_profile = result.scalar_one()

    order_item, product_id = await make_order_item(owner_profile.id)

    create_resp = await client.post(
        f"/products/{product_id}/reviews",
        json={"order_item_id": order_item.id, "rating": 5},
        headers=auth_headers(owner),
    )
    review_id = create_resp.json()["id"]

    resp = await client.put(
        f"/reviews/{review_id}", json={"rating": 1}, headers=auth_headers(intruder)
    )
    assert resp.status_code == 403
    assert resp.json()["detail"] == "You can only edit your own reviews"


async def test_update_review_unauthenticated(client, make_customer, make_order_item, db):
    user, _ = await make_customer(email="reviewupdateunauth@example.com")
    result = await db.execute(select(CustomerProfile).where(CustomerProfile.user_id == user.id))
    profile = result.scalar_one()
    order_item, product_id = await make_order_item(profile.id)

    resp = await client.put("/reviews/1", json={"rating": 3})
    assert resp.status_code == 401


async def test_delete_review_success(client, make_customer, auth_headers, make_order_item, db):
    user, _ = await make_customer(email="reviewdelete@example.com")
    headers = auth_headers(user)

    result = await db.execute(select(CustomerProfile).where(CustomerProfile.user_id == user.id))
    profile = result.scalar_one()

    order_item, product_id = await make_order_item(profile.id)

    create_resp = await client.post(
        f"/products/{product_id}/reviews",
        json={"order_item_id": order_item.id, "rating": 3},
        headers=headers,
    )
    review_id = create_resp.json()["id"]

    delete_resp = await client.delete(f"/reviews/{review_id}", headers=headers)
    assert delete_resp.status_code == 204

    list_resp = await client.get(f"/products/{product_id}/reviews")
    assert all(r["id"] != review_id for r in list_resp.json())


async def test_delete_review_not_found(client, make_customer, auth_headers):
    user, _ = await make_customer(email="reviewdeletenotfound@example.com")
    headers = auth_headers(user)

    resp = await client.delete("/reviews/999999", headers=headers)
    assert resp.status_code == 404
    assert resp.json()["detail"] == "Review not found"


async def test_delete_review_belonging_to_another_customer(client, make_customer, auth_headers, make_order_item, db):
    owner, _ = await make_customer(email="reviewdelowner@example.com")
    intruder, _ = await make_customer(email="reviewdelintruder@example.com")

    result = await db.execute(select(CustomerProfile).where(CustomerProfile.user_id == owner.id))
    owner_profile = result.scalar_one()

    order_item, product_id = await make_order_item(owner_profile.id)

    create_resp = await client.post(
        f"/products/{product_id}/reviews",
        json={"order_item_id": order_item.id, "rating": 4},
        headers=auth_headers(owner),
    )
    review_id = create_resp.json()["id"]

    resp = await client.delete(f"/reviews/{review_id}", headers=auth_headers(intruder))
    assert resp.status_code == 403
    assert resp.json()["detail"] == "You can only delete your own reviews"
````

## File: backend/tests/test_wishlist.py
````python
import pytest
from sqlalchemy import select

from app.models.product import Product

pytestmark = pytest.mark.asyncio


async def _make_product(db, name="Test Product"):
    product = Product(name=name, description="test", price=10.0)
    db.add(product)
    await db.commit()
    await db.refresh(product)
    return product


async def test_get_wishlist_empty(client, make_customer, auth_headers):
    user, _ = await make_customer(email="wishlistempty@example.com")
    headers = auth_headers(user)

    resp = await client.get("/wishlist", headers=headers)
    assert resp.status_code == 200
    assert resp.json() == []


async def test_add_to_wishlist_success(client, make_customer, auth_headers, db):
    user, _ = await make_customer(email="wishlistadd@example.com")
    headers = auth_headers(user)
    product = await _make_product(db)

    resp = await client.post(
        "/wishlist",
        json={"product_id": product.id},
        headers=headers,
    )
    assert resp.status_code == 201
    body = resp.json()
    assert body["product_id"] == product.id


async def test_add_to_wishlist_product_not_found(client, make_customer, auth_headers):
    user, _ = await make_customer(email="wishlistnotfound@example.com")
    headers = auth_headers(user)

    resp = await client.post(
        "/wishlist",
        json={"product_id": 999999},
        headers=headers,
    )
    assert resp.status_code == 404
    assert resp.json()["detail"] == "Product not found"


async def test_add_to_wishlist_duplicate(client, make_customer, auth_headers, db):
    user, _ = await make_customer(email="wishlistdup@example.com")
    headers = auth_headers(user)
    product = await _make_product(db)

    await client.post("/wishlist", json={"product_id": product.id}, headers=headers)
    resp = await client.post("/wishlist", json={"product_id": product.id}, headers=headers)

    assert resp.status_code == 400
    assert resp.json()["detail"] == "Product already in wishlist"


async def test_remove_from_wishlist_success(client, make_customer, auth_headers, db):
    user, _ = await make_customer(email="wishlistremove@example.com")
    headers = auth_headers(user)
    product = await _make_product(db)

    await client.post("/wishlist", json={"product_id": product.id}, headers=headers)
    resp = await client.delete(f"/wishlist/{product.id}", headers=headers)

    assert resp.status_code == 204


async def test_remove_from_wishlist_not_found(client, make_customer, auth_headers):
    user, _ = await make_customer(email="wishlistremovenf@example.com")
    headers = auth_headers(user)

    resp = await client.delete("/wishlist/999999", headers=headers)
    assert resp.status_code == 404
    assert resp.json()["detail"] == "Product not found in wishlist"
````

## File: backend/.dockerignore
````
__pycache__/
*.pyc
.venv/
venv/
.env
alembic/versions/__pycache__/
*.rar
*.zip
````

## File: backend/Dockerfile
````
FROM python:3.12-slim

WORKDIR /app

# System deps needed for psycopg2 / postgres client libs
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
````

## File: backend/pytest.ini
````ini
[pytest]
asyncio_mode = auto
testpaths = tests
````

## File: backend/requirements-dev.txt
````
aiosqlite==0.22.1
alembic==1.18.5
annotated-doc==0.0.4
annotated-types==0.7.0
anyio==4.14.1
asyncpg==0.31.0
bcrypt==5.0.0
certifi==2026.7.22
cffi==2.0.0
charset-normalizer==3.4.9
click==8.4.2
colorama==0.4.6
coverage==7.15.2
cryptography==49.0.0
dnspython==2.8.0
ecdsa==0.19.2
email-validator==2.3.0
Faker==40.35.0
fastapi==0.139.0
greenlet==3.5.3
h11==0.16.0
httpcore==1.0.9
httpx==0.28.1
idna==3.18
iniconfig==2.3.0
Mako==1.3.12
MarkupSafe==3.0.3
packaging==26.2
pluggy==1.6.0
psycopg==3.3.4
psycopg-binary==3.3.4
pyasn1==0.6.3
pycparser==3.0
pydantic==2.13.4
pydantic-settings==2.14.2
pydantic_core==2.46.4
Pygments==2.20.0
pytest==9.1.1
pytest-asyncio==1.4.0
pytest-cov==7.1.0
python-dotenv==1.2.2
python-jose==3.5.0
requests==2.34.2
rsa==4.9.1
six==1.17.0
SQLAlchemy==2.0.51
starlette==1.3.1
stripe==15.3.1
typing-inspection==0.4.2
typing_extensions==4.16.0
tzdata==2026.2
urllib3==2.7.0
uvicorn==0.49.0
````

## File: frontend/.claude/rules/guardrails.md
````markdown
---
globs: "*"
---

# Core Project Configuration & Architecture

## Tech Stack

- Frontend Framework: Next.js (App Router, Version 15+)
- Language: TypeScript (Strict Type Checking)
- Styling: Tailwind CSS (Utility-first configuration)
- State Management: Zustand (Global Client-Side Stores)
- Form Handling: React Hook Form
- Validation: Zod (Schema validation for forms and API responses)
- Payments: Stripe (@stripe/stripe-js and @stripe/react-stripe-js)
- Backend: External FastAPI Backend Engine

## Folder Layout Structure

- `/app`: Pages, layouts, and route handlers.
- `/components`: Reusable global UI elements (buttons, inputs, modals).
- `/lib`: Modular code utilities.
- `/lib/api`: HTTP and WebSocket connection clients for FastAPI.
- `/lib/stores`: Zustand global state store modules.
- `/hooks`: Custom stateful React hooks.
- `/types`: Explicit TypeScript data interfaces and types.
- `/tests`: Unit, integration, and End-to-End test suites.

## Strict Production Guardrails

1. NO PLACEHOLDERS: Never output placeholders, partial modifications, or comments like `// TODO: Implement logic` or `// ... rest of code here`. Write out every file completely.
2. NO PROSE IN GENERATION: When acting as a code generator, skip conversational pleasantries, introductory text, and closing summaries. Output only the file path indicator followed by the raw code block.
3. ERROR HANDLING: Every API network operation and state transaction must be wrapped inside defensive `try/catch` processing blocks with strict user-facing fallback messages.
4. TYPE SAFETY: Avoid the use of `any` types. Every utility parameter, API response payload, and form state must be strictly declared with a definitive TypeScript interface or type.
5. BEST PRACTICES: Always follow elite, production-grade software engineering practices. Avoid quick fixes, lazy shortcuts, and architectural hacks. Write clean, modular, and highly scalable logic.
6. COMPREHENSIVE GUIDANCE: Do not give vague or high-level instructions. Instead of stating "make changes" or "write tests," explicitly guide step by step on how to execute those changes and write out the exact, actionable code blocks or testing logic required.
````

## File: frontend/.github/copilot-instructions.md
````markdown
---
globs: "*"
---

# Core Project Configuration & Architecture

## Tech Stack

- Frontend Framework: Next.js (App Router, Version 15+)
- Language: TypeScript (Strict Type Checking)
- Styling: Tailwind CSS (Utility-first configuration)
- State Management: Zustand (Global Client-Side Stores)
- Form Handling: React Hook Form
- Validation: Zod (Schema validation for forms and API responses)
- Payments: Stripe (@stripe/stripe-js and @stripe/react-stripe-js)
- Backend: External FastAPI Backend Engine

## Folder Layout Structure

- `/app`: Pages, layouts, and route handlers.
- `/components`: Reusable global UI elements (buttons, inputs, modals).
- `/lib`: Modular code utilities.
- `/lib/api`: HTTP and WebSocket connection clients for FastAPI.
- `/lib/stores`: Zustand global state store modules.
- `/hooks`: Custom stateful React hooks.
- `/types`: Explicit TypeScript data interfaces and types.
- `/tests`: Unit, integration, and End-to-End test suites.

## Strict Production Guardrails

1. NO PLACEHOLDERS: Never output placeholders, partial modifications, or comments like `// TODO: Implement logic` or `// ... rest of code here`. Write out every file completely.
2. NO PROSE IN GENERATION: When acting as a code generator, skip conversational pleasantries, introductory text, and closing summaries. Output only the file path indicator followed by the raw code block.
3. ERROR HANDLING: Every API network operation and state transaction must be wrapped inside defensive `try/catch` processing blocks with strict user-facing fallback messages.
4. TYPE SAFETY: Avoid the use of `any` types. Every utility parameter, API response payload, and form state must be strictly declared with a definitive TypeScript interface or type.
5. BEST PRACTICES: Always follow elite, production-grade software engineering practices. Avoid quick fixes, lazy shortcuts, and architectural hacks. Write clean, modular, and highly scalable logic.
6. COMPREHENSIVE GUIDANCE: Do not give vague or high-level instructions. Instead of stating "make changes" or "write tests," explicitly guide step by step on how to execute those changes and write out the exact, actionable code blocks or testing logic required.
````

## File: frontend/app/api/auth/login/route.ts
````typescript
import { NextResponse } from "next/server";

export async function POST() {
  return NextResponse.json({ message: "Login via /customer/auth/login API" });
}
````

## File: frontend/app/api/auth/logout/route.ts
````typescript
import { NextResponse } from "next/server";
import { cookies } from "next/headers";

export async function POST() {
  try {
    const cookieStore = await cookies();
    cookieStore.delete("access_token");
    cookieStore.delete("refresh_token");
  } catch {
    // Ignore cookie store errors
  }

  const response = NextResponse.json({ message: "Logged out successfully" });
  response.cookies.set("access_token", "", { maxAge: 0, path: "/" });
  response.cookies.set("refresh_token", "", { maxAge: 0, path: "/" });
  return response;
}
````

## File: frontend/app/api/checkout/create-payment-intent/route.ts
````typescript
import { NextResponse } from "next/server";

export async function POST() {
  return NextResponse.json({ message: "Checkout endpoint stub" });
}
````

## File: frontend/app/api/webhooks/stripe/route.ts
````typescript
import { NextResponse } from "next/server";

export async function POST() {
  return NextResponse.json({ received: true });
}
````

## File: frontend/app/error.tsx
````typescript
"use client"; // Must be the absolute first line of code

import { useEffect } from "react";

export default function Error({
  error,
  reset,
}: {
  error: Error & { digest?: string };
  reset: () => void;
}) {
  useEffect(() => {
    console.error(error);
  }, [error]);

  return (
    <div className="flex min-h-screen flex-col items-center justify-center p-4 text-center">
      <h2 className="text-xl font-bold text-red-600">Something went wrong!</h2>
      <button
        onClick={() => reset()}
        className="mt-4 rounded bg-gray-900 px-4 py-2 text-sm font-medium text-white hover:bg-gray-800"
      >
        Try again
      </button>
    </div>
  );
}
````

## File: frontend/app/layout.tsx
````typescript
import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "E-Commerce Storefront",
  description: "Production e-commerce frontend built on Next.js",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body className="min-h-screen bg-white text-gray-900 antialiased">
        {children}
      </body>
    </html>
  );
}
````

## File: frontend/app/not-found.tsx
````typescript
import Link from "next/link";

export default function NotFound() {
  return (
    <div className="flex min-h-screen flex-col items-center justify-center bg-white px-4 text-center">
      <h1 className="text-6xl font-extrabold text-gray-900">404</h1>
      <h2 className="mt-4 text-xl font-bold text-gray-700">Page Not Found</h2>
      <p className="mt-2 text-base text-gray-500">
        Sorry, we couldn’t find the page you’re looking for.
      </p>
      <div className="mt-6">
        <Link
          href="/"
          className="inline-flex items-center rounded-md bg-gray-900 px-4 py-2 text-sm font-medium text-white shadow-sm hover:bg-gray-800 focus:outline-none"
        >
          Go back home
        </Link>
      </div>
    </div>
  );
}
````

## File: frontend/app/robots.ts
````typescript
import type { MetadataRoute } from "next";

// Forces Next.js to build this route as a static file during 'output: export'
export const dynamic = "force-static";

export default function robots(): MetadataRoute.Robots {
  return {
    rules: {
      userAgent: "*",
      allow: "/",
    },
  };
}
````

## File: frontend/app/sitemap.ts
````typescript
import type { MetadataRoute } from "next";

// Forces Next.js to build this route as a static file during 'output: export'
export const dynamic = "force-static";

export default function sitemap(): MetadataRoute.Sitemap {
  return [
    {
      url: "https://localhost:3000",
      lastModified: new Date(),
    },
  ];
}
````

## File: frontend/e2e/auth.spec.ts
````typescript

````

## File: frontend/e2e/checkout.spec.ts
````typescript

````

## File: frontend/e2e/phase1-checkpoint.spec.ts
````typescript

````

## File: frontend/hooks/useDebouncedValue.ts
````typescript

````

## File: frontend/hooks/useOrderStatusPolling.ts
````typescript

````

## File: frontend/hooks/useWebSocket.ts
````typescript

````

## File: frontend/lib/api/notifications.ts
````typescript

````

## File: frontend/lib/api/reviews.ts
````typescript

````

## File: frontend/lib/api/wishlist.ts
````typescript

````

## File: frontend/lib/stores/cartStore.ts
````typescript

````

## File: frontend/lib/stores/checkoutStore.ts
````typescript

````

## File: frontend/lib/stores/notificationStore.ts
````typescript

````

## File: frontend/lib/stores/wishlistStore.ts
````typescript

````

## File: frontend/lib/stripe/client.ts
````typescript

````

## File: frontend/lib/stripe/paymentIntent.ts
````typescript

````

## File: frontend/lib/utils/format.ts
````typescript

````

## File: frontend/lib/validation/contact.ts
````typescript

````

## File: frontend/lib/validation/review.ts
````typescript

````

## File: frontend/lib/websocket/chatConnection.ts
````typescript

````

## File: frontend/lib/websocket/connectionManager.ts
````typescript

````

## File: frontend/types/auth.ts
````typescript

````

## File: frontend/types/cart.ts
````typescript

````

## File: frontend/types/category.ts
````typescript

````

## File: frontend/types/chats.ts
````typescript

````

## File: frontend/types/notification.ts
````typescript

````

## File: frontend/types/review.ts
````typescript

````

## File: frontend/types/role.ts
````typescript

````

## File: frontend/types/wishlist.ts
````typescript

````

## File: frontend/.env.example
````
NEXT_PUBLIC_API_URL=https://api.example.com
NEXT_PUBLIC_WS_URL=wss://ws.example.com
NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY=pk_test_replace_me
````

## File: frontend/.prettierrc
````
{
  "semi": true,
  "singleQuote": false,
  "trailingComma": "es5",
  "tabWidth": 2,
  "printWidth": 100
}
````

## File: frontend/eslint.config.mjs
````javascript
import { FlatCompat } from "@eslint/eslintrc";
import { dirname } from "path";
import { fileURLToPath } from "url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

const compat = new FlatCompat({
  baseDirectory: __dirname,
});

const eslintConfig = [...compat.extends("next/core-web-vitals", "next/typescript")];

export default eslintConfig;
````

## File: frontend/gitignore
````
node_modules
.next
.env.local
*.log
````

## File: frontend/jest.config.ts
````typescript
import type { Config } from "jest";

const config: Config = {
  preset: "ts-jest",
  testEnvironment: "jsdom",
  setupFilesAfterEnv: ["<rootDir>/jest.setup.ts"],
  moduleNameMapper: {
    "^@/(.*)$": "<rootDir>/$1",
    "\\.(css|less|scss|sass)$": "identity-obj-proxy",
  },
  transform: {
    "^.+\\.(ts|tsx)$": ["ts-jest", { tsconfig: "tsconfig.jest.json" }],
  },
  testPathIgnorePatterns: ["/node_modules/", "/e2e/"],
};

export default config;
````

## File: frontend/jest.setup.ts
````typescript
import "@testing-library/jest-dom";

// Mock Next.js Navigation Router context hooks globally
jest.mock("next/navigation", () => ({
  useRouter: () => ({
    push: jest.fn(),
    replace: jest.fn(),
    prefetch: jest.fn(),
    back: jest.fn(),
    forward: jest.fn(),
    refresh: jest.fn(),
  }),
  usePathname: () => "/",
  useSearchParams: () => new URLSearchParams(),
}));

// Mock modern global browser matchMedia query compatibility
Object.defineProperty(window, "matchMedia", {
  writable: true,
  value: jest.fn().mockImplementation((query: string) => ({
    matches: false,
    media: query,
    onchange: null,
    addListener: jest.fn(),
    removeListener: jest.fn(),
    addEventListener: jest.fn(),
    removeEventListener: jest.fn(),
    dispatchEvent: jest.fn(),
  })),
});
````

## File: frontend/next.config.ts
````typescript
import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  reactStrictMode: true,
  images: {
    remotePatterns: [],
  },
  typescript: {
    // Keeps ignoring type errors from empty files during this test phase
    ignoreBuildErrors: true,
  },
};

export default nextConfig;
````

## File: frontend/playwright.config.ts
````typescript
import { defineConfig } from "@playwright/test";

export default defineConfig({
  testDir: "./e2e",
});
````

## File: frontend/postcss.config.js
````javascript
export default {
  plugins: {
    "@tailwindcss/postcss": {},
  },
};
````

## File: frontend/PROGRESS.md
````markdown
# 🚀 Project Progress Status
*Last Synced: 2026-07-13 20:11:04*

## 📁 Current File Structure Map
```text
├── .env.example
├── .env.local
├── .prettierrc
├── app
│   ├── _(auth)
│   │   ├── forgot-password
│   │   │   └── page.tsx
│   │   ├── layout.tsx
│   │   ├── login
│   │   │   └── page.tsx
│   │   ├── register
│   │   │   └── page.tsx
│   │   ├── reset-password
│   │   │   └── page.tsx
│   │   └── verify-email
│   │       └── page.tsx
│   ├── _(protected)
│   │   ├── account
│   │   │   └── page.tsx
│   │   ├── addresses
│   │   │   └── page.tsx
│   │   ├── chat-history
│   │   │   └── page.tsx
│   │   ├── checkout
│   │   │   ├── order-confirmation
│   │   │   │   └── [orderId]
│   │   │   │       └── page.tsx
│   │   │   └── page.tsx
│   │   ├── layout.tsx
│   │   ├── notifications
│   │   │   └── page.tsx
│   │   ├── orders
│   │   │   ├── [orderId]
│   │   │   │   ├── page.tsx
│   │   │   │   └── return
│   │   │   │       └── page.tsx
│   │   │   └── page.tsx
│   │   ├── profile
│   │   │   └── page.tsx
│   │   ├── settings
│   │   │   └── page.tsx
│   │   └── wishlist
│   │       └── page.tsx
│   ├── _(public)
│   │   ├── about
│   │   │   └── page.tsx
│   │   ├── cart
│   │   │   └── page.tsx
│   │   ├── categories
│   │   │   ├── [slug]
│   │   │   │   └── page.tsx
│   │   │   └── page.tsx
│   │   ├── contact
│   │   │   └── page.tsx
│   │   ├── faq
│   │   │   └── page.tsx
│   │   ├── layout.tsx
│   │   ├── loading.tsx
│   │   ├── page.tsx
│   │   ├── privacy
│   │   │   └── page.tsx
│   │   ├── products
│   │   │   ├── [slug]
│   │   │   │   ├── loading.tsx
│   │   │   │   └── page.tsx
│   │   │   ├── loading.tsx
│   │   │   └── page.tsx
│   │   ├── return-policy
│   │   │   └── page.tsx
│   │   ├── search
│   │   │   └── page.tsx
│   │   └── terms
│   │       └── page.tsx
│   ├── api
│   │   ├── auth
│   │   │   ├── login
│   │   │   │   └── route.ts
│   │   │   └── logout
│   │   │       └── route.ts
│   │   ├── checkout
│   │   │   └── create-payment-intent
│   │   │       └── route.ts
│   │   └── webhooks
│   │       └── stripe
│   │           └── route.ts
│   ├── error.tsx
│   ├── globals.css
│   ├── layout.tsx
│   ├── not-found.tsx
│   ├── page.tsx
│   ├── robots.ts
│   └── sitemap.ts
├── components
│   ├── features
│   │   ├── auth
│   │   ├── cart
│   │   ├── chat
│   │   ├── checkout
│   │   ├── notifications
│   │   ├── orders
│   │   ├── product
│   │   ├── reviews
│   │   ├── search
│   │   └── wishlist
│   ├── layout
│   └── ui
├── e2e
│   ├── auth.spec.ts
│   ├── checkout.spec.ts
│   └── phase1-checkpoint.spec.ts
├── eslint.config.mjs
├── gitignore
├── hooks
│   ├── useDebouncedValue.ts
│   ├── useOrderStatusPolling.ts
│   └── useWebSocket.ts
├── lib
│   ├── api
│   │   ├── auth.ts
│   │   ├── cart.ts
│   │   ├── client.ts
│   │   ├── notifications.ts
│   │   ├── orders.ts
│   │   ├── products.ts
│   │   ├── reviews.ts
│   │   ├── users.ts
│   │   └── wishlist.ts
│   ├── stores
│   │   ├── authStore.ts
│   │   ├── cartStore.ts
│   │   ├── checkoutStore.ts
│   │   ├── notificationStore.ts
│   │   └── wishlistStore.ts
│   ├── stripe
│   │   ├── client.ts
│   │   └── paymentIntent.ts
│   ├── utils
│   │   └── format.ts
│   ├── validation
│   │   ├── address.ts
│   │   ├── auth.ts
│   │   ├── contact.ts
│   │   └── review.ts
│   └── websocket
│       ├── chatConnection.ts
│       └── connectionManager.ts
├── next-env.d.ts
├── next.config.ts
├── package-lock.json
├── package.json
├── postcss.config.js
├── public
├── tests
│   └── smoke.test.tsx
├── tsconfig.json
└── types
    ├── api.ts
    ├── order.ts
    ├── product.ts
    └── user.ts
```

## ⏱️ Recently Modified Files (Active Workspace Delta)
- `types\user.ts` *(Modified: 2026-07-13 17:05:11)*
- `types\product.ts` *(Modified: 2026-07-13 17:05:11)*
- `types\order.ts` *(Modified: 2026-07-13 17:05:11)*
- `types\api.ts` *(Modified: 2026-07-13 17:05:11)*
- `tsconfig.json` *(Modified: 2026-07-13 18:59:31)*

## 📝 Next Steps / Tasks to Do
- [ ] Build lib/api/ with a typed client for auth, products, orders, users, cart resources.
````

## File: frontend/proxy.ts
````typescript
import { NextRequest, NextResponse } from "next/server";

const PROTECTED_PREFIXES = [
  "/account",
  "/addresses",
  "/chat-history",
  "/checkout",
  "/notifications",
  "/orders",
  "/profile",
  "/settings",
  "/wishlist",
];

const AUTH_PREFIXES = ["/login", "/register", "/forgot-password", "/reset-password"];

const ACCESS_TOKEN_COOKIE = "access_token";
const REFRESH_TOKEN_COOKIE = "refresh_token";

export function proxy(request: NextRequest) {
  const { pathname } = request.nextUrl;

  const hasSession =
    request.cookies.has(ACCESS_TOKEN_COOKIE) || request.cookies.has(REFRESH_TOKEN_COOKIE);

  const isProtected = PROTECTED_PREFIXES.some((prefix) => pathname.startsWith(prefix));
  const isAuthPage = AUTH_PREFIXES.some((prefix) => pathname.startsWith(prefix));

  if (isProtected && !hasSession) {
    const loginUrl = new URL("/login", request.url);
    loginUrl.searchParams.set("redirect", pathname);
    return NextResponse.redirect(loginUrl);
  }

  if (isAuthPage && hasSession) {
    return NextResponse.redirect(new URL("/account", request.url));
  }

  return NextResponse.next();
}

export const config = {
  matcher: [
    "/account/:path*",
    "/addresses/:path*",
    "/chat-history/:path*",
    "/checkout/:path*",
    "/notifications/:path*",
    "/orders/:path*",
    "/profile/:path*",
    "/settings/:path*",
    "/wishlist/:path*",
    "/login",
    "/register",
    "/forgot-password",
    "/reset-password",
  ],
};
````

## File: frontend/tsconfig.jest.json
````json
{
  "extends": "./tsconfig.json",
  "compilerOptions": {
    "module": "commonjs",
    "moduleResolution": "node",
    "jsx": "react-jsx",
    "esModuleInterop": true,
    "isolatedModules": true
  }
}
````

## File: frontend/update_progress.py
````python
import os
import time
from datetime import datetime

# Specific development file types and folder layers ignored by the mapping process
IGNORE_LIST = {
    '.git', '.claude', '.github', 'node_modules', '__pycache__', 
    'update_progress.py', 'PROGRESS.md', 'repomix-output.txt', '.next', 'dist'
}

def get_project_tree(dir_path, prefix=""):
    """Recursively calculates a visual text-based layout of directories and files."""
    tree = ""
    try:
        items = sorted(os.listdir(dir_path))
    except PermissionError:
        return ""
    
    # Filter out hidden deployment or asset directories
    items = [item for item in items if item not in IGNORE_LIST]
    
    for i, item in enumerate(items):
        path = os.path.join(dir_path, item)
        is_last = (i == len(items) - 1)
        connector = "└── " if is_last else "├── "
        
        tree += f"{prefix}{connector}{item}\n"
        
        if os.path.isdir(path):
            next_prefix = prefix + ("    " if is_last else "│   ")
            tree += get_project_tree(path, next_prefix)
    return tree

def get_recent_files(dir_path, limit=5):
    """Identifies and indexes the most recently updated project code files."""
    file_list = []
    for root, dirs, files in os.walk(dir_path):
        # Skip evaluating ignored system directory paths
        dirs[:] = [d for d in dirs if d not in IGNORE_LIST]
        
        for file in files:
            if file in IGNORE_LIST:
                continue
            path = os.path.join(root, file)
            try:
                mod_time = os.path.getmtime(path)
                file_list.append((path, mod_time))
            except FileNotFoundError:
                continue
                
    # Sort paths descending by date modified
    file_list.sort(key=lambda x: x, reverse=True)
    return file_list[:limit]

def main():
    root_dir = os.path.dirname(os.path.abspath(__file__))
    
    print("⏳ Analyzing project structure and identifying current development delta...")
    
    folder_tree = get_project_tree(root_dir)
    recent_files = get_recent_files(root_dir)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    markdown_content = f"""# 🚀 Project Progress Status
*Last Synced: {timestamp}*

## 📁 Current File Structure Map
```text
{folder_tree if folder_tree else 'Project root is currently clear.'}```

## ⏱️ Recently Modified Files (Active Workspace Delta)
"""
    if recent_files:
        for path, mod_time in recent_files:
            relative_path = os.path.relpath(path, root_dir)
            readable_time = datetime.fromtimestamp(mod_time).strftime("%Y-%m-%d %H:%M:%S")
            markdown_content += f"- `{relative_path}` *(Modified: {readable_time})*\n"
    else:
        markdown_content += "- No recent modifications detected in this work session.\n"
        
    markdown_content += """
## 📝 Next Steps / Tasks to Do
- [ ] *Insert your active architectural prompt or next component requirement here*
"""

    with open(os.path.join(root_dir, "PROGRESS.md"), "w", encoding="utf-8") as f:
        f.write(markdown_content)
        
    print("✅ PROGRESS.md documentation block compiled successfully.")

if __name__ == "__main__":
    main()
````

## File: package.json
````json
{
  "devDependencies": {
    "@tailwindcss/postcss": "^4.3.2"
  }
}
````

## File: backend/alembic/env.py
````python
from logging.config import fileConfig
import os

from dotenv import load_dotenv
from sqlalchemy import engine_from_config, pool

from alembic import context

load_dotenv()  # loads variables from backend/.env into os.environ

config = context.config

# Override sqlalchemy.url from the DATABASE_URL environment variable
database_url = os.getenv("DATABASE_URL")
if not database_url:
    raise RuntimeError("DATABASE_URL is not set. Check your .env file.")
config.set_main_option("sqlalchemy.url", database_url)

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

from app.database.base import Base
from app.models import *  # This pulls in every model registered in __init__.py
target_metadata = Base.metadata


def run_migrations_offline() -> None:
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
````

## File: backend/app/api/routes/checkout.py
````python
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.database.session import get_db
from app.models.cart import Cart
from app.models.cart_item import CartItem
from app.models.customer_profile import CustomerProfile
from app.models.order import Order
from app.models.order_item import OrderItem
from app.models.product_variant import ProductVariant
from app.models.user import User
from app.schemas.order import OrderOut
from app.core.auth import get_current_user

router = APIRouter()

_CART_ITEM_LOAD = selectinload(Cart.items).selectinload(CartItem.product_variant)


async def _get_or_create_customer_profile(db: AsyncSession, user: User) -> CustomerProfile:
    result = await db.execute(select(CustomerProfile).where(CustomerProfile.user_id == user.id))
    profile = result.scalar_one_or_none()
    if not profile:
        profile = CustomerProfile(user_id=user.id)
        db.add(profile)
        await db.commit()
        await db.refresh(profile)
    return profile


@router.post("/checkout", response_model=OrderOut, status_code=201)
async def checkout(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    profile = await _get_or_create_customer_profile(db, current_user)

    result = await db.execute(
        select(Cart).options(_CART_ITEM_LOAD).where(Cart.customer_id == profile.id)
    )
    cart = result.scalar_one_or_none()
    if not cart or not cart.items:
        raise HTTPException(status_code=400, detail="Cart is empty")

    # Lock and validate stock for every line before committing anything
    for item in cart.items:
        result = await db.execute(
            select(ProductVariant).where(ProductVariant.id == item.product_variant_id)
        )
        variant = result.scalar_one_or_none()
        if not variant or not variant.is_active:
            raise HTTPException(
                status_code=400,
                detail=f"Product variant {item.product_variant_id} is no longer available",
            )
        if variant.stock_quantity < item.quantity:
            raise HTTPException(
                status_code=400,
                detail=f"Insufficient stock for SKU '{variant.sku}': only {variant.stock_quantity} available",
            )

    new_order = Order(
        customer_id=profile.id,
        order_status="open",
        total_amount=0,
    )
    db.add(new_order)
    await db.flush()  # assigns new_order.id without committing

    total = 0.0
    for item in cart.items:
        result = await db.execute(
            select(ProductVariant).where(ProductVariant.id == item.product_variant_id)
        )
        variant = result.scalar_one()

        price = float(variant.price)
        db.add(OrderItem(
            order_id=new_order.id,
            product_variant_id=variant.id,
            quantity=item.quantity,
            price_at_purchase=price,
        ))
        variant.stock_quantity -= item.quantity
        total += price * item.quantity

    new_order.total_amount = total

    for item in cart.items:
        await db.delete(item)

    await db.commit()

    result = await db.execute(
        select(Order).options(selectinload(Order.items)).where(Order.id == new_order.id)
    )
    return result.scalar_one()
````

## File: backend/app/api/routes/customer_order.py
````python
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.database.session import get_db
from app.models.user import User
from app.models.customer_order import Order, OrderItem, ReturnRequest
from app.models.cart import Cart
from app.models.cart_item import CartItem
from app.models.customer_profile import CustomerProfile
from app.schemas.customer_order import (
    CustomerOrderOut,
    ReturnRequestCreate,
    ReturnRequestStatusUpdate,
    ReturnRequestOut,
)
from app.core.auth import get_current_user
from app.core.permissions import require_role, ADMIN, MANAGER, STAFF

router = APIRouter(tags=["Customer Orders"])

CANCELLABLE_STATUSES = {"open", "pending"}


async def _get_or_create_customer_profile(db: AsyncSession, user: User) -> CustomerProfile:
    result = await db.execute(select(CustomerProfile).where(CustomerProfile.user_id == user.id))
    profile = result.scalar_one_or_none()
    if not profile:
        profile = CustomerProfile(user_id=user.id)
        db.add(profile)
        await db.commit()
        await db.refresh(profile)
    return profile


async def _get_own_order(db: AsyncSession, order_id: int, profile: CustomerProfile) -> Order:
    result = await db.execute(
        select(Order).options(selectinload(Order.items)).where(Order.id == order_id)
    )
    order = result.scalar_one_or_none()
    if not order or order.customer_id != profile.id:
        raise HTTPException(status_code=404, detail="Order not found")
    return order


# ---- Orders ----

@router.post("/orders/{order_id}/cancel", response_model=CustomerOrderOut)
async def cancel_order(
    order_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    profile = await _get_or_create_customer_profile(db, current_user)
    order = await _get_own_order(db, order_id, profile)

    if order.order_status not in CANCELLABLE_STATUSES:
        raise HTTPException(
            status_code=400,
            detail=f"Order in status '{order.order_status}' cannot be cancelled",
        )

    order.order_status = "cancelled"
    await db.commit()
    order = await _get_own_order(db, order_id, profile)
    return order


@router.post("/orders/{order_id}/reorder", response_model=CustomerOrderOut, status_code=201)
async def reorder(
    order_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    profile = await _get_or_create_customer_profile(db, current_user)
    old_order = await _get_own_order(db, order_id, profile)

    result = await db.execute(select(Cart).where(Cart.customer_id == profile.id))
    cart = result.scalar_one_or_none()
    if not cart:
        cart = Cart(customer_id=profile.id)
        db.add(cart)
        await db.flush()

    for old_item in old_order.items:
        if old_item.product_variant_id is None:
            continue
        result = await db.execute(
            select(CartItem).where(
                CartItem.cart_id == cart.id,
                CartItem.product_variant_id == old_item.product_variant_id,
            )
        )
        cart_item = result.scalar_one_or_none()
        if cart_item:
            cart_item.quantity += old_item.quantity
        else:
            db.add(CartItem(
                cart_id=cart.id,
                product_variant_id=old_item.product_variant_id,
                quantity=old_item.quantity,
            ))

    await db.commit()
    old_order = await _get_own_order(db, order_id, profile)
    return old_order


@router.get("/orders/{order_id}/invoice", response_model=CustomerOrderOut)
async def get_invoice(
    order_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    profile = await _get_or_create_customer_profile(db, current_user)
    order = await _get_own_order(db, order_id, profile)
    return order


# ---- Return Requests ----

@router.post("/return-requests", response_model=ReturnRequestOut, status_code=status.HTTP_201_CREATED)
async def create_return_request(
    payload: ReturnRequestCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    profile = await _get_or_create_customer_profile(db, current_user)

    result = await db.execute(
        select(OrderItem).join(Order, Order.id == OrderItem.order_id).where(
            OrderItem.id == payload.order_item_id,
            Order.customer_id == profile.id,
        )
    )
    order_item = result.scalar_one_or_none()
    if not order_item:
        raise HTTPException(status_code=404, detail="Order item not found")

    existing = await db.execute(
        select(ReturnRequest).where(ReturnRequest.order_item_id == payload.order_item_id)
    )
    if existing.scalar_one_or_none():
        raise HTTPException(status_code=400, detail="Return request already exists for this item")

    return_request = ReturnRequest(
        order_item_id=payload.order_item_id,
        customer_id=profile.id,
        reason=payload.reason,
    )
    db.add(return_request)
    await db.commit()
    await db.refresh(return_request)
    return return_request


@router.get("/return-requests", response_model=list[ReturnRequestOut])
async def list_return_requests(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    profile = await _get_or_create_customer_profile(db, current_user)
    result = await db.execute(
        select(ReturnRequest).where(ReturnRequest.customer_id == profile.id)
    )
    return result.scalars().all()


@router.patch("/return-requests/{request_id}/status", response_model=ReturnRequestOut)
async def update_return_request_status(
    request_id: int,
    payload: ReturnRequestStatusUpdate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER, STAFF)),
):
    result = await db.execute(select(ReturnRequest).where(ReturnRequest.id == request_id))
    return_request = result.scalar_one_or_none()
    if not return_request:
        raise HTTPException(status_code=404, detail="Return request not found")

    return_request.status = payload.status
    if payload.refund_amount is not None:
        return_request.refund_amount = payload.refund_amount
    if payload.status in ("approved", "rejected", "completed"):
        from datetime import datetime, timezone
        return_request.processed_at = datetime.now(timezone.utc)

    await db.commit()
    await db.refresh(return_request)
    return return_request
````

## File: backend/app/api/routes/permissions.py
````python
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.session import get_db
from app.models.permission import Permission
from app.models.user import User
from app.schemas.permission import PermissionOut, PermissionCreate, PermissionUpdate
from app.core.permissions import require_role, ADMIN

router = APIRouter()


@router.get("/permissions", response_model=list[PermissionOut])
async def get_permissions(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN))
):
    result = await db.execute(select(Permission))
    return result.scalars().all()


@router.get("/permissions/{permission_id}", response_model=PermissionOut)
async def get_permission(
    permission_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN))
):
    result = await db.execute(select(Permission).where(Permission.id == permission_id))
    permission = result.scalar_one_or_none()
    if not permission:
        raise HTTPException(status_code=404, detail="Permission not found")
    return permission


@router.post("/permissions", response_model=PermissionOut, status_code=201)
async def create_permission(
    payload: PermissionCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN))
):
    result = await db.execute(select(Permission).where(Permission.name == payload.name))
    existing = result.scalar_one_or_none()
    if existing:
        raise HTTPException(status_code=400, detail="Permission name already exists")

    new_permission = Permission(name=payload.name, description=payload.description)
    db.add(new_permission)
    await db.commit()
    await db.refresh(new_permission)
    return new_permission


@router.put("/permissions/{permission_id}", response_model=PermissionOut)
async def update_permission(
    permission_id: int,
    payload: PermissionUpdate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN))
):
    result = await db.execute(select(Permission).where(Permission.id == permission_id))
    permission = result.scalar_one_or_none()
    if not permission:
        raise HTTPException(status_code=404, detail="Permission not found")

    update_data = payload.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(permission, field, value)

    await db.commit()
    await db.refresh(permission)
    return permission


@router.delete("/permissions/{permission_id}", status_code=204)
async def delete_permission(
    permission_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN))
):
    result = await db.execute(select(Permission).where(Permission.id == permission_id))
    permission = result.scalar_one_or_none()
    if not permission:
        raise HTTPException(status_code=404, detail="Permission not found")

    await db.delete(permission)
    await db.commit()
    return None
````

## File: backend/app/api/routes/product_categories.py
````python
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.session import get_db
from app.models.product import Product
from app.models.category import Category
from app.models.product_category import ProductCategory
from app.models.user import User
from app.schemas.product_category import ProductCategoryOut, ProductCategoryCreate
from app.core.permissions import require_role, ADMIN, MANAGER, STAFF

router = APIRouter()


@router.get("/products/{product_id}/categories", response_model=list[ProductCategoryOut])
async def get_product_categories(
    product_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER, STAFF))
):
    result = await db.execute(select(Product).where(Product.id == product_id))
    product = result.scalar_one_or_none()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    result = await db.execute(select(ProductCategory).where(ProductCategory.product_id == product_id))
    return result.scalars().all()


@router.post("/products/{product_id}/categories", response_model=ProductCategoryOut, status_code=201)
async def assign_category_to_product(
    product_id: int,
    payload: ProductCategoryCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER, STAFF))
):
    result = await db.execute(select(Product).where(Product.id == product_id))
    product = result.scalar_one_or_none()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    result = await db.execute(select(Category).where(Category.id == payload.category_id))
    category = result.scalar_one_or_none()
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")

    result = await db.execute(
        select(ProductCategory).where(
            ProductCategory.product_id == product_id,
            ProductCategory.category_id == payload.category_id,
        )
    )
    existing = result.scalar_one_or_none()
    if existing:
        raise HTTPException(status_code=400, detail="This product is already assigned to this category")

    link = ProductCategory(product_id=product_id, category_id=payload.category_id)
    db.add(link)
    await db.commit()
    await db.refresh(link)
    return link


@router.delete("/products/{product_id}/categories/{category_id}", status_code=204)
async def remove_category_from_product(
    product_id: int,
    category_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER, STAFF))
):
    result = await db.execute(
        select(ProductCategory).where(
            ProductCategory.product_id == product_id,
            ProductCategory.category_id == category_id,
        )
    )
    link = result.scalar_one_or_none()
    if not link:
        raise HTTPException(status_code=404, detail="This product is not assigned to this category")

    await db.delete(link)
    await db.commit()
    return None
````

## File: backend/app/api/routes/product_variants.py
````python
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError

from app.database.session import get_db
from app.models.product import Product
from app.models.product_variant import ProductVariant
from app.models.user import User
from app.schemas.product_variant import ProductVariantOut, ProductVariantCreate, ProductVariantUpdate
from app.core.permissions import require_role, ADMIN, MANAGER, STAFF

router = APIRouter()


@router.get("/products/{product_id}/variants", response_model=list[ProductVariantOut])
async def get_product_variants(
    product_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER, STAFF))
):
    result = await db.execute(select(Product).where(Product.id == product_id))
    product = result.scalar_one_or_none()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    result = await db.execute(select(ProductVariant).where(ProductVariant.product_id == product_id))
    return result.scalars().all()


@router.post("/products/{product_id}/variants", response_model=ProductVariantOut, status_code=201)
async def create_product_variant(
    product_id: int,
    payload: ProductVariantCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER, STAFF))
):
    result = await db.execute(select(Product).where(Product.id == product_id))
    product = result.scalar_one_or_none()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    new_variant = ProductVariant(
        product_id=product_id,
        sku=payload.sku,
        price=payload.price,
        stock_quantity=payload.stock_quantity,
        is_active=payload.is_active,
    )
    db.add(new_variant)

    try:
        await db.commit()
    except IntegrityError:
        await db.rollback()
        raise HTTPException(status_code=400, detail="SKU already exists")

    await db.refresh(new_variant)
    return new_variant


@router.get("/variants/{variant_id}", response_model=ProductVariantOut)
async def get_variant(
    variant_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER, STAFF))
):
    result = await db.execute(select(ProductVariant).where(ProductVariant.id == variant_id))
    variant = result.scalar_one_or_none()
    if not variant:
        raise HTTPException(status_code=404, detail="Variant not found")
    return variant


@router.put("/variants/{variant_id}", response_model=ProductVariantOut)
async def update_variant(
    variant_id: int,
    payload: ProductVariantUpdate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER, STAFF))
):
    result = await db.execute(select(ProductVariant).where(ProductVariant.id == variant_id))
    variant = result.scalar_one_or_none()
    if not variant:
        raise HTTPException(status_code=404, detail="Variant not found")

    update_data = payload.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(variant, field, value)

    try:
        await db.commit()
    except IntegrityError:
        await db.rollback()
        raise HTTPException(status_code=400, detail="SKU already exists")

    await db.refresh(variant)
    return variant


@router.delete("/variants/{variant_id}", status_code=204)
async def delete_variant(
    variant_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER, STAFF))
):
    result = await db.execute(select(ProductVariant).where(ProductVariant.id == variant_id))
    variant = result.scalar_one_or_none()
    if not variant:
        raise HTTPException(status_code=404, detail="Variant not found")

    try:
        await db.delete(variant)
        await db.commit()
    except IntegrityError:
        await db.rollback()
        raise HTTPException(
            status_code=400,
            detail="This variant cannot be deleted because it has existing orders. Deactivate it instead.",
        )

    return None
````

## File: backend/app/api/routes/products.py
````python
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.session import get_db
from app.models.product import Product
from app.models.user import User
from app.schemas.product import ProductOut, ProductCreate, ProductUpdate
from app.core.permissions import require_role, ADMIN, MANAGER, STAFF

router = APIRouter()


@router.get("/products", response_model=list[ProductOut])
async def get_products(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER, STAFF))
):
    result = await db.execute(select(Product))
    return result.scalars().all()


@router.get("/products/{product_id}", response_model=ProductOut)
async def get_product(
    product_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER, STAFF))
):
    result = await db.execute(select(Product).where(Product.id == product_id))
    product = result.scalar_one_or_none()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


@router.post("/products", response_model=ProductOut, status_code=201)
async def create_product(
    payload: ProductCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER, STAFF))
):
    result = await db.execute(select(Product).where(Product.name == payload.name))
    existing = result.scalar_one_or_none()
    if existing:
        raise HTTPException(status_code=400, detail="Product name already exists")

    new_product = Product(
        name=payload.name,
        description=payload.description,
        price=payload.price,
        is_active=payload.is_active,
    )
    db.add(new_product)
    await db.commit()
    await db.refresh(new_product)
    return new_product


@router.put("/products/{product_id}", response_model=ProductOut)
async def update_product(
    product_id: int,
    payload: ProductUpdate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER, STAFF))
):
    result = await db.execute(select(Product).where(Product.id == product_id))
    product = result.scalar_one_or_none()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    update_data = payload.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(product, field, value)

    await db.commit()
    await db.refresh(product)
    return product


@router.delete("/products/{product_id}", status_code=204)
async def delete_product(
    product_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER, STAFF))
):
    result = await db.execute(select(Product).where(Product.id == product_id))
    product = result.scalar_one_or_none()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    await db.delete(product)
    await db.commit()
    return None
````

## File: backend/app/api/routes/role_permissions.py
````python
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.session import get_db
from app.models.role import Role
from app.models.permission import Permission
from app.models.role_permission import RolePermission
from app.models.user import User
from app.schemas.permission import PermissionOut
from app.core.permissions import require_role, block_manager_on_admin_target, ADMIN, MANAGER

router = APIRouter()


class RolePermissionsSync(BaseModel):
    permission_ids: list[int]


@router.get("/roles/permissions", response_model=list[PermissionOut])
async def get_all_permissions(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER))
):
    result = await db.execute(select(Permission))
    return result.scalars().all()


@router.get("/roles/{role_id}/permissions", response_model=list[PermissionOut])
async def get_role_permissions(
    role_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER))
):
    result = await db.execute(select(Role).where(Role.id == role_id))
    role = result.scalar_one_or_none()
    if not role:
        raise HTTPException(status_code=404, detail="Role not found")

    result = await db.execute(
        select(Permission)
        .join(RolePermission, Permission.id == RolePermission.permission_id)
        .where(RolePermission.role_id == role_id)
    )
    return result.scalars().all()


@router.post("/roles/{role_id}/permissions", status_code=200)
async def assign_permissions_to_role(
    role_id: int,
    payload: RolePermissionsSync,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER))
):
    result = await db.execute(select(Role).where(Role.id == role_id))
    role = result.scalar_one_or_none()
    if not role:
        raise HTTPException(status_code=404, detail="Role not found")

    block_manager_on_admin_target(current_user, role.id)

    result = await db.execute(select(RolePermission).where(RolePermission.role_id == role_id))
    current_links = result.scalars().all()
    current_perm_ids = {link.permission_id for link in current_links}

    target_perm_ids = set(payload.permission_ids)
    to_delete = [link for link in current_links if link.permission_id not in target_perm_ids]
    to_insert_ids = target_perm_ids - current_perm_ids

    for link in to_delete:
        await db.delete(link)

    if to_insert_ids:
        result = await db.execute(select(func.count()).select_from(Permission).where(Permission.id.in_(to_insert_ids)))
        valid_perms_count = result.scalar_one()
        if valid_perms_count != len(to_insert_ids):
            raise HTTPException(status_code=400, detail="One or more permission IDs are invalid")

        for perm_id in to_insert_ids:
            new_link = RolePermission(role_id=role_id, permission_id=perm_id)
            db.add(new_link)

    await db.commit()
    return {"status": "success", "message": "Permissions updated successfully"}


@router.delete("/roles/{role_id}/permissions/{permission_id}", status_code=204)
async def remove_permission_from_role(
    role_id: int,
    permission_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER))
):
    result = await db.execute(select(Role).where(Role.id == role_id))
    role = result.scalar_one_or_none()
    if not role:
        raise HTTPException(status_code=404, detail="Role not found")

    block_manager_on_admin_target(current_user, role.id)

    result = await db.execute(
        select(RolePermission).where(
            RolePermission.role_id == role_id,
            RolePermission.permission_id == permission_id,
        )
    )
    link = result.scalar_one_or_none()
    if not link:
        raise HTTPException(status_code=404, detail="Permission assignment not found")

    await db.delete(link)
    await db.commit()
    return None
````

## File: backend/app/api/routes/roles.py
````python
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError

from app.database.session import get_db
from app.models.role import Role
from app.models.user import User
from app.schemas.role import RoleOut, RoleCreate, RoleUpdate
from app.core.permissions import require_role, block_manager_on_admin_target, ADMIN, MANAGER

router = APIRouter()


@router.get("/roles", response_model=list[RoleOut])
async def get_roles(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER))
):
    result = await db.execute(select(Role))
    return result.scalars().all()


@router.get("/roles/{role_id}", response_model=RoleOut)
async def get_role(
    role_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER))
):
    result = await db.execute(select(Role).where(Role.id == role_id))
    role = result.scalar_one_or_none()
    if not role:
        raise HTTPException(status_code=404, detail="Role not found")
    return role


@router.post("/roles", response_model=RoleOut, status_code=201)
async def create_role(
    payload: RoleCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN))
):
    result = await db.execute(select(Role).where(Role.name == payload.name))
    existing = result.scalar_one_or_none()
    if existing:
        raise HTTPException(status_code=400, detail="Role name already exists")

    new_role = Role(name=payload.name, description=payload.description)
    db.add(new_role)
    await db.commit()
    await db.refresh(new_role)
    return new_role


@router.put("/roles/{role_id}", response_model=RoleOut)
async def update_role(
    role_id: int,
    payload: RoleUpdate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER))
):
    result = await db.execute(select(Role).where(Role.id == role_id))
    role = result.scalar_one_or_none()
    if not role:
        raise HTTPException(status_code=404, detail="Role not found")

    block_manager_on_admin_target(current_user, role.id)

    update_data = payload.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(role, field, value)

    await db.commit()
    await db.refresh(role)
    return role


@router.delete("/roles/{role_id}", status_code=204)
async def delete_role(
    role_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN))
):
    result = await db.execute(select(Role).where(Role.id == role_id))
    role = result.scalar_one_or_none()
    if not role:
        raise HTTPException(status_code=404, detail="Role not found")

    try:
        await db.delete(role)
        await db.commit()
    except IntegrityError:
        await db.rollback()
        raise HTTPException(
            status_code=400,
            detail="Cannot delete role: it is still assigned to one or more users"
        )
    return None
````

## File: backend/app/core/jwt.py
````python
import secrets
from datetime import datetime, timedelta, timezone
from jose import jwt, JWTError
from fastapi import HTTPException, status

from app.core.config import settings

REFRESH_TOKEN_EXPIRE_DAYS = 7


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)


def create_refresh_token() -> tuple[str, datetime]:
    token = secrets.token_urlsafe(64)
    expires_at = datetime.now(timezone.utc) + timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS)
    return token, expires_at


def verify_access_token(token: str):
    try:
        return jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token"
        )
````

## File: backend/app/database/session.py
````python
from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from app.core.config import settings

# Create our asynchronous database engine using modern Asyncio wrappers
engine = create_async_engine(
    settings.DATABASE_URL,
    echo=True,  # Shows SQL queries in terminal (disable in production)
    future=True
)

# Create an asynchronous session factory
AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False,
    expire_on_commit=False,
    class_=AsyncSession
)

# Database Dependency - Yields an AsyncSession instead of a synchronous Session
async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()
````

## File: backend/app/models/category.py
````python
from datetime import datetime

from sqlalchemy import DateTime, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class Category(Base):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    name: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)

    description: Mapped[str | None] = mapped_column(String(255), nullable=True)

    created_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    updated_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )

    # Relationships
    product_links: Mapped[list["ProductCategory"]] = relationship(
        back_populates="category",
        cascade="all, delete-orphan"
    )
````

## File: backend/app/models/order_item.py
````python
from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Integer, Numeric, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class OrderItem(Base):
    __tablename__ = "order_items"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    order_id: Mapped[int] = mapped_column(ForeignKey("orders.id", ondelete="CASCADE"), nullable=False)
    product_variant_id: Mapped[int | None] = mapped_column(ForeignKey("product_variants.id", ondelete="SET NULL"), nullable=True)

    quantity: Mapped[int] = mapped_column(Integer, nullable=False)
    price_at_purchase: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False)
    discount_amount: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False, default=0)
    tax_amount: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False, default=0)

    created_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now()
    )
    updated_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )

    # Relationships
    order: Mapped["Order"] = relationship(back_populates="items")
    variant: Mapped["ProductVariant | None"] = relationship()
````

## File: backend/app/schemas/auth.py
````python
from pydantic import BaseModel, EmailStr


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class ForgotPasswordRequest(BaseModel):
    email: EmailStr


class ResetPasswordRequest(BaseModel):
    token: str
    new_password: str
````

## File: backend/app/schemas/category.py
````python
from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field


class CategoryOut(BaseModel):
    id: int
    name: str
    description: str | None = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class CategoryCreate(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    description: str | None = None


class CategoryUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=1, max_length=100)
    description: str | None = None
````

## File: backend/app/schemas/customer_order.py
````python
from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field

from app.schemas.order_item import OrderItemOut


class CustomerOrderOut(BaseModel):
    id: int
    customer_name: str | None = None
    order_status: str
    total_amount: float
    created_at: datetime
    items: list[OrderItemOut] = []

    model_config = ConfigDict(from_attributes=True)


class ReturnRequestCreate(BaseModel):
    order_item_id: int
    reason: str | None = Field(default=None, max_length=1000)


class ReturnRequestStatusUpdate(BaseModel):
    status: str = Field(max_length=20)
    refund_amount: float | None = None


class ReturnRequestOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    order_item_id: int
    customer_id: int
    reason: str | None = None
    status: str
    refund_amount: float | None = None
    requested_at: datetime
    processed_at: datetime | None = None
````

## File: backend/app/schemas/user.py
````python
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict, EmailStr, Field

from app.schemas.role import RoleOut


class UserOut(BaseModel):
    id: int
    name: str
    email: str
    phone_number: Optional[str] = None
    avatar_url: Optional[str] = None
    role_id: int
    role: RoleOut
    is_active: bool
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class UserCreate(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    email: EmailStr
    password: str = Field(min_length=8)
    phone_number: Optional[str] = None
    avatar_url: Optional[str] = None
    role_id: int
    is_active: bool = True


class UserUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=1, max_length=100)
    email: EmailStr | None = None
    phone_number: str | None = None
    avatar_url: str | None = None
    role_id: int | None = None
    is_active: bool | None = None
````

## File: backend/tests/test_customer_auth.py
````python
import pytest
from datetime import datetime, timedelta, timezone

from sqlalchemy import select

from app.models.user import User

pytestmark = pytest.mark.asyncio


async def test_register_success(client, mock_emails):
    payload = {
        "name": "Jane Doe",
        "email": "jane@example.com",
        "password": "StrongPass123!",
        "phone_number": "+1234567890",
    }
    resp = await client.post("/customer/auth/register", json=payload)
    assert resp.status_code == 201
    body = resp.json()
    assert body["email"] == "jane@example.com"
    assert body["email_verified"] is False
    assert len(mock_emails["verification"]) == 1
    assert mock_emails["verification"][0][0] == "jane@example.com"


async def test_register_duplicate_email(client, make_customer):
    user, _ = await make_customer(email="dupe@example.com")
    payload = {
        "name": "Dupe",
        "email": "dupe@example.com",
        "password": "StrongPass123!",
    }
    resp = await client.post("/customer/auth/register", json=payload)
    assert resp.status_code == 400
    assert resp.json()["detail"] == "Email already registered"


async def test_register_invalid_password_too_short(client):
    payload = {"name": "Jane", "email": "jane2@example.com", "password": "short"}
    resp = await client.post("/customer/auth/register", json=payload)
    assert resp.status_code == 422


async def test_login_success(client, make_customer):
    user, password = await make_customer(email="login@example.com")
    resp = await client.post("/customer/auth/login", json={"email": "login@example.com", "password": password})
    assert resp.status_code == 200
    body = resp.json()
    assert body["message"] == "Logged in successfully."
    set_cookie_header = resp.headers.get("set-cookie", "")
    assert "access_token=" in set_cookie_header
    assert "refresh_token=" in set_cookie_header
    assert "HttpOnly" in set_cookie_header


async def test_me_uses_access_cookie(client, make_customer):
    user, password = await make_customer(email="me-cookie@example.com")
    login_resp = await client.post(
        "/customer/auth/login",
        json={"email": "me-cookie@example.com", "password": password},
    )
    assert login_resp.status_code == 200

    me_resp = await client.get("/customer/auth/me")
    assert me_resp.status_code == 200
    assert me_resp.json()["email"] == user.email


async def test_login_wrong_password(client, make_customer):
    await make_customer(email="wrongpass@example.com")
    resp = await client.post("/customer/auth/login", json={"email": "wrongpass@example.com", "password": "WrongPass!"})
    assert resp.status_code == 401
    assert resp.json()["detail"] == "Invalid email or password"


async def test_login_nonexistent_email(client):
    resp = await client.post("/customer/auth/login", json={"email": "nouser@example.com", "password": "whatever123"})
    assert resp.status_code == 401


async def test_login_inactive_account(client, make_customer):
    await make_customer(email="inactive@example.com", active=False)
    resp = await client.post("/customer/auth/login", json={"email": "inactive@example.com", "password": "Password123!"})
    assert resp.status_code == 403
    assert resp.json()["detail"] == "Account is inactive"


async def test_verify_email_success(client, make_customer, db):
    user, _ = await make_customer(email="verify@example.com", verified=False)
    user.email_verification_token = "valid-token-123"
    user.email_verification_expires_at = datetime.now(timezone.utc) + timedelta(hours=1)
    await db.commit()

    resp = await client.post("/customer/auth/verify-email", json={"token": "valid-token-123"})
    assert resp.status_code == 200

    result = await db.execute(select(User).where(User.email == "verify@example.com"))
    refreshed = result.scalar_one()
    assert refreshed.email_verified is True
    assert refreshed.email_verification_token is None


async def test_verify_email_expired_token(client, make_customer, db):
    user, _ = await make_customer(email="expired@example.com", verified=False)
    user.email_verification_token = "expired-token"
    user.email_verification_expires_at = datetime.now(timezone.utc) - timedelta(hours=1)
    await db.commit()

    resp = await client.post("/customer/auth/verify-email", json={"token": "expired-token"})
    assert resp.status_code == 400


async def test_verify_email_invalid_token(client):
    resp = await client.post("/customer/auth/verify-email", json={"token": "does-not-exist"})
    assert resp.status_code == 400


async def test_resend_verification_unverified_user(client, make_customer, mock_emails):
    await make_customer(email="resend@example.com", verified=False)
    resp = await client.post("/customer/auth/resend-verification", json={"email": "resend@example.com"})
    assert resp.status_code == 200
    assert len(mock_emails["verification"]) == 1


async def test_resend_verification_already_verified(client, make_customer, mock_emails):
    await make_customer(email="already@example.com", verified=True)
    resp = await client.post("/customer/auth/resend-verification", json={"email": "already@example.com"})
    assert resp.status_code == 200
    assert len(mock_emails["verification"]) == 0


async def test_resend_verification_nonexistent_email_returns_generic(client, mock_emails):
    resp = await client.post("/customer/auth/resend-verification", json={"email": "ghost@example.com"})
    assert resp.status_code == 200
    assert "If that email exists" in resp.json()["message"]
    assert len(mock_emails["verification"]) == 0


async def test_forgot_password_existing_active_user(client, make_customer, mock_emails):
    await make_customer(email="forgot@example.com")
    resp = await client.post("/customer/auth/forgot-password", json={"email": "forgot@example.com"})
    assert resp.status_code == 200
    assert len(mock_emails["reset"]) == 1


async def test_forgot_password_nonexistent_email_returns_generic(client, mock_emails):
    resp = await client.post("/customer/auth/forgot-password", json={"email": "ghost2@example.com"})
    assert resp.status_code == 200
    assert len(mock_emails["reset"]) == 0


async def test_reset_password_success(client, make_customer, db):
    user, _ = await make_customer(email="reset@example.com")
    user.password_reset_token = "reset-token-123"
    user.password_reset_expires_at = datetime.now(timezone.utc) + timedelta(hours=1)
    await db.commit()

    resp = await client.post(
        "/customer/auth/reset-password",
        json={"token": "reset-token-123", "new_password": "NewStrongPass123!"},
    )
    assert resp.status_code == 200

    login_resp = await client.post(
        "/customer/auth/login", json={"email": "reset@example.com", "password": "NewStrongPass123!"}
    )
    assert login_resp.status_code == 200


async def test_reset_password_expired_token(client, make_customer, db):
    user, _ = await make_customer(email="resetexp@example.com")
    user.password_reset_token = "expired-reset-token"
    user.password_reset_expires_at = datetime.now(timezone.utc) - timedelta(hours=1)
    await db.commit()

    resp = await client.post(
        "/customer/auth/reset-password",
        json={"token": "expired-reset-token", "new_password": "NewStrongPass123!"},
    )
    assert resp.status_code == 400


async def test_reset_password_invalid_token(client):
    resp = await client.post(
        "/customer/auth/reset-password",
        json={"token": "not-a-real-token", "new_password": "NewStrongPass123!"},
    )
    assert resp.status_code == 400


async def test_reset_password_inactive_account(client, make_customer, db):
    user, _ = await make_customer(email="resetinactive@example.com", active=False)
    user.password_reset_token = "inactive-reset-token"
    user.password_reset_expires_at = datetime.now(timezone.utc) + timedelta(hours=1)
    await db.commit()

    resp = await client.post(
        "/customer/auth/reset-password",
        json={"token": "inactive-reset-token", "new_password": "NewStrongPass123!"},
    )
    assert resp.status_code == 403
````

## File: backend/alembic.ini
````ini
# A generic, single database configuration.

[alembic]
# path to migration scripts.
# this is typically a path given in POSIX (e.g. forward slashes)
# format, relative to the token %(here)s which refers to the location of this
# ini file
script_location = %(here)s/alembic

# template used to generate migration file names; The default value is %%(rev)s_%%(slug)s
# Uncomment the line below if you want the files to be prepended with date and time
# see https://alembic.sqlalchemy.org/en/latest/tutorial.html#editing-the-ini-file
# for all available tokens
# file_template = %%(year)d_%%(month).2d_%%(day).2d_%%(hour).2d%%(minute).2d-%%(rev)s_%%(slug)s
# Or organize into date-based subdirectories (requires recursive_version_locations = true)
# file_template = %%(year)d/%%(month).2d/%%(day).2d_%%(hour).2d%%(minute).2d_%%(second).2d_%%(rev)s_%%(slug)s

# sys.path path, will be prepended to sys.path if present.
# defaults to the current working directory.  for multiple paths, the path separator
# is defined by "path_separator" below.
prepend_sys_path = .


# timezone to use when rendering the date within the migration file
# as well as the filename.
# If specified, requires the tzdata library which can be installed by adding
# `alembic[tz]` to the pip requirements.
# string value is passed to ZoneInfo()
# leave blank for localtime
# timezone =

# max length of characters to apply to the "slug" field
# truncate_slug_length = 40

# set to 'true' to run the environment during
# the 'revision' command, regardless of autogenerate
# revision_environment = false

# set to 'true' to allow .pyc and .pyo files without
# a source .py file to be detected as revisions in the
# versions/ directory
# sourceless = false

# version location specification; This defaults
# to <script_location>/versions.  When using multiple version
# directories, initial revisions must be specified with --version-path.
# The path separator used here should be the separator specified by "path_separator"
# below.
# version_locations = %(here)s/bar:%(here)s/bat:%(here)s/alembic/versions

# path_separator; This indicates what character is used to split lists of file
# paths, including version_locations and prepend_sys_path within configparser
# files such as alembic.ini.
# The default rendered in new alembic.ini files is "os", which uses os.pathsep
# to provide os-dependent path splitting.
#
# Note that in order to support legacy alembic.ini files, this default does NOT
# take place if path_separator is not present in alembic.ini.  If this
# option is omitted entirely, fallback logic is as follows:
#
# 1. Parsing of the version_locations option falls back to using the legacy
#    "version_path_separator" key, which if absent then falls back to the legacy
#    behavior of splitting on spaces and/or commas.
# 2. Parsing of the prepend_sys_path option falls back to the legacy
#    behavior of splitting on spaces, commas, or colons.
#
# Valid values for path_separator are:
#
# path_separator = :
# path_separator = ;
# path_separator = space
# path_separator = newline
#
# Use os.pathsep. Default configuration used for new projects.
path_separator = os

# set to 'true' to search source files recursively
# in each "version_locations" directory
# new in Alembic version 1.10
# recursive_version_locations = false

# the output encoding used when revision files
# are written from script.py.mako
# output_encoding = utf-8

# database URL.  This is consumed by the user-maintained env.py script only.
# other means of configuring database URLs may be customized within the env.py
# file. Left unset intentionally — env.py loads DATABASE_URL from .env via pydantic-settings/os.environ.
# sqlalchemy.url = driver://user:pass@localhost/dbname


[post_write_hooks]
# post_write_hooks defines scripts or Python functions that are run
# on newly generated revision scripts.  See the documentation for further
# detail and examples

# format using "black" - use the console_scripts runner, against the "black" entrypoint
# hooks = black
# black.type = console_scripts
# black.entrypoint = black
# black.options = -l 79 REVISION_SCRIPT_FILENAME

# lint with attempts to fix using "ruff" - use the module runner, against the "ruff" module
# hooks = ruff
# ruff.type = module
# ruff.module = ruff
# ruff.options = check --fix REVISION_SCRIPT_FILENAME

# Alternatively, use the exec runner to execute a binary found on your PATH
# hooks = ruff
# ruff.type = exec
# ruff.executable = ruff
# ruff.options = check --fix REVISION_SCRIPT_FILENAME

# Logging configuration.  This is also consumed by the user-maintained
# env.py script only.
[loggers]
keys = root,sqlalchemy,alembic

[handlers]
keys = console

[formatters]
keys = generic

[logger_root]
level = WARNING
handlers = console
qualname =

[logger_sqlalchemy]
level = WARNING
handlers =
qualname = sqlalchemy.engine

[logger_alembic]
level = INFO
handlers =
qualname = alembic

[handler_console]
class = StreamHandler
args = (sys.stderr,)
level = NOTSET
formatter = generic

[formatter_generic]
format = %(levelname)-5.5s [%(name)s] %(message)s
datefmt = %H:%M:%S
````

## File: frontend/app/(auth)/forgot-password/page.tsx
````typescript
export default function ForgotPasswordPage() {
  return (
    <div className="flex min-h-screen flex-col items-center justify-center bg-white px-4">
      <div className="w-full max-w-md space-y-4 text-center">
        <h1 className="text-2xl font-bold text-gray-900">Forgot Password</h1>
        <p className="text-sm text-gray-600">
          Enter your email address to reset your account password.
        </p>
        {/* Form elements go here later */}
      </div>
    </div>
  );
}
````

## File: frontend/app/(auth)/login/page.tsx
````typescript
"use client";

import { useState } from "react";
import { useRouter, useSearchParams } from "next/navigation";
import Link from "next/link";
import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import { loginSchema, LoginSchemaType } from "@/lib/validation/auth";
import { useAuthStore } from "@/lib/stores/authStore";
import { ApiError } from "@/lib/api/client";

export default function LoginPage() {
  const router = useRouter();
  const searchParams = useSearchParams();
  const redirectTo = searchParams.get("redirect") || "/account";
  const login = useAuthStore((state) => state.login);
  const isLoading = useAuthStore((state) => state.isLoading);
  const [formError, setFormError] = useState<string | null>(null);

  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm<LoginSchemaType>({
    resolver: zodResolver(loginSchema),
  });

  const onSubmit = async (data: LoginSchemaType) => {
    setFormError(null);
    try {
      await login(data);
      router.replace(redirectTo);
    } catch (error) {
      if (error instanceof ApiError) {
        setFormError(error.message);
      } else {
        setFormError("We couldn't sign you in. Please try again.");
      }
    }
  };

  return (
    <div className="flex min-h-screen flex-col items-center justify-center bg-white px-4">
      <div className="w-full max-w-md space-y-6">
        <div className="text-center">
          <h1 className="text-2xl font-bold text-gray-900">Sign In</h1>
          <p className="mt-1 text-sm text-gray-600">
            Welcome back! Please enter your details to log in.
          </p>
        </div>

        <form onSubmit={handleSubmit(onSubmit)} noValidate className="space-y-4">
          {formError && (
            <div className="rounded-md bg-red-50 px-4 py-3 text-sm text-red-700" role="alert">
              {formError}
            </div>
          )}

          <div>
            <label htmlFor="email" className="mb-1 block text-sm font-medium text-gray-700">
              Email
            </label>
            <input
              id="email"
              type="email"
              autoComplete="email"
              {...register("email")}
              className="w-full rounded-md border border-gray-300 px-3 py-2 text-sm focus:border-gray-900 focus:outline-none focus:ring-1 focus:ring-gray-900"
            />
            {errors.email && <p className="mt-1 text-sm text-red-600">{errors.email.message}</p>}
          </div>

          <div>
            <label htmlFor="password" className="mb-1 block text-sm font-medium text-gray-700">
              Password
            </label>
            <input
              id="password"
              type="password"
              autoComplete="current-password"
              {...register("password")}
              className="w-full rounded-md border border-gray-300 px-3 py-2 text-sm focus:border-gray-900 focus:outline-none focus:ring-1 focus:ring-gray-900"
            />
            {errors.password && (
              <p className="mt-1 text-sm text-red-600">{errors.password.message}</p>
            )}
          </div>

          <div className="flex justify-end">
            <Link href="/forgot-password" className="text-sm text-gray-600 hover:text-gray-900">
              Forgot password?
            </Link>
          </div>

          <button
            type="submit"
            disabled={isLoading}
            className="w-full rounded-md bg-gray-900 px-4 py-2 text-sm font-medium text-white transition hover:bg-gray-800 disabled:cursor-not-allowed disabled:opacity-60"
          >
            {isLoading ? "Signing in..." : "Sign In"}
          </button>
        </form>

        <p className="text-center text-sm text-gray-600">
          Don&apos;t have an account?{" "}
          <Link href="/register" className="font-medium text-gray-900 hover:underline">
            Create one
          </Link>
        </p>
      </div>
    </div>
  );
}
````

## File: frontend/app/(auth)/register/page.tsx
````typescript
"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";
import Link from "next/link";
import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import { registerSchema, RegisterSchemaType } from "@/lib/validation/auth";
import { useAuthStore } from "@/lib/stores/authStore";
import { ApiError } from "@/lib/api/client";

export default function RegisterPage() {
  const router = useRouter();
  const registerUser = useAuthStore((state) => state.register);
  const isLoading = useAuthStore((state) => state.isLoading);
  const [formError, setFormError] = useState<string | null>(null);

  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm<RegisterSchemaType>({
    resolver: zodResolver(registerSchema),
  });

  const onSubmit = async (data: RegisterSchemaType) => {
    setFormError(null);
    try {
      await registerUser(data);
      router.replace("/login?registered=true");
    } catch (error) {
      if (error instanceof ApiError) {
        setFormError(error.message);
      } else {
        setFormError("We couldn't create your account. Please try again.");
      }
    }
  };

  return (
    <div className="flex min-h-screen flex-col items-center justify-center bg-white px-4">
      <div className="w-full max-w-md space-y-6">
        <div className="text-center">
          <h1 className="text-2xl font-bold text-gray-900">Create an Account</h1>
          <p className="mt-1 text-sm text-gray-600">
            Sign up today to manage your store and product logistics.
          </p>
        </div>

        <form onSubmit={handleSubmit(onSubmit)} noValidate className="space-y-4">
          {formError && (
            <div className="rounded-md bg-red-50 px-4 py-3 text-sm text-red-700" role="alert">
              {formError}
            </div>
          )}

          <div className="grid grid-cols-2 gap-4">
            <div>
              <label htmlFor="firstName" className="mb-1 block text-sm font-medium text-gray-700">
                First Name
              </label>
              <input
                id="firstName"
                type="text"
                autoComplete="given-name"
                {...register("firstName")}
                className="w-full rounded-md border border-gray-300 px-3 py-2 text-sm focus:border-gray-900 focus:outline-none focus:ring-1 focus:ring-gray-900"
              />
              {errors.firstName && (
                <p className="mt-1 text-sm text-red-600">{errors.firstName.message}</p>
              )}
            </div>

            <div>
              <label htmlFor="lastName" className="mb-1 block text-sm font-medium text-gray-700">
                Last Name
              </label>
              <input
                id="lastName"
                type="text"
                autoComplete="family-name"
                {...register("lastName")}
                className="w-full rounded-md border border-gray-300 px-3 py-2 text-sm focus:border-gray-900 focus:outline-none focus:ring-1 focus:ring-gray-900"
              />
              {errors.lastName && (
                <p className="mt-1 text-sm text-red-600">{errors.lastName.message}</p>
              )}
            </div>
          </div>

          <div>
            <label htmlFor="email" className="mb-1 block text-sm font-medium text-gray-700">
              Email
            </label>
            <input
              id="email"
              type="email"
              autoComplete="email"
              {...register("email")}
              className="w-full rounded-md border border-gray-300 px-3 py-2 text-sm focus:border-gray-900 focus:outline-none focus:ring-1 focus:ring-gray-900"
            />
            {errors.email && <p className="mt-1 text-sm text-red-600">{errors.email.message}</p>}
          </div>

          <div>
            <label htmlFor="password" className="mb-1 block text-sm font-medium text-gray-700">
              Password
            </label>
            <input
              id="password"
              type="password"
              autoComplete="new-password"
              {...register("password")}
              className="w-full rounded-md border border-gray-300 px-3 py-2 text-sm focus:border-gray-900 focus:outline-none focus:ring-1 focus:ring-gray-900"
            />
            {errors.password && (
              <p className="mt-1 text-sm text-red-600">{errors.password.message}</p>
            )}
          </div>

          <button
            type="submit"
            disabled={isLoading}
            className="w-full rounded-md bg-gray-900 px-4 py-2 text-sm font-medium text-white transition hover:bg-gray-800 disabled:cursor-not-allowed disabled:opacity-60"
          >
            {isLoading ? "Creating account..." : "Create Account"}
          </button>
        </form>

        <p className="text-center text-sm text-gray-600">
          Already have an account?{" "}
          <Link href="/login" className="font-medium text-gray-900 hover:underline">
            Sign in
          </Link>
        </p>
      </div>
    </div>
  );
}
````

## File: frontend/app/(auth)/reset-password/page.tsx
````typescript
export default function ResetPasswordPage() {
  return (
    <div className="flex min-h-screen flex-col items-center justify-center bg-white px-4">
      <div className="w-full max-w-md space-y-4 text-center">
        <h1 className="text-2xl font-bold text-gray-900">Reset Password</h1>
        <p className="text-sm text-gray-600">
          Please enter your new production password security credentials below.
        </p>
      </div>
    </div>
  );
}
````

## File: frontend/app/(auth)/verify-email/page.tsx
````typescript
export default function VerifyEmailPage() {
  return (
    <div className="flex min-h-screen flex-col items-center justify-center bg-white px-4">
      <div className="w-full max-w-md space-y-4 text-center">
        <h1 className="text-2xl font-bold text-gray-900">Verify Email</h1>
        <p className="text-sm text-gray-600">
          We have sent a verification secure link to your registered email address.
        </p>
      </div>
    </div>
  );
}
````

## File: frontend/app/(auth)/layout.tsx
````typescript
import { ReactNode } from "react";

export default function AuthLayout({ children }: { children: ReactNode }) {
  return <>{children}</>;
}
````

## File: frontend/app/(protected)/account/page.tsx
````typescript
"use client";

import { useState, useEffect } from "react";
import { useRouter } from "next/navigation";
import { useAuthStore } from "@/lib/stores/authStore";

export default function AccountPage() {
  const router = useRouter();
  const { user, logout, fetchCurrentUser, isInitialized } = useAuthStore();
  const [isLoggingOut, setIsLoggingOut] = useState(false);

  useEffect(() => {
    if (!isInitialized) {
      fetchCurrentUser();
    }
  }, [isInitialized, fetchCurrentUser]);

  const handleLogout = async () => {
    setIsLoggingOut(true);
    try {
      // Clear store state & call backend logout endpoint
      await logout();
    } catch (error) {
      console.error("Logout error:", error);
    } finally {
      // Force a full location change to /login to ensure all middleware,
      // client router cache, and session cookies are completely cleared.
      if (typeof window !== "undefined") {
        window.location.href = "/login";
      }
    }
  };

  return (
    <div className="mx-auto max-w-4xl px-4 py-12">
      <div className="flex flex-col sm:flex-row sm:items-center sm:justify-between border-b border-gray-200 pb-6 mb-8 gap-4">
        <div>
          <h1 className="text-2xl font-bold text-gray-900">Account Dashboard</h1>
          <p className="mt-1 text-sm text-gray-600">Manage your profile and session settings.</p>
        </div>

        <button
          onClick={handleLogout}
          disabled={isLoggingOut}
          className="inline-flex items-center justify-center rounded-md bg-red-600 px-4 py-2.5 text-sm font-medium text-white shadow-sm transition hover:bg-red-700 focus:outline-none focus:ring-2 focus:ring-red-500 focus:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-60"
        >
          {isLoggingOut ? (
            <span className="flex items-center gap-2">
              <svg className="h-4 w-4 animate-spin text-white" viewBox="0 0 24 24" fill="none">
                <circle
                  className="opacity-25"
                  cx="12"
                  cy="12"
                  r="10"
                  stroke="currentColor"
                  strokeWidth="4"
                />
                <path
                  className="opacity-75"
                  fill="currentColor"
                  d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4z"
                />
              </svg>
              Logging out...
            </span>
          ) : (
            <span className="flex items-center gap-2">
              <svg className="h-4 w-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  strokeWidth="2"
                  d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1"
                />
              </svg>
              Sign Out
            </span>
          )}
        </button>
      </div>

      <div className="grid gap-6 md:grid-cols-2">
        {/* Profile Card */}
        <div className="rounded-lg border border-gray-200 bg-white p-6 shadow-sm">
          <h2 className="text-lg font-semibold text-gray-900 mb-4">User Details</h2>
          {user ? (
            <dl className="space-y-3 text-sm">
              <div>
                <dt className="text-gray-500 font-medium">Full Name</dt>
                <dd className="mt-0.5 text-gray-900">{user.name || "N/A"}</dd>
              </div>
              <div>
                <dt className="text-gray-500 font-medium">Email Address</dt>
                <dd className="mt-0.5 text-gray-900">{user.email}</dd>
              </div>
              <div>
                <dt className="text-gray-500 font-medium">Account Status</dt>
                <dd className="mt-0.5 inline-flex items-center rounded-full bg-green-50 px-2.5 py-0.5 text-xs font-medium text-green-700">
                  {user.emailVerified ? "Verified User" : "Active Session"}
                </dd>
              </div>
            </dl>
          ) : (
            <p className="text-sm text-gray-500">Loading user info...</p>
          )}
        </div>

        {/* Quick Links / Session Info */}
        <div className="rounded-lg border border-gray-200 bg-white p-6 shadow-sm flex flex-col justify-between">
          <div>
            <h2 className="text-lg font-semibold text-gray-900 mb-2">Session Control</h2>
            <p className="text-sm text-gray-600 mb-4">
              Signing out will end your active session, clear cached credentials, and redirect you
              back to the sign-in page.
            </p>
          </div>
          <div className="pt-4 border-t border-gray-100">
            <button
              onClick={handleLogout}
              disabled={isLoggingOut}
              className="w-full text-center rounded-md border border-gray-300 bg-white px-4 py-2 text-sm font-medium text-gray-700 hover:bg-gray-50 transition focus:outline-none"
            >
              Log out of account
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}
````

## File: frontend/app/(protected)/addresses/page.tsx
````typescript
export default function AddressesPage() {
  return (
    <div className="mx-auto max-w-4xl px-4 py-12">
      <h1 className="text-2xl font-bold text-gray-900">Addresses</h1>
      <p className="mt-2 text-sm text-gray-600">Manage your saved addresses.</p>
    </div>
  );
}
````

## File: frontend/app/(protected)/chat-history/page.tsx
````typescript
export default function ChatHistoryPage() {
  return (
    <div className="mx-auto max-w-4xl px-4 py-12">
      <h1 className="text-2xl font-bold text-gray-900">Chat History</h1>
      <p className="mt-2 text-sm text-gray-600">Your past support conversations.</p>
    </div>
  );
}
````

## File: frontend/app/(protected)/checkout/order-confirmation/[orderId]/page.tsx
````typescript
export default function OrderConfirmationPage({ params }: { params: { orderId: string } }) {
  return (
    <div className="mx-auto max-w-4xl px-4 py-12">
      <h1 className="text-2xl font-bold text-gray-900">Order Confirmed</h1>
      <p className="mt-2 text-sm text-gray-600">Order #{params.orderId}</p>
    </div>
  );
}
````

## File: frontend/app/(protected)/checkout/page.tsx
````typescript
export default function CheckoutPage() {
  return (
    <div className="mx-auto max-w-4xl px-4 py-12">
      <h1 className="text-2xl font-bold text-gray-900">Checkout</h1>
      <p className="mt-2 text-sm text-gray-600">Complete your purchase.</p>
    </div>
  );
}
````

## File: frontend/app/(protected)/notifications/page.tsx
````typescript
export default function NotificationsPage() {
  return (
    <div className="mx-auto max-w-4xl px-4 py-12">
      <h1 className="text-2xl font-bold text-gray-900">Notifications</h1>
      <p className="mt-2 text-sm text-gray-600">Your recent notifications.</p>
    </div>
  );
}
````

## File: frontend/app/(protected)/orders/[orderId]/return/page.tsx
````typescript
export default function OrderReturnPage({ params }: { params: { orderId: string } }) {
  return (
    <div className="mx-auto max-w-4xl px-4 py-12">
      <h1 className="text-2xl font-bold text-gray-900">Return Request</h1>
      <p className="mt-2 text-sm text-gray-600">Order #{params.orderId}</p>
    </div>
  );
}
````

## File: frontend/app/(protected)/orders/[orderId]/page.tsx
````typescript
export default function OrderDetailPage({ params }: { params: { orderId: string } }) {
  return (
    <div className="mx-auto max-w-4xl px-4 py-12">
      <h1 className="text-2xl font-bold text-gray-900">Order Detail</h1>
      <p className="mt-2 text-sm text-gray-600">Order #{params.orderId}</p>
    </div>
  );
}
````

## File: frontend/app/(protected)/orders/page.tsx
````typescript
export default function OrdersPage() {
  return (
    <div className="mx-auto max-w-4xl px-4 py-12">
      <h1 className="text-2xl font-bold text-gray-900">Orders</h1>
      <p className="mt-2 text-sm text-gray-600">Your order history.</p>
    </div>
  );
}
````

## File: frontend/app/(protected)/profile/page.tsx
````typescript
export default function ProfilePage() {
  return (
    <div className="mx-auto max-w-4xl px-4 py-12">
      <h1 className="text-2xl font-bold text-gray-900">Profile</h1>
      <p className="mt-2 text-sm text-gray-600">Manage your profile details.</p>
    </div>
  );
}
````

## File: frontend/app/(protected)/settings/page.tsx
````typescript
export default function SettingsPage() {
  return (
    <div className="mx-auto max-w-4xl px-4 py-12">
      <h1 className="text-2xl font-bold text-gray-900">Settings</h1>
      <p className="mt-2 text-sm text-gray-600">Manage your account settings.</p>
    </div>
  );
}
````

## File: frontend/app/(protected)/wishlist/page.tsx
````typescript
export default function WishlistPage() {
  return (
    <div className="mx-auto max-w-4xl px-4 py-12">
      <h1 className="text-2xl font-bold text-gray-900">Wishlist</h1>
      <p className="mt-2 text-sm text-gray-600">Products you've saved.</p>
    </div>
  );
}
````

## File: frontend/app/(protected)/layout.tsx
````typescript
export default function ProtectedLayout({ children }: { children: React.ReactNode }) {
  return <>{children}</>;
}
````

## File: frontend/app/(public)/about/page.tsx
````typescript
export default function AboutPage() {
  return (
    <div className="mx-auto max-w-4xl px-4 py-12">
      <h1 className="text-2xl font-bold text-gray-900">About Us</h1>
      <p className="mt-2 text-sm text-gray-600">Learn more about our store.</p>
    </div>
  );
}
````

## File: frontend/app/(public)/cart/page.tsx
````typescript
export default function CartPage() {
  return (
    <div className="mx-auto max-w-4xl px-4 py-12">
      <h1 className="text-2xl font-bold text-gray-900">Your Cart</h1>
      <p className="mt-2 text-sm text-gray-600">Items in your shopping cart.</p>
    </div>
  );
}
````

## File: frontend/app/(public)/categories/[slug]/page.tsx
````typescript
export default function CategoryProductsPage({ params }: { params: { slug: string } }) {
  return (
    <div className="mx-auto max-w-4xl px-4 py-12">
      <h1 className="text-2xl font-bold text-gray-900">Category: {params.slug}</h1>
      <p className="mt-2 text-sm text-gray-600">Products in this category.</p>
    </div>
  );
}
````

## File: frontend/app/(public)/categories/page.tsx
````typescript
export default function CategoriesPage() {
  return (
    <div className="mx-auto max-w-4xl px-4 py-12">
      <h1 className="text-2xl font-bold text-gray-900">Categories</h1>
      <p className="mt-2 text-sm text-gray-600">Browse all product categories.</p>
    </div>
  );
}
````

## File: frontend/app/(public)/contact/page.tsx
````typescript
export default function ContactPage() {
  return (
    <div className="mx-auto max-w-4xl px-4 py-12">
      <h1 className="text-2xl font-bold text-gray-900">Contact Us</h1>
      <p className="mt-2 text-sm text-gray-600">Get in touch with our team.</p>
    </div>
  );
}
````

## File: frontend/app/(public)/faq/page.tsx
````typescript
export default function FaqPage() {
  return (
    <div className="mx-auto max-w-4xl px-4 py-12">
      <h1 className="text-2xl font-bold text-gray-900">FAQ</h1>
      <p className="mt-2 text-sm text-gray-600">Frequently asked questions.</p>
    </div>
  );
}
````

## File: frontend/app/(public)/privacy/page.tsx
````typescript
export default function PrivacyPage() {
  return (
    <div className="mx-auto max-w-4xl px-4 py-12">
      <h1 className="text-2xl font-bold text-gray-900">Privacy Policy</h1>
      <p className="mt-2 text-sm text-gray-600">How we handle your data.</p>
    </div>
  );
}
````

## File: frontend/app/(public)/products/[slug]/loading.tsx
````typescript
export default function ProductDetailLoading() {
  return (
    <div className="mx-auto max-w-4xl px-4 py-12 text-sm text-gray-500">Loading product...</div>
  );
}
````

## File: frontend/app/(public)/products/[slug]/page.tsx
````typescript
export default function ProductDetailPage({ params }: { params: { slug: string } }) {
  return (
    <div className="mx-auto max-w-4xl px-4 py-12">
      <h1 className="text-2xl font-bold text-gray-900">Product: {params.slug}</h1>
      <p className="mt-2 text-sm text-gray-600">Product details go here.</p>
    </div>
  );
}
````

## File: frontend/app/(public)/products/loading.tsx
````typescript
export default function ProductsLoading() {
  return (
    <div className="mx-auto max-w-4xl px-4 py-12 text-sm text-gray-500">Loading products...</div>
  );
}
````

## File: frontend/app/(public)/products/page.tsx
````typescript
export default function ProductsPage() {
  return (
    <div className="mx-auto max-w-4xl px-4 py-12">
      <h1 className="text-2xl font-bold text-gray-900">Products</h1>
      <p className="mt-2 text-sm text-gray-600">Browse all products.</p>
    </div>
  );
}
````

## File: frontend/app/(public)/return-policy/page.tsx
````typescript
export default function ReturnPolicyPage() {
  return (
    <div className="mx-auto max-w-4xl px-4 py-12">
      <h1 className="text-2xl font-bold text-gray-900">Return Policy</h1>
      <p className="mt-2 text-sm text-gray-600">Our return and refund policy.</p>
    </div>
  );
}
````

## File: frontend/app/(public)/search/page.tsx
````typescript
export default function SearchPage() {
  return (
    <div className="mx-auto max-w-4xl px-4 py-12">
      <h1 className="text-2xl font-bold text-gray-900">Search Results</h1>
      <p className="mt-2 text-sm text-gray-600">Results matching your search.</p>
    </div>
  );
}
````

## File: frontend/app/(public)/terms/page.tsx
````typescript
export default function TermsPage() {
  return (
    <div className="mx-auto max-w-4xl px-4 py-12">
      <h1 className="text-2xl font-bold text-gray-900">Terms &amp; Conditions</h1>
      <p className="mt-2 text-sm text-gray-600">Terms of use for our store.</p>
    </div>
  );
}
````

## File: frontend/app/(public)/layout.tsx
````typescript
export default function PublicLayout({ children }: { children: React.ReactNode }) {
  return <>{children}</>;
}
````

## File: frontend/app/(public)/loading.tsx
````typescript
export default function PublicLoading() {
  return <div className="mx-auto max-w-4xl px-4 py-12 text-sm text-gray-500">Loading...</div>;
}
````

## File: frontend/app/(public)/page.tsx
````typescript
export default function HomePage() {
  return (
    <div className="mx-auto max-w-4xl px-4 py-12 text-center">
      <h1 className="text-2xl font-bold text-gray-900">E-Commerce Storefront</h1>
      <p className="mt-2 text-sm text-gray-600">Welcome to the store.</p>
      <button className="mt-6 rounded-md bg-gray-900 px-4 py-2 text-sm font-medium text-white hover:bg-gray-800">
        Browse Products
      </button>
    </div>
  );
}
````

## File: frontend/app/globals.css
````css
@import "tailwindcss";

@theme {
  /* Brand Theme Tokens (Tailwind v4 standard configuration syntax) */
  --color-primary: #0f172a;
  --color-secondary: #475569;

  /* The engine automatically scans app/, components/, hooks/, etc. natively */
}
````

## File: frontend/app/page.tsx
````typescript
import React from "react";

export default function HomePage() {
  return (
    <main className="min-h-screen bg-gray-50 flex flex-col items-center justify-center p-6">
      <div className="max-w-md w-full bg-white shadow-md rounded-lg p-8 border border-gray-200">
        <h1 className="text-2xl font-bold text-gray-900 mb-2">E-commerce Storefront</h1>
        <p className="text-gray-600 mb-4">
          Welcome to the Next.js automated code factory enterprise web store instance.
        </p>
        <button className="w-full bg-blue-600 hover:bg-blue-700 text-white font-medium py-2 px-4 rounded transition-colors">
          Browse Products
        </button>
      </div>
    </main>
  );
}
````

## File: frontend/lib/api/cart.ts
````typescript
import { apiClient, ApiError } from "./client";
import { ApiResponse, CartResponseData } from "@/types/api";

const FALLBACK_MESSAGES = {
  get: "We couldn't load your cart right now. Please refresh and try again.",
  add: "We couldn't add that item to your cart. Please try again.",
  update: "We couldn't update that item's quantity. Please try again.",
  remove: "We couldn't remove that item from your cart. Please try again.",
  clear: "We couldn't clear your cart. Please try again.",
} as const;

function toUserFacingError(error: unknown, fallbackMessage: string): ApiError {
  if (error instanceof ApiError) {
    if (error.errorType === "network" || error.errorType === "parse") {
      return new ApiError(error.status, fallbackMessage, error.errorType, error.detail);
    }
    return error;
  }
  return new ApiError(500, fallbackMessage, "network");
}

export async function getCart(signal?: AbortSignal): Promise<ApiResponse<CartResponseData>> {
  try {
    return await apiClient.get<ApiResponse<CartResponseData>>("/cart", { signal });
  } catch (error) {
    throw toUserFacingError(error, FALLBACK_MESSAGES.get);
  }
}

export async function addToCart(
  productId: string,
  quantity: number,
  signal?: AbortSignal
): Promise<ApiResponse<CartResponseData>> {
  try {
    return await apiClient.post<ApiResponse<CartResponseData>>(
      "/cart/items",
      { productId, quantity },
      { signal }
    );
  } catch (error) {
    throw toUserFacingError(error, FALLBACK_MESSAGES.add);
  }
}

export async function updateCartItem(
  itemId: string,
  quantity: number,
  signal?: AbortSignal
): Promise<ApiResponse<CartResponseData>> {
  try {
    return await apiClient.put<ApiResponse<CartResponseData>>(
      `/cart/items/${itemId}`,
      { quantity },
      { signal }
    );
  } catch (error) {
    throw toUserFacingError(error, FALLBACK_MESSAGES.update);
  }
}

export async function removeCartItem(
  itemId: string,
  signal?: AbortSignal
): Promise<ApiResponse<CartResponseData>> {
  try {
    return await apiClient.delete<ApiResponse<CartResponseData>>(`/cart/items/${itemId}`, {
      signal,
    });
  } catch (error) {
    throw toUserFacingError(error, FALLBACK_MESSAGES.remove);
  }
}

export async function clearCart(signal?: AbortSignal): Promise<ApiResponse<null>> {
  try {
    return await apiClient.delete<ApiResponse<null>>("/cart", { signal });
  } catch (error) {
    throw toUserFacingError(error, FALLBACK_MESSAGES.clear);
  }
}
````

## File: frontend/lib/api/orders.ts
````typescript
import { apiClient, ApiError } from "./client";
import { ApiResponse, PaginatedResponse, OrderQueryParams } from "@/types/api";
import { Order } from "@/types/order";

const FALLBACK_MESSAGES = {
  getOrders: "We couldn't load your orders right now. Please try again.",
  getOrderById: "We couldn't load that order right now. Please try again.",
  createOrder: "We couldn't place your order. Please try again.",
  cancelOrder: "We couldn't cancel that order. Please try again.",
  requestOrderReturn: "We couldn't submit your return request. Please try again.",
} as const;

function toUserFacingError(error: unknown, fallbackMessage: string): ApiError {
  if (error instanceof ApiError) {
    if (error.errorType === "network" || error.errorType === "parse") {
      return new ApiError(error.status, fallbackMessage, error.errorType, error.detail);
    }
    return error;
  }
  return new ApiError(500, fallbackMessage, "network");
}

export async function getOrders(
  params?: OrderQueryParams,
  signal?: AbortSignal
): Promise<ApiResponse<PaginatedResponse<Order>>> {
  try {
    const searchParams = new URLSearchParams();
    if (params) {
      Object.entries(params).forEach(([key, value]) => {
        if (value !== undefined && value !== null && value !== "") {
          searchParams.append(key, String(value));
        }
      });
    }
    const query = searchParams.toString() ? `?${searchParams.toString()}` : "";
    return await apiClient.get<ApiResponse<PaginatedResponse<Order>>>(`/orders${query}`, {
      signal,
    });
  } catch (error) {
    throw toUserFacingError(error, FALLBACK_MESSAGES.getOrders);
  }
}

export async function getOrderById(
  orderId: string,
  signal?: AbortSignal
): Promise<ApiResponse<Order>> {
  try {
    return await apiClient.get<ApiResponse<Order>>(`/orders/${orderId}`, { signal });
  } catch (error) {
    throw toUserFacingError(error, FALLBACK_MESSAGES.getOrderById);
  }
}

export async function createOrder(
  orderData: {
    addressId: string;
    paymentIntentId: string;
  },
  signal?: AbortSignal
): Promise<ApiResponse<Order>> {
  try {
    return await apiClient.post<ApiResponse<Order>>("/orders", orderData, { signal });
  } catch (error) {
    throw toUserFacingError(error, FALLBACK_MESSAGES.createOrder);
  }
}

export async function cancelOrder(
  orderId: string,
  reason: string,
  signal?: AbortSignal
): Promise<ApiResponse<Order>> {
  try {
    return await apiClient.post<ApiResponse<Order>>(
      `/orders/${orderId}/cancel`,
      { reason },
      { signal }
    );
  } catch (error) {
    throw toUserFacingError(error, FALLBACK_MESSAGES.cancelOrder);
  }
}

export async function requestOrderReturn(
  orderId: string,
  itemIds: string[],
  reason: string,
  signal?: AbortSignal
): Promise<ApiResponse<Order>> {
  try {
    return await apiClient.post<ApiResponse<Order>>(
      `/orders/${orderId}/return`,
      { itemIds, reason },
      { signal }
    );
  } catch (error) {
    throw toUserFacingError(error, FALLBACK_MESSAGES.requestOrderReturn);
  }
}
````

## File: frontend/lib/api/products.ts
````typescript
import { apiClient, ApiError } from "./client";
import { ApiResponse, PaginatedResponse, ProductQueryParams } from "@/types/api";
import { Product } from "@/types/product";

const FALLBACK_MESSAGES = {
  getProducts: "We couldn't load products right now. Please try again.",
  getProductBySlug: "We couldn't load that product right now. Please try again.",
  getProductById: "We couldn't load that product right now. Please try again.",
  getCategories: "We couldn't load product categories right now. Please try again.",
} as const;

function toUserFacingError(error: unknown, fallbackMessage: string): ApiError {
  if (error instanceof ApiError) {
    if (error.errorType === "network" || error.errorType === "parse") {
      return new ApiError(error.status, fallbackMessage, error.errorType, error.detail);
    }
    return error;
  }
  return new ApiError(500, fallbackMessage, "network");
}

export async function getProducts(
  params?: ProductQueryParams,
  signal?: AbortSignal
): Promise<ApiResponse<PaginatedResponse<Product>>> {
  try {
    const searchParams = new URLSearchParams();
    if (params) {
      Object.entries(params).forEach(([key, value]) => {
        if (value !== undefined && value !== null && value !== "") {
          searchParams.append(key, String(value));
        }
      });
    }
    const query = searchParams.toString() ? `?${searchParams.toString()}` : "";
    return await apiClient.get<ApiResponse<PaginatedResponse<Product>>>(`/products${query}`, {
      signal,
    });
  } catch (error) {
    throw toUserFacingError(error, FALLBACK_MESSAGES.getProducts);
  }
}

export async function getProductBySlug(
  slug: string,
  signal?: AbortSignal
): Promise<ApiResponse<Product>> {
  try {
    return await apiClient.get<ApiResponse<Product>>(`/products/slug/${slug}`, { signal });
  } catch (error) {
    throw toUserFacingError(error, FALLBACK_MESSAGES.getProductBySlug);
  }
}

export async function getProductById(
  id: string,
  signal?: AbortSignal
): Promise<ApiResponse<Product>> {
  try {
    return await apiClient.get<ApiResponse<Product>>(`/products/${id}`, { signal });
  } catch (error) {
    throw toUserFacingError(error, FALLBACK_MESSAGES.getProductById);
  }
}

export async function getCategories(signal?: AbortSignal): Promise<ApiResponse<string[]>> {
  try {
    return await apiClient.get<ApiResponse<string[]>>("/products/categories", { signal });
  } catch (error) {
    throw toUserFacingError(error, FALLBACK_MESSAGES.getCategories);
  }
}
````

## File: frontend/lib/validation/address.ts
````typescript
import { z } from "zod";

export const addressSchema = z.object({
  title: z.string().min(1, "Address label title is required."),
  streetAddress: z.string().min(1, "Street address is required."),
  apartment: z.string().optional(),
  city: z.string().min(1, "City is required."),
  state: z.string().min(1, "State or province is required."),
  postalCode: z.string().min(1, "Postal code is required."),
  country: z.string().min(1, "Country name is required."),
  isDefault: z.boolean().default(false),
});

export type AddressSchemaType = z.infer<typeof addressSchema>;
````

## File: frontend/lib/validation/auth.ts
````typescript
import { z } from "zod";

export const loginSchema = z.object({
  email: z.string().email("Invalid email address format."),
  password: z.string().min(8, "Password must be at least 8 characters long."),
});

export const registerSchema = z.object({
  email: z.string().email("Invalid email address format."),
  password: z.string().min(8, "Password must be at least 8 characters long."),
  firstName: z.string().min(1, "First name is required."),
  lastName: z.string().min(1, "Last name is required."),
});

export const forgotPasswordSchema = z.object({
  email: z.string().email("Invalid email address format."),
});

export const resetPasswordSchema = z
  .object({
    token: z.string().min(1, "Reset token is required."),
    password: z.string().min(8, "Password must be at least 8 characters long."),
    confirmPassword: z.string().min(8, "Confirm password must be at least 8 characters long."),
  })
  .refine((data) => data.password === data.confirmPassword, {
    message: "Passwords must match.",
    path: ["confirmPassword"],
  });

export type LoginSchemaType = z.infer<typeof loginSchema>;
export type RegisterSchemaType = z.infer<typeof registerSchema>;
export type ForgotPasswordSchemaType = z.infer<typeof forgotPasswordSchema>;
export type ResetPasswordSchemaType = z.infer<typeof resetPasswordSchema>;
````

## File: frontend/tests/smoke.test.tsx
````typescript
import React from "react";
import { render, screen } from "@testing-library/react";
import HomePage from "@/app/page";

describe("Next.js Storefront Root Application Smoke Test Suite", () => {
  it("should successfully mount and render the main home page component layout without throwing errors", () => {
    const { container } = render(<HomePage />);

    // Assert structural visibility matches layout expectations
    const headingElement = screen.getByRole("heading", {
      level: 1,
      name: /e-commerce storefront/i,
    });
    expect(headingElement).toBeInTheDocument();

    const actionButton = screen.getByRole("button", { name: /browse products/i });
    expect(actionButton).toBeInTheDocument();

    // Verify container generated real HTML rendering paths
    expect(container.firstChild).toBeInTheDocument();
  });
});
````

## File: frontend/types/address.ts
````typescript
// Mirrors: app/schemas/address.py

export interface Address {
  id: number;
  customerId: number;
  country: string;
  state: string | null;
  city: string;
  postalCode: string | null;
  addressLine1: string;
  addressLine2: string | null;
  isDefault: boolean;
  createdAt: string;
  updatedAt: string;
}

export interface AddressCreate {
  country: string;
  state?: string | null;
  city: string;
  postalCode?: string | null;
  addressLine1: string;
  addressLine2?: string | null;
  isDefault?: boolean;
}

export interface AddressUpdate {
  country?: string;
  state?: string;
  city?: string;
  postalCode?: string;
  addressLine1?: string;
  addressLine2?: string;
  isDefault?: boolean;
}
````

## File: frontend/tsconfig.json
````json
{
  "compilerOptions": {
    "target": "ES2020",
    "lib": [
      "dom",
      "dom.iterable",
      "esnext"
    ],
    "allowJs": true,
    "skipLibCheck": true,
    "strict": true,
    "noEmit": true,
    "esModuleInterop": true,
    "module": "esnext",
    "moduleResolution": "bundler",
    "resolveJsonModule": true,
    "isolatedModules": true,
    "jsx": "react-jsx",
    "incremental": true,
    "plugins": [
      {
        "name": "next"
      }
    ],
    "paths": {
      "@/*": [
        "./*"
      ]
    }
  },
  "include": [
    "next-env.d.ts",
    "**/*.ts",
    "**/*.tsx",
    ".next/types/**/*.ts",
    ".next/dev/types/**/*.ts"
  ],
  "exclude": [
    "node_modules"
  ]
}
````

## File: backend/app/api/routes/categories.py
````python
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.session import get_db
from app.models.category import Category
from app.models.user import User
from app.schemas.category import CategoryOut, CategoryCreate, CategoryUpdate
from app.core.permissions import require_role, ADMIN, MANAGER, STAFF

router = APIRouter()


@router.get("/categories", response_model=list[CategoryOut])
async def get_categories(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER, STAFF))
):
    result = await db.execute(select(Category))
    return result.scalars().all()


@router.get("/categories/{category_id}", response_model=CategoryOut)
async def get_category(
    category_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER, STAFF))
):
    result = await db.execute(select(Category).where(Category.id == category_id))
    category = result.scalar_one_or_none()
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category


@router.post("/categories", response_model=CategoryOut, status_code=201)
async def create_category(
    payload: CategoryCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER, STAFF))
):
    result = await db.execute(select(Category).where(Category.name == payload.name))
    existing = result.scalar_one_or_none()
    if existing:
        raise HTTPException(status_code=400, detail="Category name already exists")

    new_category = Category(
        name=payload.name,
        description=payload.description,
    )
    db.add(new_category)
    await db.commit()
    await db.refresh(new_category)
    return new_category


@router.put("/categories/{category_id}", response_model=CategoryOut)
async def update_category(
    category_id: int,
    payload: CategoryUpdate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER, STAFF))
):
    result = await db.execute(select(Category).where(Category.id == category_id))
    category = result.scalar_one_or_none()
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")

    update_data = payload.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(category, field, value)

    await db.commit()
    await db.refresh(category)
    return category


@router.delete("/categories/{category_id}", status_code=204)
async def delete_category(
    category_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER, STAFF))
):
    result = await db.execute(select(Category).where(Category.id == category_id))
    category = result.scalar_one_or_none()
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")

    await db.delete(category)
    await db.commit()
    return None
````

## File: backend/app/api/routes/customer_auth.py
````python
import secrets
from datetime import datetime, timedelta, timezone

from fastapi import APIRouter, Depends, HTTPException, Request, Response, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError

from app.database.session import get_db
from app.models.user import User
from app.models.customer_profile import CustomerProfile
from app.schemas.customer_auth import (
    CustomerRegisterRequest,
    CustomerRegisterResponse,
    CustomerLoginRequest,
    CustomerAuthResponse,
    CustomerRefreshRequest,
    CustomerVerifyEmailRequest,
    CustomerResendVerificationRequest,
    CustomerForgotPasswordRequest,
    CustomerResetPasswordRequest,
    MsgResponse,
)
from app.core.security import hash_password, verify_password
from app.core.jwt import create_access_token, create_refresh_token
from app.core.email import send_verification_email, send_password_reset_email
from app.core.auth import get_current_user
from app.schemas.customer_profile import CustomerProfileOut

router = APIRouter(prefix="/customer/auth", tags=["Customer Auth"])

CUSTOMER_ROLE_ID = 4
VERIFICATION_TOKEN_EXPIRE_HOURS = 24
RESET_TOKEN_EXPIRE_HOURS = 1
ACCESS_COOKIE_NAME = "access_token"
REFRESH_COOKIE_NAME = "refresh_token"
COOKIE_MAX_AGE_SECONDS = 60 * 60 * 24 * 7


def _set_auth_cookies(response: Response, access_token: str, refresh_token: str) -> None:
    response.set_cookie(
        key=ACCESS_COOKIE_NAME,
        value=access_token,
        httponly=True,
        secure=False,
        samesite="lax",
        max_age=60 * 60 * 24,
        path="/",
    )
    response.set_cookie(
        key=REFRESH_COOKIE_NAME,
        value=refresh_token,
        httponly=True,
        secure=False,
        samesite="lax",
        max_age=COOKIE_MAX_AGE_SECONDS,
        path="/",
    )


def _clear_auth_cookies(response: Response) -> None:
    response.delete_cookie(ACCESS_COOKIE_NAME, path="/")
    response.delete_cookie(REFRESH_COOKIE_NAME, path="/")


def _issue_tokens(user: User) -> tuple[str, str]:
    access_token = create_access_token(
        {"sub": str(user.id), "email": user.email, "role_id": user.role_id}
    )
    refresh_token, refresh_expires_at = create_refresh_token()
    user.refresh_token = refresh_token
    user.refresh_token_expires_at = refresh_expires_at
    return access_token, refresh_token


@router.post("/register", response_model=CustomerRegisterResponse, status_code=status.HTTP_201_CREATED)
async def customer_register(payload: CustomerRegisterRequest, db: AsyncSession = Depends(get_db)):
    stmt = select(User).where(User.email == payload.email)
    result = await db.execute(stmt)
    existing = result.scalar_one_or_none()
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")

    verification_token = secrets.token_urlsafe(32)

    new_user = User(
        name=payload.name,
        email=payload.email,
        password=hash_password(payload.password),
        phone_number=payload.phone_number,
        role_id=CUSTOMER_ROLE_ID,
        is_active=True,
        email_verified=False,
        email_verification_token=verification_token,
        email_verification_expires_at=datetime.now(timezone.utc) + timedelta(hours=VERIFICATION_TOKEN_EXPIRE_HOURS),
    )
    db.add(new_user)

    try:
        await db.commit()
    except IntegrityError:
        await db.rollback()
        raise HTTPException(status_code=400, detail="Could not create account")

    await db.refresh(new_user)

    profile = CustomerProfile(user_id=new_user.id)
    db.add(profile)
    await db.commit()

    send_verification_email(new_user.email, verification_token)

    return CustomerRegisterResponse(
        id=new_user.id,
        name=new_user.name,
        email=new_user.email,
        email_verified=new_user.email_verified,
        message="Account created. Check your email to verify your account.",
    )


@router.post("/login", response_model=CustomerAuthResponse)
async def customer_login(
    payload: CustomerLoginRequest,
    response: Response,
    db: AsyncSession = Depends(get_db),
):
    stmt = select(User).where(User.email == payload.email)
    result = await db.execute(stmt)
    user = result.scalar_one_or_none()

    if not user or user.role_id != CUSTOMER_ROLE_ID:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid email or password")

    if not verify_password(payload.password, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid email or password")

    if not user.is_active:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Account is inactive")

    access_token, refresh_token = _issue_tokens(user)
    _set_auth_cookies(response, access_token, refresh_token)
    await db.commit()

    return CustomerAuthResponse(message="Logged in successfully.")


@router.post("/refresh", response_model=CustomerAuthResponse)
async def customer_refresh(
    request: Request,
    response: Response,
    db: AsyncSession = Depends(get_db),
):
    refresh_token = request.cookies.get(REFRESH_COOKIE_NAME)
    if not refresh_token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid refresh token")

    stmt = select(User).where(User.refresh_token == refresh_token)
    result = await db.execute(stmt)
    user = result.scalar_one_or_none()

    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid refresh token")

    if not user.refresh_token_expires_at or user.refresh_token_expires_at < datetime.now(timezone.utc):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Refresh token expired")

    if not user.is_active:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Account is inactive")

    access_token, refresh_token = _issue_tokens(user)  # rotates refresh token
    _set_auth_cookies(response, access_token, refresh_token)
    await db.commit()

    return CustomerAuthResponse(message="Session refreshed successfully.")


@router.post("/logout", response_model=MsgResponse)
async def customer_logout(
    request: Request,
    response: Response,
    db: AsyncSession = Depends(get_db),
):
    refresh_token = request.cookies.get(REFRESH_COOKIE_NAME)
    stmt = select(User).where(User.refresh_token == refresh_token)
    result = await db.execute(stmt)
    user = result.scalar_one_or_none()

    if user:
        user.refresh_token = None
        user.refresh_token_expires_at = None
        await db.commit()

    _clear_auth_cookies(response)
    return MsgResponse(message="Logged out successfully.")


@router.get("/me", response_model=CustomerProfileOut)
async def customer_me(current_user: User = Depends(get_current_user)):
    return CustomerProfileOut(
        id=current_user.id,
        name=current_user.name,
        email=current_user.email,
        phone_number=current_user.phone_number,
        avatar_url=current_user.avatar_url,
        email_verified=current_user.email_verified,
        created_at=current_user.created_at,
    )


@router.post("/verify-email", response_model=MsgResponse)
async def customer_verify_email(payload: CustomerVerifyEmailRequest, db: AsyncSession = Depends(get_db)):
    stmt = select(User).where(User.email_verification_token == payload.token)
    result = await db.execute(stmt)
    user = result.scalar_one_or_none()

    if not user:
        raise HTTPException(status_code=400, detail="Invalid or expired verification link")

    if (
        not user.email_verification_expires_at
        or user.email_verification_expires_at < datetime.now(timezone.utc)
    ):
        raise HTTPException(status_code=400, detail="Invalid or expired verification link")

    user.email_verified = True
    user.email_verification_token = None
    user.email_verification_expires_at = None
    await db.commit()

    return MsgResponse(message="Email verified successfully. You can now log in.")


@router.post("/resend-verification", response_model=MsgResponse)
async def customer_resend_verification(payload: CustomerResendVerificationRequest, db: AsyncSession = Depends(get_db)):
    stmt = select(User).where(User.email == payload.email, User.role_id == CUSTOMER_ROLE_ID)
    result = await db.execute(stmt)
    user = result.scalar_one_or_none()

    generic_response = MsgResponse(message="If that email exists and is unverified, a new link has been sent.")

    if not user or user.email_verified:
        return generic_response

    token = secrets.token_urlsafe(32)
    user.email_verification_token = token
    user.email_verification_expires_at = datetime.now(timezone.utc) + timedelta(hours=VERIFICATION_TOKEN_EXPIRE_HOURS)
    await db.commit()

    send_verification_email(user.email, token)

    return generic_response


@router.post("/forgot-password", response_model=MsgResponse)
async def customer_forgot_password(payload: CustomerForgotPasswordRequest, db: AsyncSession = Depends(get_db)):
    stmt = select(User).where(User.email == payload.email, User.role_id == CUSTOMER_ROLE_ID)
    result = await db.execute(stmt)
    user = result.scalar_one_or_none()

    generic_response = MsgResponse(message="If that email exists, a password reset link has been sent.")

    if not user or not user.is_active:
        return generic_response

    token = secrets.token_urlsafe(32)
    user.password_reset_token = token
    user.password_reset_expires_at = datetime.now(timezone.utc) + timedelta(hours=RESET_TOKEN_EXPIRE_HOURS)
    await db.commit()

    send_password_reset_email(user.email, token)

    return generic_response


@router.post("/reset-password", response_model=MsgResponse)
async def customer_reset_password(payload: CustomerResetPasswordRequest, db: AsyncSession = Depends(get_db)):
    stmt = select(User).where(User.password_reset_token == payload.token, User.role_id == CUSTOMER_ROLE_ID)
    result = await db.execute(stmt)
    user = result.scalar_one_or_none()

    if not user:
        raise HTTPException(status_code=400, detail="Invalid or expired token")

    if (
        not user.password_reset_expires_at
        or user.password_reset_expires_at < datetime.now(timezone.utc)
    ):
        raise HTTPException(status_code=400, detail="Invalid or expired token")

    if not user.is_active:
        raise HTTPException(status_code=403, detail="Account is inactive")

    user.password = hash_password(payload.new_password)
    user.password_reset_token = None
    user.password_reset_expires_at = None
    await db.commit()

    return MsgResponse(message="Password reset successfully. Please log in with your new password.")
````

## File: backend/app/api/routes/customer_profiles.py
````python
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.database.session import get_db
from app.models.user import User
from app.models.address import Address
from app.schemas.customer_profile import CustomerProfileOut, CustomerProfileUpdate
from app.schemas.address import AddressCreate, AddressUpdate, AddressOut
from app.core.auth import get_current_user

router = APIRouter(prefix="/customer/profile", tags=["Customer Profile"])


@router.get("/me", response_model=CustomerProfileOut)
async def get_customer_profile(current_user: User = Depends(get_current_user)):
    return CustomerProfileOut(
        id=current_user.id,
        name=current_user.name,
        email=current_user.email,
        phone_number=current_user.phone_number,
        avatar_url=current_user.avatar_url,
        email_verified=current_user.email_verified,
        created_at=current_user.created_at,
    )


@router.put("/me", response_model=CustomerProfileOut)
async def update_customer_profile(
    payload: CustomerProfileUpdate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    update_data = payload.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(current_user, field, value)

    await db.commit()
    await db.refresh(current_user)

    return CustomerProfileOut(
        id=current_user.id,
        name=current_user.name,
        email=current_user.email,
        phone_number=current_user.phone_number,
        avatar_url=current_user.avatar_url,
        email_verified=current_user.email_verified,
        created_at=current_user.created_at,
    )


@router.get("/addresses", response_model=list[AddressOut])
async def list_addresses(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    stmt = select(Address).where(Address.customer_id == current_user.customer_profile.id)
    result = await db.execute(stmt)
    return list(result.scalars().all())


@router.post("/addresses", response_model=AddressOut, status_code=status.HTTP_201_CREATED)
async def create_address(
    payload: AddressCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    if payload.is_default:
        stmt = select(Address).where(Address.customer_id == current_user.customer_profile.id)
        result = await db.execute(stmt)
        for existing in result.scalars().all():
            existing.is_default = False

    address = Address(customer_id=current_user.customer_profile.id, **payload.dict())
    db.add(address)
    await db.commit()
    await db.refresh(address)
    return address


@router.put("/addresses/{address_id}", response_model=AddressOut)
async def update_address(
    address_id: int,
    payload: AddressUpdate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    stmt = select(Address).where(
        Address.id == address_id, Address.customer_id == current_user.customer_profile.id
    )
    result = await db.execute(stmt)
    address = result.scalar_one_or_none()

    if not address:
        raise HTTPException(status_code=404, detail="Address not found")

    update_data = payload.dict(exclude_unset=True)

    if update_data.get("is_default"):
        stmt = select(Address).where(
            Address.customer_id == current_user.customer_profile.id,
            Address.id != address_id,
        )
        result = await db.execute(stmt)
        for other in result.scalars().all():
            other.is_default = False

    for field, value in update_data.items():
        setattr(address, field, value)

    await db.commit()
    await db.refresh(address)
    return address


@router.delete("/addresses/{address_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_address(
    address_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    stmt = select(Address).where(
        Address.id == address_id, Address.customer_id == current_user.customer_profile.id
    )
    result = await db.execute(stmt)
    address = result.scalar_one_or_none()

    if not address:
        raise HTTPException(status_code=404, detail="Address not found")

    await db.delete(address)
    await db.commit()
    return None
````

## File: backend/app/api/routes/payments.py
````python
import stripe
from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.core.auth import get_current_user
from app.core.config import settings
from app.database.session import get_db
from app.models.cart import Cart
from app.models.cart_item import CartItem
from app.models.customer_profile import CustomerProfile
from app.models.order import Order
from app.models.order_item import OrderItem
from app.models.product_variant import ProductVariant
from app.models.user import User

router = APIRouter()

stripe.api_key = settings.STRIPE_SECRET_KEY  # <-- FLAG: pulled from Settings, confirm STRIPE_SECRET_KEY is set in .env

_CART_ITEM_LOAD = selectinload(Cart.items).selectinload(CartItem.product_variant)


async def _get_or_create_customer_profile(db: AsyncSession, user: User) -> CustomerProfile:
    result = await db.execute(select(CustomerProfile).where(CustomerProfile.user_id == user.id))
    profile = result.scalar_one_or_none()
    if not profile:
        profile = CustomerProfile(user_id=user.id)
        db.add(profile)
        await db.commit()
        await db.refresh(profile)
    return profile


async def _validate_cart_stock(db: AsyncSession, cart: Cart) -> float:
    """Validates stock for every line item, returns computed total."""
    total = 0.0
    for item in cart.items:
        result = await db.execute(
            select(ProductVariant).where(ProductVariant.id == item.product_variant_id)
        )
        variant = result.scalar_one_or_none()
        if not variant or not variant.is_active:
            raise HTTPException(
                status_code=400,
                detail=f"Product variant {item.product_variant_id} is no longer available",
            )
        if variant.stock_quantity < item.quantity:
            raise HTTPException(
                status_code=400,
                detail=f"Insufficient stock for SKU '{variant.sku}': only {variant.stock_quantity} available",
            )
        total += float(variant.price) * item.quantity
    return total


@router.post("/payments/create-intent")
async def create_payment_intent(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    profile = await _get_or_create_customer_profile(db, current_user)

    result = await db.execute(
        select(Cart).options(_CART_ITEM_LOAD).where(Cart.customer_id == profile.id)
    )
    cart = result.scalar_one_or_none()
    if not cart or not cart.items:
        raise HTTPException(status_code=400, detail="Cart is empty")

    total = await _validate_cart_stock(db, cart)
    if total <= 0:
        raise HTTPException(status_code=400, detail="Invalid cart total")

    amount_in_cents = int(round(total * 100))

    intent = stripe.PaymentIntent.create(
        amount=amount_in_cents,
        currency="usd",  # <-- FLAG: confirm currency; hardcoded for now
        metadata={
            "cart_id": str(cart.id),
            "customer_id": str(profile.id),
        },
        automatic_payment_methods={"enabled": True},
    )

    return {"client_secret": intent.client_secret}

async def _create_order_from_cart(db: AsyncSession, cart_id: int, customer_id: int) -> None:
    result = await db.execute(
        select(Cart)
        .options(_CART_ITEM_LOAD)
        .where(Cart.id == cart_id, Cart.customer_id == customer_id)
        .with_for_update()
        .execution_options(populate_existing=True)
    )
    cart = result.scalar_one_or_none()
    if not cart or not cart.items:
        return

    result = await db.execute(select(CustomerProfile).where(CustomerProfile.id == customer_id))
    profile = result.scalar_one_or_none()
    if not profile:
        return

    new_order = Order(
        customer_id=profile.id,
        order_status="paid",
        total_amount=0,
    )
    db.add(new_order)
    await db.flush()

    total = 0.0
    for item in cart.items:
        result = await db.execute(
            select(ProductVariant).where(ProductVariant.id == item.product_variant_id)
        )
        variant = result.scalar_one_or_none()
        if not variant:
            continue

        price = float(variant.price)
        db.add(OrderItem(
            order_id=new_order.id,
            product_variant_id=variant.id,
            quantity=item.quantity,
            price_at_purchase=price,
        ))
        variant.stock_quantity -= item.quantity
        total += price * item.quantity

    new_order.total_amount = total

    for item in list(cart.items):
        cart.items.remove(item)
        await db.delete(item)

    await db.commit()


@router.post("/payments/webhook")
async def stripe_webhook(request: Request, db: AsyncSession = Depends(get_db)):
    payload = await request.body()
    sig_header = request.headers.get("stripe-signature")

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.STRIPE_WEBHOOK_SECRET  # <-- FLAG: pulled from Settings, confirm STRIPE_WEBHOOK_SECRET is set in .env
        )
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid payload")
    except stripe.error.SignatureVerificationError:
        raise HTTPException(status_code=400, detail="Invalid signature")

    if event["type"] == "payment_intent.succeeded":
        intent = event["data"]["object"]
        metadata = intent.get("metadata", {})
        cart_id = metadata.get("cart_id")
        customer_id = metadata.get("customer_id")

        if cart_id and customer_id:
            await _create_order_from_cart(db, int(cart_id), int(customer_id))

    return {"status": "success"}
````

## File: backend/app/api/routes/users.py
````python
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from sqlalchemy.exc import IntegrityError

from app.database.session import get_db
from app.models.user import User
from app.schemas.user import UserOut, UserCreate, UserUpdate
from app.core.security import hash_password
from app.core.permissions import require_role, block_manager_on_admin_target, ADMIN, MANAGER
from app.core.auth import get_current_user_optional

router = APIRouter()

CUSTOMER_ROLE_ID = 4


@router.get("/users", response_model=list[UserOut])
async def get_users(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER))
):
    result = await db.execute(select(User).options(selectinload(User.role)))
    return result.scalars().all()


@router.post("/users", response_model=UserOut, status_code=201)
async def create_user(
    payload: UserCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User | None = Depends(get_current_user_optional)
):
    stmt = select(User).where(User.email == payload.email)
    result = await db.execute(stmt)
    existing = result.scalar_one_or_none()
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")

    if current_user is not None and current_user.role_id == 1:
        final_role_id = payload.role_id
    else:
        final_role_id = CUSTOMER_ROLE_ID

    new_user = User(
        name=payload.name,
        email=payload.email,
        password=hash_password(payload.password),
        phone_number=payload.phone_number,
        avatar_url=payload.avatar_url,
        role_id=final_role_id,
        is_active=payload.is_active,
    )

    db.add(new_user)

    try:
        await db.commit()
    except IntegrityError:
        await db.rollback()
        raise HTTPException(status_code=400, detail="Invalid role_id: role does not exist")

    stmt = (
        select(User)
        .options(selectinload(User.role))
        .where(User.id == new_user.id)
    )
    result = await db.execute(stmt)
    created_user = result.scalar_one()

    return created_user


@router.put("/users/{user_id}", response_model=UserOut)
async def update_user(
    user_id: int,
    payload: UserUpdate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER))
):
    stmt = select(User).where(User.id == user_id)
    result = await db.execute(stmt)
    user = result.scalar_one_or_none()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    block_manager_on_admin_target(current_user, user.role_id)

    update_data = payload.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(user, field, value)

    try:
        await db.commit()
    except IntegrityError:
        await db.rollback()
        raise HTTPException(status_code=400, detail="Invalid role_id: role does not exist")

    stmt = (
        select(User)
        .options(selectinload(User.role))
        .where(User.id == user_id)
    )
    result = await db.execute(stmt)
    updated_user = result.scalar_one()

    return updated_user


@router.delete("/users/{user_id}", status_code=204)
async def delete_user(
    user_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN))
):
    stmt = select(User).where(User.id == user_id)
    result = await db.execute(stmt)
    user = result.scalar_one_or_none()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    await db.delete(user)
    await db.commit()
    return None
````

## File: backend/app/core/config.py
````python
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    SMTP_HOST: str = "sandbox.smtp.mailtrap.io"
    SMTP_PORT: int = 587
    SMTP_USERNAME: str = "PLACEHOLDER_USERNAME"
    SMTP_PASSWORD: str = "PLACEHOLDER_PASSWORD"
    FROM_EMAIL: str = "no-reply@yourapp.com"
    FRONTEND_URL: str = "https://yourapp.com"

    STRIPE_SECRET_KEY: str
    STRIPE_WEBHOOK_SECRET: str

    TEST_MODE: bool = False

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True
    )


settings = Settings()
````

## File: backend/app/database/base.py
````python
from typing import Any
from sqlalchemy.orm import DeclarativeBase, declared_attr

class Base(DeclarativeBase):
    id: Any
    __name__: str


    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()
````

## File: backend/app/models/cart_item.py
````python
from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Integer, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class CartItem(Base):
    __tablename__ = "cart_items"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    cart_id: Mapped[int] = mapped_column(ForeignKey("carts.id", ondelete="CASCADE"), nullable=False)
    product_variant_id: Mapped[int] = mapped_column(ForeignKey("product_variants.id"), nullable=False)

    quantity: Mapped[int] = mapped_column(Integer, nullable=False, default=1)

    created_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now()
    )
    updated_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )

    # Relationships
    cart: Mapped["Cart"] = relationship(back_populates="items")
    product_variant: Mapped["ProductVariant"] = relationship()
````

## File: backend/app/schemas/customer_auth.py
````python
from datetime import datetime
from pydantic import BaseModel, EmailStr, Field


class CustomerRegisterRequest(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    email: EmailStr
    password: str = Field(min_length=8)
    phone_number: str | None = None


class CustomerRegisterResponse(BaseModel):
    id: int
    name: str
    email: str
    email_verified: bool
    message: str


class CustomerLoginRequest(BaseModel):
    email: EmailStr
    password: str


class CustomerToken(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str


class CustomerAuthResponse(BaseModel):
    message: str


class CustomerRefreshRequest(BaseModel):
    refresh_token: str


class CustomerVerifyEmailRequest(BaseModel):
    token: str


class CustomerResendVerificationRequest(BaseModel):
    email: EmailStr


class CustomerForgotPasswordRequest(BaseModel):
    email: EmailStr


class CustomerResetPasswordRequest(BaseModel):
    token: str
    new_password: str = Field(min_length=8)


class MsgResponse(BaseModel):
    message: str
````

## File: backend/app/seed.py
````python
import uuid
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.database.session import AsyncSessionLocal
from app.models.role import Role
from app.models.user import User
from app.models.permission import Permission
from app.models.role_permission import RolePermission
from app.core.security import hash_password

RESOURCES = [
    "users", "roles", "permissions",
    "categories", "products", "product_categories",
    "product_variants", "orders", "order_items"
]
ACTIONS = ["create", "read", "update", "delete"]

# Updated to include our storefront target
ROLES = ["admin", "manager", "staff", "customer"]

ROLE_ACTIONS = {
    "admin": ["create", "read", "update", "delete"],
    "manager": ["create", "read", "update"],
    "staff": ["read"],
    "customer": ["read"], # Storefront customers can only view catalog items natively
}

async def get_or_create_role(db: AsyncSession, name: str, description: str) -> Role:
    result = await db.execute(select(Role).filter(Role.name == name))
    role = result.scalar_one_or_none()
    if not role:
        role = Role(id=uuid.uuid4(), name=name, description=description)
        db.add(role)
        await db.commit()
        await db.refresh(role)
        print(f"Created role: {role.name} (id={role.id})")
    else:
        print(f"Role already exists: {role.name} (id={role.id})")
    return role

async def get_or_create_permission(db: AsyncSession, name: str, description: str) -> Permission:
    result = await db.execute(select(Permission).filter(Permission.name == name))
    perm = result.scalar_one_or_none()
    if not perm:
        perm = Permission(id=uuid.uuid4(), name=name, description=description)
        db.add(perm)
        await db.commit()
        await db.refresh(perm)
    return perm

async def link_role_permission(db: AsyncSession, role_id: uuid.UUID, permission_id: uuid.UUID) -> None:
    result = await db.execute(
        select(RolePermission).filter(
            RolePermission.role_id == role_id,
            RolePermission.permission_id == permission_id
        )
    )
    exists = result.scalar_one_or_none()
    if not exists:
        db.add(RolePermission(id=uuid.uuid4(), role_id=role_id, permission_id=permission_id))

async def seed_database(db: AsyncSession) -> None:
    """
    Idempotent asynchronous database seeder managing RBAC systems
    and the Customer tier.
    """
    print("Checking database for seed records...")

    # 1. Create all roles asynchronously
    role_objs = {}
    for role_name in ROLES:
        role_objs[role_name] = await get_or_create_role(
            db, role_name, f"{role_name.capitalize()} role"
        )

    # 2. Create all permissions (resource:action)
    permission_objs = {}
    for resource in RESOURCES:
        for action in ACTIONS:
            perm_name = f"{resource}:{action}"
            permission_objs[perm_name] = await get_or_create_permission(
                db, perm_name, f"Can {action} {resource}"
            )
    await db.commit()
    print(f"Ensured {len(permission_objs)} permissions exist")

    # 3. Link roles to permissions
    for role_name, allowed_actions in ROLE_ACTIONS.items():
        role = role_objs[role_name]
        for resource in RESOURCES:
            for action in allowed_actions:
                perm_name = f"{resource}:{action}"
                await link_role_permission(db, role.id, permission_objs[perm_name].id)
    await db.commit()
    print("Linked role-permission mappings")

    # 4. Create admin user
    admin_email = "admin@rbac.com"
    user_query = await db.execute(select(User).filter(User.email == admin_email))
    admin_user = user_query.scalar_one_or_none()

    if not admin_user:
        admin_user = User(
            id=uuid.uuid4(),
            full_name="Admin",
            email=admin_email,
            hashed_password=hash_password("Admin123!"),
            is_active=True,
            role_id=role_objs["admin"].id
        )
        db.add(admin_user)
        await db.commit()
        await db.refresh(admin_user)
        print(f"Created user: {admin_user.email} (id={admin_user.id})")
    else:
        print(f"User already exists: {admin_user.email} (id={admin_user.id})")

    print("Seeding checks complete!")

async def run_seed_cli() -> None:
    """Entry point for manual execution via terminal"""
    async with AsyncSessionLocal() as session:
        await seed_database(session)

if __name__ == "__main__":
    import asyncio
    asyncio.run(run_seed_cli())
````

## File: backend/requirements.txt
````
alembic==1.18.5
annotated-doc==0.0.4
annotated-types==0.7.0
anyio==4.14.1
bcrypt==5.0.0
cffi==2.0.0
click==8.4.2
colorama==0.4.6
cryptography==49.0.0
dnspython==2.8.0
ecdsa==0.19.2
email-validator==2.3.0
fastapi==0.139.0
greenlet==3.5.3
h11==0.16.0
idna==3.18
Mako==1.3.12
MarkupSafe==3.0.3
psycopg==3.3.4
psycopg-binary==3.3.4
pyasn1==0.6.3
pycparser==3.0
pydantic==2.13.4
pydantic-settings==2.14.2
pydantic_core==2.46.4
python-dotenv==1.2.2
python-jose==3.5.0
rsa==4.9.1
six==1.17.0
SQLAlchemy==2.0.51
starlette==1.3.1
typing-inspection==0.4.2
typing_extensions==4.16.0
tzdata==2026.2
uvicorn==0.49.0
stripe
````

## File: frontend/lib/api/client.ts
````typescript
import { ApiErrorResponse } from "@/types/api";

export type ApiErrorType = "http" | "parse" | "network" | "abort";

export class ApiError extends Error {
  status: number;
  detail: string | Array<{ loc: (string | number)[]; msg: string; type: string }> | null;
  errorType: ApiErrorType;

  constructor(
    status: number,
    message: string,
    errorType: ApiErrorType,
    detail: string | Array<{ loc: (string | number)[]; msg: string; type: string }> | null = null
  ) {
    super(message);
    this.name = "ApiError";
    this.status = status;
    this.errorType = errorType;
    this.detail = detail;
  }
}

const BASE_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000/api/v1";
const DEFAULT_TIMEOUT_MS = 15000;

let refreshPromise: Promise<void> | null = null;

async function refreshAccessToken(): Promise<void> {
  if (refreshPromise) {
    return refreshPromise;
  }

  refreshPromise = (async () => {
    const response = await fetch(`${BASE_URL}/customer/auth/refresh`, {
      method: "POST",
      credentials: "include",
      headers: { "Content-Type": "application/json" },
    });

    if (!response.ok) {
      throw new ApiError(response.status, "Session expired. Please log in again.", "http");
    }
  })();

  try {
    await refreshPromise;
  } finally {
    refreshPromise = null;
  }
}

interface RequestOptions extends RequestInit {
  timeoutMs?: number;
  signal?: AbortSignal;
  skipAuthRetry?: boolean;
}

async function parseResponseBody(response: Response): Promise<unknown> {
  const contentType = response.headers.get("Content-Type");
  const isJson = contentType !== null && contentType.includes("application/json");
  const rawText = await response.text();

  if (rawText.length === 0) {
    return null;
  }

  if (isJson) {
    try {
      return JSON.parse(rawText);
    } catch {
      throw new ApiError(
        response.status,
        "The server returned a malformed response. Please try again.",
        "parse"
      );
    }
  }

  return rawText;
}

async function request<T>(endpoint: string, options: RequestOptions = {}): Promise<T> {
  const {
    timeoutMs = DEFAULT_TIMEOUT_MS,
    signal: externalSignal,
    skipAuthRetry,
    ...init
  } = options;

  const url = `${BASE_URL}${endpoint}`;

  const headers = new Headers(init.headers);
  if (!(init.body instanceof FormData) && !headers.has("Content-Type")) {
    headers.set("Content-Type", "application/json");
  }

  const timeoutController = new AbortController();
  const timeoutId = setTimeout(() => timeoutController.abort(), timeoutMs);

  const onExternalAbort = () => timeoutController.abort();
  if (externalSignal) {
    if (externalSignal.aborted) {
      timeoutController.abort();
    } else {
      externalSignal.addEventListener("abort", onExternalAbort);
    }
  }

  const config: RequestInit = {
    ...init,
    headers,
    credentials: "include",
    signal: timeoutController.signal,
  };

  try {
    let response: Response;
    try {
      response = await fetch(url, config);
    } catch (fetchError) {
      if (fetchError instanceof DOMException && fetchError.name === "AbortError") {
        if (externalSignal?.aborted) {
          throw new ApiError(0, "Request was cancelled.", "abort");
        }
        throw new ApiError(0, "The request timed out. Please try again.", "network");
      }
      throw new ApiError(0, "Unable to reach the server. Check your connection.", "network");
    }

    if (response.status === 204) {
      return {} as T;
    }

    if (
      response.status === 401 &&
      !skipAuthRetry &&
      endpoint !== "/customer/auth/refresh" &&
      endpoint !== "/auth/refresh"
    ) {
      try {
        await refreshAccessToken();
      } catch {
        throw new ApiError(401, "Your session has expired. Please log in again.", "http");
      }
      return request<T>(endpoint, { ...options, skipAuthRetry: true });
    }

    const responseData = await parseResponseBody(response);

    if (!response.ok) {
      const errorData = responseData as ApiErrorResponse | null;
      let errorMessage = "An unexpected error occurred. Please try again.";

      if (errorData && typeof errorData.detail === "string") {
        errorMessage = errorData.detail;
      } else if (errorData && Array.isArray(errorData.detail)) {
        errorMessage = errorData.detail.map((err) => `${err.loc.join(".")}: ${err.msg}`).join(", ");
      } else if (errorData && errorData.message) {
        errorMessage = errorData.message;
      }

      throw new ApiError(response.status, errorMessage, "http", errorData?.detail ?? null);
    }

    return responseData as T;
  } finally {
    clearTimeout(timeoutId);
    if (externalSignal) {
      externalSignal.removeEventListener("abort", onExternalAbort);
    }
  }
}

export const apiClient = {
  get: <T>(endpoint: string, options?: RequestOptions): Promise<T> =>
    request<T>(endpoint, { ...options, method: "GET" }),
  post: <T>(endpoint: string, body?: unknown, options?: RequestOptions): Promise<T> =>
    request<T>(endpoint, {
      ...options,
      method: "POST",
      body: body instanceof FormData ? body : JSON.stringify(body ?? {}),
    }),
  put: <T>(endpoint: string, body?: unknown, options?: RequestOptions): Promise<T> =>
    request<T>(endpoint, {
      ...options,
      method: "PUT",
      body: body instanceof FormData ? body : JSON.stringify(body ?? {}),
    }),
  patch: <T>(endpoint: string, body?: unknown, options?: RequestOptions): Promise<T> =>
    request<T>(endpoint, {
      ...options,
      method: "PATCH",
      body: body instanceof FormData ? body : JSON.stringify(body ?? {}),
    }),
  delete: <T>(endpoint: string, options?: RequestOptions): Promise<T> =>
    request<T>(endpoint, { ...options, method: "DELETE" }),
};
````

## File: frontend/lib/api/users.ts
````typescript
import { apiClient, ApiError } from "./client";
import { CustomerProfile, CustomerProfileUpdate } from "@/types/user";
import { Address, AddressCreate, AddressUpdate } from "@/types/address";

const BASE = "/customer/profile";

const FALLBACK_MESSAGES = {
  getProfile: "We couldn't load your profile. Please try again.",
  updateProfile: "We couldn't update your profile. Please try again.",
  listAddresses: "We couldn't load your addresses. Please try again.",
  createAddress: "We couldn't add that address. Please try again.",
  updateAddress: "We couldn't update that address. Please try again.",
  deleteAddress: "We couldn't delete that address. Please try again.",
} as const;

function toUserFacingError(error: unknown, fallbackMessage: string): ApiError {
  if (error instanceof ApiError) {
    if (error.errorType === "network" || error.errorType === "parse") {
      return new ApiError(error.status, fallbackMessage, error.errorType, error.detail);
    }
    return error;
  }
  return new ApiError(500, fallbackMessage, "network");
}

// GET /customer/profile/me
export async function getProfile(signal?: AbortSignal): Promise<CustomerProfile> {
  try {
    return await apiClient.get<CustomerProfile>(`${BASE}/me`, { signal });
  } catch (error) {
    throw toUserFacingError(error, FALLBACK_MESSAGES.getProfile);
  }
}

// PUT /customer/profile/me
export async function updateProfile(
  data: CustomerProfileUpdate,
  signal?: AbortSignal
): Promise<CustomerProfile> {
  try {
    return await apiClient.put<CustomerProfile>(`${BASE}/me`, data, { signal });
  } catch (error) {
    throw toUserFacingError(error, FALLBACK_MESSAGES.updateProfile);
  }
}

// GET /customer/profile/addresses
export async function listAddresses(signal?: AbortSignal): Promise<Address[]> {
  try {
    return await apiClient.get<Address[]>(`${BASE}/addresses`, { signal });
  } catch (error) {
    throw toUserFacingError(error, FALLBACK_MESSAGES.listAddresses);
  }
}

// POST /customer/profile/addresses
export async function createAddress(data: AddressCreate, signal?: AbortSignal): Promise<Address> {
  try {
    return await apiClient.post<Address>(`${BASE}/addresses`, data, { signal });
  } catch (error) {
    throw toUserFacingError(error, FALLBACK_MESSAGES.createAddress);
  }
}

// PUT /customer/profile/addresses/{addressId}
export async function updateAddress(
  addressId: number,
  data: AddressUpdate,
  signal?: AbortSignal
): Promise<Address> {
  try {
    return await apiClient.put<Address>(`${BASE}/addresses/${addressId}`, data, { signal });
  } catch (error) {
    throw toUserFacingError(error, FALLBACK_MESSAGES.updateAddress);
  }
}

// DELETE /customer/profile/addresses/{addressId} — 204 No Content
export async function deleteAddress(addressId: number, signal?: AbortSignal): Promise<void> {
  try {
    await apiClient.delete(`${BASE}/addresses/${addressId}`, { signal });
  } catch (error) {
    throw toUserFacingError(error, FALLBACK_MESSAGES.deleteAddress);
  }
}
````

## File: frontend/lib/stores/authStore.ts
````typescript
import { create } from "zustand";
import * as authApi from "@/lib/api/auth";
import { CustomerProfile } from "@/types/user";
import { LoginSchemaType, RegisterSchemaType } from "@/lib/validation/auth";

interface AuthState {
  user: CustomerProfile | null;
  isAuthenticated: boolean;
  isLoading: boolean;
  isInitialized: boolean;

  login: (credentials: LoginSchemaType) => Promise<void>;
  register: (data: RegisterSchemaType) => Promise<void>;
  logout: () => Promise<void>;
  fetchCurrentUser: () => Promise<void>;
  setUser: (user: CustomerProfile) => void;
  clearAuth: () => void;
}

function clearClientCookies() {
  if (typeof document !== "undefined") {
    const cookiesToClear = ["access_token", "refresh_token", "session", "token"];
    const paths = ["/", "/account", "/api"];
    const hostname = window.location.hostname;
    const domains = [hostname, "." + hostname];

    cookiesToClear.forEach((name) => {
      document.cookie = `${name}=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;`;
      paths.forEach((path) => {
        document.cookie = `${name}=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=${path};`;
        domains.forEach((domain) => {
          document.cookie = `${name}=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=${path}; domain=${domain};`;
        });
      });
    });
  }
}

export const useAuthStore = create<AuthState>((set) => ({
  user: null,
  isAuthenticated: false,
  isLoading: false,
  isInitialized: false,

  login: async (credentials: LoginSchemaType) => {
    set({ isLoading: true });
    try {
      await authApi.login(credentials);
      const user = await authApi.getCurrentUser();
      set({ user, isAuthenticated: true, isLoading: false, isInitialized: true });
    } catch (error) {
      set({ isLoading: false });
      throw error;
    }
  },

  register: async (data: RegisterSchemaType) => {
    set({ isLoading: true });
    try {
      await authApi.register(data);
      set({ isLoading: false });
    } catch (error) {
      set({ isLoading: false });
      throw error;
    }
  },

  logout: async () => {
    try {
      await authApi.logout();
    } catch {
      // Ignore failures — clear local state regardless.
    }
    clearClientCookies();
    if (typeof window !== "undefined") {
      localStorage.clear();
      sessionStorage.clear();
    }
    set({ user: null, isAuthenticated: false, isInitialized: true });
  },

  fetchCurrentUser: async () => {
    set({ isLoading: true });
    try {
      const user = await authApi.getCurrentUser();
      set({ user, isAuthenticated: true, isLoading: false, isInitialized: true });
    } catch {
      set({ user: null, isAuthenticated: false, isLoading: false, isInitialized: true });
    }
  },

  setUser: (user: CustomerProfile) => set({ user }),

  clearAuth: () => {
    clearClientCookies();
    if (typeof window !== "undefined") {
      localStorage.clear();
      sessionStorage.clear();
    }
    set({ user: null, isAuthenticated: false, isInitialized: true });
  },
}));
````

## File: frontend/types/api.ts
````typescript
export interface ApiErrorResponse {
  detail: string | Array<{ loc: (string | number)[]; msg: string; type: string }>;
}

export interface PaginatedResponse<T> {
  items: T[];
  total: number;
  page: number;
  size: number;
  pages: number;
}

// Mirrors: app/schemas/customer_auth.py CustomerToken
export interface AuthTokenResponse {
  accessToken: string;
  refreshToken: string;
  tokenType: string;
}

export interface ProductQueryParams {
  page?: number;
  size?: number;
  search?: string;
  category?: string;
  minPrice?: number;
  maxPrice?: number;
  sortBy?: string;
  sortOrder?: "asc" | "desc";
}

export interface OrderQueryParams {
  page?: number;
  size?: number;
  status?: string;
}
````

## File: frontend/types/order.ts
````typescript
// Mirrors: app/schemas/order.py, app/schemas/order_item.py, app/schemas/customer_order.py

export interface OrderItem {
  id: number;
  orderId: number;
  productVariantId: number | null;
  quantity: number;
  priceAtPurchase: number;
  createdAt: string;
  updatedAt: string;
}

export interface OrderItemCreate {
  productVariantId: number;
  quantity: number;
  priceAtPurchase: number;
}

export interface OrderItemUpdate {
  quantity?: number;
  priceAtPurchase?: number;
}

export interface Order {
  id: number;
  customerId: number | null;
  status: string | null;
  guestName: string | null;
  guestEmail: string | null;
  guestPhone: string | null;
  shippingAddressId: number | null;
  billingAddressId: number | null;
  couponId: number | null;
  orderStatus: string;
  subtotal: number;
  discountAmount: number;
  shippingAmount: number;
  taxAmount: number;
  totalAmount: number;
  notes: string | null;
  createdAt: string;
  placedAt: string | null;
  items: OrderItem[];
}

export interface OrderCreate {
  customerId?: number | null;
  guestName?: string;
  guestEmail?: string;
  guestPhone?: string;
  orderStatus?: string;
}

export interface OrderUpdate {
  orderStatus?: string;
  notes?: string;
}

export interface OrderStatusUpdate {
  status: string;
}

export interface CustomerOrder {
  id: number;
  customerName: string | null;
  orderStatus: string;
  totalAmount: number;
  createdAt: string;
  items: OrderItem[];
}

export interface ReturnRequestCreate {
  orderItemId: number;
  reason?: string;
}

export interface ReturnRequestStatusUpdate {
  status: string;
  refundAmount?: number;
}

export interface ReturnRequest {
  id: number;
  orderItemId: number;
  customerId: number;
  reason: string | null;
  status: string;
  refundAmount: number | null;
  requestedAt: string;
  processedAt: string | null;
}
````

## File: frontend/types/product.ts
````typescript
// Mirrors: app/schemas/product.py, app/schemas/product_variant.py, app/schemas/category.py, app/schemas/product_category.py

export interface Category {
  id: number;
  name: string;
  description: string | null;
  createdAt: string;
  updatedAt: string;
}

export interface CategoryCreate {
  name: string;
  description?: string | null;
}

export interface CategoryUpdate {
  name?: string;
  description?: string | null;
}

export interface Product {
  id: number;
  name: string;
  description: string | null;
  price: number;
  isActive: boolean;
  createdAt: string;
  updatedAt: string;
  categories: Category[];
}

export interface ProductCreate {
  name: string;
  description?: string | null;
  price: number;
  isActive?: boolean;
}

export interface ProductUpdate {
  name?: string;
  description?: string | null;
  price?: number;
  isActive?: boolean;
}

export interface ProductVariant {
  id: number;
  productId: number;
  sku: string;
  price: number;
  stockQuantity: number;
  isActive: boolean;
  createdAt: string;
  updatedAt: string;
}

export interface ProductVariantCreate {
  sku: string;
  price: number;
  stockQuantity?: number;
  isActive?: boolean;
}

export interface ProductVariantUpdate {
  sku?: string;
  price?: number;
  stockQuantity?: number;
  isActive?: boolean;
}

export interface ProductCategory {
  id: number;
  productId: number;
  categoryId: number;
  category: Category;
  createdAt: string;
  updatedAt: string;
}

export interface ProductCategoryCreate {
  categoryId: number;
}
````

## File: frontend/types/user.ts
````typescript
// Mirrors: app/schemas/user.py, app/schemas/role.py, app/schemas/customer_profile.py

export interface Role {
  id: number;
  name: string;
  description: string | null;
}

export interface User {
  id: number;
  name: string;
  email: string;
  phoneNumber: string | null;
  avatarUrl: string | null;
  roleId: number;
  role: Role;
  isActive: boolean;
  createdAt: string;
  updatedAt: string;
}

export interface UserCreate {
  name: string;
  email: string;
  password: string;
  phoneNumber?: string | null;
  avatarUrl?: string | null;
  roleId: number;
  isActive?: boolean;
}

export interface UserUpdate {
  name?: string;
  email?: string;
  phoneNumber?: string;
  avatarUrl?: string;
  roleId?: number;
  isActive?: boolean;
}

export interface CustomerProfile {
  id: number;
  name: string;
  email: string;
  phoneNumber: string | null;
  avatarUrl: string | null;
  emailVerified: boolean;
  createdAt: string;
}

export interface CustomerProfileUpdate {
  name?: string;
  phoneNumber?: string;
  avatarUrl?: string;
}
````

## File: backend/app/api/routes/auth.py
````python
import secrets
from datetime import datetime, timedelta, timezone

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.database.session import get_db
from app.models.user import User
from app.models.role import Role
from app.models.permission import Permission
from app.models.role_permission import RolePermission
from app.schemas.auth import LoginRequest, Token, ForgotPasswordRequest, ResetPasswordRequest
from app.core.jwt import create_access_token
from app.core.security import verify_password, hash_password
from app.core.auth import get_current_user
from app.core.email import send_password_reset_email
from pydantic import BaseModel

router = APIRouter()

RESET_TOKEN_EXPIRE_HOURS = 1


class MsgResponse(BaseModel):
    message: str


@router.post("/login", response_model=Token)
async def login(payload: LoginRequest, db: AsyncSession = Depends(get_db)):
    stmt = select(User).where(User.email == payload.email)
    result = await db.execute(stmt)
    user = result.scalar_one_or_none()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
        )

    if not verify_password(payload.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
        )

    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="User account is inactive",
        )

    access_token = create_access_token(
        {
            "sub": str(user.id),
            "email": user.email,
            "role_id": user.role_id,
        }
    )

    return Token(access_token=access_token, token_type="bearer")


@router.get("/me")
async def get_me(
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    stmt = (
        select(Permission.name)
        .join(RolePermission, RolePermission.permission_id == Permission.id)
        .where(RolePermission.role_id == current_user.role_id)
    )
    result = await db.execute(stmt)
    permissions = list(result.scalars().all())

    return {
        "id": current_user.id,
        "name": current_user.name,
        "email": current_user.email,
        "role_id": current_user.role_id,
        "role": {
            "id": current_user.role.id,
            "name": current_user.role.name,
            "description": current_user.role.description,
        } if current_user.role else None,
        "is_active": current_user.is_active,
        "created_at": current_user.created_at,
        "updated_at": current_user.updated_at,
        "permissions": permissions,
    }


@router.post("/forgot-password", response_model=MsgResponse)
async def forgot_password(payload: ForgotPasswordRequest, db: AsyncSession = Depends(get_db)):
    stmt = select(User).where(User.email == payload.email)
    result = await db.execute(stmt)
    user = result.scalar_one_or_none()

    generic_response = MsgResponse(
        message="If that email exists, a password reset link has been sent."
    )

    if not user or not user.is_active:
        return generic_response

    token = secrets.token_urlsafe(32)
    user.password_reset_token = token
    user.password_reset_expires_at = datetime.now(timezone.utc) + timedelta(
        hours=RESET_TOKEN_EXPIRE_HOURS
    )
    await db.commit()

    send_password_reset_email(user.email, token)

    return generic_response


@router.post("/reset-password", response_model=MsgResponse)
async def reset_password(payload: ResetPasswordRequest, db: AsyncSession = Depends(get_db)):
    stmt = select(User).where(User.password_reset_token == payload.token)
    result = await db.execute(stmt)
    user = result.scalar_one_or_none()

    if not user:
        raise HTTPException(status_code=400, detail="Invalid or expired token")

    if (
        not user.password_reset_expires_at
        or user.password_reset_expires_at < datetime.now(timezone.utc)
    ):
        raise HTTPException(status_code=400, detail="Invalid or expired token")

    if not user.is_active:
        raise HTTPException(status_code=403, detail="User account is inactive")

    user.password = hash_password(payload.new_password)
    user.password_reset_token = None
    user.password_reset_expires_at = None
    await db.commit()

    return MsgResponse(
        message="Password has been reset successfully. Please log in with your new password."
    )
````

## File: backend/app/api/routes/order_items.py
````python
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError

from app.database.session import get_db
from app.models.user import User
from app.models.order import Order
from app.models.product_variant import ProductVariant
from app.models.order_item import OrderItem
from app.schemas.order_item import OrderItemOut, OrderItemCreate, OrderItemUpdate
from app.core.permissions import require_role, ADMIN, MANAGER, STAFF

router = APIRouter()

# #TODO: final check if completed is the exact status indicator.
LOCKED_STATUS = "completed"


def _assert_order_editable(order: Order) -> None:
    if order.order_status == LOCKED_STATUS:
        raise HTTPException(
            status_code=400,
            detail=f"Order is '{LOCKED_STATUS}' and can no longer be modified",
        )

async def recalculate_total(order_id: int, db: AsyncSession) -> None:
    result = await db.execute(select(OrderItem).where(OrderItem.order_id == order_id))
    total = sum(item.quantity * float(item.price_at_purchase) for item in result.scalars().all())

    result = await db.execute(select(Order).where(Order.id == order_id))
    order = result.scalar_one_or_none()
    if not order:
        return

    order.total_amount = total
    await db.commit()


@router.get("/orders/{order_id}/items", response_model=list[OrderItemOut])
async def get_order_items(
    order_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER, STAFF))
):
    result = await db.execute(select(Order).where(Order.id == order_id))
    order = result.scalar_one_or_none()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    result = await db.execute(select(OrderItem).where(OrderItem.order_id == order_id))
    return result.scalars().all()


@router.post("/orders/{order_id}/items", response_model=OrderItemOut, status_code=201)
async def add_order_item(
    order_id: int,
    payload: OrderItemCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER, STAFF))
):
    result = await db.execute(select(Order).where(Order.id == order_id))
    order = result.scalar_one_or_none()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    _assert_order_editable(order)

    result = await db.execute(select(ProductVariant).where(ProductVariant.id == payload.product_variant_id))
    variant = result.scalar_one_or_none()
    if not variant:
        raise HTTPException(status_code=404, detail="Product variant not found")

    if variant.stock_quantity < payload.quantity:
        raise HTTPException(
            status_code=400,
            detail=f"Insufficient stock for SKU '{variant.sku}': only {variant.stock_quantity} available"
        )

    new_item = OrderItem(
        order_id=order_id,
        product_variant_id=payload.product_variant_id,
        quantity=payload.quantity,
        price_at_purchase=payload.price_at_purchase,
    )
    variant.stock_quantity -= payload.quantity
    db.add(new_item)

    try:
        await db.commit()
    except IntegrityError:
        await db.rollback()
        raise HTTPException(status_code=400, detail="Invalid product_variant_id")

    await db.refresh(new_item)
    await recalculate_total(order_id, db)
    await db.refresh(new_item)
    return new_item


@router.put("/order-items/{item_id}", response_model=OrderItemOut)
async def update_order_item(
    item_id: int,
    payload: OrderItemUpdate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER, STAFF))
):
    result = await db.execute(select(OrderItem).where(OrderItem.id == item_id))
    item = result.scalar_one_or_none()
    if not item:
        raise HTTPException(status_code=404, detail="Order item not found")

    result = await db.execute(select(Order).where(Order.id == item.order_id))
    order = result.scalar_one_or_none()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    _assert_order_editable(order)

    update_data = payload.model_dump(exclude_unset=True)

    if "quantity" in update_data:
        result = await db.execute(select(ProductVariant).where(ProductVariant.id == item.product_variant_id))
        variant = result.scalar_one_or_none()
        if not variant:
            raise HTTPException(status_code=404, detail="Product variant not found")

        old_quantity = item.quantity
        new_quantity = update_data["quantity"]
        diff = new_quantity - old_quantity

        if diff > 0 and variant.stock_quantity < diff:
            raise HTTPException(
                status_code=400,
                detail=f"Insufficient stock for SKU '{variant.sku}': only {variant.stock_quantity} available"
            )

        variant.stock_quantity -= diff

    for field, value in update_data.items():
        setattr(item, field, value)

    await db.commit()
    await db.refresh(item)
    await recalculate_total(item.order_id, db)
    await db.refresh(item)
    return item


@router.delete("/order-items/{item_id}", status_code=204)
async def delete_order_item(
    item_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER, STAFF))
):
    result = await db.execute(select(OrderItem).where(OrderItem.id == item_id))
    item = result.scalar_one_or_none()
    if not item:
        raise HTTPException(status_code=404, detail="Order item not found")

    result = await db.execute(select(Order).where(Order.id == item.order_id))
    order = result.scalar_one_or_none()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    _assert_order_editable(order)

    if item.product_variant_id is not None:
        result = await db.execute(select(ProductVariant).where(ProductVariant.id == item.product_variant_id))
        variant = result.scalar_one_or_none()
        if variant:
            variant.stock_quantity += item.quantity

    order_id = item.order_id
    await db.delete(item)
    await db.commit()

    await recalculate_total(order_id, db)
    return None
````

## File: backend/app/api/routes/orders.py
````python
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.session import get_db
from app.models.user import User
from app.models.order import Order
from app.schemas.order import OrderOut, OrderCreate, OrderUpdate, OrderStatusUpdate
from app.core.permissions import require_role, ADMIN, MANAGER, STAFF

router = APIRouter()


@router.get("/orders", response_model=list[OrderOut])
async def get_orders(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER, STAFF))
):
    result = await db.execute(select(Order))
    return result.scalars().all()


@router.get("/orders/{order_id}", response_model=OrderOut)
async def get_order(
    order_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER, STAFF))
):
    result = await db.execute(select(Order).where(Order.id == order_id))
    order = result.scalar_one_or_none()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order


@router.post("/orders", response_model=OrderOut, status_code=201)
async def create_order(
    payload: OrderCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER, STAFF))
):
    new_order = Order(
        customer_id=payload.customer_id,
        guest_name=payload.guest_name,
        guest_email=payload.guest_email,
        guest_phone=payload.guest_phone,
        order_status=payload.order_status,
        total_amount=0,
    )
    db.add(new_order)
    await db.commit()
    await db.refresh(new_order)
    return new_order


@router.put("/orders/{order_id}", response_model=OrderOut)
async def update_order(
    order_id: int,
    payload: OrderUpdate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER, STAFF))
):
    result = await db.execute(select(Order).where(Order.id == order_id))
    order = result.scalar_one_or_none()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    update_data = payload.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(order, field, value)

    await db.commit()
    await db.refresh(order)
    return order


@router.patch("/orders/{order_id}/status", response_model=OrderOut)
async def update_order_status(
    order_id: int,
    payload: OrderStatusUpdate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER, STAFF))
):
    result = await db.execute(select(Order).where(Order.id == order_id))
    order = result.scalar_one_or_none()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    order.order_status = payload.status
    await db.commit()
    await db.refresh(order)
    return order


@router.delete("/orders/{order_id}", status_code=204)
async def delete_order(
    order_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(ADMIN, MANAGER, STAFF))
):
    result = await db.execute(select(Order).where(Order.id == order_id))
    order = result.scalar_one_or_none()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    await db.delete(order)
    await db.commit()
    return None
````

## File: backend/app/models/cart.py
````python
import uuid
from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class Cart(Base):
    __tablename__ = "carts"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    customer_id: Mapped[int | None] = mapped_column(
        ForeignKey("customer_profiles.id", ondelete="CASCADE"), nullable=True, unique=True
    )
    guest_token: Mapped[uuid.UUID | None] = mapped_column(UUID(as_uuid=True), nullable=True, unique=True, index=True)
    coupon_id: Mapped[int | None] = mapped_column(ForeignKey("coupons.id", ondelete="SET NULL"), nullable=True)

    created_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )
    expires_at: Mapped[DateTime | None] = mapped_column(DateTime(timezone=True), nullable=True)

    # Relationships
    items: Mapped[list["CartItem"]] = relationship(back_populates="cart", cascade="all, delete-orphan")
    coupon: Mapped["Coupon"] = relationship(back_populates="carts")
    customer: Mapped["CustomerProfile"] = relationship(back_populates="cart")
````

## File: backend/app/schemas/cart.py
````python
from pydantic import BaseModel, Field
import uuid


class CartItemCreate(BaseModel):
    product_variant_id: int
    quantity: int = Field(default=1, ge=1)


class CartItemUpdate(BaseModel):
    quantity: int = Field(ge=1)


class CartItemOut(BaseModel):
    id: int
    product_variant_id: int
    quantity: int
    unit_price: float
    subtotal: float

    class Config:
        from_attributes = True


class CartOut(BaseModel):
    id: int
    customer_id: int | None
    guest_token: uuid.UUID | None
    coupon_id: int | None
    items: list[CartItemOut]
    total: float

    class Config:
        from_attributes = True


class CartMergeRequest(BaseModel):
    guest_token: str


class ApplyCouponRequest(BaseModel):
    code: str
````

## File: backend/app/schemas/order.py
````python
from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, model_validator

from app.schemas.order_item import OrderItemOut


class OrderOut(BaseModel):
    id: int
    customer_id: int | None = None
    status: str | None = None
    guest_name: str | None = None
    guest_email: str | None = None
    guest_phone: str | None = None
    shipping_address_id: int | None = None
    billing_address_id: int | None = None
    coupon_id: int | None = None
    order_status: str
    subtotal: float
    discount_amount: float
    shipping_amount: float
    tax_amount: float
    total_amount: float
    notes: str | None = None
    created_at: datetime
    placed_at: datetime | None = None
    items: list[OrderItemOut] = []

    model_config = ConfigDict(from_attributes=True)

    @model_validator(mode="before")
    @classmethod
    def populate_status_compat(cls, data):
        if isinstance(data, dict):
            if data.get("status") is None and data.get("order_status") is not None:
                data = dict(data)
                data["status"] = data["order_status"]
        return data


class OrderCreate(BaseModel):
    customer_id: int | None = None
    guest_name: str | None = Field(default=None, max_length=100)
    guest_email: str | None = Field(default=None, max_length=255)
    guest_phone: str | None = Field(default=None, max_length=20)
    order_status: str = Field(default="open", max_length=20)


class OrderUpdate(BaseModel):
    order_status: str | None = Field(default=None, max_length=20)
    notes: str | None = None


class OrderStatusUpdate(BaseModel):
    status: str = Field(max_length=20)
````

## File: frontend/package.json
````json
{
  "name": "ecommerce-frontend",
  "version": "0.1.0",
  "private": true,
  "type": "module",
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start",
    "lint": "next lint",
    "test": "jest",
    "test:watch": "jest --watch",
    "test:coverage": "jest --coverage"
  },
  "dependencies": {
    "@hookform/resolvers": "^5.5.7",
    "@tailwindcss/postcss": "^4.3.3",
    "next": "^16.2.12",
    "postcss": "^8.5.23",
    "react": "19.0.0",
    "react-dom": "19.0.0",
    "react-hook-form": "^7.83.0",
    "sharp": "^0.35.3",
    "tailwindcss": "^4.3.3",
    "zod": "^3.23.8",
    "zustand": "^5.0.14"
  },
  "devDependencies": {
    "@playwright/test": "^1.61.1",
    "@testing-library/dom": "^10.4.0",
    "@testing-library/jest-dom": "^6.4.2",
    "@testing-library/react": "^16.0.0",
    "@types/jest": "^29.5.12",
    "@types/node": "^20.11.24",
    "@types/react": "^19.0.0",
    "@types/react-dom": "^19.0.0",
    "brace-expansion": "^5.0.8",
    "eslint": "^10.8.0",
    "eslint-config-next": "^16.2.12",
    "jest": "^30.0.0",
    "jest-environment-jsdom": "^30.0.0",
    "ts-jest": "^29.2.0",
    "ts-node": "^10.9.2",
    "typescript": "^5.3.3"
  },
  "overrides": {
    "brace-expansion": "^5.0.8",
    "minimatch": "^10.2.5",
    "postcss": "^8.5.23",
    "sharp": "^0.35.3"
  }
}
````

## File: .gitignore
````
# ---------- Node / Next.js (frontend) ----------
node_modules/
.next/
out/
build/
dist/
.pnp/
.pnp.js

# env files
.env
.env.local
.env.*.local
.env.production
.env.development
!.env.example

# logs
npm-debug.log*
yarn-debug.log*
yarn-error.log*
pnpm-debug.log*

# testing
coverage/
playwright-report/
test-results/

# misc
.DS_Store
*.pem
next-env.d.ts
.vercel

# ---------- Python / FastAPI (backend) ----------
# Explicitly target nested __pycache__ and bytecode
**/__pycache__/
*.py[cod]
*$py.class
*.so
.Python
*.egg-info/
.pytest_cache/
.mypy_cache/
.ruff_cache/

# Explicitly target backend virtual environment paths
backend/venv/
backend/env/
backend/.venv/

# alembic (keep versions, ignore local db files)
*.sqlite3
*.db

# env files (backend)
backend/.env
backend/.env.production
backend/.env.development
backend/.env.test
backend/repomix-output.md

# ---------- Editors / OS ----------
.vscode/
.idea/
*.swp
Thumbs.db
.DS_Store

# ---------- Docker ----------
*.log
docker-compose.override.yml

#-------Repomix -------------
repomix-output.xml
````

## File: backend/app/api/routes/cart.py
````python
from datetime import datetime, timezone

from fastapi import APIRouter, Depends, HTTPException, Header
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.database.session import get_db
from app.models.cart import Cart
from app.models.cart_item import CartItem
from app.models.product_variant import ProductVariant
from app.models.coupon import Coupon
from app.models.user import User
from app.models.customer_profile import CustomerProfile
from app.schemas.cart import (
    CartItemCreate,
    CartItemUpdate,
    CartOut,
    CartMergeRequest,
    ApplyCouponRequest,
)
from app.core.auth import get_current_user_optional

router = APIRouter()

_CART_ITEM_LOAD = selectinload(Cart.items).selectinload(CartItem.product_variant)


def _compute_total(cart: Cart) -> float:
    return sum(float(item.product_variant.price) * item.quantity for item in cart.items)


def _serialize_cart(cart: Cart) -> dict:
    return {
        "id": cart.id,
        "customer_id": cart.customer_id,
        "guest_token": cart.guest_token,
        "coupon_id": cart.coupon_id,
        "items": [
            {
                "id": item.id,
                "product_variant_id": item.product_variant_id,
                "quantity": item.quantity,
                "unit_price": float(item.product_variant.price),
                "subtotal": float(item.product_variant.price) * item.quantity,
            }
            for item in cart.items
        ],
        "total": _compute_total(cart),
    }


async def _get_or_create_customer_profile(db: AsyncSession, user: User) -> CustomerProfile:
    result = await db.execute(select(CustomerProfile).where(CustomerProfile.user_id == user.id))
    profile = result.scalar_one_or_none()
    if not profile:
        profile = CustomerProfile(user_id=user.id)
        db.add(profile)
        await db.commit()
        await db.refresh(profile)
    return profile


async def _get_or_create_cart(
    db: AsyncSession,
    current_user: User | None,
    guest_token: str | None,
) -> Cart:
    if current_user:
        profile = await _get_or_create_customer_profile(db, current_user)

        result = await db.execute(
            select(Cart).options(_CART_ITEM_LOAD).where(Cart.customer_id == profile.id)
        )
        cart = result.scalar_one_or_none()
        if not cart:
            cart = Cart(customer_id=profile.id)
            db.add(cart)
            await db.commit()
            cart = await _reload_cart(db, cart.id)
        return cart

    if not guest_token:
        raise HTTPException(status_code=400, detail="Guest token required for guest cart")

    result = await db.execute(
        select(Cart).options(_CART_ITEM_LOAD).where(Cart.guest_token == guest_token)
    )
    cart = result.scalar_one_or_none()
    if not cart:
        cart = Cart(guest_token=guest_token)
        db.add(cart)
        await db.commit()
        cart = await _reload_cart(db, cart.id)
    return cart


async def _reload_cart(db: AsyncSession, cart_id: int) -> Cart:
    result = await db.execute(
        select(Cart).options(_CART_ITEM_LOAD).where(Cart.id == cart_id)
    )
    return result.scalar_one()


@router.get("/cart", response_model=CartOut)
async def get_cart(
    db: AsyncSession = Depends(get_db),
    current_user: User | None = Depends(get_current_user_optional),
    x_guest_token: str | None = Header(default=None),
):
    cart = await _get_or_create_cart(db, current_user, x_guest_token)
    return _serialize_cart(cart)


@router.post("/cart/items", response_model=CartOut, status_code=201)
async def add_cart_item(
    payload: CartItemCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User | None = Depends(get_current_user_optional),
    x_guest_token: str | None = Header(default=None),
):
    result = await db.execute(
        select(ProductVariant).where(ProductVariant.id == payload.product_variant_id)
    )
    variant = result.scalar_one_or_none()
    if not variant:
        raise HTTPException(status_code=404, detail="Product variant not found")

    cart = await _get_or_create_cart(db, current_user, x_guest_token)

    result = await db.execute(
        select(CartItem).where(
            CartItem.cart_id == cart.id,
            CartItem.product_variant_id == payload.product_variant_id,
        )
    )
    existing_item = result.scalar_one_or_none()

    if existing_item:
        existing_item.quantity += payload.quantity
    else:
        new_item = CartItem(
            cart_id=cart.id,
            product_variant_id=payload.product_variant_id,
            quantity=payload.quantity,
        )
        db.add(new_item)

    await db.commit()
    cart = await _reload_cart(db, cart.id)
    return _serialize_cart(cart)


@router.put("/cart/items/{item_id}", response_model=CartOut)
async def update_cart_item(
    item_id: int,
    payload: CartItemUpdate,
    db: AsyncSession = Depends(get_db),
    current_user: User | None = Depends(get_current_user_optional),
    x_guest_token: str | None = Header(default=None),
):
    cart = await _get_or_create_cart(db, current_user, x_guest_token)

    result = await db.execute(
        select(CartItem).where(
            CartItem.id == item_id,
            CartItem.cart_id == cart.id,
        )
    )
    item = result.scalar_one_or_none()
    if not item:
        raise HTTPException(status_code=404, detail="Cart item not found")

    item.quantity = payload.quantity
    await db.commit()
    cart = await _reload_cart(db, cart.id)
    return _serialize_cart(cart)


@router.delete("/cart/items/{item_id}", response_model=CartOut)
async def delete_cart_item(
    item_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User | None = Depends(get_current_user_optional),
    x_guest_token: str | None = Header(default=None),
):
    cart = await _get_or_create_cart(db, current_user, x_guest_token)

    result = await db.execute(
        select(CartItem).where(
            CartItem.id == item_id,
            CartItem.cart_id == cart.id,
        )
    )
    item = result.scalar_one_or_none()
    if not item:
        raise HTTPException(status_code=404, detail="Cart item not found")

    await db.delete(item)
    await db.commit()

    cart = await _reload_cart(db, cart.id)
    return _serialize_cart(cart)


@router.post("/cart/merge", response_model=CartOut)
async def merge_cart(
    payload: CartMergeRequest,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user_optional),
):
    if not current_user:
        raise HTTPException(status_code=401, detail="Login required to merge cart")

    profile = await _get_or_create_customer_profile(db, current_user)

    result = await db.execute(select(Cart).where(Cart.guest_token == payload.guest_token))
    guest_cart = result.scalar_one_or_none()
    if not guest_cart:
        raise HTTPException(status_code=404, detail="Guest cart not found")

    result = await db.execute(select(Cart).where(Cart.customer_id == profile.id))
    user_cart = result.scalar_one_or_none()
    if not user_cart:
        guest_cart.customer_id = profile.id
        guest_cart.guest_token = None
        await db.commit()
        cart = await _reload_cart(db, guest_cart.id)
        return _serialize_cart(cart)

    result = await db.execute(select(CartItem).where(CartItem.cart_id == guest_cart.id))
    guest_items = result.scalars().all()
    for guest_item in guest_items:
        result = await db.execute(
            select(CartItem).where(
                CartItem.cart_id == user_cart.id,
                CartItem.product_variant_id == guest_item.product_variant_id,
            )
        )
        existing_item = result.scalar_one_or_none()
        if existing_item:
            existing_item.quantity += guest_item.quantity
        else:
            db.add(CartItem(
                cart_id=user_cart.id,
                product_variant_id=guest_item.product_variant_id,
                quantity=guest_item.quantity,
            ))

    await db.delete(guest_cart)
    await db.commit()
    user_cart = await _reload_cart(db, user_cart.id)
    return _serialize_cart(user_cart)


@router.post("/cart/apply-coupon", response_model=CartOut)
async def apply_coupon(
    payload: ApplyCouponRequest,
    db: AsyncSession = Depends(get_db),
    current_user: User | None = Depends(get_current_user_optional),
    x_guest_token: str | None = Header(default=None),
):
    result = await db.execute(select(Coupon).where(Coupon.code == payload.code))
    coupon = result.scalar_one_or_none()
    if not coupon:
        raise HTTPException(status_code=404, detail="Coupon not found")

    if not coupon.is_active:
        raise HTTPException(status_code=400, detail="Coupon is not active")

    now = datetime.now(timezone.utc)
    if now < coupon.start_date or now > coupon.end_date:
        raise HTTPException(status_code=400, detail="Coupon is not valid at this time")

    if coupon.usage_limit is not None and coupon.usage_count >= coupon.usage_limit:
        raise HTTPException(status_code=400, detail="Coupon usage limit reached")

    cart = await _get_or_create_cart(db, current_user, x_guest_token)

    cart_total = _compute_total(cart)
    min_order = coupon.minimum_order_amount or 0
    if cart_total < float(min_order):
        raise HTTPException(
            status_code=400,
            detail=f"Order must be at least {min_order} to use this coupon",
        )

    cart.coupon_id = coupon.id
    await db.commit()
    cart = await _reload_cart(db, cart.id)
    return _serialize_cart(cart)


@router.delete("/cart/coupon", response_model=CartOut)
async def remove_coupon(
    db: AsyncSession = Depends(get_db),
    current_user: User | None = Depends(get_current_user_optional),
    x_guest_token: str | None = Header(default=None),
):
    cart = await _get_or_create_cart(db, current_user, x_guest_token)
    cart.coupon_id = None
    await db.commit()
    cart = await _reload_cart(db, cart.id)
    return _serialize_cart(cart)
````

## File: backend/app/models/order.py
````python
from datetime import datetime
from sqlalchemy import DateTime, ForeignKey, Numeric, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database.base import Base


class Order(Base):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    customer_id: Mapped[int | None] = mapped_column(
        ForeignKey("customer_profiles.id", ondelete="SET NULL"), nullable=True
    )
    guest_name: Mapped[str | None] = mapped_column(String(100), nullable=True)
    guest_email: Mapped[str | None] = mapped_column(String(255), nullable=True)
    guest_phone: Mapped[str | None] = mapped_column(String(20), nullable=True)

    shipping_address_id: Mapped[int | None] = mapped_column(
        ForeignKey("addresses.id", ondelete="SET NULL"), nullable=True
    )
    billing_address_id: Mapped[int | None] = mapped_column(
        ForeignKey("addresses.id", ondelete="SET NULL"), nullable=True
    )
    coupon_id: Mapped[int | None] = mapped_column(
        ForeignKey("coupons.id", ondelete="SET NULL"), nullable=True
    )

    order_status: Mapped[str] = mapped_column(String(20), nullable=False, default="open")

    subtotal: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False, default=0)
    discount_amount: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False, default=0)
    shipping_amount: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False, default=0)
    tax_amount: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False, default=0)
    total_amount: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False)

    notes: Mapped[str | None] = mapped_column(Text, nullable=True)

    created_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    placed_at: Mapped[DateTime | None] = mapped_column(DateTime(timezone=True), nullable=True)

    def __init__(self, **kwargs):
        if "status" in kwargs and "order_status" not in kwargs:
            kwargs["order_status"] = kwargs.pop("status")
        if "customer_name" in kwargs:
            self._customer_name = kwargs.pop("customer_name")
        super().__init__(**kwargs)

    @property
    def status(self) -> str:
        return self.order_status

    @status.setter
    def status(self, value: str) -> None:
        self.order_status = value

    @property
    def customer_name(self) -> str | None:
        return getattr(self, "_customer_name", None)

    @customer_name.setter
    def customer_name(self, value: str | None) -> None:
        self._customer_name = value

    # Relationships
    items: Mapped[list["OrderItem"]] = relationship(
        back_populates="order",
        cascade="all, delete-orphan"
    )
    customer: Mapped["CustomerProfile"] = relationship()
````

## File: backend/app/models/user.py
````python
from datetime import datetime

from sqlalchemy import Boolean, DateTime, ForeignKey, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)
    password: Mapped[str] = mapped_column(String(255), nullable=False)
    role_id: Mapped[int] = mapped_column(ForeignKey("roles.id"), nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)
    phone_number: Mapped[str | None] = mapped_column(String(20), nullable=True)
    avatar_url: Mapped[str | None] = mapped_column(String(512), nullable=True)

    password_reset_token: Mapped[str | None] = mapped_column(String(255), nullable=True)
    password_reset_expires_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True), nullable=True
    )

    email_verified: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    email_verification_token: Mapped[str | None] = mapped_column(String(255), nullable=True)
    email_verification_expires_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True), nullable=True
    )

    refresh_token: Mapped[str | None] = mapped_column(String(255), nullable=True)
    refresh_token_expires_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True), nullable=True
    )

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )

    role: Mapped["Role"] = relationship(back_populates="users")
    customer_profile: Mapped["CustomerProfile"] = relationship(
        back_populates="user", uselist=False
    )
````

## File: backend/tests/conftest.py
````python
import os
import sys
import asyncio
from datetime import datetime, timedelta, timezone

os.environ.setdefault("DATABASE_URL", "postgresql+asyncpg://postgres:admin@localhost:5432/ecommerce_test")
os.environ.setdefault("SECRET_KEY", "test-secret-key-do-not-use-in-prod")
os.environ.setdefault("ALGORITHM", "HS256")
os.environ.setdefault("ACCESS_TOKEN_EXPIRE_MINUTES", "30")
os.environ.setdefault("STRIPE_SECRET_KEY", "sk_test_dummy")
os.environ.setdefault("STRIPE_WEBHOOK_SECRET", "whsec_dummy")
os.environ.setdefault("TEST_MODE", "false")

if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

import pytest
import pytest_asyncio
from httpx import AsyncClient, ASGITransport
from sqlalchemy import select
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.pool import NullPool
from app.models.product import Product
from app.models.product_variant import ProductVariant
from app.models.cart import Cart
from app.models.cart_item import CartItem

from app.database.base import Base
from app.database.session import get_db
from app.core.config import settings
from app.core.jwt import create_access_token
from app.core.security import hash_password
from app.models.user import User
from app.models.role import Role
from app.models.customer_profile import CustomerProfile
from app.models.order import Order
from app.models.order_item import OrderItem

import app.models  # noqa: F401  registers all model metadata
from app.main import app as fastapi_app

STAFF_ROLE_ID = 3
CUSTOMER_ROLE_ID = 4

test_engine = create_async_engine(settings.DATABASE_URL, future=True, poolclass=NullPool)
TestSessionLocal = async_sessionmaker(
    bind=test_engine,
    autocommit=False,
    autoflush=False,
    expire_on_commit=False,
    class_=AsyncSession,
)


@pytest_asyncio.fixture(scope="session", autouse=True, loop_scope="session")
async def setup_database():
    async with test_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    async with TestSessionLocal() as session:
        result = await session.execute(select(Role).where(Role.id.in_([STAFF_ROLE_ID, CUSTOMER_ROLE_ID])))
        existing_role_ids = {role.id for role in result.scalars()}
        if STAFF_ROLE_ID not in existing_role_ids:
            session.add(Role(id=STAFF_ROLE_ID, name="staff", description="Staff role"))
        if CUSTOMER_ROLE_ID not in existing_role_ids:
            session.add(Role(id=CUSTOMER_ROLE_ID, name="customer", description="Customer role"))
        if STAFF_ROLE_ID not in existing_role_ids or CUSTOMER_ROLE_ID not in existing_role_ids:
            await session.commit()
    yield
    async with test_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
    await test_engine.dispose()


@pytest_asyncio.fixture
async def db():
    async with test_engine.connect() as connection:
        await connection.begin()
        session = AsyncSession(
            bind=connection,
            expire_on_commit=False,
            join_transaction_mode="create_savepoint",
        )
        try:
            yield session
        finally:
            await session.close()
            await connection.rollback()


@pytest_asyncio.fixture
async def client(db):
    async def override_get_db():
        yield db

    fastapi_app.dependency_overrides[get_db] = override_get_db
    transport = ASGITransport(app=fastapi_app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        yield ac
    fastapi_app.dependency_overrides.clear()


@pytest_asyncio.fixture
async def make_customer(db):
    async def _make_customer(email="customer@example.com", password="Password123!", verified=True, active=True):
        user = User(
            name="Test Customer",
            email=email,
            password=hash_password(password),
            role_id=CUSTOMER_ROLE_ID,
            is_active=active,
            email_verified=verified,
        )
        db.add(user)
        await db.commit()
        await db.refresh(user)

        profile = CustomerProfile(user_id=user.id)
        db.add(profile)
        await db.commit()

        return user, password

    return _make_customer


@pytest_asyncio.fixture
async def auth_headers():
    def _auth_headers(user):
        token = create_access_token({"sub": str(user.id), "email": user.email, "role_id": user.role_id})
        return {"Authorization": f"Bearer {token}"}

    return _auth_headers


@pytest.fixture(autouse=True)
def mock_emails(monkeypatch):
    sent = {"verification": [], "reset": []}

    def fake_verification(to, token):
        sent["verification"].append((to, token))

    def fake_reset(to, token):
        sent["reset"].append((to, token))

    monkeypatch.setattr("app.api.routes.customer_auth.send_verification_email", fake_verification)
    monkeypatch.setattr("app.api.routes.customer_auth.send_password_reset_email", fake_reset)

    return sent


@pytest_asyncio.fixture
async def make_product_variant(db):
    counter = {"n": 0}

    async def _make_product_variant(price=19.99, stock_quantity=10, is_active=True):
        counter["n"] += 1
        n = counter["n"]

        product = Product(
            name=f"Test Product {n}",
            description="Seeded for checkout tests",
            price=price,
            is_active=True,
        )
        db.add(product)
        await db.flush()

        variant = ProductVariant(
            product_id=product.id,
            sku=f"TEST-SKU-{n}",
            price=price,
            stock_quantity=stock_quantity,
            is_active=is_active,
        )
        db.add(variant)
        await db.commit()
        await db.refresh(variant)

        return variant

    return _make_product_variant


@pytest_asyncio.fixture
async def make_cart_with_item(db):
    async def _make_cart_with_item(customer_profile_id, variant, quantity=1):
        cart = Cart(customer_id=customer_profile_id)
        db.add(cart)
        await db.flush()

        item = CartItem(cart_id=cart.id, product_variant_id=variant.id, quantity=quantity)
        db.add(item)
        await db.commit()
        await db.refresh(cart)

        return cart

    return _make_cart_with_item


@pytest_asyncio.fixture
async def make_order_item(db, make_product_variant):
    async def _make_order_item(customer_profile_id, variant=None, quantity=1):
        if variant is None:
            variant = await make_product_variant()

        order = Order(
            customer_id=customer_profile_id,
            order_status="completed",
            total_amount=float(variant.price) * quantity,
        )
        db.add(order)
        await db.flush()

        order_item = OrderItem(
            order_id=order.id,
            product_variant_id=variant.id,
            quantity=quantity,
            price_at_purchase=float(variant.price),
        )
        db.add(order_item)
        await db.commit()
        await db.refresh(order_item)

        return order_item, variant.product_id

    return _make_order_item


@pytest_asyncio.fixture
async def make_staff(db):
    async def _make_staff(email="staff@example.com", password="Password123!"):
        user = User(
            name="Test Staff",
            email=email,
            password=hash_password(password),
            role_id=STAFF_ROLE_ID,
            is_active=True,
            email_verified=True,
        )
        db.add(user)
        await db.commit()
        await db.refresh(user)
        return user, password

    return _make_staff
````

## File: frontend/lib/api/auth.ts
````typescript
import { apiClient, ApiError } from "./client";
import { CustomerProfile } from "@/types/user";
import {
  LoginSchemaType,
  RegisterSchemaType,
  ResetPasswordSchemaType,
  ForgotPasswordSchemaType,
} from "@/lib/validation/auth";

const FALLBACK_MESSAGES = {
  login: "We couldn't sign you in. Please check your credentials and try again.",
  register: "We couldn't create your account. Please try again.",
  refresh: "Your session has expired. Please log in again.",
  logout: "We couldn't log you out. Please try again.",
  forgotPassword: "We couldn't send the password reset email. Please try again.",
  resetPassword: "We couldn't reset your password. Please try again.",
  verifyEmail: "We couldn't verify your email. Please try again.",
  resendVerification: "We couldn't resend the verification email. Please try again.",
} as const;

function toUserFacingError(error: unknown, fallbackMessage: string): ApiError {
  if (error instanceof ApiError) {
    if (error.errorType === "network" || error.errorType === "parse") {
      return new ApiError(error.status, fallbackMessage, error.errorType, error.detail);
    }
    return error;
  }
  return new ApiError(500, fallbackMessage, "network");
}

// POST /customer/auth/register — returns id/name/email/emailVerified/message, NOT a token
export async function register(
  userData: RegisterSchemaType,
  signal?: AbortSignal
): Promise<{ id: number; name: string; email: string; emailVerified: boolean; message: string }> {
  try {
    const payload = {
      name: `${userData.firstName} ${userData.lastName}`.trim(),
      email: userData.email,
      password: userData.password,
    };
    return await apiClient.post("/customer/auth/register", payload, { signal });
  } catch (error) {
    throw toUserFacingError(error, FALLBACK_MESSAGES.register);
  }
}

// POST /customer/auth/login
export async function login(
  credentials: LoginSchemaType,
  signal?: AbortSignal
): Promise<{ message: string }> {
  try {
    return await apiClient.post<{ message: string }>("/customer/auth/login", credentials, {
      signal,
    });
  } catch (error) {
    throw toUserFacingError(error, FALLBACK_MESSAGES.login);
  }
}

// POST /customer/auth/refresh
export async function refreshToken(signal?: AbortSignal): Promise<{ message: string }> {
  try {
    return await apiClient.post<{ message: string }>(
      "/customer/auth/refresh",
      {},
      { signal, skipAuthRetry: true }
    );
  } catch (error) {
    throw toUserFacingError(error, FALLBACK_MESSAGES.refresh);
  }
}

// POST /customer/auth/logout
export async function logout(signal?: AbortSignal): Promise<{ message: string }> {
  try {
    // 1. Invalidate session on FastAPI backend
    await apiClient.post("/customer/auth/logout", {}, { signal }).catch(() => {});
  } catch {
    // Ignore backend connection errors on logout
  }

  try {
    // 2. Clear Next.js cookies on frontend server/middleware context
    if (typeof window !== "undefined") {
      await fetch("/api/auth/logout", { method: "POST" }).catch(() => {});
    }
  } catch {
    // Ignore frontend route errors
  }

  return { message: "Logged out successfully" };
}

export async function getCurrentUser(signal?: AbortSignal): Promise<CustomerProfile> {
  try {
    const response = await apiClient.get<{
      id: number;
      name: string;
      email: string;
      phone_number: string | null;
      avatar_url: string | null;
      email_verified: boolean;
      created_at: string;
    }>("/customer/auth/me", { signal });

    return {
      id: response.id,
      name: response.name,
      email: response.email,
      phoneNumber: response.phone_number,
      avatarUrl: response.avatar_url,
      emailVerified: response.email_verified,
      createdAt: response.created_at,
    };
  } catch (error) {
    throw toUserFacingError(error, FALLBACK_MESSAGES.refresh);
  }
}

// POST /customer/auth/verify-email
export async function verifyEmail(
  token: string,
  signal?: AbortSignal
): Promise<{ message: string }> {
  try {
    return await apiClient.post("/customer/auth/verify-email", { token }, { signal });
  } catch (error) {
    throw toUserFacingError(error, FALLBACK_MESSAGES.verifyEmail);
  }
}

// POST /customer/auth/resend-verification
export async function resendVerification(
  email: string,
  signal?: AbortSignal
): Promise<{ message: string }> {
  try {
    return await apiClient.post("/customer/auth/resend-verification", { email }, { signal });
  } catch (error) {
    throw toUserFacingError(error, FALLBACK_MESSAGES.resendVerification);
  }
}

// POST /customer/auth/forgot-password
export async function forgotPassword(
  data: ForgotPasswordSchemaType,
  signal?: AbortSignal
): Promise<{ message: string }> {
  try {
    return await apiClient.post("/customer/auth/forgot-password", data, { signal });
  } catch (error) {
    throw toUserFacingError(error, FALLBACK_MESSAGES.forgotPassword);
  }
}

// POST /customer/auth/reset-password
export async function resetPassword(
  data: ResetPasswordSchemaType,
  signal?: AbortSignal
): Promise<{ message: string }> {
  try {
    return await apiClient.post("/customer/auth/reset-password", data, { signal });
  } catch (error) {
    throw toUserFacingError(error, FALLBACK_MESSAGES.resetPassword);
  }
}
````

## File: backend/app/core/auth.py
````python
from fastapi import Depends, HTTPException, Request, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.database.session import get_db
from app.models.user import User
from app.core.jwt import verify_access_token

security = HTTPBearer(auto_error=False)
security_optional = HTTPBearer(auto_error=False)


async def _get_current_user_by_token(token: str, db: AsyncSession) -> User:
    payload = verify_access_token(token)

    user_id = payload.get("sub")
    if user_id is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token"
        )

    stmt = (
        select(User)
        .options(selectinload(User.role), selectinload(User.customer_profile))
        .where(User.id == int(user_id))
    )
    result = await db.execute(stmt)
    user = result.scalar_one_or_none()

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found"
        )

    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Inactive user"
        )

    return user


def _extract_token(
    request: Request,
    credentials: HTTPAuthorizationCredentials | None,
) -> str | None:
    # Cookie takes priority (browser session flow), header is the fallback
    # (useful for tests / non-browser clients / Swagger "Authorize").
    cookie_token = request.cookies.get("access_token")
    if cookie_token:
        return cookie_token
    if credentials:
        return credentials.credentials
    return None


async def get_current_user(
    request: Request,
    credentials: HTTPAuthorizationCredentials | None = Depends(security),
    db: AsyncSession = Depends(get_db),
) -> User:
    token = _extract_token(request, credentials)
    if token is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated"
        )
    return await _get_current_user_by_token(token, db)


async def get_current_user_optional(
    request: Request,
    credentials: HTTPAuthorizationCredentials | None = Depends(security_optional),
    db: AsyncSession = Depends(get_db),
) -> User | None:
    token = _extract_token(request, credentials)
    if token is None:
        return None

    try:
        return await _get_current_user_by_token(token, db)
    except HTTPException:
        return None
````

## File: backend/app/models/__init__.py
````python
from .user import User
from .role import Role
from .permission import Permission
from .role_permission import RolePermission
from .product import Product
from .product_category import ProductCategory
from .category import Category
from .product_variant import ProductVariant
from .order import Order
from .order_item import OrderItem
from .cart import Cart
from .cart_item import CartItem
from .coupon import Coupon
from .customer_profile import CustomerProfile
from .address import Address
from .review import Review
from .wishlist import Wishlist
from app.models.payment import Payment
from .return_request import ReturnRequest
````

## File: backend/app/main.py
````python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import text
from app.seed import seed_database
import app.models
from app.database.session import engine, AsyncSessionLocal
from app.core.config import settings
from app.core.test_seed import ensure_bogus_data
from app.api.routes.users import router as users_router
from app.api.routes.roles import router as roles_router
from app.api.routes.permissions import router as permissions_router
from app.api.routes.role_permissions import router as role_permissions_router
from app.api.routes.categories import router as categories_router
from app.api.routes.products import router as products_router
from app.api.routes.product_categories import router as product_categories_router
from app.api.routes.product_variants import router as product_variants_router
from app.api.routes.orders import router as orders_router
from app.api.routes.order_items import router as order_items_router
from app.api.routes.auth import router as auth_router
from app.api.routes.customer_profiles import router as customer_router
from app.api.routes.cart import router as cart_router
from app.api.routes.reviews import router as reviews_router
from app.api.routes.payments import router as payments_router
from app.api.routes.customer_auth import router as customer_auth_router
from app.api.routes.checkout import router as checkout_router
from app.api.routes.wishlist import router as wishlist_router
from app.api.routes.customer_order import router as customer_order_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

ROUTERS = [
    (users_router, "Users"),
    (auth_router, "Auth-Admin"),
    (roles_router, "Roles"),
    (permissions_router, "Permissions"),
    (role_permissions_router, "Role Permissions"),
    (products_router, "Products"),
    (categories_router, "Categories"),
    (product_categories_router, "Product Categories"),
    (product_variants_router, "Product Variants"),
    (orders_router, "Orders-Admin"),
    (order_items_router, "Order Items"),
    (customer_auth_router, "Customer Auth"),
    (customer_router, "Customer Profile"),
    (cart_router, "Cart"),
    (reviews_router, "Reviews"),
    (payments_router, "Payments"),
    (checkout_router, "Checkout"),
    (wishlist_router, "Wishlist"),
    (customer_order_router, "Customer Orders"),
]

for router, tag in ROUTERS:
    app.include_router(router, tags=[tag])


@app.on_event("startup")
async def on_startup():
    if settings.TEST_MODE:
        async with AsyncSessionLocal() as db:
            await ensure_bogus_data(db)
        print("TEST_MODE is ON — bogus product/variant/coupon seeded (id 999001 / code TESTCODE10)")


print("Database URL:", settings.DATABASE_URL)
print("Algorithm:", settings.ALGORITHM)
print("Access Token Expiry:", settings.ACCESS_TOKEN_EXPIRE_MINUTES)
````
