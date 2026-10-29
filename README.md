# InnerJouney — phone testing preview

GitHub Pages package prepared for **RaeZhang8023/innerjouney**.

Expected URL after publication: https://raezhang8023.github.io/innerjouney/

This address is not live until the repository is created, these files are pushed, and GitHub Pages is enabled.

## Publish

1. Create a public repository named `innerjouney` under `RaeZhang8023`.
2. Upload/push the contents of this folder to its `main` branch.
3. In the repository, open **Settings → Pages**, and choose **GitHub Actions** as the source.
4. In **Actions → Publish InnerJouney**, run the workflow if it has not already started.
5. Open the URL shown by the successful deployment.

Alternatively, in Settings → Pages, choose **Deploy from a branch**, branch `main`, folder `/docs`. The included `.nojekyll` file preserves Expo's underscore-prefixed asset folder.

## Data and features

No personal diary entries or account credentials are included. The app begins with an empty diary. Every tester's entries stay in that tester's browser storage. No shared diary database or server login is configured. Clearing browser storage can remove entries; use sample data for testing.

This is the browser version of the mobile app. Native dictation requires a custom phone build. Spotify stores track links, and print delivery has no connected provider.

The public repository contains the compiled browser app and original artwork; it does not expose testers' browser-local data. Browser storage is not a secure backup or recovery service.

## Files

- `docs/`: ready-to-serve static web build with all font/image/audio assets.
- `.github/workflows/pages.yml`: deploys `docs/` to GitHub Pages.
- `scripts/prepare-pages.py`: records how this package was derived from the sibling `phone-preview/dist` build. It is not required for deployment or use.

All assets use `/innerjouney/` as the base path. If you rename the repository, regenerate or update those paths before publishing.
